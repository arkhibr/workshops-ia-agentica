# Agentes e subagentes

Um agente executa uma tarefa em várias etapas, decidindo por conta própria quais ferramentas chamar, e um subagente é um agente auxiliar que recebe uma parte do trabalho num contexto separado. Esta página descreve a anatomia de um subagente do Claude Code, o que o isolamento de contexto muda e os critérios para decidir entre skill, subagente e vários agentes.

## Workflow, agente e subagente

O guia [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) distingue o workflow, em que o código orquestra o modelo por um caminho predefinido, do agente, em que o próprio modelo decide os passos, e recomenda a solução mais simples possível, aumentando a autonomia somente quando o problema exige. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) define o subagente como um assistente especializado para o qual o Claude Code delega tarefas, com janela de contexto própria, prompt de sistema próprio, acesso restrito a ferramentas e permissões independentes. O agente principal delega quando a tarefa corresponde ao campo `description` do subagente, e o Claude Code exibe um aviso na inicialização quando as descrições de todos os subagentes somam mais de 15 mil tokens.

## Anatomia de um subagente

O subagente é um arquivo Markdown com frontmatter YAML, e o corpo do arquivo se torna o prompt de sistema dele. Apenas `name` e `description` são obrigatórios.

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

| Campo | Função |
|---|---|
| `name` | Identificador único, obrigatório |
| `description` | Diz ao agente principal quando delegar, obrigatório |
| `tools` | Lista de ferramentas permitidas. Se omitido, o subagente herda todas as disponíveis |
| `disallowedTools` | Lista de ferramentas negadas, aplicada antes de `tools` |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, um identificador completo ou `inherit` |
| `permissionMode` | Modo de permissão, como `default`, `acceptEdits`, `plan` ou `bypassPermissions` |
| `maxTurns` | Número máximo de turnos antes de o subagente parar |
| `skills` | Skills carregadas no contexto na inicialização |

Duas regras da documentação pedem atenção na escrita. O Claude Code ignora em silêncio os campos de frontmatter que não reconhece, e o campo `tools` omitido faz o subagente herdar todas as ferramentas. A combinação indica que um campo de restrição escrito com erro de grafia deixa o subagente com acesso total, e o teste da oficina confirmou o efeito na versão 2.1.309 do Claude Code: o subagente com `tool` no lugar de `tools` carregou e editou o arquivo, e o log de depuração registrou o campo desconhecido com a sugestão `tools`. Os campos que esta tabela não cobre, a ordem de escopo e a resolução do `model` estão em [Front-matter de subagentes](front-matter-de-subagentes.md).

Os subagentes ficam em `.claude/agents/` quando pertencem ao projeto e em `~/.claude/agents/` quando são pessoais. Em caso de nome repetido, vale o local de maior prioridade, na ordem: configurações gerenciadas da organização, a opção `--agents` da sessão, o projeto, o diretório pessoal e os plugins.

## O que o isolamento de contexto muda

Cada subagente começa com uma janela de contexto nova, sem ver o histórico da conversa nem os arquivos já lidos. A saída volumosa, como a de uma suíte de testes, permanece no contexto do subagente, e apenas o resumo retorna à conversa principal. A documentação aponta esse efeito como o principal benefício, e o guia de custo recomenda delegar a subagentes a execução de testes, a busca em documentação e o processamento de logs.

Os pedidos de um subagente contam para os mesmos limites de uso da conversa principal. O isolamento reduz o tamanho do contexto da conversa principal, mas não reduz o consumo total de tokens, que costuma aumentar pela soma dos contextos.

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

## Skill, subagente ou agente principal

| Situação | Mecanismo | Razão |
|---|---|---|
| A tarefa se repete e tem procedimento conhecido | Skill | O procedimento carrega sob demanda e fica versionado |
| A tarefa produz muita saída intermediária que a conversa não precisa ler | Subagente | Só o resumo retorna ao contexto principal |
| A tarefa precisa de permissões menores que as da conversa | Subagente com `tools` restrito | A restrição vale só para aquela delegação |
| A tarefa precisa de um modelo mais barato ou mais forte que o da conversa | Subagente com `model` próprio | O modelo é escolhido por delegação |
| As partes são independentes e o valor justifica o custo | Vários subagentes em paralelo | Reduz o tempo, ao preço de mais tokens |
| A tarefa é curta ou depende de decisões da pessoa a cada passo | Agente principal | Delegar acrescenta custo sem benefício |

**Próxima página:** [Geração de artefatos](geracao-de-artefatos.md).
