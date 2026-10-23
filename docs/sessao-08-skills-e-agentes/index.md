# S8 — Skills e agentes

**Bloco:** 4 — Automação, qualidade e integração

> **Pergunta-guia:** o que uma skill ou um agente precisa declarar antes de ser construído para que o custo, a segurança e o resultado possam ser conferidos depois?

## Problema

As sessões anteriores usaram o agente como ferramenta de uso individual. A partir desta sessão, a equipe passa a construir as próprias ferramentas: skills que ensinam o agente a executar uma tarefa recorrente do mesmo modo e agentes que recebem uma parte do trabalho com contexto, modelo e permissões próprios. Quando essa construção é feita por tentativa e erro, o custo de tokens aparece só na fatura, o modelo é escolhido por hábito, o desempenho é medido pela impressão de quem usa, e as credenciais e as permissões do agente ficam implícitas.

## A ficha de requisitos

A resposta à pergunta-guia é uma ficha de requisitos, uma tabela com uma linha para cada decisão que a skill ou o agente declara antes da construção. Cada página de teoria preenche uma ou duas linhas e termina com o bloco "Linha da ficha", que lista as perguntas daquela linha, e o exercício-âncora preenche a ficha inteira para o artefato da própria equipe.

![A ficha de requisitos do agente, com oito linhas: mecanismo, arquivo e front-matter, artefato e conferência, modelo e esforço, orçamento de tokens, tempo, ferramentas e permissões, e identidade, credencial e cofre. Cada linha traz a pergunta que responde e a página que a preenche.](assets/ficha-de-requisitos.png)

A ficha existe para que as decisões fiquem escritas antes do primeiro teste. Uma skill criada sem ela costuma esconder escolhas que só aparecem depois, como o modelo herdado da conversa, a ferramenta que o subagente herda sem que ninguém a tenha escolhido ou a credencial pessoal que o agente passa a usar.

## Mapa da sessão

A sessão percorre a ficha na ordem das linhas e usa o relógio fixo de 10h às 12h. A primeira hora apresenta o mecanismo, o arquivo, o artefato, o modelo, o custo e o tempo, e fecha com a oficina em que cada pessoa cria e mede uma skill. A segunda parte trata de segurança e credenciais e dedica a maior parte do tempo ao exercício-âncora, em que a equipe preenche a ficha inteira.

![Linha do tempo de 10h às 12h com um bloco para cada página da sessão, proporcional ao tempo recomendado: visão geral, skills, agentes e subagentes, geração de artefatos, escolha de modelos, custo de tokens e performance, oficina até as 11h, intervalo de cinco minutos, segurança e credenciais, exercício-âncora com construção e conferência cruzada, e síntese.](assets/mapa-da-sessao.png)

| Página | Linha da ficha que preenche |
|---|---|
| [Skills](skills.md) | Arquivo e front-matter da skill |
| [Agentes e subagentes](agentes-e-subagentes.md) | Mecanismo, e arquivo e front-matter do subagente |
| [Geração de artefatos](geracao-de-artefatos.md) | Artefato e conferência |
| [Escolha de modelos](escolha-de-modelos.md) | Modelo e esforço |
| [Custo de tokens](custo-de-tokens.md) | Orçamento de tokens |
| [Performance](performance.md) | Tempo |
| [Segurança e credenciais](seguranca-e-credenciais.md) | Ferramentas e permissões, e identidade, credencial e cofre |
| [Oficina de ferramentas](oficina-de-ferramentas.md) | Verificação das linhas anteriores por medição e por teste |
| [Exercícios](exercicios.md) | A ficha completa, no exercício-âncora |

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo, sem leitura prévia obrigatória. Cada página tem um tempo recomendado no roteiro abaixo, e o instrutor explica o que couber nesse tempo, com a coluna "O que explicar nesse tempo" como guia e a coluna "Fica para leitura posterior" como a parte que a turma consulta depois. A sessão pressupõe o ambiente configurado nas Sessões 1 e 2 e o uso do Claude Code, e as notas "Claude Code e Codex CLI" das páginas indicam o equivalente no Codex CLI quando a documentação o descreve.

!!! info "Versões verificadas"
    A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`. As observações foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e o comando `codex doctor` informa a versão 0.164.0 como disponível. O modelo padrão da conta exigiu uma versão mais nova do Codex e os demais modelos do catálogo foram recusados com conta ChatGPT, de modo que nenhum agente do Codex foi executado e as linhas de subagente do Codex têm o status documentado.

As páginas marcam cada afirmação de comportamento como observada, quando foi executada nas versões acima, documentada, quando vem da página oficial lida sem execução, ou não confirmada, quando a documentação lida não cobre o item. Os números citados nas páginas de teoria vêm das fontes listadas na [bibliografia do curso](../referencia/bibliografia.md), que descrevem o comportamento documentado pela Anthropic, pela OpenAI e pela especificação aberta Agent Skills. Nomes de modelos, preços e limites mudam com frequência, e a equipe confere a documentação vigente antes de decidir, a partir do estado documentado em 22/10/2026 para as páginas originais e em 23/10/2026 para o front-matter e o Codex CLI.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** skill, subagente, skill com fork, hook e arquivo de instrução e escolher o mecanismo adequado a uma tarefa.
2. **Escrever** o front-matter e o corpo de uma skill e o arquivo de um subagente, com campos e valores válidos, e diagnosticar o arquivo que falha em silêncio.
3. **Declarar** os requisitos funcionais e não funcionais de uma skill ou de um agente na ficha: artefato produzido, modelo, orçamento de tokens, tempo, permissões e credenciais.
4. **Estimar** o efeito do cache de prompt e da escolha do modelo sobre o custo de uma tarefa repetida.
5. **Aplicar** os cuidados com credenciais: identidade própria do agente, token com escopo mínimo e validade curta, armazenamento fora do repositório e rodízio.
6. **Conferir** o artefato gerado por um agente por meio de script e de critérios declarados antes da construção.
7. **Localizar** o equivalente de um recurso do Claude Code no Codex CLI e reconhecer quando não há equivalente documentado.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | O que explicar nesse tempo | Fica para leitura posterior |
|---|---|---|---|---|---|
| 0 | Visão geral | Abertura | 4 min | Pergunta-guia, ficha de requisitos e mapa da sessão | Objetivos e como conduzir |
| 1 | [Skills](skills.md) | Teoria | 10 min | Três níveis de carga, núcleo portátil, `description` como gatilho e custo, `allowed-tools` libera e não restringe | Campos menos usados, substituições e injeção de comando, diagnóstico da skill que não aciona |
| 2 | [Agentes e subagentes](agentes-e-subagentes.md) | Teoria | 12 min | Contexto isolado, `tools` omitido herda tudo e o erro de grafia, árvore de decisão, custo de vários agentes | Campos que faltam, `permissionMode` e precedência de escopo |
| 3 | [Geração de artefatos](geracao-de-artefatos.md) | Teoria | 5 min | Duas camadas de conferência e o laço de correção | Documentos prontos |
| 4 | [Escolha de modelos](escolha-de-modelos.md) | Teoria | 4 min | Quatro critérios, estratégias de partida e esforço | Matriz por modelo |
| 5 | [Custo de tokens](custo-de-tokens.md) | Teoria | 5 min | De onde o custo vem, cache em unidades relativas e orçamento da listagem | Alavancas de redução em detalhe |
| 6 | [Performance](performance.md) | Teoria | 3 min | Três medidas que se compensam | Reprodutibilidade |
| 7 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 17 min | Experimento A em 10 minutos e Experimento B em 7 minutos | Experimentos C a F |
| | Intervalo | Pausa | 5 min | | |
| 8 | [Segurança e credenciais](seguranca-e-credenciais.md) | Teoria | 10 min | Quatro pontos de entrada, permissões mínimas e restrição em camadas, identidade própria e ciclo do token | Perguntas de revisão em detalhe |
| 9 | [Exercícios](exercicios.md) | Prática avaliada | 34 min | Exercício-âncora: ficha, construção, execução com verificação da restrição e decisão | Exercícios 1 a 11 |
| 10 | [Exercícios](exercicios.md) | Conferência cruzada | 6 min | Troca do arquivo do subagente e do plano da credencial entre equipes | |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist e autoavaliação | Fundamentação e referência rápida |
| | | | **120 min** | | |
| + | [Escolher o mecanismo](escolher-o-mecanismo.md) | Aprofundamento | Fora do relógio | Critério entre skill, subagente, skill com fork, hook, MCP e arquivo de instrução | |
| + | [Front-matter de skills](front-matter-de-skills.md) | Aprofundamento | Fora do relógio | Campos do `SKILL.md`, núcleo portátil, custo da `description` e substituições no corpo | |
| + | [Front-matter de subagentes](front-matter-de-subagentes.md) | Aprofundamento | Fora do relógio | Campos que faltam, `permissionMode`, resolução do `model` e precedência de escopo | |
| + | [Depuração de skills e agentes](depuracao-de-skills-e-agentes.md) | Aprofundamento | Fora do relógio | Falhas silenciosas, o que foi carregado, log de depuração e validação da pasta | |
| + | [Claude Code e Codex CLI](claude-code-e-codex.md) | Aprofundamento | Fora do relógio | Tabela de equivalência com status de evidência e a restrição de ferramentas em camadas | |

O conteúdo soma 115 minutos, e o intervalo das 11h00 às 11h05 completa os 120 minutos de relógio. A primeira parte ocupa das 10h00 às 11h00, com 60 minutos, e a segunda, das 11h05 às 12h00, com 55 minutos.

Se faltar tempo, o corte recomendado é resumir a página de Performance a uma frase com a figura, depois reduzir pela metade a de Escolha de modelos. O Experimento A da oficina, o exercício-âncora e a página de Segurança e credenciais ficam fora de qualquer corte.

## Como conduzir

Cada página de teoria apresenta um tema, termina com o bloco "Linha da ficha" e traz tabelas de decisão que a oficina e os exercícios reutilizam. O instrutor apresenta o tema no tempo recomendado e não percorre as tabelas linha a linha, porque elas ficam à disposição da turma durante a prática.

A oficina e o exercício-âncora usam o mesmo exemplo, a skill `registrando-decisao-arquitetural`, que gera um registro de decisão arquitetural em Markdown para a ACME, uma universidade fictícia. O exemplo foi escolhido porque o artefato tem estrutura verificável por script e conteúdo que só uma pessoa confere, o que permite discutir as duas formas de conferência.

As equipes são formadas antes da sessão. Cada pessoa executa a oficina no próprio computador, numa pasta vazia, e nenhuma credencial real é usada: os exercícios de segurança trabalham com descrições e com tokens fictícios.

!!! warning "Limite desta sessão"
    Os números de custo, de ganho de desempenho e de consumo de tokens vêm de documentação e de relatos da própria Anthropic, medidos em tarefas e configurações específicas. Nenhum deles mede as tarefas da equipe. A decisão de adotar uma skill ou um agente depende da medição feita na oficina e no exercício, com as tarefas e os modelos da própria equipe.

**Próxima página:** [Skills](skills.md).
