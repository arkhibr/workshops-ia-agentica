# BR, FR e NFR

Uma especificação mal escrita esconde três perguntas diferentes: qual é a regra que o negócio impõe, o que o sistema precisa fazer, e sob que restrição de qualidade ele precisa fazer isso. Confundir as três produz uma especificação de aparência completa, com decisões de negócio ausentes do texto escrito.

## As três categorias

**Regra de negócio (BR, *business rule*)** é uma declaração sobre como o negócio funciona, independente de haver software ou não. [Ross](../referencia/bibliografia.md#ross-ed-business-rules-manifesto-2003), no *Business Rules Manifesto*, é categórico: "regras não são processo nem procedimento" e devem ser expressas de forma declarativa, sem sequenciamento implícito. Uma regra declara *o que vale* em qualquer momento, sem prescrever *em que ordem fazer*. "O desconto de um pedido nunca ultrapassa um teto fixo em reais" é uma regra de negócio: valeria mesmo que o cálculo fosse feito numa planilha, sem nenhum sistema.

**Requisito funcional (FR, *functional requirement*)** é o que o software precisa fazer para que a regra de negócio se cumpra. "O sistema calcula o desconto de um pedido a partir do valor total e do tipo de cliente" é funcional: descreve comportamento observável do sistema, não existe fora dele.

**Requisito não funcional (NFR, *non-functional requirement*)**, no vocabulário da norma [ISO/IEC/IEEE 29148](../referencia/bibliografia.md#isoiecieee-291482018), não descreve uma ação específica, mas um critério para julgar como o sistema executa a ação: desempenho, usabilidade, segurança. "O cálculo de desconto responde em menos de 100ms" é não funcional, porque o sistema já calcula desconto, e esse cálculo é o requisito funcional. O requisito não funcional acrescenta o limite de tempo sob o qual o cálculo precisa acontecer, que neste exemplo é de 100 milissegundos.

| Categoria | Pergunta que responde | Existiria sem o sistema? | Exemplo genérico |
|---|---|---|---|
| BR | O que o negócio permite, exige ou proíbe? | Sim | Desconto por volume nunca passa de um teto fixo |
| FR | O que o sistema precisa fazer? | Não | Calcular o desconto a partir de valor e tipo de cliente |
| NFR | Sob que critério de qualidade? | Não | Responder em menos de 100ms, sob qualquer carga |

## Efeito prático da distinção

[Wiegers e Beatty](../referencia/bibliografia.md#wiegers-e-beatty-software-requirements-2013) tratam regra de negócio como categoria anterior aos requisitos de software, em vez de um requisito em si. Uma regra de negócio também vale para operação manual, fora de qualquer sistema, e é dela que os requisitos funcionais derivam. Essa ordem importa para quem escreve um pedido a um agente, porque a regra de negócio é a fonte de verdade da qual o requisito funcional deriva como tradução em comportamento de sistema, e o requisito não funcional entra depois dos dois, como restrição de qualidade sobre esse comportamento.

Cada confusão entre as três categorias produz um sintoma reconhecível. Uma regra de negócio escrita como requisito funcional ("o sistema deve limitar o desconto a R$ 1.000,00") esconde que o limite é uma decisão de negócio, e não uma escolha de implementação. Se o negócio mudar o teto amanhã, ninguém vai procurar essa mudança na especificação funcional. Um requisito não funcional escrito como regra de negócio ("o sistema deve ser rápido") não diz nada verificável, porque "rápido" é uma medida de engenharia que só significa alguma coisa com um número junto.

!!! question "Antes de continuar"
    Releia a última especificação que você escreveu ou recebeu. Alguma frase que parecia requisito funcional era, na verdade, regra de negócio disfarçada, algo que valeria mesmo sem o sistema existir?

## Regra embutida em requisito funcional

O sintoma mais comum é uma frase única, funcional na forma, que carrega três regras de negócio dentro dela:

> "O sistema deve aplicar desconto de 20% para pedidos de atacado acima de R$ 10.000,00, respeitando o teto de R$ 1.000,00."

As três regras embutidas são a existência de uma faixa própria para o cliente de atacado, o valor de corte a partir do qual ela vale, e a prevalência do teto sobre qualquer faixa. Nenhuma delas tem linha própria, e por isso nenhuma delas tem identificador. Quando a gerência comercial decide baixar o corte para R$ 8.000,00, alguém precisa reabrir a especificação funcional inteira para localizar o número.

A versão separada da mesma especificação fica assim. O prefixo identifica a categoria, `BR` para regra de negócio e `FR` para requisito funcional, e o número serve para que outras linhas possam citar a regra sem repetir o conteúdo dela.

```text
BR-03: Cliente do tipo atacado tem faixa de desconto própria,
       distinta da faixa por volume.
BR-04: A faixa de atacado é de 20% e se aplica a pedido com valor
       total acima de R$ 10.000,00.
BR-05: O desconto de um pedido nunca ultrapassa R$ 1.000,00,
       qualquer que seja a faixa aplicada.

FR-03: calcularDesconto aplica a faixa definida em BR-04 quando o
       cliente é do tipo atacado e o valor total supera o corte
       dessa faixa, e limita o retorno ao teto de BR-05.
       Para valorTotal = 12000 e tipoCliente = 'atacado', o retorno
       é 1000, porque 20% de R$ 12.000,00 excede o teto.
```

Quatro linhas no lugar de uma, e cada uma responde por uma coisa só. Baixar o corte para R$ 8.000,00 altera apenas BR-04, e nem FR-03 nem as outras duas regras precisam ser reabertas. Criar uma faixa nova para outro tipo de cliente acrescenta uma BR, e BR-05 já vale para ela sem ser reescrita, porque o teto foi declarado como restrição geral e não como detalhe da faixa de atacado. FR-03 cita as regras em vez de repetir os números, de modo que nenhum valor aparece escrito em dois lugares.

Essa citação cruzada é o que um agente usa. Diante de um pedido para acrescentar uma faixa, um agente que recebeu a especificação separada trata BR-05 como restrição aplicável ao caso novo. Diante da frase única do início desta seção, o mesmo agente pode ler o teto como parte da regra de atacado e deixar a faixa nova sem limite.

A separação custa três linhas a mais na especificação, e se paga quando o número tem dono fora da equipe de desenvolvimento ou quando mais de uma faixa depende dele. Uma regra estável há anos, que ninguém de fora do time pode alterar, não precisa de linha própria.

## Para o time de negócio

Cada uma das três categorias é registrada em um artefato distinto fora do código, e confundi-las faz com
que uma decisão comercial seja registrada como detalhe técnico dentro de um item de backlog.

| Categoria | Onde ela vive | Quem aprova mudança | O que acontece se ela mudar |
|---|---|---|---|
| Regra de negócio | Política comercial escrita, numerada e datada | Área demandante | O número muda num lugar só, e todo item que a referencia continua válido |
| Requisito funcional | Item de backlog, com critério de aceitação | Produto, com a área demandante | O item é reescrito, e a regra permanece como está |
| Requisito não funcional | Acordo de nível de serviço do produto | Produto, com quem opera o sistema | A medida é renegociada, com prazo e responsável |

O teste que separa a regra de negócio do requisito funcional consiste em perguntar se a frase
continuaria verdadeira caso o trabalho fosse feito numa planilha, sem sistema nenhum. A frase "o
desconto de um pedido nunca ultrapassa R$ 1.000,00" continuaria verdadeira nessa situação, porque o
limite é decisão comercial. A frase "a tela de fechamento exibe o desconto aplicado antes da
confirmação" deixaria de fazer sentido, porque depende da existência da tela.

O antipadrão aparece quando a regra chega ao time embutida na descrição do item, sem número próprio.
A frase "o sistema deve aplicar desconto de 20% para atacado acima de R$ 10.000,00, respeitando o teto
de R$ 1.000,00" carrega três regras distintas, e nenhuma delas tem identificador. Quando a gerência
comercial decidir mudar o valor de corte, alguém vai precisar abrir os itens de backlog um a um para
descobrir onde o número está escrito.

## Para o time de desenvolvimento

As três categorias não param na especificação, e cada uma delas é verificada por um artefato diferente, sem que nenhuma descreva a estrutura interna do código que as satisfaz.

```text
BR-02:  O desconto de um pedido nunca ultrapassa R$ 1.000,00,
        qualquer que seja a faixa aplicada.
FR-02:  calcularDesconto nunca retorna desconto superior ao teto
        vigente. Para valorTotal = 100000 e tipoCliente = 'padrao',
        o retorno é 1000.
NFR-01: calcularDesconto processa 500 cálculos consecutivos em
        menos de 100ms.
```

BR-02 é a decisão de negócio, e valeria mesmo que o cálculo fosse feito numa planilha. FR-02 é o comportamento observável da função, escrito em termos de entrada e retorno, sem citar nenhuma construção da linguagem. NFR-01 é o critério de qualidade sob o qual esse comportamento acontece.

A implementação abaixo satisfaz FR-02, e não é a única que satisfaz:

```javascript
export const TETO_DESCONTO = 1000;

export function calcularDesconto(valorTotal, tipoCliente) {
  // ...
  return Math.min(valorTotal * percentual, TETO_DESCONTO); // satisfaz FR-02
}
```

Um `if` que compara o valor calculado com `TETO_DESCONTO` e atribui o menor produziria exatamente o mesmo retorno para todas as entradas, e FR-02 continuaria cumprido sem nenhuma alteração no texto. Essa independência é o que torna a separação útil: o requisito sobrevive à troca de implementação, à troca de linguagem e à reescrita da função. Um requisito escrito como "calcularDesconto aplica `Math.min` entre o valor calculado e o teto" perde essa propriedade, porque passa a ser violado por uma refatoração que não muda comportamento nenhum.

NFR-01 é verificado fora do corpo da função, por um teste que mede tempo em vez de comparar valor:

```javascript
// test/desconto.perf.test.js
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { calcularDesconto } from '../src/desconto.js';

test('NFR-01: 500 calculos consecutivos em menos de 100ms', () => {
  const inicio = performance.now();
  for (let i = 0; i < 500; i += 1) {
    calcularDesconto(12000, 'atacado');
  }
  const duracaoMs = performance.now() - inicio;
  assert.ok(duracaoMs < 100, `levou ${duracaoMs}ms`);
});
```

O teste mede 500 chamadas consecutivas, que é exatamente o que NFR-01 declara. Um requisito sobre chamadas concorrentes exigiria outro instrumento, com múltiplos processos ou medição no servidor, e um teste em laço sequencial não o verificaria. Escrever o requisito com a palavra que o teste não mede é um defeito comum, e produz um NFR que passa na esteira sem nunca ter sido verificado.

O lugar de verificação de cada categoria é distinto. A regra de negócio é conferida contra a política escrita de quem a definiu. O requisito funcional é conferido por caso de teste que compara entrada e retorno. O requisito não funcional é conferido por medição com limiar declarado. Um pedido como "o sistema deve ser rápido" não contém o limiar, a quantidade de amostras nem o critério de falha, que são os três dados de que o teste acima depende.

**Próxima página:** [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md).
