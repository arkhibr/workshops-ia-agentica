# Exercício de IA: do plano ao frete funcionando

## Passo 1: gere o plano

Digite no chat do agente, aberto na pasta `vetor-frete` do exercício do Tema 1, o comando `/speckit-plan`, seguido das escolhas técnicas. No Codex, troque a barra por cifrão (`$speckit-...`).

```text
/speckit-plan JavaScript ESM com Node 20, testes em node:test executados
por npm test, sem dependências. O frete fica em src/frete.js.
```

Depois, no terminal:

```bash
git add -A
git commit -m "plano do frete"
```

Cada passo deste exercício termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

Abra o `plan.md` e leia só a tabela do *Constitution Check*. Cada princípio deve trazer uma justificativa, além da marca de aprovado.

## Passo 2: gere as tarefas

Digite no chat do agente, sem argumentos:

```text
/speckit-tasks
```

Depois, no terminal:

```bash
git add -A
git commit -m "tarefas do frete"
```

## Passo 3: peça o esqueleto das tarefas

Digite no chat do agente o pedido abaixo. Não leia o arquivo `tasks.md`, que costuma passar de 150 linhas:

```text
Liste as tarefas do tasks.md numa tabela com ID, [P], história e no
máximo oito palavras de descrição. Depois, copie as linhas de
Checkpoint. Não altere nenhum arquivo.
```

## Passo 4: classifique três tarefas

Escolha na tabela uma tarefa de cada tipo e preencha:

| Tarefa | Atômica ou composta? | Que comando prova que terminou? | Merece parada humana? |
|---|---|---|---|
| Uma que escreve teste | | | |
| Uma que roda `npm test` esperando falha | | | |
| Uma que altera `src/frete.js` | | | |

Responda também: o template marca as tarefas de teste como opcionais. Por que elas apareceram no seu `tasks.md`?

## Passo 5: implemente até a primeira história

Digite no chat do agente o comando `/speckit-implement`, seguido do ponto de parada:

```text
/speckit-implement Execute até o checkpoint da história US1 e pare.
```

## Passo 6: revise antes de seguir

Digite no terminal:

```bash
git status
git diff --stat
npm test
```

Confira se o diff só toca arquivos listados na *Project Structure* do `plan.md`, além do `tasks.md`. Se os testes passarem, registre a parada:

```bash
git add -A
git commit -m "frete: historia US1"
```

## Passo 7: implemente o restante

Digite no chat do agente:

```text
/speckit-implement Execute as fases restantes.
```

Depois, no terminal:

```bash
npm test
git add -A
git commit -m "frete implementado"
```

O total de testes precisa ter crescido em relação à parada da US1, sem nenhuma falha.

## Passo 8: localize uma regra no código

Digite no terminal, trocando `RN-02` pelo ID que a sua spec deu à regra do frete grátis do atacado, anotado no exercício do Tema 1:

```bash
git grep -l "RN-02"
```

A saída precisa incluir o código do frete, o arquivo de teste e a `spec.md`. Os outros artefatos da pasta `specs` também aparecem, porque citam a regra. O `git grep` funciona igual nos três sistemas e procura só nos arquivos versionados, por isso o commit do Passo 7 vem antes.

## Evidência a entregar

A tabela do Passo 4 com a resposta sobre as tarefas de teste, a saída final do `npm test` e a saída do Passo 8.

## Extensão: no seu repositório

No ramo descartável em que você rodou a extensão do exercício anterior, rode `plan` e `tasks` sobre a sua spec. Antes de implementar, marque no esqueleto as tarefas que tocam código existente: são elas que pedem parada humana.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
