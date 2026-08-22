# Critérios de aceitação — Desconto por volume de pedido

Rode cada caso contra as duas saídas do Exercício 4 (prompt intuitivo e prompt estruturado). Marque passou/falhou.

| # | Valor do pedido | Tipo de cliente | Desconto esperado | O que o caso verifica |
|---|---|---|---|---|
| 1 | R$ 300,00 | padrão | R$ 0,00 | Faixa mais baixa, sem desconto |
| 2 | R$ 1.000,00 | padrão | R$ 50,00 | Faixa de 5% |
| 3 | R$ 3.000,00 | padrão | R$ 300,00 | Faixa de 10% |
| 4 | R$ 6.000,00 | padrão | R$ 900,00 | Faixa de 15%, ainda abaixo do teto |
| 5 | R$ 8.000,00 | padrão | R$ 1.000,00 | Faixa de 15% estouraria R$ 1.200,00 — teto aplicado |
| 6 | R$ 12.000,00 | atacado | R$ 1.000,00 | Faixa de 20% (atacado) estouraria R$ 2.400,00 — teto aplicado |
| 7 | R$ 12.000,00 | padrão | R$ 1.000,00 | Mesmo valor do caso 6, mas cliente padrão não tem a faixa de 20% — resultado é o mesmo pelo teto, mas por caminho diferente |
| 8 | R$ 500,00 | padrão | R$ 0,00 | Limite exato da primeira faixa (inclusivo) |

## O que este exercício deveria revelar

O prompt intuitivo, na maioria das execuções, inventa suas próprias faixas de desconto (porque nenhuma foi especificada) e não trata teto nem tipo de cliente — ele resolve *um* problema de desconto, não *o* problema desta regra de negócio. Os casos 5, 6 e 7 são os que mais frequentemente falham na saída intuitiva: são exatamente os que dependem de conhecimento de negócio que só existe no cenário, não no senso comum de "cálculo de desconto".
