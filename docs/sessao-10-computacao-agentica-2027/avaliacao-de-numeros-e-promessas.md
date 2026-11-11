# Avaliação de números e promessas sobre agentes

Pesquisas de consultoria, anúncios de fornecedores e reportagens sobre agentes de IA publicam afirmações de naturezas diferentes, como respostas a questionários, relatos de clientes escolhidos pelo fornecedor e previsões para os próximos anos. Esta página classifica essas afirmações por tipo, explica o que cada tipo permite concluir e aplica a classificação a pesquisas das consultorias McKinsey, Gartner e Forrester e a estudos publicados em 2026.

## Tipos de afirmação sobre agentes

| Tipo | O que é | O que não permite concluir |
|---|---|---|
| Resultado de estudo | Pesquisa que descreve o método e quem foi estudado, por exemplo quantas empresas e de quais setores | Não vale para empresas ou tarefas diferentes das estudadas |
| Relato de empresa | Uma empresa, ou o fornecedor dela, descreve uma implantação e o resultado obtido | Pode não haver comparação com um grupo que não usou a ferramenta, nem conferência por terceiros |
| Piloto | Teste em ambiente real, com escopo e duração limitados | Não mostra que o uso funciona em escala nem que o produto está disponível para todos |
| Anúncio de produto | Documentação ou lançamento oficial de um fornecedor | Mostra o que o produto faz, sem mostrar retorno financeiro para quem compra |
| Previsão de analista | Expectativa publicada por consultoria para uma data futura | Ainda não aconteceu |
| Hipótese | Interpretação sobre a direção do mercado | Precisa de sinais definidos que permitam confirmá-la ou descartá-la |

A [Sessão 1](../sessao-01-o-que-mudou/avaliacao-de-modelos.md) aplicou o mesmo cuidado aos placares que comparam modelos de IA, em que o número publicado pelo fabricante do modelo e o número medido por terceiros têm confiabilidade diferente. Palavras como adoção, uso em produção e uso em escala também descrevem situações diferentes, e um número de cada tipo não pode ser somado aos outros para produzir uma taxa única de adoção do mercado.

## O que as consultorias publicaram em 2026

![Três colunas com as contribuições das consultorias. McKinsey tem foco em adoção e resultado econômico, recomenda verificar o custo integral por resultado e alerta que pesquisa não é auditoria. Gartner tem foco em contexto, harness e identidade, recomenda verificar os controles da execução e alerta que previsão não é taxa observada. Forrester tem foco em prontidão operacional, recomenda verificar governança e orquestração e alerta que tecnologia exige organização. A faixa inferior soma valor econômico, capacidade de plataforma e responsabilidade operacional.](assets/tres-condicoes-para-escalar.png)

A McKinsey publicou em agosto de 2026 a pesquisa [The State of AI in 2026](../referencia/bibliografia.md#mckinsey-the-state-of-ai-in-2026-2026), com 1.719 participantes de 97 países. Nas organizações com receita anual acima de US$ 1 bilhão, 40% dos respondentes afirmam usar agentes em escala em pelo menos uma área da empresa, contra 22% nas organizações menores. Na mesma pesquisa, 32% dos respondentes afirmam ter desistido de comprar pelo menos um produto de software porque conseguiram construí-lo com agentes de programação. Os dois números são respostas dos 1.719 participantes, e a McKinsey não conferiu as implantações que eles descreveram.

Entre as previsões do Gartner, a lista de [tendências de tecnologia para 2027](../referencia/bibliografia.md#gartner-top-strategic-technology-trends-for-2027-2026) inclui plataformas para fornecer contexto aos agentes, plataformas para controlar a execução de agentes de programação e identidade própria para agentes nos sistemas da empresa. Uma [previsão de 2025](../referencia/bibliografia.md#gartner-previsao-de-cancelamento-de-projetos-agenticos-2025) estima que mais de 40% dos projetos com agentes serão cancelados até o fim de 2027 por custo alto, valor pouco claro ou controles insuficientes. Uma [análise de 107 casos públicos](../referencia/bibliografia.md#gartner-mastering-agentic-ai-2026) prevê que agentes especializados num assunto responderão por 80% do retorno financeiro mensurável até 2028.

A Forrester publicou o resumo do estudo [The State of Agentic AI, 2026](../referencia/bibliografia.md#forrester-the-state-of-agentic-ai-2026), que associa a dificuldade de ampliar o uso de agentes à coordenação entre agentes, a regras de governança aplicadas automaticamente e à identidade de sistemas que agem sem uma pessoa. Nas [previsões para 2027](../referencia/bibliografia.md#forrester-predictions-2027-2026), a Forrester estima que a IA receberá 20% dos gastos de tecnologia das áreas de negócio em 2027.

| Afirmação | Tipo |
|---|---|
| 40% das grandes organizações usam agentes em escala em pelo menos uma área | Resultado de estudo baseado em respostas declaradas |
| 32% desistiram de comprar software por construí-lo com agentes | Resultado de estudo baseado em respostas declaradas |
| Mais de 40% dos projetos com agentes serão cancelados até o fim de 2027 | Previsão de analista |
| Agentes especializados responderão por 80% do retorno até 2028 | Previsão de analista |
| IA receberá 20% dos gastos de tecnologia das áreas de negócio em 2027 | Previsão de analista |

McKinsey, Gartner e Forrester recomendam escolher processos cujo resultado possa ser conferido, medir o custo completo do uso de agentes e aplicar os controles durante a operação. Os relatórios completos da Forrester e de parte do Gartner são pagos, e os números desta página vêm dos resumos públicos.

## Estudos publicados em 2026

O estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), apresentado na conferência acadêmica ICML em 2026, analisou 20 casos e entrevistou 86 profissionais responsáveis por agentes em uso real, em 26 áreas de atuação. Em 68% dos sistemas, o agente executava no máximo dez passos antes de uma pessoa intervir, e os participantes apontaram a confiabilidade como a principal dificuldade. Os sistemas estudados não representam todas as empresas, mas o resultado indica que o uso atual se concentra em tarefas curtas e fáceis de conferir.

Uma [avaliação do Google Research](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) comparou 180 configurações de sistemas com um ou mais agentes. Vários agentes trabalhando juntos melhoraram o resultado em tarefas que podem ser divididas em partes independentes e pioraram o resultado em tarefas em que cada passo depende do anterior. A recomendação prática é começar com um agente e acrescentar outros apenas quando houver partes independentes, necessidade de informações separadas ou responsabilidades que precisem ficar isoladas.

O METR, organização independente que mede a capacidade de modelos de IA, publicou em 2025 um [experimento](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025), apresentado na Sessão 1, em que desenvolvedores experientes levaram 19% mais tempo para concluir tarefas com IA em projetos que já conheciam. Em fevereiro de 2026, o METR [informou](../referencia/bibliografia.md#metr-mudanca-no-desenho-do-experimento-de-produtividade-2026) que a nova rodada do experimento teve problemas na seleção dos participantes e na medição, e que o resultado de 2025 vale apenas para desenvolvedores experientes, projetos conhecidos e as ferramentas do início de 2025.

O METR também publica uma medida chamada horizonte de tarefa, que indica a duração das tarefas que um agente completa com 50% de sucesso. Numa [nota de janeiro de 2026](../referencia/bibliografia.md#metr-clarifying-limitations-of-time-horizon-2026), a organização explicou que essa medida não significa que o agente execute com segurança qualquer tarefa daquela duração, porque metade das tentativas ainda falha.

## Ganho num caso, nota em benchmark e efeito no processo

O ganho medido num caso isolado, a nota de um modelo num *benchmark* (conjunto padronizado de tarefas usado para comparar modelos) e o efeito do agente no processo completo da empresa são medidas diferentes. Apenas a terceira indica se o uso do agente reduz custo ou prazo para a organização, e por isso é a medida usada no plano de 90 dias desta sessão.

**Próxima página:** [Mudanças esperadas para 2027 a 2030](mudancas-esperadas-2027-2030.md).
