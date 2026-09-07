# Exemplo arquitetural: do pedido vago à especificação da Vetor

Este exemplo é uma demonstração conduzida pelo instrutor, não um exercício. O objetivo é ver o ciclo inteiro (explorar, perguntar, propor, especificar) funcionando sobre um pedido real, antes de os participantes conduzirem o próprio ciclo na oficina.

**A Vetor**, usada como caso em toda esta sessão, é uma plataforma fictícia de e-commerce B2B que atende dois tipos de cliente: padrão e atacado. Desde a Sessão 1, sua função `calcularDesconto` recebe um parâmetro `tipoCliente` que não usa — a faixa de atacado nunca foi implementada.

## O pedido, como ele chega de verdade

> "Ative o desconto de atacado que a gente conversou semana passada."

Isso é tudo que o time recebeu. Nenhuma faixa, nenhum valor, nenhuma menção ao teto que já existe para os outros clientes.

## Explorar

Antes de perguntar qualquer coisa, o código já revela parte da resposta: `calcularDesconto(valorTotal, tipoCliente)` já aceita `tipoCliente`, e a Sessão 1 documentou que a intenção sempre foi uma faixa de 20% acima de R$ 10.000,00. Isso não é a especificação — é o ponto de partida que evita perguntar algo que já está no código.

## Perguntar

Aplicando o repertório da página [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md):

| Pergunta | Resposta de quem pediu |
|---|---|
| A partir de que valor a faixa de atacado começa? | Acima de R$ 10.000,00 |
| O pedido de exatamente R$ 10.000,00 entra na faixa nova ou na anterior? | Fica na faixa anterior (10% ou 15%, conforme o valor); "acima de" é estrito |
| O teto de R$ 1.000,00 continua valendo para a faixa de atacado? | Sim, o teto vale para qualquer faixa, sempre valeu |
| O que acontece se `tipoCliente` vier diferente de `'padrao'` ou `'atacado'`? | Já lança erro hoje; continua assim |

Quatro perguntas, quatro respostas — e cada resposta já é uma regra de negócio que precisa entrar na especificação.

## Propor

> Proposta: implementar a faixa de 20% de desconto para clientes atacado, com pedidos acima de R$ 10.000,00 (exclusive), respeitando o teto de R$ 1.000,00 já existente. Nenhuma outra faixa muda.

Três frases, devolvidas para quem pediu antes de especificar em detalhe — o ponto mais barato para descobrir se a proposta pegou o problema certo.

## Especificar

Com a proposta validada, a especificação sai no padrão BR/FR/NFR:

**BR-01.** O desconto de qualquer pedido, de qualquer tipo de cliente, nunca ultrapassa R$ 1.000,00.

**BR-02.** Clientes do tipo atacado têm direito a uma faixa de desconto de 20% sobre pedidos com valor estritamente maior que R$ 10.000,00.

**FR-01.** `calcularDesconto(valorTotal, tipoCliente)` retorna 20% de `valorTotal` quando `tipoCliente` for `'atacado'` e `valorTotal` for maior que 10000, respeitando BR-01.

**FR-02.** Para `tipoCliente` igual a `'atacado'` e `valorTotal` igual ou menor que 10000, o comportamento permanece o das faixas já existentes.

**Casos de teste que a especificação precisa cobrir:**

| # | Valor do pedido | Tipo de cliente | Desconto esperado |
|---|---|---|---|
| 1 | R$ 10.000,00 | atacado | R$ 1.000,00 (faixa de 15%, não a nova) |
| 2 | R$ 10.000,01 | atacado | R$ 1.000,00 (20% seria R$ 2.000,00, mas o teto prevalece) |
| 3 | R$ 6.000,00 | atacado | R$ 900,00 (faixa de 15%, sem mudança) |

## Leitura do exemplo

Nenhuma dessas quatro linhas de regra veio de "pensar bem" sobre o problema: vieram de perguntar e registrar a resposta antes de escrever código. Se o time tivesse pedido direto ao agente "ative o desconto de atacado", ele teria adivinhado um valor de corte, uma regra de arredondamento na fronteira e uma posição sobre o teto — as mesmas três decisões que aqui vieram de quem realmente sabia a resposta.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
