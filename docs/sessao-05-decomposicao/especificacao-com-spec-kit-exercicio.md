# Exercício de IA: especificar o frete da Vetor

## Passo 1: crie a pasta do projeto

Digite no terminal:

```bash
mkdir vetor-frete
cd vetor-frete
git init
```

A pasta começa vazia. Todo o código vai sair do pedido do PO.

## Passo 2: instale o Spec Kit no projeto

Digite no terminal, trocando `claude` por `codex` ou `copilot` conforme o seu agente:

```bash
specify init --here --force --integration claude
```

Quando o comando perguntar o tipo de script, aperte Enter para aceitar o padrão do sistema. Depois, registre a instalação:

```bash
git add -A
git commit -m "spec kit instalado"
```

Cada passo deste exercício termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

Abra o agente dentro da pasta `vetor-frete`. No Codex, os comandos dos próximos passos começam com cifrão (`$speckit-...`) em vez de barra.

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

## Passo 4: gere a spec a partir do pedido do PO

Digite no chat do agente o comando `/speckit-specify`, seguido do pedido do PO em linguagem natural:

```text
/speckit-specify Sou PO da Vetor, plataforma de e-commerce B2B que vende
para dois tipos de cliente: padrão e atacado. Precisamos calcular o frete
de cada pedido. O frete normal é de R$ 80,00. Para incentivar pedidos
maiores, o cliente de atacado não paga frete quando o pedido passa de
R$ 3.000,00, e o cliente padrão paga R$ 40,00 quando o pedido passa de
R$ 5.000,00. Para essas faixas, vale o valor do pedido depois do desconto.
O desconto já chega calculado em cada pedido, e o frete não calcula desconto.
```

O agente cria a pasta `specs/001-...` com a `spec.md`. Não leia o arquivo inteiro.

## Passo 5: confira três pontos

Abra a `spec.md` e leia só as seções indicadas.

| # | Seção | Pergunta | Resposta |
|---|---|---|---|
| 1 | Tabela de regras e *Functional Requirements* | Algum `FR` não cita um `RN-xx`, ou diz mais do que a frase do PO que a regra registra? | nenhum / cite o `FR` |
| 2 | *Assumptions* e *Edge Cases* | Algum item decide o que o PO não disse, como o valor exato do limite ou o que fazer com entrada inválida? | nenhum / cite o item |
| 3 | *Success Criteria* | Algum `SC` não tem origem no pedido do PO? | nenhum / cite o `SC` |

Depois, procure na história do atacado um cenário em que o valor do pedido passa de R$ 3.000,00 e o valor depois do desconto não. Um pedido de atacado de R$ 3.500,00 com R$ 600,00 de desconto, por exemplo, fica em R$ 2.900,00 e paga R$ 80,00. Se a spec não tiver nenhum cenário desse tipo, anote: é o caso que a frase "vale o valor do pedido depois do desconto" existe para pegar.

Anote também o ID que a spec deu à regra do frete grátis do atacado. O exercício da segunda metade procura esse ID no código.

## Passo 6: registre a spec

Digite no terminal:

```bash
git add -A
git commit -m "spec do frete"
```

## Evidência a entregar

A tabela do Passo 5 preenchida, a observação sobre o cenário do desconto e o ID da regra do frete grátis do atacado. A spec continua no projeto, porque o exercício da segunda metade parte dela.

## Extensão: no seu repositório

Escreva, como PO, um pedido de três a cinco frases para uma regra de negócio pequena de um sistema seu. Num ramo descartável do repositório, rode os Passos 2 a 5 com esse pedido. Compare a tabela de regras e as suposições que o agente registrou com o que você sabe do negócio.

**Próxima página:** [Conceitos: do plano ao código](do-plano-ao-codigo-conceitos.md).
