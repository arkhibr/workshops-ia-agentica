# Métricas e economia

A decisão de ampliar o uso de agentes depende de medir o que o processo aceitou como resultado, e a quantidade de atividade produzida pelo agente fica fora dessa medida. Esta página apresenta a métrica de custo por resultado aceito, proposta no relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) como operacionalização da análise econômica de fluxos agênticos da [McKinsey](../referencia/bibliografia.md#mckinsey-where-ai-agents-pay-off-2026), as contramétricas que a acompanham e a diferença entre a confiabilidade de um passo e a de um processo.

## Custo por resultado aceito

> **Custo por resultado aceito = custo total do período / quantidade de resultados aceitos no período.**

O custo total inclui inferência, ferramentas, infraestrutura, integração, supervisão, revisão e retrabalho, e os custos fixos são alocados por uma regra explícita, registrada antes da medição. Resultado aceito é a entrega que o processo recebeu como concluída, e a contagem acompanha as reaberturas e correções posteriores, que reduzem o número de aceites do período em que ocorrem.

![Custo integral do fluxo de trabalho somando inferência, ferramentas, infraestrutura, supervisão e retrabalho, com integração, revisão e alocação explícita dos custos fixos. Ao lado, o resultado aceito exige aceite e evidência, acompanhando reaberturas e correções. A faixa central traz a fórmula custo por resultado igual a custo total dividido por resultados aceitos. Abaixo, a confiabilidade de 20 passos independentes: 95% por passo resulta em 35,8% no conjunto, 99% por passo em 81,8% e 99,9% por passo em 98,0%, como exemplo matemático didático.](assets/economia-do-resultado-aceito.png)

A métrica explica por que a escolha de modelo da [Sessão 8](../sessao-08-skills-e-agentes/escolha-de-modelos.md) não se decide pelo preço por token. Um modelo mais barato pode aumentar o número de tentativas e o tempo de revisão, e um modelo mais caro pode reduzir o custo final quando diminui retrabalho e supervisão.

## Contramétricas por dimensão

Cada métrica principal vem acompanhada de uma contramétrica que revela o efeito colateral de otimizar a primeira.

| Dimensão | Métrica principal | Contramétrica |
|---|---|---|
| Resultado | Tarefas concluídas e aceitas | Reaberturas e correções posteriores |
| Fluxo | *Lead time* e *throughput* de resultados aceitos | Trabalho em andamento e fila de revisão |
| Trabalho humano | Minutos de intervenção por resultado | Minutos de retrabalho e de investigação |
| Qualidade | Sucesso em casos representativos | Falhas raras com consequência relevante |
| Economia | Custo integral por resultado | Custos transferidos a outras equipes |
| Segurança | Ações sem autorização ou fora da política | Tentativas bloqueadas e suas causas |
| Operação | Recuperação após falhas | Duplicações e inconsistências de estado |

A linha de fluxo usa as medidas de fluxo do método Kanban, com *lead time*, *throughput* e trabalho em andamento contados sobre resultados aceitos. A fila de revisão é a contramétrica mais provável de crescer quando agentes aceleram a produção de alterações, como descreve a tendência de engenharia por delegação na página [Tendências para 2027 a 2030](tendencias-2027-2030.md#software-e-economia).

## Avaliação com casos típicos, exceções e ataques

As avaliações de agentes combinam casos típicos, exceções e ataques simulados, com verificações determinísticas, julgamento humano e, quando apropriado, avaliadores baseados em modelo calibrados por pessoas, conforme a orientação da Anthropic em [Demystifying Evals for AI Agents](../referencia/bibliografia.md#anthropic-demystifying-evals-for-ai-agents-2026). As verificações determinísticas correspondem aos testes e scripts de conferência praticados nas Sessões 6 e 8, e o julgamento humano calibrado corresponde à fonte de comparação dos casos de uso da [Sessão 7](../sessao-07-casos-de-uso-por-papel/index.md).

## Confiabilidade do passo e do processo

Num exemplo matemático exclusivamente didático, com vinte passos independentes e a mesma chance de sucesso em cada um, a chance de todos funcionarem é o produto das probabilidades.

| Sucesso por passo | Sucesso dos vinte passos |
|---|---|
| 95% | 35,8% |
| 99% | 81,8% |
| 99,9% | 98,0% |

A [Sessão 2](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) mostrou a mesma aritmética com cinquenta passos, em que 99% por passo resultam em 60,5% no conjunto. Os números não medem sistemas reais, porque dependências entre passos, correções, novas tentativas e verificação intermediária mudam o comportamento, e servem para mostrar que avaliar apenas uma resposta isolada não informa a confiabilidade do processo.

**Próxima página:** [Horizontes e plano de 90 dias](horizontes-e-90-dias.md).
