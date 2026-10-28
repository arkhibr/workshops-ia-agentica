# Exercícios — artefatos, modelos, custo e segurança

Crie e teste a skill `identificando-tarefas-e-riscos` com uma transcrição fictícia. Trabalhe em uma pasta vazia, sem credenciais reais.

Crie a skill e gere `docs/reunioes/relatorio.md`. Depois compare modelo e esforço, examine o custo e revise as permissões.

Para praticar depois da sessão, consulte os [experimentos complementares](experimentos-complementares.md).

## Preparação

Use Claude Code e Python 3. Sem Python, peça um validador em Node ou C#.

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

Cole o pedido no Claude Code.

1. Crie a skill:

    ```text
    Crie, em .claude/skills/identificando-tarefas-e-riscos/, uma skill
    que identifica tarefas e riscos de projeto em transcrições de reuniões.

    Requisitos do SKILL.md:
    - name e description válidos, em terceira pessoa, com função e gatilho.
    - Em cinco passos: ler a transcrição fornecida ou o arquivo indicado;
      identificar tarefas e riscos com evidências; gerar
      docs/reunioes/relatorio.md pelo modelo; executar o validador até OK,
      no máximo três tentativas; informar o caminho e os itens a confirmar.
    - Não inventar fatos, responsáveis ou prazos; marcar ausências como
      "A confirmar" e distinguir riscos explícitos de riscos inferidos.

    Requisitos dos demais arquivos:
    - modelo-reuniao.md com título, Fonte e seções "## Tarefas", "## Riscos"
      e "## Pontos a confirmar". Cada tarefa contém Tarefa, Responsável,
      Prazo e Evidência; cada risco contém Risco, Tipo e Evidência. Use
      "Nenhuma identificada" quando não houver itens e "Nenhum" quando não
      houver pontos a confirmar.
    - scripts/validar_reuniao.py recebe o relatório e verifica seções, campos
      preenchidos, valores de Tipo (explícito ou inferido) e padrões de segredo
      como ghp_, AKIA ou password=. Informe erros específicos ou "OK".
    ```

2. Leia os arquivos criados e confira, na lista da tabela abaixo, o que o agente produziu. Corrija com um pedido de ajuste o que estiver fora do critério.

    | Item | Critério |
    |---|---|
    | `name` | Só letras minúsculas, números e hífens, até 64 caracteres, sem "anthropic" nem "claude" |
    | `description` | Terceira pessoa, diz o que faz e quando usar, até 1.024 caracteres |
    | Corpo do `SKILL.md` | Abaixo de 60 linhas, sem explicações que o modelo já conhece |
    | Referências | Um nível de profundidade a partir do `SKILL.md`, com barras normais nos caminhos |
    | Script | Mensagens de erro que dizem o que falta e o que foi encontrado |

3. Inicie uma conversa nova com `/clear`. Invoque a skill e peça explicitamente que ela crie o relatório em Markdown:

    ```text
    /identificando-tarefas-e-riscos
    Analise a transcrição abaixo e gere o arquivo docs/reunioes/relatorio.md
    usando o modelo da skill. Execute o validador e informe o caminho e os
    pontos a confirmar.

    Transcrição da reunião do projeto de bolsas da ACME:
    Ana: Vou enviar a especificação da integração até 30 de outubro.
    Bruno: O fornecedor ainda não confirmou o prazo da API; isso pode atrasar
    a homologação. Precisamos verificar a disponibilidade do ambiente.
    Ana: Combinado. Ainda não definimos quem fará essa verificação.
    ```

4. Abra `docs/reunioes/relatorio.md` e confira o `OK` do script. Verifique se o arquivo contém as seções Tarefas, Riscos e Pontos a confirmar; depois compare cada item com a transcrição: a tarefa de Ana tem prazo, a verificação tem responsável e prazo a confirmar, e o atraso de homologação é um risco explícito. Confira evidências, omissões e riscos inferidos; não aceite fatos inventados.

## Experimento B: medir o custo e o resultado em dois modelos

Compare a mesma transcrição e os mesmos critérios em três configurações. Antes de cada execução, confira o front-matter da skill: um `model` ou `effort` declarado nele prevalece durante a execução. Altere os campos abaixo no `SKILL.md`, reinicie a sessão para carregar a mudança e registre os valores efetivamente usados. Se um modelo ou esforço não estiver disponível, escolha outro disponível e anote a substituição.

| Execução | `model` | `effort` | Comparação |
|---|---|---|---|
| A | `sonnet` | `medium` | Referência |
| B | `haiku` | `medium` | Muda o modelo |
| C | `sonnet` | `low` | Muda o esforço em relação a A |

1. Em cada configuração, inicie uma conversa nova, invoque a skill com a transcrição do experimento A e gere o relatório. Guarde uma cópia de cada arquivo para compará-los.
2. Marque o tempo entre o pedido e a entrega. Anote os tokens e o custo estimado exibidos em `/cost`, quando disponíveis; use `/usage` para consultar os limites de uso. Registre valores não exibidos como “indisponível”. O consumo pode incluir outras chamadas da sessão: anote essa limitação.
3. Confira cada relatório contra a transcrição e preencha a tabela. Uma estrutura válida não garante conteúdo correto.

| Registro | A | B | C |
|---|---|---|---|
| Modelo e esforço efetivos | | | |
| Tempo até o relatório | | | |
| Tokens de entrada, saída e cache, se disponíveis | | | |
| Custo estimado, se disponível | | | |
| Validador retornou `OK`? | | | |
| Tarefas e risco presentes, com evidências? | | | |
| Ausências marcadas sem invenção? | | | |

Qual configuração entrega o resultado correto com menor custo e tempo? A comparação A–B isola a troca de modelo; A–C, a de esforço. Uma execução por configuração não comprova superioridade: indique que outras transcrições e repetições seriam necessárias.

## Experimento C: estimar o efeito do cache

Considere um prefixo estável de 100 mil tokens enviado em 10 pedidos. Use as unidades relativas da [página de custo](custo-de-tokens.md#o-cache-de-prompt-em-unidades-relativas): entrada sem cache = 1, escrita no cache = 1,25 e leitura = 0,1 por token. Calcule o custo do prefixo sem cache e com uma escrita seguida de nove leituras. Compare com o consumo observado no experimento B, se houver dados de cache.

| Cenário | Cálculo | Total em unidades relativas |
|---|---|---|
| Sem cache | | |
| Com cache | | |

Confira: os totais são 1.000.000 e 215.000 unidades, respectivamente. O cálculo não inclui tokens novos nem saída; a medição real pode não usar cache por tamanho de entrada, validade ou mudança no prefixo.

## Experimento D: permissões e credenciais

1. Liste as operações necessárias: ler a transcrição e o modelo, escrever o relatório e executar o validador. A skill local não precisa de rede nem de credencial. Revise o `SKILL.md` e seus arquivos auxiliares: há ferramentas ou permissões além das necessárias?
2. Identifique o que `allowed-tools` libera e o que ele **não** restringe. Para um revisor que só lê o relatório e a transcrição, escreva um front-matter de subagente com `tools: Read, Grep, Glob`; justifique a ausência de escrita e shell. No projeto descartável, peça ao revisor que edite o relatório e observe se a restrição impede a edição.
3. Imagine que, numa versão futura, a transcrição venha de um serviço externo. Sem criar ou usar credenciais, preencha a ficha abaixo e justifique cada escolha com as [perguntas de revisão](seguranca-e-credenciais.md#perguntas-de-revisao).

| Decisão | Plano para a integração futura |
|---|---|
| Identidade própria e responsável | |
| Recurso e escopo mínimo de leitura | |
| Validade e responsável pela renovação | |
| Cofre e forma de fornecimento ao agente | |
| Revogação e resposta a exposição | |

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
