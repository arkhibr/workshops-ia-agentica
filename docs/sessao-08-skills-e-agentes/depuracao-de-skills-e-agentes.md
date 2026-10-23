# Depuração de skills e agentes

Uma skill ou um subagente com erro no front-matter raramente produz uma mensagem de erro na sessão: o arquivo deixa de carregar, ou carrega sem o campo errado, e o comportamento muda sem aviso. Esta página reúne as falhas silenciosas mais comuns, os comandos que mostram o que foi de fato carregado e o caminho para localizar o erro no log de depuração.

!!! info "Versões verificadas"
    As observações desta página foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e cada afirmação indica se foi observada, se vem da documentação ou se continua sem confirmação. A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`, e o comportamento pode divergir em versões diferentes das citadas.

## Falhas silenciosas

Num subagente, cada problema de front-matter tem um efeito e um lugar onde o registro aparece. A coluna de evidência indica se o comportamento foi observado na versão 2.1.309 ou se vem da documentação.

| Problema no arquivo do subagente | O que acontece | Onde aparece | Evidência |
|---|---|---|---|
| Primeira linha diferente de `---`, inclusive uma linha em branco | O arquivo é tratado como documentação e não carrega | Nenhum registro no log, e o agente fica ausente de `/context` | Observado |
| `name` com `:`, iniciado em `-` ou com mais de 256 caracteres | O arquivo é ignorado | Linha `[ERROR]` no log de depuração | Observado para `:` |
| Falta `description` | O arquivo é ignorado | Linha `[DEBUG]` no log: `missing required 'description' in frontmatter` | Observado |
| YAML que não pode ser lido | Nenhum campo é lido e o arquivo é ignorado | Erro de leitura no log | Documentado |
| Campo com nome errado, como `tool` no lugar de `tools` | O agente carrega sem o campo e, sem `tools`, herda todas as ferramentas | Linha `[WARN]` com a sugestão `did you mean "tools"?` | Observado, e o agente editou o arquivo que o `tools` correto impediu |
| Valor fora da lista documentada, como `color: magenta` | O agente carrega | Nenhum aviso | Observado |

Numa skill, o Claude Code lê o front-matter somente quando o primeiro `---` está na primeira linha do arquivo, e trata o arquivo inteiro como conteúdo da skill em qualquer outro caso. YAML inválido faz a skill carregar sem nenhum campo: o comando `/nome` continua funcionando, e o modelo deixa de acioná-la pela `description`. Campos desconhecidos são ignorados sem erro, e um nome de pasta com caracteres como o espaço de largura zero ou `<` impede o carregamento. Um `paths` que aponta para arquivos fora do diretório de trabalho atual mantém a skill inativa. Esses comportamentos de skill constam da documentação, e a observação desta sessão cobriu só os subagentes.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as regras de arquivos ignorados constam de [Subagent files Claude Code skips](https://code.claude.com/docs/en/sub-agents#subagent-files-claude-code-skips) e de [Skill not triggering](https://code.claude.com/docs/en/skills#skill-not-triggering).
    **Codex CLI:** a documentação lida não descreve falhas silenciosas de front-matter de skill ou de agente, item sem confirmação. Uma skill em `.agents/skills/` apareceu no prompt visível ao modelo pelo comando `codex debug prompt-input`, observado na versão 0.140.0.

## Ver o que foi carregado

O comando mais direto é `/context`, que no `claude 2.1.309` funcionou também em modo não interativo e lista as tabelas Custom Agents e Skills, cada uma com origem e custo em tokens. Na observação, os três subagentes inválidos estavam ausentes da tabela, `tool-errado` constava como carregado, e uma skill com `disable-model-invocation: true` existia na pasta e não aparecia na tabela de skills, o que confirma que o campo a retira do contexto do modelo.

| Comando | O que mostra | Evidência |
|---|---|---|
| `/context` | Subagentes e skills carregados, com origem e tokens | Observado |
| `/agents` | Na versão 2.1.309, informa que o assistente foi removido e orienta a editar `.claude/agents/` ou `~/.claude/agents/` | Observado. Até a v2.1.197 abria um assistente interativo, segundo a documentação |
| `/skills` | Indisponível em modo não interativo. O comportamento em sessão interativa não foi verificado | Observado em modo não interativo |
| `/doctor` | Estima o custo da listagem de skills e aponta nomes duplicados na mesma pasta de subagentes | Documentado |
| `claude agents` | Gerencia sessões em segundo plano e não lista subagentes | Observado em `claude --help` |

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os comandos constam de [Skill descriptions are cut short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short) e da página de [subagentes](https://code.claude.com/docs/en/sub-agents).
    **Codex CLI:** `/skills` lista e seleciona skills, `/subagents` alterna entre threads de subagentes e `/debug-config` imprime o diagnóstico das camadas de configuração, conforme a [documentação de comandos](https://learn.chatgpt.com/docs/developer-commands). O comando `codex agents` não existe na versão 0.140.0, observado em `codex --help`.

## Localizar o erro no log

O log de depuração é a única fonte que nomeia o erro de um subagente ou de uma skill. A opção `--debug` grava o log em `~/.claude/debug/<id-da-sessão>.txt`, e a opção `--debug-file` grava no caminho escolhido. A mensagem de campo desconhecido, `does not recognize or apply`, exige a versão 2.1.296 ou posterior, e o comando `claude --version` confirma a versão antes do Experimento D da oficina.

=== "macOS/Linux"

    ```bash
    claude -p "diga ok" --debug-file depuracao.log
    grep -n "Agent file" depuracao.log
    ```

=== "Windows (PowerShell)"

    ```powershell
    claude -p "diga ok" --debug-file depuracao.log
    Select-String -Path depuracao.log -Pattern "Agent file"
    ```

Para listar os logs gravados pela opção `--debug`, sem caminho próprio, o comando difere entre os sistemas.

=== "macOS/Linux"

    ```bash
    ls -t ~/.claude/debug | head -3
    ```

=== "Windows (PowerShell)"

    ```powershell
    Get-ChildItem "$HOME\.claude\debug" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
    ```

O caminho no Windows segue a documentação, que escreve `~/.claude/debug`, e não foi observado nessa plataforma.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a opção `--debug` e a mensagem de campo desconhecido constam de [Frontmatter reference](https://code.claude.com/docs/en/sub-agents#frontmatter-reference).
    **Codex CLI:** a documentação lida não descreve opção de log equivalente para skills e agentes, item sem confirmação. O comando `codex debug prompt-input` mostra o prompt visível ao modelo, e `codex doctor` diagnostica a instalação, ambos observados em `codex --help`.

## Validar a pasta antes da sessão

O comando `claude plugin validate` aceita uma pasta de skills ou de agentes, como `.claude/skills` ou `.claude/agents`, e exige a versão 2.1.233 ou posterior. Na observação, a pasta de skills passou, e a pasta de agentes produziu um único aviso, sobre o arquivo sem `description`. O comando deixou sem sinalização o `name` com `:`, o campo `tool`, o valor `magenta` e a primeira linha em branco, e a documentação confirma o limite: o comando verifica se o YAML pode ser lido e não sinaliza um arquivo cujo front-matter é válido e sem `name`. A ordem recomendada é rodar `claude plugin validate` antes da sessão para pegar erros de leitura do YAML e consultar o log de depuração quando o agente se comportar de modo diferente do esperado.

```bash
claude plugin validate .claude/agents
claude plugin validate .claude/skills
```

Os dois comandos funcionam do mesmo modo em macOS, Linux e Windows. Uma skill editada durante a sessão é detectada sem reinício, e uma pasta de skills criada depois do início da sessão exige `/reload-skills`. Um subagente em `~/.claude/agents/` criado quando a pasta não existia no início da sessão exige o reinício do Claude Code.

## Skill que não aciona

A documentação propõe uma sequência para a skill que o modelo não usa quando devia:

1. Conferir se a `description` contém as palavras que a pessoa diria naturalmente.
2. Verificar se a skill aparece na pergunta "What skills are available?".
3. Reformular o pedido para se aproximar da `description`.
4. Invocar a skill pelo nome com `/nome`, se ela aceitar invocação pela pessoa.
5. Se `/nome` também não for reconhecido, verificar se o Claude Code recusou o nome da skill.
6. Se a skill usa `paths`, verificar se os arquivos estão dentro do diretório de trabalho atual.

A observação desta sessão acrescenta um cuidado de método: o nome da skill também orienta o modelo, e uma skill chamada `resumo-semanal-de-chamados` acionou com as três primeiras descrições testadas. O teste da `description` isolada exige um nome neutro, como `rotina-a7`, e a oficina usa essa regra. Para o problema inverso, a skill acionada em excesso, a documentação recomenda tornar a `description` mais específica ou adicionar `disable-model-invocation: true`. Quando o modelo deixa de seguir uma skill depois do primeiro turno, a documentação orienta mover a regra obrigatória para um hook e colocar as instruções mais importantes no início do `SKILL.md`, porque a compactação da conversa pode manter só o começo da skill invocada.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a sequência consta de [Skill not triggering](https://code.claude.com/docs/en/skills#skill-not-triggering) e de [Claude stops following a skill](https://code.claude.com/docs/en/skills#claude-stops-following-a-skill).
    **Codex CLI:** a skill pode ser invocada explicitamente por `$nome`, e `policy.allow_implicit_invocation: false` restringe a invocação à forma explícita, conforme [Build skills](https://learn.chatgpt.com/docs/build-skills).

**Próxima página:** [Claude Code e Codex CLI](claude-code-e-codex.md).
