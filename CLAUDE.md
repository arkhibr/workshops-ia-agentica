# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Propósito

Workshop de engenharia agêntica disciplinada para a equipe de desenvolvimento C#, JavaScript e TypeScript da FUNDEP: 10 sessões de 2h (20h no total), organizadas em 4 blocos.

- **Bloco 1 (S1–S2):** Fundamentos — Software 3.0, Engenharia Agêntica, ambiente agêntico
- **Bloco 2 (S3–S5):** Especificação e Planejamento — requisitos BR/FR/NFR, SBVR + RuleSpeak, decomposição em planos
- **Bloco 3 (S6–S8):** Execução — TDD assistido, testes de propriedade/mutação/contrato, SDD ponta a ponta com GitHub Spec Kit
- **Bloco 4 (S9–S10):** Qualidade e Integração — depuração sistemática, esteira completa com ADR

Baseado no GitHub Spec Kit (Spec-Driven Development), OMG SBVR + RuleSpeak (Ronald G. Ross), MADR v4, xUnit Test Patterns (Meszaros) e testes de propriedade/mutação (fast-check, FsCheck, Stryker). Ver [docs/referencia/bibliografia.md](docs/referencia/bibliografia.md).

## Publicação (mkdocs)

O site é publicado com Material for MkDocs. Todo o conteúdo do participante vive em `docs/`; a raiz do repositório só tem infraestrutura (`mkdocs.yml`, `requirements.txt`, `CLAUDE.md`).

```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve            # prévia local em http://127.0.0.1:8000
mkdocs build --strict   # valida nav e links antes de commitar — deve terminar em exit 0
```

`site/` e `.venv/` são gerados e estão no `.gitignore` — nunca commitar.

## Estrutura e arquitetura

```
docs/
├── index.md                                  # visão geral, agenda, critérios de sucesso
├── referencia/bibliografia.md                # fontes padrão-ouro
├── sessao-01-o-que-mudou/                    # Bloco 1: modelo mental Software 3.0
├── sessao-02-ambiente-agentico/              # Bloco 1: cadeia de ferramentas, fluxos, isolamento por ramo
├── sessao-03-exploracao-especificacao/       # Bloco 2: requisitos BR/FR/NFR
├── sessao-04-regras-formais-com-ia/          # Bloco 2: SBVR, RuleSpeak, tabelas de decisão
├── sessao-05-decomposicao/                   # Bloco 2: planos executáveis para SDD
├── sessao-06-tdd-assistido/                  # Bloco 3: TDD com LLM, xUnit (C#) e Jest (JS/TS)
├── sessao-07-estrategias-avancadas-teste/    # Bloco 3: propriedade, mutação, contrato
├── sessao-08-sdd-ciclo-completo/             # Bloco 3: GitHub Spec Kit — constitution/spec/plan/tasks
├── sessao-09-depuracao-sistematica/          # Bloco 4: hipótese → investigação → correção → verificação
└── sessao-10-esteira-completa/               # Bloco 4: esteira ponta a ponta + ADR (MADR v4)
```

Cada sessão é autocontida e cobre o material completo de um encontro de 2h. O formato foi validado na Sessão 1 e se repete nas demais:

```
docs/sessao-NN-slug/
├── index.md                # agenda em blocos teoria+prática cronometrados, teoria de cada bloco inline, links para os exercícios
└── exercicios/
    ├── exercicio-NN-slug.md              # exercício simples, autocontido no próprio arquivo
    └── exercicio-NN-slug/                # exercício com múltiplos arquivos (cenário, critérios de aceitação)
        ├── index.md
        ├── cenario.md
        └── criterios-aceitacao.md
```

`index.md` é o nome obrigatório (não `README.md`) — é o que o mkdocs usa como página de entrada de cada pasta. Nem toda página de exercício precisa estar em `nav:` no `mkdocs.yml`; exercícios de apoio ficam acessíveis por link a partir do `index.md` da sessão, sem poluir o menu principal.

**Teoria e prática intercaladas, nunca em bloco único.** Uma sessão de 2h não é uma hora de aula seguida de meia hora de exercício — é dividida em 3–5 blocos de 20–35 min, cada um com teoria curta (10–15 min) seguida de prática imediata (10–20 min) sobre o que acabou de ser apresentado. O último bloco de cada sessão é o exercício-âncora, mais longo, que integra os blocos anteriores.

## Convenções críticas

**Sem par ruim/bom.** Este não é um workshop de refatoração de código — é um workshop de método com IA. O exercício típico é rodar um fluxo com o agente (especificar, planejar, testar, depurar) e comparar contra um critério de aceitação, não comparar uma versão "ruim" e uma "boa" do mesmo código.

**Linguagens: apenas C# e JavaScript/TypeScript.** Sem PHP, Python ou ADVPL/TLPP — esse é o stack real da equipe FUNDEP. Testes de unidade em xUnit (C#) e Jest (JS/TS); testes de propriedade em FsCheck (C#) e fast-check (JS/TS); mutação em Stryker (ambos, via Stryker.NET e StrykerJS).

**Domínio FUNDEP como variação, não como base.** Cenários genéricos de C#/JS/TS carregam a sessão; variações no domínio FUNDEP (bolsas, projetos, prestação de contas) aparecem como exercício adicional nos Blocos 3 e 4, não substituem o cenário genérico.

**Cadeia de ferramentas agnóstica.** O conteúdo metodológico não depende de uma ferramenta específica — todas passam pelos comandos `/specify` · `/plan` · `/tasks` do GitHub Spec Kit. Recomendado Claude Code + Codex CLI; alternativas: GitHub Copilot + VS Code/JetBrains, Cursor IDE.

**Escrita dos READMEs:** conceito antes da ferramenta, tom direto e factual, com fragmentos de código e links relativos aos arquivos.

**Revisão anti-cacoetes obrigatória, sem exceção.** Toda saída de conteúdo (teoria, exercício, README) passa pelo SOP anti-cacoetes-llm do PKA (repositório separado — `system/bkm/sops/anti-cacoetes-llm.md` em `Dropbox/Pessoal/pka`) antes de ser apresentada ou commitada — primeira versão já sem os 18 marcadores, mais uma passada de autorrevisão separada. As verificações mecânicas dos marcadores 13 (contrastes artificiais/quiasmo) e 18 (travessão, máx. 1 por parágrafo) são obrigatórias, não "de olho": contar `—` por parágrafo e checar toda ocorrência de "não" perto de travessão/dois-pontos antes de considerar o texto pronto. Aplicar o teste de autoria: a escrita parece de alguém que já pagou o preço das próprias opiniões?

**Barra de fundamentação: nível pós-graduação, não paráfrase de proposta comercial.** A teoria de cada sessão usa como referência de rigor as disciplinas de pós-graduação do Marco (ver `arquitetura-solucoes-ia-generativa`, especialmente `docs/modulo-1-fundamentos/sintese-e-referencias.md` e `docs/modulo-4-agentes/`). Isso significa:
- Fundamentar em pesquisa primária quando ela existe — artigos (arXiv, NeurIPS, ACL), especificações técnicas (Model Context Protocol, GitHub Spec Kit), padrões de organismos (NIST, OWASP) — não só posts de blog ou talks de conferência.
- Fontes de prática de mercado (Karpathy, Willison, blog do GitHub) são legítimas para nomear fenômenos recentes sem literatura acadêmica ainda, mas complementam a base primária — não a substituem.
- Reaproveitar frameworks já validados nas disciplinas da Arkhi em vez de reinventar categorias novas — ex.: a distinção vibe coding / assistência de codificação / SDD do Módulo 4 (Agentes) é a referência para qualquer sessão que toque nesse tema, não uma dicotomia "ad hoc vs. disciplinado" inventada para o workshop.
- Toda citação em prosa tem par na seção "Fontes desta sessão" (no `index.md`) e entrada completa em `docs/referencia/bibliografia.md` (autor, título, veículo, data, URL).

**Convenções de commit:** `<type>: <mensagem>` — tipos usados: `feat`, `docs`, `refactor`, `fix`.
