# Exercícios

Tente responder antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Situação compartilhada

Todos os exercícios desta página se referem ao mesmo projeto do Experimento A da [Oficina de ferramentas](oficina-de-ferramentas.md#experimento-a-o-efeito-de-um-agentsmd-robusto). Se você não fez a oficina, o que está aqui é tudo o que precisa para responder.

A **Vetor** é uma plataforma fictícia de e-commerce B2B que atravessa o workshop. O projeto da oficina, `oficina-arnes`, criado do zero e sem dependências, tem uma função só: `calcularJurosAtraso(valorPedido, diasAtraso)`, que calcula juros de atraso de pedido (0,1% ao dia sobre o valor, sem juros se não houver atraso, nunca ultrapassando 20% do valor do pedido), mais o teste que comprova isso.

O arquivo de instrução do projeto é este, o mesmo do Experimento A:

```markdown
# AGENTS.md

## Processo obrigatório: TDD
Toda função nova segue o ciclo vermelho-verde-refatoração:
1. Escreva o teste que falha antes de qualquer código de implementação.
2. Escreva o mínimo de código necessário para o teste passar.
3. Refatore mantendo os testes verdes.
Nunca entregue a implementação sem o teste correspondente já escrito primeiro.

## Documentação nativa obrigatória
Toda função pública recebe documentação no formato nativo da linguagem:
- JavaScript/TypeScript: bloco JSDoc (`/** ... */`) com `@param` e `@returns`.
- C#: comentário XML (`/// <summary>`, `<param>`, `<returns>`).
Comentário de texto solto, fora desse formato, não conta como documentação.

## Comando de teste
`node --test` roda toda a suíte. Não existe passo de compilação.
```

Três fatos deste arquivo **não dá para deduzir lendo o código sozinho**, e por isso são candidatos naturais a um arquivo de instrução:

- O comando de teste é `node --test`, e não existe passo de compilação.
- Toda função nova segue TDD, com o teste escrito antes da implementação.
- Documentação de função pública precisa ser JSDoc (ou comentário XML em C#), e comentário solto não conta.

Para criar o projeto do zero:

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

A engenharia de prompt cuida do texto da instrução. A engenharia de contexto cuida de tudo que chega à janela de contexto numa execução: instruções, histórico, resultado de ferramentas, arquivos lidos. A segunda é mais ampla que a primeira, sem substituí-la.
</details>

### 5. O efeito de uma linha genérica de instrução

Um colega abre um `AGENTS.md` no projeto `oficina-arnes` e escreve uma única linha: "escreva código limpo e siga boas práticas." Explique por que essa linha não muda nenhum comportamento observável do agente, e escreva uma linha que mudaria, usando um dos três fatos da situação compartilhada.

<details>
<summary>Ver resposta</summary>

A linha genérica não informa nada que o agente já não tentasse fazer por padrão, então nenhuma decisão dele muda por causa dela. Uma linha que muda decisão responde uma pergunta concreta que o código não responde. Por exemplo: "toda função nova segue TDD: escreva o teste antes da implementação" muda a ordem real de trabalho do agente, não só o resultado final. Ou: "documentação de função pública precisa ser JSDoc, comentário solto não conta" evita um comentário de uma linha sem `@param` nem `@returns`.
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

Você tem o projeto `oficina-arnes` e o `AGENTS.md` robusto da situação compartilhada acima. Se ainda não fez a oficina, crie o projeto agora (`mkdir oficina-arnes && cd oficina-arnes && git init`), salve o arquivo de instrução, e peça ao agente a função `calcularJurosAtraso` descrita acima antes de continuar.

**Seu papel**

Você decide se esse arquivo está pronto para o time inteiro usar, ou se precisa de mais uma rodada.

**Insumos disponíveis**

O projeto `oficina-arnes`, o `AGENTS.md` da situação compartilhada e o agente que você já usa.

**Como conduzir**

1. Antes de tudo, confira que o arquivo não está mentindo: rode `node --test` e confirme que o comando existe e passa, como manda [O arquivo de instrução](arquivo-de-instrucao.md#como-saber-se-o-arquivo-ainda-funciona).
2. **Entrada.** Peça ao agente, numa conversa nova: *"Crie a função `calcularMultaCancelamento(valorPedido, diasParaEntrega)`, que cobra 10% do valor do pedido como multa se o cancelamento acontecer com menos de 2 dias para a entrega prevista, e nada caso contrário."*
3. **Resposta.** Leia o que ele produziu e confira três pontos contra o `AGENTS.md`. Ele escreveu o teste antes da implementação, ou só entregou a implementação pronta? A função tem documentação no formato nativo (JSDoc)? Ele alterou o teste de `calcularJurosAtraso` sem você ter pedido?
4. **Verificação.** Rode `node --test`. Os testes de `calcularJurosAtraso` continuam passando, e os novos testes de `calcularMultaCancelamento` passam também?

**Entrega esperada**

Um registro de três linhas: o que foi pedido, o que o agente entregou nos três pontos do passo 3, e o resultado de `node --test`.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| O arquivo foi conferido antes de ser usado | 20% | Rodou `node --test` antes de pedir a nova função, em vez de supor que o comando existia |
| Verificação real executada | 40% | Rodou `node --test` de verdade depois da entrega e relatou o resultado, inclusive quando passou |
| Diagnóstico | 40% | Se algum dos três pontos falhou, aponta se foi por faltar linha no arquivo ou por o agente ter ignorado uma linha existente |

**Como verificar antes de entregar:** o registro precisa dizer o que `node --test` respondeu depois da nova função. Se você não rodou, o exercício não está completo.

## Analisar

### 8. Diagnosticar pelo tipo de falha

No passo 3 do exercício anterior, ou alguma coisa saiu diferente do esperado, ou o agente acertou os três pontos. Nos dois casos, use a tabela de [O arnês do agente](arnes.md#diagnosticar-pelo-tipo-de-falha) e responda: se o mesmo pedido fosse feito num projeto sem nenhum arquivo de instrução, qual linha da tabela descreveria a falha mais provável, e qual seria a primeira intervenção?

### 9. Avaliando dois servidores MCP

Compare dois servidores que dão ao agente acesso ao sistema de arquivos. O primeiro é o `@modelcontextprotocol/server-filesystem` do Experimento B, mantido pelo próprio projeto do MCP e configurado para uma única pasta. O segundo é um servidor hipotético de mesma função, publicado por um terceiro desconhecido, de código fechado, que pede acesso à sua pasta pessoal inteira. Aplique os três critérios de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp) e diga em qual dos três a distância entre os dois é maior.

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
