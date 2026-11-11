# Síntese e referências

## Ideias essenciais

1. **Trabalho delegado concluído.** O trabalho entregue a um agente termina quando o processo aceita o resultado, depois de uma verificação e, quando exigido, da aprovação de uma pessoa, conforme a página [Formas de delegar trabalho à IA](formas-de-delegar-trabalho.md#quando-o-trabalho-delegado-termina).
2. **Formas de delegar.** Na resposta assistida a pessoa escolhe o próximo passo, no fluxo de trabalho com IA um programa segue uma sequência fixa, no agente com autonomia delimitada o agente escolhe dentro de limites, e com vários agentes coordenados cada agente cuida de uma parte. Um mesmo processo pode usar formas diferentes em etapas diferentes.
3. **Tipos de afirmação.** Resultado de estudo, relato de empresa, piloto, anúncio de produto, previsão de analista e hipótese permitem conclusões diferentes e não podem ser somados numa taxa única de adoção, conforme a página [Avaliação de números e promessas sobre agentes](avaliacao-de-numeros-e-promessas.md#tipos-de-afirmacao-sobre-agentes).
4. **Uso atual de agentes.** No estudo [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), 68% dos sistemas em uso real executavam no máximo dez passos antes de uma pessoa intervir, e a [avaliação do Google Research](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) mostrou piora com vários agentes em tarefas em que cada passo depende do anterior.
5. **Condições das mudanças esperadas.** Agentes que retomam o trabalho depois de falhas precisam de operações idempotentes, que produzem o mesmo efeito se repetidas, informações fornecidas ao agente precisam de origem e validade, e agentes que escrevem código exigem limite de alterações em andamento, conforme a página [Mudanças esperadas para 2027 a 2030](mudancas-esperadas-2027-2030.md).
6. **Assistentes proativos.** Quatro fornecedores lançaram assistentes que agem sem receber pedido entre setembro e outubro de 2026, e o ganho para quem usa ainda não foi medido de forma independente, o que pode ser testado com um piloto de oito a doze semanas.
7. **Componentes de controle.** Um agente que altera sistemas da empresa precisa de um fluxo de trabalho que guarde o andamento, de um *gateway* que aplique as permissões fora do agente e de um registro das ações, conforme a página [Componentes de um agente que age com controle](componentes-de-um-agente-com-controle.md#funcao-de-cada-componente).
8. **Custo por resultado aceito.** A métrica inclui supervisão e retrabalho e vem acompanhada de medidas de efeito colateral, e no Experimento C da oficina o custo por resultado caiu cerca de 27% enquanto as reaberturas subiram de 4 para 18 no mês.
9. **Plano de 90 dias.** O piloto mede o processo atual no primeiro mês, testa o agente com escopo limitado no segundo e compara os resultados no terceiro, quando a liderança decide ampliar, corrigir ou interromper.

## Checklist antes de encerrar o curso

- [ ] Sei classificar uma afirmação sobre agentes num dos tipos de afirmação e formular a pergunta que falta para usá-la numa decisão.
- [ ] Sei apontar, para pelo menos quatro das onze mudanças esperadas, a sessão do curso em que pratiquei algo relacionado.
- [ ] Sei identificar, no desenho de um agente, onde fica o andamento do trabalho, quem autoriza as ações e onde ficam os dados oficiais.
- [ ] Sei calcular o custo por resultado aceito e escolher a medida de efeito colateral que o acompanha.
- [ ] Tenho uma ficha de piloto de 90 dias preenchida para um processo da ACME e revisada numa conversa separada.
- [ ] Sei o que a equipe precisa medir antes de propor um piloto real em 2027.

## Autoavaliação

Responda "sim" ou "ainda não" a cada pergunta.

1. Diante de um percentual publicado por uma empresa, consigo dizer quem mediu, contra o que comparou, o que mais mudou no período e se o número é o maior valor, a média ou um período inicial?
2. Consigo explicar por que um agente que retoma o trabalho depois de uma falha pode registrar a mesma operação duas vezes?
3. Consigo explicar por que um assistente proativo pode aumentar a fila de aprovação de um processo?
4. Consigo escrever um critério de passagem do dia 60 que possa ser verificado naquele dia?
5. Consigo justificar a forma de delegação de cada etapa de um processo pela preferência pela forma mais simples que resolve a etapa?

Se duas ou mais respostas forem "ainda não", a releitura de [Avaliação de números e promessas sobre agentes](avaliacao-de-numeros-e-promessas.md) e de [Medição do custo e do resultado de um agente](medicao-de-custo-e-resultado.md) cobre a maior parte das lacunas, e a [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md) cobre as lacunas sobre controles.

## Sinais a acompanhar depois do curso

A tabela lista, para parte das mudanças esperadas e para os assistentes proativos, os sinais que confirmam ou enfraquecem cada uma. A equipe pode revisar a tabela a cada trimestre de 2027 para identificar qual dos três cenários da página [Plano de 90 dias para testar um agente](plano-de-90-dias.md#cenarios-de-adocao-ate-2030) está acontecendo.

| Mudança | Sinal a acompanhar |
|---|---|
| 4.1 Agentes que continuam trabalhando depois da conversa | A mudança perde força se os produtos continuarem perdendo o andamento do trabalho em falhas, com retomada manual cara e poucas tarefas aceitas |
| 4.4 Padrões para conectar agentes e empresas | A mudança se confirma quando agentes de fornecedores diferentes concluírem transações entre si, com responsável e resultado conferível |
| 4.5 Desenvolvimento de software por agentes | O sinal contrário é o crescimento persistente de retrabalho, falhas de segurança e fila de revisão, anulando o ganho na escrita de código |
| 4.10 Compras e pagamentos feitos por agentes | A mudança se confirma com pagamentos recorrentes em operação normal, com taxas de falha e de contestação publicadas |
| 4.11 Pesquisa científica e robôs | A mudança se confirma quando outros laboratórios repetirem os resultados científicos e quando robôs operarem de forma estável com menos intervenção humana por tarefa |
| Assistentes proativos | A mudança perde força com queda do uso depois das primeiras semanas, revisão igual ou maior que o tempo poupado, limite de uso impedindo a rotina ou automação simples entregando o mesmo resultado |

## Fontes citadas nesta sessão

| Fonte | Tipo de afirmação | Página em que é usada |
|---|---|---|
| [Anthropic, Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) | Orientação técnica de fornecedor | Quatro formas de delegar |
| [Pan et al., Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026) | Resultado de estudo | Quatro formas de delegar, Avaliação de números e promessas |
| [McKinsey, The State of AI in 2026](../referencia/bibliografia.md#mckinsey-the-state-of-ai-in-2026-2026) | Resultado de estudo com respostas declaradas | Avaliação de números e promessas |
| [McKinsey, Where AI Agents Pay Off](../referencia/bibliografia.md#mckinsey-where-ai-agents-pay-off-2026) | Análise econômica | Medição do custo e do resultado |
| [Gartner, Top Strategic Technology Trends for 2027](../referencia/bibliografia.md#gartner-top-strategic-technology-trends-for-2027-2026) | Previsão de analista | Avaliação de números e promessas |
| [Gartner, previsão de cancelamento de projetos agênticos](../referencia/bibliografia.md#gartner-previsao-de-cancelamento-de-projetos-agenticos-2025) | Previsão de analista | Avaliação de números e promessas |
| [Gartner, Mastering Agentic AI](../referencia/bibliografia.md#gartner-mastering-agentic-ai-2026) | Previsão de analista | Avaliação de números e promessas |
| [Forrester, The State of Agentic AI](../referencia/bibliografia.md#forrester-the-state-of-agentic-ai-2026) | Resumo público de relatório comercial | Avaliação de números e promessas |
| [Forrester, Predictions 2027](../referencia/bibliografia.md#forrester-predictions-2027-2026) | Previsão de analista | Avaliação de números e promessas |
| [Google Research, Towards a Science of Scaling Agent Systems](../referencia/bibliografia.md#google-research-towards-a-science-of-scaling-agent-systems-2026) | Resultado de estudo | Avaliação de números e promessas |
| [METR, experimento de 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025) | Resultado de estudo | Avaliação de números e promessas |
| [METR, mudança no desenho do experimento](../referencia/bibliografia.md#metr-mudanca-no-desenho-do-experimento-de-produtividade-2026) | Atualização metodológica | Avaliação de números e promessas |
| [METR, limitações do horizonte de tarefa](../referencia/bibliografia.md#metr-clarifying-limitations-of-time-horizon-2026) | Nota metodológica | Avaliação de números e promessas |
| [Anthropic, Scaling Managed Agents](../referencia/bibliografia.md#anthropic-scaling-managed-agents-2026) | Anúncio de produto | Onze mudanças esperadas, Componentes de um agente com controle |
| [Temporal, Durable AI](../referencia/bibliografia.md#temporal-durable-ai-documentacao) | Anúncio de produto | Onze mudanças esperadas, Componentes de um agente com controle |
| [Anthropic, Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) | Anúncio de produto | Onze mudanças esperadas |
| [Anthropic, Code Execution with MCP](../referencia/bibliografia.md#anthropic-code-execution-with-mcp-2025) | Orientação técnica de fornecedor | Onze mudanças esperadas |
| [Microsoft, Entra Agent ID](../referencia/bibliografia.md#microsoft-entra-agent-id-documentacao) | Anúncio de produto | Onze mudanças esperadas |
| [AWS, AgentCore Policy e Evaluations](../referencia/bibliografia.md#aws-bedrock-agentcore-policy-e-evaluations-2025) | Anúncio de produto | Onze mudanças esperadas |
| [A2A Project, Agent2Agent Protocol](../referencia/bibliografia.md#a2a-project-agent2agent-protocol-documentacao) | Especificação de protocolo | Onze mudanças esperadas |
| [Agentic AI Foundation, AGENTS.md](../referencia/bibliografia.md#agentic-ai-foundation-agentsmd-standard) | Especificação | Onze mudanças esperadas |
| [Anthropic, Claude Duet](../referencia/bibliografia.md#anthropic-introducing-claude-duet-2026) | Anúncio de produto | Assistentes que agem sem pedido |
| [xAI, Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao) | Anúncio de produto | Assistentes que agem sem pedido, Componentes de um agente com controle |
| [OpenAI, dots](../referencia/bibliografia.md#openai-introducing-dots-2026) | Anúncio de produto | Assistentes que agem sem pedido |
| [Meta, Muse](../referencia/bibliografia.md#meta-introducing-muse-2026) | Anúncio de produto | Assistentes que agem sem pedido |
| [Reuters, Muse e o concierge humano](../referencia/bibliografia.md#reuters-muse-e-o-concierge-humano-2026) | Reportagem sobre episódio específico | Assistentes que agem sem pedido |
| [Cognition, Itaú](../referencia/bibliografia.md#cognition-devin-em-sao-paulo-2026) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [Nubank, skills como dependências](../referencia/bibliografia.md#nubank-when-ai-skills-become-supply-chain-dependencies-2026) | Relato da própria empresa | Resultados publicados por empresas |
| [Google Cloud, Bradesco](../referencia/bibliografia.md#google-cloud-gemini-at-work-2026) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [Microsoft, Ask Microsoft](../referencia/bibliografia.md#microsoft-ask-microsoft-com-copilot-studio-2026) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [Salesforce, OpenTable](../referencia/bibliografia.md#salesforce-opentable-com-agentforce-2025) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [AWS, Cox Automotive](../referencia/bibliografia.md#aws-cox-automotive-2026) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [ServiceNow, Thrive](../referencia/bibliografia.md#servicenow-thrive-2026) | Relato de empresa publicado pelo fornecedor | Resultados publicados por empresas |
| [Visa, piloto de pagamentos](../referencia/bibliografia.md#visa-piloto-de-pagamentos-por-agentes-2026) | Piloto | Onze mudanças esperadas, Resultados publicados por empresas |
| [BMW Group, robôs humanoides](../referencia/bibliografia.md#bmw-group-robos-humanoides-2026) | Piloto | Onze mudanças esperadas, Resultados publicados por empresas |
| [Google DeepMind, Co-Scientist](../referencia/bibliografia.md#google-deepmind-co-scientist-2026) | Pesquisa e experimentação | Onze mudanças esperadas, Resultados publicados por empresas |
| [OWASP, Top 10 for Agentic Applications](../referencia/bibliografia.md#owasp-top-10-for-agentic-applications-2026) | Referencial comunitário de riscos | Componentes de um agente com controle |
| [NIST, AI Agent Standards Initiative](../referencia/bibliografia.md#nist-ai-agent-standards-initiative-2026) | Iniciativa de padronização | Componentes de um agente com controle |
| [Anthropic, Demystifying Evals for AI Agents](../referencia/bibliografia.md#anthropic-demystifying-evals-for-ai-agents-2026) | Orientação técnica de fornecedor | Medição do custo e do resultado |
| [LangChain, runtime de Deep Agents](../referencia/bibliografia.md#langchain-runtime-de-deep-agents-2026) | Orientação técnica de fornecedor | Mudanças esperadas para 2027 a 2030 |
| [UiPath, Maestro Orchestrate](../referencia/bibliografia.md#uipath-maestro-orchestrate-documentacao) | Anúncio de produto | Mudanças esperadas para 2027 a 2030 |
| [Anthropic, computer use no Cowork](../referencia/bibliografia.md#anthropic-computer-use-no-cowork-documentacao) | Anúncio de produto | Mudanças esperadas para 2027 a 2030 |
| [GitHub, Copilot cloud agent](../referencia/bibliografia.md#github-copilot-cloud-agent-documentacao) | Anúncio de produto | Mudanças esperadas para 2027 a 2030 |
| [Microsoft, IA local no Windows](../referencia/bibliografia.md#microsoft-ia-local-no-windows-documentacao) | Anúncio de produto | Mudanças esperadas para 2027 a 2030 |
| [OpenAI e Stripe, Agentic Commerce Protocol](../referencia/bibliografia.md#openai-e-stripe-agentic-commerce-protocol-especificacao) | Especificação de protocolo | Mudanças esperadas para 2027 a 2030 |
| [Google, Agent Payments Protocol](../referencia/bibliografia.md#google-agent-payments-protocol-2026) | Especificação de protocolo | Mudanças esperadas para 2027 a 2030 |
| [NVIDIA, Isaac GR00T](../referencia/bibliografia.md#nvidia-isaac-gr00t-documentacao) | Anúncio de produto | Mudanças esperadas para 2027 a 2030 |
| [Gartner, metodologia do Hype Cycle](../referencia/bibliografia.md#gartner-hype-cycle-metodologia) | Descrição de método | Mudanças esperadas para 2027 a 2030 |
| [Gartner, Hype Cycle for Agentic AI, 2026](../referencia/bibliografia.md#gartner-hype-cycle-for-agentic-ai-2026-2026) | Previsão de analista | Mudanças esperadas para 2027 a 2030 |
| [Gartner, Hype Cycle for Generative AI, 2026](../referencia/bibliografia.md#gartner-hype-cycle-for-generative-ai-2026-2026) | Previsão de analista | Mudanças esperadas para 2027 a 2030 |
| [Gartner, Hype Cycle for Artificial Intelligence, 2026](../referencia/bibliografia.md#gartner-hype-cycle-for-artificial-intelligence-2026-2026) | Previsão de analista | Mudanças esperadas para 2027 a 2030 |
| [Pavic, análise do Hype Cycle de 2026](../referencia/bibliografia.md#pavic-gartner-ai-hype-cycle-2026-2026) | Análise secundária | Mudanças esperadas para 2027 a 2030 |
| [Aislin Consulting, análise do Hype Cycle de 2026](../referencia/bibliografia.md#aislin-consulting-agentic-ai-is-at-the-peak-2026) | Análise secundária | Mudanças esperadas para 2027 a 2030 |

Os relatórios completos da Forrester e de parte do Gartner são pagos, e os números desta sessão vêm dos resumos públicos. Os resultados de empresas não passaram por auditoria independente, e os endereços da documentação de produtos podem mudar depois da consulta de 10/11/2026.

## Conexão com as sessões anteriores

| Sessão | Uso nesta sessão |
|---|---|
| [Sessão 2](../sessao-02-ambiente-agentico/index.md) | O arnês, conjunto de instruções, ferramentas e regras que cerca o modelo, e o cálculo do erro composto, em que a chance de acerto cai a cada passo adicional, aparecem nos componentes de controle e na medição da confiabilidade |
| [Sessões 3](../sessao-03-exploracao-especificacao/index.md) e [4](../sessao-04-regras-formais-com-ia/index.md) | A especificação e as tabelas de decisão correspondem aos critérios de aceite e às etapas de regras fixas dos processos que combinam agentes e regras |
| [Sessão 6](../sessao-06-spec-kit-aprofundado/index.md) | O teste escrito antes do código é uma das formas automáticas de testar um agente |
| [Sessão 8](../sessao-08-skills-e-agentes/index.md) | A ficha de requisitos define as ferramentas e permissões do campo de controles da ficha de piloto |
| [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/index.md) | A ficha de governança define a faixa de risco e a aprovação formal do campo 8 da ficha de piloto |
