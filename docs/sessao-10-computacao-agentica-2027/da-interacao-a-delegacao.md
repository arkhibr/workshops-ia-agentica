# Formas de delegação de trabalho

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) usa o termo computação agêntica para sistemas baseados em modelos de IA que escolhem ações, operam ferramentas, observam o resultado de cada ação e ajustam a execução seguinte em função de um objetivo. Nesse uso, o agente é o sistema completo e o modelo é um dos seus componentes, como na equação agente igual a modelo mais arnês da [Sessão 2](../sessao-02-ambiente-agentico/arnes.md).

## Fluxo de trabalho e agente

O texto [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), da Anthropic, usado na Sessão 1, distingue dois tipos de sistema. Num fluxo de trabalho, o código define a sequência de etapas e o modelo executa cada etapa prevista. Num agente, o modelo escolhe o próximo passo a cada iteração, dentro do conjunto de ferramentas autorizadas. O texto é de dezembro de 2024, e a própria página informa que as ferramentas citadas como exemplo mudaram desde a publicação, sem alteração na distinção entre os dois tipos.

## As quatro formas de delegação

O relatório classifica a delegação em quatro formas, que diferem pelo responsável pela escolha do próximo passo.

| Forma | Quem escolhe o próximo passo | Exemplo do relatório |
|---|---|---|
| Resposta assistida | A pessoa, depois de receber a informação | O sistema explica uma cláusula de contrato |
| Fluxo de trabalho com IA | O código, numa sequência definida antes da execução | O sistema extrai campos de um documento e o encaminha pela sequência prevista |
| Agente com autonomia delimitada | O agente, dentro do escopo autorizado | O agente investiga uma divergência e prepara a correção para aprovação |
| Sistema com múltiplos agentes | Vários agentes com ferramentas ou contextos distintos, sob coordenação | Agentes especializados dividem o trabalho e conciliam os resultados |

Um mesmo processo pode usar formas diferentes em etapas diferentes. Pelo princípio de simplicidade da Sessão 1, cada etapa usa a forma mais simples que a resolve, e a autonomia só aumenta quando a tarefa exige.

## Etapas até o resultado aceito

O relatório considera a delegação concluída quando o processo aceita o resultado, depois da verificação e, quando exigida, da aprovação de uma pessoa. O infográfico mostra as seis etapas com o exemplo de uma divergência de faturamento.

![Ciclo de seis etapas do objetivo ao resultado aceito, ilustrado pela investigação de uma divergência de faturamento. A etapa 1, objetivo, recebe a fatura e a divergência, com escopo e critério de aceite. A etapa 2, contexto, reúne contrato e pedido com origem e acesso verificados. A etapa 3, ação, faz consulta e cálculo com ferramentas delimitadas. A etapa 4, verificação, produz proposta e evidências para validar antes de executar. A etapa 5, aprovação, registra a decisão quando exigida, vinculada à proposta. A etapa 6, resultado, entrega correção e comprovante aceitos pelo processo. Uma faixa inferior indica registrar estado, observar o resultado e retomar dentro dos limites.](assets/formas-de-delegacao.png)

| Etapa | Artefato do curso correspondente |
|---|---|
| 1, objetivo com critério de aceite | Critério de aceite exigido na [Sessão 3](../sessao-03-exploracao-especificacao/index.md) antes de acionar o agente |
| 3, ação com ferramentas delimitadas | Permissão mínima tratada na [Sessão 8](../sessao-08-skills-e-agentes/seguranca-e-credenciais.md) |
| 5, aprovação vinculada à proposta | Nível de autonomia "preparar para aprovação" da ficha de governança da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/governanca-de-ia.md) |

## Intervenção humana

O ponto em que uma pessoa intervém é definido no desenho do processo, antes da execução, e corresponde ao momento em que a tarefa excede o escopo delegado. No estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), detalhado na página seguinte, 68% dos sistemas em produção da amostra executavam no máximo dez passos antes de uma intervenção humana.

**Próxima página:** [Evidência e previsão](evidencia-e-previsao.md).
