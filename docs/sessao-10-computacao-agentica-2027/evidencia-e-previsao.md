# Evidência e previsão

As afirmações sobre agentes que circulam em relatórios de consultoria, anúncios de fornecedores e reportagens têm naturezas diferentes, e somar uma pesquisa de opinião, um caso selecionado por fornecedor e uma previsão de analista numa taxa única de maturidade produz um número sem significado. Esta página apresenta a classificação de afirmações adotada no relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) e a aplica às leituras de McKinsey, Gartner e Forrester e aos estudos empíricos mais recentes.

## Seis tipos de afirmação

| Tipo | Significado | Limite |
|---|---|---|
| Evidência empírica | Estudo com método e amostra descritos | Vale para a população e as tarefas estudadas |
| Caso operacional relatado | Cliente ou fornecedor identifica implementação e resultado | A atribuição causal e a auditoria independente podem faltar |
| Piloto | Experiência delimitada em ambiente real | Não demonstra disponibilidade nem escala generalizada |
| Capacidade de produto | Documentação ou anúncio oficial | Não prova retorno financeiro para o comprador |
| Previsão de analista | Expectativa publicada para uma data futura | Descreve uma expectativa e ainda não foi observada |
| Hipótese | Inferência sobre direção e condições de adoção | Precisa ser acompanhada por sinais que possam refutá-la |

A classificação aplica à leitura de mercado o mesmo cuidado que a [Sessão 1](../sessao-01-o-que-mudou/avaliacao-de-modelos.md) aplicou à leitura de placares de modelos, em que um número autorreportado pelo fabricante e uma medição independente recebem pesos diferentes. Termos como adoção, produção, escala em uma função e escala na empresa também designam situações diferentes e não podem ser usados como sinônimos.

## Três leituras complementares do mercado

![Três colunas com as contribuições das consultorias. McKinsey tem foco em adoção e resultado econômico, recomenda verificar o custo integral por resultado e alerta que pesquisa não é auditoria. Gartner tem foco em contexto, harness e identidade, recomenda verificar os controles da execução e alerta que previsão não é taxa observada. Forrester tem foco em prontidão operacional, recomenda verificar governança e orquestração e alerta que tecnologia exige organização. A faixa inferior soma valor econômico, capacidade de plataforma e responsabilidade operacional.](assets/tres-condicoes-para-escalar.png)

**McKinsey, adoção e resultado econômico.** A pesquisa [The State of AI in 2026](../referencia/bibliografia.md#mckinsey-the-state-of-ai-in-2026-2026) reuniu 1.719 participantes de 97 países, com coleta entre maio e junho de 2026. Entre respondentes de organizações com receita anual superior a US$ 1 bilhão, 40% relatam escalar agentes em uma ou mais funções, contra 22% nas organizações menores. A mesma pesquisa registra que 32% dos respondentes desistiram da compra de pelo menos um produto ou funcionalidade por conseguir construí-lo com agentes de código, dado que descreve decisões de construir ou comprar e não estima redução do mercado de software. Os dois percentuais são respostas declaradas pelos participantes da pesquisa de 2026, sem auditoria das implantações descritas.

**Gartner, arquitetura para operar autonomia.** A lista de [tendências estratégicas para 2027](../referencia/bibliografia.md#gartner-top-strategic-technology-trends-for-2027-2026) destaca *AI context platforms*, *AI coding agent harness* e *AI agent identity*, o que coloca contexto, arnês de execução e autorização entre as capacidades de plataforma. Uma [previsão publicada em 2025](../referencia/bibliografia.md#gartner-previsao-de-cancelamento-de-projetos-agenticos-2025) estima que mais de 40% dos projetos agênticos serão cancelados até o fim de 2027, por custo, valor indefinido e controles insuficientes, e uma [análise de 107 exemplos públicos](../referencia/bibliografia.md#gartner-mastering-agentic-ai-2026) prevê que agentes especializados responderão por 80% do retorno tangível até 2028.

**Forrester, capacidade organizacional.** O resumo público de [The State of Agentic AI, 2026](../referencia/bibliografia.md#forrester-the-state-of-agentic-ai-2026) associa a dificuldade de escalar à orquestração, à governança executável e à identidade não humana. As [previsões para 2027](../referencia/bibliografia.md#forrester-predictions-2027-2026) acrescentam contexto e adaptação do modelo operacional como barreiras, projetam que IA receberá 20% dos gastos de tecnologia de negócios em 2027 e estimam que apenas uma em cada quatro iniciativas de camada de contexto sustentará agentes em produção.

As três leituras convergem na recomendação de escolher processos com resultado verificável, medir o custo integral e tornar os controles operacionais. Os relatórios integrais da Forrester e alguns do Gartner são comerciais, e o relatório de origem usou apenas os resumos e comentários públicos citados.

## Alcance dos estudos empíricos

**A produção continua exigindo controle.** O estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), publicado na ICML 2026, reúne 20 estudos de caso e uma pesquisa com 86 profissionais de sistemas implantados em 26 domínios. Na amostra, 68% dos sistemas executavam no máximo dez passos antes de intervenção humana, e a confiabilidade aparece como o desafio central. A amostra descreve práticas reais e não é um censo das empresas, o que sustenta a hipótese de que a expansão ocorre primeiro por muitas tarefas delimitadas e verificáveis.

**Mais agentes exigem justificativa técnica.** A [avaliação do Google Research](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) com 180 configurações encontrou benefício de coordenação em tarefas paralelizáveis e degradação em tarefas predominantemente sequenciais, com resultados dependentes da arquitetura e dos *benchmarks* utilizados. A recomendação decorrente é começar pelo menor desenho que resolve o problema e acrescentar agentes quando houver necessidade demonstrável de paralelismo, contexto separado, ferramentas especializadas ou isolamento de responsabilidades.

**A produtividade precisa ser medida de novo.** A Sessão 1 apresentou o [experimento do METR de 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025), em que desenvolvedores experientes levaram 19% mais tempo com IA em repositórios que conheciam. Em fevereiro de 2026, o METR [informou](../referencia/bibliografia.md#metr-mudanca-no-desenho-do-experimento-de-produtividade-2026) que a nova rodada do experimento sofria efeitos de seleção e dificuldades de medição, e que o resultado de 2025 vale para desenvolvedores experientes, repositórios conhecidos e ferramentas do início de 2025, sem sustentar uma medida geral para as ferramentas de 2026. O METR também [registrou](../referencia/bibliografia.md#metr-clarifying-limitations-of-time-horizon-2026) que um horizonte de tarefa medido a 50% de sucesso não significa que um agente receba com confiabilidade qualquer trabalho daquela duração.

O ganho observado num caso, o desempenho num *benchmark* e o impacto econômico no fluxo completo são, portanto, três evidências diferentes, e a decisão de investimento da equipe precisa da terceira.

**Próxima página:** [Tendências para 2027 a 2030](tendencias-2027-2030.md).
