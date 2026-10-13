# Exercício de IA: do vermelho à fronteira do saldo

## Passo 1: retome a pasta do exercício anterior

Digite no terminal:

```bash
cd acme-saldo-rubrica
git log --oneline
```

O histórico precisa terminar no commit `plan e checklist` do exercício do Tema 1, sobre o saldo da rubrica no sistema de pagamentos de projetos de pesquisa da ACME, uma universidade fictícia, ou no commit `reserva de saldo pendente`, para quem o fez. Se o exercício anterior parou antes, rode no chat só os comandos que faltam, na ordem `/speckit-clarify`, `/speckit-plan` e `/speckit-checklist`, com um commit depois de cada um. No ensaio, esses três comandos somaram cerca de sete minutos de espera, que saem do tempo deste exercício. No Codex CLI, os comandos de chat deste exercício começam com cifrão (`$speckit-...`) no lugar da barra.

## Passo 2: gere as tarefas

Digite no chat do agente:

```text
/speckit-tasks
```

O `tasks.md` passa de duzentas linhas. Não leia o arquivo inteiro: procure só o título da seção de testes da primeira história, confira se ela vem antes da seção de implementação e registre as tarefas com os dois comandos abaixo:

```bash
git add -A
git commit -m "tasks"
```

## Passo 3: analise os artefatos

Digite no chat do agente:

```text
/speckit-analyze
```

Enquanto o relatório é gerado, anote a resposta à pergunta 1 da tabela do Passo 8. Quando ele terminar, confira no terminal que nenhum arquivo mudou:

```bash
git status
```

Se houver achado CRITICAL, peça ao agente a correção só desse achado, como no exemplo, e registre com `git commit -am "corrige achado critico"`. Os demais achados ficam anotados para a pergunta 2.

## Passo 4: implemente até o vermelho

Digite no chat do agente:

```text
/speckit-implement Execute só as fases de setup e fundação e as tarefas de teste da primeira história, e pare.
```

O `implement` vai parar na trava do checklist, porque os itens do `checklists/` gerado no Tema 1 estão desmarcados. Antes de responder, leia os itens que o agente destacar como lacunas que afetam os testes da primeira história e anote-os. Responda `sim` ou `yes`, conforme o idioma da pergunta, se nenhum deles mudar o que os testes da primeira história verificam, e `não` se algum mudar, levando o item ao PO antes de seguir.

## Passo 5: confira o vermelho

Digite no terminal:

```bash
npm test
```

Leia o resumo no fim da saída e o motivo das primeiras falhas. No ensaio deste exercício, feito em 13/10/2026, o resumo mostrou 52 testes com 46 passando e 6 falhando, e as 6 falhas eram `ERR_MODULE_NOT_FOUND`, porque os arquivos das regras da primeira história ainda não existiam, o que produz um vermelho fraco, já que nenhuma asserção da história chegou a executar. Se o seu vermelho tiver esse motivo, peça ao agente os esqueletos dos módulos, com funções que lancem um erro de não implementado, e rode `npm test` de novo até que as falhas venham das asserções ou dos esqueletos.

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

Todos os testes precisam passar, e o histórico precisa mostrar um commit de testes antes de cada commit de implementação.

## Passo 7: altere a fronteira

Na tabela de regras da `spec.md`, anote o ID da regra que exige saldo suficiente para a solicitação. Depois, localize essa regra no código, trocando `RN-03` pelo ID que você anotou.

=== "macOS/Linux"

    ```bash
    grep -rn "RN-03" src
    ```

=== "Windows (PowerShell)"

    ```powershell
    Get-ChildItem src -Recurse -File | Select-String "RN-03"
    ```

Abra no editor o arquivo que contém a comparação entre o valor do pagamento e o saldo, troque `<=` por `<` nessa comparação e salve. Se o agente escreveu a comparação ao contrário, com `>=` ou `>`, troque `>` por `>=`, que produz o mesmo efeito no valor exato do saldo, e rode a suíte com o comando abaixo:

```bash
npm test
```

Anote quantos testes falharam e o nome de um deles. Em seguida, desfaça a alteração e confirme que tudo voltou a passar:

```bash
git checkout -- src
npm test
```

No ensaio, a troca derrubou 3 dos 176 testes, entre eles "RN-03: aceita valor igual ao saldo disponível".

## Passo 8: responda a três perguntas

| # | Onde ler | Pergunta | Resposta |
|---|---|---|---|
| 1 | Seção de testes da primeira história no `tasks.md` | As tarefas de teste vêm antes das de implementação, com a indicação de que devem falhar? | sim / não |
| 2 | Relatório do `analyze` | Qual foi o achado de maior severidade, e ele trata da ordem entre teste e código, exigida pelo princípio II? | cite o ID e a severidade |
| 3 | Saídas dos Passos 5 e 7 | O vermelho falhou pelo motivo certo, e algum teste percebeu a troca do operador na fronteira do saldo? | motivo da falha / nome do teste ou "nenhum" |

Se nenhum teste falhou no Passo 7, a suíte não tem o caso do pagamento de valor igual ao saldo. Peça ao agente esse teste, confira que ele falha com `<` e passa com `<=`, e registre o resultado na pergunta 3.

## Evidência a entregar

A tabela do Passo 8 preenchida, a saída do `npm test` do Passo 5 e o nome do teste que falhou no Passo 7.

## Extensão: no seu repositório

Num ramo descartável de um repositório seu, escolha uma regra com limite numérico que já tenha testes. Troque o operador da comparação, rode a suíte e anote se algum teste falhou. Se nenhum falhar, escreva o teste do valor exato do limite e confira que ele falha antes de restaurar o operador.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
