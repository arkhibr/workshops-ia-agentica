# Exercício de IA: especificar o frete da Vetor

## Passo 1: baixe o projeto da Vetor

Digite no terminal para baixar o projeto de exemplo da Vetor, plataforma fictícia de e-commerce B2B do workshop, e conferir os testes:

```bash
npx degit arkhibr/workshops-ia-agentica/exemplo/vetor vetor-frete
cd vetor-frete
npm test
```

O `npm test` precisa mostrar 6 testes passando.

## Passo 2: registre o estado inicial

Digite no terminal:

```bash
git init
git add -A
git commit -m "estado inicial"
```

Cada passo deste exercício termina com um commit. Os comandos do Spec Kit criam e reescrevem arquivos, e o commit separa o que cada comando produziu: depois do comando seguinte, `git diff` mostra só o que ele mudou. Se o resultado de um comando não servir, o commit anterior é o ponto para onde voltar.

## Passo 3: instale o Spec Kit no projeto

Digite no terminal, trocando `claude` por `codex` ou `copilot` conforme o seu agente:

```bash
specify init --here --force --integration claude
```

Quando o comando perguntar o tipo de script, aperte Enter para aceitar o padrão do sistema. Depois, registre a instalação:

```bash
git add -A
git commit -m "spec kit instalado"
```

Abra o agente dentro da pasta `vetor-frete`. No Codex, os comandos dos próximos passos começam com cifrão (`$speckit-...`) em vez de barra.

## Passo 4: defina a constitution

Digite no chat do agente o comando `/speckit-constitution`, seguido dos três princípios:

```text
/speckit-constitution Três princípios, nada além deles.
I. Rastreabilidade: toda regra de negócio implementada cita o ID de
origem (RC-xx, RD-xx ou RN-xx) no requisito, no teste e no comentário
do código.
II. Testes antes do código: cada requisito funcional ganha um teste em
node:test que falha antes da implementação; npm test é o único comando
de verificação.
III. Sem dependências: o projeto continua sem pacotes de terceiros e
usa só a biblioteca padrão do Node 20.
```

Depois, no terminal:

```bash
git add -A
git commit -m "constitution"
```

## Passo 5: gere a spec

Digite no chat do agente o comando `/speckit-specify`, seguido do nome da feature e das quatro regras de origem:

```text
/speckit-specify Cálculo de frete da Vetor. Regras de origem:
RD-11: Valor de referência do frete é o valor total do pedido menos
o desconto calculado pela regra de desconto vigente.
RN-11: O frete de um pedido é de R$ 80,00, salvo quando outra regra
deste mapa se aplicar.
RN-12: O frete de um pedido de cliente atacado é zero quando o valor
de referência ultrapassa R$ 3.000,00.
RN-13: O frete de um pedido de cliente padrão é de R$ 40,00 quando o
valor de referência ultrapassa R$ 5.000,00.
```

O agente cria a pasta `specs/001-...` com a `spec.md`. Não leia o arquivo inteiro.

## Passo 6: confira três pontos

Abra a `spec.md` e leia só as seções indicadas.

| # | Seção | Pergunta | Resposta |
|---|---|---|---|
| 1 | *Functional Requirements* | Todo `FR` cita um ID de origem (`RD-11`, `RN-11`...)? | sim / não: qual `FR` |
| 2 | *Assumptions* e *Edge Cases* | Algum item decide o que as regras não fixaram, como o valor exato do limite ou o arredondamento? | nenhum / cite o item |
| 3 | *Success Criteria* | Algum `SC` não tem origem nas quatro regras? | nenhum / cite o `SC` |

Depois, procure na história do atacado um cenário em que o valor total passa de R$ 3.000,00 e o valor de referência não. Um pedido de atacado de R$ 3.000,00, por exemplo, tem desconto de R$ 300,00, referência de R$ 2.700,00 e paga R$ 80,00. Se a spec não tiver nenhum cenário desse tipo, anote: é a armadilha que a RD-11 cria.

## Passo 7: registre a spec

Digite no terminal:

```bash
git add -A
git commit -m "spec do frete"
```

## Evidência a entregar

A tabela do Passo 6 preenchida e a observação sobre o pedido de R$ 3.000,00. A spec continua no projeto, porque o exercício da segunda metade parte dela.

## Extensão: no seu repositório

Escolha uma regra de negócio pequena de um sistema seu, com no máximo três regras de origem. Num ramo descartável do repositório, rode os Passos 3 a 6 com essas regras. Compare as suposições que o agente registrou com o que você sabe do negócio.

**Próxima página:** [Conceitos: do plano ao código](do-plano-ao-codigo-conceitos.md).
