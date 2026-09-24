# Exercício de IA — Geral: especifique e retrotraduza

**Para quem não escreve código.** Este exercício não usa terminal nem execução de teste. Tudo o que ele pede acontece numa conversa com o agente, em interface de chat, e a verificação é feita por retrotradução e por conferência manual de casos.

## Regra de desconto em vigor

A Vetor calcula desconto por faixa de valor do pedido, com um teto por pedido:

| Valor do pedido | Desconto |
|---|---|
| Até R$ 500,00 | Nenhum |
| Acima de R$ 500,00 até R$ 2.000,00 | 5% |
| Acima de R$ 2.000,00 até R$ 5.000,00 | 10% |
| Acima de R$ 5.000,00 | 15% |

Sobre qualquer faixa incide um teto de R$ 1.000,00 de desconto por pedido. O sistema registra o tipo de cliente, padrão ou atacado, e nenhuma regra em vigor usa essa informação.

## O pedido

> "Quero um desconto de lançamento pra atrair cliente novo: primeiro pedido dele, se for baixinho, ganha um desconto a mais."

## Passo 1 — perguntas

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de redigir a especificação, aplicando a disciplina da [intervenção socrática](intervencao-socratica-conceitos.md): uma pergunta de cada vez, sem a resposta embutida na formulação.

## Passo 2 — respostas

??? note "Respostas de quem pediu — abra só depois do passo 1"
    - O que conta como "primeiro pedido"? Cliente sem nenhum pedido aprovado antes, e vale para cliente padrão e atacado, sem distinção de tipo.
    - O que conta como "baixinho"? Valor do pedido menor que R$ 1.000,00. Pedidos grandes de cliente novo não se qualificam.
    - Quanto é o desconto a mais? 3 pontos percentuais, somados à faixa normal.
    - O teto de R$ 1.000,00 continua valendo? Sim, sempre.

## Passo 3 — especifique

Escreva a regra de negócio e o requisito funcional, separados, no formato do [Exemplo de aplicação de IA](decomposicao-de-requisitos-exemplo-de-aplicacao-de-ia.md). A regra de negócio declara o que vale no negócio, sem mencionar tela nem sistema; o requisito funcional declara o que o sistema faz para cumpri-la.

## Passo 4 — retrotraduza

Abra uma conversa nova, sem histórico. Cole apenas a regra e o requisito que você escreveu, sem o pedido original e sem as respostas do passo 2, e peça: "descreva em prosa o comportamento que estas regras produzem, sem sugerir melhoria e sem corrigir nada". Compare a descrição devolvida com a intenção que você tinha ao escrever. Toda diferença é ambiguidade que sobreviveu à sua especificação.

## Passo 5 — confira os quatro casos

Preencha a coluna de desconto esperado à mão, usando apenas a regra em vigor e a especificação que você escreveu, antes de consultar o agente. Depois peça ao agente o mesmo cálculo a partir da sua especificação, e compare linha a linha.

| # | Valor do pedido | Tipo de cliente | Primeiro pedido? | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 800,00 | padrão | sim | |
| 2 | R$ 1.500,00 | padrão | sim | |
| 3 | R$ 800,00 | atacado | sim | |
| 4 | R$ 400,00 | padrão | não | |

??? note "Gabarito — abra só depois de preencher a tabela à mão"
    1. R$ 64,00. Faixa de 5% somada aos 3 pontos percentuais do bônus, o que dá 8%.
    2. R$ 75,00. Faixa de 5% sem bônus, porque R$ 1.500,00 não é considerado valor baixo.
    3. R$ 64,00. O bônus não distingue tipo de cliente, e o resultado é igual ao do caso 1.
    4. R$ 0,00. Faixa de 0% e sem bônus, porque não é o primeiro pedido do cliente.

**Observe:** o caso 2, de valor grande, e o caso 4, que não é primeiro pedido, são os dois que provam que o bônus tem fronteira, em vez de nunca se aplicar. Se qualquer um dos dois falhar na sua conferência manual, releia sua especificação em busca da frase que deixou essa fronteira implícita.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Perguntas antes da resposta | 20% | As perguntas do passo 1 foram escritas e preservadas antes de abrir o bloco de respostas |
| Especificação no padrão BR/FR | 40% | A regra de negócio e o requisito funcional estão separados, com valores concretos, não uma frase genérica |
| Retrotradução executada e divergência registrada | 40% | A conversa nova foi conduzida, e o resultado traz a divergência encontrada ou a afirmação explícita de que não houve nenhuma |

**Próxima página:** [Exercício de IA — Especialista](decomposicao-de-requisitos-exercicio-especialista.md).
