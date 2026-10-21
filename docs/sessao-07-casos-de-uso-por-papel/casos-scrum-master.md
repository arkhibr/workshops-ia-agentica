# Casos de uso de IA para Scrum Master

Esta página reúne quinze casos de uso de IA generativa para o Scrum Master, a pessoa que facilita as cerimônias de um time ágil e acompanha a saúde do fluxo de trabalho. Dez casos compõem o catálogo do mural da sessão, e cinco são complementares. O papel inclui facilitação, leitura de métricas e comunicação com a gestão, e os casos seguem essa divisão.

## Onde a IA entra no trabalho do Scrum Master

A parte do trabalho que lida com texto, como notas de retrospectiva, respostas abertas de pesquisa e relatórios de status, tem entrada e saída em linguagem natural e é a que o agente trata com mais facilidade. A parte que lida com números de fluxo exige cuidado adicional, porque o agente pode escrever uma leitura plausível de uma métrica sem refazer a conta. Dois casos do catálogo produzem números, a leitura de métricas e a previsão de entrega, e a coluna de conferência exige para eles um recálculo feito fora do agente.

As práticas que os casos apoiam têm fonte própria. O [Scrum Guide de 2020](../referencia/bibliografia.md#schwaber-e-sutherland-the-2020-scrum-guide-2020) descreve a retrospectiva da sprint como o momento de planejar maneiras de aumentar qualidade e efetividade, e [Derby e Larsen (2006)](../referencia/bibliografia.md#derby-e-larsen-agile-retrospectives-2006) tratam as retrospectivas como prática recorrente ao longo do projeto. O [Kanban Guide de 2025](../referencia/bibliografia.md#coleman-et-al-the-kanban-guide-2025) define quatro métricas de fluxo, que são o trabalho em andamento, a vazão, a idade do item e o tempo de ciclo, e a relação entre elas segue a fórmula L = λW demonstrada por [Little (1961)](../referencia/bibliografia.md#little-a-proof-for-the-queuing-formula-1961).

Esta pesquisa não localizou estudo revisado por pares que meça o uso de IA nas tarefas do Scrum Master, e os casos da página são hipóteses de trabalho a testar com a tarefa real de cada participante.

## Catálogo do mural

| Caso | Entrada e saída | Pedido-base | Conferência |
|---|---|---|---|
| Processar a retrospectiva | Notas dos participantes viram temas, causas prováveis e ações com dono | "Agrupe as notas por tema, cite as notas de origem e proponha ação apenas com dono indicado" | Os participantes reconhecem as próprias notas nos temas, e cada ação tem dono e prazo |
| Ler métricas de fluxo | Tempo de ciclo, vazão e trabalho em andamento viram leitura em linguagem simples e hipóteses | "Descreva o que cada métrica indica e proponha hipóteses, sem recomendar ação que os dados não sustentem" | Recalcular uma métrica em planilha e comparar com o texto |
| Mapear bloqueios recorrentes | Histórico do quadro vira lista de bloqueios ordenada por frequência | "Liste os bloqueios com o item de origem e a contagem" | Contar à mão cinco bloqueios da lista no histórico |
| Roteirizar cerimônias | Objetivo da reunião vira roteiro cronometrado | "Monte um roteiro de 60 minutos com objetivo, perguntas e tempo por etapa" | Percorrer o roteiro com o relógio e ajustar as etapas que não cabem |
| Registrar experimentos | Ideia de melhoria vira hipótese, ação, evidência esperada e decisão | "Declare como a equipe saberá se a hipótese se confirmou" | A hipótese é refutável e a evidência existe antes do experimento |
| Resumir status para a gestão | Itens e métricas viram relatório de uma página | "Use apenas os números fornecidos e marque o que está sem dado" | Cada número do relatório é reproduzido a partir da fonte |
| Prever entrega por simulação | Histórico de vazão vira faixa de datas com probabilidade | "Escreva o script de simulação a partir do histórico, sem estimar datas por conta própria" | A simulação roda em script ou planilha, e a faixa de datas vem da execução e não do texto do agente |
| Sintetizar pesquisa de clima | Respostas abertas viram temas com exemplos | "Agrupe as respostas por tema e cite trechos literais" | Contar os temas em uma amostra de vinte respostas e preservar o anonimato |
| Acompanhar riscos e ações | Atas e e-mails viram registro de riscos atualizado | "Liste riscos novos e mudanças de status com a origem de cada um" | O Scrum Master confere cada mudança de status na fonte |
| Integrar pessoa nova | Documentação da equipe vira guia de integração | "Organize a documentação em um roteiro de primeira semana" | Uma pessoa recém-chegada usa o guia e aponta as lacunas |

## Casos complementares

| Caso | Entrada e saída | Conferência |
|---|---|---|
| Comparar retrospectivas de vários ciclos | Atas de retrospectiva viram lista de temas que se repetem | Conferir três repetições citadas nas atas originais |
| Preparar a pauta de uma cerimônia | Contexto do time vira pauta com objetivo por item | O Scrum Master remove itens sem decisão associada |
| Explicar uma métrica a um gestor | Métrica e contexto viram explicação sem jargão | Um gestor lê a explicação e reformula com as próprias palavras |
| Redigir comunicado de impedimento | Descrição do bloqueio vira comunicado com impacto e pedido | O texto cita o item bloqueado e quem pode resolver |
| Montar mapa de dependências entre equipes | Backlogs de duas equipes viram lista de itens que dependem um do outro | Os dois times confirmam cada dependência listada |

## Onde os casos falham

Dois casos do catálogo produzem números, e a conferência por recálculo é o que os sustenta. O caso de previsão por simulação é o mais exposto, porque um agente pode escrever uma faixa de datas sem ter rodado simulação nenhuma, e o texto fica igual ao de uma simulação real. O sumário do livro de [Vacanti, *When Will It Be Done?*](../referencia/bibliografia.md#vacanti-when-will-it-be-done), inclui um capítulo sobre planejamento probabilístico de releases com simulação de Monte Carlo, e [Miranda et al. (2021)](../referencia/bibliografia.md#miranda-et-al-monte-carlo-para-prever-projetos-de-software-2021) analisam simulações de Monte Carlo na previsão de projetos de software. A regra para o caso é que o agente escreve o script e a simulação roda fora dele.

Nos casos que partem de texto de terceiros, como notas de retrospectiva e respostas de pesquisa de clima, o risco é o resumo atribuir ao grupo uma opinião que uma pessoa expressou. A conferência por amostra e a preservação do anonimato respondem a esse risco, e o [estudo de caso](estudo-de-caso.md) da sessão mostra o efeito de uma conferência omitida.

**Próxima página:** [Casos de uso para Desenvolvimento](casos-desenvolvimento.md).
