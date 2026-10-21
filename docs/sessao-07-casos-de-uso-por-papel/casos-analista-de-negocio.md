# Casos de uso de IA para Analista de Negócio

Esta página reúne quinze casos de uso de IA generativa para o analista de negócio, a pessoa que levanta, escreve e valida requisitos e regras de negócio com quem conhece o domínio. Dez casos compõem o catálogo do mural da sessão, e cinco são complementares. Sete dos dez casos do mural aplicam técnicas trabalhadas nas Sessões 3 e 4, e a página indica a sessão de origem em cada um.

## Onde a IA entra no trabalho do analista

O analista converte conversas, documentos e normas em requisitos que outras pessoas conseguem implementar e testar. Quase todas as tarefas têm entrada em texto e saída em texto estruturado, e o agente produz rascunhos de glossário, de regra e de requisito com rapidez. A verificação é o que sustenta o caso, porque o analista responde pela fidelidade do requisito ao que o especialista disse, e o agente não tem acesso a essa intenção.

A literatura sobre o uso de modelos de linguagem em engenharia de requisitos é recente. A revisão sistemática de [Zadenoori et al. (2025)](../referencia/bibliografia.md#zadenoori-et-al-llms-para-engenharia-de-requisitos-2025) cobriu 74 estudos publicados em 2023 e 2024, relatou que a maioria trata de elicitação e validação e que as avaliações ocorrem em geral em ambiente controlado, com pouco uso na indústria. Os autores não concluem que o ganho se repete no trabalho cotidiano de uma equipe, e as páginas desta sessão tratam os casos como hipóteses a testar com a tarefa real de cada participante.

A norma [ISO/IEC/IEEE 29148:2018](../referencia/bibliografia.md#isoiecieee-291482018) e o livro de [Wiegers e Beatty (2013)](../referencia/bibliografia.md#wiegers-e-beatty-software-requirements-2013) fornecem os critérios de qualidade que a coluna de conferência usa, como requisito verificável e sem ambiguidade. O vocabulário controlado dos casos de formalização vem do [SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules), do [RuleSpeak](../referencia/bibliografia.md#ross-rulespeak) e da [tabela de decisão DMN](../referencia/bibliografia.md#decision-model-and-notation-dmn).

## Catálogo do mural

| Caso | Entrada e saída | Pedido-base | Conferência |
|---|---|---|---|
| Processar entrevistas | Transcrição de conversa com especialista vira termos, regras e dúvidas | "Separe o que o especialista afirmou do que você inferiu e liste as dúvidas" | Devolver a lista de regras ao especialista e pedir correção |
| Montar glossário do domínio | Documentos viram vocabulário com definição e sinônimos a evitar (Sessão 4) | "Defina cada termo e liste os sinônimos usados nos documentos" | O especialista valida cada definição |
| Formalizar regra em RuleSpeak | Regra em prosa vira sentença numerada com "deve", "não deve" ou "pode ... somente se" (Sessão 4) | "Reescreva a regra numa das três formas e cite a evidência" | Retrotradução em conversa limpa, comparada com a regra original |
| Construir tabela de decisão | Regras com várias condições viram tabela com política de acerto declarada (Sessão 4) | "Monte a tabela e declare a política de acerto" | Preencher à mão quatro casos e comparar com o resultado da tabela |
| Modelar processo atual e futuro | Descrição do processo vira fluxo antes e depois, em notação [BPMN](../referencia/bibliografia.md#omg-bpmn-202-2014) | "Desenhe só os passos citados e marque como lacuna o que faltar" | Quem executa o processo percorre o fluxo e aponta os passos ausentes |
| Escrever requisitos BR, FR e NFR | Pedido vira requisitos classificados e numerados (Sessão 3) | "Classifique cada requisito e escreva o critério verificável" | Cada requisito tem um teste imaginável, critério da norma 29148 |
| Verificar por retrotradução | Especificação vira descrição em prosa numa conversa nova (Sessão 3) | "Descreva em prosa o comportamento que esta especificação produz" | Comparar a prosa com a intenção original e registrar a divergência |
| Preparar perguntas de elicitação | Tema da reunião vira perguntas que expõem ambiguidade (Sessão 3) | "Gere perguntas abertas que revelem o que o pedido deixa em aberto" | O analista descarta as perguntas decorativas, que não mudam a especificação |
| Avaliar impacto normativo | Norma nova e regras atuais viram lista de regras e sistemas afetados | "Para cada regra, diga se a norma a altera e cite o artigo" | Um especialista confere cada artigo citado, porque o agente pode citar artigo inexistente |
| Rastrear requisito até o teste | Requisitos e testes viram matriz de rastreabilidade | "Liste requisitos sem teste e testes sem requisito" | Conferir dez linhas da matriz contra os documentos originais |

## Casos complementares

| Caso | Entrada e saída | Conferência |
|---|---|---|
| Revisar ambiguidade em requisito escrito | Texto de requisito vira lista de termos vagos com sugestão de reescrita | O analista aceita ou rejeita cada sugestão |
| Comparar duas versões de um documento normativo | Duas versões viram lista de diferenças | Conferir cada diferença nos dois textos originais |
| Extrair regras de documento de política | Documento vira lista de regras candidatas com trecho de origem | O trecho citado existe e sustenta a regra |
| Resumir documento longo | Norma ou manual vira resumo por seção | Conferir três afirmações do resumo no texto original |
| Gerar perguntas de validação | Especificação vira perguntas para o usuário confirmar | O analista escolhe as perguntas e conduz a validação |

## Onde os casos falham

Os casos de formalização e rastreabilidade produzem texto com aparência de rigor, e esse é o risco: uma regra numerada e com evidência citada parece verificada mesmo quando a evidência não existe. A conferência por retrotradução, a devolução ao especialista e a amostra de linhas contra o documento original são os três mecanismos desta página, e nenhum depende de o analista conhecer o domínio melhor do que o especialista. Em resumo de conversas, [Tang et al. (2024)](../referencia/bibliografia.md#tang-et-al-tofueval-2024) encontraram erros factuais em resumos de diálogo gerados por modelos de vários tamanhos, o que justifica a devolução ao especialista nos casos que partem de transcrição.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
