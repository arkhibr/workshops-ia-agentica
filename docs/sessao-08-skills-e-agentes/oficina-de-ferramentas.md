# Oficina de ferramentas: criar e medir uma skill

Esta oficina conduz cada participante a criar uma skill que gera um artefato, a executá-la e a medir o resultado em dois modelos, num projeto vazio criado durante a própria sessão. O exemplo é a skill `registrando-decisao-arquitetural`, que escreve um registro de decisão arquitetural em Markdown para a ACME, uma universidade fictícia, e o mesmo exemplo volta no exercício-âncora.

## Roteiro sugerido para a sessão

| Experimento | Tempo | Classificação |
|---|---:|---|
| A. Criar a skill e gerar um artefato conferido por script | 12 min | Essencial em aula |
| B. Medir o custo e o resultado em dois modelos | 9 min | Essencial em aula |
| C. Restringir um subagente e testar a restrição | fora do relógio | Extensão opcional |

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

Depois repita o teste com o campo escrito com erro de grafia, trocando `tools` por `tool`. A [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) informa que os campos desconhecidos são ignorados em silêncio e que o campo `tools` omitido faz o subagente herdar todas as ferramentas, e o teste verifica se essa combinação se confirma na versão instalada. O resultado esperado, a confirmar na execução, é que o subagente com `tools: Read, Grep, Glob` não consiga editar o arquivo e que o subagente com o campo escrito errado o edite.

**Próxima página:** [Segurança e credenciais](seguranca-e-credenciais.md).
