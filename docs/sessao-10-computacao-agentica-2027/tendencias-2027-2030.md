# Tendências para 2027 a 2030

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) descreve onze tendências para o período de 2027 a 2030 e as organiza em quatro grupos, que podem avançar ao mesmo tempo e não formam uma sequência de maturidade. Para cada tendência, o relatório indica a condição que precisa ser atendida para que a tendência produza resultado de negócio, e esta página apresenta as onze tendências com essa condição.

![Quatro quadros com as onze tendências. Execução e contexto reúne 4.1 persistência e execução assíncrona, com eventos, checkpoints e retomada, 4.2 contexto, memória e skills, com origem, autorização e validade, e 4.3 identidade e controles externos, com escopo, políticas e credenciais. Integração e processos reúne 4.4 interoperabilidade, com MCP para ferramentas e A2A para agentes, 4.7 processos híbridos, com agentes, regras, APIs e pessoas, e 4.8 multimodalidade e interfaces, com voz, documentos e sistemas legados. Software e economia reúne 4.5 engenharia por delegação, com branch, testes e revisão, 4.6 software temporário, com validade, manutenção e descarte, e 4.9 economia por resultado, com modelos combinados e custo integral. Transações e mundo físico reúne 4.10 comércio e pagamentos, com intenção, autorização e confirmação, e 4.11 ciência e robótica, com hipóteses, simulação e validação física.](assets/onze-tendencias-em-quatro-frentes.png)

## Execução e contexto

| Tendência | Mudança esperada | Exemplos documentados | Condição |
|---|---|---|---|
| 4.1 Agentes persistentes e execução assíncrona | Tarefas que continuam depois que o usuário encerra a conversa, como investigar um incidente ou implementar uma alteração | O [Claude Managed Agents](../referencia/bibliografia.md#anthropic-scaling-managed-agents-2026) separa sessão, execução e ambiente de ferramentas, e o [Temporal](../referencia/bibliografia.md#temporal-durable-ai-documentacao) retoma o estado e espera decisão humana | Operações com efeito de negócio precisam de idempotência e reconciliação, porque a retomada de uma execução pode repetir uma ação externa |
| 4.2 Contexto, memória e skills | O resultado do agente passa a depender da qualidade do contexto autorizado, como significado dos dados, procedimentos, regras e estado do trabalho | As [skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) empacotam instruções reutilizáveis, e a [execução de código sobre ferramentas MCP](../referencia/bibliografia.md#anthropic-code-execution-with-mcp-2025) reduz o conteúdo enviado ao modelo | Cada memória ou procedimento precisa de origem, validade, autorização, prazo de retenção e responsável |
| 4.3 Identidade própria e controles externos ao modelo | Agentes em operação com identidade, proprietário, escopo de acesso e ciclo de vida próprios | O [Microsoft Entra Agent ID](../referencia/bibliografia.md#microsoft-entra-agent-id-documentacao) documenta identidade de agentes, e a AWS liberou [Policy e Evaluations no AgentCore](../referencia/bibliografia.md#aws-bedrock-agentcore-policy-e-evaluations-2025) em março de 2026 | A identidade autoriza o acesso sem validar a adequação da ação, que exige critério de negócio, limite de volume e detecção de desvio |

O relatório registra também que armazenar memória ou recuperar instruções não altera os pesos do modelo, embora material comercial às vezes chame os dois mecanismos de aprendizado.

## Integração e processos

| Tendência | Mudança esperada | Exemplos documentados | Condição |
|---|---|---|---|
| 4.4 Interoperabilidade entre ferramentas, agentes e organizações | Integração entre capacidades de fornecedores diferentes, com menos dependência de um único framework | O MCP padroniza o acesso a ferramentas, o [A2A](../referencia/bibliografia.md#a2a-project-agent2agent-protocol-documentacao) padroniza a comunicação entre agentes, e o [AGENTS.md](../referencia/bibliografia.md#agentic-ai-foundation-agentsmd-standard) registra orientações de projeto, todos mantidos pela Agentic AI Foundation | A autorização de negócio e a qualidade dos dados continuam sob responsabilidade dos sistemas integrados |
| 4.7 Processos híbridos com agentes, APIs, automações e pessoas | Cada etapa do processo recebe o grau de autonomia compatível com a verificabilidade e a consequência dela | No exemplo do relatório, a IA classifica uma solicitação, regras explícitas verificam a elegibilidade, uma API registra a operação e uma pessoa trata as exceções | O agente precisa consultar o estado oficial no sistema de registro e conhecer as operações permitidas |
| 4.8 Interação multimodal e operação de interfaces | Voz, documentos, imagens e telas ampliam as tarefas delegáveis, inclusive em sistemas legados sem API | A Anthropic documenta *computer use* em beta no Cowork e no Claude Code | A integração estruturada tem preferência quando existe, porque a operação de tela precisa tratar mudança de layout, tempo de resposta e recuperação |

As regras explícitas da tendência 4.7 correspondem às tabelas de decisão e às sentenças RuleSpeak da [Sessão 4](../sessao-04-regras-formais-com-ia/index.md).

## Software e economia

| Tendência | Mudança esperada | Exemplos documentados | Condição |
|---|---|---|---|
| 4.5 Engenharia de software por delegação | A pessoa define o problema, especifica o comportamento e revisa a mudança, e o agente pesquisa o repositório, planeja e altera o código num ramo | GitHub Copilot cloud agent, Codex, Claude Code e Devin | Limite de trabalho em andamento dos agentes e medição do tempo até a mudança aceita |
| 4.6 Software temporário | Aplicações pequenas criadas para uma campanha ou uma análise e descartadas depois | O Gartner inclui *disposable applications* nas tendências de 2027, e a McKinsey registra empresas que construíram com agentes funcionalidades que antes comprariam | Identidade, acesso a dados, prazo de validade e responsável definidos na criação da aplicação |
| 4.9 Economia por resultado e combinação de modelos | Escolha de modelo e de local de execução por complexidade, latência, custo e restrição de dados | Roteamento, cache, processamento em lote e limite de tentativas, tratados na [Sessão 8](../sessao-08-skills-e-agentes/custo-de-tokens.md) | Medição do custo total por resultado aceito, tratada na página [Métricas e economia](metricas-e-economia.md) |

Na tendência 4.5, o relatório considera pull requests produzidos, tokens consumidos e linhas de código como medidas de atividade, e o sinal contrário a acompanhar é o aumento persistente de retrabalho, vulnerabilidades e filas de revisão. Na tendência 4.6, o relatório registra que construir depressa não elimina os custos de manutenção, integração e suporte, e que a tendência não justifica reconstruir sistemas de registro consolidados.

## Transações e mundo físico

| Tendência | Mudança esperada | Exemplos documentados | Condição |
|---|---|---|---|
| 4.10 Comércio e pagamentos mediados por agentes | Agentes participam de seleção, compra e pagamento com delegação delimitada | Protocolos ACP, UCP e AP2, e um [piloto real](../referencia/bibliografia.md#visa-piloto-de-pagamentos-por-agentes-2026) de pagamento de faturas por agentes relatado por Visa, BILL e Billtrust em outubro de 2026 | A autorização registra quem delegou, o que autorizou, sob quais condições e como tratar disputa ou cancelamento |
| 4.11 Agentes científicos, modelos de mundo e robótica | Ciclos de proposta, simulação, execução e medição em pesquisa e indústria, previstos para 2028 a 2030 ou depois | O [Google Co-Scientist](../referencia/bibliografia.md#google-deepmind-co-scientist-2026) gera hipóteses com vários agentes, a [BMW](../referencia/bibliografia.md#bmw-group-robos-humanoides-2026) relata pilotos de humanoides, e a NVIDIA oferece a plataforma Isaac GR00T | Validação experimental das hipóteses e segurança física nas operações industriais |

## Conclusões sem sustentação na pesquisa

O relatório lista cinco conclusões que a pesquisa não sustenta:

- Data confiável para inteligência artificial geral ou para substituição generalizada de profissões.
- Garantia de retorno baseada na quantidade de agentes.
- Necessidade de tornar autônomos todos os processos.
- Superioridade universal de um fornecedor, framework ou modelo.
- Redução de custo da empresa calculada diretamente a partir do ganho na escrita de código.

**Próxima página:** [Assistentes pessoais proativos](assistentes-proativos.md).
