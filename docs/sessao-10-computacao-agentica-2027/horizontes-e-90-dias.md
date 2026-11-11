# Horizontes e plano de 90 dias

As tendências de computação agêntica avançam em ritmos diferentes, e uma equipe que precisa decidir o que fazer em 2027 ganha mais com um experimento de prazo curto e critério declarado do que com um compromisso irreversível com uma previsão. Esta página apresenta os horizontes e os três cenários do relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) e o plano de 90 dias que ele propõe para testar um processo antes de ampliar a delegação.

## Três horizontes

![Linha do tempo com três horizontes. Em 2027, operar com controle, com execução persistente, identidade e autorização, e contexto e avaliação, condicionado a resultado verificável e custo medido. De 2027 a 2029, integrar e transacionar, com MCP e A2A e processos híbridos, comércio e pagamentos, e software temporário, condicionado a confiança, intenção e semântica. De 2028 a 2030 em diante, ciência e mundo físico, com hipóteses e experimentos, simulação e modelos de mundo, e políticas e operação robótica, condicionado a validação experimental e segurança. Abaixo, três cenários: base, com tarefas verificáveis e pessoas nas exceções, aceleração, com menos revisão e recuperação, e adoção restrita, com supervisão cara e contexto insuficiente.](assets/horizontes-de-evolucao.png)

| Horizonte | Foco | Condição de avanço |
|---|---|---|
| 2027 | Operar com controle: execução persistente, identidade e autorização, contexto e avaliação | Resultado verificável e custo medido |
| 2027 a 2029 | Integrar e transacionar: MCP, A2A, processos híbridos, comércio, pagamentos e software temporário | Confiança entre as partes, registro de intenção e semântica compartilhada |
| 2028 a 2030 em diante | Ciência e mundo físico: hipóteses, simulação, modelos de mundo e robótica | Validação experimental e segurança física |

As datas são cenários analíticos sem garantia de adoção. O relatório atribui confiança média-alta à interoperabilidade e média ao software temporário e ao comércio, classificações editoriais sem valor de probabilidade calculada.

## Três cenários

No cenário base, que orienta as recomendações do relatório e do plano de 90 dias desta página, agentes se expandem em unidades de trabalho verificáveis, pessoas tratam as exceções, as políticas operam continuamente e a integração com sistemas existentes continua relevante.

**Cenário de aceleração.** Melhorias de modelos e de ambientes reduzem fortemente a revisão e a recuperação, e a delegação avança para processos mais longos com resultado verificável.

**Cenário de adoção restrita.** Custo de supervisão, incidentes e dificuldades de contexto mantêm os agentes concentrados em poucos processos e reforçam a automação convencional.

Os cenários de aceleração e de adoção restrita justificam revisões periódicas do plano. A seção [Depois do curso](sintese-e-referencias.md#depois-do-curso) lista os sinais que indicam qual dos três cenários está se confirmando para cada tendência.

## O plano de 90 dias

![Plano em três fases. Dias 1 a 30, processo e linha de base: entregar escopo e casos de avaliação, medir volume, tempo, custo e qualidade, com passagem quando resultado e responsável estão definidos. Dias 31 a 60, execução delimitada: entregar ferramentas restritas e registros, medir aceites, falhas e intervenção, com passagem quando controle e recuperação funcionam. Dias 61 a 90, comparação e decisão: entregar comparação com a linha de base, medir ganho líquido e fila de revisão, com passagem para ampliar, corrigir ou interromper. A faixa inferior distribui responsabilidades: negócio define resultado e exceções, engenharia define execução e verificação, arquitetura define padrões e integração, segurança define acesso e controles, e liderança decide a expansão.](assets/decisao-nos-90-dias.png)

| Fase | O que se entrega | O que se mede | Critério de passagem |
|---|---|---|---|
| Dias 1 a 30, processo e linha de base | Um processo escolhido, as decisões delegáveis delimitadas e os casos de avaliação | Volume, tempo, custo e qualidade do processo atual | Resultado observável, responsável pelo processo, acesso viável e volume conhecido |
| Dias 31 a 60, execução delimitada | Execução em ambiente controlado e depois sobre trabalho real com escopo limitado, com ferramentas restritas e registros | Aceites, falhas e minutos de intervenção | Controles e recuperação funcionando, com as falhas compreendidas antes de aumentar a delegação |
| Dias 61 a 90, comparação e decisão | Comparação com a linha de base e ajuste do fluxo | Ganho líquido e fila de revisão | Ampliar somente com ganho líquido, recuperação funcional e responsabilidade explícita, ou corrigir, ou interromper |

A divisão de responsabilidades proposta atribui ao negócio a definição do resultado e das exceções, à engenharia a execução e a verificação, à arquitetura os padrões e a integração, à segurança o acesso e os controles, e à liderança a decisão sobre onde ampliar. Cada passagem entre fases depende de evidência produzida pelo processo, e a capacidade demonstrada pelo modelo numa demonstração entra como premissa a verificar.

## Ligação com as fichas do curso

O plano de 90 dias reaproveita os artefatos construídos nas sessões anteriores. O escopo e os casos de avaliação do primeiro mês seguem o ciclo de especificação da [Sessão 3](../sessao-03-exploracao-especificacao/index.md), as ferramentas restritas do segundo mês seguem a ficha de requisitos da [Sessão 8](../sessao-08-skills-e-agentes/index.md#a-ficha-de-requisitos), e a decisão de ampliar do terceiro mês passa pela faixa de risco e pelo gate da ficha de governança da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md#a-ficha-de-governanca). A [oficina desta sessão](oficina-de-ferramentas.md) reúne esses elementos numa ficha de piloto com nove campos, preenchida com o agente para um processo fictício da ACME.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
