# Exemplo de aplicação de IA: decomposição de um ninho de regras de IRPF

Esta demonstração usa o cálculo do Imposto de Renda da Pessoa Física (IRPF) como domínio conhecido, sem reproduzir a legislação vigente. O objetivo é observar uma política confusa sendo separada em conceitos, fatos, regras, tabela de decisão e testes, com o vocabulário do SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG para vocabulário e regras de negócio).

!!! warning "Exemplo fictício"
    Todos os limites, percentuais e valores monetários desta página são **valores hipotéticos** criados para a aula, diferentes da tabela vigente do IRPF, e o exemplo **não é orientação tributária** nem calculadora fiscal.

## O ninho de regras

> Para calcular o imposto mensal, considere os rendimentos recebidos no mês, mas retire os valores isentos e também as deduções aceitas, sendo que dependente vale R$ 200 por pessoa e despesas de saúde entram pelo valor comprovado, com o total das deduções, tirando saúde, limitado a R$ 1.000. Se depois disso a base ficar até R$ 2.500 não há imposto, e passando disso até R$ 4.000 cobra-se 10% só do que passou de R$ 2.500, e acima de R$ 4.000 cobra-se R$ 150 mais 20% do excedente, e o imposto devido no mês é o calculado menos o que já foi retido, sem gerar imposto negativo, e quem tiver moléstia grave não paga sobre proventos de aposentadoria desde que exista laudo válido no mês.

O parágrafo mistura definições, fórmula, faixas, teto, exceção documental e compensação. Um pedido para que o agente “transforme isso em regra”, sem contrato de saída, deixa o formato da resposta a critério do modelo e admite como resposta uma paráfrase do parágrafo, sem identificadores, evidência ou tipo de regra que um teste consiga verificar.

![À esquerda, o ninho de regras aparece como um único bloco de texto com trechos de cores diferentes. Uma seta de decomposição leva a oito cartões: 8 conceitos e 6 tipos de fato (Passo 1), 2 classificações RC e 6 derivações RD (Passo 2), 2 regras operativas RN candidatas (Passo 3), precedência em 6 etapas inferidas (Passo 4), 3 faixas F na tabela de decisão (Passo 5) e 1 lacuna de arredondamento (Passo 6). Os cartões convergem para 5 casos de fronteira.](assets/ninho-irpf.png)

*Leitura da figura: cada cartão corresponde a um passo desta página e traz a quantidade de itens que o passo extrai do parágrafo. A borda contínua marca regra extraída do texto, a tracejada marca inferência que aguarda o especialista e a pontilhada marca a lacuna registrada como pergunta.*

## Passo 1 — conceitos e fatos

| Conceito | Definição neste exemplo |
|---|---|
| Rendimento Isento | Rendimento que a política retira da base por classificação expressa |
| Rendimento Tributável | Rendimento recebido no mês que não é Rendimento Isento |
| Dedução Aceita | Valor que a política permite retirar dos rendimentos tributáveis |
| Base de Cálculo | Valor usado para selecionar a faixa e calcular o imposto bruto |
| Imposto Bruto | Valor produzido pela tabela progressiva antes da retenção |
| Imposto Retido | Valor já recolhido no mês |
| Imposto Devido | Resultado final, limitado a zero |
| Laudo Válido | Documento vigente no mês de cálculo |

Os tipos de fato que ligam esses conceitos são:

- Pessoa recebe Rendimento
- Rendimento possui Classificação
- Pessoa possui Dependente
- Despesa de Saúde possui Comprovante
- Laudo possui Período de Validade
- Imposto Retido reduz Imposto Bruto

## Passo 2 — regras estruturais

Quase todo o ninho é estrutural. Excluir rendimento isento, limitar deduções e compensar retenção são passos de cálculo ou critérios de inclusão, e nenhum deles descreve a conduta de um ator que poderia descumpri-los.

| ID | Tipo | Sentença | Evidência | Confiança |
|---|---|---|---|---|
| RC-01 | Classificação | Provento de aposentadoria recebido por pessoa com moléstia grave e laudo válido no mês é Rendimento Isento. | “não paga sobre proventos de aposentadoria desde que exista laudo válido no mês” | alta dentro do cenário fictício |
| RC-02 | Classificação | Rendimento recebido no mês que não é Rendimento Isento é Rendimento Tributável. | “considere os rendimentos recebidos no mês, mas retire os valores isentos” | alta |
| RD-01 | Derivação | A Dedução por Dependentes é a quantidade de dependentes multiplicada por R$ 200. | “dependente vale R$ 200 por pessoa” | alta |
| RD-02 | Derivação | A Dedução de Saúde é a soma das despesas de saúde que possuem comprovante. | “despesas de saúde entram pelo valor comprovado” | alta |
| RD-03 | Derivação | A Dedução Aceita é a Dedução de Saúde mais as demais deduções, limitadas a R$ 1.000. | “o total das deduções, tirando saúde, limitado a R$ 1.000” | alta |
| RD-04 | Derivação | A Base de Cálculo é o total de Rendimentos Tributáveis menos a Dedução Aceita. | “retire os valores isentos e também as deduções aceitas” | média, pois a ordem não foi declarada |
| RD-05 | Derivação | O Imposto Bruto é o valor da faixa da Base de Cálculo na tabela do Passo 5. | “Se depois disso a base ficar até R$ 2.500 não há imposto” | alta |
| RD-06 | Derivação | O Imposto Devido é o maior valor entre zero e Imposto Bruto menos Imposto Retido. | “menos o que já foi retido, sem gerar imposto negativo” | alta |

## Passo 3 — regras operativas

O ninho não nomeia nenhum ator, e por isso nenhuma regra operativa tem confiança alta. As duas candidatas abaixo atribuem conduta ao contribuinte por inferência, e o mapa as mantém como hipóteses até a validação do especialista.

| ID | Tipo | Sentença | Evidência | Confiança | Questão em aberto |
|---|---|---|---|---|---|
| RN-01 | Proibição | O contribuinte não deve informar como Dedução de Saúde despesa sem comprovante. | “pelo valor comprovado” | média | A política proíbe a declaração ou apenas exclui o valor do cálculo, como já faz RD-02? |
| RN-02 | Obrigação | O contribuinte deve manter Laudo Válido para cada mês em que usar a isenção de RC-01. | “desde que exista laudo válido no mês” | baixa | Quem precisa apresentar o laudo, e a quem? |

Se o especialista responder que a política só limita o cálculo, RN-01 sai do mapa e RD-02 cobre o caso sozinha, sem duplicar a regra em dois tipos.

## Passo 4 — precedência

1. classificar rendimentos isentos pela exceção RC-01
2. classificar os demais como tributáveis por RC-02
3. calcular e limitar as deduções por RD-01, RD-02 e RD-03
4. derivar a base por RD-04
5. aplicar a faixa por RD-05
6. compensar o imposto retido e limitar o resultado a zero por RD-06

Essa ordem foi inferida das dependências entre valores, e sua confiança permanece média até a validação pelo especialista do domínio.

## Passo 5 — tabela de decisão

A **tabela de decisão** de RD-05 organiza as faixas em linhas, cada uma com uma condição sobre a base e o imposto bruto correspondente.

**Política de acerto: Unique.** As faixas F1, F2 e F3 são mutuamente exclusivas, e cada base de cálculo satisfaz a condição de exatamente uma linha.

| Regra | Base de cálculo | Imposto bruto |
|---|---:|---:|
| F1 | até R$ 2.500,00 | R$ 0,00 |
| F2 | acima de R$ 2.500,00 até R$ 4.000,00 | 10% × (base − R$ 2.500,00) |
| F3 | acima de R$ 4.000,00 | R$ 150,00 + 20% × (base − R$ 4.000,00) |

O valor fixo de R$ 150 preserva a continuidade, pois é o imposto acumulado na faixa F2 quando a base chega a R$ 4.000,00.

## Passo 6 — casos de fronteira

| Caso | Base | Retido | Resultado esperado | Regras |
|---|---:|---:|---:|---|
| Limite isento | R$ 2.500,00 | R$ 0,00 | R$ 0,00 | F1, RD-06 |
| Primeiro centavo da faixa 2 | R$ 2.500,01 | R$ 0,00 | R$ 0,001 | F2 |
| Limite superior da faixa 2 | R$ 4.000,00 | R$ 0,00 | R$ 150,00 | F2 |
| Primeiro centavo da faixa 3 | R$ 4.000,01 | R$ 0,00 | R$ 150,002 | F3 |
| Retenção maior que o bruto | R$ 4.000,00 | R$ 200,00 | R$ 0,00 | F2, RD-06 |

Como a política não define arredondamento, o mapa registra a lacuna com a pergunta **qual regra de arredondamento vale e em que etapa do cálculo?**, e a tabela mantém as casas decimais produzidas pela fórmula.

## Leitura final

O ninho continha duas classificações, seis derivações, duas regras operativas candidatas com ator inferido, uma precedência inferida, três faixas e uma lacuna de arredondamento, todas identificadas por RC, RD, RN ou F e acompanhadas do trecho do parágrafo original que as sustenta.

**Próxima página:** [Exercício de IA — Geral](regras-formais-exercicio-geral.md).
