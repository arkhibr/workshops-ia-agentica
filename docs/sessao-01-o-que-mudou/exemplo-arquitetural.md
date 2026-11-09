# Exemplo arquitetural

O instrutor conduz esta demonstração sem que os participantes executem nada, para mostrar, antes da prática, em que ponto um prompt vago perde uma regra de negócio.

A **Vetor** é uma empresa fictícia de e-commerce B2B, usada nos exemplos deste workshop. Ela atende dois tipos de cliente, padrão e atacado.

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

Uma saída típica desse prompt inventa as próprias faixas, porque nenhuma foi especificada. Ela ignora o teto de R$ 1.000,00 e nem sabe que existe um tipo de cliente chamado atacado, já que essa informação nunca apareceu no pedido. O código compila e roda, mas calcula um desconto genérico, diferente do que a Vetor aplica.

## Prompt estruturado

> Escreva uma função `calcularDesconto(valorPedido: decimal, tipoCliente: "padrao" | "atacado"): decimal` que recebe o valor de um pedido e o tipo de cliente e devolve o valor do desconto em reais, seguindo a tabela de faixas [tabela colada aqui], respeitando um teto de R$ 1.000,00, e aplicando a faixa adicional de 20% acima de R$ 10.000,00 apenas para clientes atacado.

Essa versão acerta a regra porque o pedido trazia as faixas, o teto e a exceção do atacado, reunidos por quem escreveu o prompt.

## Onde a diferença aparece

| Caso de teste | Prompt intuitivo | Prompt estruturado |
|---|---|---|
| Pedido de R$ 300 (padrão) | depende da faixa inventada pelo modelo | R$ 0,00 (correto) |
| Pedido de R$ 8.000 (padrão) | provavelmente aplica 15% sem teto: R$ 1.200,00 | R$ 1.000,00 (teto aplicado) |
| Pedido de R$ 12.000 (atacado) | não reconhece o conceito de atacado | R$ 1.000,00 (20% estouraria o teto) |

A diferença aparece nos dois casos que dependem de conhecimento de negócio, o teto e o tipo de cliente, e o modelo não tinha como deduzir nenhum dos dois porque nenhum estava escrito no pedido intuitivo.

## Leitura do exemplo

O ganho veio do trabalho de reunir a regra de negócio completa antes de escrever o prompt, e esse trabalho é o assunto da Sessão 3, de exploração e especificação, e da Sessão 4, de regras formais com IA.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
