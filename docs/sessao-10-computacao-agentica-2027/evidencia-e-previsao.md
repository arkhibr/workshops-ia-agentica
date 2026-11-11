# Evidência e previsão

Relatórios de consultoria, anúncios de fornecedores e reportagens sobre agentes publicam afirmações de tipos diferentes, como respostas de pesquisa, casos selecionados pelo fornecedor e previsões para datas futuras. Esta página apresenta a classificação de afirmações do relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) e a aplica às publicações de McKinsey, Gartner e Forrester e a três estudos empíricos de 2026.

## Seis tipos de afirmação

| Tipo | Significado | Limite |
|---|---|---|
| Evidência empírica | Estudo com método e amostra descritos | Vale para a população e as tarefas estudadas |
| Caso operacional relatado | Cliente ou fornecedor descreve uma implementação e o resultado dela | Pode não ter atribuição causal nem auditoria independente |
| Piloto | Experiência delimitada em ambiente real | Não demonstra disponibilidade geral nem escala |
| Capacidade de produto | Documentação ou anúncio oficial | Não demonstra retorno financeiro para o comprador |
| Previsão de analista | Expectativa publicada para uma data futura | Ainda não foi observada |
| Hipótese | Inferência sobre direção e condições de adoção | Precisa de sinais definidos que possam refutá-la |

A [Sessão 1](../sessao-01-o-que-mudou/avaliacao-de-modelos.md) aplicou o mesmo cuidado aos placares de modelos, em que o número publicado pelo fabricante e a medição independente têm confiabilidade diferente. Os termos adoção, produção, escala em uma função e escala na empresa também descrevem situações diferentes e não podem ser somados numa taxa única de maturidade.

## Publicações de McKinsey, Gartner e Forrester

![Três colunas com as contribuições das consultorias. McKinsey tem foco em adoção e resultado econômico, recomenda verificar o custo integral por resultado e alerta que pesquisa não é auditoria. Gartner tem foco em contexto, harness e identidade, recomenda verificar os controles da execução e alerta que previsão não é taxa observada. Forrester tem foco em prontidão operacional, recomenda verificar governança e orquestração e alerta que tecnologia exige organização. A faixa inferior soma valor econômico, capacidade de plataforma e responsabilidade operacional.](assets/tres-condicoes-para-escalar.png)

| Publicação | Afirmação | Tipo |
|---|---|---|
| McKinsey, [The State of AI in 2026](../referencia/bibliografia.md#mckinsey-the-state-of-ai-in-2026-2026) | 40% dos respondentes de organizações com receita anual acima de US$ 1 bilhão relatam escalar agentes em pelo menos uma função, contra 22% nas organizações menores | Resposta de pesquisa com 1.719 participantes de 97 países, coletada entre maio e junho de 2026, sem auditoria |
| McKinsey, mesma pesquisa | 32% dos respondentes desistiram de comprar pelo menos um produto ou funcionalidade porque conseguiram construí-lo com agentes de código | Resposta de pesquisa sobre decisões de construir ou comprar, sem estimativa de efeito no mercado de software |
| Gartner, [tendências estratégicas para 2027](../referencia/bibliografia.md#gartner-top-strategic-technology-trends-for-2027-2026) | *AI context platforms*, *AI coding agent harness* e *AI agent identity* estão entre as tendências de 2027 | Previsão de analista |
| Gartner, [previsão de 2025](../referencia/bibliografia.md#gartner-previsao-de-cancelamento-de-projetos-agenticos-2025) | Mais de 40% dos projetos agênticos serão cancelados até o fim de 2027 por custo, valor indefinido ou controles insuficientes | Previsão de analista |
| Gartner, [análise de 107 exemplos públicos](../referencia/bibliografia.md#gartner-mastering-agentic-ai-2026) | Agentes especializados responderão por 80% do retorno tangível até 2028 | Previsão de analista |
| Forrester, [The State of Agentic AI, 2026](../referencia/bibliografia.md#forrester-the-state-of-agentic-ai-2026) | A dificuldade de escalar agentes está associada a orquestração, governança executável e identidade não humana | Resumo público de relatório comercial |
| Forrester, [previsões para 2027](../referencia/bibliografia.md#forrester-predictions-2027-2026) | IA receberá 20% dos gastos de tecnologia de negócios em 2027, e uma em cada quatro iniciativas de camada de contexto sustentará agentes em produção | Previsão de analista |

As três consultorias recomendam escolher processos com resultado verificável, medir o custo integral e aplicar os controles na operação. O relatório de origem consultou apenas os resumos e comentários públicos dos relatórios comerciais da Forrester e de parte dos relatórios do Gartner.

## Três estudos empíricos de 2026

O estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), publicado na ICML 2026, reúne 20 estudos de caso e uma pesquisa com 86 profissionais responsáveis por sistemas em produção em 26 domínios. Na amostra, 68% dos sistemas executavam no máximo dez passos antes de uma intervenção humana, e os participantes apontaram a confiabilidade como o principal desafio. A amostra não representa o conjunto das empresas, e o relatório usa o resultado como base para a hipótese de que a adoção cresce primeiro em tarefas delimitadas e verificáveis.

A [avaliação do Google Research](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) comparou 180 configurações de sistemas de agentes e encontrou melhora com coordenação de vários agentes em tarefas paralelizáveis e piora em tarefas predominantemente sequenciais. O relatório deriva desse resultado a recomendação de começar pelo menor desenho que resolve o problema e acrescentar agentes somente quando houver necessidade de paralelismo, contexto separado, ferramenta especializada ou isolamento de responsabilidade.

O [experimento do METR de 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025), apresentado na Sessão 1, mediu que desenvolvedores experientes levaram 19% mais tempo com IA em repositórios que já conheciam. Em fevereiro de 2026, o METR [informou](../referencia/bibliografia.md#metr-mudanca-no-desenho-do-experimento-de-produtividade-2026) que a nova rodada do experimento apresentava efeitos de seleção e dificuldades de medição, e que o resultado de 2025 se limita a desenvolvedores experientes, repositórios conhecidos e ferramentas do início de 2025. Numa nota de janeiro de 2026, o METR [registrou](../referencia/bibliografia.md#metr-clarifying-limitations-of-time-horizon-2026) que um horizonte de tarefa medido a 50% de sucesso não autoriza delegar com confiabilidade qualquer trabalho daquela duração.

Para a decisão de investimento da equipe, o relatório distingue o ganho medido num caso, o desempenho num *benchmark* e o efeito econômico no fluxo completo do processo, e só o último indica retorno para a organização.

**Próxima página:** [Tendências para 2027 a 2030](tendencias-2027-2030.md).
