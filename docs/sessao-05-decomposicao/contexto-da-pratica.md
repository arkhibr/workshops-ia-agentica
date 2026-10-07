# Contexto da prática: exemplos e exercícios

As quatro páginas práticas da sessão, dois exemplos e dois exercícios, são roteiros de comandos: cada passo começa pelo comando a digitar. Esta página reúne o que elas não repetem: o objetivo de cada uma, o projeto de partida e as regras de origem.

## O projeto de partida

Todas partem do projeto de exemplo da Vetor, plataforma fictícia de e-commerce B2B usada no workshop. O projeto fica em `exemplo/vetor` no repositório do workshop, tem a regra de desconto e seis testes, e roda só com Node 20, sem dependências. Cada roteiro baixa uma cópia nova dele: os exemplos na pasta `vetor-pedido-minimo` e os exercícios na pasta `vetor-frete`.

A instalação do GitHub Spec Kit 1.1.1 e do agente está na [preparação do ambiente](preparacao.md).

## O objetivo de cada página

| Página | Feature | Comandos | Objetivo | Produto | Tempo |
|---|---|---|---|---|---:|
| [Exemplo do Tema 1](especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md) | Pedido mínimo | `init`, `constitution`, `specify` | Mostrar as decisões que o agente toma sozinho ao escrever a spec | Spec do pedido mínimo e três achados sobre ela | 8 min |
| [Exercício do Tema 1](especificacao-com-spec-kit-exercicio.md) | Frete | `init`, `constitution`, `specify` | Encontrar na própria spec requisito sem origem, suposição que decide negócio e critério sem lastro | `spec.md` do frete versionada e três respostas | 25 min |
| [Exemplo do Tema 2](do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md) | Pedido mínimo | `plan`, `tasks`, `implement` | Mostrar o que o plano e as tarefas carregam da spec para o código, e onde entra a parada humana | Pedido mínimo implementado, com 18 testes passando | 8 min |
| [Exercício do Tema 2](do-plano-ao-codigo-exercicio.md) | Frete | `plan`, `tasks`, `implement` | Classificar tarefas, parar depois da primeira história e localizar uma regra no código | Frete implementado, testes passando e RN-12 localizada | 30 min |

O exemplo do Tema 2 continua a pasta do exemplo do Tema 1, e o exercício do Tema 2 continua a do exercício do Tema 1. Quem não terminou o exercício do Tema 1 roda os passos dele até o commit da spec antes de começar o do Tema 2.

## As regras de origem

As regras seguem o formato da Sessão 4: RD para regra de derivação e RN para regra operativa.

**Pedido mínimo, usado nos exemplos:**

```text
RD-01: Valor do pedido, para efeito de pedido mínimo, é o valor total
antes do desconto.
RN-01: É obrigatório que pedido de cliente atacado tenha valor do
pedido de pelo menos R$ 1.000,00.
RN-02: Pedido de cliente padrão não tem valor mínimo.
```

**Frete, usado nos exercícios:**

```text
RD-11: Valor de referência do frete é o valor total do pedido menos
o desconto calculado pela regra de desconto vigente.
RN-11: O frete de um pedido é de R$ 80,00, salvo quando outra regra
deste mapa se aplicar.
RN-12: O frete de um pedido de cliente atacado é zero quando o valor
de referência ultrapassa R$ 3.000,00.
RN-13: O frete de um pedido de cliente padrão é de R$ 40,00 quando o
valor de referência ultrapassa R$ 5.000,00.
```

## Comandos por agente

Os roteiros usam a forma do Claude Code. As diferenças para os outros agentes:

| Agente | Integração no `specify init` | Prefixo dos comandos no chat |
|---|---|---|
| Claude Code | `--integration claude` | `/speckit-...` |
| Codex CLI | `--integration codex` | `$speckit-...` |
| GitHub Copilot | `--integration copilot` | `/speckit-...` |

**Próxima página:** [Especificação com Spec Kit: constitution e spec](especificacao-com-spec-kit-conceitos.md).
