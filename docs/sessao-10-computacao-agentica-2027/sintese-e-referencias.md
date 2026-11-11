# Síntese e referências

## Ideias essenciais

1. **A unidade de delegação passa a ser a tarefa concluída e aceita.** Computação agêntica designa sistemas que escolhem ações, operam ferramentas, observam resultados e ajustam a execução para um objetivo, e a delegação se completa quando o processo aceita o resultado, conforme a página [Da interação à delegação](da-interacao-a-delegacao.md#o-ciclo-do-objetivo-ao-resultado-aceito).
2. **As quatro formas de delegação diferem pelo responsável pelo próximo passo.** Resposta assistida, fluxo de trabalho com IA, agente com autonomia delimitada e sistema com múltiplos agentes convivem no mesmo processo, e a escolha de cada etapa segue o princípio de simplicidade da Sessão 1.
3. **Pesquisa, caso relatado, piloto, capacidade de produto, previsão e hipótese têm alcances diferentes.** A página [Evidência e previsão](evidencia-e-previsao.md#seis-tipos-de-afirmacao) mostra por que somar esses tipos numa taxa única de maturidade produz um número sem significado.
4. **A produção atual delega unidades curtas e verificáveis.** Na amostra de [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), 68% dos sistemas executavam no máximo dez passos antes de intervenção humana, e a [avaliação do Google Research](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) encontrou degradação com múltiplos agentes em tarefas sequenciais.
5. **Cada uma das onze tendências tem uma condição crítica.** Execução persistente exige idempotência, memória exige origem e validade, identidade exige critério de negócio, e engenharia por delegação exige limite de trabalho em andamento e medida de tempo até a mudança aceita, conforme a página [Tendências para 2027 a 2030](tendencias-2027-2030.md).
6. **A convergência de produtos de assistentes proativos está mais demonstrada do que o ganho econômico sustentado.** O teste proposto acompanha a mesma responsabilidade por oito a doze semanas, com entregas aceitas, alertas descartados, minutos de supervisão e gasto total.
7. **A arquitetura separa estado, arnês, ambiente, autorização e sistema de registro.** Persistir conversa, preservar arquivos e recuperar uma execução são propriedades diferentes, e a autorização fica num *gateway* que o modelo não altera, como descreve a página [Arquitetura de referência](arquitetura-de-referencia.md#responsabilidades-da-arquitetura).
8. **O custo por resultado aceito inclui supervisão e retrabalho e vem acompanhado de contramétricas.** No Experimento C da oficina, o custo por resultado aceito caiu cerca de 27% enquanto as reaberturas subiram de 4 para 18 no mês, e a decisão correta foi corrigir o piloto antes de ampliá-lo.
9. **O plano de 90 dias condiciona cada passagem à evidência do processo.** Linha de base no primeiro mês, execução delimitada no segundo e comparação no terceiro, com a decisão de ampliar, corrigir ou interromper tomada pela liderança a partir dos dados.

## Checklist antes de encerrar o curso

- [ ] Sei classificar uma afirmação sobre agentes em um dos seis tipos e formular a pergunta que falta para usá-la.
- [ ] Sei apontar, para pelo menos quatro tendências, a sessão do curso em que pratiquei a capacidade correspondente.
- [ ] Sei identificar, numa arquitetura de agente, onde ficam o estado pendente, a autorização e o sistema de registro.
- [ ] Sei calcular o custo por resultado aceito e escolher a contramétrica que o acompanha.
- [ ] Tenho uma ficha de piloto de 90 dias preenchida para um processo da ACME e revisada numa conversa separada.
- [ ] Sei o que a equipe precisa medir antes de propor um piloto real em 2027.

## Autoavaliação

Responda "sim" ou "ainda não" a cada pergunta.

1. Diante de um percentual de caso relatado, consigo dizer quem mediu, contra qual base, o que mais mudou no período e se o número é máximo, média ou período inicial?
2. Consigo explicar por que retomar uma execução não impede a duplicação de uma ação externa?
3. Consigo explicar por que um assistente proativo pode aumentar a fila de aprovação de um processo?
4. Consigo escrever um critério de passagem do dia 60 que seja verificável naquele dia?
5. Consigo justificar a escolha da forma de delegação de cada etapa de um processo pelo princípio de simplicidade?

Se duas ou mais respostas forem "ainda não", a releitura de [Evidência e previsão](evidencia-e-previsao.md) e de [Métricas e economia](metricas-e-economia.md) cobre a maior parte das lacunas, e a [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md) cobre as lacunas sobre controles.

## Depois do curso

O relatório registra sinais que confirmam ou enfraquecem as tendências, e a equipe pode revisá-los a cada trimestre de 2027 para decidir se o cenário base, o de aceleração ou o de adoção restrita está se confirmando.

| Tendência | Sinal a acompanhar |
|---|---|
| 4.1 Agentes persistentes | A hipótese enfraquece se os produtos continuarem limitados a sessões frágeis, com retomada manual cara e baixa aceitação de tarefas concluídas |
| 4.4 Interoperabilidade | A tendência se confirma com transações entre agentes de fornecedores diferentes, com responsabilidade e resultado verificáveis |
| 4.5 Engenharia por delegação | O sinal contrário é o aumento persistente de retrabalho, vulnerabilidades e filas de revisão anulando o ganho de implementação |
| 4.10 Comércio e pagamentos | A maturidade aparece em pagamentos recorrentes em operação regular, com métricas de falha e de disputa |
| 4.11 Ciência e robótica | A tendência se confirma com repetição independente de resultados científicos e operação industrial estável com menos intervenção humana por tarefa |
| Assistentes proativos | A hipótese enfraquece com queda do uso depois da novidade, revisão igual ou maior que o tempo poupado, limites de consumo impedindo a rotina ou automação mais simples entregando o mesmo resultado |

## Fundamentação

A sessão parte do relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026), com corte em 10/11/2026, e cita diretamente as fontes primárias que o relatório usa em cada argumento.

| Fonte | Tipo de afirmação | Onde é usada |
|---|---|---|
| [Anthropic, Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) | Orientação técnica do fornecedor | Da interação à delegação |
| [Pan et al., Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026) | Evidência empírica | Da interação à delegação, Evidência e previsão |
| [McKinsey, The State of AI in 2026](../referencia/bibliografia.md#mckinsey-the-state-of-ai-in-2026-2026) | Pesquisa sem auditoria | Evidência e previsão |
| [McKinsey, Where AI Agents Pay Off](../referencia/bibliografia.md#mckinsey-where-ai-agents-pay-off-2026) | Análise econômica | Métricas e economia |
| [Gartner, Top Strategic Technology Trends for 2027](../referencia/bibliografia.md#gartner-top-strategic-technology-trends-for-2027-2026) | Previsão de analista | Evidência e previsão |
| [Gartner, previsão de cancelamento de projetos agênticos](../referencia/bibliografia.md#gartner-previsao-de-cancelamento-de-projetos-agenticos-2025) | Previsão de analista | Evidência e previsão |
| [Gartner, Mastering Agentic AI](../referencia/bibliografia.md#gartner-mastering-agentic-ai-2026) | Previsão de analista | Evidência e previsão |
| [Forrester, The State of Agentic AI](../referencia/bibliografia.md#forrester-the-state-of-agentic-ai-2026) | Resumo público de relatório comercial | Evidência e previsão |
| [Forrester, Predictions 2027](../referencia/bibliografia.md#forrester-predictions-2027-2026) | Previsão de analista | Evidência e previsão |
| [Google Research, Towards a Science of Scaling Agent Systems](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) | Evidência empírica | Evidência e previsão |
| [METR, experimento de 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025) | Evidência empírica | Evidência e previsão |
| [METR, mudança no desenho do experimento](../referencia/bibliografia.md#metr-mudanca-no-desenho-do-experimento-de-produtividade-2026) | Atualização metodológica | Evidência e previsão |
| [METR, limitações do horizonte de tarefa](../referencia/bibliografia.md#metr-clarifying-limitations-of-time-horizon-2026) | Nota metodológica | Evidência e previsão |
| [Anthropic, Scaling Managed Agents](../referencia/bibliografia.md#anthropic-scaling-managed-agents-2026) | Capacidade de produto | Tendências, Arquitetura de referência |
| [Temporal, Durable AI](../referencia/bibliografia.md#temporal-durable-ai-documentacao) | Capacidade de produto | Tendências, Arquitetura de referência |
| [Anthropic, Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) | Capacidade de produto | Tendências |
| [Anthropic, Code Execution with MCP](../referencia/bibliografia.md#anthropic-code-execution-with-mcp-2025) | Orientação técnica do fornecedor | Tendências |
| [Microsoft, Entra Agent ID](../referencia/bibliografia.md#microsoft-entra-agent-id-documentacao) | Capacidade de produto | Tendências |
| [AWS, AgentCore Policy e Evaluations](../referencia/bibliografia.md#aws-bedrock-agentcore-policy-e-evaluations-2025) | Capacidade de produto | Tendências |
| [A2A Project, Agent2Agent Protocol](../referencia/bibliografia.md#a2a-project-agent2agent-protocol-documentacao) | Especificação de protocolo | Tendências |
| [Agentic AI Foundation, AGENTS.md](../referencia/bibliografia.md#agentic-ai-foundation-agentsmd-standard) | Especificação | Tendências |
| [Anthropic, Claude Duet](../referencia/bibliografia.md#anthropic-introducing-claude-duet-2026) | Capacidade de produto | Assistentes proativos |
| [xAI, Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao) | Capacidade de produto | Assistentes proativos, Arquitetura de referência |
| [OpenAI, dots](../referencia/bibliografia.md#openai-introducing-dots-2026) | Capacidade de produto | Assistentes proativos |
| [Meta, Muse](../referencia/bibliografia.md#meta-introducing-muse-2026) | Capacidade de produto | Assistentes proativos |
| [Reuters, Muse e o concierge humano](../referencia/bibliografia.md#reuters-muse-e-o-concierge-humano-2026) | Reportagem sobre episódio específico | Assistentes proativos |
| [Cognition, Itaú](../referencia/bibliografia.md#cognition-devin-em-sao-paulo-2026) | Caso relatado pelo fornecedor | Casos reais |
| [Nubank, skills como dependências](../referencia/bibliografia.md#nubank-when-ai-skills-become-supply-chain-dependencies-2026) | Caso relatado pela organização | Casos reais |
| [Google Cloud, Bradesco](../referencia/bibliografia.md#google-cloud-gemini-at-work-2026) | Caso relatado pelo fornecedor | Casos reais |
| [Microsoft, Ask Microsoft](../referencia/bibliografia.md#microsoft-ask-microsoft-com-copilot-studio-2026) | Caso relatado pelo fornecedor | Casos reais |
| [Salesforce, OpenTable](../referencia/bibliografia.md#salesforce-opentable-com-agentforce-2025) | Caso relatado pelo fornecedor | Casos reais |
| [AWS, Cox Automotive](../referencia/bibliografia.md#aws-cox-automotive-2026) | Caso relatado pelo fornecedor | Casos reais |
| [ServiceNow, Thrive](../referencia/bibliografia.md#servicenow-thrive-2026) | Caso relatado pelo fornecedor | Casos reais |
| [Visa, piloto de pagamentos](../referencia/bibliografia.md#visa-piloto-de-pagamentos-por-agentes-2026) | Piloto | Tendências, Casos reais |
| [BMW Group, robôs humanoides](../referencia/bibliografia.md#bmw-group-robos-humanoides-2026) | Piloto | Tendências, Casos reais |
| [Google DeepMind, Co-Scientist](../referencia/bibliografia.md#google-deepmind-co-scientist-2026) | Pesquisa e experimentação | Tendências, Casos reais |
| [OWASP, Top 10 for Agentic Applications](../referencia/bibliografia.md#owasp-top-10-for-agentic-applications-2026) | Referencial comunitário de riscos | Arquitetura de referência |
| [NIST, AI Agent Standards Initiative](../referencia/bibliografia.md#nist-ai-agent-standards-initiative-2026) | Iniciativa de padronização | Arquitetura de referência |
| [Anthropic, Demystifying Evals for AI Agents](../referencia/bibliografia.md#anthropic-demystifying-evals-for-ai-agents-2026) | Orientação técnica do fornecedor | Métricas e economia |

Os relatórios integrais da Forrester e alguns do Gartner são comerciais, e o relatório de origem usou apenas os resumos e comentários públicos citados. Os resultados de casos não passaram por auditoria independente, e os endereços de documentação de produto podem mudar depois da consulta de 10/11/2026.

## Conexão com as sessões anteriores

Esta sessão encerra o workshop retomando as nove anteriores pela mesma pergunta: o que o agente pode decidir sozinho, com que contexto e com qual evidência de resultado. O arnês e o erro composto da [Sessão 2](../sessao-02-ambiente-agentico/index.md) reaparecem na arquitetura de referência e na confiabilidade do processo, a especificação e as regras formais das [Sessões 3](../sessao-03-exploracao-especificacao/index.md) e [4](../sessao-04-regras-formais-com-ia/index.md) reaparecem nos critérios de aceite e nos passos determinísticos dos processos híbridos, o teste antes do código da [Sessão 6](../sessao-06-spec-kit-aprofundado/index.md) reaparece na validação que a engenharia por delegação pressiona, e a ficha de requisitos da [Sessão 8](../sessao-08-skills-e-agentes/index.md) e a ficha de governança da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md) compõem os campos da ficha de piloto de 90 dias preparada na oficina.
