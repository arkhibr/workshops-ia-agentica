# Estudo de caso: a linha que ninguém viu sobrepor

Discussão em grupo, sem resposta certa preparada. O objetivo é o grupo chegar a um critério, não a uma opinião, sobre quem responde quando uma tabela de decisão sem política de acerto declarada produz um resultado que ninguém decidiu conscientemente.

## O incidente

Depois da Sessão 3, a Vetor tinha duas regras de desconto especificadas em BR/FR: a faixa por valor e tipo de cliente (já formalizada em tabela na demonstração desta sessão) e o adicional de 5 pontos percentuais para cliente atacado recorrente. Alguém do time formalizou as duas juntas, rápido, sem revisão:

| Valor do Pedido | Tipo de Cliente | Pedidos Aprovados | Desconto |
|---|---|---|---|
| > R$ 10.000,00 | atacado | qualquer | 20% |
| qualquer | atacado | > 5 | faixa normal + 5% |
| ≤ R$ 500,00 | qualquer | qualquer | 0% |
| ... | ... | ... | ... |

Um pedido de R$ 12.000,00, de um cliente atacado com 8 pedidos aprovados, combina com a primeira linha (valor acima de R$ 10.000,00, atacado) e também com a segunda (atacado, mais de 5 pedidos aprovados). Ninguém declarou o que fazer quando as duas se aplicam ao mesmo tempo.

O agente que implementou a tabela tratou as linhas como uma cadeia de `if/else` — a primeira que combinasse "ganhava", como First implícito, embora ninguém tivesse pedido First. O pedido recebeu 20% de desconto, não 25% (20% da faixa mais 5% de recorrência). Três semanas depois, um vendedor recebeu a reclamação de um cliente atacado de longa data: "o desconto de cliente fiel que vocês prometeram não apareceu no meu último pedido, que foi grande."

## Onde a formalização estava, e não estava, errada

A tabela, linha por linha, estava correta: cada linha isolada descrevia exatamente a regra que a Sessão 3 tinha especificado. O problema não é nenhuma linha errada — é a ausência de uma decisão sobre o que fazer quando duas linhas se aplicam ao mesmo caso. Essa decisão não é um detalhe técnico de quem implementa a tabela; é uma regra de negócio que ninguém escreveu: os dois descontos se somam, ou o maior prevalece?

## Perguntas para orientar a discussão

- A falha está na tabela, na especificação BR/FR que a originou, ou em nenhuma das duas — é uma pergunta que só aparece quando duas regras específicas colidem, e nenhum processo de especificação prevê toda colisão possível?
- Se a tabela tivesse declarado explicitamente uma política de acerto — Unique, First, Priority ou Collect — antes de a implementação começar, esse incidente teria acontecido do mesmo jeito? Qual política, se qualquer uma tivesse sido escolhida sem pensar, ainda produziria o resultado errado?
- Quem deveria ter percebido a sobreposição entre as duas linhas: quem escreveu a segunda regra (cliente recorrente), sem revisar a tabela já existente, ou quem revisou a tabela depois de as duas regras estarem juntas? Existe uma etapa do processo, nesta sessão ou na Sessão 3, que deveria ter pego isso?
- O agente decidiu, sozinho, tratar a tabela como First. Isso é um erro do agente, ou é exatamente o comportamento esperado quando ninguém formaliza uma política de acerto — o agente preencheu uma lacuna que era responsabilidade de alguém preencher antes?

!!! question "Antes de continuar"
    Sem consultar o restante do grupo, escreva sua posição em uma frase: toda tabela de decisão com mais de uma dimensão de condição deveria, por padrão, ter a política de acerto revisada por uma segunda pessoa antes de ir para implementação? Ou isso sobrecarregaria regras que nunca colidiriam de verdade?

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
