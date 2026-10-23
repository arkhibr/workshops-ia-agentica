# Claude Code e Codex CLI: equivalências

Skills e subagentes existem nas duas ferramentas, com nomes, arquivos e campos diferentes, e esta página reúne a correspondência entre elas para quem usa o Codex CLI e lê exemplos escritos para o Claude Code. Cada linha traz um status de evidência: **observado** quando o comportamento foi executado na versão registrada, **documentado** quando a informação foi lida na página oficial sem execução, e **não confirmado** quando a documentação lida não cobre o item ou o resultado não pôde ser verificado.

!!! info "Versões verificadas"
    A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`. As observações desta página foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e o comando `codex doctor` informa a versão 0.164.0 como disponível. O modelo padrão da conta exigiu uma versão mais nova do Codex e os demais modelos do catálogo foram recusados com conta ChatGPT, de modo que nenhum agente do Codex foi executado e as linhas de subagente do Codex têm o status documentado.

## Skills

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

## Subagentes

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

## Instruções, hooks e diagnóstico

| Recurso | Claude Code | Codex CLI | Status |
|---|---|---|---|
| Arquivo de instrução do projeto | `CLAUDE.md` | `AGENTS.md`, lido da raiz do projeto até o diretório atual e concatenado nessa ordem, com limite padrão de 32 KiB | Codex CLI documentado |
| Leitura do `CLAUDE.md` | Arquivo próprio da ferramenta | A página do `AGENTS.md` não menciona o `CLAUDE.md` | Codex CLI não confirmado |
| Hooks | Descritos na Sessão 2 | Recurso estável e ativo em `codex features list` | Codex CLI observado |
| Ver o que o modelo recebe | `/context` | `codex debug prompt-input` mostra o prompt visível ao modelo, inclusive as skills | Observado nas duas |
| Diagnóstico | `claude --debug` e o log em `~/.claude/debug/` | `/debug-config` imprime o diagnóstico das camadas de configuração, e `codex doctor` examina a instalação | Claude Code observado, Codex CLI documentado |

## Restrição em camadas

A diferença de maior efeito prático entre as duas ferramentas está em onde a restrição de ferramentas acontece. No Claude Code, os campos `tools` e `disallowedTools` do arquivo do agente removem ferramentas do conjunto, e a restrição foi observada: o subagente com `tools: Read, Grep, Glob` não editou o arquivo. No Codex CLI, o sandbox e a aprovação são definidos na sessão que inicia o agente e herdados pelos subagentes, e a documentação adverte que instruções para evitar edições não criam um sandbox somente leitura.

![Duas colunas comparam as camadas de restrição. No Claude Code, tools e disallowedTools do subagente e disallowed-tools da skill removem ferramentas, allowed-tools e permissionMode liberam ou definem a aprovação sem restringir, o corpo do arquivo orienta e os hooks bloqueiam por programa. No Codex CLI, sandbox_mode e approval_policy da sessão são herdados, as chaves features removem capacidades, developer_instructions e AGENTS.md apenas orientam, e não há equivalente documentado para liberar ferramenta por skill, enquanto valores de permissão colocados no arquivo do agente não sobrescrevem a sessão pai.](assets/restricao-em-camadas.png)

Para o Codex CLI, o equivalente de um subagente somente leitura é iniciar a sessão com o sandbox `read-only`, e esse valor consta da documentação de aprovações e segurança sem execução observada. Um exemplo de agente escrito para o Claude Code com `tools: Read, Grep, Glob` precisa, portanto, de uma ressalva ao ser reaproveitado no Codex, porque o arquivo equivalente não restringe nada sozinho.

## Fontes lidas em 23/10/2026

As páginas do Claude Code foram lidas em Markdown cru e as do Codex CLI também, e a especificação aberta foi lida na página oficial. As URLs `developers.openai.com/codex/...` respondem 308 para `learn.chatgpt.com/docs/...`, e nenhuma das páginas exibe data de publicação.

- Claude Code: [skills](https://code.claude.com/docs/en/skills) e [subagentes](https://code.claude.com/docs/en/sub-agents).
- Codex CLI: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security), [comandos](https://learn.chatgpt.com/docs/developer-commands) e [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference).
- Padrão aberto: [especificação Agent Skills](https://agentskills.io/specification).

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
