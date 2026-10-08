# Exemplo de aplicação de IA: a spec do pedido mínimo

## Passo 1: crie a pasta do projeto

Digite no terminal:

```bash
mkdir vetor-pedido-minimo
cd vetor-pedido-minimo
git init
```

A pasta começa vazia. Todo o código vai sair do pedido do PO.

## Passo 2: instale o Spec Kit no projeto

Digite no terminal:

```bash
specify init --here --force --integration claude
```

Quando o comando perguntar o tipo de script, aperte Enter para aceitar o padrão do sistema. Depois, registre a instalação:

```bash
git add -A
git commit -m "spec kit instalado"
```

Cada passo deste roteiro termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

Abra o agente dentro da pasta `vetor-pedido-minimo`.

## Passo 3: defina a constitution

Digite no chat do agente o comando `/speckit-constitution`, seguido dos três princípios:

```text
/speckit-constitution Três princípios, nada além deles.
I. Rastreabilidade: cada regra de negócio extraída do pedido do PO
recebe um ID RN-xx na spec, e esse ID é citado no requisito, no teste
e no comentário do código.
II. Testes antes do código: cada requisito funcional ganha um teste em
node:test que falha antes da implementação; npm test é o único comando
de verificação.
III. Sem dependências: o projeto usa só a biblioteca padrão do Node 20,
sem pacotes de terceiros.
```

Depois, no terminal:

```bash
git add -A
git commit -m "constitution"
```

**O que o agente gerou.** O comando levou cerca de 35 segundos. O agente gravou os três princípios em `.specify/memory/constitution.md` e acrescentou a cada um uma justificativa. A do princípio I diz para que serve o ID:

```text
**Por quê**: o PO precisa conseguir partir de uma frase do pedido dele e
chegar ao teste e ao código que a cumprem — e o caminho inverso, do
código até a regra, também precisa existir. Um `grep RN-07` resolve as
duas direções.
```

Ele também criou uma seção de governança com versionamento semântico da própria constitution, que ninguém pediu. A seção não muda nenhuma saída dos comandos seguintes, e por isso passa pelo critério da página de conceitos como decoração inofensiva. A pergunta para discussão é se ela é ganho ou ruído.

## Passo 4: gere a spec a partir do pedido do PO

Digite no chat do agente o comando `/speckit-specify`, seguido do pedido do PO em linguagem natural:

```text
/speckit-specify Sou PO da Vetor, plataforma de e-commerce B2B que vende
para dois tipos de cliente: padrão e atacado. Pedidos pequenos de atacado
não compensam o custo de separação, então queremos um pedido mínimo para
esses clientes. Um pedido de atacado precisa ter pelo menos R$ 1.000,00.
Cliente padrão continua sem mínimo. Para o mínimo, vale o valor do pedido
antes do desconto. O desconto já chega calculado em cada pedido, e a
verificação do mínimo não calcula desconto.
```

Depois, no terminal:

```bash
git add -A
git commit -m "spec do pedido minimo"
```

**O que o agente gerou.** O comando levou cerca de um minuto e criou a pasta `specs/001-pedido-minimo-atacado/` com uma `spec.md` de 111 linhas. Os pontos a observar estão em três trechos.

*O pedido virou regras com ID.* Por causa do princípio I, o agente abriu a spec com uma tabela que quebra o pedido em regras e guarda a frase de origem de cada uma:

```text
| ID | Regra | Origem no pedido do PO |
| RN-01 | Pedido de cliente de atacado só é aceito se o valor for **maior ou igual** a R$ 1.000,00. | "Um pedido de atacado precisa ter pelo menos R$ 1.000,00." |
| RN-03 | O valor comparado com o mínimo é o valor do pedido **antes** do desconto. | "Para o mínimo, vale o valor do pedido antes do desconto." |
```

A coluna de origem é o que permite ao PO conferir a tradução frase por frase. Nesta execução foram quatro regras, da RN-01 à RN-04.

*Requisito com ID e conteúdo a mais.* O FR-003 cita a RN-01, e a RN-01 não fala em "quanto falta":

```text
- FR-003 (RN-01): Ao recusar pedido de atacado por valor mínimo, o
  sistema MUST informar o valor mínimo exigido (R$ 1.000,00) e quanto
  falta para atingi-lo.
- SC-003: 100% das recusas por mínimo informam ao cliente o valor mínimo
  e quanto falta, permitindo que ele complete o pedido sem contatar o
  atendimento.
```

Uma verificação que só procura o ID aprova esse requisito. O PO pediu o mínimo, e o agente acrescentou o valor que falta, que exige outro cálculo e outra mensagem. O critério de sucesso SC-003 repete o acréscimo.

*Suposição que decide o negócio.* Na seção *Assumptions*:

```text
- "Valor do pedido antes do desconto" é a soma dos itens (preço ×
  quantidade), sem frete nem impostos destacados. Se a Vetor quiser
  incluir frete no cálculo, isso muda RN-03 e precisa ser revisto.
```

O PO não disse se o frete conta para o mínimo. O agente decidiu que não conta, e a decisão muda quais pedidos são aceitos. Ela volta para o PO antes do plano.

Na mesma seção, o agente se recusou a inventar uma regra para o tipo de cliente ausente ou desconhecido e registrou que o PO não definiu esse caso. É o princípio I funcionando: criar a regra exigiria um `RN-xx` sem frase de origem.

## O que levar para o exercício

Os três achados correspondem às três perguntas do exercício: requisito que diz mais que a frase do PO, decisão tomada fora do pedido e critério sem lastro. Nenhum deles impede o ciclo de seguir, e todos chegariam ao código se ninguém lesse as três seções.

Os trechos vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 07/10/2026. Outra execução produz texto diferente, e os pontos a observar costumam se repetir.

**Próxima página:** [Exercício de IA: especificar o frete da Vetor](especificacao-com-spec-kit-exercicio.md).
