# Escolher o mecanismo

Um agente de codificação oferece seis mecanismos para guardar uma instrução, um procedimento ou uma restrição: o arquivo de instrução, a skill (um procedimento reutilizável escrito em Markdown), o subagente (um agente auxiliar com janela de contexto própria), a skill executada em contexto isolado com `context: fork`, o hook e o servidor MCP. A escolha entre eles segue seis perguntas, apresentadas em ordem na figura, e cada pergunta elimina uma opção antes de a seguinte ser feita.

![Árvore de decisão com seis perguntas em sequência. As perguntas 1 a 3 levam a servidor MCP, hook e arquivo de instrução. A pergunta 4 leva à pergunta 5, que separa skill com context: fork de subagente. A pergunta 6 separa skill de acionamento manual, com disable-model-invocation, de skill acionada pelo modelo.](assets/arvore-de-decisao-do-mecanismo.png)

!!! info "Versões verificadas"
    As observações desta página foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e cada afirmação indica se foi observada, se vem da documentação ou se continua sem confirmação. A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`, e o comportamento pode divergir em versões diferentes das citadas.

## O que cada mecanismo muda

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

## Skill ou subagente

As duas formas diferem em onde o trabalho acontece: a skill carrega o procedimento na conversa principal, e o subagente executa em janela própria e devolve apenas o resumo. A escolha depende do volume da saída, das permissões necessárias e de quem deve acionar o procedimento, e a tabela transforma cada fator numa pergunta.

| Pergunta | Se a resposta é sim | Evidência |
|---|---|---|
| A saída intermediária é grande e a conversa não precisa lê-la? | Subagente, ou skill com `context: fork` | Documentado: o subagente tem contexto próprio e só o resumo retorna |
| A tarefa precisa de menos ferramentas que a conversa? | Subagente com `tools`, ou skill com `disallowed-tools` enquanto o procedimento durar | Observado: `tools` impediu a edição, e `disallowed-tools` bloqueou a escrita |
| A tarefa precisa de um modelo diferente do da conversa? | Subagente com `model`, ou skill com `model`, que vale só no turno | Documentado |
| O procedimento se repete e deve sair igual para todos? | Skill | Documentado |
| A pessoa precisa decidir o momento de acionar? | Skill com `disable-model-invocation: true` | Observado: o pedido em linguagem natural não acionou a skill, e a chamada pelo nome funcionou |
| A mesma definição precisa valer no Claude Code e no Codex CLI? | Skill, que segue o padrão aberto Agent Skills nas duas ferramentas | Documentado: o subagente tem formato diferente em cada uma, Markdown e TOML |

O isolamento reduz o contexto da conversa principal e soma o consumo de cada janela, razão pela qual a delegação compensa quando a saída intermediária é grande ou quando a tarefa precisa de menos ferramentas que a conversa. A página [Agentes e subagentes](agentes-e-subagentes.md#quando-usar-varios-agentes) reúne os números de custo de sistemas com vários agentes.

## Quando usar fork

A skill com `context: fork` combina o procedimento fixo de uma skill com o isolamento de um subagente: o conteúdo da skill vira o prompt de um subagente que não enxerga o histórico da conversa, e o campo `agent` escolhe o tipo desse subagente. A combinação serve a tarefas recorrentes de saída volumosa, como rodar uma suíte de testes e relatar só as falhas, em que a pessoa quer o mesmo roteiro a cada uso e uma conversa principal limpa.

O custo da combinação é a ausência do histórico. Na observação, a skill bifurcada respondeu que não via mensagens anteriores da conversa, e por isso tudo o que a tarefa precisa deve chegar pelos argumentos ou pelo corpo da skill.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os campos `context: fork` e `agent` constam da [documentação das skills](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), e a skill bifurcada foi observada na versão 2.1.309.
    **Codex CLI:** a documentação lida não traz equivalente de `context: fork` para skills, item sem confirmação, e os subagentes do Codex são acionados por pedido em linguagem natural, conforme a [documentação de Subagents](../referencia/bibliografia.md#openai-codex-subagents-documentacao).

## Hook, MCP e arquivo de instrução

Os três mecanismos restantes cobrem necessidades que skill e subagente não atendem. O arquivo de instrução guarda a orientação que vale para toda sessão do projeto, e a página [O arquivo de instrução](../sessao-02-ambiente-agentico/arquivo-de-instrucao.md) aplica a régua de que uma linha só entra no arquivo se mudar uma decisão do agente. O hook entra quando a regra precisa ser cumprida mesmo que o agente decida ignorá-la, porque a verificação ocorre fora do modelo. O servidor MCP entra quando falta ao agente uma ferramenta ou um dado externo.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a Sessão 2 apresenta os hooks como pontos de interceptação antes e depois da execução de uma ferramenta, na página [Autonomia e supervisão](../sessao-02-ambiente-agentico/autonomia-e-supervisao.md).
    **Codex CLI:** os hooks aparecem como recurso estável e ativo em `codex features list`, observado na versão 0.140.0, e a [documentação do AGENTS.md](../referencia/bibliografia.md#openai-codex-agentsmd-documentacao) informa a precedência dos arquivos da raiz do projeto até o diretório atual e o limite padrão de 32 KiB.

## Antipadrões

| Antipadrão | Sintoma | Correção |
|---|---|---|
| Skill enciclopédica | O corpo ultrapassa o limite recomendado de 5 mil tokens e o procedimento se dilui entre exceções | Mover referências e scripts para o terceiro nível de carga, que só consome tokens quando acessado |
| Subagente por cargo | Subagentes chamados analista, desenvolvedor e testador, criados para espelhar o organograma sem que a tarefa peça contexto isolado, ferramentas restritas ou modelo próprio | Criar subagente somente quando a pergunta 4 da árvore tiver resposta afirmativa. A origem é o [princípio de simplicidade](../sessao-01-o-que-mudou/sistemas-agenticos.md#o-principio-de-simplicidade), e a aplicação ao caso é inferência deste material |
| Vários agentes sem necessidade | Partes dependentes entre si, divididas entre agentes que precisam do mesmo contexto | Manter um agente e, se necessário, adicionar subagentes de leitura. A [aritmética do erro composto](../sessao-02-ambiente-agentico/arnes.md#a-aritmetica-do-erro-composto) mostra que cada etapa acrescentada multiplica a chance de falha |

**Próxima página:** [Front-matter de skills](front-matter-de-skills.md).
