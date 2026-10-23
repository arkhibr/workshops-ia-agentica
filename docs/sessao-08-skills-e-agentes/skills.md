# Skills

Uma skill é uma pasta com um arquivo `SKILL.md` que ensina o agente a executar um tipo de tarefa da equipe sempre do mesmo modo, sem que a pessoa repita as instruções a cada conversa. Esta página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Arquivo e front-matter" no recorte da skill, e percorre a anatomia da pasta, o front-matter com os campos de cada ferramenta, o custo de carga em três níveis, as regras de escrita da descrição e do corpo, a diferença entre liberar e restringir ferramentas e o diagnóstico da skill que não aciona.

## Anatomia de uma skill

A [documentação das skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) define como obrigatório um arquivo `SKILL.md` com frontmatter YAML que contém dois campos. O campo `name` aceita até 64 caracteres, apenas letras minúsculas, números e hífens, e não pode conter as palavras reservadas "anthropic" e "claude". O campo `description` não pode ficar vazio, aceita até 1.024 caracteres e precisa dizer o que a skill faz e quando usá-la.

No Claude Code, as skills ficam em `~/.claude/skills/` quando são pessoais e em `.claude/skills/` quando pertencem ao projeto, e cada skill ocupa uma pasta com o nome dela. As skills do Claude Code são baseadas em arquivos e não são sincronizadas com as do claude.ai nem com as da API, de modo que cada superfície recebe a própria cópia. No Claude Code, a skill também pode ser distribuída por meio de plugins.

```text
.claude/skills/registrando-decisao-arquitetural/
├── SKILL.md            instruções principais, carregadas quando a skill é acionada
├── modelo-adr.md       modelo do artefato, lido só quando o agente precisa dele
└── scripts/
    └── validar_adr.py  script de conferência, executado sem entrar no contexto
```

## Front-matter

O front-matter de uma skill é o bloco YAML entre dois marcadores `---` no início do arquivo `SKILL.md`, e define como o agente descobre a skill, quando a aciona e que permissões ela concede. A figura marca, num arquivo de exemplo, o núcleo que vale em qualquer ferramenta, os campos da especificação aberta de suporte variável e os campos exclusivos do Claude Code.

![Um arquivo SKILL.md com front-matter em que name e description aparecem em verde como núcleo portátil, allowed-tools em cinza como campo da especificação aberta e when_to_use, disable-model-invocation, context, agent e o marcador $ARGUMENTS em laranja como específicos do Claude Code. À direita, uma anotação curta explica o efeito de cada campo.](assets/skill-anotada-nucleo-portatil.png)

### Núcleo portátil

A [especificação aberta Agent Skills](../referencia/bibliografia.md#agent-skills-especificacao-aberta) define o formato mínimo de uma skill, e a documentação do Codex CLI declara seguir esse padrão. Dois campos formam o núcleo: `name` e `description`, e uma skill que usa só esses dois funciona nas duas ferramentas.

| Campo | Regra na especificação aberta | No Claude Code |
|---|---|---|
| `name` | Obrigatório, de 1 a 64 caracteres, com letras minúsculas, números e hifens, sem hífen no início, no fim ou repetido, e igual ao nome do diretório | Opcional, e o padrão é o nome do diretório. A tabela de campos do Claude Code não repete as regras de tamanho e de caracteres |
| `description` | Obrigatório, de 1 a 1.024 caracteres | Recomendado. Se faltar, vale a primeira linha não vazia do corpo, e a listagem corta `description` e `when_to_use` somados em 1.536 caracteres |

As regras de `name` e `description` da seção anterior, com as palavras reservadas, vêm da documentação de skills da plataforma Claude, que vale para a API e para o claude.ai, e a tabela de campos do Claude Code torna todos os campos opcionais. A seção [Quando a skill não aciona](#quando-a-skill-nao-aciona) traz a regra sobre a posição do primeiro `---` e sobre o YAML inválido, e mostra como localizar o erro.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as skills ficam em `.claude/skills/<nome>/SKILL.md`, e a [tabela de campos](https://code.claude.com/docs/en/skills#frontmatter-reference) lista cada campo aceito.
    **Codex CLI:** as skills ficam em `.agents/skills/<nome>/SKILL.md`, com `name` e `description` obrigatórios segundo a [documentação de Build skills](https://learn.chatgpt.com/docs/build-skills), e a descoberta da skill foi observada na versão 0.140.0 pelo comando `codex debug prompt-input`.

### Campos do Claude Code

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

## Três níveis de carga

A skill usa divulgação progressiva: o agente carrega a informação em etapas, conforme a tarefa exige. A tabela reproduz os valores da documentação.

| Nível | Quando carrega | Custo em tokens | Conteúdo |
|---|---|---|---|
| 1. Metadados | Sempre, na inicialização | Cerca de 100 tokens por skill | `name` e `description` do frontmatter |
| 2. Instruções | Quando a skill é acionada | Abaixo de 5 mil tokens | Corpo do `SKILL.md` |
| 3. Recursos e código | Sob demanda | Nenhum até o acesso | Arquivos de referência, modelos e scripts |

![Três caixas empilhadas mostram os níveis de carga de uma skill. O nível 1, metadados, entra na inicialização com cerca de 100 tokens por skill. O nível 2, instruções, entra quando a skill é acionada, com corpo abaixo de 5 mil tokens. O nível 3, recursos e scripts, entra sob demanda. Um painel à direita descreve o orçamento da listagem, o que acontece quando ele estoura, como ajustá-lo e como medi-lo.](assets/carga-em-tres-niveis-e-listagem.png)

Enquanto uma skill não é acionada, somente o nome e a descrição ocupam o contexto, e por isso uma equipe pode instalar muitas skills sem penalidade relevante. Os scripts têm uma vantagem adicional: o código nunca entra no contexto, e apenas a saída do script consome tokens. A documentação recomenda escrever scripts para as operações determinísticas, porque são mais confiáveis que o código gerado a cada uso, economizam tokens e garantem consistência entre execuções. O [orçamento da listagem](custo-de-tokens.md#orcamento-da-listagem-de-skills) do nível 1, de 1% da janela de contexto, e a [medição do que foi carregado](custo-de-tokens.md#o-que-o-claude-code-mostra-do-que-foi-carregado) ficam na página de Custo de tokens.

## Escrever a descrição

A descrição é o texto contra o qual o agente compara o pedido da pessoa para decidir se aciona a skill, e a documentação indica que essa escolha ocorre entre possivelmente mais de 100 skills disponíveis. As regras de escrita são três: a descrição vem em terceira pessoa, porque é injetada no prompt de sistema e a mudança de ponto de vista prejudica a descoberta, informa o que a skill faz e em que situações deve ser usada, e contém os termos que a pessoa costuma empregar no pedido.

| Descrição | Avaliação |
|---|---|
| `Processa arquivos Excel e gera relatórios. Use ao analisar planilhas, dados tabulares ou arquivos .xlsx.` | Terceira pessoa, diz o que faz e quando usar |
| `Posso ajudar você a processar arquivos Excel.` | Primeira pessoa, sem gatilho de uso |
| `Ajuda com documentos.` | Vaga, o agente não distingue de outras skills |

Cada entrada da listagem é cortada em 1.536 caracteres, somando `description` e `when_to_use`, e a documentação recomenda colocar o caso de uso principal no começo do texto. A `description` também decide o acionamento na prática. Numa skill de nome neutro, `rotina-a7`, uma descrição específica, a descrição de uma palavra ("Chamados.") e uma descrição genérica ("Ajuda com várias tarefas da equipe.") acionaram a skill diante do pedido "Preciso do resumo semanal da fila de chamados.", e uma descrição sobre outro assunto não a acionou. Cada variante rodou uma vez, no modelo haiku, e com uma única skill disponível, de modo que com várias skills concorrentes o resultado pode diferir, e o Experimento E da oficina propõe a medição com as skills da própria equipe.

## Escrever o corpo

O corpo deve conter apenas o que o agente ainda não sabe. A documentação trata a janela de contexto como um recurso compartilhado entre o prompt de sistema, o histórico da conversa, os metadados das outras skills e o pedido, e pede que cada parágrafo justifique o custo em tokens. O corpo do `SKILL.md` fica abaixo de 500 linhas, e o conteúdo excedente vai para arquivos separados, referenciados diretamente a partir do `SKILL.md`, a um nível de profundidade, porque o agente pode ler apenas o início de arquivos referenciados por outros arquivos.

O grau de liberdade da instrução acompanha a fragilidade da tarefa.

| Grau de liberdade | Quando usar | Forma da instrução |
|---|---|---|
| Alto | Vários caminhos válidos, decisão depende do contexto | Passos em texto e heurísticas |
| Médio | Existe um padrão preferido, com alguma variação aceitável | Modelo ou pseudocódigo com parâmetros |
| Baixo | Operação frágil, em que a ordem importa | Script exato, sem alteração dos parâmetros |

A documentação ainda recomenda usar uma única palavra para cada conceito ao longo da skill, evitar informação que perde a validade com a data e oferecer um caminho padrão com uma exceção explícita para o caso especial, sem listar alternativas equivalentes.

### Substituições e comandos no corpo

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

O comando `git --version` é igual em macOS, Linux e Windows, e a documentação informa que o Claude Code executa a injeção pela ferramenta Bash quando há bash disponível e pela ferramenta PowerShell quando não há, como no Windows sem Git Bash. A observação desta sessão foi feita no macOS, e o efeito da regra `Bash(git --version)` em `allowed-tools` no Windows sem Git Bash não foi verificado. O campo `shell: powershell` executa os blocos de injeção no PowerShell quando essa ferramenta está habilitada.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** as variáveis constam de [Available string substitutions](https://code.claude.com/docs/en/skills#available-string-substitutions), e a injeção de comando de [Inject dynamic context](https://code.claude.com/docs/en/skills#inject-dynamic-context).
    **Codex CLI:** o uso de `$ARGUMENTS` e de injeção de comando em skills do Codex continua sem confirmação, e o estado documentado das skills está em [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Liberar não é restringir

O nome `allowed-tools` sugere uma lista de ferramentas permitidas, e a documentação diz o contrário: o campo concede permissão para as ferramentas listadas durante o turno da skill, e todas as outras ferramentas continuam disponíveis, regidas pelas configurações de permissão. A restrição vem de `disallowed-tools`. A tabela resume o que se observou numa skill que pede a criação de um arquivo com a ferramenta `Write`.

| Skill | Modo de permissão | Resultado observado |
|---|---|---|
| Sem campo de ferramenta | `default` | Escrita negada por falta de permissão, arquivo não criado |
| `allowed-tools: Write` | `default` | Arquivo criado, porque a escrita foi liberada para o turno |
| `allowed-tools: Read` | `acceptEdits` | Arquivo criado, porque o campo não restringiu a escrita |
| `disallowed-tools: Write Edit Bash` | `acceptEdits` | Arquivo não criado, porque as ferramentas saíram do conjunto |

A observação veio de uma execução de cada variante com `claude 2.1.309` em modo não interativo, e a documentação acrescenta um aviso de segurança: o Claude Code aplica o `allowed-tools` de uma skill de projeto mesmo numa execução com `-p` em pasta nunca marcada como confiável. O `allowed-tools` de uma skill versionada em repositório alheio merece, por isso, a mesma revisão que um script recebido.

## Skill, instrução de projeto e pedido avulso

Uma instrução pode ficar em três lugares, e cada um tem um custo de carga diferente. O guia de [custo do Claude Code](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) informa que o `CLAUDE.md` é carregado no início de toda sessão, que as skills carregam apenas sob demanda e que o `CLAUDE.md` deve ter menos de 200 linhas, com instruções de fluxos específicos, como revisão de pull request, movidas para skills.

| Lugar | Carga | Indicado para |
|---|---|---|
| `CLAUDE.md` | Toda sessão | Regras que valem para qualquer tarefa do projeto |
| Skill | Quando acionada | Procedimento recorrente de um tipo de tarefa |
| Pedido avulso | Uma conversa | Tarefa que não se repete |

A comparação da skill com o subagente, a skill com fork, o hook e o servidor MCP está na seção [Escolher o mecanismo](agentes-e-subagentes.md#escolher-o-mecanismo) da página de agentes e subagentes.

## Quando a skill não aciona

A skill com erro de front-matter raramente produz mensagem na sessão. O Claude Code lê o front-matter somente quando o primeiro `---` está na primeira linha do arquivo, e trata o arquivo inteiro como conteúdo da skill em qualquer outro caso. YAML inválido faz a skill carregar sem nenhum campo: o comando `/nome` continua funcionando, e o modelo deixa de acioná-la pela `description`. Campos desconhecidos são ignorados sem erro, e um nome de pasta com caracteres como o espaço de largura zero ou `<` impede o carregamento. Um `paths` que aponta para arquivos fora do diretório de trabalho atual mantém a skill inativa. Esses comportamentos constam da documentação, e a observação desta sessão cobriu só os subagentes, tratados na página de [agentes e subagentes](agentes-e-subagentes.md#ferramentas-permissoes-e-arquivos-ignorados).

A documentação propõe uma sequência para a skill que o modelo não usa quando devia:

1. Conferir se a `description` contém as palavras que a pessoa diria naturalmente.
2. Verificar se a skill aparece na pergunta "What skills are available?".
3. Reformular o pedido para se aproximar da `description`.
4. Invocar a skill pelo nome com `/nome`, se ela aceitar invocação pela pessoa.
5. Se `/nome` também não for reconhecido, verificar se o Claude Code recusou o nome da skill.
6. Se a skill usa `paths`, verificar se os arquivos estão dentro do diretório de trabalho atual.

A observação desta sessão acrescenta um cuidado de método: o nome da skill também orienta o modelo, e uma skill chamada `resumo-semanal-de-chamados` acionou com as três primeiras descrições testadas. O teste da `description` isolada exige um nome neutro, como `rotina-a7`, e a oficina usa essa regra. Para o problema inverso, a skill acionada em excesso, a documentação recomenda tornar a `description` mais específica ou adicionar `disable-model-invocation: true`. Quando o modelo deixa de seguir uma skill depois do primeiro turno, a documentação orienta mover a regra obrigatória para um hook e colocar as instruções mais importantes no início do `SKILL.md`, porque a compactação da conversa pode manter só o começo da skill invocada. O comando `claude plugin validate .claude/skills` encontra os `SKILL.md` cujo front-matter não pode ser lido, e o [Experimento D](oficina-de-ferramentas.md#experimento-d-localizar-front-matter-com-erro-no-log-de-depuracao) mostra o log de depuração.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a sequência consta de [Skill not triggering](https://code.claude.com/docs/en/skills#skill-not-triggering) e de [Claude stops following a skill](https://code.claude.com/docs/en/skills#claude-stops-following-a-skill).
    **Codex CLI:** a skill pode ser invocada explicitamente por `$nome`, e `policy.allow_implicit_invocation: false` restringe a invocação à forma explícita, conforme [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Avaliar antes de escrever

A documentação recomenda criar as avaliações antes do texto extenso. O procedimento tem cinco passos: executar o agente em tarefas representativas sem a skill e registrar as falhas, criar três cenários que testem essas falhas, medir o desempenho sem a skill, escrever o mínimo de instruções que resolva as falhas e iterar contra a medição inicial. A lista de verificação da própria documentação pede pelo menos três avaliações e testes com Haiku, Sonnet e Opus, porque o que basta para o Opus pode exigir mais detalhe para o Haiku.

!!! warning "Skill de terceiros"
    A documentação orienta usar apenas skills criadas pela própria equipe ou obtidas da Anthropic, porque uma skill maliciosa pode instruir o agente a chamar ferramentas ou executar código de modo diferente do objetivo declarado. No Claude Code, a skill tem o mesmo acesso de rede que qualquer programa do computador da pessoa. Antes de instalar uma skill externa, revise todos os arquivos dela, incluindo scripts, e procure chamadas de rede e acessos a arquivos que não combinem com a finalidade descrita.

!!! abstract "Linha da ficha"
    Arquivo e front-matter da skill:

    - Quais campos o arquivo da skill declara e com que valores?
    - A `description` basta para o acionamento, sem depender do nome da skill?
    - A skill libera ferramentas ou as restringe, e quem a aciona, a pessoa ou o modelo?

**Próxima página:** [Agentes e subagentes](agentes-e-subagentes.md).
