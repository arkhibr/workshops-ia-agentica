# Exercício de IA — Especialista: formalize, verifique, resolva a sobreposição

**Para quem implementa em código.** Este é o exercício-âncora da sessão: formalizar uma regra ainda em prosa, verificar por retrotradução numa conversa separada, e resolver uma sobreposição real entre duas regras com um cálculo numérico, não só uma política nomeada.

## Situação

A regra de cliente recorrente, em prosa: "cliente atacado com mais de 5 pedidos aprovados recebe 5 pontos percentuais adicionais de desconto, somados à faixa normal, respeitando sempre o teto de R$ 1.000,00." A Vetor também já tem, do exercício de vocabulário e sentenças, a regra de lançamento: "primeiro pedido de qualquer cliente, se o valor for menor que R$ 1.000,00, recebe 3 pontos percentuais adicionais, somados à faixa normal."

## Passo 1 — formalize

Peça ao agente o vocabulário mínimo com sinônimos a evitar, a sentença RuleSpeak numerada (`RN-` para a regra operativa, `RD-` se você identificar uma regra de classificação escondida nela — "Cliente Recorrente" é ou não é um conceito que merece nome próprio aqui?), com evidência e confiança, e a linha de tabela de decisão para a regra de cliente recorrente.

## Passo 2 — retrotraduza, numa conversa nova

Abra uma conversa nova com o agente, sem colar o resultado do passo 1, e cole só a sentença RuleSpeak e a linha de tabela que ele gerou. Peça: "reescreva esta regra formal em prosa comum, como se explicasse para alguém que nunca viu a versão técnica."

## Passo 3 — compare

A retrotradução do passo 2 preservou que o adicional é exclusivo de cliente atacado, que exige mais de 5 pedidos aprovados, e que é aditivo (soma-se à faixa, não substitui)? Marque qual dos três, se algum, se perdeu ou mudou de escopo.

## Passo 4 — resolva a sobreposição

Um pedido de R$ 800,00, de um cliente atacado com 6 pedidos aprovados que também seja o primeiro pedido dele, combina com a regra de cliente recorrente **e** com a regra de lançamento ao mesmo tempo. Declare a política de acerto (Unique, Priority ou Collect) para esse caso e calcule o desconto resultante segundo a política escolhida.

**Entrega esperada**

A formalização do passo 1, a retrotradução do passo 2, a comparação do passo 3, e a política de acerto com o cálculo do passo 4.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Formalização completa | 30% | Vocabulário com sinônimos, sentença RuleSpeak na forma correta, numeração `RN-`/`RD-` com evidência e confiança, e linha de tabela, todos presentes |
| Retrotradução numa conversa separada | 30% | Pedida sem o contexto original, com a comparação apontando com precisão o que preservou ou mudou |
| Política de acerto justificada | 40% | A política escolhida resolve o caso de sobreposição do passo 4 com um cálculo numérico explícito, não só uma escolha nomeada |

**Como verificar antes de entregar:** confira se o cálculo do passo 4 usa a política que você declarou. É comum declarar Collect e depois calcular como se fosse Priority, por hábito de escolher "a maior regra vence".

## Extensão para quem terminar antes: a regra composta com teto próprio

A Vetor quer lançar uma quarta regra: cliente atacado que é, ao mesmo tempo, recorrente e está fazendo um pedido de lançamento (primeiro pedido de uma nova linha de produto, valor menor que R$ 1.000,00) recebe os três adicionais somados (recorrência, lançamento e a faixa base), mas o total nunca ultrapassa 30 pontos percentuais, mesmo que a soma das três regras ultrapasse isso. Formalize essa regra completa: vocabulário com sinônimos a evitar, a regra de derivação do limite de 30 pontos percentuais (separada, numerada `RD-`, das três regras operativas que ela limita), as sentenças RuleSpeak necessárias (numeradas `RN-`, cada uma com evidência e confiança) e a linha de tabela de decisão.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
