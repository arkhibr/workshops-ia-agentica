# Custo de tokens

O custo de uma skill ou de um agente cresce com o tamanho do contexto enviado a cada pedido e com o número de pedidos, e por isso precisa ser declarado como requisito antes da construção. Esta página apresenta de onde o custo vem, o efeito do cache de prompt em unidades relativas e as alavancas de redução que o guia de custo do Claude Code documenta. A página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Orçamento de tokens".

## De onde o custo vem

O Claude Code cobra pelo consumo de tokens da API. O [guia de custo](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) informa que, em implantações corporativas, a média é de cerca de US$ 13 por desenvolvedor por dia ativo e de US$ 150 a US$ 250 por mês, e que o custo fica abaixo de US$ 30 por dia ativo para 90% dos usuários. Esses valores são médias de uso geral e variam com o modelo, o tamanho do código e o uso de várias instâncias ou de automação.

A causa principal é o contexto. Cada pedido carrega a conversa inteira, e cada uso de ferramenta gera outro pedido com os resultados acumulados. Uma sessão aberta por horas pode, assim, consumir mais do que a atividade da pessoa sugere. O guia lista, além do contexto longo, as falhas de cache após uma pausa maior que a vida do cache, as tarefas agendadas que reenviam o contexto a cada disparo, cada subagente e cada integrante de uma equipe de agentes, e a compactação, que é em si um pedido grande.

Os tokens de raciocínio estendido são cobrados como tokens de saída, e o orçamento padrão pode chegar a dezenas de milhares de tokens por pedido, conforme o modelo.

![Cinco pedidos em sequência, em que o contexto acumulado cresce a cada pedido e cada resultado de ferramenta gera outro pedido, sem escala de tokens. À direita, as médias do guia de custo: cerca de US$ 13 por desenvolvedor por dia ativo e abaixo de US$ 30 por dia ativo para 90% dos usuários. Abaixo, cinco outros fatores de custo: falha de cache após pausa, tarefas agendadas, subagentes e equipes de agentes, compactação e raciocínio estendido.](assets/de-onde-o-custo-vem.png)

## O cache de prompt em unidades relativas

A [documentação do cache de prompt](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao) define multiplicadores sobre o preço-base de entrada. A tabela usa a unidade relativa "1 = preço-base de um token de entrada".

| Operação | Multiplicador |
|---|---|
| Escrita no cache, vida de 5 minutos | 1,25 |
| Escrita no cache, vida de 1 hora | 2 |
| Leitura do cache, maioria dos modelos | 0,1 |
| Leitura do cache, Claude Opus 5.5 e Claude Sonnet 5.5 | 0,05 |
| Leitura do cache, Claude Fable 5.1 | 0,025 |

A vida padrão do cache é de 5 minutos, renovada sem custo a cada uso, e prompts abaixo do tamanho mínimo, que varia de 512 a 4.096 tokens conforme o modelo, são processados sem cache e sem erro. O cache não altera a geração de saída.

Para um prefixo estável de 100 mil tokens, enviado em 10 pedidos seguidos dentro da vida do cache, num modelo de leitura a 0,1, o cálculo em unidades relativas é o seguinte.

| Cenário | Cálculo | Total |
|---|---|---:|
| Sem cache | 10 × 100 mil × 1 | 1.000 mil |
| Com cache de 5 minutos | 100 mil × 1,25 (escrita) + 9 × 100 mil × 0,1 (leituras) | 215 mil |

A redução calculada é de 78,5% sobre a entrada do prefixo. A conta considera apenas o prefixo repetido e ignora os tokens novos de cada pedido e os tokens de saída, e a primeira mensagem depois de uma pausa maior que a vida do cache paga a escrita de novo.

![À esquerda, barras com os multiplicadores do cache sobre o preço-base de entrada: escrita de 5 minutos a 1,25, escrita de 1 hora a 2, leitura a 0,1 na maioria dos modelos, 0,05 no Opus 5.5 e no Sonnet 5.5 e 0,025 no Fable 5.1. À direita, o exemplo de um prefixo de 100 mil tokens em 10 pedidos: 1.000 mil sem cache e 215 mil com cache de 5 minutos, uma redução de 78,5%.](assets/cache-em-unidades-relativas.png)

## Alavancas de redução

O guia reúne as práticas abaixo. A coluna da direita indica onde cada uma aparece num projeto com skills e agentes.

| Alavanca | O que o guia recomenda | Efeito numa skill ou agente |
|---|---|---|
| Limpar o contexto | `/clear` ao trocar de tarefa e `/compact` com instruções do que preservar | Cada execução de uma skill começa de um contexto pequeno |
| Escolher o modelo | Sonnet para a maioria das tarefas, Opus para decisões complexas, `model: haiku` em subagentes simples | O campo `model` do subagente é uma decisão de custo |
| Mover instruções para skills | `CLAUDE.md` abaixo de 200 linhas, procedimentos específicos em skills | O procedimento só ocupa contexto quando acionado |
| Delegar saída volumosa | Testes, documentação e logs em subagentes | O contexto principal recebe apenas o resumo |
| Filtrar com hooks e scripts | Um hook que filtra a saída de testes reduz o contexto de dezenas de milhares de tokens para centenas | Um script de skill devolve só o resultado |
| Reduzir o esforço | `/effort` mais baixo ou raciocínio desativado em tarefas simples | O custo de raciocínio cai nas tarefas de rotina |
| Reduzir servidores MCP | Preferir ferramentas de linha de comando e desativar servidores sem uso | Menos definições de ferramenta no contexto |
| Pedir com especificidade | Um pedido como "adicionar validação de entrada à função de login em auth.ts" exige poucas leituras, e um pedido vago como "melhorar o código" dispara varredura ampla | O pedido da skill nomeia arquivo e critério |

O guia observa que os modelos Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable sempre usam raciocínio estendido, e que nesses modelos a redução se faz pelo nível de esforço.

## Vários agentes multiplicam o custo

Os dois relatos citam multiplicadores da mesma ordem de grandeza. O [relato do sistema multiagente](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) cita cerca de 15 vezes os tokens de um chat, e o guia de custo do Claude Code cita cerca de 7 vezes os tokens de uma sessão comum para equipes de agentes em modo de plano. As duas medidas diferem em tarefa, em modelo e em configuração, e por isso servem como ordem de grandeza e não como previsão. O mesmo relato informa que o uso de tokens, sozinho, explicou 80% da variação de desempenho no benchmark BrowseComp, o que sugere que parte do ganho de qualidade é paga em tokens.

## Medir e declarar

O Claude Code mostra o consumo da sessão com `/usage`, que lista os tokens por modelo e uma estimativa em dólares calculada localmente a preço de tabela, e o estado do contexto com `/context`. O guia indica que a cifra é uma estimativa e que a fatura de referência está no Console. Cada skill ou agente deve declarar, entre os requisitos não funcionais, o orçamento de tokens por execução medido na oficina, e uma execução que ultrapasse o orçamento é um defeito a investigar.

### Orçamento da listagem de skills

Toda skill habilitada ocupa espaço na listagem de nomes e descrições carregada no início da sessão, e o orçamento dessa listagem é de 1% da janela de contexto do modelo. Cada entrada é cortada em 1.536 caracteres somando `description` e `when_to_use`, e a documentação recomenda colocar o caso de uso principal no começo. Quando a listagem estoura o orçamento, todo nome permanece, e as descrições saem primeiro das skills menos invocadas.

Os ajustes são a configuração `skillListingBudgetFraction` (por exemplo, 0.02 para 2%), a variável `SLASH_COMMAND_TOOL_CHAR_BUDGET`, com um número fixo de caracteres, e o valor `"name-only"` em `skillOverrides`, que lista a skill só pelo nome. O comando `/doctor` estima o custo da listagem, `/context` mostra o tamanho da listagem depois do orçamento, e `claude --debug` registra um aviso no log quando a listagem excede o orçamento.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** o orçamento e o corte constam de [Skill descriptions are cut short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short), e `/doctor`, `/context` e `claude --debug` são comandos do Claude Code.
    **Codex CLI:** a documentação informa orçamento de 2% da janela para a lista inicial de skills, e a execução da versão 0.140.0 registrou o aviso de que as descrições foram encurtadas para caber nesse orçamento. A fonte é [Build skills](https://learn.chatgpt.com/docs/build-skills).

### O que o Claude Code mostra do que foi carregado

O comando mais direto é `/context`, que no `claude 2.1.309` funcionou também em modo não interativo e lista as tabelas Custom Agents e Skills, cada uma com origem e custo em tokens. Na observação, os três subagentes inválidos estavam ausentes da tabela, `tool-errado` constava como carregado, e uma skill com `disable-model-invocation: true` existia na pasta e não aparecia na tabela de skills, o que confirma que o campo a retira do contexto do modelo.

| Comando | O que mostra | Evidência |
|---|---|---|
| `/context` | Subagentes e skills carregados, com origem e tokens | Observado |
| `/agents` | Na versão 2.1.309, informa que o assistente foi removido e orienta a editar `.claude/agents/` ou `~/.claude/agents/` | Observado. Até a v2.1.197 abria um assistente interativo, segundo a documentação |
| `/skills` | Indisponível em modo não interativo. O comportamento em sessão interativa não foi verificado | Observado em modo não interativo |
| `/doctor` | Estima o custo da listagem de skills e aponta nomes duplicados na mesma pasta de subagentes | Documentado |
| `claude agents` | Gerencia sessões em segundo plano e não lista subagentes | Observado em `claude --help` |

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os comandos constam de [Skill descriptions are cut short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short) e da página de [subagentes](https://code.claude.com/docs/en/sub-agents).
    **Codex CLI:** `/skills` lista e seleciona skills, `/subagents` alterna entre threads de subagentes e `/debug-config` imprime o diagnóstico das camadas de configuração, conforme a [documentação de comandos](https://learn.chatgpt.com/docs/developer-commands). O comando `codex agents` não existe na versão 0.140.0, observado em `codex --help`.

!!! abstract "Linha da ficha"
    Orçamento de tokens:

    - Qual o orçamento de tokens por execução, medido na oficina e não estimado de cabeça?
    - Que comandos medem o consumo e o que foi carregado, e quem registra o resultado?
    - A listagem de skills cabe no orçamento de 1% da janela, ou alguma `description` precisa ser encurtada?

**Próxima página:** [Performance](performance.md).
