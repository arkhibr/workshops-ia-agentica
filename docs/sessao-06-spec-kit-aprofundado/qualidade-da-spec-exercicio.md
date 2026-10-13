# Exercício de IA: a spec do saldo da rubrica

## Passo 1: crie a pasta do projeto

Digite no terminal:

```bash
mkdir acme-saldo-rubrica
cd acme-saldo-rubrica
git init
```

O exercício parte de um pedido do PO do sistema de pagamentos de projetos de pesquisa da ACME, uma universidade fictícia, sobre o saldo de cada rubrica do plano de trabalho.

## Passo 2: instale o Spec Kit no projeto

Digite no terminal o comando da sua ferramenta e registre a instalação:

```bash
specify init --here --force --integration claude
git add -A
git commit -m "spec kit instalado"
```

No Codex CLI, troque `claude` por `codex` no `specify init` e use os comandos dos próximos passos com cifrão (`$speckit-...`) no lugar da barra. Abra o agente dentro da pasta `acme-saldo-rubrica` antes de seguir.

## Passo 3: defina a constitution

Digite no chat do agente o comando `/speckit-constitution`, seguido dos três princípios:

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

Depois, no terminal:

```bash
git add -A
git commit -m "constitution"
```

## Passo 4: gere a spec a partir do pedido do PO

Digite no chat do agente o comando `/speckit-specify`, seguido do pedido do PO:

```text
/speckit-specify Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME.
Cada projeto tem rubricas, como material de consumo, serviços de
terceiros e diárias, e cada rubrica tem um valor aprovado no plano de
trabalho. Um pagamento só pode ser solicitado se a rubrica tiver saldo
para ele. O saldo da rubrica é o valor aprovado menos os pagamentos já
liquidados.
```

O agente cria a pasta `specs/001-...` com a `spec.md` e pode terminar com uma pergunta, como "Sua escolha: responda, por exemplo, 'P1: B'", sobre um ponto que marcou como `[NEEDS CLARIFICATION]`. Se isso acontecer, não responda a essa pergunta, porque ela é a matéria do `clarify` no passo seguinte. Não leia o arquivo inteiro, porque as perguntas do Passo 7 indicam as seções a ler, e registre a spec com os dois comandos abaixo antes do passo seguinte:

```bash
git add -A
git commit -m "spec do saldo"
```

## Passo 5: esclareça a spec

Digite no chat do agente:

```text
/speckit-clarify
```

Responda a cada pergunta como o PO responderia, com base só no pedido do Passo 4. Antes de aceitar uma recomendação, confira se ela altera alguma frase do pedido. Se alterar, responda com a opção que preserva o pedido ou com uma resposta curta sua, e anote a pergunta para o Passo 7. Quando o agente encerrar as perguntas, registre o resultado e veja o tamanho da alteração com os três comandos abaixo:

```bash
git add -A
git commit -m "clarify"
git diff HEAD~1 --stat
```

O `git diff` mostra quantas linhas da spec o `clarify` alterou a partir das suas respostas.

## Passo 6: gere o plano e o checklist

Digite no chat do agente:

```text
/speckit-plan Node 20, node:test, sem dependências, uma função pura por regra.
```

Enquanto o plano é gerado, avance para o Passo 7 nas perguntas que dependem só da spec. Depois do plano, digite:

```text
/speckit-checklist requisitos de saldo de rubrica
```

Se o agente fizer perguntas para delimitar o checklist, sobre foco, profundidade ou público, responda com a opção recomendada ou com a palavra "padrão".

E registre os dois artefatos:

```bash
git add -A
git commit -m "plan e checklist"
```

## Passo 7: responda a três perguntas

Leia só as seções indicadas na tabela.

| # | Onde ler | Pergunta | Resposta |
|---|---|---|---|
| 1 | `## Clarifications` da `spec.md` | O `clarify` perguntou se um pagamento solicitado e ainda não liquidado reserva saldo da rubrica? Se não perguntou, essa decisão aparece em *Assumptions*? | perguntou / respondida no specify / decidido em *Assumptions* / ausente |
| 2 | Sua anotação do Passo 5 | Qual recomendação do agente você recusou, ou qual aceitou mesmo alterando uma frase do pedido, e por quê? | cite a pergunta e a frase do pedido |
| 3 | `checklists/` | Qual item do checklist aponta algo que a spec ainda não decide, e quem precisa decidir? | cite o `CHK` e quem decide |

Se a resposta 1 for "ausente", acrescente você mesmo à spec, em *Assumptions*, a pergunta sobre a reserva de saldo como pendência do PO, e registre com `git commit -am "reserva de saldo pendente"`. Sem essa decisão, dois pagamentos solicitados ao mesmo tempo podem consumir o mesmo saldo.

No ensaio deste exercício, feito em 13/10/2026, o próprio `specify` marcou a reserva de saldo como `[NEEDS CLARIFICATION]`, e a recomendação do `clarify` mudava a fórmula do saldo escrita pelo PO, de "aprovado menos liquidados" para "aprovado menos liquidados menos solicitados pendentes".

## Evidência a entregar

A tabela do Passo 7 preenchida e a saída do `git diff HEAD~1 --stat` do Passo 5. A spec, o plano e o checklist continuam na pasta, porque o exercício do Tema 2 parte deles.

## Extensão: no seu repositório

Num ramo descartável de um repositório seu, rode `/speckit-clarify` sobre uma spec que já exista ou sobre uma gerada com um pedido seu de três a cinco frases. Compare as perguntas que o agente fez com as decisões que estavam em *Assumptions* antes do comando e anote quais delas nenhuma pergunta alcançou.

**Próxima página:** [Teste antes do código: analyze e teste vermelho](teste-antes-do-codigo-conceitos.md).
