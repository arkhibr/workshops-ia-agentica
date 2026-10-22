# Escolha de modelos

A escolha do modelo de uma skill ou de um agente é uma decisão de projeto que equilibra capacidade, velocidade e custo, e não uma configuração herdada da conversa. Esta página reúne os critérios e as duas estratégias de partida do [guia de escolha de modelo](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) da Anthropic e mostra onde cada decisão aparece nos arquivos de skill e de subagente.

## Quatro critérios

O guia recomenda avaliar, antes de escolher, quatro fatores. A capacidade responde que recursos a tarefa exige. A velocidade responde em quanto tempo a resposta precisa chegar, e o modo rápido entrega até 2,5 vezes mais velocidade de saída, a preço premium, nos modelos que o suportam. O custo responde ao orçamento de desenvolvimento e de produção. O esforço é um parâmetro, disponível em vários modelos, que troca inteligência por latência e custo dentro de um mesmo modelo, e o guia afirma que ajustar o esforço costuma ser uma alavanca melhor que trocar de modelo.

## Duas estratégias de partida

| Estratégia | Como proceder | Indicada para |
|---|---|---|
| Eficiência primeiro | Implementar com o Claude Haiku 5.5, testar a fundo e subir de modelo apenas diante de uma lacuna de capacidade específica | Protótipos, latência apertada, volume alto de tarefas simples, custo sensível |
| Capacidade primeiro | Implementar com o Claude Opus 5.5, otimizar o prompt para ele, avaliar e reduzir o esforço ou o modelo ao longo do tempo | Raciocínio complexo, programação avançada e agentes de alta autonomia, em que a precisão pesa mais que o custo |

Se as avaliações no esforço `xhigh` ou `max` ainda ficam abaixo do necessário em raciocínio exigente ou em trabalho agêntico de longo horizonte, o guia indica passar ao Claude Fable 5.1. Os dois caminhos têm o mesmo requisito: um conjunto de avaliações próprio. O guia classifica esse conjunto como o passo mais importante do processo.

## Matriz de uso por modelo

A matriz resume o guia, com os modelos vigentes em 22/10/2026.

| Necessidade | Ponto de partida | Exemplos de uso |
|---|---|---|
| A maior capacidade disponível | Claude Fable 5.1 | Sessões de agente que duram horas, pesquisa em várias etapas |
| Programação agêntica complexa e trabalho corporativo | Claude Opus 5.5 | Agentes autônomos de várias horas, refatoração em larga escala |
| Velocidade e capacidade para o uso diário | Claude Sonnet 5.5 | Geração de código, análise de dados, uso agêntico de ferramentas |
| Menor latência e menor preço | Claude Haiku 5.5 | Aplicações em tempo real, alto volume, tarefas de subagente |

Para o Claude Code, o [guia de custo](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) acrescenta que o Sonnet atende bem à maioria das tarefas de programação e custa menos que o Opus, que fica reservado a decisões de arquitetura complexas e a raciocínio em várias etapas, e que subagentes de tarefas simples podem declarar `model: haiku`.

## Onde a decisão aparece nos arquivos

No subagente, o campo `model` aceita `sonnet`, `opus`, `haiku`, `fable`, um identificador completo ou `inherit`. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) fixa a ordem de resolução do modelo: primeiro o parâmetro passado pelo agente principal em cada chamada, depois o campo `model` do arquivo, depois a variável `CLAUDE_CODE_SUBAGENT_MODEL` e, por último, o modelo da conversa principal. Por isso uma troca do modelo da conversa para o Opus se estende aos subagentes que usam `inherit`, o que eleva o custo desses subagentes ao preço do Opus.

A skill não declara modelo. O guia de boas práticas pede, por isso, que a skill seja testada com os três modelos que a equipe pretende usar, porque o texto que basta para o Opus pode exigir mais detalhe para o Haiku, e o texto escrito para o Haiku pode explicar demais para o Opus.

## Combinar modelos

O guia descreve duas estratégias que pagam a maior parte dos tokens à tarifa do modelo mais barato: um executor que escala as decisões difíceis a um consultor mais forte, e um orquestrador que delega o trabalho em volume a trabalhadores de menor custo. O relato do [sistema multiagente da Anthropic](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) usou a segunda forma, com orquestrador Opus e subagentes Sonnet, e o guia de custo recomenda Sonnet para os integrantes de equipes de agentes.

## Como decidir na equipe

1. Escreva de 3 a 5 tarefas reais da skill, com o resultado esperado de cada uma.
2. Execute as tarefas no modelo de partida da estratégia escolhida e registre o resultado conferido, o tempo e os tokens.
3. Repita com um modelo menor ou com esforço menor e compare os três registros.
4. Adote o menor modelo cujo resultado conferido atenda ao critério, e anote a data da medição, porque a conclusão vale para as versões testadas.

**Próxima página:** [Custo de tokens](custo-de-tokens.md).
