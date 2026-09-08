# Exemplo arquitetural: a regra de desconto formalizada

Este exemplo é uma demonstração conduzida pelo instrutor, não um exercício. O objetivo é ver a regra de desconto da Vetor, já especificada em BR/FR na Sessão 3, virar vocabulário SBVR, regra de classificação, regra de derivação, sentenças RuleSpeak numeradas e uma tabela de decisão DMN.

**A Vetor**, usada como caso em toda esta sessão, tem hoje a regra de desconto com faixas de valor, um teto de R$ 1.000,00, uma faixa de 20% para clientes atacado acima de R$ 10.000,00 e um adicional de 5 pontos percentuais para cliente atacado recorrente — toda ela em prosa e em código, `src/desconto.js`, nunca em vocabulário controlado.

## Vocabulário SBVR

| Termo | O que significa | Sinônimos a evitar |
|---|---|---|
| Pedido | Uma solicitação de compra na Vetor, com um Valor Total e um Cliente associado | "order", "compra" |
| Cliente | Quem faz o Pedido; tem um Tipo (padrão ou atacado) | "usuário", "conta" |
| Faixa de Desconto | Percentual aplicável ao Valor Total, determinado pelo intervalo em que ele se encaixa | "tier", "nível" |
| Teto de Desconto | Valor máximo, em reais, que o Desconto de um Pedido pode atingir | "limite", "cap" |
| Cliente Recorrente | Cliente atacado com mais de 5 pedidos aprovados nos últimos 12 meses | (conceito não nomeado no código hoje) |

A última linha é a mais importante: "Cliente Recorrente" nunca teve nome no código. Ele existe hoje como um `if (pedidosAprovados > 5)` solto, sem que o conceito por trás da condição tenha sido nomeado em lugar nenhum — é exatamente esse tipo de lacuna que a regra de classificação, a seguir, torna explícita.

## Regras de classificação e derivação (estruturais)

**RD-001 — Classificação.** Um Pedido cujo Cliente tem mais de 5 pedidos aprovados nos últimos 12 meses é um Pedido de Cliente Recorrente.
Evidência: `src/desconto.js`, parâmetro `pedidosAprovados`, ainda sem nome de conceito no código.
Confiança: 🟡 inferida (a condição existe no código, mas o conceito "Cliente Recorrente" nunca foi validado como nome oficial com o time de negócio).

**RD-002 — Derivação.** O Desconto de um Pedido é calculado como o Valor Total multiplicado pelo percentual da Faixa de Desconto correspondente, mais 5 pontos percentuais se o Pedido for de Cliente Recorrente, respeitando sempre o Teto de Desconto.
Evidência: `src/desconto.js`, função `calcularDesconto`.
Confiança: 🟢 confirmada.

**Regra estrutural adicional.** É necessário que todo Pedido tenha exatamente um Cliente associado, e que esse Cliente tenha exatamente um Tipo.

## Regras operativas (comportamentais)

No vocabulário do RuleSpeak, numeradas e com evidência:

**RN-001**: O Desconto de um Pedido **must** ser calculado pela Faixa de Desconto correspondente ao Valor Total.
Evidência: `src/desconto.js`, linhas 24-28. Confiança: 🟢 confirmada.

**RN-002**: O Desconto de um Pedido **must not** exceder o Teto de Desconto de R$ 1.000,00.
Evidência: `src/desconto.js`, `Math.min(..., TETO_DESCONTO)`. Confiança: 🟢 confirmada.

**RN-003**: Um Pedido **may** receber a Faixa de Desconto de 20% **only if** o Cliente for do Tipo atacado e o Valor Total for maior que R$ 10.000,00.
Evidência: especificação da Sessão 3; sem implementação correspondente ainda. Confiança: 🔴 lacuna.

**RN-004**: Um Pedido de Cliente Recorrente **may** receber 5 pontos percentuais adicionais de desconto **only if** o Pedido for de cliente atacado.
Evidência: especificação da Sessão 3, oficina de ferramentas. Confiança: 🟡 inferida (implementada no exercício, ainda sem revisão de negócio).

## Tabela de decisão DMN

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

A última linha usa "—", não "0%": cliente padrão nunca é classificado como Cliente Recorrente pela regra RD-001, então essa combinação não deveria existir nos dados. Se ela aparecer em produção, o problema não é a tabela: é algum outro ponto do sistema que deixou um cliente padrão ser marcado como recorrente.

**Política de acerto: Priority.** As duas últimas linhas se sobrepõem às seis primeiras sempre que "Cliente Recorrente" for verdadeiro — por isso a tabela não pode ser Unique. A prioridade declarada é: se Cliente Recorrente for verdadeiro, essa linha vence sobre a linha correspondente de valor e tipo, e o resultado soma o adicional à faixa que seria aplicada de outro modo.

## Verificação por retrotradução

Peça a alguém (ou ao próprio agente, numa conversa nova) para reescrever a tabela de volta em prosa, sem ver a especificação original:

> "Pedidos até R$ 500 não têm desconto; de R$ 500,01 a R$ 2.000 têm 5%; de R$ 2.000,01 a R$ 5.000 têm 10%; acima de R$ 5.000 até R$ 10.000 têm 15%; acima de R$ 10.000, cliente atacado tem 20% e cliente padrão continua com 15%. Se o cliente for atacado e recorrente, soma-se mais 5 pontos percentuais à faixa que já valeria, respeitando o teto."

Essa retrotradução bate com a regra original — nenhum escopo foi ampliado, nenhuma condição foi perdida, e a composição (soma sobre a faixa já aplicável) ficou explícita. Se a retrotradução tivesse dito "cliente recorrente sempre paga 5%", sem mencionar que o adicional se soma à faixa normal, isso teria exposto uma perda de composição antes de o erro chegar a produção.

## Leitura do exemplo

A regra não mudou de significado ao longo do processo: mudou de forma. Prosa, BR/FR, vocabulário com sinônimos, regra de classificação, regra de derivação, sentença RuleSpeak numerada com evidência e confiança, tabela de decisão: cada forma é mais estruturada que a anterior, e cada uma facilita um tipo diferente de verificação. A prosa é fácil de escrever e difícil de verificar; a tabela é mais trabalhosa de montar e quase impossível de deixar uma combinação de fora sem que isso apareça como uma linha ausente ou um "—" mal justificado.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
