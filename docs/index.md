# Workshop: IA Agêntica na Prática

Workshop de engenharia agêntica disciplinada para equipes de desenvolvimento C#, JavaScript e TypeScript. Dez sessões que levam o time do uso ad hoc de LLMs (cada desenvolvedor com seu próprio jeito de pedir código, sem vocabulário ou contrato compartilhado) a uma esteira de engenharia com IA como parceiro de execução controlado e saídas previsíveis.

A tese: a janela de contexto virou o programa. O LLM é o interpretador; o desenvolvedor escreve em linguagem natural, e o que era arte ou intuição agora é engenharia — especificação, decomposição, verificação. O piso sobe para todos; o teto sobe só com disciplina; o julgamento humano sobe de valor.

**Público:** desenvolvedores C#, JavaScript e TypeScript com experiência intermediária nessas linguagens, que já experimentam IA no dia a dia sem processo formal.

**Formato:** 10 sessões de 2h cada (problema → método → exercício), 20h no total, modalidade online. Cenários genéricos C#/JS/TS alternam com casos de projetos de pesquisa da ACME, uma universidade fictícia, no Bloco 3.

**Cadeia de ferramentas:** conteúdo metodológico agnóstico ao ambiente. Recomendado Claude Code + Codex CLI; também compatível com GitHub Copilot + VS Code/JetBrains e Cursor IDE, todos via os comandos `/specify` · `/plan` · `/tasks` do [GitHub Spec Kit](referencia/bibliografia.md).

---

## Agenda

| Bloco | Sessões | Tema | Intenção metodológica |
|---|---|---|---|
| 1 — Fundamentos | S1–S2 | O novo modelo mental, a primeira ferramenta nas mãos | Software 3.0 · Engenharia Agêntica · cadeia de ferramentas e isolamento por ramo |
| 2 — Especificação e Planejamento | S3–S5 | A habilidade mais valiosa da era agêntica: dizer o quê com precisão | Requisitos BR/FR/NFR · SBVR + RuleSpeak + tabelas de decisão · caminho básico do Spec Kit, da regra ao código |
| 3 — Execução e adoção | S6–S7 | Do plano ao código verificado, e do uso individual ao uso por papel | Qualidade da spec e teste antes do código · casos de uso de IA por papel, com mural das equipes e pitch |
| 4 — Automação, qualidade e integração | S8–S10 | Skills e agentes próprios, depuração com método e SDD de ponta a ponta | Criação de skills e agentes · depuração sistemática · SDD ciclo completo |

## Sessões

| # | Sessão | Bloco |
|---|---|---|
| S1 | [O que mudou](sessao-01-o-que-mudou/index.md) | 1 — Fundamentos |
| S2 | [O ambiente agêntico](sessao-02-ambiente-agentico/index.md) | 1 — Fundamentos |
| S3 | [Exploração e especificação](sessao-03-exploracao-especificacao/index.md) | 2 — Especificação e Planejamento |
| S4 | [Regras formais com IA](sessao-04-regras-formais-com-ia/index.md) | 2 — Especificação e Planejamento |
| S5 | [Spec Kit: da regra ao código](sessao-05-decomposicao/index.md) | 2 — Especificação e Planejamento |
| S6 | [Spec Kit: qualidade da spec e teste antes do código](sessao-06-spec-kit-aprofundado/index.md) | 3 — Execução e adoção |
| S7 | [Casos de uso de IA por papel](sessao-07-casos-de-uso-por-papel/index.md) | 3 — Execução e adoção |
| S8 | [Skills e agentes](sessao-08-skills-e-agentes/index.md) | 4 — Automação, qualidade e integração |
| S9 | [Depuração sistemática](sessao-09-depuracao-sistematica/index.md) | 4 — Automação, qualidade e integração |
| S10 | [SDD ciclo completo](sessao-10-sdd-ciclo-completo/index.md) | 4 — Automação, qualidade e integração |

## Critérios de sucesso

Ao final das 20h, cada participante consegue:

- Executar a esteira completa de engenharia agêntica de forma autônoma
- Escrever especificações e planos que um agente consegue seguir
- Formalizar regras de negócio em SBVR com auxílio de IA
- Aplicar TDD com assistência de IA em funcionalidades novas
- Escolher, aplicar e conferir casos de uso de IA do próprio papel, com a fonte de comparação declarada
- Executar um ciclo SDD completo com os modelos de especificação agênticas da Arkhi
- Depurar sistematicamente sem depender de tentativa e erro
- Registrar decisões arquiteturais em ADRs (MADR v4)

## Fora de escopo

Para deixar claro o que este workshop não cobre: treinamento em LLMs (operação de modelos, ajuste fino, infraestrutura), esteiras CI/CD automatizadas e operação de agentes em produção. A criação de skills e de subagentes e a estimativa de custo de tokens são cobertas na Sessão 8.

## Referências

Ver [referencia/bibliografia.md](referencia/bibliografia.md) para as fontes padrão-ouro que embasam cada sessão.

