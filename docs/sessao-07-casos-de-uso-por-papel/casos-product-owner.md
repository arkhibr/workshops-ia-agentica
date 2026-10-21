# Casos de uso de IA para Product Owner

Esta página reúne quinze casos de uso de IA generativa para quem exerce o papel de product owner (PO), a pessoa que decide o que entra no backlog de um produto e em que ordem. Dez casos compõem o catálogo do mural da sessão, e cinco são complementares. Cada caso traz a entrada, a saída esperada, um pedido-base que o PO adapta ao próprio contexto e a conferência que precisa acontecer antes de o resultado circular.

## Onde a IA entra no trabalho do PO

A maior parte do trabalho do PO é texto em linguagem natural: conversas com patrocinadores, relatos de usuários, pedidos vagos e decisões que precisam virar itens de backlog. É nesse tipo de tarefa que a IA gera rascunho com mais facilidade, e a decisão sobre valor e prioridade permanece com a pessoa. O critério que separa um bom caso de um mau caso aparece na coluna de conferência: o resultado só é útil quando o PO consegue verificá-lo contra uma fonte que ele conhece, como a fala da reunião, o relato do usuário ou o critério de priorização que ele mesmo definiu.

A evidência disponível para o papel é limitada e recente. [Quattrocchi et al. (2025)](../referencia/bibliografia.md#quattrocchi-et-al-user-stories-geradas-por-llms-2025) compararam histórias de usuário geradas por dez modelos com histórias escritas por especialistas e estudantes e relataram que as geradas se assemelham às humanas em cobertura e qualidade de estilo, com menor diversidade e menor frequência no atendimento aos critérios de aceitação definidos no estudo. Para resumo de conversas, [Tang et al. (2024)](../referencia/bibliografia.md#tang-et-al-tofueval-2024) mediram, em diálogos, erros factuais em resumos de modelos de vários tamanhos, com resultados que não dependeram do tamanho do modelo. Os modelos de ambos os estudos são de 2023 e 2024, e os modelos atuais podem ter resultados diferentes.

## Catálogo do mural

| Caso | Entrada e saída | Pedido-base | Conferência |
|---|---|---|---|
| Processar reuniões | Transcrição vira ata com decisões, ações e pontos sem decisão | "Registre apenas o que está na transcrição e escreva *sem responsável citado* quando ninguém foi indicado" | Comparar cada decisão, número e prazo com a fala, como na [demonstração](exemplo-arquitetural.md) |
| Escrever histórias de usuário | Pedido vago do patrocinador vira histórias no formato "como, quero, para" | "Gere histórias independentes e testáveis e liste as suposições que você fez" | Aplicar os critérios de [Wake (2003)](../referencia/bibliografia.md#wake-invest-in-good-stories-and-smart-tasks-2003) a cada história e devolver as que não passam |
| Desenhar jornada de usuário | Relatos e entrevistas viram etapas, ações, dores e oportunidades | "Use só o que está nos relatos e marque como lacuna a etapa sem relato" | Uma pessoa que vive a jornada confere cada dor, porque [Gibbons (2018)](../referencia/bibliografia.md#gibbons-journey-mapping-101-2018) descreve as ações do mapa como baseadas em dados e recomenda falas reais de clientes obtidas em pesquisa |
| Refinar o backlog | Item grande vira itens menores com dependências e dúvidas | "Fatie por valor entregável e liste as dúvidas que o PO precisa responder" | Cada fatia atravessa o fluxo do usuário de ponta a ponta, como as faixas de release que [Patton (2008)](../referencia/bibliografia.md#patton-the-new-user-story-backlog-is-a-map-2008) descreve no mapa de histórias |
| Priorizar com critério | Lista de itens e um critério viram ranking com justificativa | "Aplique o critério informado a cada item e mostre a conta" | Refazer a conta de dois itens à mão. O critério é escolha do PO |
| Escrever critérios em Gherkin | História vira cenários no formato dado, quando, então | "Inclua um cenário de borda e um de erro" | Desenvolvimento e testes leem os cenários, que seguem a [referência do Gherkin](../referencia/bibliografia.md#cucumber-gherkin-reference), e apontam o que falta |
| Preparar a revisão da sprint | Itens concluídos viram roteiro de demonstração e resumo | "Ordene pelo valor ao usuário e indique o que não será demonstrado" | Confirmar que cada item listado como concluído existe e funciona |
| Analisar feedback de usuários | Chamados e comentários viram temas com contagem e exemplos | "Cite o comentário de origem de cada tema" | Contar os temas numa amostra de vinte comentários e confirmar que as citações existem |
| Montar o roadmap | Iniciativas e objetivos viram roadmap por horizonte, com riscos | "Não invente datas e marque cada dependência" | Validar com os patrocinadores antes de publicar |
| Ensaiar com o patrocinador | Proposta vira perguntas difíceis com respostas-base | "Aja como um patrocinador cético e pergunte o que mais o preocupa" | O PO escolhe as perguntas relevantes e escreve as próprias respostas |

## Casos complementares

| Caso | Entrada e saída | Conferência |
|---|---|---|
| Resolver ambiguidade de pedido | Pedido vago vira perguntas de uma por vez, no formato da entrevista socrática da [Sessão 3](../sessao-03-exploracao-especificacao/index.md) | O PO responde às perguntas e o dossiê resultante é lido pelo patrocinador |
| Redigir notas de versão | Lista de mudanças vira texto para usuários finais | Cada mudança citada existe na versão e nenhuma foi omitida |
| Comparar alternativas de solução | Duas ou mais opções e critérios viram matriz de comparação | O PO confere as notas atribuídas a cada critério |
| Preparar entrevistas com usuários | Objetivo da pesquisa vira roteiro de perguntas abertas | O PO remove perguntas que induzem a resposta |
| Detectar conflito entre histórias | Conjunto de histórias vira lista de pares em contradição | O PO confere cada par apontado, porque a lista pode conter falsos positivos |

## Onde os casos falham

Os cinco primeiros casos do catálogo dependem de o PO conhecer a fonte melhor do que o agente. Uma ata que atribui uma decisão à pessoa errada, uma história que repete o pedido com outra formatação e uma jornada com dor sem relato correspondente passam numa leitura rápida e se propagam para o backlog. A regra operacional desta sessão é que nenhum resultado dos casos desta página circula sem conferência de quem decide, e que o material de entrada não contém dado pessoal nem sigiloso. O [estudo de caso](estudo-de-caso.md) discute o que acontece quando essa conferência é omitida numa ata de reunião.

**Próxima página:** [Casos de uso para Scrum Master](casos-scrum-master.md).
