# Exercício de IA: do plano ao frete funcionando

Este exercício individual continua o projeto `vetor-frete` do exercício anterior, em que a Vetor, plataforma fictícia de e-commerce B2B do workshop, ganhou a spec do cálculo de frete. Agora o GitHub Spec Kit gera o plano e as tarefas, você classifica três delas e o agente implementa em duas etapas, com uma parada sua no meio. O exercício termina com os testes passando e cada regra de origem localizada no código.

Tempo: 30 minutos. Ponto de partida: a pasta `vetor-frete` com a `spec.md` commitada. Se você não terminou o exercício anterior, rode os Passos 1 a 4 da [página dele](especificacao-com-spec-kit-exercicio.md) e o commit do Passo 5 antes de começar.

No Codex, troque a barra dos comandos por cifrão (`$speckit-...`).

## Passo 1: plan

```text
/speckit-plan JavaScript ESM com Node 20, testes em node:test executados
por npm test, sem dependências. O frete fica em src/frete.js e
reaproveita calcularDesconto de src/desconto.js.
```

Abra o `plan.md` e leia só a tabela do *Constitution Check*. Cada princípio deve trazer uma justificativa, além da marca de aprovado.

## Passo 2: tasks

```text
/speckit-tasks
```

O `tasks.md` costuma passar de 150 linhas. Não leia o arquivo. Peça ao agente o esqueleto:

```text
Liste as tarefas do tasks.md numa tabela com ID, [P], história e no
máximo oito palavras de descrição. Depois, copie as linhas de
Checkpoint. Não altere nenhum arquivo.
```

## Passo 3: classifique três tarefas

Escolha na tabela uma tarefa de cada tipo e preencha:

| Tarefa | Atômica ou composta? | Que comando prova que terminou? | Merece parada humana? |
|---|---|---|---|
| Uma que escreve teste | | | |
| Uma que roda `npm test` esperando falha | | | |
| Uma que altera `src/frete.js` | | | |

Responda também: o template marca as tarefas de teste como opcionais. Por que elas apareceram no seu `tasks.md`?

## Passo 4: implemente a primeira história e pare

```text
/speckit-implement Execute até o checkpoint da história US1 e pare.
```

Revise o que mudou e rode os testes:

```bash
git status
npm test
```

Se os testes passarem, registre o ponto de parada:

```bash
git add -A
git commit -m "frete: historia US1"
```

## Passo 5: implemente o restante

```text
/speckit-implement Execute as fases restantes.
```

Rode `npm test` de novo. O total de testes precisa ter crescido em relação aos 6 iniciais, sem nenhuma falha.

## Passo 6: localize uma regra no código

Procure o ID da regra de frete grátis do atacado:

=== "macOS/Linux"
    ```bash
    grep -rl "RN-12" src test specs
    ```

=== "Windows (PowerShell)"
    ```powershell
    Get-ChildItem src, test, specs -Recurse -File | Select-String "RN-12" -List | Select-Object Path
    ```

A saída precisa incluir `src/frete.js`, `test/frete.test.js` e a `spec.md`. Os outros artefatos da pasta `specs` também aparecem, porque citam a regra. Feche com o commit final:

```bash
git add -A
git commit -m "frete implementado"
```

## Evidência a entregar

A tabela do Passo 3 com a resposta sobre as tarefas de teste, a saída final do `npm test` e a saída do Passo 6.

## Extensão: no seu repositório

No ramo descartável em que você rodou a extensão do exercício anterior, rode `plan` e `tasks` sobre a sua spec. Antes de implementar, marque no esqueleto as tarefas que tocam código existente: são elas que pedem parada humana.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
