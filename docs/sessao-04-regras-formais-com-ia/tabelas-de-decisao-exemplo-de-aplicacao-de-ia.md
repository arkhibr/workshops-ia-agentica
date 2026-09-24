# Exemplo de aplicação de IA: tabela de decisão e o incidente da sobreposição

Esta é uma demonstração conduzida pelo instrutor, continuação do exemplo de vocabulário e sentenças. O objetivo é ver as sentenças RuleSpeak da Vetor virarem uma tabela de decisão DMN completa, verificada por retrotradução, e depois examinar um incidente real em que a ausência de política de acerto produziu um resultado que ninguém decidiu conscientemente.

## Tabela de decisão DMN

A partir das sentenças RN-001 a RN-004 do exemplo anterior, a tabela completa:

| Valor do Pedido | Tipo de Cliente | Cliente Recorrente? | Desconto |
|---|---|---|---|
| ≤ R$ 500,00 | qualquer | não | 0% |
| R$ 500,01 a R$ 2.000,00 | qualquer | não | 5% |
| R$ 2.000,01 a R$ 5.000,00 | qualquer | não | 10% |
| > R$ 5.000,00 e ≤ R$ 10.000,00 | qualquer | não | 15% |
| > R$ 10.000,00 | atacado | não | 20% |
| > R$ 10.000,00 | padrão | não | 15% |
| qualquer | atacado | sim | faixa correspondente + 5 pontos percentuais |
| qualquer | padrão | sim | — |

A última linha usa "—", não "0%": cliente padrão nunca é classificado como Cliente Recorrente pela regra RD-001, então essa combinação não deveria existir nos dados. Se ela aparecer em produção, o problema não é a tabela, é algum outro ponto do sistema que deixou um cliente padrão ser marcado como recorrente.

**Política de acerto: Priority.** As duas últimas linhas se sobrepõem às seis primeiras sempre que "Cliente Recorrente" for verdadeiro, e por isso a tabela não pode ser Unique. A prioridade declarada: se Cliente Recorrente for verdadeiro, essa linha vence sobre a linha correspondente de valor e tipo, e o resultado soma o adicional à faixa que seria aplicada de outro modo.

Peça a retrotradução da tabela, numa conversa nova, sem contexto:

> "Pedidos até R$ 500 não têm desconto; de R$ 500,01 a R$ 2.000 têm 5%; de R$ 2.000,01 a R$ 5.000 têm 10%; acima de R$ 5.000 até R$ 10.000 têm 15%; acima de R$ 10.000, cliente atacado tem 20% e cliente padrão continua com 15%. Se o cliente for atacado e recorrente, soma-se mais 5 pontos percentuais à faixa que já valeria, respeitando o teto."

Essa retrotradução bate com a regra original: nenhum escopo foi ampliado, nenhuma condição foi perdida, e a composição (soma sobre a faixa já aplicável) ficou explícita.

## O incidente: a linha que ninguém viu sobrepor

Depois da Sessão 3, a Vetor tinha duas regras de desconto especificadas em BR/FR: a faixa por valor e tipo de cliente (a tabela acima) e o adicional de recorrência. Alguém do time formalizou as duas juntas, rápido, sem revisão:

| Valor do Pedido | Tipo de Cliente | Pedidos Aprovados | Desconto |
|---|---|---|---|
| > R$ 10.000,00 | atacado | qualquer | 20% |
| qualquer | atacado | > 5 | faixa normal + 5% |
| ≤ R$ 500,00 | qualquer | qualquer | 0% |

Um pedido de R$ 12.000,00, de um cliente atacado com 8 pedidos aprovados, combina com a primeira linha (valor acima de R$ 10.000,00, atacado) e também com a segunda (atacado, mais de 5 pedidos aprovados). Ninguém declarou o que fazer quando as duas se aplicam ao mesmo tempo.

O agente que implementou a tabela tratou as linhas como uma cadeia de `if/else`: a primeira que combinasse "ganhava", como First implícito, embora ninguém tivesse pedido First. O pedido recebeu 20% de desconto, não 25% (20% da faixa mais 5% de recorrência). Três semanas depois, um vendedor recebeu a reclamação de um cliente atacado de longa data: "o desconto de cliente fiel que vocês prometeram não apareceu no meu último pedido, que foi grande."

A tabela, linha por linha, estava correta: cada linha isolada descrevia exatamente a regra que a Sessão 3 tinha especificado. O problema não é nenhuma linha errada, é a ausência de uma decisão sobre o que fazer quando duas linhas se aplicam ao mesmo caso. Essa decisão não é detalhe técnico de quem implementa a tabela — é uma regra de negócio que ninguém escreveu: os dois descontos se somam, ou o maior prevalece?

!!! question "Antes de continuar"
    O agente decidiu, sozinho, tratar a tabela como First. Isso é um erro do agente, ou é exatamente o comportamento esperado quando ninguém formaliza uma política de acerto — o agente preencheu uma lacuna que era responsabilidade de alguém preencher antes?

**Próxima página:** [Exercício de IA — Geral](tabelas-de-decisao-exercicio-geral.md).
