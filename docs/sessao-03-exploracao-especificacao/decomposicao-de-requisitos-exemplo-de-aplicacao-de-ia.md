# Exemplo de aplicação de IA: decomposição de requisitos

Esta é uma demonstração conduzida pelo instrutor. O objetivo é acompanhar o ciclo inteiro — explorar, perguntar, propor, especificar — sobre um pedido vago real da Vetor, até uma especificação decomposta em BR, FR e NFR, verificada por retrotradução, antes de qualquer linha de código mudar.

**A Vetor**, usada como caso em toda esta sessão, é uma plataforma fictícia de e-commerce B2B que atende dois tipos de cliente: padrão e atacado. Sua função `calcularDesconto` recebe um parâmetro `tipoCliente` que não usa, e a faixa de atacado nunca foi implementada.

## O pedido original

> "Ative o desconto de atacado que a gente conversou semana passada."

Isso é tudo que o time recebeu. Nenhuma faixa, nenhum valor, nenhuma menção ao teto que já existe para os outros clientes.

## Explorar

Antes da primeira pergunta, o código já revela parte da resposta: `calcularDesconto(valorTotal, tipoCliente)` já aceita `tipoCliente`, e uma conversa anterior documentou que a intenção sempre foi uma faixa de 20% acima de R$ 10.000,00. Isso ainda não é a especificação, mas evita perguntar algo cuja resposta já está registrada no código.

## Perguntar

| Pergunta | Resposta de quem pediu |
|---|---|
| A partir de que valor a faixa de atacado começa? | Acima de R$ 10.000,00 |
| O pedido de exatamente R$ 10.000,00 entra na faixa nova ou na anterior? | Fica na faixa anterior. "Acima de" é estrito |
| O teto de R$ 1.000,00 continua valendo para a faixa de atacado? | Sim, o teto vale para qualquer faixa, sempre valeu |
| O que acontece se `tipoCliente` vier diferente de `'padrao'` ou `'atacado'`? | Já lança erro hoje, e continua assim |
| A faixa de atacado pode ficar mais lenta que as outras, já que envolve mais um cálculo? | Não. O checkout roda sob pico de tráfego e precisa continuar respondendo rápido para todo tipo de cliente |

Cinco perguntas, cinco respostas, e cada uma já é uma regra de negócio ou de qualidade que precisa entrar na especificação.

## Propor

> Proposta: implementar a faixa de 20% de desconto para clientes atacado, com pedidos acima de R$ 10.000,00 (exclusive), respeitando o teto de R$ 1.000,00 já existente. Nenhuma outra faixa muda.

Três frases, devolvidas para quem pediu antes de especificar em detalhe, no ponto mais barato para descobrir se a proposta pegou o problema certo.

## Especificar

**BR-01.** O desconto de qualquer pedido, de qualquer tipo de cliente, nunca ultrapassa R$ 1.000,00.

**BR-02.** Clientes do tipo atacado têm direito a uma faixa de desconto de 20% sobre pedidos com valor estritamente maior que R$ 10.000,00.

**FR-01.** `calcularDesconto(valorTotal, tipoCliente)` retorna 20% de `valorTotal` quando `tipoCliente` for `'atacado'` e `valorTotal` for maior que 10000, respeitando BR-01.

**FR-02.** Para `tipoCliente` igual a `'atacado'` e `valorTotal` igual ou menor que 10000, o comportamento permanece o das faixas já existentes.

**NFR-01**, como cenário de qualidade completo:

| Elemento | Valor |
|---|---|
| Fonte | O checkout da Vetor, sob pico de tráfego |
| Estímulo | 500 pedidos de cliente atacado chegam no mesmo segundo |
| Ambiente | Operação normal, sem degradação prévia |
| Artefato | `calcularDesconto` |
| Resposta | Calcula o desconto de cada pedido, incluindo a faixa nova, sem enfileirar |
| Medida | 95% das chamadas respondem em menos de 100ms |

**Função de aptidão correspondente:** um teste de carga na esteira de integração contínua, com limiar de 100ms no percentil 95, responsável (o time que mantém `desconto.js`) e reação declarada (bloquear o *deploy* se o limiar for ultrapassado).

**Casos de teste que a especificação precisa cobrir:**

| # | Valor do pedido | Tipo de cliente | Desconto esperado |
|---|---|---|---|
| 1 | R$ 10.000,00 | atacado | R$ 1.000,00 (faixa de 15%, não a nova) |
| 2 | R$ 10.000,01 | atacado | R$ 1.000,00 (20% seria R$ 2.000,00, mas o teto prevalece) |
| 3 | R$ 6.000,00 | atacado | R$ 900,00 (faixa de 15%, sem mudança) |

## Retrotradução da especificação

A especificação acima foi escrita por quem conduziu a conversa, e quem escreve enxerga nela a intenção que tinha na cabeça, não apenas o que o texto diz. A retrotradução separa as duas coisas: abre-se uma conversa nova com o agente, sem nenhum histórico desta sessão, cola-se somente as regras e os requisitos, e pede-se a descrição em prosa do comportamento que eles produzem, sem julgamento e sem sugestão de melhoria.

O que volta é a leitura de quem só tem o texto, e a conferência é comparar essa leitura com a intenção original. Três divergências aparecem com frequência nesta especificação: a faixa de atacado substituir ou somar à faixa por volume, o valor de R$ 10.000,00 exato entrar ou ficar de fora, e o teto incidir sobre o percentual final ou sobre cada faixa isoladamente. A retrotradução é a única verificação disponível para quem não vai executar código, e ela funciona igualmente bem para quem vai: um caso de teste prova que a implementação corresponde à especificação, e a retrotradução prova que a especificação corresponde à intenção, uma pergunta anterior que nenhum teste responde.

## Leitura do exemplo

Nenhuma das cinco linhas de regra veio de "pensar bem" sobre o problema. Vieram de perguntar e registrar a resposta antes de escrever código. Se o time tivesse pedido direto ao agente "ative o desconto de atacado", ele teria adivinhado um valor de corte, uma regra de arredondamento na fronteira, uma posição sobre o teto e nenhuma exigência de desempenho sob carga — quatro decisões que aqui vieram de quem realmente sabia a resposta, a última só porque alguém perguntou por um atributo de qualidade em vez de assumir que "rápido o bastante" já estava implícito.

**Próxima página:** [Exercício de IA — Geral](decomposicao-de-requisitos-exercicio-geral.md).
