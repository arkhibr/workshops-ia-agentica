# Medição do custo e do resultado de um agente

Para decidir se um agente de IA compensa num processo, a equipe precisa medir quantas entregas do agente o processo aceitou como corretas e quanto custou produzir cada uma, incluindo o tempo das pessoas que revisam e corrigem o trabalho. Esta página explica a métrica de custo por resultado aceito, as medidas que acompanham essa métrica para revelar efeitos indesejados e o cálculo da confiabilidade de uma tarefa com vários passos.

## Custo por resultado aceito

> **Custo por resultado aceito = custo total do período / quantidade de resultados aceitos no período.**

| Termo | O que entra |
|---|---|
| Custo total | Uso do modelo de IA, ferramentas, infraestrutura, integração com outros sistemas, horas de supervisão, horas de revisão e horas de retrabalho, mais uma parte dos custos fixos, distribuída por uma regra definida antes da medição |
| Resultado aceito | Entrega que o processo recebeu como concluída e correta, descontadas as entregas que precisaram ser reabertas ou corrigidas depois, no mês em que isso acontece |

Essa forma de medir segue a recomendação da McKinsey, na análise [Where AI Agents Pay Off](../referencia/bibliografia.md#mckinsey-where-ai-agents-pay-off-2026), de calcular o custo completo do trabalho concluído. A oficina desta sessão aplica a fórmula a um processo fictício, com os números de um mês.

![Custo integral do fluxo de trabalho somando inferência, ferramentas, infraestrutura, supervisão e retrabalho, com integração, revisão e alocação explícita dos custos fixos. Ao lado, o resultado aceito exige aceite e evidência, acompanhando reaberturas e correções. A faixa central traz a fórmula custo por resultado igual a custo total dividido por resultados aceitos. Abaixo, a confiabilidade de 20 passos independentes: 95% por passo resulta em 35,8% no conjunto, 99% por passo em 81,8% e 99,9% por passo em 98,0%, como exemplo matemático didático.](assets/economia-do-resultado-aceito.png)

No infográfico, inferência é o nome técnico para o uso do modelo de IA, cobrado por quantidade de texto processado. A métrica muda a forma de escolher o modelo, tratada na [Sessão 8](../sessao-08-skills-e-agentes/escolha-de-modelos.md): um modelo mais barato por uso pode exigir mais tentativas e mais revisão humana, e um modelo mais caro pode sair mais barato por resultado aceito quando reduz retrabalho e supervisão.

## Medidas que mostram efeitos indesejados

Quando a equipe melhora uma medida, outra pode piorar sem que ninguém perceba. Por isso cada medida principal da tabela vem acompanhada de uma medida de efeito colateral, chamada contramétrica, que mostra o que a melhoria da primeira pode ter prejudicado.

| Área | Medida principal | Medida de efeito colateral |
|---|---|---|
| Resultado | Tarefas concluídas e aceitas | Tarefas reabertas ou corrigidas depois |
| Fluxo | *Lead time* (tempo total entre o pedido e a entrega aceita) e *throughput* (entregas aceitas por período) | Trabalho em andamento (itens iniciados e não concluídos) e tamanho da fila de revisão |
| Trabalho humano | Minutos de intervenção humana por resultado | Minutos de retrabalho e de investigação de erros |
| Qualidade | Acertos em casos típicos | Falhas raras com consequência grave |
| Custo | Custo completo por resultado | Custos que passaram para outras equipes |
| Segurança | Ações sem autorização ou fora das regras | Tentativas bloqueadas e suas causas |
| Operação | Recuperação depois de falhas | Ações duplicadas e dados inconsistentes |

Quando agentes produzem alterações mais depressa do que as pessoas conseguem revisar, a fila de revisão cresce, e por isso ela é a medida de efeito colateral mais importante no desenvolvimento de software com agentes, descrito na página [Mudanças esperadas para 2027 a 2030](mudancas-esperadas-2027-2030.md#software-custo-e-escolha-de-modelos).

## Como testar um agente antes de liberá-lo

A Anthropic, no texto [Demystifying Evals for AI Agents](../referencia/bibliografia.md#anthropic-demystifying-evals-for-ai-agents-2026), recomenda testar um agente com três grupos de casos: casos típicos do dia a dia, exceções que fogem do padrão e ataques simulados, como um documento com instruções maliciosas. A conferência do resultado pode ser feita por um programa que compara a resposta com o valor esperado, por uma pessoa ou, quando cabível, por outro modelo de IA cujas avaliações foram comparadas antes com as de pessoas. Os testes automatizados das Sessões 6 e 8 são exemplos do primeiro tipo, e a conferência contra uma fonte, usada nos casos de uso da [Sessão 7](../sessao-07-casos-de-uso-por-papel/index.md), é um exemplo do segundo.

## Confiabilidade de uma tarefa com vários passos

Quando um agente executa vários passos em sequência e cada passo pode falhar, a chance de a tarefa inteira dar certo é a chance de cada passo multiplicada pelas demais. Com vinte passos independentes e a mesma chance de acerto em cada um, os valores são os da tabela.

| Acerto em cada passo | Acerto na tarefa de vinte passos |
|---|---|
| 95% | 35,8% |
| 99% | 81,8% |
| 99,9% | 98,0% |

A [Sessão 2](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) chamou esse efeito de erro composto e fez o mesmo cálculo com cinquenta passos, em que 99% de acerto por passo resultam em 60,5% de acerto na tarefa. Em sistemas reais os passos dependem uns dos outros e há correções e novas tentativas, de modo que esses números servem como ilustração, e mostram que testar uma resposta isolada do agente não informa a confiabilidade da tarefa inteira.

**Próxima página:** [Plano de 90 dias para testar um agente](plano-de-90-dias.md).
