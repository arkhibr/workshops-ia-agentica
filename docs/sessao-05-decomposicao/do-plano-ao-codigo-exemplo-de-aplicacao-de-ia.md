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

**O que o agente gerou.** O comando levou cerca de dois minutos e gerou, além do `plan.md`, quatro documentos de apoio: `research.md`, `data-model.md`, `contracts/` e `quickstart.md`, e dois trechos desses documentos interessam à sessão.

*Uma decisão de interface que o PO não tomou.* O `research.md` decidiu como o dinheiro entra na função:

```text
- Decision: valores em centavos inteiros (Number inteiro). Mínimo = 100000.
- Rationale: a borda de RN-01 é R$ 999,99 vs R$ 1.000,00. Em ponto
  flutuante, valores vindos de somas (0.1 + 0.2) podem cair em
  999.9999999 e recusar um pedido que deveria passar.
```

A justificativa técnica é consistente, mas a decisão muda o contrato da função: quem chama a função passa a enviar `100000` em vez de `1000`. O pedido do PO dizia que o valor "já chega calculado", sem dizer em que formato. A equipe que integra a função ao resto da plataforma precisa conhecer esse formato antes da implementação.

*O acréscimo da spec entrou no contrato.* No exemplo do Tema 1, o FR-003 acrescentou "quanto falta" à regra do mínimo. O `research.md` transformou o acréscimo em campos de retorno:

```text
- Decision: retorno estruturado { aceito, motivo?, minimoCentavos?,
  faltaCentavos?, mensagem? }. mensagem é montada com
  Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).
- Rationale: FR-003 / SC-003 pedem que o cliente saiba o mínimo e quanto
  falta.
```

Junto vieram a formatação monetária e uma nota sobre o espaço não separável que o `Intl` insere depois de `R$`, que os testes precisam respeitar, e nenhum desses itens constava do pedido do PO.

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

**O que o agente gerou.** O `tasks.md` saiu com 27 tarefas em 222 linhas, distribuídas nas fases da tabela abaixo:

| Fase | Tarefas | Conteúdo | Checkpoint |
|---|---|---|---|
| 1. Setup | T001 | Criar o `package.json` sem dependências | nenhum |
| 2. Foundational | T002–T004 | Módulo e arquivo de teste vazios, `npm test` conectado | `npm test` roda |
| 3. US1 (P1) 🎯 | T005–T009 | Testes da RN-01, ver falhar, implementar | regra do mínimo funciona para atacado |
| 4. US2 (P1) | T010–T013 | Testes da RN-02, ver falhar, implementar | MVP completo: atacado tem mínimo, padrão não |
| 5. US3 (P2) | T014–T022 | Testes da RN-03 e da RN-04, sabotagens para provar que detectam o erro | todas as regras com teste que já falhou |
| 6. Polish | T023–T027 | Conferir contrato, busca pelos IDs, ausência de dependências | nenhum |

O arquivo tem três pontos que interessam à sessão.

*O checkpoint que avisa um defeito.* O checkpoint da US1 diz:

```text
Checkpoint: regra do mínimo funciona para atacado. Atenção: neste ponto
um pedido padrão abaixo de R$ 1.000,00 também é recusado — a US2
corrige. Não entregar US1 sem US2 (ambas P1).
```

O agente separou as histórias para que o teste da RN-02 pudesse falhar antes do código, como manda o princípio II. Como consequência, existe um estado intermediário com defeito conhecido, que só é observado se houver uma parada humana nesse ponto.

*A tarefa composta.* A T008 tem um parágrafo inteiro. Ela cria a constante do mínimo, o formatador monetário, a função auxiliar de formatação, a comparação, o cálculo de `faltaCentavos` e a mensagem de recusa, e ainda instrui o agente a não incluir a checagem do tipo de cliente. A tarefa concentra seis decisões, duas delas originadas no acréscimo do FR-003, e por isso é a principal candidata a uma parada humana antes da execução.

*Os testes que passariam antes do código.* Os testes da RN-03 verificam que o desconto não muda o resultado, e o código da US1 já usa o valor antes do desconto. Esses testes passariam já na primeira execução, e o agente identificou o problema e criou tarefas de sabotagem:

```text
- T019 [US3] Provar que os testes RN-03: pegam o erro: em
  src/pedido-minimo.js, trocar temporariamente a base da comparação
  para pedido.valorAntesDescontoCentavos - (pedido.descontoCentavos ?? 0),
  rodar npm test, confirmar que [...] falham, e reverter a alteração.
```

É o problema da página de conceitos, resolvido de outro jeito: quando o teste não pode falhar antes do código, o código é quebrado de propósito para provar que o teste discrimina.

## Passo 3: implemente até a primeira história

Digite no chat do agente o comando `/speckit-implement`, seguido do ponto de parada:

```text
/speckit-implement Execute até o checkpoint da história US1 e pare.
```

**O que o agente gerou.** O comando levou menos de um minuto, marcou T001 a T009 como concluídas e parou com 3 testes passando. O relatório final repetiu o aviso do checkpoint:

```text
- Ainda não dá para entregar: neste ponto, um pedido de cliente padrão
  abaixo de R$ 1.000,00 também é recusado. Isso é esperado pelo plano:
  a verificação do tipo de cliente é a implementação da RN-02 e entra
  na US2 (T010–T013), depois que o teste dela falhar.
```

Um pedido de cliente padrão de R$ 50,00, nesse ponto, volta recusado com a mensagem "Faltam R$ 950,00".

## Passo 4: revise antes de seguir

Digite no terminal:

```bash
git status
git diff --stat
npm test
```

O `npm test` mostra 3 testes passando, todos com nome começando por `RN-01`. Esse é o ponto de controle humano que o modo básico não cria sozinho: quem revisa decide se o estado com defeito conhecido pode ser registrado em commit ou se as duas histórias precisam seguir juntas. Com a revisão feita, registre a parada:

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

**O que o agente gerou.** A segunda etapa levou menos de dois minutos e terminou com as 27 tarefas marcadas e 10 testes passando, todos com nome começando pelo ID da regra que verificam, de `RN-01` a `RN-04`. Dois registros do relatório final interessam.

A sabotagem da T020, que inseria um desconto padrão em pedidos sem desconto, não fez o teste da RN-04 falhar, porque o teste sempre informava um desconto. O agente acrescentou ao teste um pedido sem desconto e repetiu a sabotagem, que passou a ser detectada. Uma tarefa de verificação encontrou um teste fraco que a regra de ver o teste falhar não teria encontrado.

O agente também registrou que um tipo de cliente desconhecido, como `'Atacado'` com maiúscula, é aceito sem mínimo. Se o PO não concordar, falta uma regra nova, a RN-05.

## O que levar para o exercício

O plano e as tarefas carregam para o código tudo o que a spec deixou sem revisão, como o "quanto falta", que foi convertido em campo de retorno, formatação e teste. No exercício do frete, a classificação de três tarefas e a parada depois da primeira história são os dois momentos em que você pode interromper essa cadeia.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 07/10/2026. Outra execução produz texto diferente, e os pontos a observar costumam se repetir.

**Próxima página:** [Exercício de IA: do plano ao frete funcionando](do-plano-ao-codigo-exercicio.md).
