# Escolha de modelos

A escolha do modelo de uma skill ou de um agente é uma decisão de projeto que equilibra capacidade, velocidade e custo, e não uma configuração herdada da conversa. Esta página reúne os critérios e as duas estratégias de partida do [guia de escolha de modelo](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) da Anthropic e mostra onde cada decisão aparece nos arquivos de skill e de subagente. A página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Modelo e esforço".

## Quatro critérios

O guia recomenda avaliar, antes de escolher, quatro fatores. A capacidade responde que recursos a tarefa exige. A velocidade responde em quanto tempo a resposta precisa chegar, e o modo rápido entrega até 2,5 vezes mais velocidade de saída, a preço premium, nos modelos que o suportam. O custo responde ao orçamento de desenvolvimento e de produção. O esforço é um parâmetro, disponível em vários modelos, que troca inteligência por latência e custo dentro de um mesmo modelo, e o guia afirma que ajustar o esforço costuma ser uma alavanca melhor que trocar de modelo.

## Duas estratégias de partida

| Estratégia | Como proceder | Indicada para |
|---|---|---|
| Eficiência primeiro | Implementar com o Claude Haiku 5.5, testar a fundo e subir de modelo apenas diante de uma lacuna de capacidade específica | Protótipos, latência apertada, volume alto de tarefas simples, custo sensível |
| Capacidade primeiro | Implementar com o Claude Opus 5.5, otimizar o prompt para ele, avaliar e reduzir o esforço ou o modelo ao longo do tempo | Raciocínio complexo, programação avançada e agentes de alta autonomia, em que a precisão pesa mais que o custo |

Se as avaliações no esforço `xhigh` ou `max` ainda ficam abaixo do necessário em raciocínio exigente ou em trabalho agêntico de longo horizonte, o guia indica passar ao Claude Fable 5.1. Os dois caminhos têm o mesmo requisito: um conjunto de avaliações próprio. O guia classifica esse conjunto como o passo mais importante do processo.

![Duas faixas de estratégia. Eficiência primeiro: implementar com Claude Haiku 5.5, testar a fundo e subir de modelo só diante de uma lacuna de capacidade específica. Capacidade primeiro: implementar com Claude Opus 5.5, otimizar o prompt e avaliar, e reduzir o esforço ou o modelo ao longo do tempo. Abaixo, o esforço como alavanca dentro do modelo e a indicação do Claude Fable 5.1 quando xhigh ou max ainda ficam abaixo do necessário.](assets/estrategias-de-escolha-de-modelo.png)

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

No subagente, o campo `model` aceita `sonnet`, `opus`, `haiku`, `fable`, um identificador completo ou `inherit`, e uma troca do modelo da conversa para o Opus se estende aos subagentes que usam `inherit`, o que eleva o custo desses subagentes ao preço do Opus. Na skill, a plataforma Claude e a especificação aberta não declaram modelo, e o Claude Code acrescenta o campo `model`, que vale apenas no turno em que a skill está ativa e não grava nas configurações. O guia de boas práticas pede que a skill seja testada com os três modelos que a equipe pretende usar, porque o texto que basta para o Opus pode exigir mais detalhe para o Haiku, e o texto escrito para o Haiku pode explicar demais para o Opus.

### Resolução do model por subagente e por skill

A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) fixa a ordem em que o Claude Code resolve o modelo do subagente, em quatro passos:

1. O parâmetro `model` passado pelo agente principal na própria chamada de delegação.
2. O campo `model` do arquivo do subagente, em que `inherit` seleciona o modelo da conversa principal.
3. A variável de ambiente `CLAUDE_CODE_SUBAGENT_MODEL`, quando definida com um apelido ou um identificador.
4. O modelo da conversa principal.

Antes da v2.1.251, a variável de ambiente vinha em primeiro lugar e prevalecia sobre a chamada e sobre o arquivo. A lista completa de identificadores válidos não foi confirmada, e por isso os exemplos do material usam apenas os apelidos. Na skill, o campo `model` aceita os mesmos valores do comando `/model` ou `inherit`, e o modelo da sessão volta a valer na mensagem seguinte.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a ordem de resolução consta de [Choose a model](https://code.claude.com/docs/en/sub-agents#choose-a-model).
    **Codex CLI:** o arquivo do agente aceita `model` e `model_reasoning_effort`, e o valor do arquivo prevalece sobre o do pai, enquanto os padrões globais dos subagentes ficam em `agents.default_subagent_model`, conforme a [documentação de Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao) e a [referência de configuração](../referencia/bibliografia.md#openai-codex-configuration-reference-documentacao). Os modelos disponíveis dependem da conta, e na observação desta sessão o modelo padrão da conta exigiu uma versão do Codex mais nova que a instalada.

### Exemplo: o modelo declarado nos arquivos

Os três arquivos abaixo reaproveitam os exemplos das páginas de [Skills](skills.md#exemplo-um-skillmd-com-valores-escolhidos) e de [Agentes e subagentes](agentes-e-subagentes.md#anatomia-e-front-matter-do-subagente), e mostram onde cada decisão de modelo é escrita. São exemplos ilustrativos, sem execução.

A skill `registrando-decisao-arquitetural` gera registros de decisão arquitetural (ADR) e declara o modelo e o esforço no front-matter:

```markdown
---
name: registrando-decisao-arquitetural
model: sonnet
effort: medium
---
```

O subagente `revisor-de-adr` revisa o registro depois de gerado e declara um modelo menor, além de um limite de turnos:

```markdown
---
name: revisor-de-adr
tools: Read, Grep, Glob
model: haiku
maxTurns: 8
---
```

Uma skill de saída volumosa, que roda num subagente por `context: fork`, declara o modelo do subagente no mesmo campo, porque com `fork` o valor de `model` passa a valer para o subagente:

```markdown
---
name: relatar-falhas-de-teste
context: fork
agent: general-purpose
model: haiku
---
```

| Arquivo | Linha | Decisão de modelo | Alcance |
|---|---|---|---|
| Skill | `model: sonnet` | Ponto de partida intermediário, adequado a redação estruturada conferida por script | Só o turno em que a skill é invocada |
| Skill | `effort: medium` | Esforço abaixo do máximo, porque a camada estrutural é conferida pelo script | Só o turno da skill |
| Subagente | `model: haiku` | Estratégia de eficiência primeiro, para uma revisão curta e de leitura | Toda delegação a esse subagente, salvo o parâmetro `model` da chamada de delegação, que vence o arquivo |
| Subagente | `maxTurns: 8` | Limite de custo e de tempo da revisão | Cada execução do subagente |
| Skill com `fork` | `model: haiku` | Tarefa de saída volumosa e de pouca decisão | O subagente criado pelo `fork` |

Se a pessoa trocar o modelo da conversa para o Opus com `/model`, a skill continua com `sonnet` no próprio turno e o `revisor-de-adr` continua com `haiku`, porque os dois declaram o modelo. Um subagente com `model: inherit`, ou sem o campo e sem a variável `CLAUDE_CODE_SUBAGENT_MODEL`, passaria a usar o Opus e custaria o preço dele. A [oficina](oficina-de-ferramentas.md#experimento-b-medir-o-custo-e-o-resultado-em-dois-modelos) mede a skill em dois modelos, e o resultado decide se o `sonnet` e o `medium` do exemplo se mantêm.

## Combinar modelos

O guia descreve duas estratégias que pagam a maior parte dos tokens à tarifa do modelo mais barato: um executor que escala as decisões difíceis a um consultor mais forte, e um orquestrador que delega o trabalho em volume a trabalhadores de menor custo. O relato do [sistema multiagente da Anthropic](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) usou a segunda forma, com orquestrador Opus e subagentes Sonnet, e o guia de custo recomenda Sonnet para os integrantes de equipes de agentes.

## Como decidir na equipe

1. Escreva de 3 a 5 tarefas reais da skill, com o resultado esperado de cada uma.
2. Execute as tarefas no modelo de partida da estratégia escolhida e registre o resultado conferido, o tempo e os tokens.
3. Repita com um modelo menor ou com esforço menor e compare os três registros.
4. Adote o menor modelo cujo resultado conferido atenda ao critério, e anote a data da medição, porque a conclusão vale para as versões testadas.

!!! abstract "Linha da ficha"
    Modelo e esforço:

    - Qual modelo e qual esforço a skill ou o subagente usa, e com que razão?
    - Que conjunto de avaliações próprio sustenta a escolha, e em que data foi medido?
    - O `model` do subagente é explícito ou herdado da conversa com `inherit`?

**Próxima página:** [Custo de tokens](custo-de-tokens.md).
