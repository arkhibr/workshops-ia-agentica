# Cenário — Desconto por volume de pedido

> Este arquivo é o gabarito da regra de negócio. Não mostre ao agente literalmente — use-o para construir o Prompt Estruturado do Passo 2 com suas próprias palavras.

## Regra de negócio

Um pedido recebe desconto sobre o valor total, de acordo com faixas de valor:

| Faixa de valor do pedido | Desconto |
|---|---|
| Até R$ 500,00 | 0% |
| De R$ 500,01 a R$ 2.000,00 | 5% |
| De R$ 2.000,01 a R$ 5.000,00 | 10% |
| Acima de R$ 5.000,00 | 15% |

## Exceção 1 — Teto de desconto

Independentemente da faixa, o desconto em reais não pode ultrapassar **R$ 1.000,00** por pedido. Um pedido de R$ 8.000,00 calcularia 15% = R$ 1.200,00 de desconto — mas o valor aplicado é limitado a R$ 1.000,00.

## Exceção 2 — Cliente atacado

Clientes classificados como **atacado** têm uma faixa adicional: pedidos acima de R$ 10.000,00 recebem **20%** de desconto, ainda respeitando o teto de R$ 1.000,00 (ou seja, o teto sempre prevalece).

## Assinatura-alvo sugerida

```
calcularDesconto(valorPedido: decimal, tipoCliente: "padrao" | "atacado"): decimal
```

Retorna o valor do desconto em reais (não o percentual, não o valor final do pedido).
