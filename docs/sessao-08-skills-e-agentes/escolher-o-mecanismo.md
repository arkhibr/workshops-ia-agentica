# Escolher o mecanismo

Um agente de codificação oferece seis mecanismos para guardar uma instrução, um procedimento ou uma restrição: o arquivo de instrução, a skill (um procedimento reutilizável escrito em Markdown), o subagente (um agente auxiliar com janela de contexto própria), a skill executada em contexto isolado com `context: fork`, o hook e o servidor MCP. Esta página reúne os critérios da escolha, compara skill, subagente e agente principal dimensão por dimensão e lista os antipadrões. Ela preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Mecanismo".

## Skill com fork ou subagente: qual é a diferença?

Uma **skill** guarda um procedimento reutilizável: o que fazer, em que ordem e como entregar o resultado. Um **subagente personalizado** configura um especialista: seu papel, suas instruções e, quando necessário, suas ferramentas e seu modelo.

A skill pode rodar na conversa principal ou em um subagente. Com `context: fork`, o Claude Code inicia um subagente em contexto separado e entrega a ele as instruções da skill. Por isso, os dois caminhos usam um subagente; a diferença é se o ponto de partida é **um procedimento a executar** ou **um especialista para receber uma tarefa**.

### Exemplo: analisar uma reunião

A equipe quer identificar tarefas e riscos numa transcrição. Ela cria a skill `.claude/skills/analisar-reuniao/SKILL.md`:

```markdown
---
name: analisar-reuniao
description: Identifica tarefas e riscos em transcrições de reunião.
context: fork
agent: general-purpose
---
Leia a transcrição indicada em $ARGUMENTS.
Liste tarefas e riscos, cite os trechos que sustentam cada item e marque
responsáveis ou prazos ausentes como "A confirmar".
```

A chamada `/analisar-reuniao reuniao.md` envia a receita e o caminho da transcrição ao subagente. Ele executa o procedimento em sua própria janela e devolve o resultado à conversa principal. O mesmo procedimento pode ser usado com outras transcrições.

Agora a equipe quer um **revisor** que receba diferentes pedidos: conferir um relatório, verificar uma correção ou comparar versões. Ela define `.claude/agents/revisor-reuniao.md`:

```markdown
---
name: revisor-reuniao
description: Revisa relatórios de reunião em relação à transcrição.
tools: Read, Grep, Glob
---
Você revisa relatórios de reunião. Compare os documentos indicados,
aponte omissões e informações sem evidência e não edite arquivos.
```

A pessoa pode pedir: “Use o revisor-reuniao para comparar `relatorio.md` com `reuniao.md`”. O agente principal delega esse pedido ao revisor, que trabalha em contexto separado e devolve seus achados. Em outro pedido, o mesmo revisor pode conferir se as correções resolveram os problemas.

| Pergunta | Skill com `context: fork` | Subagente personalizado |
|---|---|---|
| O que fica definido? | O procedimento de análise | O papel e a configuração do especialista |
| O que recebe em cada uso? | Os dados necessários ao procedimento, como o caminho da transcrição | Uma tarefa específica, como revisar ou comparar documentos |
| Quem executa? | Um subagente que recebe o conteúdo da skill | O subagente definido no arquivo de agente |
| Onde executa? | Em contexto separado | Em contexto separado |
| O que volta à conversa? | O resultado da execução | O resultado da tarefa delegada |

Escolha uma **skill com fork** quando quiser repetir um procedimento e manter o trabalho intermediário fora da conversa. Escolha um **subagente personalizado** quando quiser reutilizar um especialista, com ferramentas ou modelo próprios, para diferentes tarefas. Isso é uma orientação, não uma fronteira rígida: uma skill pode deixar decisões em aberto e um subagente pode seguir passos fixos.

A equipe também pode usar os dois juntos: a skill gera o relatório e o subagente revisor compara o resultado com a transcrição. Em qualquer dos casos, informe os caminhos e o contexto necessários no pedido: o subagente não recebe automaticamente o histórico da conversa. Contexto separado não garante acesso somente de leitura; para isso, configure ferramentas e permissões, como `tools: Read, Grep, Glob` no exemplo do revisor.

## A árvore de seis perguntas

A escolha entre os seis mecanismos segue seis perguntas, apresentadas em ordem na figura, e cada pergunta elimina uma opção antes de a seguinte ser feita.

![Árvore de decisão com seis perguntas em sequência. As perguntas 1 a 3 levam a servidor MCP, hook e arquivo de instrução. A pergunta 4 leva à pergunta 5, que separa skill com context: fork de subagente. A pergunta 6 separa skill de acionamento manual, com disable-model-invocation, de skill acionada pelo modelo.](assets/arvore-de-decisao-do-mecanismo.png)

A tabela seguinte explica cada pergunta e o que a resposta elimina.

| Pergunta | Resposta sim | Resposta não |
|---|---|---|
| 1. A tarefa exige ferramenta ou dado externo que o agente ainda não tem? | Servidor MCP, que declara ao agente as ferramentas e os recursos do sistema externo | Segue para a pergunta 2 |
| 2. A regra precisa valer mesmo que o agente decida ignorá-la? | Hook, porque a verificação ocorre na camada de execução, fora do modelo | Segue para a pergunta 3 |
| 3. A orientação vale para toda sessão do projeto, qualquer que seja a tarefa? | Arquivo de instrução (`AGENTS.md` ou `CLAUDE.md`), carregado em toda sessão | Segue para a pergunta 4 |
| 4. A saída é volumosa ou a tarefa pede ferramentas e permissões próprias? | Segue para a pergunta 5, porque o isolamento de um subagente se justifica | Segue para a pergunta 6, porque não há razão para isolar |
| 5. O foco é reutilizar um procedimento em contexto separado? | Comece com uma skill com `context: fork` | Considere um subagente personalizado para receber tarefas de um mesmo papel |
| 6. A pessoa deve decidir o momento de acionar o procedimento? | Skill de acionamento manual, com `disable-model-invocation: true` | Skill acionada pelo modelo pela `description` |

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

As três formas diferem em onde o trabalho acontece: o agente principal trabalha na própria conversa, a skill carrega um procedimento nessa conversa e o subagente executa em janela própria e devolve apenas o resumo. A tabela compara as três por dimensão, e os valores marcados como documentados vêm da [documentação das skills](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao) e da [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao).

| Dimensão | Agente principal | Skill | Subagente |
|---|---|---|---|
| Onde o trabalho acontece | Na conversa da sessão | Na conversa, ou num subagente quando a skill declara `context: fork` | Na janela de contexto própria do subagente |
| O que entra no contexto | O histórico completo | O corpo do `SKILL.md` entra como uma mensagem e permanece nos turnos seguintes | O corpo do arquivo, como prompt de sistema, e a mensagem de delegação do agente principal |
| O que volta à conversa | Tudo o que o agente produz | O resultado fica na conversa | Apenas o resumo do subagente |
| Quem aciona | A pessoa, a cada mensagem | A pessoa pelo nome e o modelo pela `description`, conforme `disable-model-invocation` e `user-invocable` | O modelo pela `description`, ou a pessoa por pedido |
| Ferramentas | Todas as da sessão | As da sessão, com `allowed-tools` para liberar e `disallowed-tools` para remover durante o turno | `tools` e `disallowedTools`, e todas as ferramentas disponíveis quando `tools` é omitido |
| Modelo | O da sessão | `model` e `effort` valem só no turno da skill | `model` próprio, resolvido pela ordem descrita em [Escolha de modelos](escolha-de-modelos.md#resolucao-do-model-por-subagente-e-por-skill) |
| Permissões | O modo da sessão | O modo da sessão, mais a liberação de `allowed-tools` no turno | `permissionMode` próprio, descrito em [Agentes e subagentes](agentes-e-subagentes.md#o-permissionmode) |
| Custo de tokens | Os tokens da conversa, que crescem com a saída intermediária | Cerca de 100 tokens por skill na listagem e, ao acionar, um corpo abaixo de 5 mil tokens | A soma do consumo de cada janela, em troca de uma conversa principal menor |
| Depois da compactação | O resumo da conversa | O Claude Code reanexa os primeiros 5 mil tokens da última invocação de cada skill, num orçamento combinado de 25 mil | Não se aplica, porque o contexto do subagente termina com o resumo |
| Onde o arquivo fica | Não se aplica | `.claude/skills/`, formato aberto Agent Skills, igual no Codex CLI | `.claude/agents/` em Markdown e `.codex/agents/` em TOML |
| Falha típica | A conversa enche de saída que ninguém lê | A skill não aciona, ou aciona em excesso | O subagente herda ferramentas por erro de grafia em `tools` |

O isolamento reduz o contexto da conversa principal e soma o consumo de cada janela, razão pela qual a delegação compensa quando a saída intermediária é grande ou quando a tarefa precisa de menos ferramentas que a conversa. A seção [Quando usar vários agentes](agentes-e-subagentes.md#quando-usar-varios-agentes) reúne os números de custo de sistemas com vários agentes.

#### As oito perguntas e os sinais contrários

A tabela transforma cada fator da escolha numa pergunta, indica a evidência da resposta afirmativa e acrescenta o sinal que inverte a decisão. A coluna de sinal contrário é inferência deste material e não consta da documentação.

| Pergunta | Se a resposta é sim | Evidência | Sinal contrário |
|---|---|---|---|
| A saída intermediária é grande e a conversa não precisa lê-la? | Subagente, ou skill com `context: fork` | Documentado: o subagente tem contexto próprio e só o resumo retorna | A conversa precisa dos trechos da saída para decidir o passo seguinte, e o resumo perderia o que importa. Fica o agente principal |
| A tarefa precisa de menos ferramentas que a conversa? | Subagente com `tools`, ou skill com `disallowed-tools` enquanto o procedimento durar | Observado: `tools` impediu a edição, e `disallowed-tools` bloqueou a escrita | A restrição precisa valer na sessão inteira ou contra a vontade do agente. Fica um hook ou uma regra de negação nas configurações de permissão |
| A tarefa precisa de um modelo diferente do da conversa? | Subagente com `model`, ou skill com `model`, que vale só no turno | Documentado | A diferença de preço é pequena diante de uma tarefa curta. A configuração extra não se paga |
| O procedimento se repete e deve sair igual para todos? | Skill | Documentado: o procedimento carrega sob demanda e fica versionado | A tarefa ocorre uma só vez. Fica o pedido avulso |
| A pessoa precisa decidir o momento de acionar? | Skill com `disable-model-invocation: true` | Observado: o pedido em linguagem natural não acionou a skill, e a chamada pelo nome funcionou | O procedimento deve ocorrer sempre que o assunto surgir. Fica a skill acionada pelo modelo, com uma `description` precisa |
| As partes são independentes e o valor justifica o custo? | Vários subagentes em paralelo | Documentado: reduz o tempo, ao preço de mais tokens | As partes dependem do mesmo contexto. Fica um agente, com subagentes só de leitura |
| A tarefa é curta ou depende de decisões da pessoa a cada passo? | Agente principal | Documentado: delegar acrescenta custo sem benefício | A saída intermediária cresce a ponto de poluir a conversa. Passa a valer a primeira pergunta |
| A mesma definição precisa valer no Claude Code e no Codex CLI? | Skill, que segue o padrão aberto Agent Skills nas duas ferramentas | Documentado: o subagente tem formato diferente em cada uma, Markdown e TOML | A tarefa exige ferramentas ou modelo próprios. Fica um subagente com um arquivo para cada ferramenta |

#### Situações típicas e o mecanismo indicado

A tabela aplica as perguntas a tarefas comuns de uma equipe de desenvolvimento. A escolha de cada linha é a indicada pelos critérios acima e não resulta de medição.

| Tarefa | Mecanismo | Razão |
|---|---|---|
| Rodar a suíte de testes e relatar só as falhas, do mesmo modo a cada vez | Skill com `context: fork` | A saída é volumosa, e o roteiro é fixo |
| Investigar um módulo desconhecido para responder a uma pergunta | Subagente `Explore`, que é um tipo embutido com ferramentas de leitura | A exploração gera muita saída intermediária, e o resumo basta |
| Revisar um arquivo sem poder editá-lo | Subagente com `tools: Read, Grep, Glob` | A restrição de ferramentas é o requisito |
| Gerar um documento no formato fixo da equipe, com conferência por script | Skill | O procedimento se repete e o artefato tem estrutura verificável |
| Fazer o commit com a mensagem no padrão, quando a pessoa decidir | Skill com `disable-model-invocation: true` e `allowed-tools` limitado aos comandos de git | A pessoa escolhe o momento, e o efeito é uma mudança no repositório |
| Corrigir um defeito que depende do que a pessoa decidiu nos turnos anteriores | Agente principal | O histórico da conversa é a entrada da tarefa |
| Alterar uma linha de um arquivo | Agente principal | A delegação custaria mais que a tarefa |
| Impedir qualquer edição nos arquivos de migração do banco | Hook | A regra precisa valer ainda que o agente a ignore |
| Consultar o sistema de chamados da equipe | Servidor MCP | Falta ao agente o acesso a um sistema externo |
| Registrar a convenção de nomes do projeto | Arquivo de instrução | A orientação vale para toda sessão |

#### Como skill e subagente se combinam

Skill e subagente combinam-se de duas maneiras, e a diferença está em quem escreve a tarefa e em quem fornece o prompt de sistema.

| Combinação | Prompt de sistema | Tarefa | Também carrega |
|---|---|---|---|
| Skill com `context: fork` | Do tipo de agente escolhido em `agent` | O conteúdo do `SKILL.md` | O `CLAUDE.md`, conforme o contexto de inicialização do agente |
| Subagente com o campo `skills` | O corpo do arquivo do subagente | A mensagem de delegação do agente principal | As skills pré-carregadas e o `CLAUDE.md` |

Na primeira combinação, a pessoa escreve a tarefa na skill e escolhe o tipo de agente que a executa. Na segunda, a pessoa define um subagente que usa skills como material de referência. Uma skill com `disable-model-invocation: true` não pode ser pré-carregada num subagente, e os subagentes embutidos `Explore` e `Plan` começam sem o `CLAUDE.md`, de modo que o `SKILL.md` de um `fork` com esses tipos precisa conter tudo o que a tarefa exige.

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
| Fork sem tarefa | Uma skill com `context: fork` que traz só diretrizes, como convenções de API, e nenhuma tarefa, de modo que o subagente retorna sem produzir resultado útil | Reservar o `fork` a skills com instruções explícitas de tarefa, e deixar as diretrizes numa skill comum ou no arquivo de instrução |
| Skill para tarefa única | Uma pasta de skill criada para um pedido que não se repetirá | Fazer o pedido avulso e criar a skill só quando a tarefa se repetir |
| Vários agentes sem necessidade | Partes dependentes entre si, divididas entre agentes que precisam do mesmo contexto | Manter um agente e, se necessário, adicionar subagentes de leitura. A [aritmética do erro composto](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) mostra que cada etapa acrescentada multiplica a chance de falha |

!!! abstract "Linha da ficha"
    Mecanismo:

    - Qual mecanismo atende a tarefa: skill, subagente, skill com fork, hook, servidor MCP ou arquivo de instrução?
    - Que pergunta da árvore elimina cada alternativa descartada?
    - O sinal contrário da escolha está ausente, ou a tarefa pede outro mecanismo?

**Próxima página:** [Geração de artefatos](geracao-de-artefatos.md).
