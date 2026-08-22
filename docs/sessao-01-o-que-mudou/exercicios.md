# Exercícios

Tente responder antes de abrir os blocos de feedback nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Recordar

### 1. Três modos de trabalho

Nomeie os três modos de trabalho com IA distinguidos nesta sessão e o artefato que cada um usa para governar qualidade.

<details>
<summary>Ver resposta</summary>

Vibe coding (conversa corrente e resultado aparente), assistência de codificação (ticket, código existente e revisão do desenvolvedor) e SDD (constitution, spec, plano, tarefas, testes e gates versionados).
</details>

### 2. Aprendizado em contexto

Em uma frase, explique o que é aprendizado em contexto (in-context learning) e por que ele torna um prompt capaz de funcionar como programa.

<details>
<summary>Ver resposta</summary>

É a capacidade de um modelo executar uma tarefa nova a partir da descrição em linguagem natural e de exemplos no próprio texto de entrada, sem ajuste de peso — demonstrada por Brown et al. (2020). Sem ela, um prompt seria só um pedido; com ela, o prompt vira a própria especificação executada.
</details>

## Compreender

### 3. Por que vibe coding não é o problema

Explique por que vibe coding não é, por si, uma prática ruim — e onde exatamente ela se torna um risco.

<details>
<summary>Ver resposta</summary>

Vibe coding é legítimo para prototipagem descartável. O risco aparece quando o protótipo atravessa, sem ninguém decidir isso explicitamente, a fronteira para produto — carregando decisões que nunca chegam ao repositório.
</details>

### 4. Piso, teto e julgamento

Um colega diz: "a IA já resolve tudo, só falta ela escrever testes sozinha para eu confiar." Explique, usando os três conceitos desta sessão, o que essa frase confunde.

<details>
<summary>Ver resposta</summary>

Confunde piso (o código roda) com teto (o código está correto e testável) e ignora o julgamento humano (decidir se aquele era o problema certo, e se o teste gerado verifica o comportamento certo ou só confirma o que o código já faz).
</details>

## Aplicar

### 5. Exercício-âncora: intuição vs. prompt estruturado

**O que é:** o mesmo problema, resolvido duas vezes pelo agente, com dois níveis de contexto diferentes. A diferença entre as duas saídas mede piso e teto na prática.

**Onde encontrar:** [Exemplo arquitetural](exemplo-arquitetural.md) mostrou a regra da Vetor e uma demonstração. Aqui você repete o experimento com um cenário próprio, sem consultar a solução já mostrada.

**Situação**

A Vetor (a plataforma fictícia de e-commerce B2B usada nesta sessão) precisa da mesma função de desconto do exemplo, mas agora você vai gerá-la do zero, medindo o próprio resultado contra critérios que só serão revelados depois do primeiro prompt.

**Seu papel**

Você é o desenvolvedor responsável por essa função antes que ela vá para o checkout de produção.

**Insumos disponíveis**

Seu agente de codificação configurado na Sessão 0. Não abra [Exemplo arquitetural](exemplo-arquitetural.md) até concluir o passo 1.

**Como conduzir**

1. Peça ao agente: "Escreva uma função que calcula o desconto de um pedido baseado no valor total." Guarde a saída completa.
2. Agora abra a regra de negócio completa em [Exemplo arquitetural](exemplo-arquitetural.md#a-regra-de-negocio-completa) e reescreva o pedido incorporando a regra inteira — contexto de domínio, assinatura-alvo, faixas, teto, variação por tipo de cliente. Guarde a saída completa.
3. Rode os casos de teste abaixo contra as duas saídas.

| # | Valor do pedido | Tipo de cliente | Desconto esperado |
|---|---|---|---|
| 1 | R$ 300,00 | padrão | R$ 0,00 |
| 2 | R$ 1.000,00 | padrão | R$ 50,00 |
| 3 | R$ 6.000,00 | padrão | R$ 900,00 |
| 4 | R$ 8.000,00 | padrão | R$ 1.000,00 (teto) |
| 5 | R$ 12.000,00 | atacado | R$ 1.000,00 (teto) |

**Entrega esperada**

As duas saídas (passos 1 e 2) e uma tabela marcando quais dos cinco casos cada versão passa.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Execução dos dois prompts | 20% | As duas saídas foram geradas e preservadas, sem edição manual |
| Verificação dos cinco casos | 40% | Cada caso foi de fato testado contra as duas saídas, não estimado |
| Diagnóstico | 40% | Aponta com precisão qual caso revela a diferença e por que (regra de negócio ausente do primeiro prompt, não "o modelo errou") |

**Como verificar antes de entregar:** confira se os casos 4 e 5 (os que dependem do teto e do tipo de cliente) foram mesmo testados, não só assumidos como corretos.

## Analisar

### 6. Comparando com o exemplo da Vetor

Compare sua saída do prompt intuitivo (exercício 5) com a saída demonstrada em [Exemplo arquitetural](exemplo-arquitetural.md). As duas erraram nos mesmos casos? Se não, qual regra de negócio cada uma perdeu de forma diferente?

## Avaliar

### 7. A proibição total

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: a Vetor deveria proibir vibe coding para todo tipo de tarefa, incluindo scripts internos de uso único? Justifique com o critério de reversibilidade e tempo de vida, não com preferência pessoal.

## Criar

### 8. Checklist de time

Escreva um checklist de no máximo cinco itens que qualquer prompt de geração de código na Vetor deveria atender antes de ser aceito em produção. Cada item precisa ser verificável por outra pessoa, não uma intenção vaga como "ser claro".

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
