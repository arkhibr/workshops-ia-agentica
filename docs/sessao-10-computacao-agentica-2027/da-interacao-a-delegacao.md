# Da interação à delegação

Computação agêntica, no recorte do relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026), designa sistemas baseados em modelos de IA capazes de escolher ações, operar ferramentas, observar resultados e ajustar a própria execução para atender a um objetivo. O agente é o sistema completo, e o modelo é um de seus componentes, o que corresponde à equação agente igual a modelo mais arnês estudada na [Sessão 2](../sessao-02-ambiente-agentico/arnes.md).

## Fluxo de trabalho e agente

A distinção arquitetural mais útil para começar vem de [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), da Anthropic, já usada na Sessão 1. Num fluxo de trabalho, o código define o caminho e o modelo executa etapas previstas. Num agente, o modelo escolhe dinamicamente o próximo passo dentro de um conjunto de ferramentas autorizadas. O texto é de dezembro de 2024, e a própria página do fornecedor registra que o panorama de ferramentas mudou desde então, de modo que a distinção continua válida como conceito e os exemplos de produto envelheceram.

## As quatro formas de delegação

O relatório organiza a delegação em quatro formas, que diferem pelo responsável pela escolha do próximo passo e pelo alcance da ação.

| Forma | Quem escolhe o próximo passo | Exemplo ilustrativo |
|---|---|---|
| Resposta assistida | A pessoa, que recebe a informação e decide o que fazer | O sistema explica uma cláusula de contrato |
| Fluxo de trabalho com IA | O código, numa sequência definida antes da execução | O sistema extrai campos de um documento e o encaminha pela sequência prevista |
| Agente com autonomia delimitada | O agente, dentro do escopo autorizado | O agente investiga uma divergência e prepara a correção para aprovação |
| Sistema com múltiplos agentes | Vários agentes, com ferramentas ou contextos distintos, sob alguma coordenação | Agentes especializados dividem o trabalho e reconciliam os resultados |

As quatro formas convivem na mesma organização e, com frequência, no mesmo processo. A escolha de uma delas para cada etapa segue o princípio de simplicidade da Sessão 1: a forma mais simples que resolve a etapa, com aumento de autonomia somente quando a tarefa o exigir.

## O ciclo do objetivo ao resultado aceito

A delegação se completa quando o processo aceita o resultado, o que inclui a verificação e, quando exigida, a aprovação de uma pessoa. O infográfico abaixo usa um exemplo ilustrativo, a investigação de uma divergência de faturamento, para mostrar as seis etapas do ciclo.

![Ciclo de seis etapas do objetivo ao resultado aceito, ilustrado pela investigação de uma divergência de faturamento. A etapa 1, objetivo, recebe a fatura e a divergência, com escopo e critério de aceite. A etapa 2, contexto, reúne contrato e pedido com origem e acesso verificados. A etapa 3, ação, faz consulta e cálculo com ferramentas delimitadas. A etapa 4, verificação, produz proposta e evidências para validar antes de executar. A etapa 5, aprovação, registra a decisão quando exigida, vinculada à proposta. A etapa 6, resultado, entrega correção e comprovante aceitos pelo processo. Uma faixa inferior indica registrar estado, observar o resultado e retomar dentro dos limites.](assets/formas-de-delegacao.png)

Três etapas do ciclo correspondem a práticas do curso. O critério de aceite da etapa 1 é o mesmo critério que a [Sessão 3](../sessao-03-exploracao-especificacao/index.md) exige antes de acionar o agente. A delimitação de ferramentas da etapa 3 é a permissão mínima tratada na [Sessão 8](../sessao-08-skills-e-agentes/seguranca-e-credenciais.md). A aprovação vinculada à proposta, na etapa 5, é o nível de autonomia "preparar para aprovação" definido na ficha de governança da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/governanca-de-ia.md).

## A intervenção humana como parte do desenho

A intervenção humana entra no ciclo quando a tarefa ultrapassa o que foi delegado, e a decisão sobre esse ponto é tomada no desenho do processo, antes da execução. O estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), apresentado na seção seguinte, encontrou que 68% dos sistemas implantados na amostra executavam no máximo dez passos antes de uma intervenção humana, o que indica que a delegação em produção ocorre hoje em unidades curtas e verificáveis.

**Próxima página:** [Evidência e previsão](evidencia-e-previsao.md).
