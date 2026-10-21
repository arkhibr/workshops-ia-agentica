# Tarefa entre sessões: a ordem de compra

Esta tarefa é obrigatória e deve ser entregue antes da Sessão 7. Ela repete, sobre um terceiro pedido do sistema de pagamentos de projetos, o fluxo desta sessão do `init` ao `analyze`, sem implementação. No ensaio feito em 13/10/2026, a espera pelo agente somou cerca de oito minutos e meio, e a tarefa inteira cabe em 30 a 40 minutos com a leitura das seções indicadas.

O pedido é um cenário sobre projetos de pesquisa da ACME, uma universidade fictícia, e não reproduz regra vigente de nenhuma instituição real. A constitution e os comandos de cada agente estão no [contexto da prática](contexto-da-pratica.md), e no Codex CLI os comandos de chat começam com cifrão (`$speckit-...`).

## Passo 1: crie a pasta e instale o Spec Kit

Digite no terminal:

```bash
mkdir acme-ordem-de-compra
cd acme-ordem-de-compra
git init
specify init --here --force --integration claude
git add -A
git commit -m "spec kit instalado"
```

Abra o agente dentro da pasta `acme-ordem-de-compra` e cole no chat a constitution da sessão, que está no contexto da prática e começa por `/speckit-constitution Três princípios, nada além deles.`, registrando depois com `git add -A` e `git commit -m "constitution"`.

## Passo 2: gere a spec

Digite no chat do agente:

```text
/speckit-specify Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME.
Um pagamento não pode ser liquidado se a ordem de compra correspondente
não tiver sido aprovada, salvo nos pagamentos automáticos autorizados,
como contas de consumo com débito em conta.
```

Antes de registrar, leia só a tabela de regras e a seção *Assumptions* da `spec.md`, e anote as decisões que o agente tomou sem o pedido dizer. Depois, registre a spec com os comandos `git add -A` e `git commit -m "spec"`.

## Passo 3: esclareça a spec

Digite no chat do agente:

```text
/speckit-clarify
```

Responda a cada pergunta como o PO responderia, conferindo se a recomendação altera alguma frase do pedido. Quando o agente encerrar, registre e guarde o diff da spec:

```bash
git add -A
git commit -m "clarify"
git diff HEAD~1 -- specs
```

## Passo 4: gere o plano e as tarefas

Digite no chat do agente, um comando de cada vez, e faça um commit depois de cada um:

```text
/speckit-plan Node 20, node:test, sem dependências, uma função pura por regra.
```

```text
/speckit-tasks
```

## Passo 5: analise os artefatos

Digite no chat do agente:

```text
/speckit-analyze
```

Copie o relatório inteiro que o agente mostrar e não peça correções. A tarefa termina aqui, sem `implement`, porque o objetivo é chegar à Sessão 7 com a análise lida e os achados classificados.

## Evidência a entregar

A entrega tem três partes, enviadas pelo canal a combinar com o instrutor:

1. A saída do `git diff HEAD~1 -- specs` do Passo 3, com as perguntas e respostas do `clarify`.
2. O relatório do `analyze` do Passo 5.
3. Duas frases: uma com a decisão do agente que você levaria ao PO antes de implementar, e outra com o achado do `analyze` que você corrigiria primeiro e o motivo.

No ensaio, o `clarify` fez três perguntas, uma delas sobre como o sistema sabe que um pagamento automático está autorizado, e o `analyze` apontou um achado CRITICAL sobre tarefas de implementação que poderiam ser adiantadas antes do vermelho.

**Próxima página:** [S7 — Casos de uso de IA por papel](../sessao-07-casos-de-uso-por-papel/index.md).
