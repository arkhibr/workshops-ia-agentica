# Exemplo de aplicação de IA: do analyze ao verde na dupla aprovação

## Passo 1: gere as tarefas

Digite no chat do agente, dentro da pasta `fundep-dupla-aprovacao` do exemplo do Tema 1:

```text
/speckit-tasks
```

Depois, no terminal:

```bash
git add -A
git commit -m "tasks"
```

**O que o agente gerou:** o comando levou pouco mais de três minutos e gravou 46 tarefas em 282 linhas, para o pedido de dupla aprovação de pagamentos, cenário inspirado no domínio da FUNDEP. Por causa do princípio II da constitution, cada uma das três histórias ganhou uma seção de testes antes da seção de implementação, com o aviso de que os testes devem falhar, como no trecho da primeira história:

```text
### Tests for User Story 1 (escrever primeiro; devem FALHAR) ⚠️

- [ ] T010 [P] [US1] Criar `tests/regras/rn-04.test.js` com
  `describe('RN-04 exigenciaAteLimite', ...)`: `500_000` → `1` (limite
  inclusivo); `500_001` → `null`; e `LIMITE_CENTAVOS === 500_000`
- [ ] T014 [US1] Registrar o vermelho: npm test, confirmar código de
  saída ≠ 0
```

## Passo 2: analise os artefatos

Digite no chat do agente:

```text
/speckit-analyze
```

Ao final, confira no terminal que nenhum arquivo mudou:

```bash
git status
```

**O que o agente gerou:** o comando levou cerca de um minuto e meio, o `git status` voltou sem nenhum arquivo alterado, e o relatório trouxe 14 achados, dois deles CRITICAL. Os dois tratam da ordem exigida pelo princípio II, e o C2 aponta um teste que passaria antes de existir código da história:

```text
| C2 | Constituição (II) | CRITICAL | tasks.md:L63 (T004), L87 (T010) |
`LIMITE_CENTAVOS = 500_000` entra com o valor real na fase Foundational,
antes do vermelho da US1. A asserção `LIMITE_CENTAVOS === 500_000` do
T010 já nasce verde. |
| C3 | Constituição (II) | HIGH | tasks.md:L155 (T036) | Com o código da
US2, os cenários US3-2, US3-3, US3-4 [...] já passam. [...] um teste que
nasce verde não prova nada. |
```

O relatório termina com a pergunta "Quer que eu sugira as edições concretas para os 5 problemas principais? Não vou aplicar nada sem sua aprovação."

## Passo 3: aprove só as correções críticas

Digite no chat do agente:

```text
Aplique só as correções de C1 e C2 no tasks.md.
```

E registre a correção:

```bash
git add -A
git commit -m "corrige C1 e C2 do analyze"
```

**O que o agente gerou:** a correção levou cerca de 40 segundos e alterou quatro linhas do `tasks.md`, com a constante do limite criada sem valor na fundação e o valor definido só na implementação da primeira história. O C3 ficou em aberto, porque a pergunta foi respondida apenas para os dois achados críticos.

## Passo 4: implemente até o vermelho

Digite no chat do agente:

```text
/speckit-implement Execute só as fases de setup e fundação e as tarefas de teste da primeira história, e pare.
```

**O que o agente gerou:** antes de qualquer tarefa, o `implement` leu os checklists e parou na trava, depois de cerca de 25 segundos:

```text
| Checklist | Total | Marcados | Desmarcados | Status |
| requirements.md | 19 | 18 | 1 | ✗ FAIL |
| aprovacao.md | 39 | 0 | 39 | ✗ FAIL |

**Quer que eu siga com a implementação mesmo assim? (sim/não)**
```

Os 39 itens desmarcados são os do checklist gerado no exemplo do Tema 1, e nenhum deles muda os testes da primeira história. Responda no chat:

```text
sim
```

O agente levou mais dois minutos, criou a estrutura do projeto, os esqueletos das funções e os testes da primeira história, e fez dois commits, um para a estrutura e outro com o título `test(US1): cenários RN-01, RN-04, RN-05 em vermelho`.

## Passo 5: confira o vermelho

Digite no terminal:

```bash
npm test
```

**O que o terminal mostrou:** 34 testes em 5 suítes, nenhum passando, e saída com código 1. A maior parte das falhas tem a mensagem `Error: não implementado`, que vem dos esqueletos das funções, e o teste do limite falha por asserção:

```text
✖ RN-04: LIMITE_CENTAVOS é R$ 5.000,00 (500_000 centavos)
  AssertionError [ERR_ASSERTION]: Expected values to be strictly equal:
  + undefined
  - 500000
```

As duas falhas têm o motivo certo para esta etapa: as funções ainda não existem, e o valor do limite ainda não foi definido, como pediu a correção do C2. Uma falha por `ERR_MODULE_NOT_FOUND` ou por erro de digitação no nome de uma função indicaria problema no teste, e o próprio agente registrou que nenhuma delas apareceu.

## Passo 6: implemente até o verde

Digite no chat do agente:

```text
Continue o implement até o fim, sem parar entre as histórias.
```

Depois, no terminal:

```bash
npm test
git log --oneline
```

**O que o terminal mostrou:** depois de pouco mais de três minutos, 57 testes, todos passando, e o histórico com um commit de testes em vermelho antes de cada commit de implementação:

```text
07fab27 feat(US3): exceção para fornecedores recorrentes (RN-03)
a876a1f test(US3): cenários RN-03 em vermelho
2c8d28d feat(US2): dupla aprovação acima de R$ 5.000,00 (RN-02, RN-06)
b436858 test(US2): cenários RN-02, RN-06 em vermelho
9decb87 feat(US1): aprovação simples e bloqueio de liquidação (RN-01, RN-04, RN-05)
4336b06 test(US1): cenários RN-01, RN-04, RN-05 em vermelho
```

No fim da execução, o agente registrou: "Três cenários da US3 já nasceram verdes. US3-2, US3-3 e US3-4 passaram antes da implementação da RN-03, porque o que verificam [...] já existia da US1 e da US2." Esse é o achado C3 do `analyze`, que ficou sem correção no Passo 3 e se confirmou na execução.

## O que levar para o exercício

O `analyze` previu, antes da execução, os dois casos de teste que nascem verde, e o achado que não foi corrigido apareceu de novo no fim do `implement`. O vermelho do Passo 5 foi conferido pelo motivo das falhas, uma a uma, e o exercício acrescenta uma verificação depois do verde, com a troca do operador da comparação de fronteira.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 13/10/2026, com os blocos de tarefas e de achados encurtados. Outra execução produz números e achados diferentes, e os tipos de achado costumam se repetir.

**Próxima página:** [Exercício de IA](teste-antes-do-codigo-exercicio.md).
