# Exemplo arquitetural: o desconto da Vetor

Este exemplo é uma demonstração conduzida pelo instrutor, não um exercício. O objetivo é ver, antes de praticar, exatamente onde um prompt vago perde regra de negócio.

**A Vetor**, usada como caso em toda esta sessão, é uma plataforma fictícia de e-commerce B2B que atende dois tipos de cliente: padrão e atacado.

## A regra de negócio completa

A Vetor calcula desconto sobre o valor total de um pedido:

| Faixa de valor do pedido | Desconto |
|---|---|
| Até R$ 500,00 | 0% |
| De R$ 500,01 a R$ 2.000,00 | 5% |
| De R$ 2.000,01 a R$ 5.000,00 | 10% |
| Acima de R$ 5.000,00 | 15% |

Duas exceções que um pedido vago dificilmente cobre: o desconto nunca ultrapassa **R$ 1.000,00** por pedido, e clientes classificados como **atacado** têm uma faixa adicional de **20%** acima de R$ 10.000,00, ainda respeitando o teto.

## Prompt intuitivo

> Escreva uma função que calcula o desconto de um pedido baseado no valor total.

Uma saída típica desse prompt inventa suas próprias faixas (porque nenhuma foi especificada), ignora o teto de R$ 1.000,00 e não sabe que existe um tipo de cliente "atacado" porque essa informação nunca apareceu no pedido. O código compila e roda, mas resolve um desconto genérico, diferente da regra real da Vetor.

## Prompt estruturado

> Escreva uma função `calcularDesconto(valorPedido: decimal, tipoCliente: "padrao" | "atacado"): decimal` que recebe o valor de um pedido e o tipo de cliente e devolve o valor do desconto em reais, seguindo a tabela de faixas [tabela colada aqui], respeitando um teto de R$ 1.000,00, e aplicando a faixa adicional de 20% acima de R$ 10.000,00 apenas para clientes atacado.

Essa versão captura a regra inteira porque a regra inteira estava no prompt. Não é uma vitória do modelo: é uma vitória de quem escreveu o pedido.

## Onde a diferença aparece

| Caso de teste | Prompt intuitivo | Prompt estruturado |
|---|---|---|
| Pedido de R$ 300 (padrão) | depende da faixa inventada pelo modelo | R$ 0,00 — correto |
| Pedido de R$ 8.000 (padrão) | provavelmente aplica 15% sem teto: R$ 1.200,00 | R$ 1.000,00 — teto aplicado |
| Pedido de R$ 12.000 (atacado) | não reconhece o conceito de atacado | R$ 1.000,00 — 20% estouraria o teto |

Os casos que mais revelam a diferença são exatamente os que dependem de conhecimento de negócio que só existe fora do senso comum: teto e tipo de cliente. Nenhum modelo adivinha uma regra que ninguém escreveu.

## Leitura do exemplo

O ganho não veio de um modelo melhor nem de um prompt mais "inteligente". Veio de alguém ter feito, antes de escrever o prompt, o trabalho de reunir a regra de negócio inteira. Esse trabalho é exatamente o que a Sessão 3 (Exploração e especificação) e a Sessão 4 (Regras formais com IA) tratam com profundidade — aqui ele aparece em miniatura.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
