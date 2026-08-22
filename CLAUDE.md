# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Propósito

Workshop de engenharia agêntica disciplinada para a equipe de desenvolvimento C#, JavaScript e TypeScript da FUNDEP: 10 sessões de 2h (20h no total), organizadas em 4 blocos.

- **Bloco 1 (S1–S2):** Fundamentos — Software 3.0, Engenharia Agêntica, ambiente agêntico
- **Bloco 2 (S3–S5):** Especificação e Planejamento — requisitos BR/FR/NFR, SBVR + RuleSpeak, decomposição em planos
- **Bloco 3 (S6–S8):** Execução — TDD assistido, testes de propriedade/mutação/contrato, SDD ponta a ponta com GitHub Spec Kit
- **Bloco 4 (S9–S10):** Qualidade e Integração — depuração sistemática, esteira completa com ADR

Baseado no GitHub Spec Kit (Spec-Driven Development), OMG SBVR + RuleSpeak (Ronald G. Ross), MADR v4, xUnit Test Patterns (Meszaros) e testes de propriedade/mutação (fast-check, FsCheck, Stryker). Ver [referencia/bibliografia.md](referencia/bibliografia.md).

## Estrutura e arquitetura

```
sessao-01-o-que-mudou/                  # Bloco 1: modelo mental Software 3.0
sessao-02-ambiente-agentico/            # Bloco 1: cadeia de ferramentas, fluxos, isolamento por ramo
sessao-03-exploracao-especificacao/     # Bloco 2: requisitos BR/FR/NFR
sessao-04-regras-formais-com-ia/        # Bloco 2: SBVR, RuleSpeak, tabelas de decisão
sessao-05-decomposicao/                 # Bloco 2: planos executáveis para SDD
sessao-06-tdd-assistido/                # Bloco 3: TDD com LLM, xUnit (C#) e Jest (JS/TS)
sessao-07-estrategias-avancadas-teste/  # Bloco 3: propriedade, mutação, contrato
sessao-08-sdd-ciclo-completo/           # Bloco 3: GitHub Spec Kit — constitution/spec/plan/tasks
sessao-09-depuracao-sistematica/        # Bloco 4: hipótese → investigação → correção → verificação
sessao-10-esteira-completa/             # Bloco 4: esteira ponta a ponta + ADR (MADR v4)
```

Cada sessão é autocontida e cobre o material completo de um encontro de 2h. O formato foi validado na Sessão 1 e se repete nas demais:

```
sessao-NN-slug/
├── README.md              # agenda em blocos teoria+prática cronometrados, teoria de cada bloco inline, links para os exercícios
└── exercicios/
    ├── exercicio-NN-slug.md              # exercício simples, autocontido no próprio arquivo
    └── exercicio-NN-slug/                # exercício com múltiplos arquivos (cenário, critérios de aceitação)
        ├── README.md
        ├── cenario.md
        └── criterios-aceitacao.md
```

**Teoria e prática intercaladas, nunca em bloco único.** Uma sessão de 2h não é uma hora de aula seguida de meia hora de exercício — é dividida em 3–5 blocos de 20–35 min, cada um com teoria curta (10–15 min) seguida de prática imediata (10–20 min) sobre o que acabou de ser apresentado. O último bloco de cada sessão é o exercício-âncora, mais longo, que integra os blocos anteriores.

## Convenções críticas

**Sem par ruim/bom.** Este não é um workshop de refatoração de código — é um workshop de método com IA. O exercício típico é rodar um fluxo com o agente (especificar, planejar, testar, depurar) e comparar contra um critério de aceitação, não comparar uma versão "ruim" e uma "boa" do mesmo código.

**Linguagens: apenas C# e JavaScript/TypeScript.** Sem PHP, Python ou ADVPL/TLPP — esse é o stack real da equipe FUNDEP. Testes de unidade em xUnit (C#) e Jest (JS/TS); testes de propriedade em FsCheck (C#) e fast-check (JS/TS); mutação em Stryker (ambos, via Stryker.NET e StrykerJS).

**Domínio FUNDEP como variação, não como base.** Cenários genéricos de C#/JS/TS carregam a sessão; variações no domínio FUNDEP (bolsas, projetos, prestação de contas) aparecem como exercício adicional nos Blocos 3 e 4, não substituem o cenário genérico.

**Cadeia de ferramentas agnóstica.** O conteúdo metodológico não depende de uma ferramenta específica — todas passam pelos comandos `/specify` · `/plan` · `/tasks` do GitHub Spec Kit. Recomendado Claude Code + Codex CLI; alternativas: GitHub Copilot + VS Code/JetBrains, Cursor IDE.

**Escrita dos READMEs:** conceito antes da ferramenta, sem cacoetes de IA (aberturas dramáticas, "não apenas... mas também", conclusões retóricas), tom direto e factual, com fragmentos de código e links relativos aos arquivos.

**Convenções de commit:** `<type>: <mensagem>` — tipos usados: `feat`, `docs`, `refactor`, `fix`.
