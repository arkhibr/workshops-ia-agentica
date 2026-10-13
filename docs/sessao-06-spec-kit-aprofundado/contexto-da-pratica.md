# Contexto da prática: exemplos e exercícios

As quatro páginas práticas da sessão, dois exemplos e dois exercícios, são roteiros de comandos em que cada passo começa pelo comando a digitar. Esta página reúne o que elas não repetem: o ponto de partida, o objetivo de cada uma, os pedidos do PO e a constitution usada em todas.

## O ponto de partida

Exemplos e exercícios começam numa pasta vazia, sem código. Quem conduz faz o papel do PO de um sistema de pagamentos de projetos e entrega ao agente um pedido em linguagem natural. A partir dele, o GitHub Spec Kit leva o agente pela constitution, pela spec, pelo esclarecimento, pelo plano, pelo checklist, pelas tarefas e pela análise até o código com testes.

Os três pedidos são cenários inventados para esta sessão, sobre projetos de pesquisa da ACME, uma universidade fictícia, e não reproduzem regra vigente de nenhuma instituição real.

Os exemplos usam a pasta `acme-dupla-aprovacao`, os exercícios usam a pasta `acme-saldo-rubrica` e a tarefa entre sessões usa a pasta `acme-ordem-de-compra`. Antes de começar, confira se o terminal responde `CLI Version 1.1.1` ao comando `specify version`. Se não responder, siga a [preparação do ambiente da Sessão 5](../sessao-05-decomposicao/preparacao.md).

## O objetivo de cada página

| Página | Caso | Comandos | Objetivo | Produto | Tempo |
|---|---|---|---|---|---:|
| [Exemplo do Tema 1](qualidade-da-spec-exemplo-de-aplicacao-de-ia.md) | Dupla aprovação | `init` a `checklist` | Mostrar o que o `clarify` pergunta, o que ele deixa de perguntar e o que o checklist aponta | Spec com `## Clarifications` e checklist de 39 itens | 8 min |
| [Exercício do Tema 1](qualidade-da-spec-exercicio.md) | Saldo da rubrica | `init` a `checklist` | Responder ao `clarify` como dono da regra e ler o checklist como teste dos requisitos | Spec esclarecida, checklist e três respostas | 25 min |
| [Exemplo do Tema 2](teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md) | Dupla aprovação | `tasks` a `implement` | Mostrar o achado crítico do `analyze`, a trava do checklist e o vermelho conferido | Dupla aprovação implementada, com 57 testes passando | 8 min |
| [Exercício do Tema 2](teste-antes-do-codigo-exercicio.md) | Saldo da rubrica | `tasks` a `implement` | Conferir o motivo do vermelho e testar a fronteira do saldo | Saldo implementado, vermelho conferido e fronteira testada | 30 min |

O exemplo do Tema 2 continua a pasta do exemplo do Tema 1, e o exercício do Tema 2 continua a do exercício do Tema 1. Quem não terminou o exercício do Tema 1 roda os passos dele até o commit do checklist antes de começar o do Tema 2.

## Os pedidos do PO

Os pedidos não trazem IDs de regra. A constitution manda o agente extrair as regras e dar a cada uma um ID `RN-xx`, e a numeração pode mudar de uma execução para outra.

**Dupla aprovação, usada nos exemplos:**

```text
Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME. Todo pagamento
feito com recurso de um projeto precisa ser aprovado antes de ser
liquidado. Pagamentos acima de R$ 5.000,00 precisam de duas aprovações,
exceto quando o fornecedor está na lista de fornecedores recorrentes
pré-aprovados, caso em que uma aprovação basta. Pagamentos até esse
valor precisam de uma aprovação. Quem solicitou o pagamento não pode
aprová-lo.
```

**Saldo da rubrica, usado nos exercícios:**

```text
Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME. Cada projeto
tem rubricas, como material de consumo, serviços de terceiros e
diárias, e cada rubrica tem um valor aprovado no plano de trabalho.
Um pagamento só pode ser solicitado se a rubrica tiver saldo para ele.
O saldo da rubrica é o valor aprovado menos os pagamentos já
liquidados.
```

**Ordem de compra, usada na tarefa entre sessões:**

```text
Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME. Um pagamento
não pode ser liquidado se a ordem de compra correspondente não tiver
sido aprovada, salvo nos pagamentos automáticos autorizados, como
contas de consumo com débito em conta.
```

Os três pedidos deixam lacunas de propósito, como o que acontece quando a mesma pessoa tenta aprovar duas vezes, se um pagamento ainda não liquidado reserva saldo e o que define um pagamento automático autorizado. São elas que o `clarify` deveria levar ao PO.

## A constitution da sessão

Os quatro roteiros e a tarefa usam a mesma constitution, em que os princípios I e III repetem os da Sessão 5 e o princípio II passa a exigir que a implementação de cada história espere o `npm test` mostrar os testes dela falhando:

```text
/speckit-constitution Três princípios, nada além deles.
I. Rastreabilidade: cada regra de negócio extraída do pedido do PO
recebe um ID RN-xx na spec, e esse ID é citado no requisito, no teste
e no comentário do código.
II. Teste vermelho antes do código: cada requisito funcional ganha um
teste em node:test, e a implementação de uma história só começa depois
que npm test mostra os testes dessa história falhando.
III. Sem dependências: o projeto usa só a biblioteca padrão do Node 20,
sem pacotes de terceiros.
```

## Comandos por agente

Os roteiros usam a forma do Claude Code. As diferenças para os outros agentes:

| Agente | Integração no `specify init` | Prefixo dos comandos no chat |
|---|---|---|
| Claude Code | `--integration claude` | `/speckit-...` |
| Codex CLI | `--integration codex` | `$speckit-...` |
| GitHub Copilot | `--integration copilot` | `/speckit-...` |

**Próxima página:** [Qualidade da spec: clarify e checklist](qualidade-da-spec-conceitos.md).
