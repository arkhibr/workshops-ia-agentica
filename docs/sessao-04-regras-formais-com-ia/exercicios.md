# Exercícios

Tente responder antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Situação compartilhada

Todos os exercícios desta página se referem às regras de desconto da Vetor especificadas em BR/FR na Sessão 3: a faixa por valor e tipo de cliente, o adicional de cliente recorrente (atacado, mais de 5 pedidos aprovados, +5 pontos percentuais) e o desconto de lançamento (primeiro pedido, valor menor que R$ 1.000,00, +3 pontos percentuais, qualquer tipo de cliente). O teto de R$ 1.000,00 por pedido vale para todas as combinações.

## Recordar

### 1. As duas categorias de regra

Nomeie as duas categorias de regra que o SBVR distingue, e o tipo de operador modal que cada uma usa.

<details>
<summary>Ver resposta</summary>

Regra estrutural (ou definicional), com operadores aléticos ("necessário", "possível"); regra operativa (ou comportamental), com operadores deônticos ("obrigatório", "permitido"). A regra estrutural se divide em duas formas concretas: classificação (nomeia um subtipo a partir de uma condição) e derivação (explica de onde vem um valor calculado).
</details>

### 2. As três formas do RuleSpeak

Nomeie as três formas de sentença do RuleSpeak que contam como regra de negócio.

<details>
<summary>Ver resposta</summary>

"Must" (exigência), "must not" (proibição) e "may ... only" (permissão condicional).
</details>

## Compreender

### 3. Estrutural ou operativa?

"Todo Cliente da Vetor tem exatamente um Tipo, padrão ou atacado." Essa regra é estrutural ou operativa? Justifique pelo teste de violação.

<details>
<summary>Ver resposta</summary>

Estrutural: ninguém "viola" essa regra fazendo uma escolha errada — ela define o que um Cliente é, não rege uma conduta que poderia ter sido diferente.
</details>

### 4. Classificação ou derivação?

"O Desconto de um Pedido é o Valor Total vezes o percentual da Faixa correspondente." Essa regra é de classificação ou de derivação? E "Um Cliente com mais de 5 pedidos aprovados é um Cliente Recorrente" — classificação ou derivação?

<details>
<summary>Ver resposta</summary>

A primeira é derivação: explica de onde vem um valor calculado. A segunda é classificação: nomeia um subtipo a partir de uma condição, sem calcular nenhum valor novo.
</details>

### 5. Política de acerto

Uma tabela de decisão tem duas linhas: "Valor > R$ 10.000,00 e Tipo = atacado → 20%" e "Tipo = atacado e Pedidos Aprovados > 5 → faixa normal + 5%". Um pedido de R$ 12.000,00 de cliente atacado com 8 pedidos aprovados combina com as duas. Se a política declarada for Collect com agregação de soma, qual o desconto resultante?

<details>
<summary>Ver resposta</summary>

25% (20% + 5%), respeitando o teto de R$ 1.000,00 se o valor calculado ultrapassá-lo.
</details>

## Aplicar

### 6. Exercício-âncora: formalize, verifique, resolva a sobreposição

**O que é:** o mesmo ciclo do Experimento A da oficina, aplicado à regra de cliente recorrente, seguido da resolução da sobreposição que o Experimento B da oficina apenas identificou.

**Antes de começar: por que a ordem importa.** A retrotradução do passo 2 só prova alguma coisa se acontecer numa conversa que não viu a formalização do passo 1.

**Situação**

A regra de cliente recorrente, em prosa: "cliente atacado com mais de 5 pedidos aprovados recebe 5 pontos percentuais adicionais de desconto, somados à faixa normal, respeitando sempre o teto de R$ 1.000,00."

**Seu papel**

Você formaliza essa regra e decide, sozinho, como ela se combina com a tabela base do [Exemplo arquitetural](exemplo-arquitetural.md) e com a regra de lançamento da oficina.

**Insumos disponíveis**

O agente que você já usa, e as três regras da situação compartilhada acima.

**Como conduzir**

1. **Formalize.** Peça ao agente o vocabulário mínimo com sinônimos a evitar, a sentença RuleSpeak numerada (`RN-` para a regra operativa, `RD-` se você identificar uma regra de classificação escondida nela — "Cliente Recorrente" é ou não é um conceito que merece nome próprio aqui?), com evidência e confiança, e a linha de tabela de decisão.
2. **Retrotraduza, numa conversa nova.** Cole só a sentença e a linha de tabela geradas, sem o contexto original, e peça a reescrita em prosa comum.
3. **Compare.** A retrotradução preservou que o adicional é exclusivo de cliente atacado, que exige mais de 5 pedidos aprovados, e que é aditivo (soma-se à faixa, não substitui)?
4. **Resolva a sobreposição.** Um pedido de R$ 800,00, de um cliente atacado com 6 pedidos aprovados que também seja o primeiro pedido dele, combina com a regra de cliente recorrente **e** com a regra de lançamento ao mesmo tempo. Declare a política de acerto (Unique, Priority ou Collect) para esse caso e calcule o desconto resultante segundo a política escolhida.

**Entrega esperada**

A formalização do passo 1, a retrotradução do passo 2, a comparação do passo 3, e a política de acerto com o cálculo do passo 4.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Formalização completa | 30% | Vocabulário com sinônimos, sentença RuleSpeak na forma correta ("must", "must not" ou "may ... only"), numeração `RN-`/`RD-` com evidência e confiança, e linha de tabela, todos presentes |
| Retrotradução numa conversa separada | 30% | A retrotradução foi pedida sem o contexto original, e a comparação aponta com precisão o que preservou ou mudou |
| Política de acerto justificada | 40% | A política escolhida resolve o caso de sobreposição do passo 4 com um cálculo numérico explícito, não só uma escolha nomeada |

**Como verificar antes de entregar:** confira se o cálculo do passo 4 usa a política que você declarou — é comum declarar Collect e depois calcular como se fosse Priority, por hábito de escolher "a maior regra vence".

## Analisar

### 7. Duas regras, duas formas

Compare a sentença RuleSpeak da regra de cliente recorrente (exercício 6) com a da regra de lançamento (oficina). As duas usam a mesma forma ("must", "must not" ou "may ... only")? Se usam formas diferentes, o que na regra de negócio de cada uma explica a escolha?

## Avaliar

### 8. A tabela sem política

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: toda tabela de decisão da Vetor deveria ter revisão obrigatória de sobreposição antes de qualquer implementação, mesmo quando o time está confiante de que as linhas não se cruzam? Justifique com o critério de quantas regras diferentes já incidem sobre o mesmo Pedido, não com preferência pessoal.

## Criar

### 9. Formalize a regra que ainda não existe

A Vetor quer lançar uma quarta regra: cliente atacado que é, ao mesmo tempo, recorrente (mais de 5 pedidos aprovados) e está fazendo um pedido de lançamento (primeiro pedido de uma nova linha de produto, valor menor que R$ 1.000,00) recebe os três adicionais somados (recorrência, lançamento e a faixa base), mas o total nunca ultrapassa 30 pontos percentuais, mesmo que a soma das três regras ultrapasse isso. Formalize essa regra completa: vocabulário com sinônimos a evitar, a regra de derivação do limite de 30 pontos percentuais (separada, numerada `RD-`, das três regras operativas que ela limita), as sentenças RuleSpeak necessárias (numeradas `RN-`, cada uma com evidência e confiança) e a linha de tabela de decisão.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
