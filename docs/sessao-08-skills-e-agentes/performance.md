# Performance

O desempenho de uma skill ou de um agente tem três medidas, o tempo até o resultado, o consumo de tokens e a taxa de resultados corretos, e melhorar uma delas costuma custar as outras. Esta página reúne as alavancas de tempo que a documentação e o relato da Anthropic descrevem e o método de avaliação que permite saber se uma mudança melhorou o conjunto. A página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Tempo".

## Três medidas que se compensam

O tempo total depende do número de chamadas, do tamanho do contexto e do modelo. O consumo de tokens determina o custo, tratado na [página anterior](custo-de-tokens.md). A taxa de resultados corretos é medida contra a conferência declarada na skill. O [relato do sistema multiagente](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) mostra a compensação: três fatores explicaram 95% da variação de desempenho no benchmark BrowseComp, sendo 80% pelo uso de tokens, e os outros dois foram o número de chamadas de ferramenta e a escolha do modelo.

![Três cartões ligados por setas duplas: o tempo até o resultado, que depende do número de chamadas, do tamanho do contexto e do modelo, o consumo de tokens, que determina o custo, e a taxa de resultados corretos, medida contra a conferência declarada na skill. Abaixo, o que o relato multiagente mediu no BrowseComp, o registro por execução e a avaliação com cerca de 20 consultas reais.](assets/tres-medidas-de-desempenho.png)

## Alavancas de tempo

| Alavanca | Fonte | O que se informa |
|---|---|---|
| Paralelizar subagentes e ferramentas | Relato multiagente | Executar de 3 a 5 subagentes em paralelo e 3 ou mais ferramentas por subagente reduziu o tempo de pesquisa em até 90% em consultas complexas |
| Cache de prompt | [Documentação do cache](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao) | Melhora o tempo até o primeiro token em documentos longos, sem efeito na geração da saída |
| Reduzir o esforço | [Guia de escolha de modelo](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) | Troca inteligência por latência e custo dentro do mesmo modelo |
| Modo rápido | Guia de escolha de modelo | Até 2,5 vezes mais velocidade de saída, a preço premium, nos modelos que o suportam |
| Modelo menor em subagentes | Guia de escolha de modelo | O Haiku 5.5 tem a menor latência e é indicado para tarefas de subagente |
| Scripts em lugar de código gerado | [Boas práticas de skills](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) | Economizam tempo porque dispensam a geração de código a cada uso |
| Descrições de ferramenta claras | Relato multiagente | Um agente que reescreveu descrições de ferramenta defeituosas cortou em 40% o tempo de conclusão da tarefa |

O relato também aponta um gargalo: quando o orquestrador espera cada subagente terminar antes de seguir, a execução síncrona limita o ganho da paralelização. O Claude Code permite subagentes em segundo plano com o campo `background`, e a documentação informa que subagentes em segundo plano recebem um conjunto menor de ferramentas que os de primeiro plano.

## Avaliar com casos reais

Toda alavanca da tabela troca algo por tempo, e a troca só se justifica com medição. O relato recomenda começar com cerca de 20 consultas que representem o uso real, sem esperar por um conjunto grande de avaliações.

Para a nota, o relato usou um modelo como juiz, com uma rubrica de exatidão factual, exatidão das citações, completude, qualidade das fontes e eficiência no uso de ferramentas, em uma única chamada que devolve uma nota de 0,0 a 1,0 e um resultado de aprovação. Segundo o relato, essa forma foi a mais consistente com o julgamento humano, e os testes feitos por pessoas ainda encontraram vieses que a avaliação automática não detectou. Para agentes que alteram estado, o relato avalia o estado final e não a sequência exata de passos.

A [documentação de boas práticas de skills](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) propõe um formato de avaliação mais simples, com a skill, a consulta, os arquivos de teste e uma lista do comportamento esperado, e observa que não há ferramenta nativa para executá-lo: a equipe monta o próprio sistema de avaliação.

## Reprodutibilidade

As execuções de agente não são determinísticas, o que dificulta a depuração. O relato resolveu o problema com rastreamento completo em produção, e com pontos de retomada, porque erros se acumulam em agentes de longa duração. A equipe que mede o desempenho de uma skill deve registrar, em cada execução, o modelo, o esforço, o número de tokens, o tempo e o resultado da conferência, para comparar execuções feitas em dias diferentes.

!!! abstract "Linha da ficha"
    Tempo:

    - Qual o tempo máximo por execução, e a medição foi feita com casos reais da equipe?
    - Que alavanca de tempo a skill ou o agente usa, e o que ela troca em tokens ou em acerto?
    - Que registro cada execução deixa: modelo, esforço, tokens, tempo e resultado da conferência?

**Próxima página:** [Segurança e credenciais](seguranca-e-credenciais.md).
