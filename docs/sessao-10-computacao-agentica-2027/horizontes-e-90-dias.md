# Cenários e plano de 90 dias

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) divide as tendências em três períodos, descreve três cenários de adoção e propõe um plano de 90 dias para testar o uso de agentes num processo antes de ampliar a delegação. O relatório recomenda testes de prazo curto com critério definido antes do início, porque as tendências avançam em velocidades diferentes e as datas de previsão não têm garantia.

## Três períodos

![Linha do tempo com três horizontes. Em 2027, operar com controle, com execução persistente, identidade e autorização, e contexto e avaliação, condicionado a resultado verificável e custo medido. De 2027 a 2029, integrar e transacionar, com MCP e A2A e processos híbridos, comércio e pagamentos, e software temporário, condicionado a confiança, intenção e semântica. De 2028 a 2030 em diante, ciência e mundo físico, com hipóteses e experimentos, simulação e modelos de mundo, e políticas e operação robótica, condicionado a validação experimental e segurança. Abaixo, três cenários: base, com tarefas verificáveis e pessoas nas exceções, aceleração, com menos revisão e recuperação, e adoção restrita, com supervisão cara e contexto insuficiente.](assets/horizontes-de-evolucao.png)

| Período | Tendências | Condição para avançar |
|---|---|---|
| 2027 | Execução persistente, identidade e autorização, contexto e avaliação | Resultado verificável e custo medido |
| 2027 a 2029 | MCP, A2A, processos híbridos, comércio, pagamentos e software temporário | Confiança entre as partes, registro de intenção e significado comum dos dados |
| 2028 a 2030 ou depois | Hipóteses científicas, simulação, modelos de mundo e robótica | Validação experimental e segurança física |

O relatório atribui confiança média-alta à interoperabilidade e confiança média ao software temporário e ao comércio, como avaliação editorial e sem valor de probabilidade calculada.

## Três cenários

| Cenário | Descrição |
|---|---|
| Base | Agentes são usados em unidades de trabalho verificáveis, pessoas tratam as exceções, as políticas são aplicadas de forma contínua e a integração com os sistemas existentes continua necessária |
| Aceleração | Modelos e ambientes melhores reduzem muito a revisão e a recuperação, e a delegação passa a cobrir processos mais longos com resultado verificável |
| Adoção restrita | Custo de supervisão, incidentes e falta de contexto mantêm os agentes em poucos processos, e a automação convencional continua predominante |

As recomendações do relatório e o plano de 90 dias partem do cenário base. Os outros dois cenários justificam revisar o plano periodicamente, e a seção [Depois do curso](sintese-e-referencias.md#depois-do-curso) lista os sinais que indicam, para cada tendência, qual cenário está se confirmando.

## Plano de 90 dias

![Plano em três fases. Dias 1 a 30, processo e linha de base: entregar escopo e casos de avaliação, medir volume, tempo, custo e qualidade, com passagem quando resultado e responsável estão definidos. Dias 31 a 60, execução delimitada: entregar ferramentas restritas e registros, medir aceites, falhas e intervenção, com passagem quando controle e recuperação funcionam. Dias 61 a 90, comparação e decisão: entregar comparação com a linha de base, medir ganho líquido e fila de revisão, com passagem para ampliar, corrigir ou interromper. A faixa inferior distribui responsabilidades: negócio define resultado e exceções, engenharia define execução e verificação, arquitetura define padrões e integração, segurança define acesso e controles, e liderança decide a expansão.](assets/decisao-nos-90-dias.png)

| Fase | Entrega | Medição | Critério de passagem |
|---|---|---|---|
| Dias 1 a 30, processo e linha de base | Processo escolhido, decisões delegáveis delimitadas e casos de avaliação | Volume, tempo, custo e qualidade do processo atual | Resultado observável, responsável pelo processo, acesso viável e volume conhecido |
| Dias 31 a 60, execução delimitada | Execução em ambiente controlado e depois em trabalho real com escopo limitado, com ferramentas restritas e registros | Aceites, falhas e minutos de intervenção | Controles e recuperação funcionando e falhas analisadas antes de aumentar a delegação |
| Dias 61 a 90, comparação e decisão | Comparação com a linha de base e ajuste do fluxo | Ganho líquido e fila de revisão | Decisão de ampliar, corrigir ou interromper, com ampliação somente se houver ganho líquido, recuperação funcionando e responsável definido |

| Área | Responsabilidade no piloto |
|---|---|
| Negócio | Define o resultado esperado e as exceções |
| Engenharia | Define a execução e a verificação |
| Arquitetura | Define os padrões e a integração |
| Segurança | Define o acesso e os controles |
| Liderança | Decide onde ampliar |

Cada passagem de fase depende de evidência produzida pelo próprio processo, e o desempenho do modelo numa demonstração é tratado como premissa a verificar durante o piloto.

## Artefatos do curso usados no plano

| Fase | Artefato do curso |
|---|---|
| Dias 1 a 30 | Escopo e casos de avaliação escritos com o ciclo de especificação da [Sessão 3](../sessao-03-exploracao-especificacao/index.md) |
| Dias 31 a 60 | Ferramentas e permissões declaradas na [ficha de requisitos da Sessão 8](../sessao-08-skills-e-agentes/index.md#a-ficha-de-requisitos) |
| Dias 61 a 90 | Faixa de risco e aprovação no gate da [ficha de governança da Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md#a-ficha-de-governanca) |

A [oficina desta sessão](oficina-de-ferramentas.md) reúne esses artefatos numa ficha de piloto com nove campos, preenchida com o agente para um processo fictício da ACME.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
