# Custo de tokens

O custo de uma skill ou de um agente cresce com o tamanho do contexto enviado a cada pedido e com o número de pedidos, e por isso precisa ser declarado como requisito antes da construção. Esta página apresenta de onde o custo vem, o efeito do cache de prompt em unidades relativas e as alavancas de redução que o guia de custo do Claude Code documenta.

## De onde o custo vem

O Claude Code cobra pelo consumo de tokens da API. O [guia de custo](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) informa que, em implantações corporativas, a média é de cerca de US$ 13 por desenvolvedor por dia ativo e de US$ 150 a US$ 250 por mês, e que o custo fica abaixo de US$ 30 por dia ativo para 90% dos usuários. Esses valores são médias de uso geral e variam com o modelo, o tamanho do código e o uso de várias instâncias ou de automação.

A causa principal é o contexto. Cada pedido carrega a conversa inteira, e cada uso de ferramenta gera outro pedido com os resultados acumulados. Uma sessão aberta por horas pode, assim, consumir mais do que a atividade da pessoa sugere. O guia lista, além do contexto longo, as falhas de cache após uma pausa maior que a vida do cache, as tarefas agendadas que reenviam o contexto a cada disparo, cada subagente e cada integrante de uma equipe de agentes, e a compactação, que é em si um pedido grande.

Os tokens de raciocínio estendido são cobrados como tokens de saída, e o orçamento padrão pode chegar a dezenas de milhares de tokens por pedido, conforme o modelo.

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

**Próxima página:** [Performance](performance.md).
