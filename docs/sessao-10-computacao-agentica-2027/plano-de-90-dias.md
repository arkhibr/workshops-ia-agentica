# Plano de 90 dias para testar um agente

Antes de usar um agente de IA em todo um processo, a equipe pode testá-lo durante 90 dias num processo escolhido, com medição antes e depois e critérios definidos no início para decidir se o uso será ampliado, corrigido ou interrompido. Esta página descreve as três fases desse teste, chamado de piloto, mostra quais artefatos do curso entram em cada fase e apresenta três cenários possíveis para a adoção de agentes até 2030, que ajudam a decidir com que frequência o plano deve ser revisto.

## As três fases do piloto

![Plano em três fases. Dias 1 a 30, processo e linha de base: entregar escopo e casos de avaliação, medir volume, tempo, custo e qualidade, com passagem quando resultado e responsável estão definidos. Dias 31 a 60, execução delimitada: entregar ferramentas restritas e registros, medir aceites, falhas e intervenção, com passagem quando controle e recuperação funcionam. Dias 61 a 90, comparação e decisão: entregar comparação com a linha de base, medir ganho líquido e fila de revisão, com passagem para ampliar, corrigir ou interromper. A faixa inferior distribui responsabilidades: negócio define resultado e exceções, engenharia define execução e verificação, arquitetura define padrões e integração, segurança define acesso e controles, e liderança decide a expansão.](assets/decisao-nos-90-dias.png)

No primeiro mês, a equipe escolhe o processo, define quais decisões o agente poderá tomar e mede como o processo funciona hoje, sem o agente. Essa medição inicial se chama linha de base e registra volume, tempo, custo e qualidade. A equipe também escreve os casos de avaliação, que são exemplos de entrada com o resultado esperado, usados para testar o agente.

No segundo mês, o agente trabalha primeiro num ambiente de teste e depois numa parte do trabalho real, com acesso apenas às ferramentas necessárias e com registro de todas as ações. A equipe mede quantas entregas foram aceitas, quantas falharam e quanto tempo as pessoas gastaram intervindo.

No terceiro mês, a equipe compara os resultados com a linha de base e decide se amplia, corrige ou interrompe o uso do agente.

| Fase | Critério para passar à fase seguinte |
|---|---|
| Dias 1 a 30 | O resultado do processo pode ser observado, há um responsável pelo processo, o agente pode ter acesso aos dados necessários e o volume de trabalho é conhecido |
| Dias 31 a 60 | Os controles funcionam, o processo se recupera de falhas e as falhas observadas foram entendidas antes de dar mais autonomia ao agente |
| Dias 61 a 90 | Ampliar somente se houver ganho líquido, isto é, ganho depois de descontar revisão e retrabalho, com recuperação de falhas funcionando e responsável definido, e caso contrário corrigir ou interromper |

Cada passagem de fase depende do que o próprio processo mostrou, e o desempenho do agente numa demonstração do fornecedor é tratado como suposição a ser verificada durante o piloto.

## Quem decide o quê no piloto

| Área | Responsabilidade |
|---|---|
| Negócio | Define o resultado esperado e quais situações são exceções |
| Engenharia | Define como o agente executa e como o resultado é verificado |
| Arquitetura | Define os padrões técnicos e a integração com os outros sistemas |
| Segurança | Define os acessos e os controles |
| Liderança | Decide em quais processos o uso será ampliado |

## Artefatos do curso usados no piloto

| Fase | Artefato do curso |
|---|---|
| Dias 1 a 30 | O escopo e os casos de avaliação seguem o ciclo de especificação da [Sessão 3](../sessao-03-exploracao-especificacao/index.md), que pergunta antes de especificar e escreve critérios verificáveis |
| Dias 31 a 60 | As ferramentas e permissões do agente seguem a [ficha de requisitos da Sessão 8](../sessao-08-skills-e-agentes/index.md#a-ficha-de-requisitos), que registra modelo, custo, permissões e credenciais antes de construir o agente |
| Dias 61 a 90 | A decisão de ampliar passa pela faixa de risco e pela aprovação formal da [ficha de governança da Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md#a-ficha-de-governanca) |

A [oficina desta sessão](oficina-de-ferramentas.md) junta esses artefatos numa ficha de piloto com nove campos, preenchida com o agente para um processo fictício da ACME.

## Três cenários de adoção até 2030

![Linha do tempo com três horizontes. Em 2027, operar com controle, com execução persistente, identidade e autorização, e contexto e avaliação, condicionado a resultado verificável e custo medido. De 2027 a 2029, integrar e transacionar, com MCP e A2A e processos híbridos, comércio e pagamentos, e software temporário, condicionado a confiança, intenção e semântica. De 2028 a 2030 em diante, ciência e mundo físico, com hipóteses e experimentos, simulação e modelos de mundo, e políticas e operação robótica, condicionado a validação experimental e segurança. Abaixo, três cenários: base, com tarefas verificáveis e pessoas nas exceções, aceleração, com menos revisão e recuperação, e adoção restrita, com supervisão cara e contexto insuficiente.](assets/horizontes-de-evolucao.png)

O infográfico distribui as mudanças descritas na página [Onze mudanças esperadas para 2027 a 2030](mudancas-esperadas-2027-2030.md) em três períodos: agentes que trabalham com controle em 2027, agentes conectados entre empresas e fazendo pagamentos entre 2027 e 2029, e pesquisa científica e robôs a partir de 2028. As datas são estimativas sem garantia, e a adoção pode seguir um dos três cenários da tabela.

| Cenário | O que acontece |
|---|---|
| Base | Agentes são usados em tarefas cujo resultado pode ser conferido, pessoas tratam as exceções e a integração com os sistemas existentes continua necessária |
| Aceleração | Modelos e ferramentas melhores reduzem muito a revisão humana, e os agentes passam a executar processos mais longos |
| Adoção restrita | O custo de supervisão, os incidentes e a falta de informação adequada mantêm os agentes em poucos processos, e a automação tradicional continua predominante |

O plano de 90 dias foi desenhado para o cenário base. Como os outros dois cenários também são possíveis, a equipe deve revisar o plano a cada trimestre, usando os sinais listados na seção [Sinais a acompanhar depois do curso](sintese-e-referencias.md#sinais-a-acompanhar-depois-do-curso).

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
