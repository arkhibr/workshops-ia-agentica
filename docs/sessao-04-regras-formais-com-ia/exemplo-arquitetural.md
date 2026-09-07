# Exemplo arquitetural: a regra de desconto formalizada

Este exemplo é uma demonstração conduzida pelo instrutor, não um exercício. O objetivo é ver a regra de desconto da Vetor, já especificada em BR/FR na Sessão 3, virar vocabulário SBVR, sentenças RuleSpeak e uma tabela de decisão DMN.

**A Vetor**, usada como caso em toda esta sessão, tem hoje a regra de desconto com faixas de valor, um teto de R$ 1.000,00 e uma faixa de 20% para clientes atacado acima de R$ 10.000,00 — toda ela em prosa e em código, nunca em vocabulário controlado.

## Vocabulário SBVR

| Termo | O que significa |
|---|---|
| Pedido | Uma solicitação de compra na Vetor, com um Valor Total e um Cliente associado |
| Cliente | Quem faz o Pedido; tem um Tipo (padrão ou atacado) |
| Faixa de Desconto | Percentual aplicável ao Valor Total, determinado pelo intervalo em que ele se encaixa |
| Teto de Desconto | Valor máximo, em reais, que o Desconto de um Pedido pode atingir |

## Regras: estrutural e operativa

**Regra estrutural.** É necessário que todo Pedido tenha exatamente um Cliente associado, e que esse Cliente tenha exatamente um Tipo.

**Regras operativas**, no vocabulário do RuleSpeak:

- O Desconto de um Pedido **must** ser calculado pela Faixa de Desconto correspondente ao Valor Total.
- O Desconto de um Pedido **must not** exceder o Teto de Desconto de R$ 1.000,00.
- Um Pedido **may** receber a Faixa de Desconto de 20% **only if** o Cliente for do Tipo atacado e o Valor Total for maior que R$ 10.000,00.

## Tabela de decisão DMN

| Valor do Pedido | Tipo de Cliente | Desconto |
|---|---|---|
| ≤ R$ 500,00 | qualquer | 0% |
| R$ 500,01 a R$ 2.000,00 | qualquer | 5% |
| R$ 2.000,01 a R$ 5.000,00 | qualquer | 10% |
| > R$ 5.000,00 e ≤ R$ 10.000,00 | qualquer | 15% |
| > R$ 10.000,00 | atacado | 20% |
| > R$ 10.000,00 | padrão | 15% |

**Política de acerto: Unique.** Nenhuma combinação real de Valor do Pedido e Tipo de Cliente aparece em mais de uma linha — as faixas de valor são mutuamente exclusivas, e as duas últimas linhas se distinguem pelo Tipo. Isso é o que permite declarar Unique em vez de First: a ordem das linhas não importa para o resultado.

## Verificação por retrotradução

Peça a alguém (ou ao próprio agente, numa conversa nova) para reescrever a tabela de volta em prosa, sem ver a especificação original:

> "Pedidos até R$ 500 não têm desconto; de R$ 500,01 a R$ 2.000 têm 5%; de R$ 2.000,01 a R$ 5.000 têm 10%; acima de R$ 5.000 até R$ 10.000 têm 15%; acima de R$ 10.000, cliente atacado tem 20% e cliente padrão continua com 15%."

Essa retrotradução bate com a regra original — nenhum escopo foi ampliado, nenhuma condição foi perdida. Se a retrotradução tivesse dito "todo pedido acima de R$ 10.000 tem 20%", sem mencionar o tipo de cliente, isso teria exposto uma generalização indevida antes de o erro chegar a produção.

## Leitura do exemplo

A regra não mudou de significado ao longo do processo — mudou de forma. Prosa, BR/FR, vocabulário, sentença RuleSpeak, tabela de decisão: cada forma é mais estruturada que a anterior, e cada uma facilita um tipo diferente de verificação. A prosa é fácil de escrever e difícil de verificar; a tabela é mais trabalhosa de montar e quase impossível de deixar uma combinação de fora sem que isso apareça como uma linha ausente.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
