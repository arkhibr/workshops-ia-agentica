# Workshop: IA Agêntica na Prática

Workshop de engenharia agêntica disciplinada para a equipe de desenvolvimento C#, JavaScript e TypeScript da FUNDEP. Dez sessões que levam o time do uso ad hoc de LLMs (cada desenvolvedor com seu próprio jeito de pedir código, sem vocabulário ou contrato compartilhado) a uma esteira de engenharia com IA como parceiro de execução controlado e saídas previsíveis.

A tese: a janela de contexto virou o programa. O LLM é o interpretador; o desenvolvedor escreve em linguagem natural, e o que era arte ou intuição agora é engenharia — especificação, decomposição, verificação. O piso sobe para todos; o teto sobe só com disciplina; o julgamento humano sobe de valor.

**Público:** desenvolvedores C#, JavaScript e TypeScript com experiência intermediária na stack, que já experimentam IA no dia a dia sem processo formal.

**Formato:** 10 sessões de 2h cada (problema → método → exercício), 20h no total, modalidade online. Cenários genéricos C#/JS/TS alternam com variações no domínio FUNDEP nos Blocos 3 e 4.

**Cadeia de ferramentas:** conteúdo metodológico agnóstico ao ambiente. Recomendado Claude Code + Codex CLI; também compatível com GitHub Copilot + VS Code/JetBrains e Cursor IDE, todos via os comandos `/specify` · `/plan` · `/tasks` do [GitHub Spec Kit](referencia/bibliografia.md).

---

## Agenda

| Bloco | Sessões | Tema | Intenção metodológica |
|---|---|---|---|
| 1 — Fundamentos | S1–S2 | O novo modelo mental, a primeira ferramenta nas mãos | Software 3.0 · Engenharia Agêntica · cadeia de ferramentas e isolamento por ramo |
| 2 — Especificação e Planejamento | S3–S5 | A habilidade mais valiosa da era agêntica: dizer o quê com precisão | Requisitos BR/FR/NFR · SBVR + RuleSpeak + tabelas de decisão · planos executáveis para SDD |
| 3 — Execução | S6–S8 | Do plano ao código, com testes na frente e Spec Kit como esteira | TDD assistido · testes de propriedade/mutação/contrato · SDD ponta a ponta |
| 4 — Qualidade e Integração | S9–S10 | O fechamento da esteira: depuração com método e decisões registradas | Depuração sistemática · esteira completa com ADR (MADR v4) |

## Sessões

| # | Sessão | Bloco |
|---|---|---|
| S1 | [O que mudou: Software 3.0 e Engenharia Agêntica](sessao-01-o-que-mudou/index.md) | 1 — Fundamentos |
| S2 | [O ambiente agêntico — ferramentas e fluxo](sessao-02-ambiente-agentico/index.md) | 1 — Fundamentos |
| S3 | [Exploração e especificação](sessao-03-exploracao-especificacao/index.md) | 2 — Especificação e Planejamento |
| S4 | [Regras formais com IA](sessao-04-regras-formais-com-ia/index.md) | 2 — Especificação e Planejamento |
| S5 | [Decomposição — planos para SDD](sessao-05-decomposicao/index.md) | 2 — Especificação e Planejamento |
| S6 | [TDD assistido por IA](sessao-06-tdd-assistido/index.md) | 3 — Execução |
| S7 | [Estratégias avançadas de teste](sessao-07-estrategias-avancadas-teste/index.md) | 3 — Execução |
| S8 | [SDD — ciclo completo](sessao-08-sdd-ciclo-completo/index.md) | 3 — Execução |
| S9 | [Depuração sistemática e revisão de código](sessao-09-depuracao-sistematica/index.md) | 4 — Qualidade e Integração |
| S10 | [Esteira completa e decisões arquiteturais](sessao-10-esteira-completa/index.md) | 4 — Qualidade e Integração |

## Critérios de sucesso

Ao final das 20h, cada participante consegue:

- Executar a esteira completa de engenharia agêntica de forma autônoma
- Escrever especificações e planos que um agente consegue seguir
- Formalizar regras de negócio em SBVR com auxílio de IA
- Aplicar TDD com assistência de IA em funcionalidades novas
- Definir estratégia de teste por risco — propriedade, mutação, contrato
- Executar um ciclo SDD completo com os modelos de especificação agênticas da Arkhi
- Depurar sistematicamente sem depender de tentativa e erro
- Registrar decisões arquiteturais em ADRs (MADR v4)

## Fora de escopo

Para deixar claro o que este workshop não cobre: treinamento em LLMs (operação de modelos, ajuste fino, infraestrutura), agentes customizados além do uso dos existentes, esteiras CI/CD automatizadas, gestão de custos de uso de API.

## Referências

Ver [referencia/bibliografia.md](referencia/bibliografia.md) para as fontes padrão-ouro que embasam cada sessão.

---

*Baseado na proposta comercial Arkhi `OS2025-05-RR1-Proposta_FUNDEP_-_Workshops_de_IA_Agentica`, aprovada por André, aguardando aceite comercial.*
