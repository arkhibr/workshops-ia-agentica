# Bibliografia — Fontes Padrão-Ouro

Referências que embasam o conteúdo metodológico do workshop, em ordem alfabética por autor. Cada entrada indica a que sessão(ões) serve de base.

Para configurar os recursos de memória na ferramenta, consulte o [apêndice sobre memória do Claude](#apendice-ativar-e-conferir-a-memoria-do-claude), no fim desta página.

## Índice Alfabético

- [Agentic AI Foundation — AGENTS.md Standard](#agentic-ai-foundation-agentsmd-standard)
- [Anthropic — Building Effective Agents (2024)](#anthropic-building-effective-agents-2024)
- [Anthropic — Code Execution with MCP (2025)](#anthropic-code-execution-with-mcp-2025)
- [Anthropic — Effective Context Engineering (2025)](#anthropic-effective-context-engineering-2025)
- [Anthropic — Introducing the Model Context Protocol (2024)](#anthropic-introducing-the-model-context-protocol-2024)
- [Anthropic — Steering Claude Code (2026)](#anthropic-steering-claude-code-2026)
- [Anthropic — Writing Effective Tools for Agents (2025)](#anthropic-writing-effective-tools-for-agents-2025)
- [Bass, Clements e Kazman — Software Architecture in Practice (2021)](#bass-clements-e-kazman-software-architecture-in-practice-2021)
- [Beck — Test-Driven Development: By Example (2002)](#beck-test-driven-development-by-example-2002)
- [Böckeler — Understanding Spec-Driven Development (2025)](#bockeler-understanding-spec-driven-development-2025)
- [Boehm — Software Engineering Economics (1981)](#boehm-software-engineering-economics-1981)
- [Brown et al. — Language Models are Few-Shot Learners (2020)](#brown-et-al-language-models-are-few-shot-learners-2020)
- [Chen et al. — Codex e HumanEval (2021)](#chen-et-al-codex-e-humaneval-2021)
- [Chikofsky e Cross — Reverse Engineering and Design Recovery (1990)](#chikofsky-e-cross-reverse-engineering-and-design-recovery-1990)
- [Datacurve — DeepSWE Leaderboard](#datacurve-deepswe-leaderboard)
- [Decision Model and Notation (DMN)](#decision-model-and-notation-dmn)
- [Delimarsky — Spec-Driven Development with AI (2025)](#delimarsky-spec-driven-development-with-ai-2025)
- [Diggs et al. — LLMs for Legacy Code Documentation (2024)](#diggs-et-al-llms-for-legacy-code-documentation-2024)
- [fast-check e FsCheck — Property-Based Testing](#fast-check-e-fscheck-property-based-testing)
- [Feathers — Working Effectively with Legacy Code (2004)](#feathers-working-effectively-with-legacy-code-2004)
- [Fission-AI — OpenSpec](#fission-ai-openspec)
- [Ford, Parsons, Kua e Sadalage — Building Evolutionary Architectures (2023)](#ford-parsons-kua-e-sadalage-building-evolutionary-architectures-2023)
- [GitHub Spec Kit](#github-spec-kit)
- [gszhangwei — OpenSPDD](#gszhangwei-openspdd)
- [Hunt e Thomas — Software Archaeology (2002)](#hunt-e-thomas-software-archaeology-2002)
- [ISO/IEC/IEEE 29148:2018](#isoiecieee-291482018)
- [Jimenez et al. — SWE-bench (2024)](#jimenez-et-al-swe-bench-2024)
- [Karpathy — Software 2.0 (2017)](#karpathy-software-20-2017)
- [Karpathy — Software Is Changing Again (2025)](#karpathy-software-is-changing-again-2025)
- [Lei Complementar 214/2025 — IBS, CBS e Imposto Seletivo](#lei-complementar-2142025-ibs-cbs-e-imposto-seletivo)
- [MADR — Markdown Architectural Decision Records v4](#madr-markdown-architectural-decision-records-v4)
- [Mendes — Controle e Autonomia (Módulo 4, Agentes)](#mendes-controle-e-autonomia-modulo-4-agentes)
- [Meszaros — xUnit Test Patterns (2007)](#meszaros-xunit-test-patterns-2007)
- [METR — Experienced Developer Productivity (2025)](#metr-experienced-developer-productivity-2025)
- [OMG — Semantics of Business Vocabulary and Business Rules](#omg-semantics-of-business-vocabulary-and-business-rules)
- [Osmani — Agent Harness Engineering (2026)](#osmani-agent-harness-engineering-2026)
- [Paul e Elder — The Thinker's Guide to Socratic Questioning (2019)](#paul-e-elder-the-thinkers-guide-to-socratic-questioning-2019)
- [Pearce et al. — Copilot Security (2022)](#pearce-et-al-copilot-security-2022)
- [Peng et al. — Copilot Productivity (2023)](#peng-et-al-copilot-productivity-2023)
- [Ross (ed.) — Business Rules Manifesto (2003)](#ross-ed-business-rules-manifesto-2003)
- [Ross — RuleSpeak](#ross-rulespeak)
- [Sneed e Erdős — Extracting Business Rules from Source Code (1996)](#sneed-e-erdos-extracting-business-rules-from-source-code-1996)
- [StrykerJS e Stryker.NET — Mutation Testing](#strykerjs-e-strykernet-mutation-testing)
- [Trivedy — The Anatomy of an Agent Harness (2026)](#trivedy-the-anatomy-of-an-agent-harness-2026)
- [Vaswani et al. — Attention Is All You Need (2017)](#vaswani-et-al-attention-is-all-you-need-2017)
- [Vercel — Removing 80% of Agent Tools (2026)](#vercel-removing-80-of-agent-tools-2026)
- [Vincent e Prime Radiant — Superpowers (2026)](#vincent-e-prime-radiant-superpowers-2026)
- [Wei et al. — Chain-of-Thought Prompting (2022)](#wei-et-al-chain-of-thought-prompting-2022)
- [Wiegers e Beatty — Software Requirements (2013)](#wiegers-e-beatty-software-requirements-2013)
- [Willison — What is Agentic Engineering (2026)](#willison-what-is-agentic-engineering-2026)
- [Yao et al. — ReAct (2023)](#yao-et-al-react-2023)
- [Zhang e Xia — Structured Prompt-Driven Development (2026)](#zhang-e-xia-structured-prompt-driven-development-2026)
- [Zeller — Why Programs Fail (2005)](#zeller-why-programs-fail-2005)

---

### Agentic AI Foundation — AGENTS.md Standard

**Agentic AI Foundation (Linux Foundation). "AGENTS.md".** Padrão aberto, formalizado em ago. 2025 por OpenAI, Google, Cursor, Factory e Sourcegraph. <https://agents.md/>

Arquivo markdown na raiz do repositório, sem esquema obrigatório, que instrui agentes de codificação sobre build, testes, convenções e segurança — mais de 20 mil repositórios adotantes, lido por ferramentas de múltiplos fornecedores concorrentes.

→ Sessão 2.

---

### Anthropic — Building Effective Agents (2024)

**ANTHROPIC. "Building Effective Agents".** Anthropic Engineering, dez. 2024. <https://www.anthropic.com/engineering/building-effective-agents>

Guia de referência do mercado para decidir entre workflow (código orquestra o modelo em caminho predefinido) e agente (o modelo decide os próprios passos); recomenda a solução mais simples possível, aumentando autonomia apenas quando o problema exigir. Cataloga cinco padrões de workflow: encadeamento de prompts, roteamento, paralelização, orquestrador-trabalhadores, avaliador-otimizador.

→ Sessão 1.

---

### Anthropic — Code Execution with MCP (2025)

**ANTHROPIC. "Code execution with MCP".** Anthropic Engineering, 2025. <https://www.anthropic.com/engineering/code-execution-with-mcp>

Caso em que carregar definições de ferramenta sob demanda, em vez de todas de uma vez, reduziu o consumo de 150 mil para 2 mil tokens.

→ Sessão 2.

---

### Anthropic — Effective Context Engineering (2025)

**ANTHROPIC. "Effective context engineering for AI agents".** Anthropic Engineering, set. 2025. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

Define context engineering como a evolução do prompt engineering: cuidar de tudo que chega à janela de contexto numa execução, não só do texto da instrução. Descreve ferramentas como o contrato entre o agente e o ambiente, desenhadas para eficiência de token.

→ Sessão 2.

---

### Anthropic — Introducing the Model Context Protocol (2024)

**ANTHROPIC. "Introducing the Model Context Protocol".** Anthropic News, 25 nov. 2024. <https://www.anthropic.com/news/model-context-protocol>

Anúncio do MCP, protocolo aberto que resolve o problema M×N de integrações entre modelos e ferramentas. Um ano depois, adotado por OpenAI, Google e Microsoft.

→ Sessão 2.

---

### Anthropic — Steering Claude Code (2026)

**ANTHROPIC. "Steering Claude Code".** Anthropic Blog, 2026. <https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more>

Separa os mecanismos que guiam o modelo, como arquivos de contexto, dos que impõem comportamento, como hooks e permissões — a base da regra de que proteção real precisa ser determinística.

→ Sessões 2, 10.

---

### Anthropic — Writing Effective Tools for Agents (2025)

**ANTHROPIC. "Writing effective tools for agents".** Anthropic Engineering, 2025. <https://www.anthropic.com/engineering/writing-tools-for-agents>

Critério verificável para catálogo de ferramentas: se uma pessoa da engenharia não sabe dizer qual ferramenta usar numa situação, o modelo também não saberá. Recomenda consolidar por fluxo de trabalho em vez de espelhar endpoints.

→ Sessão 2.

---

### Bass, Clements e Kazman — Software Architecture in Practice (2021)

**BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *Software Architecture in Practice*, 4ª ed.** Addison-Wesley (SEI Series in Software Engineering), 2021.

Referência canônica para o vocabulário de requisito arquiteturalmente significativo. Define o cenário de qualidade (*quality attribute scenario*) em seis elementos (fonte do estímulo, estímulo, ambiente, artefato, resposta, medida de resposta), o template que torna um requisito não funcional testável em vez de um adjetivo. Define tática arquitetural como "uma decisão que afeta o controle de uma ou mais respostas de atributo de qualidade", distinta de um padrão arquitetural por não incorporar, sozinha, os *trade-offs* entre características concorrentes.

→ Sessão 3.

---

### Beck — Test-Driven Development: By Example (2002)

**BECK, Kent. *Test-Driven Development: By Example*. Addison-Wesley, 2002.**

O ciclo vermelho-verde-refatoração, adaptado neste workshop para o fluxo assistido por LLM. Fundamenta a prática de TDD clássico, que neste material é combinado com agentes de codificação.

→ Sessão 6.

---

### Böckeler — Understanding Spec-Driven Development (2025)

**BÖCKELER, Birgitta. "Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl".** *martinfowler.com*, 15 out. 2025. <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html>

Comparação de três ferramentas de SDD que estabelece a taxonomia usada na Sessão 8 para distinguir graus de compromisso entre especificação e código: *spec-first* (a especificação orienta a primeira geração e pode ser abandonada depois), *spec-anchored* (especificação e código evoluem juntos, com reconciliação a cada mudança) e *spec-as-source* (a especificação é o artefato primário e o código é projeção regenerável). O argumento central é que ferramentas distintas não são equivalentes só porque todas produzem arquivos Markdown.

→ Sessões 5, 8.

---

### Boehm — Software Engineering Economics (1981)

**BOEHM, Barry W. *Software Engineering Economics*.** Prentice-Hall, 1981.

Documentou empiricamente que o custo de corrigir um defeito cresce a cada fase do desenvolvimento — em sistemas grandes e críticos, um problema descoberto depois da entrega pode custar da ordem de 100 vezes mais do que o mesmo problema pego na fase de requisitos. Pesquisa mais recente questiona o multiplicador exato em times ágeis com integração contínua, mas não a direção do efeito. Fundamenta por que reversibilidade e tempo de vida pesam na escolha entre vibe coding, assistência e SDD.

→ Sessão 1.

---

### Brown et al. — Language Models are Few-Shot Learners (2020)

**BROWN, Tom B. et al. *Language Models are Few-Shot Learners*.** NeurIPS, 2020. <https://arxiv.org/abs/2005.14165>

Demonstra que aumentar a escala de modelos de linguagem melhora substancialmente o desempenho em aprendizado com poucos exemplos, sem necessidade de ajuste fino. Apresenta o GPT-3, modelo autorregressivo com 175 bilhões de parâmetros, aplicado apenas via interação textual sem atualização de gradientes. Alcança desempenho competitivo em tradução, resposta a perguntas, preenchimento de texto, raciocínio e adaptação de domínio. Gera textos tão realistas que avaliadores humanos têm dificuldade em distinguir de conteúdo humano — mecanismo técnico que torna um prompt capaz de funcionar como programa (Software 3.0).

→ Sessão 1.

---

### Chen et al. — Codex e HumanEval (2021)

**CHEN, Mark et al. *Evaluating Large Language Models Trained on Code*.** arXiv:2107.03374, 2021. <https://arxiv.org/abs/2107.03374>

Apresenta Codex, versão do GPT ajustada em código do GitHub, com foco em síntese de programas em Python. Introduz HumanEval, novo conjunto de avaliação para medir correção funcional em síntese de código a partir de docstrings. Codex resolve 28,8% de problemas HumanEval (vs. 0% do GPT-3), aumentando para 70,2% com amostragem de 100 tentativas por problema. Analisa limitações com docstrings complexas e vinculação de variáveis. Contraste com o SWE-bench: mede capacidade de codificação, não de engenharia de software num repositório real.

→ Sessão 1.

---

### Chikofsky e Cross — Reverse Engineering and Design Recovery (1990)

**CHIKOFSKY, Elliot J.; CROSS II, James H. "Reverse Engineering and Design Recovery: A Taxonomy".** *IEEE Software*, v. 7, n. 1, p. 13-17, jan. 1990. DOI: [10.1109/52.43044](https://doi.org/10.1109/52.43044)

Taxonomia que define e relaciona seis termos da manutenção de software: engenharia direta, engenharia reversa, redocumentação, recuperação de projeto, reestruturação e reengenharia. A engenharia reversa é definida como a análise de um sistema para identificar seus componentes e as relações entre eles e para representá-lo em outra forma ou num nível mais alto de abstração, sem alterar o sistema. A recuperação de projeto é a subárea em que conhecimento de domínio, informação externa e dedução são acrescentados às observações do sistema para identificar abstrações de nível mais alto. Fundamenta o enquadramento da arqueologia de regras como recuperação de projeto restrita às decisões de negócio.

→ Sessão 4.

---

### Datacurve — DeepSWE Leaderboard

**DATACURVE. *DeepSWE Leaderboard*.** Publicado em benchlm.ai. <https://benchlm.ai/benchmarks/deepswe>

Leitura independente de modelos em 113 tarefas de engenharia de software de longo horizonte, tiradas de 91 repositórios de código aberto em 5 linguagens, verificadas por programa. Espelha o placar público do DeepSWE usando, para cada modelo, a melhor configuração disponível do `mini-swe-agent` — o que mede o par modelo mais arnês, e não o modelo isolado.

→ Sessões 1, 2.

---

### Decision Model and Notation (DMN)

**OMG. *Decision Model and Notation (DMN)*, versão 1.5.** Object Management Group, ago. 2024. <https://www.omg.org/spec/DMN/>

Padrão para representar regras condicionais como tabelas de decisão, complemento ao RuleSpeak para regras de cálculo e elegibilidade que combinam várias condições. Define sete políticas de acerto (*hit policies*) que resolvem o que fazer quando mais de uma linha da tabela poderia se aplicar: Unique (as regras nunca se sobrepõem), Any (podem se sobrepor, mas toda regra que casar produz a mesma saída), Priority (vale a de maior prioridade), First (vale a primeira que casar, de cima para baixo), Collect (retorna todos os resultados, com agregação opcional de soma, mínimo, máximo ou contagem), Rule Order e Output Order (retornam todos os resultados, em ordem de aparição ou de prioridade).

→ Sessão 4.

---

### Delimarsky — Spec-Driven Development with AI (2025)

**DELIMARSKY, Den. "Spec-driven development with AI: Get started with a new open source toolkit".** *The GitHub Blog*, 2 set. 2025. <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>

Post oficial de lançamento do GitHub Spec Kit — define o problema do vibe coding ("você descreve o objetivo, recebe um bloco de código de volta, e frequentemente... parece certo, mas não funciona direito") e o papel da especificação como "contrato para como seu código deve se comportar".

→ Sessões 1, 3, 5, 8.

---

### Diggs et al. — LLMs for Legacy Code Documentation (2024)

**DIGGS, Colin et al. *Leveraging LLMs for Legacy Code Modernization: Challenges and Opportunities for LLM-Generated Documentation*.** arXiv:2411.14971, nov. 2024. Versão resumida submetida ao workshop LLM4Code 2025, colocalizado com o ICSE 2025. <https://arxiv.org/abs/2411.14971>

Estudo empírico com quatro modelos (Claude 3.0 Sonnet, Llama 3 Instruct 70B, Mixtral 8×7B e GPT-4 Turbo Preview) na geração de comentários linha a linha para código legado em MUMPS, de um sistema de prontuário eletrônico, e em linguagem de montagem de mainframe IBM. Avaliadores com experiência profissional nas duas linguagens julgaram completude, legibilidade, utilidade e alucinação por rubrica. Os comentários foram, em geral, livres de alucinação, completos, legíveis e úteis em comparação com comentários de desenvolvedores, com resultado pior na linguagem de montagem, e nenhuma métrica automática testada (complexidade ciclomática, Halstead, BLEU, ROUGE, CHRF, similaridade de cosseno) apresentou correlação forte com a avaliação humana. Fundamenta, na Sessão 4, o limite do que se sabe sobre LLM na leitura de código legado. O estudo avalia a redocumentação, e esta bibliografia trata a aplicação do resultado à recuperação da intenção de negócio como inferência própria, sem medição publicada que a sustente.

→ Sessão 4.

---

### fast-check e FsCheck — Property-Based Testing

**fast-check** (JavaScript/TypeScript) e **FsCheck** (.NET) — bibliotecas de referência para testes baseados em propriedade.

→ Sessão 7.

---

### Feathers — Working Effectively with Legacy Code (2004)

**FEATHERS, Michael C. *Working Effectively with Legacy Code*.** Prentice Hall, 2004. ISBN 978-0-13-117705-5.

Referência para a manutenção de código sem testes. Cunha o termo *characterization test* (teste de caracterização) para o teste que descreve o comportamento real de um trecho de código: o teste é escrito depois do código, e o resultado observado na execução passa a ser a expectativa registrada. Fundamenta a distinção, na Sessão 4, entre o teste que registra o comportamento implementado e o teste de aceitação que verifica a intenção confirmada pelo domínio.

→ Sessão 4.

---

### Fission-AI — OpenSpec

**FISSION-AI. *OpenSpec*.** Repositório de software. <https://github.com/Fission-AI/OpenSpec>

Ferramenta de SDD que organiza o trabalho em torno da mudança, não da funcionalidade: um espaço descreve o comportamento atual do sistema e outro contém uma pasta por mudança proposta, com proposta, especificação-delta, design e tarefas. O arquivamento incorpora o delta à especificação principal e preserva o histórico da mudança. Serve na Sessão 8 como contraste ao Spec Kit, por operar sem uma camada de princípios de projeto acima das mudanças individuais.

→ Sessão 8.

---

### Ford, Parsons, Kua e Sadalage — Building Evolutionary Architectures (2023)

**FORD, Neal; PARSONS, Rebecca; KUA, Patrick; SADALAGE, Pramod. *Building Evolutionary Architectures: Automated Software Governance*, 2ª ed.** O'Reilly Media, 2023.

Origem do termo função de aptidão arquitetural (*architectural fitness function*): "uma função de aptidão arquitetural fornece uma avaliação objetiva de integridade de alguma característica arquitetural." A tríade usada neste workshop para documentar uma função de aptidão (limiar, responsável, reação à falha) é uma adaptação pedagógica para fins de verificação prática, não uma citação literal do livro; o texto original classifica funções de aptidão por outros eixos (atômica ou holística, disparada ou contínua, estática ou dinâmica, entre outros).

→ Sessão 3.

---

### GitHub Spec Kit

**GitHub Spec Kit.** Implementação de referência open source do Spec-Driven Development (SDD) — mais de 90 mil estrelas no GitHub. Define os quatro artefatos canônicos (`constitution.md`, `spec.md`, `plan.md`, `tasks.md`) e os comandos `/specify`, `/plan`, `/tasks`, compatíveis com Claude Code, GitHub Copilot e Cursor. O modelo de especificação (`spec-template.md`) numera cada requisito funcional com prefixo `FR-001`, `FR-002` etc., em frases no padrão "o sistema deve..."; não reserva uma seção separada para requisito não funcional.

→ Sessões 3, 5, 8.

---

### gszhangwei — OpenSPDD

**GSZHANGWEI. *OpenSPDD: A SPDD AI coding assistant command template manager*.** Repositório de software. <https://github.com/gszhangwei/open-spdd>

Implementação de referência da comunidade para o método SPDD, com os comandos que materializam o fluxo: analisar requisitos e código existente, produzir o Painel REASONS, gerar a implementação e sincronizar de volta as alterações feitas no código. A distinção que o projeto faz entre plano e Painel é a citada na Sessão 8: um plano diz o que fazer, o Painel especifica como fazer. Projeto de terceiros, não vinculado à Thoughtworks.

→ Sessão 8.

---

### Hunt e Thomas — Software Archaeology (2002)

**HUNT, Andy; THOMAS, Dave. "Software Archaeology".** *IEEE Software*, v. 19, n. 2, p. 20-22, mar./abr. 2002. DOI: [10.1109/52.991327](https://doi.org/10.1109/52.991327)

Coluna da série dos autores na *IEEE Software* que desenvolve a analogia entre arqueologia e leitura de código herdado. A coluna abre com a queixa de um programador anônimo para quem o trabalho diante de código antigo era arqueologia, e os autores descrevem a arqueologia propriamente dita como a investigação de uma situação em que se procura entender o que se vê e como as partes se encaixam. A analogia é anterior à coluna: os autores registram que eles, Brian Marick e Ward Cunningham conduziram um workshop sobre *Software Archaeology* na OOPSLA 2001. A coluna também adverte que é perigoso supor que o código ou os comentários sejam inteiramente verdadeiros. Fundamenta, na Sessão 4, a origem da analogia que dá nome ao Tema 2 e o peso baixo atribuído ao comentário como evidência.

→ Sessão 4.

---

### ISO/IEC/IEEE 29148:2018

**ISO/IEC/IEEE. *Systems and software engineering — Life cycle processes — Requirements engineering*, 29148:2018.** <https://www.iso.org/standard/72089.html>

Norma internacional de engenharia de requisitos, sucessora do IEEE 830. Distingue requisito funcional (o que o sistema deve fazer) de requisito não funcional ou de qualidade (o critério usado para julgar como o sistema opera, não um comportamento específico), e subdivide requisito não funcional em classes mais finas — desempenho, usabilidade, interface, entre outras. O texto normativo integral está atrás de paywall; a distinção funcional/não funcional citada aqui segue paráfrase amplamente aceita do padrão, não transcrição literal.

→ Sessão 3.

---

### Jimenez et al. — SWE-bench (2024)

**JIMENEZ, Carlos E. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*.** ICLR, 2024. <https://arxiv.org/abs/2310.06770>

Apresenta SWE-bench, benchmark contendo 2.294 problemas reais de engenharia de software extraídos do GitHub em 12 repositórios Python populares. Avalia capacidade de modelos em editar bases de código para resolver problemas, exigindo compreensão de múltiplas funções, classes, arquivos e interação com ambientes de execução. Modelos de ponta, incluindo Claude 2, resolvem apenas 1,96% dos problemas no artigo original; em 2026, os melhores agentes resolvem cerca de 97% na versão revisada (SWE-bench Verified) — a evidência quantitativa por trás de "por que agora".

→ Sessão 1.

---

### Karpathy — Software 2.0 (2017)

**KARPATHY, Andrej. "Software 2.0".** Medium, nov. 2017. <https://karpathy.medium.com/software-2-0-a64152b37c35>

Ensaio precursor da tese de Software 3.0: uma rede neural treinada é compilada a partir de dados por um processo de otimização, um tipo de programa fundamentalmente diferente do código explícito escrito à mão.

→ Sessão 1.

---

### Karpathy — Software Is Changing Again (2025)

**KARPATHY, Andrej. *Software Is Changing (Again)*.** Palestra, YC AI Startup School, 17 jun. 2025. Recapitulação: Latent Space, <https://www.latent.space/p/s3>

Formulação dos três paradigmas coexistentes: Software 1.0 (código explícito), Software 2.0 (redes neurais treinadas), Software 3.0 (prompt em linguagem natural como programa executável); e do conceito de *generation-verification loop* ("demo is works.any(), product is works.all()"). Karpathy também cunhou o termo *vibe coding*, em publicação de fevereiro de 2025.

→ Sessão 1.

---

### Lei Complementar 214/2025 — IBS, CBS e Imposto Seletivo

**BRASIL. *Lei Complementar nº 214, de 16 de janeiro de 2025: texto compilado*.** Presidência da República, com alterações posteriores, inclusive da Lei Complementar nº 227/2026. <https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm>. Acesso em: 29 set. 2026.

Institui IBS, CBS e Imposto Seletivo. Os arts. 112, 113, 116, 117, 118 e 124, recorte usado na Sessão 4, disciplinam a devolução personalizada para pessoas físicas de famílias de baixa renda: instituição da devolução (art. 112), destinatário e critérios cumulativos (art. 113), momento da devolução (art. 116), consumo considerado e ressalva do Imposto Seletivo (art. 117, com redação da LC 227/2026), percentuais e limite de ampliação por lei específica (art. 118) e definição de devolução geral e devolução específica (art. 124). É a única fonte legal do exercício de mapa de regras e testes da Sessão 4.

→ Sessão 4.

---

### MADR — Markdown Architectural Decision Records v4

**MADR (Markdown Architectural Decision Records) v4.** Template leve para registro de decisões arquiteturais — contexto, opções consideradas, decisão, consequências.

→ Sessão 10.

---

### Mendes — Controle e Autonomia (Módulo 4, Agentes)

**MENDES, Marco. "Controle e Autonomia".** *Arquitetura de Soluções com IA Generativa*, Módulo 4 — Agentes. <https://aulas-marco.github.io/arquitetura-solucoes-ia-generativa/modulo-4-agentes/controle-e-autonomia/>

Material da disciplina de pós-graduação que fundamenta a distinção entre workflow e agente usada nesta sessão. Define quatro formas de controle operacional (chatbot, copiloto, fluxo de trabalho determinístico e agente), distinguidas por uma única pergunta: quem escolhe a próxima transição. A categorização separa controle de qualidade ou maturidade: um fluxo de trabalho bem desenhado pode superar um agente mal supervisionado, e um copiloto que chama ferramenta de leitura continua copiloto, não agente. Cataloga também os critérios técnicos que justificam a escolha de um agente: sequências de comprimento variável, feedback de ferramenta verificável, erros conteníveis, conclusão observável e autoridade/orçamento delimitados.

→ Sessão 1.

---

### Meszaros — xUnit Test Patterns (2007)

**MESZAROS, Gerard. *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley, 2007.**

Referência canônica em padrões de teste. Cataloga 60+ padrões para escrever testes mantíveis e confiáveis em frameworks xUnit (JUnit, NUnit, etc.). Cobre testes de unidade, integração e aceitação com padrões como Arrange-Act-Assert, Test Fixtures, Mocks, Stubs e Test Data Builders. Fundamenta a cultura xUnit adotada no workshop (C# com xUnit, JavaScript/TypeScript com Jest). Essencial para qualidade de teste: sem padrões aplicados, testes viram débito técnico que desacelera evolução — base para TDD assistido por IA e para detectar quando o agente erra ao gerar testes.

→ Sessão 6.

---

### METR — Experienced Developer Productivity (2025)

**METR. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*.** jul. 2025. <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>

Experimento randomizado com 16 desenvolvedores experientes (cerca de 5 anos de trajetória nos próprios projetos) em 246 tarefas reais de manutenção de código aberto. Usar IA tornou a conclusão das tarefas 19% mais lenta. Mais revelador ainda: os próprios desenvolvedores, depois de terminar, estimaram que a IA os havia deixado 20% mais rápidos — o oposto exato do que os dados mediram. Contraponto empírico direto à métrica de produtividade de Peng et al., evidenciando a diferença entre tarefas novas e delimitadas (onde vibe coding ganha) versus manutenção em sistema maduro com contexto implícito.

→ Sessão 1.

---

### OMG — Semantics of Business Vocabulary and Business Rules

**OMG. *Semantics of Business Vocabulary and Business Rules (SBVR)*, versão 1.5.** Object Management Group, dez. 2019. <https://www.omg.org/spec/SBVR/1.5/About-SBVR/>

Especificação para vocabulário de negócio e regras formais, usada como base do bloco de especificação em linguagem controlada. Distingue duas categorias de regra. A **regra estrutural** (ou definicional) usa operadores aléticos ("é necessário que", "é possível que") para dizer como o negócio organiza e define seus próprios conceitos. A **regra operativa** (ou comportamental) usa operadores deônticos ("é obrigatório que", "é permitido que") para reger conduta e é a única das duas que alguém pode efetivamente violar.

→ Sessão 4.

---

### Osmani — Agent Harness Engineering (2026)

**OSMANI, Addy. "Agent Harness Engineering".** Blog pessoal, 2026. <https://addyosmani.com/blog/agent-harness-engineering/>

Síntese prática do mesmo achado: um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

→ Sessão 2.

---

### Paul e Elder — The Thinker's Guide to Socratic Questioning (2019)

**PAUL, Richard; ELDER, Linda. *The Thinker's Guide to Socratic Questioning*.** Foundation for Critical Thinking Press, 2019.

Define o questionamento socrático como a forma disciplinada de pensamento crítico aplicada em diálogo, e não como técnica de retórica: uma pergunta bem colocada expõe a estrutura lógica de um pensamento (o que ele pressupõe, que evidência sustenta, que implicação segue) em vez de aceitar a primeira formulação como definitiva. Classifica as perguntas em seis categorias — esclarecimento, pressupostos, evidências e razões, implicações e consequências, pontos de vista alternativos, e perguntas sobre a própria pergunta —, adotadas neste workshop como as seis categorias da entrevista socrática. O argumento central é que perguntar bem adia o fechamento em uma única leitura, e por isso mantém mais de uma interpretação viva por mais tempo do que a convergência prematura permitiria.

→ Sessão 3.

---

### Pearce et al. — Copilot Security (2022)

**PEARCE, Hammond et al. *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions*.** IEEE Symposium on Security and Privacy (S&P), 2022. <https://arxiv.org/abs/2108.09293>

Investiga segurança do GitHub Copilot avaliando com que frequência recomenda código inseguro. Criou 89 cenários sobre vulnerabilidades de alto risco (Top 25 MITRE), gerando 1.689 programas. Resultado preocupante: aproximadamente 40% foram classificados como vulneráveis. Atribui achado ao fato de Copilot ser treinado em código aberto do GitHub, que inclui código bugado e padrões explorados — base empírica para o risco "sem rede" do vibe coding.

→ Sessão 1.

---

### Peng et al. — Copilot Productivity (2023)

**PENG, Sida; KALLIAMVAKOU, Eirini; CIHON, Peter; DEMIRER, Mert. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*.** arXiv:2302.06590, 2023. <https://arxiv.org/abs/2302.06590>

Experimento randomizado com 70 desenvolvedores profissionais que completam uma tarefa de implementação de servidor HTTP. O grupo com Copilot completou a tarefa 55,8% mais rápido (71 minutos contra 161 minutos). O efeito foi maior para desenvolvedores menos experientes, sugerindo que a assistência reduz a curva de aprendizado para tarefas bem delimitadas e novas, onde o contexto é contido e explícito.

→ Sessão 1.

---

### Ross (ed.) — Business Rules Manifesto (2003)

**ROSS, Ronald G. (ed.). *Business Rules Manifesto — The Principles of Rule Independence*, versão 2.0.** Business Rules Group, 1 nov. 2003. <https://www.businessrulesgroup.org/brmanifesto/BRManifesto.pdf>

Dez artigos que definem regra de negócio como categoria própria de conhecimento, separada de processo. O Artigo 2 ("Separate From Processes, Not Contained In Them") declara que "regras não são processo nem procedimento" e que "regras se aplicam através de processos e procedimentos". Deve existir um corpo coeso de regras, cumprido de forma consistente em toda a atividade de negócio relevante. O Artigo 4 ("Declarative, Not Procedural") exige que toda regra seja expressa em frase declarativa, sem sequenciamento implícito: é essa declaratividade que distingue uma regra de negócio (BR) de um passo de um fluxo.

→ Sessão 3.

---

### Ross — RuleSpeak

**ROSS, Ronald G. *RuleSpeak Sentence Forms*, versão 2.2.** Business Rule Solutions, LLC. Desenvolvido a partir de 1996. <https://www.rulespeak.com/en/>

Notação em linguagem natural controlada para expressar regra de negócio sem ambiguidade. O documento normativo organiza cinco formas de sentença em torno de duas palavras-chave de regra e duas de conselho: **"must"** (algo é exigido), **"must not"** (algo é proibido), **"may ... only"** (permissão condicional, que continua sendo regra de negócio, com exceção explícita) e, como *statements of advice*, que o documento classifica à parte das regras, **"may"** isolado e **"need not"**. O próprio documento afirma que o RuleSpeak foi "uma das três notações de referência usadas na criação do SBVR, e é consistente com esse padrão".

→ Sessão 4.

---

### Sneed e Erdős — Extracting Business Rules from Source Code (1996)

**SNEED, Harry M.; ERDŐS, Katalin. "Extracting Business Rules from Source Code".** In: *WPC '96, 4th Workshop on Program Comprehension*, Berlim, 1996. IEEE Computer Society Press, p. 240-247. DOI: [10.1109/WPC.1996.501138](https://doi.org/10.1109/WPC.1996.501138)

Revisa o estado da arte da aquisição de conhecimento de aplicação a partir de sistemas existentes, define o papel das regras de negócio nesse conhecimento e propõe um método de extração que parte da identificação das saídas de dados e reduz o programa às instruções que contribuem para cada saída (*program stripping*). O método foi implementado na ferramenta de engenharia reversa SOFT-REDOC, para programas COBOL, com o objetivo de ajudar o analista de negócio a compreender programas legados.

→ Sessão 4.

---

### StrykerJS e Stryker.NET — Mutation Testing

**StrykerJS** (JavaScript/TypeScript) e **Stryker.NET** (.NET) — ferramentas de referência para testes de mutação.

→ Sessão 7.

---

### Trivedy — The Anatomy of an Agent Harness (2026)

**TRIVEDY, Vivek. "The Anatomy of an Agent Harness".** *LangChain Blog*, 2026. <https://www.langchain.com/blog/the-anatomy-of-an-agent-harness>

Formulação canônica do arnês (*harness*) como tudo o que cerca o modelo e o transforma em agente: "if you're not the model, you're the harness". Traz a medição de que a mesma família de modelo muda de faixa no Terminal Bench 2.0 quando só o arnês muda.

→ Sessão 2.

---

### Vaswani et al. — Attention Is All You Need (2017)

**VASWANI, Ashish et al. *Attention Is All You Need*.** NeurIPS, 2017. <https://arxiv.org/abs/1706.03762>

Apresenta a arquitetura Transformer, substituindo modelos recorrentes e convolucionais complexos por mecanismos de atenção puros. Alcançou desempenho estado-da-arte em tradução automática: 28,4 BLEU em English-to-German e 41,8 BLEU em English-to-French (treinado em apenas 3,5 dias em oito GPUs). A arquitetura oferece melhor paralelização, reduz significativamente o tempo de treinamento e generaliza bem para outras tarefas, como análise sintática. O trabalho fundou a base para todos os modelos de linguagem modernos.

→ Sessão 1.

---

### Vercel — Removing 80% of Agent Tools (2026)

**VERCEL. "We removed 80% of our agent's tools".** *Vercel Blog*, 2026. <https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools>

Relato de redução de dezesseis ferramentas especializadas para acesso a sistema de arquivos num agente de texto para SQL, com taxa de sucesso subindo de 80% para 100% e 40% menos passos — evidência de que catálogo mínimo de ferramentas é decisão de qualidade.

→ Sessão 2.

---

### Vincent e Prime Radiant — Superpowers (2026)

**VINCENT, Jesse; PRIME RADIANT. *Superpowers: An agentic skills framework & software development methodology*.** Repositório de software. <https://github.com/obra/superpowers>

Conjunto de habilidades combináveis para agentes de codificação, acionadas automaticamente conforme a situação, com uma metodologia de execução em volta: levantamento de ideias e aprovação do design antes de qualquer código, cópia isolada do repositório, plano de tarefas pequenas, ciclo vermelho-verde-refatorar obrigatório, revisão em duas etapas e verificação antes de declarar conclusão. Entra na Sessão 8 como o contraponto que mostra que disciplina documental e disciplina operacional são eixos independentes: o projeto não mantém especificação consolidada do domínio e ainda assim é mais exigente que o Spec Kit na execução.

→ Sessão 8.

---

### Wei et al. — Chain-of-Thought Prompting (2022)

**WEI, Jason et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.** NeurIPS, 2022. <https://arxiv.org/abs/2201.11903>

Demonstra que solicitar ao modelo que gere uma sequência de passos intermediários de raciocínio (*chain of thought*) melhora significativamente o desempenho em tarefas de raciocínio complexo. A técnica emerge naturalmente em modelos suficientemente grandes quando exemplos de raciocínio são fornecidos como demonstrações no prompt. Experimentos comprovam ganho em tarefas aritméticas, senso comum e raciocínio simbólico. Um modelo de 540B parâmetros com apenas oito exemplos alcança estado-da-arte no benchmark GSM8K, superando até GPT-3 ajustado com verificador: a metade "raciocínio" que o ReAct combina com ação.

→ Sessão 1.

---

### Wiegers e Beatty — Software Requirements (2013)

**WIEGERS, Karl; BEATTY, Joy. *Software Requirements*, 3ª ed.** Microsoft Press, 2013. <https://www.microsoftpressstore.com/store/software-requirements-9780735679665>

Referência de mercado em engenharia de requisitos. Organiza requisitos em camadas (requisito de negócio, requisito de usuário, requisito funcional de software) e trata regra de negócio como categoria própria e anterior a essas camadas: uma regra de negócio não é, em si, um requisito de software, porque também rege operação manual; ela é a origem de onde requisitos funcionais são derivados, não um requisito por si só.

→ Sessão 3.

---

### Willison — What is Agentic Engineering (2026)

**WILLISON, Simon. "What is agentic engineering?"** — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026. <https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/>

Define engenharia agêntica como "a prática de desenvolver software com o auxílio de agentes de codificação", sustentada por três responsabilidades humanas (especificação do problema, provisão de ferramentas, verificação e iteração), e distingue a prática de "vibe coding", termo que reserva para código de protótipo não revisado.

→ Sessão 1.

---

### Yao et al. — ReAct (2023)

**YAO, Shunyu et al. *ReAct: Synergizing Reasoning and Acting in Language Models*.** ICLR, 2023. <https://arxiv.org/abs/2210.03629>

Propõe ReAct, que integra raciocínio e ação em modelos de linguagem, permitindo que gerem simultaneamente pensamento e ações específicas da tarefa. O raciocínio induz e atualiza planos de ação; as ações permitem interface com fontes externas como bases de conhecimento. Reduz alucinação em QA ao integrar APIs de conhecimento e alcança 34% e 10% de melhoria em benchmarks ALFWorld e WebShop em relação a métodos de imitação. As trajetórias de resolução são mais interpretáveis e confiáveis que abordagens sem raciocínio — a base técnica que distingue um agente de codificação de um LLM respondendo uma pergunta isolada.

→ Sessão 1.

---

### Zhang e Xia — Structured Prompt-Driven Development (2026)

**ZHANG, Wei; XIA, Jing Jing. "Structured-Prompt-Driven Development (SPDD)".** *martinfowler.com*, 28 abr. 2026. <https://martinfowler.com/articles/structured-prompt-driven/>

Método desenvolvido por um time de tecnologia interna da Thoughtworks que trata o prompt como artefato de entrega versionado, organizado no Painel REASONS de sete dimensões (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards). O artigo é também a fonte do diagnóstico usado na Sessão 8 sobre por que escalar geração desloca o gargalo, com a metáfora do motor de Ferrari em estrada ruim: a potência local não determina o horário de chegada. Os autores são explícitos sobre os limites do método, incluindo o custo de experiência sênior antecipada e a variação remanescente entre praticantes que escrevem o mesmo Painel.

→ Sessão 8.

---

### Zeller — Why Programs Fail (2005)

**ZELLER, Andreas. *Why Programs Fail: A Guide to Systematic Debugging*. Morgan Kaufmann, 2005.**

Livro clássico sobre depuração sistemática de programas. Apresenta metodologia científica aplicada à localização de erros: reproduzir o defeito consistentemente, formular hipóteses sobre causas, projetar testes para refutá-las e isolar o código responsável. Zeller desenvolve técnicas como delta debugging (automatizar redução de entradas que causam falha), execução reversa e análise de dependência. Fundamental para engenheiros que buscam evitar tentativa-e-erro em depuração, oferecendo processos rigorosos e automatizáveis para diagnóstico — base do protocolo hipótese → investigação → correção → verificação usado na Sessão 9.

→ Sessão 9.

---

## Apêndice — Ativar e conferir a memória do Claude

Este roteiro cobre os recursos de memória do Claude nas aplicações de conversa e no Claude Code, com seus controles, escopos e locais de armazenamento. Cada técnica traz os passos de configuração e um roteiro curto para testar se a configuração produziu efeito, e a busca de chats anteriores fica na última seção.

!!! info "Ambiente desta edição"
    As fontes oficiais listadas abaixo foram consultadas em 30/09/2026. O único teste local foi `claude --version`, que retornou `2.1.285 (Claude Code)` em macOS. Os caminhos de interface do Claude web, Desktop e Mobile e os comandos `/init`, `/context` e `/memory` foram conferidos na documentação, sem execução numa conta de participante, e plano e tipo de conta não foram verificados. Ao repetir os roteiros, anote aplicação, versão, plataforma, plano, data e resultado, e corrija o passo que divergir da tela observada.

Fontes oficiais:

- [Anthropic — Usar busca de chats e memória no Claude](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- [Anthropic — Criar e gerenciar projetos](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Anthropic — Como Claude Code lembra seu projeto](https://code.claude.com/docs/en/memory)
- [Anthropic — Importar e exportar memória](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude)

### Escolha o mecanismo

| Necessidade | Recurso | Onde fica |
|---|---|---|
| Claude lembrar preferências e contexto entre conversas | Memória das conversas | Claude web, Desktop e Mobile: **Configurações → Memória** |
| Manter contexto de um assunto separado dos demais | Memória de projeto | Conversas dentro de um **Projeto** do Claude |
| Fixar convenções de um repositório para sessões de programação | `CLAUDE.md` | Arquivo no repositório ou na pasta pessoal do Claude Code |
| Permitir que Claude Code anote aprendizados por repositório | Memória automática | Comando `/memory` no Claude Code |
| Encontrar o que foi dito em um chat anterior | Busca e referência a chats | Alternância em **Configurações → Memória** e consulta no chat |

Memória de conversas e busca de chats têm controles próprios, e o arquivo `CLAUDE.md` fornece instruções persistentes ao Claude Code.

### Memória das conversas no Claude

A Anthropic informa que a memória vem ligada por padrão nos planos Free, Pro e Max. Nos planos Team e Enterprise, um proprietário precisa habilitá-la para a organização antes de o membro ativá-la.

1. Abra o Claude e entre em **Configurações → Memória**.
2. Ative **Gerar memória a partir dos chats** (*Generate memory from chats*).

!!! warning "Se a opção não aparecer"
    Em Team ou Enterprise, peça ao proprietário que confira **Configurações da organização → Capacidades**, porque algumas organizações têm restrições de disponibilidade. Se a conta ainda mostrar **Memória** dentro de **Configurações → Capacidades**, siga a seção de experiência legada da [documentação oficial](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#information-for-legacy-memory-users) e anote esse caminho.

#### Roteiro de teste: memória das conversas

1. Em uma conversa comum, peça: “Lembre que, neste workshop, prefiro exemplos de C# e TypeScript.”
2. Abra **Configurações → Memória → Tópicos** e confira se a entrada foi criada.
3. Inicie uma nova conversa comum e pergunte qual linguagem você prefere nos exemplos.
4. Compare a resposta com a entrada exibida em Tópicos. O teste passa quando a resposta cita C# e TypeScript sem que você repita a preferência.

### Memória de projeto

Crie um projeto em **Projetos → Novo projeto** e abra uma conversa dentro dele. Cada projeto tem seu próprio espaço de memória, separado dos chats comuns e dos demais projetos. Use **Definir instruções do projeto** para orientações que devem valer em todas as conversas do projeto e coloque documentos de referência na base de conhecimento do projeto.

#### Roteiro de teste: memória de projeto

1. Crie o projeto “Teste de memória” e, na primeira conversa dele, diga: “Neste projeto, os testes usam xUnit.”
2. Abra uma segunda conversa no mesmo projeto e pergunte qual framework de teste o projeto usa. A resposta esperada é xUnit.
3. Abra uma conversa comum, fora de qualquer projeto, e faça a mesma pergunta. O teste passa quando essa conversa não recupera a informação do projeto.

### Instruções persistentes com `CLAUDE.md`

1. No terminal, entre na raiz do repositório e execute `claude`.
2. Dentro da sessão, execute `/init` para gerar uma proposta inicial de `CLAUDE.md`. Se o arquivo já existir, o comando sugere melhorias ao conteúdo existente.
3. Revise o arquivo e registre comandos de build e teste, estrutura do projeto e convenções que devem valer em todas as sessões. Um exemplo curto:

   ```markdown
   # Convenções do projeto

   - Execute `npm test` antes de propor um commit.
   - Código de interface fica em `src/ui/`.
   - Exemplos de API usam TypeScript.
   ```

O arquivo `./CLAUDE.md` ou `./.claude/CLAUDE.md` serve ao projeto e pode ser versionado com a equipe. O arquivo `~/.claude/CLAUDE.md` serve às preferências pessoais em todos os projetos daquela máquina. Essas instruções orientam o comportamento do agente e não bloqueiam ações tecnicamente.

#### Roteiro de teste: `CLAUDE.md`

1. Encerre a sessão e inicie uma nova com `claude` no mesmo repositório.
2. Execute `/context` e confirme que o arquivo aparece em **Memory files**.
3. Pergunte: “Qual comando devo rodar antes de propor um commit?” A resposta esperada é `npm test`, conforme o exemplo acima.
4. Execute `/memory` e confirme que o `CLAUDE.md` editado está entre os arquivos carregados.

### Memória automática do Claude Code

1. Na sessão do Claude Code, execute `/memory`.
2. Confira a alternância de **auto memory**, que a documentação descreve como ligada por padrão. Se estiver desligada, ative-a no menu, e o controle gravará `autoMemoryEnabled` nas configurações do usuário.

A memória automática fica em `~/.claude/projects/<project>/memory/`, é local à máquina e é compartilhada entre worktrees do mesmo repositório. O índice `MEMORY.md` é carregado no início da conversa, e os arquivos de tópicos são lidos quando necessários. Para desativar apenas em um projeto, a documentação descreve `"autoMemoryEnabled": false` em `.claude/settings.json`.

#### Roteiro de teste: memória automática

1. Peça uma lembrança útil para sessões futuras, como “Lembre que os testes de integração deste projeto exigem Redis local”.
2. Volte a `/memory`, abra a pasta de memória automática e confira o índice `MEMORY.md` e o arquivo do tópico criado, se houver.
3. Abra uma nova sessão no mesmo repositório e pergunte o que os testes de integração exigem. O teste passa quando a resposta cita Redis local.
4. Se a informação não voltar, confira o arquivo antes de concluir que o recurso falhou, porque a gravação não ocorre necessariamente em toda sessão.

### Trazer memória de outro assistente

No Claude web ou Desktop, abra **Configurações → Memória → Iniciar importação**, cole o texto exportado do serviço anterior e selecione **Adicionar à memória**. A Anthropic classifica a importação como experimental, informa que nem toda entrada será incorporada e documenta o recurso para Free, Pro, Max e Team.

#### Roteiro de teste: importação

1. Antes de importar, anote duas ou três preferências presentes no texto exportado.
2. Depois da importação, abra **Configurações → Memória → Tópicos** e verifique quais delas foram registradas como entradas.
3. Em uma nova conversa, pergunte por uma das preferências importadas e compare a resposta com o tópico correspondente.

### Revisar, pausar e apagar

Na memória de conversas, **Configurações → Memória → Tópicos** permite ler, editar e excluir entradas. **Pausar memória** preserva as entradas sem usá-las ou criar outras, e **Redefinir memória** apaga as entradas, inclusive as dos projetos, de forma irreversível. Chats anônimos não entram na memória.

No Claude Code, `/memory` abre os arquivos de instrução e a pasta de memória automática para inspeção. Antes de excluir um arquivo, confirme seu escopo: pessoal, projeto ou organização.

#### Roteiro de teste: pausa

1. Ative **Pausar memória** e, em uma nova conversa, pergunte pela preferência gravada no roteiro da memória das conversas.
2. Confirme que a resposta não usa a preferência e que a entrada continua listada em Tópicos.
3. Retome a memória e repita a pergunta em outra conversa para confirmar que a preferência voltou a ser usada.

### Busca e referência a chats anteriores

Nos planos pagos Pro, Max, Team e Enterprise, a alternância **Buscar e referenciar chats** fica em **Configurações → Memória**. Dentro de um projeto, a busca fica limitada às conversas daquele projeto, e nos chats comuns ela cobre os chats fora de projetos. A disponibilidade pode depender da implantação gradual na conta.

1. Abra **Configurações → Memória**.
2. Ative **Buscar e referenciar chats**.

#### Roteiro de teste: busca de chats

1. Em um chat comum, discuta um assunto com termo fácil de reconhecer, como “faixa de atacado da regra de desconto”.
2. Abra um novo chat comum e pergunte: “O que discutimos sobre a faixa de atacado?”
3. Observe se a busca aparece como chamada de ferramenta, com referência ao chat de origem. O teste passa quando a resposta aponta o chat do passo 1.
4. Repita a pergunta dentro de um projeto. A busca deve ficar restrita às conversas daquele projeto e não deve encontrar o chat comum.
