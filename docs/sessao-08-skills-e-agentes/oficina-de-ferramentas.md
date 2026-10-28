# Exercícios — artefatos, modelos, custo e segurança

Crie e teste a skill `identificando-tarefas-e-riscos` com uma transcrição fictícia. Trabalhe em uma pasta vazia, sem credenciais reais.

Crie a skill, confira o relatório e compare dois modelos.

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

3. Inicie uma conversa nova com `/clear` e peça a análise desta transcrição fictícia:

    ```text
    Analise a reunião do projeto de bolsas da ACME:
    Ana: Vou enviar a especificação da integração até 30 de outubro.
    Bruno: O fornecedor ainda não confirmou o prazo da API; isso pode atrasar
    a homologação. Precisamos verificar a disponibilidade do ambiente.
    Ana: Combinado. Ainda não definimos quem fará essa verificação.
    ```

4. Confira o `OK` do script e compare cada item com a transcrição: a tarefa de Ana tem prazo, a verificação tem responsável e prazo a confirmar, e o atraso de homologação é um risco explícito. Confira evidências, omissões e riscos inferidos; não aceite fatos inventados.

## Experimento B: medir o custo e o resultado em dois modelos

Compare o mesmo pedido em dois modelos.

1. Ao final do experimento A, execute `/usage` e anote os tokens da sessão por modelo e a estimativa em dólares. O guia de custo esclarece que o valor é uma estimativa calculada a preço de tabela.
2. Apague o arquivo gerado em `docs/reunioes/`, execute `/model` e troque para um modelo diferente do primeiro, por exemplo do Sonnet para o Haiku, ou o inverso.
3. Execute `/clear`, repita o mesmo pedido do passo 3 do experimento A e anote os mesmos números.
4. Preencha a tabela com os dois registros e compare.

| Registro | Modelo A | Modelo B |
|---|---|---|
| Modelo e esforço usados | | |
| Tokens de entrada, de saída e de cache (do `/usage`) | | |
| Estimativa de custo da execução | | |
| Tempo até o término, em segundos | | |
| Script terminou em `OK` na primeira tentativa? | | |
| Responsáveis e prazos ausentes marcados "A confirmar"? | | |
| Erro de conteúdo encontrado na leitura | | |

Uma execução isolada em cada modelo não permite concluir qual é melhor, porque o resultado varia entre execuções. A tabela serve para a turma discutir que medição adicional seria necessária, e o guia de escolha de modelo recomenda um conjunto de avaliações próprio como o passo mais importante.


**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
