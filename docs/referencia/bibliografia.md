# Bibliografia — Fontes Padrão-Ouro

Referências que embasam o conteúdo metodológico do workshop. Cada entrada indica a que sessão(ões) serve de base.

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

**MESZAROS, Gerard. *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley, 2007.** Referência canônica de padrões de teste de unidade — base para TDD assistido por IA e para detectar quando o agente erra ao gerar testes.
→ Sessão 6.

**BECK, Kent. *Test-Driven Development: By Example*. Addison-Wesley, 2002.** O ciclo vermelho-verde-refatoração, adaptado neste workshop para o fluxo assistido por LLM.
→ Sessão 6.

**fast-check** (JavaScript/TypeScript) e **FsCheck** (.NET) — bibliotecas de referência para testes baseados em propriedade.
→ Sessão 7.

**StrykerJS** (JavaScript/TypeScript) e **Stryker.NET** (.NET) — ferramentas de referência para testes de mutação.
→ Sessão 7.

## Depuração Sistemática

**ZELLER, Andreas. *Why Programs Fail: A Guide to Systematic Debugging*. Morgan Kaufmann, 2005.** Base do protocolo hipótese → investigação → correção → verificação usado na Sessão 9.
→ Sessão 9.

## Economia de Engenharia de Software

**BOEHM, Barry W. *Software Engineering Economics*.** Prentice-Hall, 1981. Documentou que o custo de corrigir um defeito cresce a cada fase do desenvolvimento — em sistemas grandes e críticos, um problema descoberto depois da entrega pode custar da ordem de 100 vezes mais do que o mesmo problema pego na fase de requisitos. Pesquisa mais recente questiona o multiplicador exato em times ágeis com integração contínua, mas não a direção do efeito. Fundamenta por que reversibilidade e tempo de vida pesam na escolha entre vibe coding, assistência e SDD.
→ Sessão 1.

## Fundamentos Técnicos (LLMs e Agentes)

**VASWANI, Ashish et al. *Attention Is All You Need*.** NeurIPS, 2017. <https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html>. Artigo que introduziu a arquitetura Transformer — base técnica de todo LLM usado em ferramentas agênticas de codificação.
→ Sessão 1.

**BROWN, Tom B. et al. *Language Models are Few-Shot Learners*.** NeurIPS, 2020. <https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html>. Artigo de apresentação do GPT-3 — demonstra empiricamente o aprendizado em contexto (*in-context learning*): um modelo executa uma tarefa nova a partir da descrição em linguagem natural e de poucos exemplos, sem ajuste de peso. Mecanismo técnico que torna um prompt capaz de funcionar como programa (Software 3.0).
→ Sessão 1.

**WEI, Jason et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.** NeurIPS, 2022. <https://arxiv.org/abs/2201.11903>. Demonstra que pedir ao modelo para expor o raciocínio passo a passo antes da resposta final melhora o desempenho em tarefas de múltiplas etapas — a metade "raciocínio" que o ReAct combina com ação.
→ Sessão 1.

**YAO, Shunyu et al. *ReAct: Synergizing Reasoning and Acting in Language Models*.** ICLR, 2023. <https://openreview.net/forum?id=WE_vluYUL-X>. Formaliza o ciclo de raciocínio intercalado com ação verificável — a base técnica que distingue um agente de codificação de um LLM respondendo uma pergunta isolada.
→ Sessão 1.

**JIMENEZ, Carlos E. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*.** ICLR, 2024. <https://arxiv.org/abs/2310.06770>. Benchmark que mede se um agente resolve issues reais de repositórios GitHub, produzindo um patch que passa nos testes da comunidade. O melhor resultado do artigo original (Claude 2 com recuperação por palavras-chave) resolveu 1,96% dos casos; em 2026, os melhores agentes resolvem cerca de 97% na versão revisada (SWE-bench Verified) — a evidência quantitativa por trás de "por que agora".
→ Sessão 1.

**CHEN, Mark et al. *Evaluating Large Language Models Trained on Code*.** arXiv:2107.03374, 2021. <https://arxiv.org/abs/2107.03374>. Artigo do Codex que introduziu o HumanEval — benchmark de geração de função isolada a partir de enunciado. Contraste com o SWE-bench: mede capacidade de codificação, não de engenharia de software num repositório real.
→ Sessão 1.

**vals.ai. "SWE-bench Verified".** Leaderboard independente, atualizado continuamente. <https://www.vals.ai/benchmarks/swebench>. Reavalia modelos de diferentes fabricantes sob o mesmo arnês de teste — referência para comparar sem depender de número autorreportado pelo fabricante do modelo.
→ Sessão 1.

**SWE-bench. "SWE-bench Verified Leaderboard".** <https://www.swebench.com/>. Leaderboard oficial do benchmark, com as variantes Verified, Lite, Pro e Multimodal.
→ Sessão 1.

**ANTHROPIC. "Introducing Claude Haiku 4.5".** Anthropic News, 2026. <https://www.anthropic.com/news/claude-haiku-4-5>. Anúncio oficial de lançamento, com os números de SWE-bench Verified do modelo mais barato da família Claude — referência de custo-benefício frente aos modelos de topo da tabela.
→ Sessão 1.

**OpenAI. "GPT-5.6" (Sol, Terra, Luna).** Anúncio de lançamento, 9 jul. 2026. Recapitulação: MarkTechPost, <https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/>. Família de três níveis lançada sem número de SWE-bench Verified — só SWE-bench Pro foi divulgado. Exemplo real do critério "desconfie do benchmark que o fabricante escolhe divulgar".
→ Sessão 1.

**Datacurve. "DeepSWE".** Leaderboard independente. <https://benchlm.ai/benchmarks/deepswe>. Benchmark de longo horizonte com 113 tarefas de 91 repositórios open source ativos em 5 linguagens, verificadas por programa. Avalia Claude, GPT-5.6 e GLM sob a mesma régua e na mesma data — referência para comparar fabricantes diferentes sem misturar benchmarks distintos.
→ Sessão 1.

## Evidência Empírica sobre Produtividade e Risco

**PENG, Sida; KALLIAMVAKOU, Eirini; CIHON, Peter; DEMIRER, Mert. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*.** arXiv:2302.06590, 2023. <https://arxiv.org/abs/2302.06590>. Experimento randomizado com 70 desenvolvedores profissionais: o grupo com Copilot completou uma tarefa de implementação de servidor HTTP 55,8% mais rápido (71 min contra 161 min). O efeito foi maior para desenvolvedores menos experientes.
→ Sessão 1.

**METR. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*.** jul. 2025. <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>. Experimento randomizado com 16 desenvolvedores experientes (cerca de 5 anos de trajetória nos próprios projetos) em 246 tarefas reais de manutenção: usar IA tornou a conclusão das tarefas 19% mais lenta, embora os desenvolvedores tenham estimado, depois, que a IA os deixara 20% mais rápidos. Contraponto empírico direto à métrica de produtividade de Peng et al. em tarefas de manutenção complexa versus tarefas novas e delimitadas.
→ Sessão 1.

**PEARCE, Hammond et al. *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions*.** IEEE Symposium on Security and Privacy (S&P), 2022. <https://arxiv.org/abs/2108.09293>. Estudo seminal: 89 cenários cobrindo o CWE Top 25 produziram 1.689 programas, dos quais cerca de 40% continham vulnerabilidade de segurança. Base empírica para o risco "sem rede" do vibe coding.
→ Sessão 1.

## Engenharia de Software na Era dos LLMs

**KARPATHY, Andrej. "Software 2.0".** Medium, nov. 2017. <https://karpathy.medium.com/software-2-0-a64152b37c35>. Ensaio precursor da tese de Software 3.0: uma rede neural treinada é compilada a partir de dados por um processo de otimização, não escrita à mão — um tipo de programa diferente do código explícito.
→ Sessão 1.

**KARPATHY, Andrej. *Software Is Changing (Again)*.** Palestra, YC AI Startup School, 17 jun. 2025. Recapitulação: Latent Space, <https://www.latent.space/p/s3>. Formulação dos três paradigmas coexistentes: Software 1.0 (código explícito), Software 2.0 (redes neurais treinadas), Software 3.0 (prompt em linguagem natural como programa executável); e do conceito de *generation-verification loop* ("demo is works.any(), product is works.all()"). Karpathy também cunhou o termo *vibe coding*, em publicação de fevereiro de 2025.
→ Sessão 1.

**WILLISON, Simon. "What is agentic engineering?"** — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026. <https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/>. Define engenharia agêntica como "a prática de desenvolver software com o auxílio de agentes de codificação", sustentada por três responsabilidades humanas (especificação do problema, provisão de ferramentas, verificação e iteração), e distingue a prática de "vibe coding", termo que reserva para código de protótipo não revisado.
→ Sessão 1.

**ANTHROPIC. "Building Effective Agents".** Anthropic Engineering, dez. 2024. <https://www.anthropic.com/engineering/building-effective-agents>. Guia de referência do mercado para decidir entre workflow (código orquestra o modelo em caminho predefinido) e agente (o modelo decide os próprios passos); recomenda a solução mais simples possível, aumentando autonomia apenas quando o problema exigir. Cataloga cinco padrões de workflow: encadeamento de prompts, roteamento, paralelização, orquestrador-trabalhadores, avaliador-otimizador.
→ Sessão 1.
