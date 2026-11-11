# Métricas e economia

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) propõe medir o uso de agentes pelos resultados que o processo aceita, com base na análise econômica de fluxos agênticos publicada pela [McKinsey](../referencia/bibliografia.md#mckinsey-where-ai-agents-pay-off-2026). Esta página apresenta a métrica de custo por resultado aceito, as contramétricas que a acompanham e o cálculo da confiabilidade de um processo com vários passos.

## Custo por resultado aceito

> **Custo por resultado aceito = custo total do período / quantidade de resultados aceitos no período.**

| Termo | Definição |
|---|---|
| Custo total | Inferência, ferramentas, infraestrutura, integração, supervisão, revisão e retrabalho, com os custos fixos alocados por regra registrada antes da medição |
| Resultado aceito | Entrega que o processo recebeu como concluída, descontadas as reaberturas e correções posteriores no período em que ocorrem |

![Custo integral do fluxo de trabalho somando inferência, ferramentas, infraestrutura, supervisão e retrabalho, com integração, revisão e alocação explícita dos custos fixos. Ao lado, o resultado aceito exige aceite e evidência, acompanhando reaberturas e correções. A faixa central traz a fórmula custo por resultado igual a custo total dividido por resultados aceitos. Abaixo, a confiabilidade de 20 passos independentes: 95% por passo resulta em 35,8% no conjunto, 99% por passo em 81,8% e 99,9% por passo em 98,0%, como exemplo matemático didático.](assets/economia-do-resultado-aceito.png)

Com essa métrica, a escolha de modelo tratada na [Sessão 8](../sessao-08-skills-e-agentes/escolha-de-modelos.md) passa a considerar o custo final do resultado, além do preço por token. Um modelo mais barato pode aumentar o número de tentativas e o tempo de revisão, e um modelo mais caro pode reduzir o custo final quando diminui retrabalho e supervisão.

## Contramétricas por dimensão

Para cada métrica principal, o relatório indica uma contramétrica que registra o efeito indesejado de melhorar apenas a métrica principal.

| Dimensão | Métrica principal | Contramétrica |
|---|---|---|
| Resultado | Tarefas concluídas e aceitas | Reaberturas e correções posteriores |
| Fluxo | *Lead time* e *throughput* de resultados aceitos | Trabalho em andamento e fila de revisão |
| Trabalho humano | Minutos de intervenção por resultado | Minutos de retrabalho e de investigação |
| Qualidade | Sucesso em casos representativos | Falhas raras com consequência relevante |
| Economia | Custo integral por resultado | Custos transferidos a outras equipes |
| Segurança | Ações sem autorização ou fora da política | Tentativas bloqueadas e suas causas |
| Operação | Recuperação após falhas | Duplicações e inconsistências de estado |

A linha de fluxo usa as medidas do método Kanban contadas sobre resultados aceitos. Quando agentes produzem alterações mais depressa, a fila de revisão tende a crescer, como descreve a tendência de engenharia por delegação na página [Tendências para 2027 a 2030](tendencias-2027-2030.md#software-e-economia).

## Avaliação de agentes

A orientação da Anthropic em [Demystifying Evals for AI Agents](../referencia/bibliografia.md#anthropic-demystifying-evals-for-ai-agents-2026) recomenda montar o conjunto de avaliação com casos típicos, exceções e ataques simulados, e conferir os resultados por verificação determinística, por julgamento humano e, quando cabível, por avaliador baseado em modelo calibrado por pessoas. Os testes e scripts de conferência das Sessões 6 e 8 são verificações determinísticas, e a fonte de comparação dos casos de uso da [Sessão 7](../sessao-07-casos-de-uso-por-papel/index.md) é uma forma de julgamento humano.

## Confiabilidade do passo e do processo

O relatório usa um exemplo didático com vinte passos independentes e a mesma probabilidade de sucesso em cada passo, caso em que a probabilidade de sucesso do conjunto é o produto das probabilidades.

| Sucesso por passo | Sucesso dos vinte passos |
|---|---|
| 95% | 35,8% |
| 99% | 81,8% |
| 99,9% | 98,0% |

A [Sessão 2](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) fez o mesmo cálculo com cinquenta passos, em que 99% por passo resultam em 60,5% no conjunto. Os valores não descrevem sistemas reais, em que dependências entre passos, correções, novas tentativas e verificações intermediárias alteram o resultado, e mostram que a avaliação de uma resposta isolada não informa a confiabilidade do processo inteiro.

**Próxima página:** [Cenários e plano de 90 dias](horizontes-e-90-dias.md).
