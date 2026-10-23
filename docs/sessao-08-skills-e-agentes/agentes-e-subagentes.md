# Agentes e subagentes

Um agente executa uma tarefa em várias etapas, decidindo por conta própria quais ferramentas chamar, e um subagente é um agente auxiliar que recebe uma parte do trabalho num contexto separado. Esta página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Mecanismo" e a linha "Arquivo e front-matter" no recorte do subagente, e percorre a anatomia do arquivo, o isolamento de contexto, as ferramentas e as permissões, a ordem de escopo e o critério para escolher entre skill, subagente, skill com fork, hook, servidor MCP e arquivo de instrução.

## Workflow, agente e subagente

O guia [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) distingue o workflow, em que o código orquestra o modelo por um caminho predefinido, do agente, em que o próprio modelo decide os passos, e recomenda a solução mais simples possível, aumentando a autonomia somente quando o problema exige. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) define o subagente como um assistente especializado para o qual o Claude Code delega tarefas, com janela de contexto própria, prompt de sistema próprio, acesso restrito a ferramentas e permissões independentes. O agente principal delega quando a tarefa corresponde ao campo `description` do subagente, e o Claude Code exibe um aviso na inicialização quando as descrições de todos os subagentes somam mais de 15 mil tokens.

## Anatomia e front-matter do subagente

O subagente é um arquivo Markdown com frontmatter YAML, e o corpo do arquivo se torna o prompt de sistema dele. Apenas `name` e `description` são obrigatórios, e os nomes compostos usam camelCase, como `maxTurns` e `disallowedTools`. O campo precisa ter o nome exato da documentação, porque o Claude Code ignora sem reportar erro o campo que não reconhece.

```markdown
---
name: revisor-de-adr
description: Revisa registros de decisão arquitetural quanto a estrutura e consistência. Use depois de gerar ou editar um ADR.
tools: Read, Grep, Glob
model: haiku
maxTurns: 8
---

Você revisa um registro de decisão arquitetural. Leia o arquivo indicado,
liste as seções ausentes e aponte opções sem consequência declarada.
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

Cada subagente começa com uma janela de contexto nova, sem ver o histórico da conversa nem os arquivos já lidos, e o corpo do arquivo é o prompt de sistema dele. A saída volumosa, como a de uma suíte de testes, permanece no contexto do subagente, e apenas o resumo retorna à conversa principal. A documentação aponta esse efeito como o principal benefício, e o guia de custo recomenda delegar a subagentes a execução de testes, a busca em documentação e o processamento de logs. A skill carrega o procedimento na janela principal, e a skill com `context: fork` combina o procedimento fixo com o isolamento do subagente.

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

O log de depuração, o comando `/context` e o `claude plugin validate .claude/agents` mostram o que carregou e o que foi ignorado. O [Experimento D](oficina-de-ferramentas.md#experimento-d-localizar-front-matter-com-erro-no-log-de-depuracao) da oficina reproduz os três erros mais comuns e traz os comandos, e a página de [Custo de tokens](custo-de-tokens.md) reúne os comandos que mostram o que está carregado.

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

## Escolher o mecanismo

Um agente de codificação oferece seis mecanismos para guardar uma instrução, um procedimento ou uma restrição: o arquivo de instrução, a skill (um procedimento reutilizável escrito em Markdown), o subagente (um agente auxiliar com janela de contexto própria), a skill executada em contexto isolado com `context: fork`, o hook e o servidor MCP. A escolha entre eles segue seis perguntas, apresentadas em ordem na figura, e cada pergunta elimina uma opção antes de a seguinte ser feita.

![Árvore de decisão com seis perguntas em sequência. As perguntas 1 a 3 levam a servidor MCP, hook e arquivo de instrução. A pergunta 4 leva à pergunta 5, que separa skill com context: fork de subagente. A pergunta 6 separa skill de acionamento manual, com disable-model-invocation, de skill acionada pelo modelo.](assets/arvore-de-decisao-do-mecanismo.png)

### O que cada mecanismo muda

A tabela compara os seis mecanismos pelo momento em que entram no contexto, por quem os aciona e pelo que impõem ao agente.

| Mecanismo | Quando entra no contexto | Quem aciona | O que impõe |
|---|---|---|---|
| Arquivo de instrução (`AGENTS.md`, `CLAUDE.md`) | Em toda sessão, antes da primeira mensagem | Sempre ativo | Orientação que o agente pode seguir ou ignorar |
| Skill | Nome e descrição sempre, corpo somente ao acionar | O modelo pela `description` ou a pessoa pelo nome | Procedimento reutilizável, com permissões ajustáveis por campos do front-matter |
| Subagente | Contexto próprio, e só o resumo volta à conversa | O modelo pela `description` ou a pessoa | Ferramentas, modelo e permissões próprios |
| Skill com `context: fork` | Roda em subagente, sem o histórico da conversa | A pessoa ou o modelo | O procedimento da skill dentro do isolamento do subagente |
| Hook | Fora do contexto, na camada de execução | O evento configurado, como antes ou depois de uma ferramenta | Bloqueio, registro ou confirmação verificados por programa |
| Servidor MCP | Ferramentas, recursos e prompts declarados ao agente | O modelo, conforme a primitiva | Acesso a sistema ou dado externo |

O arquivo de instrução e a skill orientam o agente, que pode seguir ou ignorar o texto, e o hook roda na camada de execução e consegue bloquear a ação. A [Sessão 2](../sessao-02-ambiente-agentico/autonomia-e-supervisao.md) detalha a diferença de força entre o arquivo de instrução e o hook, e a página [MCP e ferramentas externas](../sessao-02-ambiente-agentico/mcp.md) trata da integração com sistemas externos.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as skills ficam em `.claude/skills/` ([documentação das skills](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao)) e os subagentes em `.claude/agents/` ([documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao)).
    **Codex CLI:** as skills ficam em `.agents/skills/` ([Build skills](../referencia/bibliografia.md#openai-codex-build-skills-documentacao)), com a descoberta observada na versão 0.140.0, e os subagentes são arquivos TOML em `.codex/agents/` ([Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao)), formato documentado e ainda sem execução observada.

### Skill, subagente ou agente principal

As formas diferem em onde o trabalho acontece: a skill carrega o procedimento na conversa principal, e o subagente executa em janela própria e devolve apenas o resumo. A escolha depende do volume da saída, das permissões necessárias e de quem deve acionar o procedimento, e a tabela transforma cada fator numa pergunta.

| Pergunta | Se a resposta é sim | Evidência |
|---|---|---|
| A saída intermediária é grande e a conversa não precisa lê-la? | Subagente, ou skill com `context: fork` | Documentado: o subagente tem contexto próprio e só o resumo retorna |
| A tarefa precisa de menos ferramentas que a conversa? | Subagente com `tools`, ou skill com `disallowed-tools` enquanto o procedimento durar | Observado: `tools` impediu a edição, e `disallowed-tools` bloqueou a escrita |
| A tarefa precisa de um modelo diferente do da conversa? | Subagente com `model`, ou skill com `model`, que vale só no turno | Documentado |
| O procedimento se repete e deve sair igual para todos? | Skill | Documentado: o procedimento carrega sob demanda e fica versionado |
| A pessoa precisa decidir o momento de acionar? | Skill com `disable-model-invocation: true` | Observado: o pedido em linguagem natural não acionou a skill, e a chamada pelo nome funcionou |
| As partes são independentes e o valor justifica o custo? | Vários subagentes em paralelo | Documentado: reduz o tempo, ao preço de mais tokens |
| A tarefa é curta ou depende de decisões da pessoa a cada passo? | Agente principal | Documentado: delegar acrescenta custo sem benefício |
| A mesma definição precisa valer no Claude Code e no Codex CLI? | Skill, que segue o padrão aberto Agent Skills nas duas ferramentas | Documentado: o subagente tem formato diferente em cada uma, Markdown e TOML |

O isolamento reduz o contexto da conversa principal e soma o consumo de cada janela, razão pela qual a delegação compensa quando a saída intermediária é grande ou quando a tarefa precisa de menos ferramentas que a conversa. A seção [Quando usar vários agentes](#quando-usar-varios-agentes) reúne os números de custo de sistemas com vários agentes.

### Quando usar fork

A skill com `context: fork` combina o procedimento fixo de uma skill com o isolamento de um subagente: o conteúdo da skill vira o prompt de um subagente que não enxerga o histórico da conversa, e o campo `agent` escolhe o tipo desse subagente. A combinação serve a tarefas recorrentes de saída volumosa, como rodar uma suíte de testes e relatar só as falhas, em que a pessoa quer o mesmo roteiro a cada uso e uma conversa principal limpa.

O custo da combinação é a ausência do histórico. Na observação, a skill bifurcada respondeu que não via mensagens anteriores da conversa, e por isso tudo o que a tarefa precisa deve chegar pelos argumentos ou pelo corpo da skill.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os campos `context: fork` e `agent` constam da [documentação das skills](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), e a skill bifurcada foi observada na versão 2.1.309.
    **Codex CLI:** a documentação lida não traz equivalente de `context: fork` para skills, item sem confirmação, e os subagentes do Codex são acionados por pedido em linguagem natural, conforme a [documentação de Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao).

### Hook, MCP e arquivo de instrução

Os três mecanismos restantes cobrem necessidades que skill e subagente não atendem. O arquivo de instrução guarda a orientação que vale para toda sessão do projeto, e a página [O arquivo de instrução](../sessao-02-ambiente-agentico/arquivo-de-instrucao.md) aplica a régua de que uma linha só entra no arquivo se mudar uma decisão do agente. O hook entra quando a regra precisa ser cumprida mesmo que o agente decida ignorá-la, porque a verificação ocorre fora do modelo. O servidor MCP entra quando falta ao agente uma ferramenta ou um dado externo.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a Sessão 2 apresenta os hooks como pontos de interceptação antes e depois da execução de uma ferramenta, na página [Autonomia e supervisão](../sessao-02-ambiente-agentico/autonomia-e-supervisao.md).
    **Codex CLI:** os hooks aparecem como recurso estável e ativo em `codex features list`, observado na versão 0.140.0, e a [documentação do AGENTS.md](../referencia/bibliografia.md#openai-codex-agentsmd-documentacao) informa a precedência dos arquivos da raiz do projeto até o diretório atual e o limite padrão de 32 KiB.

### Antipadrões

| Antipadrão | Sintoma | Correção |
|---|---|---|
| Skill enciclopédica | O corpo ultrapassa o limite recomendado de 5 mil tokens e o procedimento se dilui entre exceções | Mover referências e scripts para o terceiro nível de carga, que só consome tokens quando acessado |
| Subagente por cargo | Subagentes chamados analista, desenvolvedor e testador, criados para espelhar o organograma sem que a tarefa peça contexto isolado, ferramentas restritas ou modelo próprio | Criar subagente somente quando a pergunta 4 da árvore tiver resposta afirmativa. A origem é o [princípio de simplicidade](../sessao-01-o-que-mudou/sistemas-agenticos.md#o-principio-de-simplicidade), e a aplicação ao caso é inferência deste material |
| Vários agentes sem necessidade | Partes dependentes entre si, divididas entre agentes que precisam do mesmo contexto | Manter um agente e, se necessário, adicionar subagentes de leitura. A [aritmética do erro composto](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) mostra que cada etapa acrescentada multiplica a chance de falha |

!!! abstract "Linha da ficha"
    Mecanismo, e arquivo e front-matter do subagente:

    - Qual mecanismo atende a tarefa: skill, subagente, skill com fork, hook, servidor MCP ou arquivo de instrução?
    - Que ferramentas e que modo de permissão o subagente declara, e o `tools` está escrito sem erro de grafia?
    - Em que escopo o arquivo fica e quem o aciona, a pessoa ou o modelo pela `description`?

**Próxima página:** [Geração de artefatos](geracao-de-artefatos.md).
