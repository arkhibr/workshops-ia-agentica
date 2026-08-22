# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Propósito

Workshop de engenharia agêntica disciplinada para a equipe de desenvolvimento C#, JavaScript e TypeScript da FUNDEP: 10 sessões de 2h (20h no total), organizadas em 4 blocos.

- **Bloco 1 (S1–S2):** Fundamentos — Software 3.0, Engenharia Agêntica, ambiente agêntico
- **Bloco 2 (S3–S5):** Especificação e Planejamento — requisitos BR/FR/NFR, SBVR + RuleSpeak, decomposição em planos
- **Bloco 3 (S6–S8):** Execução — TDD assistido, testes de propriedade/mutação/contrato, SDD ponta a ponta com GitHub Spec Kit
- **Bloco 4 (S9–S10):** Qualidade e Integração — depuração sistemática, esteira completa com ADR

Baseado no GitHub Spec Kit (Spec-Driven Development), OMG SBVR + RuleSpeak (Ronald G. Ross), MADR v4, xUnit Test Patterns (Meszaros) e testes de propriedade/mutação (fast-check, FsCheck, Stryker). Ver [docs/referencia/bibliografia.md](docs/referencia/bibliografia.md).

**Horário fixo: todas as sessões vão das 14h às 16h.** Não é provisório — use este horário em qualquer plano de aula ou material que faça referência a hora do relógio, sem ressalva de "a confirmar".

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

Cada sessão é autocontida e cobre o material completo de um encontro de 2h. O formato foi validado na Sessão 1 e se repete nas demais — mesmo esqueleto de 8 páginas das disciplinas de pós-graduação da Arkhi (`arquitetura-solucoes-ia-generativa/docs/modulo-N/`), com profundidade calibrada para 2h ao vivo, não para um módulo de leitura de 60–90 min:

```
docs/sessao-NN-slug/
├── index.md                    # pergunta-guia, objetivos Bloom, roteiro cronometrado com link para cada página
├── conceitos.md                # teoria fundamentada — o que o instrutor explora ao vivo
├── padroes-e-decisoes.md       # comparação de abordagens, critério de decisão, anti-padrão
├── exemplo-arquitetural.md     # demonstração conduzida pelo instrutor, com o caso Vetor
├── estudo-de-caso.md           # dilema sem resposta prescrita, perguntas para orientar a discussão
├── oficina-de-ferramentas.md   # prática guiada em experimentos, com roteiro sugerido de condução no topo da página
├── exercicios.md               # exercícios em 6 níveis de Bloom (Recordar → Criar), com rubrica no nível Aplicar
└── sintese-e-referencias.md    # ideias essenciais, checklist, autoavaliação, fontes completas
```

`index.md` é o nome obrigatório (não `README.md`) — é o que o mkdocs usa como página de entrada de cada pasta. Todas as 8 páginas de uma sessão entram no `nav:` do `mkdocs.yml`, aninhadas sob o título da sessão (ver S1 como referência).

**Estas páginas não são leitura prévia do aluno.** Diferente do `arquitetura-solucoes-ia-generativa`, ninguém lê 60–90 minutos antes da sessão. O instrutor conduz a exploração dos conceitos e o trabalho dos exercícios ao vivo, durante as 2h — a estrutura em 8 páginas organiza o material de apoio do instrutor, não uma tarefa de casa. Cada `index.md` declara isso explicitamente em "Como usar este material".

**Caso contínuo: Vetor.** Uma plataforma fictícia de e-commerce B2B (clientes padrão e atacado) atravessa as dez sessões como fio condutor de exemplos e exercícios, equivalente aos casos Horizonte/Aurora/Lume do `arquitetura-solucoes-ia-generativa`. Cenários genéricos de C#/JS/TS usam a Vetor; variações no domínio FUNDEP continuam restritas aos Blocos 3 e 4, como exercício adicional.

**O caso aplicado fica fora de `conceitos.md` e `padroes-e-decisoes.md`.** Essas duas páginas ficam em nível conceitual — framework, tabela de critérios, evidência empírica, princípio geral. A Vetor (ou qualquer cenário concreto) só entra em `exemplo-arquitetural.md`, `estudo-de-caso.md`, `oficina-de-ferramentas.md` e `exercicios.md`. Um framework teórico seguido de repente por "a Vetor precisa de..." é uma quebra de nível que o participante não tem como acompanhar — o exemplo cabe na página feita para exemplo.

**Toda página é autocontida — sem exceção.** O `nav:` do mkdocs lista as 8 páginas de cada sessão lado a lado; o participante pode abrir qualquer uma diretamente, sem ter lido as anteriores. Por isso, a primeira vez que uma página usa a Vetor (ou qualquer termo específico do workshop definido em outra página, mesmo que já definido no `index.md` da sessão), ela recebe uma frase curta de contexto — "a Vetor, plataforma fictícia de e-commerce B2B usada nesta sessão" — antes de assumir que o leitor já sabe do que se trata.

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
- Toda citação em prosa tem par na seção "Fundamentação" de `sintese-e-referencias.md` e entrada completa em `docs/referencia/bibliografia.md` (autor, título, veículo, data, URL).

**Todo comando de terminal em exercício ou oficina funciona em Windows, macOS e Linux.** A equipe FUNDEP usa as três plataformas. Nunca publicar um comando que só roda num shell POSIX (`mkdir -p`, `~`, `printf`, redirecionamento `2>&1` específico de bash) sem equivalente para Windows. Quando os comandos divergem entre sistemas, usar blocos `=== "macOS/Linux"` / `=== "Windows (PowerShell)"` (`pymdownx.tabbed`, `alternate_style: true`, já habilitado em `mkdocs.yml`) — nunca aninhar esses blocos dentro de um item de lista numerada (`1.`, `2.`), porque o Python-Markdown quebra o parsing; usar rótulo em negrito (`**Passo N:** texto`) para numerar passos que precisem de blocos `===` logo abaixo. Quando o comando já é multiplataforma por natureza (git, npm, npx, dotnet), não precisa de duas versões. Qual experimento é essencial em aula, exploração em dupla ou extensão opcional aparece uma única vez, na seção "Roteiro sugerido para a sessão" no topo de `oficina-de-ferramentas.md` — não repetir como rótulo `**Classificação:**` sob cada `## Experimento`.

**Convenções de commit:** `<type>: <mensagem>` — tipos usados: `feat`, `docs`, `refactor`, `fix`.
