# Exemplo de aplicação de IA: a spec do pedido mínimo

Esta demonstração aplica a constitution e a spec do GitHub Spec Kit a uma feature pequena da Vetor, a plataforma fictícia de e-commerce B2B do workshop: o pedido mínimo para clientes de atacado. Os trechos abaixo vêm de uma execução real com Spec Kit 1.1.1 e Claude Code, em 07/10/2026. Outra execução produz texto diferente, e os pontos a observar costumam se repetir.

## As regras de origem

```text
RD-01: Valor do pedido, para efeito de pedido mínimo, é o valor total
       antes do desconto.
RN-01: É obrigatório que pedido de cliente atacado tenha valor do
       pedido de pelo menos R$ 1.000,00.
RN-02: Pedido de cliente padrão não tem valor mínimo.
```

O projeto de partida é o mesmo do exercício: o exemplo da Vetor, que só calcula desconto. A constitution usada é a do [exercício](especificacao-com-spec-kit-exercicio.md#passo-3-constitution), com os princípios de rastreabilidade, teste antes do código e nenhuma dependência.

## A constitution gerada

O comando levou cerca de 40 segundos. O agente escreveu os três princípios pedidos e acrescentou, a cada um, um parágrafo de justificativa:

```text
### II. Testes antes do código

Cada requisito funcional MUST ganhar um teste em `node:test` escrito
antes da implementação, e esse teste MUST ser visto falhando antes de o
código existir. [...]

Por quê: teste que nunca falhou não prova nada sobre o código que diz
cobrir.
```

Ele também criou uma seção de governança com versionamento semântico da própria constitution, que ninguém pediu. A seção não muda nenhuma saída dos comandos seguintes, e por isso passa pelo critério da página de conceitos como decoração inofensiva. A pergunta para discussão é se ela é ganho ou ruído.

## A spec gerada

O `specify` levou cerca de um minuto e meio e produziu uma `spec.md` de pouco mais de cem linhas. Os pontos a observar estão em três trechos.

**O caso que a RD-01 existe para pegar.** O agente transformou a regra de derivação numa história própria, com o exemplo que separa as duas leituras possíveis:

```text
1. Given um cliente atacado, When ele submete um pedido de R$ 1.050,00
   que recebe R$ 52,50 de desconto, Then o pedido é aceito, porque o
   valor considerado é R$ 1.050,00 (RD-01).
```

É o resultado esperado de uma regra bem decomposta: a RD-01 virou um cenário que falha se alguém usar o valor líquido.

**Requisitos sem origem.** A constitution exige ID em todo requisito que implementa regra de negócio, e dois requisitos saíram sem:

```text
- FR-006: O sistema MUST recusar como entrada inválida valor de pedido
  negativo ou não numérico, de forma distinguível da recusa por pedido
  mínimo.
- FR-007: A verificação de pedido mínimo MUST NOT alterar o cálculo de
  desconto existente.
```

O FR-007 é uma proteção técnica contra regressão e pode ficar sem ID. O FR-006 decide como o sistema responde a uma entrada que o mapa não previa, e essa decisão pode afetar a mensagem que o cliente vê. Fica em aberto se ele precisa de uma regra de origem.

**Critério que diz mais que o requisito.** Compare:

```text
- FR-004 (RN-01): Ao recusar um pedido pelo mínimo, o sistema MUST
  informar o motivo, incluindo o valor mínimo exigido (R$ 1.000,00).
- SC-004: Toda recusa por mínimo deixa claro para o cliente o valor
  que falta atingir, sem precisar consultar outra fonte.
```

O requisito pede o mínimo exigido. O critério de sucesso pede o valor que falta, que é outra informação e exige outro cálculo. Nenhuma das três regras fala disso. Se o critério ficar, o plano vai tentar cumpri-lo e alguém vai implementar uma mensagem que o negócio não pediu.

## O que levar para o exercício

Os três achados correspondem às três perguntas do exercício: requisito sem origem, decisão tomada fora do mapa de regras e critério sem lastro. Nenhum deles impede o ciclo de seguir, e todos chegariam ao código se ninguém lesse as três seções.

**Próxima página:** [Exercício de IA: especificar o frete da Vetor](especificacao-com-spec-kit-exercicio.md).
