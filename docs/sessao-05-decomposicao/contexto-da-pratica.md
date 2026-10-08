# Contexto da prática: exemplos e exercícios

As quatro páginas práticas da sessão, dois exemplos e dois exercícios, são roteiros de comandos: cada passo começa pelo comando a digitar. Esta página reúne o que elas não repetem: o ponto de partida, o objetivo de cada uma e os pedidos do PO.

## O ponto de partida

Exemplos e exercícios começam numa pasta vazia, sem código. Quem conduz faz o papel do PO da Vetor, plataforma fictícia de e-commerce B2B usada no workshop, e entrega ao agente um pedido em linguagem natural. A partir dele, o GitHub Spec Kit leva o agente pela constitution, pela spec, pelo plano e pelas tarefas até o código com testes.

Os exemplos usam a pasta `vetor-pedido-minimo` e os exercícios, a pasta `vetor-frete`. A instalação do Spec Kit 1.1.1 e do agente está na [preparação do ambiente](preparacao.md).

## O objetivo de cada página

| Página | Feature | Comandos | Objetivo | Produto | Tempo |
|---|---|---|---|---|---:|
| [Exemplo do Tema 1](especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md) | Pedido mínimo | `init`, `constitution`, `specify` | Mostrar como o pedido do PO vira regras com ID e quais decisões o agente toma sozinho | Spec do pedido mínimo e três achados sobre ela | 8 min |
| [Exercício do Tema 1](especificacao-com-spec-kit-exercicio.md) | Frete | `init`, `constitution`, `specify` | Encontrar na própria spec requisito que diz mais que o pedido, suposição que decide negócio e critério sem lastro | `spec.md` do frete versionada e três respostas | 25 min |
| [Exemplo do Tema 2](do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md) | Pedido mínimo | `plan`, `tasks`, `implement` | Mostrar o que o plano e as tarefas carregam da spec para o código, e onde entra a parada humana | Pedido mínimo implementado, com 10 testes passando | 8 min |
| [Exercício do Tema 2](do-plano-ao-codigo-exercicio.md) | Frete | `plan`, `tasks`, `implement` | Classificar tarefas, parar depois da primeira história e localizar uma regra no código | Frete implementado, testes passando e a regra do frete grátis localizada | 30 min |

O exemplo do Tema 2 continua a pasta do exemplo do Tema 1, e o exercício do Tema 2 continua a do exercício do Tema 1. Quem não terminou o exercício do Tema 1 roda os passos dele até o commit da spec antes de começar o do Tema 2.

## Os pedidos do PO

Os pedidos não trazem IDs de regra. A constitution manda o agente extrair as regras e dar a cada uma um ID `RN-xx`, e a numeração pode mudar de uma execução para outra.

**Pedido mínimo, usado nos exemplos:**

```text
Sou PO da Vetor, plataforma de e-commerce B2B que vende para dois tipos
de cliente: padrão e atacado. Pedidos pequenos de atacado não compensam
o custo de separação, então queremos um pedido mínimo para esses
clientes. Um pedido de atacado precisa ter pelo menos R$ 1.000,00.
Cliente padrão continua sem mínimo. Para o mínimo, vale o valor do
pedido antes do desconto. O desconto já chega calculado em cada pedido,
e a verificação do mínimo não calcula desconto.
```

**Frete, usado nos exercícios:**

```text
Sou PO da Vetor, plataforma de e-commerce B2B que vende para dois tipos
de cliente: padrão e atacado. Precisamos calcular o frete de cada
pedido. O frete normal é de R$ 80,00. Para incentivar pedidos maiores,
o cliente de atacado não paga frete quando o pedido passa de
R$ 3.000,00, e o cliente padrão paga R$ 40,00 quando o pedido passa de
R$ 5.000,00. Para essas faixas, vale o valor do pedido depois do
desconto. O desconto já chega calculado em cada pedido, e o frete não
calcula desconto.
```

Os dois pedidos deixam lacunas de propósito, como o valor exato do limite e o formato em que o valor chega. São elas que o agente preenche sozinho e que as perguntas dos exercícios pedem para encontrar.

## Comandos por agente

Os roteiros usam a forma do Claude Code. As diferenças para os outros agentes:

| Agente | Integração no `specify init` | Prefixo dos comandos no chat |
|---|---|---|
| Claude Code | `--integration claude` | `/speckit-...` |
| Codex CLI | `--integration codex` | `$speckit-...` |
| GitHub Copilot | `--integration copilot` | `/speckit-...` |

**Próxima página:** [Especificação com Spec Kit: constitution e spec](especificacao-com-spec-kit-conceitos.md).
