# Exemplo de aplicação de IA: a spec do pedido mínimo

## Passo 1: baixe o projeto da Vetor

Digite no terminal para baixar o projeto de exemplo da Vetor, plataforma fictícia de e-commerce B2B do workshop, e conferir os testes:

```bash
npx degit arkhibr/workshops-ia-agentica/exemplo/vetor vetor-pedido-minimo
cd vetor-pedido-minimo
npm test
```

O `npm test` mostra 6 testes passando.

## Passo 2: registre o estado inicial

Digite no terminal:

```bash
git init
git add -A
git commit -m "estado inicial"
```

Cada passo deste roteiro termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

## Passo 3: instale o Spec Kit no projeto

Digite no terminal:

```bash
specify init --here --force --integration claude
```

Quando o comando perguntar o tipo de script, aperte Enter para aceitar o padrão do sistema. Depois, registre a instalação:

```bash
git add -A
git commit -m "spec kit instalado"
```

Abra o agente dentro da pasta `vetor-pedido-minimo`.

## Passo 4: defina a constitution

Digite no chat do agente o comando `/speckit-constitution`, seguido dos três princípios:

```text
/speckit-constitution Três princípios, nada além deles.
I. Rastreabilidade: toda regra de negócio implementada cita o ID de
origem (RC-xx, RD-xx ou RN-xx) no requisito, no teste e no comentário
do código.
II. Testes antes do código: cada requisito funcional ganha um teste em
node:test que falha antes da implementação; npm test é o único comando
de verificação.
III. Sem dependências: o projeto continua sem pacotes de terceiros e
usa só a biblioteca padrão do Node 20.
```

Depois, no terminal:

```bash
git add -A
git commit -m "constitution"
```

**O que o agente gerou.** O comando levou cerca de 40 segundos. O agente escreveu os três princípios pedidos em `.specify/memory/constitution.md` e acrescentou, a cada um, um parágrafo de justificativa:

```text
### II. Testes antes do código

Cada requisito funcional MUST ganhar um teste em `node:test` escrito
antes da implementação, e esse teste MUST ser visto falhando antes de o
código existir. [...]

Por quê: teste que nunca falhou não prova nada sobre o código que diz
cobrir.
```

Ele também criou uma seção de governança com versionamento semântico da própria constitution, que ninguém pediu. A seção não muda nenhuma saída dos comandos seguintes, e por isso passa pelo critério da página de conceitos como decoração inofensiva. A pergunta para discussão é se ela é ganho ou ruído.

## Passo 5: gere a spec

Digite no chat do agente o comando `/speckit-specify`, seguido do nome da feature e das três regras de origem:

```text
/speckit-specify Pedido mínimo de atacado da Vetor. Regras de origem:
RD-01: Valor do pedido, para efeito de pedido mínimo, é o valor total
antes do desconto.
RN-01: É obrigatório que pedido de cliente atacado tenha valor do
pedido de pelo menos R$ 1.000,00.
RN-02: Pedido de cliente padrão não tem valor mínimo.
```

Depois, no terminal:

```bash
git add -A
git commit -m "spec do pedido minimo"
```

**O que o agente gerou.** O comando levou cerca de um minuto e meio e criou a pasta `specs/001-...` com uma `spec.md` de pouco mais de cem linhas. Os pontos a observar estão em três trechos.

*O caso que a RD-01 existe para pegar.* O agente transformou a regra de derivação numa história própria, com o exemplo que separa as duas leituras possíveis:

```text
1. Given um cliente atacado, When ele submete um pedido de R$ 1.050,00
   que recebe R$ 52,50 de desconto, Then o pedido é aceito, porque o
   valor considerado é R$ 1.050,00 (RD-01).
```

É o resultado esperado de uma regra bem decomposta: a RD-01 virou um cenário que falha se alguém usar o valor líquido.

*Requisitos sem origem.* A constitution exige ID em todo requisito que implementa regra de negócio, e dois requisitos saíram sem:

```text
- FR-006: O sistema MUST recusar como entrada inválida valor de pedido
  negativo ou não numérico, de forma distinguível da recusa por pedido
  mínimo.
- FR-007: A verificação de pedido mínimo MUST NOT alterar o cálculo de
  desconto existente.
```

O FR-007 é uma proteção técnica contra regressão e pode ficar sem ID. O FR-006 decide como o sistema responde a uma entrada que o mapa não previa, e essa decisão pode afetar a mensagem que o cliente vê. Fica em aberto se ele precisa de uma regra de origem.

*Critério que diz mais que o requisito.* Compare:

```text
- FR-004 (RN-01): Ao recusar um pedido pelo mínimo, o sistema MUST
  informar o motivo, incluindo o valor mínimo exigido (R$ 1.000,00).
- SC-004: Toda recusa por mínimo deixa claro para o cliente o valor
  que falta atingir, sem precisar consultar outra fonte.
```

O requisito pede o mínimo exigido. O critério de sucesso pede o valor que falta, que é outra informação e exige outro cálculo. Nenhuma das três regras fala disso. Se o critério ficar, o plano vai tentar cumpri-lo e alguém vai implementar uma mensagem que o negócio não pediu.

## O que levar para o exercício

Os três achados correspondem às três perguntas do exercício: requisito sem origem, decisão tomada fora do mapa de regras e critério sem lastro. Nenhum deles impede o ciclo de seguir, e todos chegariam ao código se ninguém lesse as três seções.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 07/10/2026. Outra execução produz texto diferente, e os pontos a observar costumam se repetir.

**Próxima página:** [Exercício de IA: especificar o frete da Vetor](especificacao-com-spec-kit-exercicio.md).
