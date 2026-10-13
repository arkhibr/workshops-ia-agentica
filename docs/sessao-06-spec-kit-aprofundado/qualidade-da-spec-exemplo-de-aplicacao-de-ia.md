# Exemplo de aplicação de IA: as perguntas da dupla aprovação

## Passo 1: crie a pasta do projeto

Digite no terminal:

```bash
mkdir fundep-dupla-aprovacao
cd fundep-dupla-aprovacao
git init
```

A pasta começa vazia, e todo o código vai sair do pedido do PO do sistema de pagamentos de projetos, um cenário inspirado no domínio administrativo e financeiro da FUNDEP.

## Passo 2: instale o Spec Kit no projeto

Digite no terminal:

```bash
specify init --here --force --integration claude
git add -A
git commit -m "spec kit instalado"
```

Quando o `specify init` perguntar o tipo de script, aperte Enter para aceitar o padrão do sistema. Cada passo deste roteiro termina com um commit, para que `git diff` mostre depois só o que o comando seguinte mudou, e o agente deve ser aberto dentro da pasta `fundep-dupla-aprovacao` antes do passo seguinte.

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

O comando levou cerca de 25 segundos e gravou o princípio II com a forma normativa do Spec Kit: "A implementação de uma história de usuário MUST começar somente depois que `npm test` for executado e mostrar os testes dessa história falhando (vermelho)."

## Passo 4: gere a spec a partir do pedido do PO

Digite no chat do agente o comando `/speckit-specify`, seguido do pedido do PO:

```text
/speckit-specify Sou PO do sistema de pagamentos de projetos da FUNDEP.
Todo pagamento feito com recurso de um projeto precisa ser aprovado antes
de ser liquidado. Pagamentos acima de R$ 5.000,00 precisam de duas
aprovações, exceto quando o fornecedor está na lista de fornecedores
recorrentes pré-aprovados, caso em que uma aprovação basta. Pagamentos
até esse valor precisam de uma aprovação. Quem solicitou o pagamento não
pode aprová-lo.
```

Depois, no terminal:

```bash
git add -A
git commit -m "spec da dupla aprovacao"
```

**O que o agente gerou:** o comando levou cerca de um minuto e meio e criou uma `spec.md` de 147 linhas com seis regras. Cinco delas têm origem no pedido do PO, e a sexta foi deduzida pelo agente:

```text
| RN-06 | Quando duas aprovações são exigidas, elas devem vir de duas pessoas
distintas; a mesma pessoa não conta duas vezes. | Derivada de RN-02 (sem
ela, a dupla aprovação perde o sentido) |
```

Na seção *Assumptions*, o agente decidiu duas questões que o pedido não tratava:

```text
- **Reprovação fora do escopo**: o pedido trata apenas de aprovações; o
  fluxo de reprovação ou cancelamento de pagamentos não faz parte desta
  feature.
- **Quem pode aprovar**: qualquer pessoa identificada, exceto o
  solicitante, pode aprovar; perfis, alçadas e vínculo do aprovador com
  o projeto ficam fora do escopo.
```

O pagamento fracionado ao mesmo fornecedor, para ficar abaixo do limite, não aparece em nenhum ponto da spec.

## Passo 5: esclareça a spec

Digite no chat do agente:

```text
/speckit-clarify
```

O agente faz uma pergunta por vez, e cada uma aceita como resposta a letra da opção, a palavra "yes" para aceitar a recomendação ou uma resposta curta. Quando o agente encerrar as perguntas, registre o resultado com os dois comandos abaixo:

```bash
git add -A
git commit -m "clarify"
```

**O que o agente gerou:** a primeira pergunta chegou em cerca de 20 segundos e tratou de uma lacuna que o pedido tinha e que ninguém havia apontado, o momento em que o sistema consulta a lista de recorrentes, aqui com as opções resumidas:

```text
**Question:** Quando o pedido é registrado e quando se verifica se o
pagamento pode ser liquidado, em qual desses momentos o sistema deve
olhar se o fornecedor está na lista de recorrentes pré-aprovados?

**Recommended:** Option C. É a opção mais conservadora. Hoje a spec usa
a opção A, e com ela basta incluir um fornecedor na lista depois do
pedido para dispensar a segunda aprovação, o que abre uma brecha no
controle.

| A | Só na verificação de liquidação. |
| B | Só no registro do pedido. |
| C | Nos dois momentos. Uma aprovação só basta se o fornecedor estava na
lista no registro e continua nela na liquidação. |
```

A resposta "C" fechou a brecha. A segunda pergunta pediu a confirmação da RN-06, que o agente havia deduzido, e a resposta "yes" a transformou em regra do PO. Depois disso, o agente encerrou com duas perguntas, antes do limite de cinco, com a justificativa de que "nada mais que ficou em aberto mudaria a implementação ou os testes", e gravou na spec a seção a seguir, aqui com o texto das perguntas encurtado:

```text
## Clarifications

### Session 2026-10-13

- Q: Em que momento o sistema verifica se o fornecedor está na lista de
  recorrentes pré-aprovados? → A: Em ambos: uma aprovação só basta se o
  fornecedor estava na lista no registro do pedido e continua nela na
  verificação de liquidação; caso contrário, exige duas.
- Q: Quando duas aprovações são exigidas, elas precisam vir de duas
  pessoas distintas, ambas diferentes do solicitante? (RN-06) → A: Sim.
```

A reprovação, quem pode aprovar e o fracionamento não foram perguntados. As duas primeiras já estavam decididas em *Assumptions*, e o `clarify` as tratou como resolvidas. O fracionamento não estava em lugar nenhum da spec, e por isso também não entrou na varredura.

## Passo 6: gere o plano e o checklist

Digite no chat do agente:

```text
/speckit-plan Node 20, node:test, sem dependências, uma função pura por regra.
```

Depois do commit do plano, digite:

```text
/speckit-checklist requisitos de aprovação de pagamento
```

E, no terminal:

```bash
git add -A
git commit -m "plan e checklist"
```

**O que o agente gerou:** o `plan` levou cerca de dois minutos e meio, e o `checklist` cerca de um minuto, que gravou o checklist em `checklists/aprovacao.md` com 39 itens, de `CHK001` a `CHK039`, todos desmarcados. Entre os itens que o agente destacou, três tratam de lacunas que a spec ainda tem depois do `clarify`:

```text
- CHK002: a spec não diz quem pode liquidar um pagamento.
- CHK012: a spec não diz se a lista de recorrentes é global ou por projeto.
- CHK027: a spec não cobre o fornecedor entrar ou sair da lista entre a
  primeira e a segunda aprovação.
```

Nenhum dos 39 itens pergunta se o código funciona, porque ainda não existe código. Todos perguntam se o requisito está escrito de forma completa e verificável.

## O que levar para o exercício

O exemplo mostra três achados que o exercício pede para procurar na própria spec: o `clarify` encontrou uma lacuna real e fez uma recomendação que alterou uma regra, deixou sem pergunta tudo o que o `specify` já tinha decidido em *Assumptions*, e o checklist apontou lacunas que continuavam na spec depois das duas respostas.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 13/10/2026. Outra execução produz texto e perguntas diferentes, e os três tipos de achado costumam se repetir.

**Próxima página:** [Exercício de IA: a spec do saldo da rubrica](qualidade-da-spec-exercicio.md).
