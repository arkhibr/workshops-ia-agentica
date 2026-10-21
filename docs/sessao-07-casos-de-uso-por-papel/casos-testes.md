# Casos de uso de IA para Testes

Esta página reúne quinze casos de uso de IA generativa para quem planeja, escreve e analisa testes de software, seja como analista de testes, seja como desenvolvedor que testa o próprio código. Dez casos compõem o catálogo do mural da sessão, e cinco são complementares. O papel de testes verifica o trabalho dos outros papéis, e por isso a pergunta de conferência de cada caso inclui quem verifica o próprio teste.

## Onde a IA entra no trabalho de testes

As tarefas de testes combinam dois tipos de trabalho. O primeiro é a derivação sistemática, em que a técnica é conhecida e o agente acelera a aplicação, como a partição de equivalência e a análise de valor-limite que o [syllabus do ISTQB](../referencia/bibliografia.md#istqb-certified-tester-foundation-level-syllabus-v401-2024) descreve nas seções 4.2.1 e 4.2.2. O segundo é o julgamento de risco e de severidade, em que a decisão cabe a quem responde pelo resultado do teste.

A evidência sobre geração de testes por modelos de linguagem já existe. [Schäfer et al. (2024)](../referencia/bibliografia.md#schafer-et-al-testpilot-2024) avaliaram a ferramenta TestPilot em 25 pacotes npm e 1.684 funções de API e relataram mediana de cobertura de instruções de 70,2% e de ramos de 52,8%, contra 51,3% e 25,6% de uma ferramenta de referência. [Harman et al. (2025)](../referencia/bibliografia.md#harman-et-al-mutation-guided-llm-test-generation-at-meta-2025) descreveram, na Meta, uma geração de testes guiada por mutantes em que os engenheiros aceitaram 73% dos 571 testes gerados. Os dois estudos medem testes de unidade em código aberto e em ambiente industrial específico, e o resultado em outro contexto precisa ser medido.

## Catálogo do mural

| Caso | Entrada e saída | Pedido-base | Conferência |
|---|---|---|---|
| Derivar casos da história | História e critérios de aceite viram casos positivos, negativos e de borda | "Liste os casos por critério de aceite e indique a que critério cada um responde" | Cada caso aponta para um critério, e cada critério tem pelo menos um caso |
| Gerar dados de teste | Esquema do banco vira conjunto de dados realistas e anonimizados | "Gere dados fictícios que respeitem as restrições do esquema" | Nenhum dado real, e o conjunto passa nas restrições do esquema |
| Escrever testes automatizados | Caso de teste vira teste de API ou de interface | "Escreva o teste sem alterar o código de produção" | Executar o teste, que deve falhar quando o comportamento muda |
| Explorar valores-limite | Regra vira partições de equivalência e valores de fronteira | "Liste as partições e os valores em cada lado da fronteira" | Conferir cada fronteira contra a regra e os valores de cada lado |
| Criar testes de propriedade | Regra vira propriedades verificáveis, com [FsCheck e fast-check](../referencia/bibliografia.md#fast-check-e-fscheck-property-based-testing) | "Escreva propriedades que valem para qualquer entrada válida" | Introduzir um defeito e conferir que a propriedade o encontra |
| Triar defeitos | Relato bruto vira severidade proposta, indicação de duplicidade e passos | "Proponha a severidade e cite o trecho do relato que a justifica" | A severidade final é decisão humana |
| Redigir relato de bug | Comportamento observado vira relato reproduzível | "Descreva passos, resultado obtido e resultado esperado" | Outra pessoa reproduz o defeito só com o relato |
| Investigar testes instáveis | Histórico de execuções vira causas prováveis | "Liste hipóteses de causa e o dado que confirmaria cada uma" | Reexecutar o teste em ambiente controlado para verificar a primeira hipótese |
| Avaliar a suíte por mutação | Suíte e relatório de mutantes viram lacunas e testes fracos | "Liste os mutantes sobreviventes e proponha um teste para cada um" | O novo teste mata o mutante, conforme a [documentação do Stryker](../referencia/bibliografia.md#stryker-mutator-documentacao) |
| Montar o relatório de testes | Resultados viram relatório da entrega | "Use somente os resultados fornecidos e marque o que não foi testado" | Cada número do relatório é reproduzido a partir dos resultados |

## Casos complementares

| Caso | Entrada e saída | Conferência |
|---|---|---|
| Definir estratégia de teste por risco | Módulos e criticidade viram plano de profundidade de teste | O responsável pelo risco aprova a criticidade atribuída a cada módulo |
| Escrever testes de contrato | Especificação de uma API vira testes entre consumidor e provedor | Executar os testes contra o provedor real em ambiente de teste |
| Analisar falhas de pipeline | Log de execução vira lista de causas prováveis | Reproduzir a falha localmente com o primeiro passo indicado |
| Revisar testes existentes | Suíte vira lista de testes frágeis ou redundantes | Conferir três testes apontados e decidir manter ou remover |
| Propor roteiros de teste exploratório | Funcionalidade vira missões de exploração de 30 minutos | O testador executa uma missão e avalia se revelou comportamento inesperado |

## Onde os casos falham

O risco central dos casos de geração de teste é o teste que passa sem verificar nada. [Claessen e Hughes (2000)](../referencia/bibliografia.md#claessen-e-hughes-quickcheck-2000) registram, na seção 5.1.4 do artigo que apresentou o QuickCheck, o falso senso de segurança de um programa que passa muitos testes sobre casos triviais, e o mesmo risco vale para testes de qualquer origem. A conferência por mutação, descrita por [Papadakis et al. (2019)](../referencia/bibliografia.md#papadakis-et-al-mutation-testing-advances-2019), mede se a suíte detecta defeitos introduzidos de propósito, e é a verificação que sustenta os casos de geração de teste.

Nos casos de triagem e de investigação de testes instáveis, a decisão final é humana. Em testes instáveis, [Luo et al. (2014)](../referencia/bibliografia.md#luo-et-al-an-empirical-analysis-of-flaky-tests-2014) analisaram 201 commits em 51 projetos e encontraram espera assíncrona, concorrência e dependência de ordem entre as categorias de causa mais frequentes, o que orienta as hipóteses que o agente deve listar. Esta pesquisa não encontrou artigo revisado por pares sobre o uso de modelos de linguagem na triagem de defeitos, e o caso é tratado como hipótese de trabalho.

**Próxima página:** [Casos de uso para Analista de Negócio](casos-analista-de-negocio.md).
