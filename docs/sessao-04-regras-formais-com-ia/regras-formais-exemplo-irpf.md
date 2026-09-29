# Exemplo: decomposição de um ninho de regras de IRPF

Esta demonstração usa o cálculo do Imposto de Renda da Pessoa Física (IRPF) como domínio conhecido, sem reproduzir a legislação vigente. O objetivo é observar uma política confusa sendo separada em conceitos, fatos, regras, tabela e testes.

!!! warning "Exemplo fictício"
    Todos os limites, percentuais e valores monetários desta página são **valores hipotéticos** criados para a aula. O exemplo não representa a tabela vigente, não é uma calculadora fiscal e **não é orientação tributária**.

## O ninho de regras

> Para calcular o imposto mensal, considere os rendimentos recebidos no mês, mas retire os valores isentos e também as deduções aceitas, sendo que dependente vale R$ 200 por pessoa e despesas de saúde entram pelo valor comprovado, embora o total das deduções, tirando saúde, não possa passar de R$ 1.000. Se depois disso a base ficar até R$ 2.500 não há imposto; passando disso até R$ 4.000 cobra-se 10% só do que passou de R$ 2.500, e acima de R$ 4.000 cobra-se R$ 150 mais 20% do excedente, mas o imposto devido no mês é o calculado menos o que já foi retido, sem gerar imposto negativo, e quem tiver moléstia grave não paga sobre proventos de aposentadoria desde que exista laudo válido no mês.

O parágrafo mistura definições, fórmula, faixas, teto, exceção documental e compensação. Pedir a um agente que “transforme isso em regra” sem contrato de saída tende a produzir uma paráfrase, não um modelo verificável.

## Passo 1 — conceitos e fatos

| Conceito | Definição neste exemplo |
|---|---|
| Rendimento Tributável | Rendimento que permanece após a classificação de isenção |
| Dedução Aceita | Valor que a política permite retirar dos rendimentos tributáveis |
| Base de Cálculo | Valor usado para selecionar a faixa e calcular o imposto bruto |
| Imposto Bruto | Valor produzido pela tabela progressiva antes da retenção |
| Imposto Retido | Valor já recolhido no mês |
| Imposto Devido | Resultado final, limitado a zero |
| Laudo Válido | Documento vigente no mês de cálculo |

Os tipos de fato incluem: Pessoa recebe Rendimento; Rendimento possui Classificação; Pessoa possui Dependente; Despesa possui Comprovante; Laudo possui Período de Validade; e Imposto Retido reduz Imposto Bruto.

## Passo 2 — regras estruturais

**RC-01 — Classificação.** Provento de aposentadoria recebido por pessoa com moléstia grave e laudo válido no mês é Rendimento Isento. Evidência: “não paga sobre proventos de aposentadoria desde que exista laudo válido no mês”. Confiança: alta dentro do cenário fictício.

**RD-01 — Derivação.** A Dedução por Dependentes é a quantidade de dependentes multiplicada por R$ 200. Evidência: “dependente vale R$ 200 por pessoa”. Confiança: alta.

**RD-02 — Derivação.** A Base de Cálculo é o total de Rendimentos Tributáveis menos as Deduções Aceitas. Evidência: “retire os valores isentos e também as deduções aceitas”. Confiança: média, pois a ordem não foi declarada.

**RD-03 — Derivação.** O Imposto Devido é o maior valor entre zero e Imposto Bruto menos Imposto Retido. Evidência: “menos o que já foi retido, sem gerar imposto negativo”. Confiança: alta.

## Passo 3 — regras operativas

- **RN-01 — Obrigação.** A apuração deve excluir Rendimentos Isentos antes de calcular a Base de Cálculo.
- **RN-02 — Permissão.** Uma Despesa de Saúde pode compor a Dedução Aceita somente se possuir comprovante.
- **RN-03 — Proibição.** As deduções que não sejam de saúde não devem exceder R$ 1.000 no mês.
- **RN-04 — Permissão.** Um provento de aposentadoria pode ser isento por moléstia grave somente se houver Laudo Válido no mês.

## Passo 4 — precedência

1. classificar rendimentos isentos, inclusive pela exceção RC-01;
2. somar apenas rendimentos tributáveis;
3. calcular e limitar as deduções;
4. derivar a base;
5. aplicar a faixa;
6. compensar o imposto retido;
7. limitar o resultado final a zero.

Essa ordem foi inferida das dependências entre valores. Sua confiança permanece média até validação pelo especialista do domínio.

## Passo 5 — tabela de decisão

**Política de acerto: Unique.** Os intervalos são mutuamente exclusivos.

| Regra | Base de cálculo | Imposto bruto |
|---|---:|---:|
| F1 | até R$ 2.500,00 | R$ 0,00 |
| F2 | acima de R$ 2.500,00 até R$ 4.000,00 | 10% × (base − R$ 2.500,00) |
| F3 | acima de R$ 4.000,00 | R$ 150,00 + 20% × (base − R$ 4.000,00) |

O valor fixo de R$ 150 preserva a continuidade: é o imposto acumulado na faixa anterior.

## Passo 6 — casos de fronteira

| Caso | Base | Retido | Resultado esperado | Regras |
|---|---:|---:|---:|---|
| Limite isento | R$ 2.500,00 | R$ 0,00 | R$ 0,00 | F1, RD-03 |
| Primeiro centavo da faixa 2 | R$ 2.500,01 | R$ 0,00 | R$ 0,001 | F2 |
| Limite superior da faixa 2 | R$ 4.000,00 | R$ 0,00 | R$ 150,00 | F2 |
| Primeiro centavo da faixa 3 | R$ 4.000,01 | R$ 0,00 | R$ 150,002 | F3 |
| Retenção maior que o bruto | R$ 4.000,00 | R$ 200,00 | R$ 0,00 | F2, RD-03 |

O arredondamento não foi definido. Em vez de escolher duas casas por hábito, o mapa registra a lacuna: **qual regra de arredondamento vale e em que etapa?**

## Leitura final

O ninho continha uma classificação, três derivações, quatro regras operativas, uma precedência inferida, três faixas e uma lacuna. O mapa torna cada decisão localizável e cada incerteza discutível.

**Próxima página:** [Exercício de IA — Geral](regras-formais-exercicio-geral.md).
