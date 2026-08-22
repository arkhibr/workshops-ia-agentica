# Conceitos

## Do ambiente individual ao ambiente compartilhado

Um ambiente agêntico é a combinação de quatro peças: o modelo, o harness que orquestra a conversa com ele (Claude Code, Codex CLI, Copilot, Cursor), o arquivo de configuração que carrega convenções do repositório, e o conjunto de ferramentas que o agente pode acionar. Quando cada desenvolvedor monta essa combinação à própria maneira, o time herda exatamente o sintoma "ad hoc" descrito na Sessão 1: nenhum vocabulário compartilhado sobre o que configurar, e o resultado de um prompt na máquina de alguém não se repete na do colega.

A correção não é escolher uma ferramenta única para todo o time. É compartilhar as três peças que independem da ferramenta escolhida: o arquivo de configuração, o protocolo de acesso a ferramentas externas, e a disciplina de isolamento de contexto.

## De prompt engineering para context engineering

A Anthropic, no guia de engenharia "Effective context engineering for AI agents" (setembro de 2025), descreve uma virada de foco: depois de alguns anos em que prompt engineering (encontrar as palavras certas para uma instrução) dominava a atenção, o problema real passou a ser outro: qual configuração de contexto tem mais chance de produzir o comportamento desejado do modelo. Prompt engineering cuida do texto da instrução. Context engineering cuida de tudo que chega à janela de contexto numa execução: instruções, histórico, resultados de ferramentas, arquivos lidos.

O guia é específico sobre o papel das ferramentas nessa mudança: elas são o contrato entre o agente e o espaço de informação e ação disponível, e precisam ser desenhadas para eficiência de token e para induzir comportamento eficiente do agente. Uma ferramenta mal desenhada consome espaço de contexto que poderia ir para informação relevante ao problema, além de ser mais incômoda de usar.

## O problema M×N e o Model Context Protocol

Antes de novembro de 2024, conectar um agente a uma ferramenta externa (um banco de dados, um rastreador de issues, um sistema de arquivos) exigia uma integração específica para aquele par modelo-ferramenta. Com M modelos e N ferramentas, o time enfrentava M×N integrações para manter.

A Anthropic abriu o código do Model Context Protocol (MCP) para resolver exatamente essa conta: um protocolo aberto no qual cada modelo implementa o MCP uma vez, e cada ferramenta ou serviço implementa o MCP uma vez. A multiplicação vira soma. Um ano depois do lançamento, o protocolo já tinha adoção de OpenAI, Google e Microsoft, tornando-se o padrão de fato para conectar agentes a sistemas externos — não porque uma empresa impôs, mas porque resolvia um problema real de manutenção que todo mundo compartilhava.

## Um arquivo de instrução, qualquer ferramenta: AGENTS.md

Se MCP resolve como um agente acessa uma ferramenta, falta resolver como um agente aprende as convenções do repositório em que está trabalhando. Em agosto de 2025, OpenAI, Google, Cursor, Factory e Sourcegraph formalizaram juntos o AGENTS.md: um arquivo markdown simples, na raiz do repositório, sem esquema obrigatório, que qualquer agente de codificação lê para saber como construir, testar e alterar o projeto. Diferente do README, que fala com uma pessoa, o AGENTS.md fala com o agente: comandos de build e teste, convenções de estilo, regras de segurança, formato de commit.

O padrão hoje é mantido pela Agentic AI Foundation, um projeto da Linux Foundation — não pertence a um único fornecedor. Mais de 20 mil repositórios já adotaram o formato, e ferramentas de fornecedores concorrentes (GitHub Copilot, Codex, Cursor, Gemini) leem o mesmo arquivo. O `CLAUDE.md` que este próprio workshop usa para configurar convenções do repositório cumpre esse mesmo papel, num formato específico do Claude Code.

## Isolamento de contexto por ramo

A última peça é operacional: o que acontece quando duas pessoas, ou a mesma pessoa em duas tarefas, usam um agente ao mesmo tempo no mesmo repositório. Sem isolamento, os dois agentes leem e escrevem no mesmo diretório de trabalho — um pode sobrescrever a edição do outro, ou um terminar de ler arquivos que o outro está no meio de alterar.

O git worktree resolve isso na camada de sistema de arquivos, não de configuração de agente: cada worktree é um diretório de trabalho separado, apontando para o mesmo repositório, cada um numa branch diferente. Um agente trabalhando num worktree não vê, e não pode corromper, o que outro agente está fazendo no worktree paralelo. Isso separa dois problemas que costumam ser confundidos: contexto de conversa (o que o agente lembra) e estado do sistema de arquivos (o que existe em disco). O segundo pode ser isolado mesmo quando o primeiro continua específico de cada sessão.

!!! question "Antes de continuar"
    Pense na última vez que dois agentes (ou duas pessoas usando IA) mexeram no mesmo repositório ao mesmo tempo. Alguém percebeu um conflito antes ou depois de acontecer?

## As quatro peças, lado a lado

| Peça | O que resolve | Compartilhado entre ferramentas? |
|---|---|---|
| Arquivo de configuração (AGENTS.md / CLAUDE.md) | O agente conhece as convenções do repositório | Sim — mesmo arquivo, qualquer agente que o leia |
| MCP | O agente acessa uma ferramenta externa sem integração específica | Sim — protocolo aberto, adotado por múltiplos fornecedores |
| Isolamento por ramo (worktree) | Duas sessões não corrompem o trabalho uma da outra | Sim — é uma prática de git, não de uma ferramenta de IA específica |
| Harness (Claude Code, Copilot, Cursor) | Orquestra a conversa entre humano, modelo e ferramentas | Não — cada equipe escolhe o próprio, o método é agnóstico |

!!! question "Antes de continuar"
    Das quatro peças da tabela, qual o seu time já tem hoje? Qual está completamente ausente?

**Próxima página:** [Padrões e decisões](padroes-e-decisoes.md).
