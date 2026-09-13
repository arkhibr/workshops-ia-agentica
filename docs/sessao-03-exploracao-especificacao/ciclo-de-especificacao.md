# O ciclo de especificação

Entre o pedido vago e o código, existe um trabalho que a maioria dos times pula: transformar "ative o desconto de atacado" numa descrição que não deixa nada para o agente inventar sozinho. Quatro etapas fazem esse trabalho, e pular qualquer uma delas custa mais caro depois do que custaria antes.

## Explorar, perguntar, propor, especificar

Um pedido chega quase sempre incompleto. A cabeça de quem pediu já resolveu metade do problema sem perceber que resolveu. "Ative o desconto de atacado" pressupõe uma faixa de valor, um teto, uma data de início. Tudo isso existe na cabeça de quem escreveu a frase, e nada disso está escrito nela.

O ciclo tem quatro etapas, nessa ordem:

- **Explorar.** Antes de perguntar qualquer coisa, olhe o que já existe: código, teste, documentação, conversa anterior. Um parâmetro que a função já recebe e nunca usa, um campo que o banco já guarda e a tela não mostra. Isso é pista de intenção não implementada, e ainda não vale como requisito.
- **Perguntar.** Levante as perguntas cuja resposta muda o comportamento do sistema. A página seguinte trata só disso.
- **Propor.** Depois de reunir as respostas, escreva uma proposta curta — três ou quatro frases — e devolva para quem pediu, antes de especificar tudo em detalhe. É o ponto mais barato para descobrir que a proposta pegou o problema errado.
- **Especificar.** Só agora, com a proposta validada, escreva a especificação completa: regra de negócio (BR), requisito funcional (FR) e requisito não funcional (NFR), no padrão da próxima página.

!!! question "Antes de continuar"
    Pense no último pedido que você recebeu e resolveu sem perguntar nada. Quantas das quatro etapas você pulou, e qual delas, se tivesse acontecido, teria mudado o resultado?

## O custo de pular direto para o código

[Boehm](../referencia/bibliografia.md#boehm-software-engineering-economics-1981) documentou, décadas antes de qualquer LLM, que o custo de corrigir uma ambiguidade cresce a cada fase do desenvolvimento. A Sessão 1 já usou esse dado na escolha entre vibe coding, assistência e SDD. O ciclo de especificação aplica a mesma lógica dentro de uma única tarefa: a etapa de explorar e perguntar é a fase mais barata para corrigir uma ambiguidade, porque ainda não existe código escrito que dependa dela. Pular para a implementação empurra o mesmo custo para a fase em que corrigir já significa reescrever.

A pressa de "só implementar logo" tem uma armadilha específica com agentes de codificação: o agente não vai parar para perguntar, a menos que seja instruído a fazer isso. Ele completa a lacuna com a suposição mais provável estatisticamente, que para aquele negócio costuma ser a errada. O resultado compila, passa nos testes que já existiam, e resolve um problema ligeiramente diferente do que foi pedido. A Sessão 1 chamou esse padrão de piso alto e teto baixo.

## Quando o ciclo compensa e quando é exagero

Nem todo pedido precisa das quatro etapas por extenso. Um ajuste de uma linha, reversível, sem regra de negócio nova, resolve-se explorando e perguntando de cabeça, sem formalizar proposta nem especificação. O mesmo critério de [reversibilidade e tempo de vida](../sessao-01-o-que-mudou/modos-de-trabalho.md#quando-cada-modo-se-justifica) da Sessão 1 decide isso. O ciclo completo se paga quando a regra de negócio é nova, quando mais de uma pessoa vai manter o código depois, ou quando o pedido já revelou, na primeira leitura, mais de uma interpretação possível. "Ative o desconto de atacado" é desse tipo: não diz onde a faixa começa nem se o teto de R$ 1.000,00 continua valendo.

!!! tip "Aplique agora"
    Pegue um pedido real que está no seu backlog. Você consegue nomear pelo menos uma pergunta cuja resposta mudaria o código gerado? Se não conseguir nenhuma, o ciclo completo é exagero para esse caso. Assistência de codificação direta já resolve.

## Isso vira código assim

"Ative o desconto de atacado" chega como uma frase. O código que existe hoje na função de desconto não tem nenhuma noção de tipo de cliente:

```javascript
// src/desconto.js — antes do ciclo
export function calcularDesconto(valorTotal, tipoCliente) {
  let percentual = 0;
  if (valorTotal > 5000) {
    percentual = 0.15;
  } else if (valorTotal > 2000) {
    percentual = 0.1;
  } else if (valorTotal > 500) {
    percentual = 0.05;
  }
  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
```

A função já recebe `tipoCliente` como parâmetro e nunca o usa, exatamente o tipo de pista que a etapa **explorar** procura antes de perguntar qualquer coisa. As etapas seguintes produzem, nessa ordem: a pergunta ("a partir de que valor a faixa de atacado começa, e ela substitui ou soma à faixa por volume?"), a proposta curta ("atacado acima de R$ 10.000,00 recebe 20%, em vez da faixa por volume"), e só então a especificação com regra numerada:

```text
BR-01: Pedido de cliente atacado com valor acima de R$ 10.000,00
       recebe a faixa de 20%, substituindo a faixa por volume.
FR-01: calcularDesconto retorna 20% do valor total quando
       tipoCliente === 'atacado' e valorTotal > 10000.
```

Só com BR-01 e FR-01 escritos o código muda de forma segura:

```javascript
export function calcularDesconto(valorTotal, tipoCliente) {
  if (tipoCliente === 'atacado' && valorTotal > 10000) {
    return Math.min(valorTotal * 0.2, TETO_DESCONTO);
  }
  let percentual = 0;
  if (valorTotal > 5000) {
    percentual = 0.15;
  } else if (valorTotal > 2000) {
    percentual = 0.1;
  } else if (valorTotal > 500) {
    percentual = 0.05;
  }
  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
```

Sem o ciclo, um agente vendo só "ative o desconto de atacado" tinha três leituras plausíveis para o `if` acima: substituir a faixa, somar a ela, ou aplicar só acima de outro valor de corte. A regra numerada elimina as três dúvidas de uma vez, antes da primeira linha de código mudar.

**Próxima página:** [BR, FR e NFR](br-fr-nfr.md).
