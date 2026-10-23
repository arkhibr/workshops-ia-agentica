# Oficina de ferramentas: criar e medir uma skill

Esta oficina conduz cada participante a criar uma skill que gera um artefato, a executá-la e a medir o resultado em dois modelos, num projeto vazio criado durante a própria sessão. O exemplo é a skill `registrando-decisao-arquitetural`, que escreve um registro de decisão arquitetural em Markdown para a ACME, uma universidade fictícia, e o mesmo exemplo volta no exercício-âncora.

## Roteiro sugerido para a sessão

| Experimento | Tempo | Classificação |
|---|---:|---|
| A. Criar a skill e gerar um artefato conferido por script | 12 min | Essencial em aula |
| B. Medir o custo e o resultado em dois modelos | 9 min | Essencial em aula |
| C. Restringir um subagente e testar a restrição | fora do relógio | Extensão opcional |
| D. Localizar front-matter com erro no log de depuração | fora do relógio | Extensão opcional |
| E. Medir o disparo pela `description` e liberar ou restringir ferramentas | fora do relógio | Extensão opcional |
| F. Argumentos, acionamento manual, injeção de comando e fork | fora do relógio | Extensão opcional |

## Preparação

A oficina usa uma pasta vazia, criada do zero, para que nenhum repositório de trabalho seja alterado. É necessário ter o Claude Code instalado conforme a Sessão 1 e o Python 3 disponível no terminal. Quem não tem o Python pede ao agente que escreva o script de conferência em C# ou em Node, e o restante da oficina permanece igual.

=== "macOS/Linux"
    ```bash
    mkdir oficina-skills
    cd oficina-skills
    claude
    ```

=== "Windows (PowerShell)"
    ```powershell
    mkdir oficina-skills
    cd oficina-skills
    claude
    ```

## Experimento A: criar a skill e gerar um artefato

O pedido abaixo descreve a skill por seus requisitos, e o agente escreve os arquivos. A documentação indica que os modelos de Claude conhecem o formato de skill, e por isso o pedido não explica a estrutura do arquivo.

1. Cole o pedido a seguir no Claude Code.

    ```text
    Crie, em .claude/skills/registrando-decisao-arquitetural/, uma skill de
    projeto que gera registros de decisão arquitetural em Markdown.

    Requisitos do SKILL.md:
    - name e description válidos, com a description em terceira pessoa,
      dizendo o que a skill faz e quando usá-la.
    - Corpo com menos de 60 linhas e um procedimento em cinco passos:
      ler a descrição da decisão, perguntar se faltar contexto, duas
      opções ou a decisão, gerar o arquivo em docs/adr/NNNN-titulo.md
      pelo modelo, executar o script de conferência até a saída OK com no
      máximo três tentativas e informar o caminho e os itens a confirmar.
    - Regra: nunca inventar fatos. Consequência que não estiver na
      descrição recebe o texto "A confirmar com <responsável>".

    Requisitos dos demais arquivos:
    - modelo-adr.md na pasta da skill, com o título "# NNNN. Título", as
      linhas "Status:" e "Data:" e as seções "## Contexto",
      "## Opções consideradas", "## Decisão" e "## Consequências".
    - scripts/validar_adr.py na pasta da skill. Recebe o caminho do ADR e
      confere: as cinco partes do modelo existem, o status é um destes
      (proposta, aceita, rejeitada, substituída), a data está no formato
      AAAA-MM-DD, há ao menos duas opções e nenhum texto parece um segredo
      (por exemplo "ghp_", "AKIA" ou "password="). Cada erro informa o que
      falta e o que foi encontrado. A saída final é "OK" ou a lista de erros.
    ```

2. Leia os arquivos criados e confira, na lista da tabela abaixo, o que o agente produziu. Corrija com um pedido de ajuste o que estiver fora do critério.

    | Item | Critério |
    |---|---|
    | `name` | Só letras minúsculas, números e hífens, até 64 caracteres, sem "anthropic" nem "claude" |
    | `description` | Terceira pessoa, diz o que faz e quando usar, até 1.024 caracteres |
    | Corpo do `SKILL.md` | Abaixo de 60 linhas, sem explicações que o modelo já conhece |
    | Referências | Um nível de profundidade a partir do `SKILL.md`, com barras normais nos caminhos |
    | Script | Mensagens de erro que dizem o que falta e o que foi encontrado |

3. Inicie uma conversa nova com `/clear` e peça o registro com o texto abaixo, que omite de propósito as consequências.

    ```text
    Registre a decisão da ACME de integrar o sistema de bolsas e o de
    pagamentos por fila de mensagens gerenciada. Contexto: o sistema de
    pagamentos não pode parar quando o de bolsas ficar indisponível.
    Opções: chamadas síncronas, fila gerenciada, arquivo em lote noturno.
    Decisão: fila gerenciada. Status: proposta. Data: 2026-10-22.
    ```

4. Verifique o artefato em duas camadas. A camada estrutural é o resultado do script, que deve terminar em `OK`. A camada de conteúdo é a sua leitura: cada consequência deve vir marcada como "A confirmar", e nenhuma pode ter sido inventada.

## Experimento B: medir o custo e o resultado em dois modelos

O objetivo é produzir um registro de medição que sirva de base para a decisão de modelo da skill, no formato da [página de escolha de modelos](escolha-de-modelos.md).

1. Ao final do experimento A, execute `/usage` e anote os tokens da sessão por modelo e a estimativa em dólares. O guia de custo esclarece que o valor é uma estimativa calculada a preço de tabela.
2. Apague o arquivo gerado em `docs/adr/`, execute `/model` e troque para um modelo diferente do primeiro, por exemplo do Sonnet para o Haiku, ou o inverso.
3. Execute `/clear`, repita o mesmo pedido do passo 3 do experimento A e anote os mesmos números.
4. Preencha a tabela com os dois registros e compare.

| Registro | Modelo A | Modelo B |
|---|---|---|
| Modelo e esforço usados | | |
| Tokens de entrada, de saída e de cache (do `/usage`) | | |
| Estimativa de custo da execução | | |
| Tempo até o término, em segundos | | |
| Script terminou em `OK` na primeira tentativa? | | |
| Consequências marcadas "A confirmar" sem invenção? | | |
| Erro de conteúdo encontrado na leitura | | |

Uma execução isolada em cada modelo não permite concluir qual é melhor, porque o resultado varia entre execuções. A tabela serve para a turma discutir que medição adicional seria necessária, e o guia de escolha de modelo recomenda um conjunto de avaliações próprio como o passo mais importante.

## Experimento C: restringir um subagente e testar a restrição

Este experimento é opcional e fica fora do relógio. Peça ao agente que crie o subagente `revisor-de-adr` em `.claude/agents/`, com `tools: Read, Grep, Glob`, `model: haiku` e a instrução de apenas listar problemas, sem editar arquivos. Em seguida, peça que o subagente corrija um problema do ADR e observe a resposta.

Depois repita o teste com o campo escrito com erro de grafia, trocando `tools` por `tool`. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) informa que os campos desconhecidos são ignorados em silêncio e que o campo `tools` omitido faz o subagente herdar todas as ferramentas, e o teste verifica se essa combinação se confirma na versão instalada. O resultado esperado, confirmado na execução com a versão 2.1.309 do Claude Code, é que o subagente com `tools: Read, Grep, Glob` não consiga editar o arquivo e que o subagente com o campo escrito errado o edite.

No Codex CLI, o passo com `tools` não tem correspondente direto, porque o arquivo TOML do agente não traz uma lista de ferramentas permitidas como o `tools`, e as chaves `features.*` com valor `false` removem apenas capacidades específicas, como `shell_tool`. A documentação adverte que a instrução "não edite arquivos" não cria um sandbox somente leitura, e a restrição de escrita vem do sandbox da sessão.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** `tools` e `disallowedTools` constam da [tabela de campos dos subagentes](https://code.claude.com/docs/en/sub-agents#frontmatter-reference).
    **Codex CLI:** a restrição vem da sessão que inicia o agente, com `sandbox_mode = "read-only"`, e as chaves `features.*` com valor `false` removem capacidades do agente, conforme [aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security) e [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents). Esse comportamento está documentado e ainda sem execução observada.

## Experimento D: localizar front-matter com erro no log de depuração

O objetivo é prever e depois confirmar o que acontece com quatro arquivos de subagente, três deles com erro de front-matter, e localizar a causa no log de depuração. O experimento exige o Claude Code 2.1.296 ou posterior para a mensagem de campo desconhecido, e o comando `claude --version` confirma a versão instalada. Os resultados esperados pressupõem que o projeto não tenha outros subagentes nem skills, e por isso o experimento usa uma pasta nova, criada com `mkdir oficina-skills-d` e acessada com `cd oficina-skills-d`, comandos iguais em macOS, Linux e Windows.

**Passo 1:** crie a pasta dos subagentes.

=== "macOS/Linux"
    ```bash
    mkdir -p .claude/agents
    ```

=== "Windows (PowerShell)"
    ```powershell
    mkdir .claude\agents
    ```

**Passo 2:** crie os quatro arquivos abaixo com o editor de texto, sem pedir ao agente, porque o agente tende a corrigir os erros que o experimento quer observar. O arquivo `sem-delimitador.md` começa com uma linha em branco, e essa linha vazia é o erro.

Arquivo `.claude/agents/revisor-controle.md`:

```markdown
---
name: revisor-controle
description: Revisa a estrutura de um registro de decisão arquitetural. Use quando pedirem revisão de ADR.
tools: Read, Grep, Glob
---
Liste as seções ausentes do ADR indicado, sem editar arquivos.
```

Arquivo `.claude/agents/sem-delimitador.md`, com a primeira linha vazia:

```markdown

---
name: sem-delimitador
description: Revisa a estrutura de um ADR, com uma linha em branco antes do primeiro delimitador.
---
Liste as seções ausentes do ADR indicado.
```

Arquivo `.claude/agents/nome-com-dois-pontos.md`:

```markdown
---
name: acme:revisor
description: Revisa a estrutura de um ADR, com dois-pontos no nome.
---
Liste as seções ausentes do ADR indicado.
```

Arquivo `.claude/agents/tool-errado.md`, com `tool` no lugar de `tools`:

```markdown
---
name: tool-errado
description: Revisa a estrutura de um ADR, com o campo de ferramentas escrito errado.
tool: Read, Grep, Glob
---
Liste as seções ausentes do ADR indicado, sem editar arquivos.
```

**Passo 3:** antes de executar, preencha a previsão da equipe para cada arquivo.

| Arquivo | Carrega? | Aparece registro no log? |
|---|---|---|
| `revisor-controle.md` | | |
| `sem-delimitador.md` | | |
| `nome-com-dois-pontos.md` | | |
| `tool-errado.md` | | |

**Passo 4:** execute o Claude Code em modo não interativo, gravando o log de depuração, e procure as linhas dos arquivos de subagente.

=== "macOS/Linux"
    ```bash
    claude -p "Liste o nome de todos os subagentes customizados do projeto que você pode invocar com a ferramenta Agent, um por linha, sem comentários." --model haiku --setting-sources project,local --debug-file depuracao.log
    grep -n "Agent file" depuracao.log
    ```

=== "Windows (PowerShell)"
    ```powershell
    claude -p "Liste o nome de todos os subagentes customizados do projeto que você pode invocar com a ferramenta Agent, um por linha, sem comentários." --model haiku --setting-sources project,local --debug-file depuracao.log
    Select-String -Path depuracao.log -Pattern "Agent file"
    ```

**Passo 5:** compare o resultado com a previsão e confira o que foi carregado na tabela Custom Agents do comando `/context`, digitado numa sessão iniciada com `claude` na mesma pasta.

O resultado esperado, observado no `claude 2.1.309` com o modelo haiku, é o carregamento de `revisor-controle` e `tool-errado`, com um `[WARN]` que traz `frontmatter key Claude Code does not recognize or apply: "tool" (did you mean "tools"?)` e um `[ERROR]` que traz `names must not contain ':' (reserved for plugin namespacing)`. O arquivo `sem-delimitador.md` fica fora da tabela de `/context` e sem nenhuma linha no log, o que faz dele o único dos três erros que só se encontra comparando o resultado com a previsão do passo 3.

**Questões exploratórias:**

- Qual dos três erros tem o efeito mais perigoso para a segurança, e por quê?
- Qual deles não deixa nenhum rastro no log, e como a equipe o encontraria sem a previsão feita no passo 3?
- O comando `claude plugin validate .claude/agents` aponta esses três erros? A página [Depuração de skills e agentes](depuracao-de-skills-e-agentes.md#validar-a-pasta-antes-da-sessao) traz o resultado observado.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** a mensagem de campo desconhecido e os arquivos ignorados constam de [Frontmatter reference](https://code.claude.com/docs/en/sub-agents#frontmatter-reference) e de [Subagent files Claude Code skips](https://code.claude.com/docs/en/sub-agents#subagent-files-claude-code-skips).
    **Codex CLI:** a documentação lida não descreve um log equivalente para arquivos de agente com erro, item sem confirmação. O comando `codex debug prompt-input` mostra o prompt visível ao modelo, e o formato TOML dos agentes está na [documentação de Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Experimento E: medir o disparo pela description e liberar ou restringir ferramentas

A primeira parte mede se a `description` basta para o modelo acionar uma skill, e a segunda parte mostra a diferença entre `allowed-tools` e `disallowed-tools`. Os dois testes usam `claude -p`, de modo que a equipe repete as execuções sem uma sessão interativa, e a opção `--setting-sources project,local` isola o resultado das configurações pessoais de cada máquina. Os resultados esperados pressupõem um projeto sem outras skills, e por isso o experimento usa uma pasta nova, criada com `mkdir oficina-skills-e` e acessada com `cd oficina-skills-e`, comandos iguais em macOS, Linux e Windows.

**E.1: o disparo pela description.** O nome da skill é neutro de propósito, porque um nome como `resumo-semanal-de-chamados` já dá a pista ao modelo e esconde o efeito da `description`.

**Passo 1:** crie a pasta da skill.

=== "macOS/Linux"
    ```bash
    mkdir -p .claude/skills/rotina-a7
    ```

=== "Windows (PowerShell)"
    ```powershell
    mkdir .claude\skills\rotina-a7
    ```

**Passo 2:** crie o arquivo `.claude/skills/rotina-a7/SKILL.md` com o conteúdo abaixo, em que o texto da `description` muda a cada variação.

```markdown
---
name: rotina-a7
description: <texto da variação>
---
Escreva o resumo semanal da fila de chamados da ACME. Comece a resposta com a linha RESUMO-ACME.
```

**Passo 3:** para cada uma das quatro descrições da tabela, troque a linha `description`, execute o pedido abaixo e conte as chamadas à ferramenta `Skill` no registro da execução.

=== "macOS/Linux"
    ```bash
    claude -p "Preciso do resumo semanal da fila de chamados." --model haiku --setting-sources project,local --output-format stream-json --verbose > disparo.jsonl
    grep -c '"name":"Skill","input"' disparo.jsonl
    ```

=== "Windows (PowerShell)"
    ```powershell
    claude -p "Preciso do resumo semanal da fila de chamados." --model haiku --setting-sources project,local --output-format stream-json --verbose > disparo.jsonl
    (Select-String -Path disparo.jsonl -Pattern '"name":"Skill","input"').Count
    ```

| Variação da `description` | Skill acionada? |
|---|---|
| Escreve o resumo semanal da fila de chamados no formato fixo da ACME. Use quando pedirem resumo semanal de chamados ou da fila de suporte. | |
| Chamados. | |
| Ajuda com várias tarefas da equipe. | |
| Prepara o relatório trimestral de custos de infraestrutura. | |

O resultado observado no `claude 2.1.309` com o modelo haiku, em uma execução por variação, foi o disparo nas três primeiras descrições e nenhum disparo na quarta. Uma execução por variação e uma única skill disponível não permitem concluir que uma descrição vaga seja suficiente, e a extensão do experimento cria uma segunda skill, `rotina-b3`, sobre outro assunto, e repete as quatro variações com as duas skills presentes.

**E.2: liberar não é restringir.** Crie quatro skills com o mesmo corpo, que pede a criação de um arquivo com a ferramenta `Write`, e linhas de front-matter diferentes.

**Passo 1:** crie uma pasta por skill, com os nomes `sem-campo`, `liberar-escrita`, `liberar-leitura` e `bloquear-escrita` dentro de `.claude/skills/`.

=== "macOS/Linux"
    ```bash
    mkdir -p .claude/skills/sem-campo .claude/skills/liberar-escrita .claude/skills/liberar-leitura .claude/skills/bloquear-escrita
    ```

=== "Windows (PowerShell)"
    ```powershell
    New-Item -ItemType Directory -Force .claude\skills\sem-campo, .claude\skills\liberar-escrita, .claude\skills\liberar-leitura, .claude\skills\bloquear-escrita | Out-Null
    ```

**Passo 2:** crie o `SKILL.md` de cada pasta com o modelo abaixo, trocando `<nome>` pelo nome da pasta e `<linha extra>` pela linha indicada na tabela, que a skill `sem-campo` não tem.

```markdown
---
name: <nome>
description: Cria um arquivo de teste com a ferramenta Write.
<linha extra>
---
Crie o arquivo saida-<nome>.txt contendo apenas a palavra ok, usando a ferramenta Write. Relate em uma frase se conseguiu.
```

| Skill | Linha extra | Modo de permissão | Previsão | Arquivo criado? |
|---|---|---|---|---|
| `sem-campo` | nenhuma | `default` | | |
| `liberar-escrita` | `allowed-tools: Write` | `default` | | |
| `liberar-leitura` | `allowed-tools: Read` | `acceptEdits` | | |
| `bloquear-escrita` | `disallowed-tools: Write Edit Bash` | `acceptEdits` | | |

**Passo 3:** execute cada skill pelo nome com o modo de permissão da tabela, e liste os arquivos criados. O exemplo mostra a primeira execução, e as demais trocam o nome da skill e o valor de `--permission-mode`.

=== "macOS/Linux"
    ```bash
    claude -p "/sem-campo" --model haiku --setting-sources project,local --permission-mode default
    ls saida-*.txt
    ```

=== "Windows (PowerShell)"
    ```powershell
    claude -p "/sem-campo" --model haiku --setting-sources project,local --permission-mode default
    Get-ChildItem saida-*.txt
    ```

O resultado observado foi a escrita negada na skill `sem-campo`, o arquivo criado em `liberar-escrita`, o arquivo criado em `liberar-leitura`, apesar de o campo listar só `Read`, e o arquivo ausente em `bloquear-escrita`. O terceiro caso é o que desfaz a leitura intuitiva de `allowed-tools`, porque o campo libera as ferramentas listadas sem restringir as demais.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** `description`, `allowed-tools` e `disallowed-tools` constam da [tabela de campos das skills](https://code.claude.com/docs/en/skills#frontmatter-reference) e de [Pre-approve tools for a skill](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill), e o acionamento por `/nome` em modo não interativo foi observado na versão 2.1.309.
    **Codex CLI:** a skill é acionada pela `description` ou pelo nome com `$nome`, conforme [Build skills](https://learn.chatgpt.com/docs/build-skills). O uso de `allowed-tools` em skills do Codex não tem confirmação, e a especificação aberta lista o campo como experimental.

## Experimento F: argumentos, acionamento manual, injeção de comando e fork

O experimento reúne quatro recursos do corpo e do front-matter que mudam o modo como a skill é montada e acionada. Cada parte cria uma ou duas skills pequenas em `.claude/skills/` e uma execução com `claude -p`, e as pastas são criadas como no experimento E.

**F.1: argumentos.** Crie a pasta `.claude/skills/args-demo` com o `SKILL.md` abaixo e execute `claude -p "/args-demo alfa beta" --model haiku --setting-sources project,local`.

```markdown
---
name: args-demo
description: Demonstra a substituição de argumentos.
argument-hint: [a] [b]
---
Responda apenas com esta linha, substituindo o que vier: TODOS=[$ARGUMENTS] PRIMEIRO=[$0] SEGUNDO=[$1]
```

O resultado observado foi `TODOS=[alfa beta] PRIMEIRO=[alfa] SEGUNDO=[beta]`, o que mostra que a numeração dos argumentos começa em 0.

**F.2: acionamento manual.** Crie a pasta `.claude/skills/so-pessoa` com o `SKILL.md` abaixo e execute dois pedidos, um em linguagem natural e outro pelo nome.

```markdown
---
name: so-pessoa
description: Escreve o resumo semanal da fila de chamados da ACME.
disable-model-invocation: true
---
Comece a resposta com a linha RESUMO-SO-PESSOA.
```

Execute `claude -p "Preciso do resumo semanal da fila de chamados da ACME." --model haiku --setting-sources project,local` e depois `claude -p "/so-pessoa" --model haiku --setting-sources project,local`, e verifique em qual das duas respostas aparece a linha `RESUMO-SO-PESSOA`. No resultado observado, a linha apareceu somente na chamada pelo nome, e o pedido em linguagem natural não acionou a skill.

**F.3: injeção de comando.** Crie a pasta `.claude/skills/injecao` com o `SKILL.md` abaixo, que não declara `allowed-tools`, e execute `claude -p "/injecao" --model haiku --setting-sources project,local`.

```markdown
---
name: injecao
description: Demonstra a injeção de comando.
---
A versão do git neste computador é: !`git --version`. Repita essa frase exatamente, sem comentar.
```

Sem o campo, a execução observada falhou com `Shell command permission check failed ... This command requires approval`, e a skill não foi montada. Acrescente a linha `allowed-tools: Bash(git --version)` ao front-matter e repita a chamada, e a saída observada trouxe a versão do `git` no texto. A observação foi feita no macOS, e a documentação informa que o Claude Code executa a injeção pela ferramenta Bash quando há bash disponível e pela ferramenta PowerShell quando não há, como no Windows sem Git Bash, caso em que o efeito da regra `Bash(git --version)` não foi verificado.

**F.4: fork e histórico.** Crie duas skills com a mesma pergunta, `sem-fork` e `com-fork`, que diferem só pela linha `context: fork`.

```markdown
---
name: com-fork
description: Pergunta pela palavra-secreta citada antes.
context: fork
---
Responda em uma frase: qual foi a palavra-secreta citada antes nesta conversa? Se você não souber, escreva NÃO SEI.
```

Para cada skill, abra uma conversa e retome-a pelo nome, com duas chamadas. A opção `--continue` retoma a conversa mais recente da pasta, e por isso as duas chamadas de cada skill precisam ser feitas em sequência.

=== "macOS/Linux"
    ```bash
    claude -p "A palavra-secreta desta conversa é BANANA. Responda apenas: anotado." --model haiku --setting-sources project,local
    claude -p --continue "/com-fork" --model haiku --setting-sources project,local
    ```

=== "Windows (PowerShell)"
    ```powershell
    claude -p "A palavra-secreta desta conversa é BANANA. Responda apenas: anotado." --model haiku --setting-sources project,local
    claude -p --continue "/com-fork" --model haiku --setting-sources project,local
    ```

O resultado observado foi `NÃO SEI` na skill com `context: fork` e a resposta com a palavra BANANA na skill sem o campo, porque o fork não enxerga o histórico da conversa.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os argumentos e a injeção constam de [Pass arguments to skills](https://code.claude.com/docs/en/skills#pass-arguments-to-skills) e de [Inject dynamic context](https://code.claude.com/docs/en/skills#inject-dynamic-context), e o fork de [Run skills in a subagent](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent).
    **Codex CLI:** `policy.allow_implicit_invocation: false` em `agents/openai.yaml` corresponde a `disable-model-invocation: true` com polaridade inversa, e a chamada pelo nome usa `$nome`, conforme [Build skills](https://learn.chatgpt.com/docs/build-skills). Argumentos, injeção de comando e fork em skills do Codex não têm confirmação.

**Próxima página:** [Segurança e credenciais](seguranca-e-credenciais.md).
