# Exercícios

Responda antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples, recordar, ao mais exigente, criar.

## Situação compartilhada

Todos os exercícios desta página usam o mesmo caso da [Oficina de ferramentas](oficina-de-ferramentas.md#o-caso-fechamento-de-descontos-da-vetor). Se você não fez a oficina, o que está aqui basta para responder.

A **Vetor** é uma empresa fictícia de e-commerce B2B, usada nos exemplos deste workshop. Ela classifica cada cliente como padrão ou atacado, e dá desconto por faixa de valor do pedido. A pasta da oficina, `oficina-arnes`, tem uma planilha do Excel, `pedidos-setembro.xlsx`, com 22 pedidos de setembro de 2026. Três deles estão cancelados, então 19 entram no fechamento, que soma **R$ 68.668,44**.

O arquivo de instrução do projeto é este, o mesmo da oficina:

```markdown
# AGENTS.md

## O que este projeto entrega
O fechamento mensal de descontos da Vetor. O entregável é sempre uma pasta de
trabalho do Excel (`.xlsx`), nunca um relatório em texto na conversa.

## Stack permitido
Scripts auxiliares em JavaScript, com Node.js 20 e a biblioteca `exceljs`.
Este projeto não usa Python em nenhuma hipótese.

## Regras de desconto da Vetor
- O valor bruto do pedido é a quantidade vezes o valor unitário.
- Até R$ 500,00 de valor bruto, nenhum desconto.
- De R$ 500,01 a R$ 2.000,00, 5%.
- De R$ 2.000,01 a R$ 5.000,00, 10%.
- Acima de R$ 5.000,00, 15%.
- Cliente atacado tem uma faixa a mais: 20% acima de R$ 10.000,00.
- O desconto nunca passa de R$ 1.000,00 por pedido, em nenhuma faixa.
- Pedido com status `cancelado` fica fora do fechamento.

## Formato da pasta de trabalho
Três abas, nesta ordem: `Pedidos` (os dados de origem, sem alteração),
`Fechamento` (uma linha por pedido elegível, com valor bruto, faixa aplicada,
desconto e valor final) e `Resumo` (uma linha por cliente, com o total final).

## Aba Conferência obrigatória
Toda entrega inclui uma quarta aba, `Conferência`, com estes seis números,
calculados a partir da aba `Pedidos`:
- linhas lidas
- pedidos cancelados
- pedidos elegíveis
- pedidos com data fora do mês de fechamento
- pedidos com valor unitário negativo
- soma da coluna de valor final da aba `Fechamento`

Se qualquer uma das duas contagens de anomalia for maior que zero, liste na
conversa os pedidos envolvidos e pare antes de declarar o fechamento pronto.
```

Quatro fatos deste arquivo **não dá para deduzir olhando a planilha de pedidos**, e por isso são candidatos naturais a um arquivo de instrução:

- As faixas de desconto e o arredondamento para baixo em múltiplos de R$ 0,50.
- Que pedido cancelado fica fora do fechamento.
- Que o projeto resolve em JavaScript com `exceljs`, e nunca em Python.
- Que nenhuma entrega é considerada pronta sem a aba `Conferência` conferida.

Para montar o caso do zero, salve o CSV publicado na [oficina](oficina-de-ferramentas.md#o-caso-fechamento-de-descontos-da-vetor) dentro de uma pasta nova:

```bash
mkdir oficina-arnes && cd oficina-arnes
git init
```

## Recordar

### 1. As quatro peças

Nomeie as quatro peças de um ambiente agêntico descritas nesta sessão.

<details>
<summary>Ver resposta</summary>

Arquivo de configuração (AGENTS.md/CLAUDE.md), MCP (acesso a ferramentas externas), isolamento por ramo (worktree) e a aplicação agêntica (Claude Code, Codex CLI, Gemini CLI).
</details>

### 2. A equação do arnês

Complete: agente = modelo + ______. E diga qual das quatro peças do exercício anterior fica de fora desse segundo termo.

<details>
<summary>Ver resposta</summary>

Agente = modelo + **arnês**. Nenhuma das quatro peças fica de fora: as quatro são arnês. O que fica de fora é o modelo, que não está entre elas.
</details>

### 3. O problema M×N

Em uma frase, explique o problema que o MCP resolve.

<details>
<summary>Ver resposta</summary>

Sem um protocolo comum, conectar M modelos a N ferramentas exige M×N integrações específicas. O MCP faz cada modelo e cada ferramenta implementarem o protocolo uma única vez, reduzindo a multiplicação a uma soma.
</details>

## Compreender

### 4. Engenharia de prompt vs. engenharia de contexto

Explique a diferença entre as duas práticas, sem usar a palavra "melhor" para nenhuma delas.

<details>
<summary>Ver resposta</summary>

A engenharia de prompt cuida do texto da instrução. A engenharia de contexto cuida de tudo que chega à janela de contexto numa execução: instruções, histórico, resultado de ferramentas, arquivos lidos. A segunda é mais ampla que a primeira, e continua precisando dela.
</details>

### 5. O efeito de uma linha genérica de instrução

Um colega abre um `AGENTS.md` na pasta `oficina-arnes` e escreve uma única linha: "gere planilhas de qualidade e siga boas práticas de negócio." Explique por que essa linha não muda nenhum comportamento observável do agente, e escreva uma linha que mudaria, usando um dos quatro fatos da situação compartilhada.

<details>
<summary>Ver resposta</summary>

A linha genérica não informa nada que o agente já não tentasse fazer, então nenhuma decisão dele muda por causa dela. Uma linha que muda decisão responde uma pergunta cuja resposta só existe dentro da Vetor. Por exemplo: "o desconto nunca passa de R$ 1.000,00 por pedido" decide um número que o agente chutaria de outro jeito. Ou: "cliente atacado tem uma faixa de 20% acima de R$ 10.000,00", que nenhum prior de mercado adivinha.
</details>

### 6. Tool ou resource?

A Vetor quer que o agente consulte o status de entrega de um pedido no sistema do transportador parceiro, que muda várias vezes ao dia e não existe no repositório. Essa informação deveria chegar como *tool* ou como *resource*? Justifique pelo critério de quem decide o momento de buscar.

<details>
<summary>Ver resposta</summary>

*Tool*. O status muda com frequência e só serve se buscado no momento em que a pergunta aparece, decisão que cabe ao agente durante a execução. Um *resource* faz mais sentido para informação estável e sempre necessária, que a aplicação injeta de antemão sem gastar uma chamada de ferramenta.
</details>

## Aplicar

### 7. Exercício-âncora: ciclo entrada → resposta → verificação

**O que é:** um ciclo completo de entrada, resposta e verificação, para medir se um arquivo de instrução muda mesmo o comportamento do agente.

**Situação**

A Vetor mudou uma regra a partir de outubro: o teto de desconto sobe de R$ 1.000,00 para R$ 1.500,00 por pedido. As faixas continuam iguais. Você tem a pasta `oficina-arnes`, a planilha de pedidos e o `AGENTS.md` da situação compartilhada.

**Seu papel**

Você decide se esse arquivo de instrução está pronto para o time inteiro usar, ou se precisa de mais uma rodada.

**Insumos disponíveis**

A pasta `oficina-arnes`, a planilha `pedidos-setembro.xlsx`, o `AGENTS.md` da situação compartilhada e o agente que você já usa.

**Como conduzir**

1. Antes de tudo, confira que o arquivo ainda descreve a realidade. Rode o fechamento uma vez com as regras atuais e confirme que o total bate com os R$ 68.668,44 da situação compartilhada, como manda [O arquivo de instrução](arquivo-de-instrucao.md#como-saber-se-o-arquivo-ainda-funciona). Se o resultado não reproduz a regra escrita, tudo que vier depois mede outra coisa.
2. **Entrada.** Edite o `AGENTS.md` para refletir o teto novo, e peça ao agente, numa conversa nova: *"Refaça o fechamento com as regras atuais do AGENTS.md."*
3. **Resposta.** Confira três pontos contra o arquivo de instrução. Ele aplicou o teto novo nos cinco pedidos que batiam no teto antigo? Ele deixou intactos os pedidos cujo desconto já era menor que R$ 1.000,00? Ele alterou a aba `Pedidos`, que o arquivo manda preservar sem alteração?
4. **Verificação.** Abra a aba `Conferência`. O total final correto depois da mudança é **R$ 66.600,44**, sobre os mesmos 19 pedidos elegíveis. Se a sua planilha mostrar outro número, decida se o erro está na regra que você escreveu ou no que o agente fez com ela.

**Entrega esperada**

Um registro de três linhas: o que foi pedido, o que o agente entregou nos três pontos do passo 3, e o total final que apareceu na aba `Conferência`.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| O arquivo foi conferido antes de ser usado | 20% | Rodou o fechamento com as regras antigas e confirmou os R$ 68.668,44 antes de mudar qualquer coisa |
| Verificação real executada | 40% | Comparou o total da aba `Conferência` contra o número esperado e relatou o resultado, inclusive quando bateu |
| Diagnóstico | 40% | Se algum dos três pontos falhou, aponta se foi por faltar precisão na linha que você escreveu ou por o agente ter ignorado uma linha existente |

**Como verificar antes de entregar:** o registro precisa dizer que número apareceu na aba `Conferência`. Se você não abriu a planilha, o exercício não está completo.

**Onde olhar primeiro:** o total cai R$ 2.068,00 em relação a setembro, que é exatamente R$ 500,00 a mais de desconto em cada um dos quatro pedidos que batiam no teto, mais R$ 68,00 no pedido VT-1014, cujo desconto de 15% dá R$ 1.068,00 e agora cabe inteiro dentro do teto novo. Papelaria Sul e Farmácia Tavares não mudam, porque nenhum pedido delas chegava perto de R$ 1.000,00 de desconto.

## Analisar

### 8. Diagnosticar pelo tipo de falha

No passo 3 do exercício anterior, o agente acertou os três pontos ou errou algum. Nos dois casos, use a tabela de [O arnês do agente](arnes.md#diagnosticar-pelo-tipo-de-falha) e responda: se o mesmo pedido fosse feito num projeto sem nenhum arquivo de instrução, qual linha da tabela descreveria a falha mais provável, e qual seria a primeira intervenção?

### 9. Avaliando dois servidores MCP

Compare dois servidores que dão ao agente acesso ao sistema de arquivos. O primeiro é o `@modelcontextprotocol/server-filesystem` da rodada 3 da oficina, mantido pelo próprio projeto do MCP e configurado para uma única pasta. O segundo é um servidor hipotético de mesma função, publicado por um terceiro desconhecido, de código fechado, que pede acesso à sua pasta pessoal inteira. Aplique os três critérios de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp) e diga em qual dos três a distância entre os dois é maior.

### 10. O que o seu arquivo tem que o exemplo não tem

Compare o `AGENTS.md` que você escreveu com o arquivo de [Exemplo arquitetural](exemplo-arquitetural.md). Alguma seção de lá faria sentido no seu e ficou faltando? Alguma linha sua ficaria deslocada lá, e por quê?

## Avaliar

### 11. O commit que sumiu

No [Estudo de caso](estudo-de-caso.md) desta sessão, dois desenvolvedores da Vetor rodaram agentes ao mesmo tempo no mesmo diretório de trabalho, e a alteração de um desapareceu sem que ninguém percebesse na hora. Em até 100 palavras, defenda uma posição: o time deveria exigir worktree separado para toda tarefa, inclusive as pequenas e feitas por uma pessoa só? Justifique pelos critérios de tamanho de time e frequência de uso da tabela de [O ambiente compartilhado](ambiente-compartilhado.md#quando-vale-configurar-um-ambiente-compartilhado).

## Criar

### 12. Um AGENTS.md para o módulo novo

A Vetor vai ganhar um segundo módulo, de cálculo de frete, com estas características: fica em `src/frete.js`, usa a mesma convenção de valores em reais, depende de uma tabela de CEP que muda toda semana num sistema externo, e nunca deve arredondar valor para cima.

Escreva o `AGENTS.md` desse módulo, com no máximo cinco linhas. Cada linha precisa responder uma pergunta que o agente faria de fato, e pelo menos uma delas precisa resolver se a tabela de CEP entra no arquivo de instrução ou pede um servidor MCP.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
