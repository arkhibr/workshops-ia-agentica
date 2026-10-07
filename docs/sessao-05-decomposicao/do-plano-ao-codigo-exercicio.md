# Exercício de IA: do plano ao frete funcionando

## Passo 1: gere o plano

Digite no chat do agente, aberto na pasta `vetor-frete` do exercício do Tema 1, o comando `/speckit-plan`, seguido das escolhas técnicas. No Codex, troque a barra por cifrão (`$speckit-...`).

```text
/speckit-plan JavaScript ESM com Node 20, testes em node:test executados
por npm test, sem dependências. O frete fica em src/frete.js e
reaproveita calcularDesconto de src/desconto.js.
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

Se os testes passarem e o diff não tocar `src/desconto.js` nem `test/desconto.test.js`, registre a parada:

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

O total de testes precisa ter crescido em relação aos 6 iniciais, sem nenhuma falha.

## Passo 8: localize uma regra no código

Digite no terminal, para procurar o ID da regra de frete grátis do atacado:

=== "macOS/Linux"
    ```bash
    grep -rl "RN-12" src test specs
    ```

=== "Windows (PowerShell)"
    ```powershell
    Get-ChildItem src, test, specs -Recurse -File | Select-String "RN-12" -List | Select-Object Path
    ```

A saída precisa incluir `src/frete.js`, `test/frete.test.js` e a `spec.md`. Os outros artefatos da pasta `specs` também aparecem, porque citam a regra.

## Evidência a entregar

A tabela do Passo 4 com a resposta sobre as tarefas de teste, a saída final do `npm test` e a saída do Passo 8.

## Extensão: no seu repositório

No ramo descartável em que você rodou a extensão do exercício anterior, rode `plan` e `tasks` sobre a sua spec. Antes de implementar, marque no esqueleto as tarefas que tocam código existente: são elas que pedem parada humana.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
