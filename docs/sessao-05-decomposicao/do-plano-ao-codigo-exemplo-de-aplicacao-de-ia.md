# Exemplo de aplicação de IA: as tarefas do pedido mínimo

## Passo 1: gere o plano

Digite no chat do agente, aberto na pasta `vetor-pedido-minimo` do exemplo do Tema 1, o comando `/speckit-plan`, seguido das escolhas técnicas:

```text
/speckit-plan JavaScript ESM com Node 20, testes em node:test executados
por npm test, sem dependências. A validação fica em src/pedido-minimo.js.
```

Depois, no terminal:

```bash
git add -A
git commit -m "plano"
```

Cada passo deste roteiro termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

**O que o agente gerou.** O comando levou cerca de dois minutos e gerou, além do `plan.md`, quatro documentos de apoio: `research.md`, `data-model.md`, `contracts/` e `quickstart.md`. Dois pontos interessam aqui.

*O portão que passou por cima de um requisito.* A linha do princípio de rastreabilidade no *Constitution Check* diz:

```text
| I. Rastreabilidade | ... | Spec já cita RD-01/RN-01/RN-02 em
  FR-001..005. [...] | PASS |
```

A spec tem sete requisitos, e o FR-006 e o FR-007 não citam regra de origem. O portão contou só os cinco que citavam e aprovou. A pergunta para discussão é o que teria acontecido se o princípio fosse lido literalmente.

*O critério sem lastro virou contrato.* No exemplo do Tema 1, o SC-004 prometia informar ao cliente "o valor que falta atingir", coisa que nenhuma regra pedia. O `research.md` registrou a consequência:

```text
- Decision: retornar objeto. [...] Recusado: { aceito: false, motivo,
  minimo, falta }.
- Rationale: [...] `minimo` atende FR-004; `falta` atende SC-004 sem o
  chamador refazer a conta.
```

O campo `falta` trouxe junto uma decisão de arredondamento para centavos e a formatação monetária com `Intl.NumberFormat`. Nenhuma das três regras de origem fala de nada disso.

## Passo 2: gere as tarefas

Digite no chat do agente, sem argumentos:

```text
/speckit-tasks
```

Depois, no terminal:

```bash
git add -A
git commit -m "tarefas"
```

**O que o agente gerou.** O `tasks.md` saiu com 18 tarefas em 169 linhas. O esqueleto por fase:

| Fase | Tarefas | Conteúdo | Checkpoint |
|---|---|---|---|
| 1. Setup | T001 | Confirmar Node 20 e os 6 testes de desconto | nenhum |
| 2. Foundational | T002–T005 | Teste e código da entrada inválida (FR-006) | módulo recusa entrada inválida |
| 3. US1 + US2 (P1) 🎯 | T006–T011 | Testes de RN-01 e RD-01, ver falhar, implementar | MVP: RN-01 medida como RD-01 manda |
| 4. US3 (P2) | T012–T015 | Testes de RN-02, ver falhar, implementar | as três histórias verdes |
| 5. Polish | T016–T018 | Diff vazio nos arquivos antigos, rastreabilidade, verificação final | nenhum |

Seis das dezoito tarefas só rodam `npm test`. Três delas esperam falha (T003, T008, T013) e provam que o teste discrimina. As outras três esperam sucesso e funcionam como critério de aceitação da tarefa anterior.

O arquivo tem três pontos que interessam à sessão.

*A tarefa composta.* A T009 tem um parágrafo inteiro. Ela cria o formatador monetário, implementa o ramo do atacado, decide que "pelo menos" vira `<` na comparação, calcula `falta` com arredondamento e escreve a mensagem de recusa com o comentário `FR-004 / SC-004`. São cinco decisões numa tarefa, e duas delas vêm do critério sem lastro. Ela é a candidata natural a uma parada humana antes da execução.

*O critério que nasceria verde.* O template pede uma fase por história, e o agente juntou US1 e US2 numa fase só. A justificativa ficou registrada no arquivo:

```text
Consequência: se os testes RD-01 forem escritos depois da implementação
de RN-01, passam na primeira execução e nunca são vistos falhando, o
que viola o Princípio II para FR-001.
```

É o problema da página de conceitos, encontrado pelo próprio agente porque a constitution exigia ver o teste falhar. Sem o princípio II, as duas histórias teriam ficado separadas e os testes da RD-01 passariam sem nunca terem falhado.

*O requisito sem dono virou fundação.* O FR-006, que não tem regra de origem, ocupa a fase *Foundational* inteira e é executado antes de qualquer história. A decisão sobre entrada inválida, que nenhum dono de regra tomou, é a primeira coisa a virar código.

## Passo 3: implemente até a primeira história

Digite no chat do agente o comando `/speckit-implement`, seguido do ponto de parada:

```text
/speckit-implement Execute até o checkpoint da história US1 e pare.
```

**O que o agente gerou.** O comando levou um minuto e meio, marcou T001 a T011 como concluídas no `tasks.md` e parou. Criou `src/pedido-minimo.js` e `test/pedido-minimo.test.js` e não tocou nos arquivos de desconto.

## Passo 4: revise antes de seguir

Digite no terminal:

```bash
git status
git diff --stat
npm test
```

O `npm test` mostra 15 testes passando. Esse é o ponto de controle humano que o modo básico não cria sozinho: o diff e os testes passam por revisão antes da segunda chamada. Com a revisão feita, registre a parada:

```bash
git add -A
git commit -m "pedido minimo: historia US1"
```

## Passo 5: implemente o restante

Digite no chat do agente:

```text
/speckit-implement Execute as fases restantes.
```

Depois, no terminal:

```bash
npm test
git add -A
git commit -m "pedido minimo implementado"
```

**O que o agente gerou.** A segunda etapa levou menos de um minuto e terminou com 18 testes passando: os 6 de desconto, que já existiam, e 12 novos. Dez dos testes novos começam pelo ID da regra que verificam. Os outros dois começam por `FR-006`, o requisito sem regra de origem.

## O que levar para o exercício

O plano e as tarefas carregam para o código tudo o que a spec deixou passar. No exercício do frete, a classificação de três tarefas e a parada depois da primeira história são os dois momentos em que você pode interromper essa cadeia.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 07/10/2026. Outra execução produz texto diferente, e os pontos a observar costumam se repetir.

**Próxima página:** [Exercício de IA: do plano ao frete funcionando](do-plano-ao-codigo-exercicio.md).
