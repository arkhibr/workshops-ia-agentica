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

### 3. O limite entre vibe coding legítimo e arriscado

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

### 6. Exercício de aplicação: classifique três tarefas reais do seu backlog

**O que é:** a atividade de 20 minutos em que a tabela de critérios sai do slide e encosta no trabalho que você tem para fazer nesta semana. Vale para qualquer repositório, inclusive privado, porque nada aqui exige mostrar código.

**Situação**

Você tem um backlog real, com tarefas de tamanhos e riscos diferentes. A tabela de cinco critérios de [Modos de trabalho com IA](modos-de-trabalho.md#quando-cada-modo-se-justifica) diz qual modo cada tarefa pede. O que este exercício mede é se você consegue aplicar a tabela quando a resposta não é óbvia.

**Seu papel**

Você decide, por escrito e antes de abrir o agente, como vai atacar cada uma das três tarefas, e depois defende essa decisão para um colega que não conhece o seu sistema.

**Insumos disponíveis**

Seu próprio backlog, a tabela de cinco critérios e um colega de dupla. Nenhum código precisa ser exibido: as tarefas são descritas em uma linha cada.

**Como conduzir**

**Etapa 1 — Levantamento (5 min, individual).** Escreva três tarefas reais do seu backlog, uma linha cada, escolhidas assim: uma que você faria hoje sem pensar duas vezes com vibe coding, uma que pediria assistência de codificação com revisão, e uma que você suspeita que exija SDD. Se não conseguir preencher as três, a lacuna já é um achado: registre qual faltou.

**Etapa 2 — Classificação (7 min, individual).** Escolha a tarefa sobre a qual você tem *menos* certeza e preencha a tabela abaixo para ela. Feche com duas frases: qual modo você vai usar e por quê.

| Critério | A tarefa é... | Puxa para |
|---|---|---|
| Reversibilidade | fácil ou difícil de desfazer depois de pronta? | fácil → vibe coding · difícil → SDD |
| Tempo de vida | descartável ou vai durar meses no sistema? | descartável → vibe coding · duradoura → SDD |
| Quantas pessoas mexem depois | só você ou o time inteiro? | só você → vibe coding · time → SDD |
| Regra de negócio | tem regra que só existe na cabeça de alguém? | não tem → vibe coding · tem → SDD |
| Familiaridade com o código | você conhece bem essa parte do sistema? | conhece → vibe coding · não conhece → SDD |

**Etapa 3 — Defesa em dupla (6 min).** Troque a classificação com um colega. Cada um defende a decisão do outro contra os cinco critérios, procurando a linha em que discordaria. O objetivo não é convencer: é achar o critério que não é autoevidente.

**Etapa 4 — Divergências (2 min, plenário).** Só as discordâncias vão para o plenário. Elas mostram onde a tabela precisa de julgamento e onde ela decide sozinha.

**Entrega esperada**

As três tarefas em uma linha cada, a tabela preenchida para a tarefa escolhida, as duas frases de decisão, e o critério em que a dupla divergiu (ou a confirmação de que não divergiu em nenhum).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| As três tarefas são reais e distintas em risco | 20% | Vieram do backlog de verdade e não são três variações da mesma coisa |
| A classificação usa os cinco critérios | 40% | Cada linha da tabela foi respondida para a tarefa escolhida, inclusive as que puxam para lados opostos |
| A decisão é justificada pelos critérios | 20% | As duas frases citam as linhas que pesaram, e não preferência pessoal ou hábito |
| A divergência foi examinada | 20% | Nomeia o critério em que a dupla discordou e por quê, ou registra que a leitura foi idêntica nos cinco |

**Como verificar antes de entregar:** se todas as cinco linhas apontaram para o mesmo modo, você provavelmente escolheu a tarefa fácil. Troque pela que estava em segundo lugar na sua lista de incerteza.

!!! tip "Depois da aula"
    Rode a tarefa no modo que você decidiu e compare: o resultado confirmou a classificação, ou revelou que ela pedia mais cuidado do que você achava? Essa comparação é a que faz o critério grudar.

## Analisar

### 7. Comparando com o exemplo da Vetor

Compare sua saída do prompt intuitivo (exercício 5) com a saída demonstrada em [Exemplo arquitetural](exemplo-arquitetural.md). As duas erraram nos mesmos casos? Se não, qual regra de negócio cada uma perdeu de forma diferente?

## Avaliar

### 8. A proibição total

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: a Vetor deveria proibir vibe coding para todo tipo de tarefa, incluindo scripts internos de uso único? Justifique com o critério de reversibilidade e tempo de vida, não com preferência pessoal.

## Criar

### 9. Checklist de time

Escreva um checklist de no máximo cinco itens que qualquer prompt de geração de código na Vetor deveria atender antes de ser aceito em produção. Cada item precisa ser verificável por outra pessoa, não uma intenção vaga como "ser claro".

### 10. Desafio: um ciclo avaliador-otimizador para a função de desconto

**Nível:** mais exigente que os demais exercícios desta sessão. Combina o padrão avaliador-otimizador de [Sistemas agênticos e simplicidade](sistemas-agenticos.md#o-principio-de-simplicidade) com o cenário do exercício-âncora.

Você já gerou, no exercício 5, duas versões da função de desconto: uma a partir do prompt intuitivo, outra do prompt estruturado. Neste desafio, você vai usar o próprio agente para descobrir os erros da primeira versão, sem revelar a ele quais casos falham.

**Execute:**

1. Volte à saída do prompt intuitivo (exercício 5, passo 1). Não abra de novo a tabela de 5 casos de teste.
2. Numa nova interação, peça ao agente para atuar como revisor crítico dessa função: cole a regra de negócio completa de [Exemplo arquitetural](exemplo-arquitetural.md#a-regra-de-negocio-completa) e peça que ele aponte todos os casos em que a função produz um valor errado. Não mencione o teto nem o tipo de cliente atacado — deixe o agente encontrar sozinho.
3. Compare os casos que o agente encontrou sozinho com os 5 casos de teste oficiais do exercício 5. Ele achou os dois casos-armadilha (teto e atacado)?
4. Peça ao agente para corrigir a função com base na própria crítica, sem que você aponte a correção.

**Entrega esperada:** a crítica do passo 2, a comparação do passo 3, e a versão corrigida do passo 4, testada contra os 5 casos oficiais.

**Por que isso é mais difícil:** nos exercícios anteriores, você forneceu a regra de negócio completa de uma vez. Aqui, o agente precisa descobrir sozinho onde a primeira versão falha, o papel de "avaliador" do padrão visto em Padrões e decisões, e você precisa julgar se a autocrítica dele foi rigorosa ou só superficial.

<details>
<summary>O que evidencia um bom resultado</summary>

O agente identificou pelo menos o caso do teto ou o caso do cliente atacado sem que fossem mencionados no prompt. Se não identificou nenhum dos dois, isso também é um resultado válido para discutir: ciclo de autocrítica não garante pegar tudo, e é por isso que a verificação por teste automatizado continua necessária mesmo com um passo de revisão a mais.
</details>

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
