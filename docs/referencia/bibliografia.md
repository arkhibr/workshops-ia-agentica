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

## Engenharia de Software na Era dos LLMs

**KARPATHY, Andrej. *Software Is Changing (Again)*.** Palestra, YC AI Startup School, 17 jun. 2025. Recapitulação: Latent Space, <https://www.latent.space/p/s3>. Formulação dos três paradigmas coexistentes — Software 1.0 (código explícito), Software 2.0 (redes neurais treinadas), Software 3.0 (prompt em linguagem natural como programa executável) — e do conceito de *generation-verification loop* ("demo is works.any(), product is works.all()"). Karpathy também cunhou o termo *vibe coding*, em publicação de fevereiro de 2025.
→ Sessão 1.

**WILLISON, Simon. "What is agentic engineering?"** — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026. <https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/>. Define engenharia agêntica como "a prática de desenvolver software com o auxílio de agentes de codificação", sustentada por três responsabilidades humanas — especificação do problema, provisão de ferramentas, verificação e iteração — e distingue a prática de "vibe coding", termo que reserva para código de protótipo não revisado.
→ Sessão 1.

**Glossário controlado — disciplina de Arquitetura de Soluções com IA Generativa (Arkhi).** Definições compartilhadas de *vibe coding*, *janela de contexto*, *agente de codificação*, *SDD*, *spec* e *constitution* — vocabulário comum entre os dois cursos da Arkhi sobre IA aplicada à engenharia de software.
→ Sessão 1.
