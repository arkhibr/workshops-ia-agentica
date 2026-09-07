# Bibliografia — Fontes Padrão-Ouro

Referências que embasam o conteúdo metodológico do workshop. Cada entrada indica a que sessão(ões) serve de base.

## Índice de Referências

- [Spec-Driven Development](#spec-driven-development)
- [Regras de Negócio](#regras-de-negocio)
- [Arquitetura de Decisão](#arquitetura-de-decisao)
- [Testes](#testes)
  - [xUnit Test Patterns](#meszaros-xunit-test-patterns-2007)
  - [Test-Driven Development](#beck-test-driven-development-by-example-2002)
  - [Property-Based Testing](#fast-check-e-fscheck-property-based-testing)
  - [Mutation Testing](#strykerjs-e-strykernet-mutation-testing)
- [Depuração Sistemática](#depuracao-sistematica)
  - [Why Programs Fail](#zeller-why-programs-fail-2005)
- [Economia de Engenharia](#economia-de-engenharia-de-software)
  - [Software Engineering Economics](#boehm-software-engineering-economics-1981)
- [Fundamentos Técnicos](#fundamentos-tecnicos-llms-e-agentes)
  - [Transformer Architecture](#vaswani-et-al-attention-is-all-you-need-2017)
  - [Few-Shot Learning](#brown-et-al-language-models-are-few-shot-learners-2020)
  - [Chain-of-Thought Prompting](#wei-et-al-chain-of-thought-prompting-2022)
  - [ReAct](#yao-et-al-react-2023)
  - [SWE-bench](#jimenez-et-al-swe-bench-2024)
  - [Codex](#chen-et-al-codex-e-humaneval-2021)
- [Evidência Empírica](#evidencia-empirica-sobre-produtividade-e-risco)
  - [Copilot Productivity](#peng-et-al-copilot-productivity-2023)
  - [Experienced Developer Study](#metr-experienced-developer-productivity-2025)
  - [Security Assessment](#pearce-et-al-copilot-security-2022)
- [Engenharia de Software na Era dos LLMs](#engenharia-de-software-na-era-dos-llms)
  - [Software 2.0](#karpathy-software-20-2017)
  - [Software Is Changing Again](#karpathy-software-is-changing-again-2025)
  - [What is Agentic Engineering](#willison-what-is-agentic-engineering-2026)
  - [Controle e Autonomia (4 formas de controle operacional)](#mendes-controle-e-autonomia-modulo-4-agentes)
  - [Building Effective Agents](#anthropic-building-effective-agents-2024)
- [Ambiente Agêntico](#ambiente-agentico-e-engenharia-de-contexto)
  - [DeepSWE Leaderboard](#datacurve-deepswe-leaderboard)
  - [Writing Effective Tools for Agents](#anthropic-writing-effective-tools-for-agents-2025)
  - [Code Execution with MCP](#anthropic-code-execution-with-mcp-2025)
  - [Steering Claude Code](#anthropic-steering-claude-code-2026)
  - [Agent Harness Engineering](#trivedy-the-anatomy-of-an-agent-harness-2026)
  - [Context Engineering](#anthropic-effective-context-engineering-2025)
  - [Model Context Protocol](#anthropic-introducing-the-model-context-protocol-2024)
  - [AGENTS.md Standard](#agentic-ai-foundation-agentsmd-standard)

## Spec-Driven Development

**DELIMARSKY, Den. "Spec-driven development with AI: Get started with a new open source toolkit".** *The GitHub Blog*, 2 set. 2025. <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>. Post oficial de lançamento do GitHub Spec Kit — define o problema do vibe coding ("você descreve o objetivo, recebe um bloco de código de volta, e frequentemente... parece certo, mas não funciona direito") e o papel da especificação como "contrato para como seu código deve se comportar".
→ Sessões 1, 3, 5, 8.

**GitHub Spec Kit.** Implementação de referência open source do Spec-Driven Development (SDD) — mais de 90 mil estrelas no GitHub. Define os quatro artefatos canônicos (`constitution.md`, `spec.md`, `plan.md`, `tasks.md`) e os comandos `/specify`, `/plan`, `/tasks`, compatíveis com Claude Code, GitHub Copilot e Cursor.
→ Sessões 3, 5, 8.

## Regras de Negócio

**OMG. *Semantics of Business Vocabulary and Business Rules (SBVR)*.** Especificação da Object Management Group para vocabulário de negócio e regras formais — a base do bloco de especificação em linguagem controlada.
→ Sessão 4.

**ROSS, Ronald G. *RuleSpeak* — Business Rules Solutions.** Notação em linguagem natural controlada para expressar as três formas de regra: obrigação, proibição e possibilidade.
→ Sessão 4.

**Decision Model and Notation (DMN) / tabelas de decisão.** Notação para representar regras condicionais como tabelas — usada como complemento ao RuleSpeak para regras de cálculo e elegibilidade.
→ Sessão 4.

## Arquitetura de Decisão

**MADR (Markdown Architectural Decision Records) v4.** Template leve para registro de decisões arquiteturais — contexto, opções consideradas, decisão, consequências.
→ Sessão 10.

## Testes

### MESZAROS — xUnit Test Patterns (2007)
**MESZAROS, Gerard. *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley, 2007.**

Referência canônica em padrões de teste. Cataloga 60+ padrões para escrever testes mantíveis e confiáveis em frameworks xUnit (JUnit, NUnit, etc.). Cobre testes de unidade, integração e aceitação com padrões como Arrange-Act-Assert, Test Fixtures, Mocks, Stubs e Test Data Builders. Fundamenta a cultura xUnit adotada no workshop (C# com xUnit, JavaScript/TypeScript com Jest). Essencial para qualidade de teste: sem padrões aplicados, testes viram débito técnico que desacelera evolução — base para TDD assistido por IA e para detectar quando o agente erra ao gerar testes.

→ Sessão 6.

---

### BECK — Test-Driven Development: By Example (2002)

**BECK, Kent. *Test-Driven Development: By Example*. Addison-Wesley, 2002.**

O ciclo vermelho-verde-refatoração, adaptado neste workshop para o fluxo assistido por LLM. Fundamenta a prática de TDD clássico, que neste material é combinado com agentes de codificação.

→ Sessão 6.

---

### fast-check e FsCheck — Property-Based Testing

**fast-check** (JavaScript/TypeScript) e **FsCheck** (.NET) — bibliotecas de referência para testes baseados em propriedade.

→ Sessão 7.

---

### StrykerJS e Stryker.NET — Mutation Testing

**StrykerJS** (JavaScript/TypeScript) e **Stryker.NET** (.NET) — ferramentas de referência para testes de mutação.

→ Sessão 7.

## Depuração Sistemática

### ZELLER — Why Programs Fail (2005)

**ZELLER, Andreas. *Why Programs Fail: A Guide to Systematic Debugging*. Morgan Kaufmann, 2005.**

Livro clássico sobre depuração sistemática de programas. Apresenta metodologia científica aplicada à localização de erros: reproduzir o defeito consistentemente, formular hipóteses sobre causas, projetar testes para refutá-las e isolar o código responsável. Zeller desenvolve técnicas como delta debugging (automatizar redução de entradas que causam falha), execução reversa e análise de dependência. Fundamental para engenheiros que buscam evitar tentativa-e-erro em depuração, oferecendo processos rigorosos e automatizáveis para diagnóstico — base do protocolo hipótese → investigação → correção → verificação usado na Sessão 9.

→ Sessão 9.

---

## Economia de Engenharia de Software

### BOEHM — Software Engineering Economics (1981)

**BOEHM, Barry W. *Software Engineering Economics*.** Prentice-Hall, 1981.

Documentou empiricamente que o custo de corrigir um defeito cresce a cada fase do desenvolvimento — em sistemas grandes e críticos, um problema descoberto depois da entrega pode custar da ordem de 100 vezes mais do que o mesmo problema pego na fase de requisitos. Pesquisa mais recente questiona o multiplicador exato em times ágeis com integração contínua, mas não a direção do efeito. Fundamenta por que reversibilidade e tempo de vida pesam na escolha entre vibe coding, assistência e SDD.

→ Sessão 1.

## Fundamentos Técnicos (LLMs e Agentes)

### VASWANI et al. — Attention Is All You Need (2017)

**VASWANI, Ashish et al. *Attention Is All You Need*.** NeurIPS, 2017. <https://arxiv.org/abs/1706.03762>

Apresenta a arquitetura Transformer, substituindo modelos recorrentes e convolucionais complexos por mecanismos de atenção puros. Alcançou desempenho estado-da-arte em tradução automática: 28,4 BLEU em English-to-German e 41,8 BLEU em English-to-French (treinado em apenas 3,5 dias em oito GPUs). A arquitetura oferece melhor paralelização, reduz significativamente o tempo de treinamento e generaliza bem para outras tarefas, como análise sintática. O trabalho fundou a base para todos os modelos de linguagem modernos.

→ Sessão 1.

---

### BROWN et al. — Language Models are Few-Shot Learners (2020)

**BROWN, Tom B. et al. *Language Models are Few-Shot Learners*.** NeurIPS, 2020. <https://arxiv.org/abs/2005.14165>

Demonstra que aumentar a escala de modelos de linguagem melhora substancialmente o desempenho em aprendizado com poucos exemplos, sem necessidade de ajuste fino. Apresenta o GPT-3, modelo autorregressivo com 175 bilhões de parâmetros, aplicado apenas via interação textual sem atualização de gradientes. Alcança desempenho competitivo em tradução, resposta a perguntas, preenchimento de texto, raciocínio e adaptação de domínio. Gera textos tão realistas que avaliadores humanos têm dificuldade em distinguir de conteúdo humano — mecanismo técnico que torna um prompt capaz de funcionar como programa (Software 3.0).

→ Sessão 1.

---

### WEI et al. — Chain-of-Thought Prompting (2022)

**WEI, Jason et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.** NeurIPS, 2022. <https://arxiv.org/abs/2201.11903>

Demonstra que solicitar ao modelo que gere uma sequência de passos intermediários de raciocínio — *chain of thought* — melhora significativamente o desempenho em tarefas de raciocínio complexo. A técnica emerge naturalmente em modelos suficientemente grandes quando exemplos de raciocínio são fornecidos como demonstrações no prompt. Experimentos comprovam ganho em tarefas aritméticas, senso comum e raciocínio simbólico. Um modelo de 540B parâmetros com apenas oito exemplos alcança estado-da-arte no benchmark GSM8K, superando até GPT-3 ajustado com verificador — a metade "raciocínio" que o ReAct combina com ação.

→ Sessão 1.

---

### YAO et al. — ReAct (2023)

**YAO, Shunyu et al. *ReAct: Synergizing Reasoning and Acting in Language Models*.** ICLR, 2023. <https://arxiv.org/abs/2210.03629>

Propõe ReAct, que integra raciocínio e ação em modelos de linguagem, permitindo que gerem simultaneamente pensamento e ações específicas da tarefa. O raciocínio induz e atualiza planos de ação; as ações permitem interface com fontes externas como bases de conhecimento. Reduz alucinação em QA ao integrar APIs de conhecimento e alcança 34% e 10% de melhoria em benchmarks ALFWorld e WebShop em relação a métodos de imitação. As trajetórias de resolução são mais interpretáveis e confiáveis que abordagens sem raciocínio — a base técnica que distingue um agente de codificação de um LLM respondendo uma pergunta isolada.

→ Sessão 1.

---

### JIMENEZ et al. — SWE-bench (2024)

**JIMENEZ, Carlos E. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*.** ICLR, 2024. <https://arxiv.org/abs/2310.06770>

Apresenta SWE-bench, benchmark contendo 2.294 problemas reais de engenharia de software extraídos do GitHub em 12 repositórios Python populares. Avalia capacidade de modelos em editar bases de código para resolver problemas, exigindo compreensão de múltiplas funções, classes, arquivos e interação com ambientes de execução. Modelos de ponta, incluindo Claude 2, resolvem apenas 1,96% dos problemas no artigo original; em 2026, os melhores agentes resolvem cerca de 97% na versão revisada (SWE-bench Verified) — a evidência quantitativa por trás de "por que agora".

→ Sessão 1.

---

### CHEN et al. — Codex e HumanEval (2021)

**CHEN, Mark et al. *Evaluating Large Language Models Trained on Code*.** arXiv:2107.03374, 2021. <https://arxiv.org/abs/2107.03374>

Apresenta Codex, versão do GPT ajustada em código do GitHub, com foco em síntese de programas em Python. Introduz HumanEval, novo conjunto de avaliação para medir correção funcional em síntese de código a partir de docstrings. Codex resolve 28,8% de problemas HumanEval (vs. 0% do GPT-3), aumentando para 70,2% com amostragem de 100 tentativas por problema. Analisa limitações com docstrings complexas e vinculação de variáveis. Contraste com o SWE-bench: mede capacidade de codificação, não de engenharia de software num repositório real.

→ Sessão 1.

## Evidência Empírica sobre Produtividade e Risco

### PENG et al. — Copilot Productivity (2023)

**PENG, Sida; KALLIAMVAKOU, Eirini; CIHON, Peter; DEMIRER, Mert. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*.** arXiv:2302.06590, 2023. <https://arxiv.org/abs/2302.06590>

Experimento randomizado com 70 desenvolvedores profissionais que completam uma tarefa de implementação de servidor HTTP. O grupo com Copilot completou a tarefa 55,8% mais rápido (71 minutos contra 161 minutos). O efeito foi maior para desenvolvedores menos experientes, sugerindo que a assistência reduz a curva de aprendizado para tarefas bem delimitadas e novas, onde o contexto é contido e explícito.

→ Sessão 1.

---

### METR — Experienced Developer Productivity (2025)

**METR. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*.** jul. 2025. <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>

Experimento randomizado com 16 desenvolvedores experientes (cerca de 5 anos de trajetória nos próprios projetos) em 246 tarefas reais de manutenção de código aberto. Usar IA tornou a conclusão das tarefas 19% mais lenta. Mais revelador ainda: os próprios desenvolvedores, depois de terminar, estimaram que a IA os havia deixado 20% mais rápidos — o oposto exato do que os dados mediram. Contraponto empírico direto à métrica de produtividade de Peng et al., evidenciando a diferença entre tarefas novas e delimitadas (onde vibe coding ganha) versus manutenção em sistema maduro com contexto implícito.

→ Sessão 1.

---

### PEARCE et al. — Copilot Security (2022)

**PEARCE, Hammond et al. *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions*.** IEEE Symposium on Security and Privacy (S&P), 2022. <https://arxiv.org/abs/2108.09293>

Investiga segurança do GitHub Copilot avaliando com que frequência recomenda código inseguro. Criou 89 cenários sobre vulnerabilidades de alto risco (Top 25 MITRE), gerando 1.689 programas. Resultado preocupante: aproximadamente 40% foram classificados como vulneráveis. Atribui achado ao fato de Copilot ser treinado em código aberto do GitHub, que inclui código bugado e padrões explorados — base empírica para o risco "sem rede" do vibe coding.

→ Sessão 1.

## Engenharia de Software na Era dos LLMs

### KARPATHY — Software 2.0 (2017)

**KARPATHY, Andrej. "Software 2.0".** Medium, nov. 2017. <https://karpathy.medium.com/software-2-0-a64152b37c35>

Ensaio precursor da tese de Software 3.0: uma rede neural treinada é compilada a partir de dados por um processo de otimização, um tipo de programa fundamentalmente diferente do código explícito escrito à mão.

→ Sessão 1.

---

### KARPATHY — Software Is Changing Again (2025)

**KARPATHY, Andrej. *Software Is Changing (Again)*.** Palestra, YC AI Startup School, 17 jun. 2025. Recapitulação: Latent Space, <https://www.latent.space/p/s3>

Formulação dos três paradigmas coexistentes: Software 1.0 (código explícito), Software 2.0 (redes neurais treinadas), Software 3.0 (prompt em linguagem natural como programa executável); e do conceito de *generation-verification loop* ("demo is works.any(), product is works.all()"). Karpathy também cunhou o termo *vibe coding*, em publicação de fevereiro de 2025.

→ Sessão 1.

---

### WILLISON — What is Agentic Engineering (2026)

**WILLISON, Simon. "What is agentic engineering?"** — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026. <https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/>

Define engenharia agêntica como "a prática de desenvolver software com o auxílio de agentes de codificação", sustentada por três responsabilidades humanas (especificação do problema, provisão de ferramentas, verificação e iteração), e distingue a prática de "vibe coding", termo que reserva para código de protótipo não revisado.

→ Sessão 1.

---

### MENDES — Controle e Autonomia (Módulo 4, Agentes)

**MENDES, Marco. "Controle e Autonomia".** *Arquitetura de Soluções com IA Generativa*, Módulo 4 — Agentes. <https://aulas-marco.github.io/arquitetura-solucoes-ia-generativa/modulo-4-agentes/controle-e-autonomia/>

Material da disciplina de pós-graduação que fundamenta a distinção entre workflow e agente usada nesta sessão. Define quatro formas de controle operacional — chatbot, copiloto, fluxo de trabalho determinístico e agente — distinguidas por uma única pergunta: quem escolhe a próxima transição. A categorização separa controle de qualidade ou maturidade: um fluxo de trabalho bem desenhado pode superar um agente mal supervisionado, e um copiloto que chama ferramenta de leitura continua copiloto, não agente. Cataloga também os critérios técnicos que justificam a escolha de um agente: sequências de comprimento variável, feedback de ferramenta verificável, erros conteníveis, conclusão observável e autoridade/orçamento delimitados.

→ Sessão 1.

### ANTHROPIC — Building Effective Agents (2024)

**ANTHROPIC. "Building Effective Agents".** Anthropic Engineering, dez. 2024. <https://www.anthropic.com/engineering/building-effective-agents>

Guia de referência do mercado para decidir entre workflow (código orquestra o modelo em caminho predefinido) e agente (o modelo decide os próprios passos); recomenda a solução mais simples possível, aumentando autonomia apenas quando o problema exigir. Cataloga cinco padrões de workflow: encadeamento de prompts, roteamento, paralelização, orquestrador-trabalhadores, avaliador-otimizador.

→ Sessão 1.

## Ambiente Agêntico e Engenharia de Contexto

### DATACURVE — DeepSWE Leaderboard

**DATACURVE. *DeepSWE Leaderboard*.** Publicado em benchlm.ai. <https://benchlm.ai/benchmarks/deepswe>

Leitura independente de modelos em 113 tarefas de engenharia de software de longo horizonte, tiradas de 91 repositórios de código aberto em 5 linguagens, verificadas por programa. Espelha o placar público do DeepSWE usando, para cada modelo, a melhor configuração disponível do `mini-swe-agent` — o que mede o par modelo mais arnês, e não o modelo isolado.

→ Sessões 1, 2.

---

### ANTHROPIC — Writing Effective Tools for Agents (2025)

**ANTHROPIC. "Writing effective tools for agents".** Anthropic Engineering, 2025. <https://www.anthropic.com/engineering/writing-tools-for-agents>

Critério verificável para catálogo de ferramentas: se uma pessoa da engenharia não sabe dizer qual ferramenta usar numa situação, o modelo também não saberá. Recomenda consolidar por fluxo de trabalho em vez de espelhar endpoints.

→ Sessão 2.

---

### ANTHROPIC — Code Execution with MCP (2025)

**ANTHROPIC. "Code execution with MCP".** Anthropic Engineering, 2025. <https://www.anthropic.com/engineering/code-execution-with-mcp>

Caso em que carregar definições de ferramenta sob demanda, em vez de todas de uma vez, reduziu o consumo de 150 mil para 2 mil tokens.

→ Sessão 2.

---

### ANTHROPIC — Steering Claude Code (2026)

**ANTHROPIC. "Steering Claude Code".** Anthropic Blog, 2026. <https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more>

Separa os mecanismos que guiam o modelo, como arquivos de contexto, dos que impõem comportamento, como hooks e permissões — a base da regra de que proteção real precisa ser determinística.

→ Sessões 2, 10.

---

### TRIVEDY — The Anatomy of an Agent Harness (2026)

**TRIVEDY, Vivek. "The Anatomy of an Agent Harness".** *LangChain Blog*, 2026. <https://www.langchain.com/blog/the-anatomy-of-an-agent-harness>

Formulação canônica do arnês (*harness*) como tudo o que cerca o modelo e o transforma em agente — "if you're not the model, you're the harness" — com a medição de que a mesma família de modelo muda de faixa no Terminal Bench 2.0 quando só o arnês muda.

→ Sessão 2.

---

### OSMANI — Agent Harness Engineering (2026)

**OSMANI, Addy. "Agent Harness Engineering".** Blog pessoal, 2026. <https://addyosmani.com/blog/agent-harness-engineering/>

Síntese prática do mesmo achado: um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

→ Sessão 2.

---

### VERCEL — Removing 80% of Agent Tools (2026)

**VERCEL. "We removed 80% of our agent's tools".** *Vercel Blog*, 2026. <https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools>

Relato de redução de dezesseis ferramentas especializadas para acesso a sistema de arquivos num agente de texto para SQL, com taxa de sucesso subindo de 80% para 100% e 40% menos passos — evidência de que catálogo mínimo de ferramentas é decisão de qualidade.

→ Sessão 2.

---

### ANTHROPIC — Effective Context Engineering (2025)

**ANTHROPIC. "Effective context engineering for AI agents".** Anthropic Engineering, set. 2025. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

Define context engineering como a evolução do prompt engineering: cuidar de tudo que chega à janela de contexto numa execução, não só do texto da instrução. Descreve ferramentas como o contrato entre o agente e o ambiente, desenhadas para eficiência de token.

→ Sessão 2.

---

### ANTHROPIC — Introducing the Model Context Protocol (2024)

**ANTHROPIC. "Introducing the Model Context Protocol".** Anthropic News, 25 nov. 2024. <https://www.anthropic.com/news/model-context-protocol>

Anúncio do MCP, protocolo aberto que resolve o problema M×N de integrações entre modelos e ferramentas. Um ano depois, adotado por OpenAI, Google e Microsoft.

→ Sessão 2.

---

### Agentic AI Foundation — AGENTS.md Standard

**Agentic AI Foundation (Linux Foundation). "AGENTS.md".** Padrão aberto, formalizado em ago. 2025 por OpenAI, Google, Cursor, Factory e Sourcegraph. <https://agents.md/>

Arquivo markdown na raiz do repositório, sem esquema obrigatório, que instrui agentes de codificação sobre build, testes, convenções e segurança — mais de 20 mil repositórios adotantes, lido por ferramentas de múltiplos fornecedores concorrentes.

→ Sessão 2.
