# Oficina de ferramentas — do pedido vago à especificação testada

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Codex CLI ou Gemini CLI), o git e o Node.js 20 ou superior. Tempo estimado: 30 minutos.

Todos os experimentos rodam sobre o projeto de exemplo da Vetor, para que cada pessoa parta do mesmo estado. Antes de começar, clone o repositório e confirme que os testes passam:

```bash
git clone https://github.com/arkhibr/workshops-ia-agentica.git
cd workshops-ia-agentica/exemplo/vetor
node --version   # precisa mostrar v20 ou superior
node --test       # deve terminar com 6 testes passando
```

**Decisão em foco:** transformar um pedido vago numa especificação BR/FR/NFR verificável, antes de acionar o agente para implementar.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, o ciclo completo do pedido à especificação testada.
- **Extensão para quem terminar antes:** Experimento B, sobre requisito não funcional.

## Experimento A — feche um pedido vago com especificação

**Objetivo:** conduzir o ciclo explorar → perguntar → propor → especificar sobre um pedido novo da Vetor, e comprovar que a especificação escrita é o que o agente de fato implementa.

**Antes de começar: por que a ordem importa.** O bloco de respostas abaixo simula quem pediu a mudança. Ele só cumpre a função de mostrar o efeito das perguntas se você escrever suas próprias perguntas antes de abri-lo. Abrir antes esvazia o experimento.

**Passo 1 — o pedido.** É este, e nada além disso:

> "Dá pra dar um desconto extra pros clientes que compram muito com a gente?"

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de especificar qualquer coisa. Use o repertório de [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) como referência.

**Passo 2 — as respostas.** Abra o bloco e compare com as perguntas que você escreveu.

??? note "Respostas de quem pediu — abra só depois de escrever suas próprias perguntas"
    - O que conta como "compra muito"? Cliente do tipo atacado com mais de 5 pedidos aprovados nos últimos 12 meses.
    - Esse desconto extra é cumulativo com a faixa normal, ou substitui? Cumulativo: soma-se à faixa normal, em pontos percentuais.
    - O desconto extra é de quantos pontos percentuais? 5 pontos percentuais.
    - O teto de R$ 1.000,00 por pedido continua valendo com o desconto extra somado? Sim, sempre — nenhuma regra nova revoga o teto.
    - Esse desconto vale para cliente padrão também? Não, só para atacado.

**Passo 3 — proponha e especifique.** Escreva a proposta em três frases, depois a especificação em BR/FR, seguindo o formato de [Exemplo arquitetural](exemplo-arquitetural.md). `calcularDesconto` vai precisar de um terceiro parâmetro, `pedidosAprovados`, opcional, com valor padrão que preserve o comportamento dos seis testes já existentes.

**Passo 4 — peça a implementação.** Cole sua especificação para o agente e peça a implementação, com testes, dentro de `exemplo/vetor`.

**Passo 5 — rode os casos abaixo contra o resultado.**

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 3.000,00 | atacado | 2 | R$ 300,00 (10%, não elegível ao adicional) |
| 2 | R$ 3.000,00 | atacado | 6 | R$ 450,00 (10% + 5% = 15%) |
| 3 | R$ 6.000,00 | atacado | 6 | R$ 1.000,00 (15% + 5% = 20% de R$ 6.000,00 seria R$ 1.200,00, mas o teto prevalece) |
| 4 | R$ 3.000,00 | padrão | 6 | R$ 300,00 (o adicional não vale para cliente padrão) |

Rode `node --test` e confira também que os seis testes originais continuam passando.

**Observe:** o caso 3 é o único em que a faixa normal, o adicional de recorrência e o teto se cruzam ao mesmo tempo. Se ele falhar, é sinal de que a especificação não deixou claro que o teto se aplica depois de somar os dois percentuais, não antes.

**Questões exploratórias:**

- Alguma das suas perguntas do passo 1 não apareceu entre as respostas do passo 2? O que você teria feito sem essa resposta?
- Se você tivesse pedido direto ao agente "dá pra dar um desconto extra pros clientes que compram muito", sem o ciclo completo, qual das quatro respostas do passo 2 ele teria decidido sozinho?

## Experimento B — especifique um requisito não funcional

**Objetivo:** escrever um NFR verificável para a mesma função, e reconhecer a diferença entre um NFR real e uma frase de intenção.

**Execute:** a Vetor pede que `calcularDesconto` "continue rápida mesmo com muito tráfego". Escreva um NFR que substitua essa frase por um critério mensurável — precisa ter um número e uma condição de medição, não um adjetivo. Peça ao agente uma forma simples de medir o tempo de execução da função em Node (por exemplo, `console.time`/`console.timeEnd` ao redor de mil chamadas) e rode.

**Questões exploratórias:**

- O NFR que você escreveu seria o mesmo se a função fosse chamada uma vez por pedido, ou mil vezes por segundo no checkout? O número muda com a escala esperada de uso?
- Que diferença prática existe entre "a função deve ser rápida" e o NFR que você escreveu, além do número?

## Evidência a entregar

Três itens, verificáveis contra o mesmo projeto de exemplo:

1. As perguntas do passo 1 do Experimento A, escritas antes de abrir as respostas.
2. A especificação BR/FR escrita no passo 3, e o resultado de `node --test` no passo 5 — os seis testes originais e os casos novos.
3. O NFR reescrito do Experimento B, com o número e a condição de medição.

**Próxima página:** [Exercícios](exercicios.md).
