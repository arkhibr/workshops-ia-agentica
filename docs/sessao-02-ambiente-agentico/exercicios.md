# Exercícios

Tente responder antes de abrir os blocos de feedback nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Recordar

### 1. As quatro peças

Nomeie as quatro peças de um ambiente agêntico descritas nesta sessão.

<details>
<summary>Ver resposta</summary>

Arquivo de configuração (AGENTS.md/CLAUDE.md), MCP (acesso a ferramentas externas), isolamento por ramo (worktree) e a aplicação agêntica (Claude Code, Copilot, Cursor).
</details>

### 2. O problema M×N

Em uma frase, explique o problema que o MCP resolve.

<details>
<summary>Ver resposta</summary>

Sem um protocolo comum, conectar M modelos a N ferramentas exige M×N integrações específicas. O MCP faz cada modelo e cada ferramenta implementarem o protocolo uma única vez, reduzindo a multiplicação a uma soma.
</details>

## Compreender

### 3. Prompt engineering vs. context engineering

Explique a diferença entre as duas práticas, sem usar a palavra "melhor" para nenhuma delas.

<details>
<summary>Ver resposta</summary>

Prompt engineering cuida do texto da instrução. Context engineering cuida de tudo que chega à janela de contexto numa execução — instruções, histórico, resultado de ferramentas, arquivos lidos. A segunda é mais ampla que a primeira, não uma substituta.
</details>

### 4. O efeito de uma linha genérica de instrução

Um colega escreve num AGENTS.md: "escreva código limpo e siga boas práticas." Explique por que essa linha, sozinha, não muda nenhum comportamento observável do agente.

<details>
<summary>Ver resposta</summary>

A linha não dá nenhuma informação que o agente não teria por padrão. Uma linha útil responde uma pergunta concreta que muda uma decisão real — por exemplo, qual comando roda os testes, ou qual convenção de nomenclatura o time usa.
</details>

### 5. Tool ou resource?

Um agente precisa saber, a cada execução, o status atual de um pedido num sistema externo de logística que muda várias vezes ao dia. Essa informação deveria chegar como *tool* ou como *resource*? Justifique com o critério de quem decide quando buscar a informação.

<details>
<summary>Ver resposta</summary>

*Tool*. O status muda com frequência e só é útil se buscado no momento certo, algo que o próprio agente deveria decidir durante a execução, não algo que a aplicação injeta de antemão em todo prompt. Um *resource* faz mais sentido para informação estável, sempre necessária, que não depende de o agente decidir buscar.
</details>

## Aplicar

### 6. Exercício-âncora: ciclo entrada → resposta → verificação

**O que é:** configurar um arquivo de instrução real e rodar um ciclo completo com o agente, medindo se o arquivo de fato mudou o comportamento.

**Onde encontrar:** [Oficina de ferramentas](oficina-de-ferramentas.md#experimento-a-escreva-o-agentsmd-do-seu-proprio-repositorio) já produziu um `AGENTS.md` ou `CLAUDE.md` real. Este exercício usa esse mesmo arquivo.

Antes de rodar o ciclo, aplique a verificação de [Padrões e decisões](padroes-e-decisoes.md#como-saber-se-o-arquivo-ainda-funciona): rode cada comando documentado no arquivo, um por um, e confirme que nenhum falhou antes de usar o arquivo no exercício.

**Situação**

Você tem, da oficina, um arquivo de instrução para um repositório real seu. Agora vai medir, com critério, se ele funciona.

**Seu papel**

Você é a pessoa responsável por decidir se esse arquivo está pronto para o time inteiro usar, ou se precisa de mais uma rodada.

**Insumos disponíveis**

O arquivo produzido na oficina e o próprio repositório.

**Como conduzir**

1. Escolha uma tarefa pequena e real do repositório que dependa de pelo menos uma convenção documentada no arquivo (por exemplo, uma convenção de nomenclatura ou um comando de teste específico).
2. Peça ao agente para executar essa tarefa (entrada).
3. Leia a saída do agente e verifique se ela respeitou a convenção documentada (resposta).
4. Rode o comando de verificação real do projeto (teste, lint, build) para confirmar que a saída funciona de fato, não só parece correta (verificação).

**Entrega esperada**

Um registro de três linhas: o que foi pedido, o que o agente entregou, e o resultado da verificação (passou, falhou, ou passou parcialmente).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Tarefa escolhida depende de fato de uma convenção do arquivo | 30% | Não é uma tarefa genérica que funcionaria igual sem o arquivo |
| Verificação real executada | 40% | Rodou o comando de teste/lint/build de verdade, não assumiu que passaria |
| Diagnóstico | 30% | Se falhou, aponta se foi o arquivo que estava incompleto ou o agente que ignorou a instrução |

**Como verificar antes de entregar:** confira se você rodou a verificação de fato, não só leu a saída do agente e achou que parecia certa.

## Analisar

### 7. Comparando com o exemplo da Vetor

Compare seu `AGENTS.md`/`CLAUDE.md` do exercício 6 com o exemplo mostrado em [Exemplo arquitetural](exemplo-arquitetural.md). Alguma seção do exemplo da Vetor faria sentido no seu arquivo, e não estava lá? Alguma seção sua não teria lugar no exemplo da Vetor?

### 8. Avaliando um servidor MCP antes de conectar

Escolha um servidor MCP que você usa ou pretende usar (pode ser o do rastreador de tarefas do seu time, um servidor de arquivos, ou qualquer outro). Aplique os três critérios de [Padrões e decisões](padroes-e-decisoes.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp) (origem, escopo, auditabilidade) e aponte qual dos três é o ponto mais fraco desse servidor específico hoje.

## Avaliar

### 9. O commit que sumiu

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: o time da Vetor deveria exigir worktree separado para toda tarefa, mesmo as pequenas e solo? Justifique com o critério de frequência de uso e tamanho do time, não com preferência pessoal.

## Criar

### 10. Um AGENTS.md para o time

Escreva um `AGENTS.md` de no máximo cinco linhas para um time fictício que você conhece bem (pode ser um projeto pessoal, ou um cenário hipotético). Cada linha precisa responder uma pergunta concreta que um agente teria dúvida sem ela.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
