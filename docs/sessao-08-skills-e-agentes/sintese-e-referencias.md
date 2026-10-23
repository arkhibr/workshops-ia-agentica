# Síntese e referências

## Dez ideias essenciais

1. **A ficha de requisitos declara as decisões antes da construção.** Cada linha da ficha, do mecanismo ao cofre da credencial, pertence a uma página e é verificada na oficina e no exercício-âncora, de modo que o custo, a segurança e o resultado possam ser conferidos depois, como descreve a [visão geral](index.md#a-ficha-de-requisitos).
2. **Uma skill carrega em três níveis.** Os metadados custam cerca de 100 tokens por skill e ficam sempre no contexto, o corpo do `SKILL.md` carrega quando a skill é acionada e fica abaixo de 5 mil tokens, e os recursos e scripts carregam sob demanda, conforme a [documentação das skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao).
3. **O front-matter falha em silêncio, e `allowed-tools` libera sem restringir.** O Claude Code ignora sem erro o campo que não reconhece, de modo que `tool` no lugar de `tools` deixou o subagente editar o arquivo, e o log de depuração e o comando `/context` mostram o que carregou, segundo a [documentação das skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao) e a [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao).
4. **Um subagente tem contexto, ferramentas e modelo próprios.** O isolamento mantém a saída volumosa fora da conversa principal, e o campo `tools` omitido faz o subagente herdar todas as ferramentas, de acordo com a [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao).
5. **Vários agentes só compensam em tarefas amplas e paralelizáveis.** O [relato da Anthropic](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) cita cerca de 4 vezes os tokens de um chat para um agente e cerca de 15 vezes para vários agentes, e aponta a maioria das tarefas de programação como mau encaixe.
6. **O artefato tem duas camadas de conferência.** O script verifica a estrutura, e a pessoa nomeada verifica o conteúdo que o script não decide, com o plano, a validação e a execução como padrão para operações em lote, segundo as [boas práticas de skills](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao).
7. **O modelo certo é o menor que passa nas avaliações da própria equipe.** O [guia de escolha](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) oferece duas estratégias de partida, com Haiku 5.5 ou Opus 5.5, e aponta o esforço como alavanca dentro de um mesmo modelo.
8. **O custo se declara antes e se mede depois.** A leitura do cache custa 0,1 do preço-base na maioria dos modelos, conforme a [documentação do cache](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao), e o [guia de custo](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) mostra o consumo com `/usage`.
9. **Desempenho tem três medidas que se compensam.** Tempo, tokens e taxa de acerto precisam ser registrados juntos, e o relato multiagente recomenda começar com cerca de 20 consultas reais.
10. **O agente usa identidade própria e credencial mínima.** O token tem escopo mínimo, validade curta e local de guarda fora do repositório, e o rodízio segue seis passos, conforme o [Microsoft Learn](../referencia/bibliografia.md#microsoft-use-personal-access-tokens-in-azure-devops-documentacao) e o [GitHub](../referencia/bibliografia.md#github-managing-your-personal-access-tokens-documentacao).

## Checklist antes de encerrar a sessão

- [ ] Cada equipe preencheu a ficha de requisitos inteira antes de construir, incluindo o mecanismo e o front-matter.
- [ ] Cada pessoa criou uma skill, executou e conferiu o artefato nas duas camadas.
- [ ] A tabela de medição da oficina tem os dois modelos preenchidos.
- [ ] O subagente da equipe tem `tools` explícito e justificativa para escrita ou rede, e a restrição foi verificada com um pedido de edição.
- [ ] Nenhuma credencial real foi usada, e o plano de cada equipe indica identidade, escopo, validade e cofre.
- [ ] A conferência cruzada produziu ao menos um achado por equipe.
- [ ] A equipe conferiu o front-matter de cada agente e de cada skill com `/context` e, quando algo não carregou, com o log de `claude --debug`.
- [ ] A equipe registrou, para cada recurso específico do Claude Code que usa, se o Codex CLI tem equivalente documentado.

## Autoavaliação

1. Consigo dizer quando uma tarefa deve ser uma skill, um subagente, uma skill com fork ou o agente principal?
2. Sei estimar, em unidades relativas, o efeito do cache sobre uma tarefa repetida?
3. Sei explicar por que um campo de restrição com erro de grafia pode deixar um subagente com acesso total?
4. Consigo dizer qual identidade o meu agente usa e o que acontece se o token vazar hoje?
5. Sei dizer a diferença entre `allowed-tools`, que libera ferramentas numa skill, e `disallowed-tools`, que as restringe?
6. Sei encontrar, no log de depuração, o motivo de um arquivo de subagente não ter carregado?

Se duas ou mais respostas forem "ainda não", releia [Segurança e credenciais](seguranca-e-credenciais.md) e [Custo de tokens](custo-de-tokens.md) antes da Sessão 9.

## Referência rápida: Claude Code e Codex CLI

Skills e subagentes existem nas duas ferramentas, com nomes, arquivos e campos diferentes, e as tabelas abaixo reúnem a correspondência para quem usa o Codex CLI e lê exemplos escritos para o Claude Code. Cada linha traz um status de evidência: **observado** quando o comportamento foi executado na versão registrada, **documentado** quando a informação foi lida na página oficial sem execução, e **não confirmado** quando a documentação lida não cobre o item ou o resultado não pôde ser verificado.

!!! info "Versões verificadas"
    A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`. As observações foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e o comando `codex doctor` informa a versão 0.164.0 como disponível. O modelo padrão da conta exigiu uma versão mais nova do Codex e os demais modelos do catálogo foram recusados com conta ChatGPT, de modo que nenhum agente do Codex foi executado e as linhas de subagente do Codex têm o status documentado.

### Skills

| Recurso | Claude Code | Codex CLI | Status |
|---|---|---|---|
| Pasta da skill | `.claude/skills/<nome>/SKILL.md` | `.agents/skills/<nome>/SKILL.md` | Observado nas duas |
| Campos obrigatórios | Nenhum, com `description` recomendada | `name` e `description` | Documentado |
| Acionar só pela pessoa | `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` em `agents/openai.yaml`, com polaridade inversa | Claude Code observado, Codex CLI documentado |
| Chamar pelo nome | `/nome` | `$nome` | Claude Code observado, Codex CLI documentado |
| Execução isolada | `context: fork` | Sem equivalente na documentação lida | Claude Code observado, Codex CLI não confirmado |
| Liberar ferramentas | `allowed-tools` | Sem equivalente na documentação lida, e a especificação aberta lista o campo como experimental | Claude Code observado, Codex CLI não confirmado |
| Restringir ferramentas | `disallowed-tools` | Sem equivalente na documentação lida | Claude Code observado, Codex CLI não confirmado |
| Argumentos e injeção de comando | `$ARGUMENTS`, `$N` e `` !`comando` `` | Uso em skills do Codex sem confirmação | Claude Code observado, Codex CLI não confirmado |
| Orçamento da lista de skills | 1% da janela, com corte de 1.536 caracteres por entrada | 2% da janela, ou 8.000 caracteres se a janela é desconhecida | Documentado, e o aviso de encurtamento foi observado no Codex CLI |

### Subagentes

| Recurso | Claude Code | Codex CLI | Status |
|---|---|---|---|
| Formato do arquivo | Markdown com front-matter YAML | TOML | Claude Code observado, Codex CLI documentado |
| Pasta | `.claude/agents/` | `.codex/agents/` | Claude Code observado, Codex CLI documentado |
| Campos obrigatórios | `name` e `description` | `name`, `description` e `developer_instructions` | Claude Code observado, Codex CLI documentado |
| Instruções do agente | Corpo do arquivo, que vira o prompt de sistema | Campo `developer_instructions` | Documentado |
| Restringir ferramentas | `tools` e `disallowedTools` | Chaves `features.*` com valor `false` removem capacidades, como `shell_tool`, `apps` e `plugins` | Claude Code observado, Codex CLI documentado |
| Permissões do agente | `permissionMode` no arquivo | Herdadas da sessão pai, e `sandbox_mode` e `approval_policy` colocados no arquivo do agente não as sobrescrevem | Documentado |
| Modelo | `model` | `model` e `model_reasoning_effort` | Documentado |
| Como invocar | Delegação pela `description`, nome citado no pedido, `@agent-<nome>` ou a opção `--agent` | Pedido em linguagem natural, com `/subagents` para alternar entre threads | Documentado |
| Aninhamento | Até três camadas por padrão | Limite de profundidade (`max_depth` não aparece na documentação lida) | Claude Code documentado, Codex CLI não confirmado |
| Ver os agentes carregados | `/context` lista os agentes, e `/agents` apenas orienta a editar os arquivos | O subcomando `codex agents` não existe na versão 0.140.0 | Observado |

### Instruções, hooks e diagnóstico

| Recurso | Claude Code | Codex CLI | Status |
|---|---|---|---|
| Arquivo de instrução do projeto | `CLAUDE.md` | `AGENTS.md`, lido da raiz do projeto até o diretório atual e concatenado nessa ordem, com limite padrão de 32 KiB | Codex CLI documentado |
| Leitura do `CLAUDE.md` | Arquivo próprio da ferramenta | A página do `AGENTS.md` não menciona o `CLAUDE.md` | Codex CLI não confirmado |
| Hooks | Descritos na Sessão 2 | Recurso estável e ativo em `codex features list` | Codex CLI observado |
| Ver o que o modelo recebe | `/context` | `codex debug prompt-input` mostra o prompt visível ao modelo, inclusive as skills | Observado nas duas |
| Diagnóstico | `claude --debug` e o log em `~/.claude/debug/` | `/debug-config` imprime o diagnóstico das camadas de configuração, e `codex doctor` examina a instalação | Claude Code observado, Codex CLI documentado |

A comparação de onde a restrição de ferramentas acontece em cada ferramenta está na seção [Restrição em camadas](seguranca-e-credenciais.md#restricao-em-camadas) da página de segurança.

## Fundamentação

Todas as fontes citadas nesta sessão estão na [bibliografia do curso](../referencia/bibliografia.md), com URL. As fontes das páginas originais são documentação oficial acessada em 22/10/2026 e um relato de engenharia da própria Anthropic. As fontes do front-matter e do Codex CLI são a documentação do Claude Code, a do Codex CLI e a especificação Agent Skills, acessadas em 23/10/2026, e nenhuma delas mede as tarefas da equipe. Os números de custo e de desempenho valem para as versões e as configurações descritas em cada fonte.

| Página | Fontes citadas |
|---|---|
| Skills | [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao), [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao), [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code), [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Agent Skills: especificação aberta](../referencia/bibliografia.md#agent-skills-especificacao-aberta) e [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao) |
| Agentes e subagentes | [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system), [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao), [Codex: Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao) e [Codex: AGENTS.md](../referencia/bibliografia.md#openai-codex-agentsmd-documentacao) |
| Escolher o mecanismo | [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) e [Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao) |
| Geração de artefatos | [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) e [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) |
| Escolha de modelos | [Choosing the Right Model](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code), [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) e [Codex: Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao) |
| Custo de tokens | [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code), [Prompt Caching](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao), [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system), [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao) e [Codex: comandos](../referencia/bibliografia.md#openai-codex-developer-commands-documentacao) |
| Performance | [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system), [Prompt Caching](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao), [Choosing the Right Model](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) e [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) |
| Segurança e credenciais | [Claude Code Security](../referencia/bibliografia.md#anthropic-claude-code-security-documentacao), [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Azure DevOps PATs](../referencia/bibliografia.md#microsoft-use-personal-access-tokens-in-azure-devops-documentacao), [GitHub PATs](../referencia/bibliografia.md#github-managing-your-personal-access-tokens-documentacao), [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Codex: aprovações e segurança](../referencia/bibliografia.md#openai-codex-agent-approvals-and-security-documentacao) e [Codex: referência de configuração](../referencia/bibliografia.md#openai-codex-configuration-reference-documentacao) |
| Oficina de ferramentas | [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao), [Codex: Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao), [Codex: aprovações e segurança](../referencia/bibliografia.md#openai-codex-agent-approvals-and-security-documentacao) e [Codex: comandos](../referencia/bibliografia.md#openai-codex-developer-commands-documentacao) |
| Exercícios | [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao) e [Codex: Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao) |
| Referência rápida desta página | [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Agent Skills: especificação aberta](../referencia/bibliografia.md#agent-skills-especificacao-aberta), [Codex: Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao), [Codex: Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao), [Codex: AGENTS.md](../referencia/bibliografia.md#openai-codex-agentsmd-documentacao), [Codex: aprovações e segurança](../referencia/bibliografia.md#openai-codex-agent-approvals-and-security-documentacao), [Codex: comandos](../referencia/bibliografia.md#openai-codex-developer-commands-documentacao) e [Codex: referência de configuração](../referencia/bibliografia.md#openai-codex-configuration-reference-documentacao) |

As páginas do Claude Code foram lidas em Markdown cru e as do Codex CLI também, e a especificação aberta foi lida na página oficial. As URLs `developers.openai.com/codex/...` respondem 308 para `learn.chatgpt.com/docs/...`, e nenhuma das páginas exibe data de publicação.

- Claude Code: [skills](https://code.claude.com/docs/en/skills) e [subagentes](https://code.claude.com/docs/en/sub-agents).
- Codex CLI: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security), [comandos](https://learn.chatgpt.com/docs/developer-commands) e [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference).
- Padrão aberto: [especificação Agent Skills](https://agentskills.io/specification).

## Conexão com a próxima sessão

A Sessão 9 trata de depuração sistemática e de revisão de código gerado por IA. Ela parte de skills e agentes que a equipe já escreveu nesta sessão, porque um agente que gera código ou artefatos produz defeitos que precisam de hipótese, investigação e verificação, e o registro de modelo, tokens, tempo e resultado da conferência, definido aqui, é o primeiro dado que a depuração consulta.
