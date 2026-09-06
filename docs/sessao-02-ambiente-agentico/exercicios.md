# Exercícios

Tente responder antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Situação compartilhada

Todos os exercícios desta página se referem ao mesmo projeto da [Oficina de ferramentas](oficina-de-ferramentas.md). Se você não fez a oficina, o que está aqui é tudo o que precisa para responder.

A **Vetor** é uma plataforma fictícia de e-commerce B2B que atravessa o workshop. A versão executável dela está em `exemplo/vetor`, dentro do repositório do workshop, e cabe em três arquivos:

- `src/desconto.js` calcula o desconto de um pedido por faixa de valor: nada até R$ 500,00, 5% até R$ 2.000,00, 10% até R$ 5.000,00 e 15% acima disso, com teto de R$ 1.000,00 por pedido.
- `test/desconto.test.js` tem seis testes cobrindo as quatro faixas, o teto e a entrada inválida.
- `package.json` define `npm test` e nenhuma dependência.

Três fatos do projeto que **não dá para deduzir lendo o código**, e que por isso são candidatos naturais a entrar num arquivo de instrução: o comando de teste é `npm test` e não existe compilação; `tipoCliente` chega sempre em minúsculas, `'padrao'` ou `'atacado'`; e `calcularDesconto` recebe `tipoCliente` sem usar, porque a faixa de 20% para atacado acima de R$ 10.000,00 ainda não foi implementada.

Para clonar:

```bash
git clone https://github.com/arkhibr/workshops-ia-agentica.git
cd workshops-ia-agentica/exemplo/vetor && npm test
```

## Recordar

### 1. As quatro peças

Nomeie as quatro peças de um ambiente agêntico descritas nesta sessão.

<details>
<summary>Ver resposta</summary>

Arquivo de configuração (AGENTS.md/CLAUDE.md), MCP (acesso a ferramentas externas), isolamento por ramo (worktree) e a aplicação agêntica (Claude Code, Copilot, Cursor).
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

A engenharia de prompt cuida do texto da instrução. A engenharia de contexto cuida de tudo que chega à janela de contexto numa execução: instruções, histórico, resultado de ferramentas, arquivos lidos. A segunda é mais ampla que a primeira, e não uma substituta.
</details>

### 5. O efeito de uma linha genérica de instrução

Um colega abre um `AGENTS.md` no projeto Vetor e escreve uma única linha: "escreva código limpo e siga boas práticas." Explique por que essa linha não muda nenhum comportamento observável do agente, e escreva uma linha que mudaria, usando um dos três fatos da situação compartilhada.

<details>
<summary>Ver resposta</summary>

A linha genérica não informa nada que o agente já não tentasse fazer por padrão, então nenhuma decisão dele muda por causa dela. Uma linha que muda decisão responde uma pergunta concreta que o código não responde. Por exemplo: "o comando de teste é `npm test`; não existe script de compilação" evita que o agente invente um `npm run build` inexistente. Ou: "`tipoCliente` chega em minúsculas, `'padrao'` ou `'atacado'`" evita a comparação com `'Atacado'`.
</details>

### 6. Tool ou resource?

A Vetor quer que o agente consulte o status de entrega de um pedido no sistema do transportador parceiro, que muda várias vezes ao dia e não existe no repositório. Essa informação deveria chegar como *tool* ou como *resource*? Justifique pelo critério de quem decide o momento de buscar.

<details>
<summary>Ver resposta</summary>

*Tool*. O status muda com frequência e só serve se buscado no momento em que a pergunta aparece, decisão que cabe ao agente durante a execução. Um *resource* faz mais sentido para informação estável e sempre necessária, que a aplicação injeta de antemão sem gastar uma chamada de ferramenta.
</details>

## Aplicar

### 7. Exercício-âncora: ciclo entrada → resposta → verificação

**O que é:** medir, com critério, se um arquivo de instrução muda mesmo o comportamento do agente, num ciclo completo de entrada, resposta e verificação.

**Situação**

Você tem o projeto `exemplo/vetor` clonado e o `AGENTS.md` que escreveu no [Experimento A da oficina](oficina-de-ferramentas.md#experimento-a-escreva-o-agentsmd-do-projeto-vetor). Se não fez a oficina, escreva agora um `AGENTS.md` de até quatro linhas usando os três fatos da situação compartilhada.

**Seu papel**

Você decide se esse arquivo está pronto para o time inteiro usar, ou se precisa de mais uma rodada.

**Insumos disponíveis**

O projeto `exemplo/vetor` no estado original, que `git checkout -- src/ test/` sempre devolve, o seu `AGENTS.md` e o agente que você já usa.

**Como conduzir**

1. Antes de tudo, confira que o arquivo não está mentindo: rode cada comando que ele documenta e confirme que todos existem, como manda [O arquivo de instrução](arquivo-de-instrucao.md#como-saber-se-o-arquivo-ainda-funciona).
2. **Entrada.** Peça ao agente: *"Implemente a faixa de atacado de 20% acima de R$ 10.000,00 em `calcularDesconto`, com testes."*
3. **Resposta.** Leia o que ele produziu e confira três pontos contra a situação compartilhada. O valor comparado em `tipoCliente` está em minúsculas? O teto de R$ 1.000,00 continua valendo para a faixa nova? Ele alterou arquivos de `test/` que você não pediu para alterar?
4. **Verificação.** Rode `npm test`. Os seis testes originais continuam passando, ou a mudança quebrou algum?

**Entrega esperada**

Um registro de três linhas: o que foi pedido, o que o agente entregou nos três pontos do passo 3, e o resultado de `npm test`.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| O arquivo foi conferido antes de ser usado | 20% | Rodou os comandos documentados, em vez de supor que existiam |
| Verificação real executada | 40% | Rodou `npm test` de verdade e relatou o resultado, inclusive quando passou |
| Diagnóstico | 40% | Se algum dos três pontos falhou, aponta se faltou linha no arquivo ou se o agente ignorou uma linha existente |

**Como verificar antes de entregar:** o registro precisa dizer o que `npm test` respondeu. Se você não rodou, o exercício não está completo.

## Analisar

### 8. Diagnosticar pelo tipo de falha

No passo 3 do exercício anterior, ou alguma coisa saiu diferente do esperado, ou o agente acertou os três pontos. Nos dois casos, use a tabela de [O arnês do agente](arnes.md#diagnosticar-pelo-tipo-de-falha) e responda: se o mesmo pedido fosse feito num projeto sem nenhum arquivo de instrução, qual linha da tabela descreveria a falha mais provável, e qual seria a primeira intervenção?

### 9. Avaliando dois servidores MCP

Compare dois servidores que dão ao agente acesso ao sistema de arquivos. O primeiro é o `@modelcontextprotocol/server-filesystem` do Experimento B, mantido pelo próprio projeto do MCP e configurado para uma única pasta. O segundo é um servidor hipotético de mesma função, publicado por um terceiro desconhecido, de código fechado, que pede acesso à sua pasta pessoal inteira. Aplique os três critérios de [MCP e ferramentas externas](mcp.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp) e diga em qual dos três a distância entre os dois é maior.

### 10. O que o seu arquivo tem que o exemplo não tem

Compare o `AGENTS.md` que você escreveu com o arquivo mostrado em [Exemplo arquitetural](exemplo-arquitetural.md). Alguma seção de lá faria sentido no seu e não estava presente? Alguma linha sua não teria lugar lá, e por quê?

## Avaliar

### 11. O commit que sumiu

No [Estudo de caso](estudo-de-caso.md) desta sessão, dois desenvolvedores da Vetor rodaram agentes ao mesmo tempo no mesmo diretório de trabalho, e a alteração de um desapareceu sem que ninguém percebesse na hora. Em até 100 palavras, defenda uma posição: o time deveria exigir worktree separado para toda tarefa, inclusive as pequenas e feitas por uma pessoa só? Justifique pelos critérios de tamanho de time e frequência de uso da tabela de [O ambiente compartilhado](ambiente-compartilhado.md#quando-vale-configurar-um-ambiente-compartilhado), em vez de preferência pessoal.

## Criar

### 12. Um AGENTS.md para o módulo novo

A Vetor vai ganhar um segundo módulo, de cálculo de frete, com estas características: fica em `src/frete.js`, usa a mesma convenção de valores em reais, depende de uma tabela de CEP que muda toda semana num sistema externo, e nunca deve arredondar valor para cima.

Escreva o `AGENTS.md` desse módulo, com no máximo cinco linhas. Cada linha precisa responder uma pergunta que o agente teria de verdade, e pelo menos uma delas precisa resolver se a tabela de CEP entra no arquivo de instrução ou pede um servidor MCP.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
