# Agentes e subagentes

Um agente executa uma tarefa em várias etapas, decidindo por conta própria quais ferramentas chamar, e um subagente é um agente auxiliar que recebe uma parte do trabalho num contexto separado. Esta página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Arquivo e front-matter" no recorte do subagente, e percorre a anatomia do arquivo, o isolamento de contexto, as ferramentas e as permissões, a ordem de escopo e o custo de usar vários agentes. A escolha entre subagente, skill e os demais mecanismos fica na página [Escolher o mecanismo](escolher-o-mecanismo.md).

## Workflow, agente e subagente

O guia [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) distingue o workflow, em que o código orquestra o modelo por um caminho predefinido, do agente, em que o próprio modelo decide os passos, e recomenda a solução mais simples possível, aumentando a autonomia somente quando o problema exige. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) define o subagente como um assistente especializado para o qual o Claude Code delega tarefas, com janela de contexto própria, prompt de sistema próprio, acesso restrito a ferramentas e permissões independentes. O agente principal delega quando a tarefa corresponde ao campo `description` do subagente, e o Claude Code exibe um aviso na inicialização quando as descrições de todos os subagentes somam mais de 15 mil tokens.

## Anatomia e front-matter do subagente

O subagente é um arquivo Markdown com frontmatter YAML, e o corpo do arquivo se torna o prompt de sistema dele. Apenas `name` e `description` são obrigatórios, e os nomes compostos usam camelCase, como `maxTurns` e `disallowedTools`. O campo precisa ter o nome exato da documentação, porque o Claude Code ignora sem reportar erro o campo que não reconhece.

```markdown
---
name: revisor-de-reuniao
description: Revisa tarefas e riscos extraídos de transcrições. Use depois de gerar ou editar o relatório de reunião.
tools: Read, Grep, Glob
model: haiku
maxTurns: 8
---

Você revisa um relatório de reunião e sua transcrição. Liste seções ausentes,
afirmativas sem evidência e responsáveis ou prazos inventados.
Não edite arquivos. Devolva uma lista curta, com a linha de cada problema.
```

### Campos de uso comum

| Campo | Função |
|---|---|
| `name` | Identificador único, obrigatório |
| `description` | Diz ao agente principal quando delegar, obrigatório |
| `tools` | Lista de ferramentas permitidas. Se omitido, o subagente herda todas as disponíveis |
| `disallowedTools` | Lista de ferramentas negadas, aplicada antes de `tools` |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, um identificador completo ou `inherit`, com a ordem de resolução descrita em [Escolha de modelos](escolha-de-modelos.md#resolucao-do-model-por-subagente-e-por-skill) |
| `permissionMode` | Modo de permissão, como `default`, `acceptEdits`, `plan` ou `bypassPermissions` |
| `maxTurns` | Número máximo de turnos antes de o subagente parar |
| `skills` | Skills carregadas no contexto na inicialização |

### Campos menos usados

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

## Contexto e isolamento

Cada subagente começa com uma janela de contexto nova, sem ver o histórico da conversa nem os arquivos já lidos, e o corpo do arquivo é o prompt de sistema dele. A saída volumosa, como a de uma suíte de testes, permanece no contexto do subagente, e apenas o resumo retorna à conversa principal. A documentação aponta esse efeito como o principal benefício, e o guia de custo recomenda delegar a subagentes a execução de testes, a busca em documentação e o processamento de logs. Uma skill comum carrega suas instruções na janela principal; com `context: fork`, suas instruções são executadas em um subagente. Para comparar os dois casos com um exemplo completo de reunião, veja [Skill com fork ou subagente: qual é a diferença?](escolher-o-mecanismo.md#skill-com-fork-ou-subagente-qual-e-a-diferenca).

![Três colunas comparam onde o trabalho acontece. Na skill, o corpo e a saída das ferramentas somam à janela principal. No subagente, uma janela própria começa vazia, recebe o corpo do arquivo como prompt de sistema e devolve só o resumo. Na skill com context fork, a janela do subagente recebe o corpo da skill como prompt, sem o histórico, e devolve só o resumo.](assets/contexto-skill-subagente-fork.png)

Os pedidos de um subagente contam para os mesmos limites de uso da conversa principal. O isolamento reduz o tamanho do contexto da conversa principal, mas não reduz o consumo total de tokens, que costuma aumentar pela soma dos contextos.

O campo `skills` injeta o conteúdo completo das skills listadas na inicialização do subagente, e uma skill com `disable-model-invocation: true` não pode ser pré-carregada dessa forma. Um subagente pode criar subagentes próprios, até três camadas abaixo da conversa principal, e a variável `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` altera o limite. No limite, o Claude Code retira a ferramenta `Agent` do subagente, que executa o trabalho sozinho e devolve um único resumo.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** o isolamento e o aninhamento constam de [Let subagents spawn their own subagents](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents), e a skill com fork de [Run skills in a subagent](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent).
    **Codex CLI:** os subagentes herdam o sandbox da sessão pai, e o limite de profundidade de aninhamento é um item sem confirmação nas páginas lidas. A fonte é a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Ferramentas, permissões e arquivos ignorados

Duas regras da documentação pedem atenção na escrita. O Claude Code ignora em silêncio os campos de frontmatter que não reconhece, e o campo `tools` omitido faz o subagente herdar todas as ferramentas. A combinação indica que um campo de restrição escrito com erro de grafia deixa o subagente com acesso total, e o teste da oficina confirmou o efeito na versão 2.1.309 do Claude Code: o subagente com `tool` no lugar de `tools` carregou e editou o arquivo, e o log de depuração registrou o campo desconhecido com a sugestão `tools`.

### O `permissionMode`

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

### Arquivos que o Claude Code ignora

Num subagente, cada problema de front-matter tem um efeito e um lugar onde o registro aparece. A coluna de evidência indica se o comportamento foi observado na versão 2.1.309 ou se vem da documentação.

| Problema no arquivo do subagente | O que acontece | Onde aparece | Evidência |
|---|---|---|---|
| Primeira linha diferente de `---`, inclusive uma linha em branco | O arquivo é tratado como documentação e não carrega | Nenhum registro no log, e o agente fica ausente de `/context` | Observado |
| `name` com `:`, iniciado em `-` ou com mais de 256 caracteres | O arquivo é ignorado | Linha `[ERROR]` no log de depuração | Observado para `:` |
| Falta `description` | O arquivo é ignorado | Linha `[DEBUG]` no log: `missing required 'description' in frontmatter` | Observado |
| YAML que não pode ser lido | Nenhum campo é lido e o arquivo é ignorado | Erro de leitura no log | Documentado |
| Campo com nome errado, como `tool` no lugar de `tools` | O agente carrega sem o campo e, sem `tools`, herda todas as ferramentas | Linha `[WARN]` com a sugestão `did you mean "tools"?` | Observado, e o agente editou o arquivo que o `tools` correto impediu |
| Valor fora da lista documentada, como `color: magenta` | O agente carrega | Nenhum aviso | Observado |

O log de depuração, o comando `/context` e o `claude plugin validate .claude/agents` mostram o que carregou e o que foi ignorado. O [Experimento D](experimentos-complementares.md#experimento-d-localizar-front-matter-com-erro-no-log-de-depuracao) da oficina reproduz os três erros mais comuns e traz os comandos, e a seção [O que o Claude Code mostra do que foi carregado](custo-de-tokens.md#o-que-o-claude-code-mostra-do-que-foi-carregado) reúne os comandos que mostram o que está carregado.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as regras de arquivos ignorados constam de [Subagent files Claude Code skips](https://code.claude.com/docs/en/sub-agents#subagent-files-claude-code-skips).
    **Codex CLI:** a documentação lida não descreve falhas silenciosas de front-matter de agente, item sem confirmação.

## Escopo e precedência

Os subagentes ficam em `.claude/agents/` quando pertencem ao projeto e em `~/.claude/agents/` quando são pessoais. Quando dois arquivos declaram o mesmo `name`, vale o de maior prioridade, e a ordem dos subagentes difere da ordem das skills.

![Duas escadas de precedência lado a lado. Subagentes: configurações gerenciadas, opção --agents, pasta .claude/agents do projeto, pasta pessoal e pasta agents de plugin. Skills: corporativa, pessoal e projeto, com os plugins fora da disputa por usarem prefixo. Um aviso destaca que em subagentes o projeto vence o escopo pessoal e em skills o escopo pessoal vence o projeto.](assets/precedencia-de-escopo.png)

O Claude Code procura subagentes de projeto subindo do diretório de trabalho até a raiz do repositório, e em pastas aninhadas com o mesmo `name` vale a definição mais próxima do diretório de trabalho. Dois arquivos com o mesmo `name` dentro da mesma árvore `.claude/agents/` resultam no carregamento de apenas um, escolhido pela ordem de leitura do sistema de arquivos, sem precedência documentada. Como a escolha entre duplicatas depende da ordem de leitura do sistema de arquivos, o nome de cada subagente precisa ser único na árvore inteira, e o comando `/doctor` lista as duplicatas encontradas na mesma pasta.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as duas ordens constam de [Choose the subagent scope](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope) e de [Resolve skills that share a name](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name).
    **Codex CLI:** um agente customizado com o mesmo nome de um agente embutido, como `explorer`, tem precedência sobre ele, e vale o campo `name` do arquivo, conforme a [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Quando usar vários agentes

A Anthropic relatou, em [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system), que um orquestrador Opus com subagentes Sonnet superou em 90,2% o agente Opus único na avaliação interna de pesquisa. O mesmo relato informa que agentes usam cerca de 4 vezes os tokens de um chat e que sistemas com vários agentes usam cerca de 15 vezes. Esses números vêm do relato da própria empresa, em tarefas de pesquisa, e não foram replicados de forma independente.

| Cabem em vários agentes | Não cabem em vários agentes |
|---|---|
| Pesquisa aberta e ampla, com muita paralelização | Domínios em que todos os agentes precisam do mesmo contexto |
| Informação maior que uma janela de contexto | Tarefas com muitas dependências entre as partes |
| Tarefas com muitas ferramentas complexas | A maioria das tarefas de programação, com poucas partes realmente paralelas |
| Tarefas de valor suficiente para pagar o custo extra | Coordenação e delegação em tempo real |

O relato lista os modos de falha observados: criação de 50 subagentes para uma consulta simples, busca interminável por fontes inexistentes, subagentes que duplicam trabalho ou deixam lacunas, e subagentes que se distraem com atualizações excessivas. A causa mais citada foi instrução vaga de delegação, e a correção foi dar a cada subagente um objetivo, um formato de saída, orientação sobre ferramentas e limites da tarefa. O relato também dimensiona o esforço pela complexidade: uma busca de fato simples usa um agente com 3 a 10 chamadas de ferramenta, e uma comparação usa de 2 a 4 subagentes com 10 a 15 chamadas cada.

O Claude Code limita por padrão o aninhamento a três camadas abaixo da conversa principal, com a variável `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, e a execução simultânea a 20 subagentes, com `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`. O guia de custo informa ainda que equipes de agentes consomem cerca de 7 vezes mais tokens que uma sessão comum quando os integrantes trabalham em modo de plano.

!!! abstract "Linha da ficha"
    Arquivo e front-matter do subagente:

    - Que ferramentas e que modo de permissão o subagente declara, e o `tools` está escrito sem erro de grafia?
    - Em que escopo o arquivo fica e quem o aciona, a pessoa ou o modelo pela `description`?

**Próxima página:** [Escolher o mecanismo](escolher-o-mecanismo.md).
