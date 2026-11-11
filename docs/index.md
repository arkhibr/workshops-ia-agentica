# Workshop: IA Agêntica na Prática

Workshop de engenharia agêntica disciplinada para equipes de desenvolvimento C#, JavaScript e TypeScript. As dez sessões conduzem o time do uso ad hoc de LLMs, em que cada desenvolvedor pede código do próprio jeito e sem vocabulário compartilhado, até uma esteira de engenharia em que o agente executa sob especificação e verificação definidas pela equipe.

A tese do workshop parte de uma mudança no modo de programar. Num fluxo agêntico, o comportamento do código gerado depende do que está escrito na janela de contexto do modelo, e o desenvolvedor escreve boa parte desse conteúdo em linguagem natural, que o LLM interpreta e executa. O workshop trata a escrita desse conteúdo como prática de engenharia, composta por especificar o comportamento esperado, decompor o trabalho em tarefas que o agente consegue executar e verificar o resultado contra critérios de aceitação. A IA eleva o resultado mínimo de qualquer desenvolvedor, enquanto chegar à qualidade de produto exige disciplina de método, e por isso o julgamento humano sobre o que especificar e o que aceitar passa a ter mais peso no trabalho da equipe.

**Público:** desenvolvedores C#, JavaScript e TypeScript com experiência intermediária nessas linguagens, que já experimentam IA no dia a dia sem processo formal.

**Formato:** 10 sessões de 2h cada (problema → método → exercício), 20h no total, modalidade online. Cenários genéricos C#/JS/TS alternam com casos de projetos de pesquisa da ACME, uma universidade fictícia, no Bloco 3.

**Cadeia de ferramentas:** o conteúdo metodológico não depende do ambiente. A combinação recomendada é Claude Code com Codex CLI, e o material também funciona com GitHub Copilot em VS Code ou JetBrains e com o Cursor IDE, todos por meio d os comandos `/specify` · `/plan` · `/tasks` do [GitHub Spec Kit](referencia/bibliografia.md).

---

## Agenda

| Bloco | Sessões | Tema | Intenção metodológica |
|---|---|---|---|
| 1 — Fundamentos e ambiente de trabalho com agentes | S1–S2 | Modelo mental do Software 3.0 e primeiro uso da ferramenta | Software 3.0 · Engenharia Agêntica · cadeia de ferramentas e isolamento por ramo |
| 2 — Especificação de requisitos e regras de negócio | S3–S5 | Especificação precisa do comportamento esperado | Requisitos BR/FR/NFR · SBVR + RuleSpeak + tabelas de decisão · caminho básico do Spec Kit, da regra ao código |
| 3 — Testes e uso de IA por papel | S6–S7 | Verificação do código contra o plano e uso de IA por papel | Qualidade da spec e teste antes do código · casos de uso de IA por papel, com mural das equipes e pitch |
| 4 — Skills, agentes e uso nas empresas | S8–S10 | Skills e agentes próprios, governança antes do compartilhamento e fechamento do curso com o horizonte de 2027 | Criação de skills e agentes · governança de skills e agentes · computação agêntica em 2027 e plano de 90 dias |

## Sessões

| # | Sessão | Bloco |
|---|---|---|
| S1 | [Modos de trabalho com IA no desenvolvimento de software](sessao-01-o-que-mudou/index.md) | 1 — Fundamentos e ambiente de trabalho com agentes |
| S2 | [Configuração do ambiente compartilhado de agentes na equipe](sessao-02-ambiente-agentico/index.md) | 1 — Fundamentos e ambiente de trabalho com agentes |
| S3 | [Especificação de requisitos antes de pedir código ao agente](sessao-03-exploracao-especificacao/index.md) | 2 — Especificação de requisitos e regras de negócio |
| S4 | [Regras de negócio escritas em formato verificável com IA](sessao-04-regras-formais-com-ia/index.md) | 2 — Especificação de requisitos e regras de negócio |
| S5 | [Desenvolvimento guiado por especificação com o GitHub Spec Kit](sessao-05-decomposicao/index.md) | 2 — Especificação de requisitos e regras de negócio |
| S6 | [Revisão da especificação e testes escritos antes do código](sessao-06-spec-kit-aprofundado/index.md) | 3 — Testes e uso de IA por papel |
| S7 | [Usos de IA conferíveis em cada papel da equipe](sessao-07-casos-de-uso-por-papel/index.md) | 3 — Testes e uso de IA por papel |
| S8 | [Construção de skills e agentes próprios da equipe](sessao-08-skills-e-agentes/index.md) | 4 — Skills, agentes e uso nas empresas |
| S9 | [Regras para compartilhar skills e agentes entre colegas](sessao-09-governanca-de-skills-e-agentes/index.md) | 4 — Skills, agentes e uso nas empresas |
| S10 | [Uso de agentes nas empresas em 2027 e plano de teste de 90 dias](sessao-10-computacao-agentica-2027/index.md) | 4 — Skills, agentes e uso nas empresas |

## Critérios de sucesso

Ao final das 20h, cada participante consegue:

- Executar a esteira completa de engenharia agêntica de forma autônoma
- Escrever especificações e planos que um agente consegue seguir
- Formalizar regras de negócio em SBVR com auxílio de IA
- Aplicar TDD com assistência de IA em funcionalidades novas
- Escolher, aplicar e conferir casos de uso de IA do próprio papel, com a fonte de comparação declarada
- Executar o caminho do SDD com o GitHub Spec Kit, da constitution ao código com testes passando
- Classificar e governar skills e agentes antes de compartilhá-los
- Classificar afirmações sobre agentes pelo tipo de evidência e propor um piloto de 90 dias medido por custo por resultado aceito

## Fora de escopo

O workshop não cobre treinamento em LLMs (operação de modelos, ajuste fino, infraestrutura), esteiras CI/CD automatizadas e operação de agentes em produção. A criação de skills e de subagentes e a estimativa de custo de tokens são cobertas na Sessão 8.

## Referências

Ver [referencia/bibliografia.md](referencia/bibliografia.md) para as fontes padrão-ouro que embasam cada sessão.

