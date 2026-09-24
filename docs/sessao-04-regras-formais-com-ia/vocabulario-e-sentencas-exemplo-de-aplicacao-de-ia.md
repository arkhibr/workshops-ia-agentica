# Exemplo de aplicação de IA: vocabulário e sentenças de regra

Esta é uma demonstração conduzida pelo instrutor. O objetivo é ver a regra de desconto da Vetor, já especificada em BR/FR na Sessão 3, virar vocabulário SBVR, regra de classificação, regra de derivação e sentenças RuleSpeak numeradas, com evidência e confiança — antes de qualquer tabela de decisão entrar em cena.

**A Vetor**, usada como caso em toda esta sessão, tem hoje a regra de desconto com faixas de valor, um teto de R$ 1.000,00, uma faixa de 20% para clientes atacado acima de R$ 10.000,00 e um adicional de 5 pontos percentuais para cliente atacado recorrente — toda ela em prosa e em código, `src/desconto.js`, nunca em vocabulário controlado.

## Vocabulário SBVR

| Termo | O que significa | Sinônimos a evitar |
|---|---|---|
| Pedido | Uma solicitação de compra na Vetor, com um Valor Total e um Cliente associado | "order", "compra" |
| Cliente | Quem faz o Pedido; tem um Tipo (padrão ou atacado) | "usuário", "conta" |
| Faixa de Desconto | Percentual aplicável ao Valor Total, determinado pelo intervalo em que ele se encaixa | "tier", "nível" |
| Teto de Desconto | Valor máximo, em reais, que o Desconto de um Pedido pode atingir | "limite", "cap" |
| Cliente Recorrente | Cliente atacado com mais de 5 pedidos aprovados nos últimos 12 meses | (conceito não nomeado no código hoje) |

A última linha é a mais importante: "Cliente Recorrente" nunca teve nome no código. Existe hoje como um `if (pedidosAprovados > 5)` solto, sem que o conceito por trás da condição tenha sido nomeado em lugar nenhum.

## Regras de classificação e derivação (estruturais)

**RD-001 — Classificação.** Um Pedido cujo Cliente tem mais de 5 pedidos aprovados nos últimos 12 meses é um Pedido de Cliente Recorrente.
Evidência: `src/desconto.js`, parâmetro `pedidosAprovados`, ainda sem nome de conceito no código.
Confiança: 🟡 inferida.

**RD-002 — Derivação.** O Desconto de um Pedido é calculado como o Valor Total multiplicado pelo percentual da Faixa de Desconto correspondente, mais 5 pontos percentuais se o Pedido for de Cliente Recorrente, respeitando sempre o Teto de Desconto.
Evidência: `src/desconto.js`, função `calcularDesconto`.
Confiança: 🟢 confirmada.

## Regras operativas (comportamentais)

**RN-001**: O Desconto de um Pedido **deve** ser calculado pela Faixa de Desconto correspondente ao Valor Total.
Evidência: `src/desconto.js`, linhas 24-28. Confiança: 🟢 confirmada.

**RN-002**: O Desconto de um Pedido **não deve** exceder o Teto de Desconto de R$ 1.000,00.
Evidência: `src/desconto.js`, `Math.min(..., TETO_DESCONTO)`. Confiança: 🟢 confirmada.

**RN-003**: Um Pedido **pode** receber a Faixa de Desconto de 20% **somente se** o Cliente for do Tipo atacado e o Valor Total for maior que R$ 10.000,00.
Evidência: especificação da Sessão 3; sem implementação correspondente ainda. Confiança: 🔴 lacuna.

**RN-004**: Um Pedido de Cliente Recorrente **pode** receber 5 pontos percentuais adicionais de desconto **somente se** o Pedido for de cliente atacado.
Evidência: especificação da Sessão 3. Confiança: 🟡 inferida.

## Verificação por retrotradução

A técnica que confirma se a formalização preservou a intenção original chama-se retrotradução: peça a alguém, ou ao próprio agente numa conversa nova, sem ver a formalização, para reescrever a regra formal de volta em prosa comum. Peça a retrotradução das quatro sentenças acima, sem contexto adicional:

> "O desconto de um pedido segue a faixa correspondente ao valor total, sem nunca passar de R$ 1.000,00. Pedidos de cliente atacado acima de R$ 10.000,00 entram numa faixa de 20%. E se o pedido for de um cliente atacado que já fez mais de 5 pedidos aprovados, soma-se mais 5 pontos percentuais a essa faixa."

Essa retrotradução preserva os quatro elementos: a faixa por valor, o teto, a faixa de atacado condicionada ao valor de corte, e o adicional de recorrência como soma, não substituição. Se a retrotradução tivesse dito "cliente recorrente sempre paga 5%", sem mencionar que o adicional se soma à faixa normal, isso teria exposto uma perda de composição antes de o erro chegar a qualquer implementação.

## Leitura do exemplo

A regra não mudou de significado ao longo do processo: mudou de forma. Prosa, BR/FR, vocabulário com sinônimos, regra de classificação, regra de derivação, sentença RuleSpeak numerada com evidência e confiança — cada forma é mais estruturada que a anterior, e cada uma facilita um tipo diferente de verificação.

**Próxima página:** [Exercício de IA — Geral](vocabulario-e-sentencas-exercicio-geral.md).
