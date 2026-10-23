# Front-matter de skills

O front-matter de uma skill é o bloco YAML entre dois marcadores `---` no início do arquivo `SKILL.md`, e define como o agente descobre a skill, quando a aciona e que permissões ela concede. Uma skill é um procedimento reutilizável escrito em Markdown e guardado numa pasta própria, e esta página separa os campos que valem em qualquer ferramenta dos campos exclusivos do Claude Code, com o efeito de cada um.

!!! info "Versões verificadas"
    As observações desta página foram feitas em 23/10/2026 com `claude 2.1.309` e `codex-cli 0.140.0`, e cada afirmação indica se foi observada, se vem da documentação ou se continua sem confirmação. A versão instalada em cada máquina aparece nos comandos `claude --version` e `codex --version`, e o comportamento pode divergir em versões diferentes das citadas.

![Um arquivo SKILL.md com front-matter em que name e description aparecem em verde como núcleo portátil, allowed-tools em cinza como campo da especificação aberta e when_to_use, disable-model-invocation, context, agent e o marcador $ARGUMENTS em laranja como específicos do Claude Code. À direita, uma anotação curta explica o efeito de cada campo.](assets/skill-anotada-nucleo-portatil.png)

## Núcleo portátil

A [especificação aberta Agent Skills](../referencia/bibliografia.md#agent-skills-especificacao-aberta) define o formato mínimo de uma skill, e a documentação do Codex CLI declara seguir esse padrão. Dois campos formam o núcleo: `name` e `description`, e uma skill que usa só esses dois funciona nas duas ferramentas.

| Campo | Regra na especificação aberta | No Claude Code |
|---|---|---|
| `name` | Obrigatório, de 1 a 64 caracteres, com letras minúsculas, números e hifens, sem hífen no início, no fim ou repetido, e igual ao nome do diretório | Opcional, e o padrão é o nome do diretório. A tabela de campos do Claude Code não repete as regras de tamanho e de caracteres |
| `description` | Obrigatório, de 1 a 1.024 caracteres | Recomendado. Se faltar, vale a primeira linha não vazia do corpo, e a listagem corta `description` e `when_to_use` somados em 1.536 caracteres |

O Claude Code só lê o front-matter quando o primeiro `---` está na primeira linha do arquivo, e trata o arquivo inteiro como conteúdo da skill em qualquer outro caso. Se o YAML entre os marcadores não for válido, a skill carrega sem nenhum campo, e a página de depuração de skills e agentes do aprofundamento mostra como localizar o erro. As regras de nome com palavras reservadas e o limite de 64 caracteres que a página [Skills](skills.md#anatomia-de-uma-skill) cita vêm da documentação de skills da plataforma Claude, usada na API e no claude.ai.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as skills ficam em `.claude/skills/<nome>/SKILL.md`, e a [tabela de campos](https://code.claude.com/docs/en/skills#frontmatter-reference) lista cada campo aceito.
    **Codex CLI:** as skills ficam em `.agents/skills/<nome>/SKILL.md`, com `name` e `description` obrigatórios segundo a [documentação de Build skills](https://learn.chatgpt.com/docs/build-skills), e a descoberta da skill foi observada na versão 0.140.0 pelo comando `codex debug prompt-input`.

## Campos do Claude Code

Todos os campos são opcionais no Claude Code, e os nomes usam letras minúsculas separadas por hifens, com a exceção de `when_to_use`. Um campo precisa ter o nome exato da tabela, e o Claude Code ignora sem reportar erro o campo que não reconhece, segundo a documentação. Os campos booleanos aceitam `true` e `false`, e também `yes`, `no`, `on`, `off`, `1` e `0` a partir da v2.1.218.

| Campo | Efeito | Padrão |
|---|---|---|
| `when_to_use` | Pistas de acionamento, somadas à `description` na listagem e ao mesmo corte de 1.536 caracteres | Nenhum |
| `argument-hint` | Texto de ajuda no autocompletar, como `[numero-da-issue]` | Nenhum |
| `arguments` | Nomes dos argumentos posicionais, usados como `$nome` no corpo | Nenhum |
| `disable-model-invocation` | Com `true`, o modelo não carrega a skill sozinha, e ela também não pode ser pré-carregada em subagentes | `false` |
| `user-invocable` | Com `false`, a skill sai do menu `/` e só o modelo a aciona | `true` |
| `allowed-tools` | Ferramentas liberadas sem pedir permissão no turno que invoca a skill | Nenhum |
| `disallowed-tools` | Ferramentas removidas do conjunto disponível enquanto a skill estiver ativa | Nenhum |
| `model` | Modelo usado durante o turno atual, sem gravar nas configurações | Herda a sessão |
| `effort` | Nível de esforço (`low`, `medium`, `high`, `xhigh`, `max`) durante a skill | Herda a sessão |
| `context` | Com `fork`, executa a skill em um subagente | Sem `fork` |
| `agent` | Tipo do subagente quando `context: fork` está ativo | `general-purpose` |
| `background` | Só com `context: fork`. Com `false`, espera o resultado do subagente no mesmo turno | `true` |
| `hooks` | Hooks registrados na invocação e mantidos até o fim da sessão | Nenhum |
| `paths` | Globs que limitam o carregamento automático aos arquivos correspondentes | Nenhum |
| `shell` | Shell dos blocos `` !`comando` ``, com `bash` ou `powershell` | `bash` |
| `metadata`, `license`, `compatibility` | Aceitos como dados da especificação aberta, sem efeito no comportamento do Claude Code | Nenhum |

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os campos acima constam da [tabela de campos](https://code.claude.com/docs/en/skills#frontmatter-reference), e `context: fork` e `agent` estão descritos em [Run skills in a subagent](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent).
    **Codex CLI:** o equivalente documentado de `disable-model-invocation` é `policy.allow_implicit_invocation: false` no arquivo `agents/openai.yaml`, com polaridade inversa, conforme [Build skills](https://learn.chatgpt.com/docs/build-skills). Os demais campos da tabela não têm equivalente confirmado no Codex.

## Liberar não é restringir

O nome `allowed-tools` sugere uma lista de ferramentas permitidas, e a documentação diz o contrário: o campo concede permissão para as ferramentas listadas durante o turno da skill, e todas as outras ferramentas continuam disponíveis, regidas pelas configurações de permissão. A restrição vem de `disallowed-tools`. A tabela resume o que se observou numa skill que pede a criação de um arquivo com a ferramenta `Write`.

| Skill | Modo de permissão | Resultado observado |
|---|---|---|
| Sem campo de ferramenta | `default` | Escrita negada por falta de permissão, arquivo não criado |
| `allowed-tools: Write` | `default` | Arquivo criado, porque a escrita foi liberada para o turno |
| `allowed-tools: Read` | `acceptEdits` | Arquivo criado, porque o campo não restringiu a escrita |
| `disallowed-tools: Write Edit Bash` | `acceptEdits` | Arquivo não criado, porque as ferramentas saíram do conjunto |

A observação veio de uma execução de cada variante com `claude 2.1.309` em modo não interativo, e a documentação acrescenta um aviso de segurança: o Claude Code aplica o `allowed-tools` de uma skill de projeto mesmo numa execução com `-p` em pasta nunca marcada como confiável. O `allowed-tools` de uma skill versionada em repositório alheio merece, por isso, a mesma revisão que um script recebido.

## Custo da description

Toda skill habilitada ocupa espaço na listagem de nomes e descrições carregada no início da sessão, e o orçamento dessa listagem é de 1% da janela de contexto do modelo. Cada entrada é cortada em 1.536 caracteres somando `description` e `when_to_use`, e a documentação recomenda colocar o caso de uso principal no começo. Quando a listagem estoura o orçamento, todo nome permanece, e as descrições saem primeiro das skills menos invocadas.

![Três caixas empilhadas mostram os níveis de carga de uma skill. O nível 1, metadados, entra na inicialização com cerca de 100 tokens por skill. O nível 2, instruções, entra quando a skill é acionada, com corpo abaixo de 5 mil tokens. O nível 3, recursos e scripts, entra sob demanda. Um painel à direita descreve o orçamento da listagem, o que acontece quando ele estoura, como ajustá-lo e como medi-lo.](assets/carga-em-tres-niveis-e-listagem.png)

O custo se mede com `/doctor`, que estima o custo da listagem, e com `/context`, que mostra o tamanho da listagem depois do orçamento. O comando `claude --debug` registra um aviso no log quando a listagem excede o orçamento, e os ajustes são a configuração `skillListingBudgetFraction`, a variável `SLASH_COMMAND_TOOL_CHAR_BUDGET` e o valor `"name-only"` em `skillOverrides`.

A `description` também decide o acionamento. Numa skill de nome neutro, `rotina-a7`, uma descrição específica, a descrição de uma palavra ("Chamados.") e uma descrição genérica ("Ajuda com várias tarefas da equipe.") acionaram a skill diante do pedido "Preciso do resumo semanal da fila de chamados.", e uma descrição sobre outro assunto não a acionou. Cada variante rodou uma vez, no modelo haiku, e com uma única skill disponível. Com várias skills concorrentes o resultado pode diferir, e a oficina propõe a medição com as skills da própria equipe.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** o orçamento e o corte constam de [Skill descriptions are cut short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short), e `/doctor`, `/context` e `claude --debug` são comandos do Claude Code.
    **Codex CLI:** a documentação informa orçamento de 2% da janela para a lista inicial de skills, e a execução da versão 0.140.0 registrou o aviso de que as descrições foram encurtadas para caber nesse orçamento. A fonte é [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Substituições e comandos no corpo

O corpo da skill aceita variáveis que o Claude Code substitui antes de enviar o texto ao modelo, e um bloco de injeção que executa um comando e insere a saída.

| Sintaxe | Substituição |
|---|---|
| `$ARGUMENTS` | Todos os argumentos da chamada. Sem placeholder no corpo, o Claude Code acrescenta `ARGUMENTS: <valor>` ao fim |
| `$ARGUMENTS[N]` ou `$N` | O argumento de índice N, contado a partir de 0 |
| `$nome` | O argumento declarado em `arguments`, na mesma ordem |
| `${CLAUDE_SKILL_DIR}` | O diretório do `SKILL.md`, útil para chamar scripts da própria skill |
| `` !`comando` `` | A saída do comando, executada antes de o texto chegar ao modelo |

A chamada `/args-demo alfa beta` de uma skill com `TODOS=[$ARGUMENTS] PRIMEIRO=[$0] SEGUNDO=[$1]` produziu `TODOS=[alfa beta] PRIMEIRO=[alfa] SEGUNDO=[beta]`, o que confirma a numeração a partir de 0. A injeção de comando precisa de permissão para a ferramenta de shell: sem `allowed-tools`, a execução registrou `Shell command permission check failed ... This command requires approval` e o texto não foi montado, e com `allowed-tools: Bash(git --version)` na própria skill a saída `git version 2.54.0` entrou no texto.

```markdown
---
name: versao-do-git
description: Informa a versão do git instalada no computador.
allowed-tools: Bash(git --version)
---
A versão do git neste computador é: !`git --version`
```

O mesmo bloco funciona nas três plataformas, porque o `git` aceita o mesmo comando em macOS, Linux e Windows. Para comandos específicos de shell, o campo `shell: powershell` executa os blocos de injeção no PowerShell quando essa ferramenta está habilitada.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as variáveis constam de [Available string substitutions](https://code.claude.com/docs/en/skills#available-string-substitutions), e a injeção de comando de [Inject dynamic context](https://code.claude.com/docs/en/skills#inject-dynamic-context).
    **Codex CLI:** o uso de `$ARGUMENTS` e de injeção de comando em skills do Codex continua sem confirmação, e o estado documentado das skills está em [Build skills](https://learn.chatgpt.com/docs/build-skills).

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
