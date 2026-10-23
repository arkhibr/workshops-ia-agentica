# Front-matter de subagentes

Um subagente é um agente auxiliar com janela de contexto própria, definido num arquivo Markdown cujo front-matter YAML declara nome, ferramentas, modelo e permissões, e cujo corpo vira o prompt de sistema. A tabela de oito campos da página [Agentes e subagentes](agentes-e-subagentes.md#anatomia-de-um-subagente) cobre o uso básico, e esta página completa a lista, explica o `permissionMode`, a resolução do `model` e a ordem de escopo, e compara o contexto do subagente com o da skill.

!!! info "Versões verificadas"
    As observações desta página foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e cada afirmação indica se foi observada, se vem da documentação ou se continua sem confirmação. A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`, e o comportamento pode divergir em versões diferentes das citadas.

## Campos que a tabela anterior não cobre

Só `name` e `description` são obrigatórios, e os nomes compostos usam camelCase, como `maxTurns` e `disallowedTools`. O campo precisa ter o nome exato da documentação, porque o Claude Code ignora sem reportar erro o campo que não reconhece. Os campos da tabela completam os oito já apresentados, que são `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns` e `skills`.

| Campo | Efeito | Observação |
|---|---|---|
| `mcpServers` | Servidores MCP disponíveis só para este subagente, por nome ou por definição completa | Ignorado em subagentes de plugin |
| `hooks` | Hooks de ciclo de vida limitados ao subagente | Ignorado em subagentes de plugin |
| `memory` | Memória persistente entre sessões, com escopo `user`, `project` ou `local` | Sem o campo, o subagente não tem memória própria, e a memória automática da conversa principal não é carregada nele |
| `background` | Com `true`, mantém o subagente em segundo plano mesmo quando o modelo pede para esperá-lo | Subagentes criados pela conversa principal já começam em segundo plano por padrão |
| `omitClaudeMd` | Com `true`, inicia sem os arquivos `CLAUDE.md` de usuário, projeto e local | Requer v2.1.271 ou posterior |
| `effort` | Nível de esforço do subagente (`low`, `medium`, `high`, `xhigh`, `max`) | Não sobrepõe a variável `CLAUDE_CODE_EFFORT_LEVEL` |
| `isolation` | Com `worktree`, executa numa cópia temporária do repositório, ramificada da branch padrão | A worktree é removida se não houver alterações |
| `color` | Cor na lista de tarefas e na transcrição | Valores documentados: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` |
| `initialPrompt` | Primeira mensagem enviada automaticamente quando o agente roda como agente principal | Só vale com `--agent` ou com a configuração `agent` |
| `autoCompactWindow` | Reduz a janela de compactação automática, entre 100000 e 1000000 tokens | Requer v2.1.296 ou posterior |
| `experimental` | Mapa de opções experimentais, hoje com `cacheTtl` igual a `5m` ou `1h` | Requer v2.1.248 ou posterior |

O campo `name` aceita até 256 caracteres, exige um primeiro caractere diferente de `-` e proíbe `:`, símbolo que pertence aos identificadores de plugin, como `meu-plugin:revisor`. Na observação, um arquivo com `name: meu:revisor` não carregou, e o log de depuração registrou `names must not contain ':' (reserved for plugin namespacing)`.

O campo `color` mostra a diferença entre o que a documentação lista e o que a versão instalada aceita. Um subagente com `color: magenta`, valor fora da lista, foi carregado sem nenhum aviso no log da versão 2.1.309, e o efeito visual do valor não foi observado. Uma lista de valores válidos é, por isso, mais segura do que um exemplo copiado de outro projeto.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os subagentes ficam em `.claude/agents/` e a [tabela de campos](https://code.claude.com/docs/en/sub-agents#frontmatter-reference) lista cada campo aceito.
    **Codex CLI:** o subagente é um arquivo TOML em `.codex/agents/` com `name`, `description` e `developer_instructions` obrigatórios, e os campos `model` e `model_reasoning_effort` ajustam o modelo, conforme a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents). Esse formato está documentado e ainda sem execução observada, e o Codex não tem campo equivalente a `isolation`, `memory` ou `color` na documentação lida.

## Contexto próprio e isolamento

Cada subagente começa com uma janela de contexto nova, sem o histórico da conversa, e o corpo do arquivo é o prompt de sistema dele. A saída volumosa de ferramentas fica na janela do subagente, e apenas o resumo volta à conversa principal. A skill carrega o procedimento na janela principal, e a skill com `context: fork` combina o procedimento fixo com o isolamento do subagente.

![Três colunas comparam onde o trabalho acontece. Na skill, o corpo e a saída das ferramentas somam à janela principal. No subagente, uma janela própria começa vazia, recebe o corpo do arquivo como prompt de sistema e devolve só o resumo. Na skill com context fork, a janela do subagente recebe o corpo da skill como prompt, sem o histórico, e devolve só o resumo.](assets/contexto-skill-subagente-fork.png)

O campo `skills` injeta o conteúdo completo das skills listadas na inicialização do subagente, e uma skill com `disable-model-invocation: true` não pode ser pré-carregada dessa forma. Um subagente pode criar subagentes próprios, até três camadas abaixo da conversa principal, e a variável `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` altera o limite. No limite, o Claude Code retira a ferramenta `Agent` do subagente, que executa o trabalho sozinho e devolve um único resumo.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** o isolamento e o aninhamento constam de [Let subagents spawn their own subagents](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents), e a skill com fork de [Run skills in a subagent](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent).
    **Codex CLI:** os subagentes herdam o sandbox da sessão pai, e o limite de profundidade de aninhamento é um item sem confirmação nas páginas lidas. A fonte é a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## O `permissionMode`

O campo `permissionMode` aceita `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` e `plan`, e `manual` funciona como apelido de `default`. A configuração do subagente vale somente em parte dos casos, porque o modo da conversa principal prevalece.

| Modo da conversa principal | Efeito sobre o `permissionMode` do subagente |
|---|---|
| `bypassPermissions`, `acceptEdits` ou `auto` | O subagente roda no mesmo modo da conversa, e o valor do arquivo é ignorado |
| `plan` | O subagente permanece em `plan`, qualquer que seja o valor do arquivo |
| `default` ou `dontAsk` | O subagente roda no modo do arquivo, salvo `bypassPermissions` (a partir da v2.1.267) e `auto` quando o modo automático não está disponível |

A restrição de `tools` é independente do modo de permissão. Na observação, a conversa principal estava em `acceptEdits`, e o subagente com `tools: Read, Grep, Glob` ainda assim não conseguiu editar o arquivo, enquanto o subagente com o campo escrito `tool` editou. O `tools` define quais ferramentas existem para o subagente, e o `permissionMode` define apenas se a execução delas pede aprovação.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os modos constam de [Permission modes](https://code.claude.com/docs/en/sub-agents#permission-modes).
    **Codex CLI:** o sandbox e a aprovação se definem na sessão pai, e `sandbox_mode` e `approval_policy` colocados no arquivo do agente não sobrescrevem essa configuração, de modo que não há permissão por agente. A documentação adverte ainda que instruções para evitar edições não criam um sandbox somente leitura. A redução de capacidades por agente usa chaves como `features.shell_tool` com valor `false`, e a fonte é a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Resolução do `model`

O campo `model` aceita os apelidos `sonnet`, `opus`, `haiku` e `fable`, um identificador completo de modelo ou `inherit`. O Claude Code resolve o modelo do subagente em quatro passos, na ordem em que aparecem:

1. O parâmetro `model` passado pelo modelo na própria chamada de delegação.
2. O campo `model` do arquivo do subagente, em que `inherit` seleciona o modelo da conversa principal.
3. A variável de ambiente `CLAUDE_CODE_SUBAGENT_MODEL`, quando definida com um apelido ou um identificador.
4. O modelo da conversa principal.

Antes da v2.1.251, a variável de ambiente vinha em primeiro lugar e prevalecia sobre a chamada e sobre o arquivo. A lista completa de identificadores válidos não foi confirmada, e por isso os exemplos do material usam apenas os apelidos.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a ordem consta de [Choose a model](https://code.claude.com/docs/en/sub-agents#choose-a-model).
    **Codex CLI:** o valor de `model` no arquivo do agente prevalece sobre o do pai, e os padrões globais dos subagentes ficam em `agents.default_subagent_model`, conforme a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) e a referência de configuração.

## Precedência de escopo

Quando dois arquivos declaram o mesmo `name`, vale o de maior prioridade, e a ordem dos subagentes difere da ordem das skills.

![Duas escadas de precedência lado a lado. Subagentes: configurações gerenciadas, opção --agents, pasta .claude/agents do projeto, pasta pessoal e pasta agents de plugin. Skills: corporativa, pessoal e projeto, com os plugins fora da disputa por usarem prefixo. Um aviso destaca que em subagentes o projeto vence o escopo pessoal e em skills o escopo pessoal vence o projeto.](assets/precedencia-de-escopo.png)

O Claude Code procura subagentes de projeto subindo do diretório de trabalho até a raiz do repositório, e em pastas aninhadas com o mesmo `name` vale a definição mais próxima do diretório de trabalho. Dois arquivos com o mesmo `name` dentro da mesma árvore `.claude/agents/` resultam no carregamento de apenas um, escolhido pela ordem de leitura do sistema de arquivos, sem precedência documentada. Como a escolha entre duplicatas depende da ordem de leitura do sistema de arquivos, o nome de cada subagente precisa ser único na árvore inteira, e o comando `/doctor` lista as duplicatas encontradas na mesma pasta.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as duas ordens constam de [Choose the subagent scope](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope) e de [Resolve skills that share a name](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name).
    **Codex CLI:** um agente customizado com o mesmo nome de um agente embutido, como `explorer`, tem precedência sobre ele, e vale o campo `name` do arquivo, conforme a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

**Próxima página:** [Depuração de skills e agentes](depuracao-de-skills-e-agentes.md).
