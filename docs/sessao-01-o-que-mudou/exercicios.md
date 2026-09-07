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

É a capacidade de um modelo executar uma tarefa nova a partir da descrição em linguagem natural e de exemplos no próprio texto de entrada, sem ajuste de peso — demonstrada por [Brown et al. (2020)](../referencia/bibliografia.md#brown-et-al-language-models-are-few-shot-learners-2020). Sem ela, um prompt seria só um pedido; com ela, o prompt vira a própria especificação executada.
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

**Antes de começar: por que a ordem importa.** Este exercício só mede alguma coisa se o passo 1 for executado sem conhecer a regra completa do passo 2. Ler a regra antes, ou pular direto para o prompt estruturado porque "já sacou o padrão" do Exemplo arquitetural, apaga a distância entre as duas saídas — e essa distância é justamente o que o exercício quer que você veja no seu próprio trabalho. Role a página na ordem, não abra o bloco "Regra completa" abaixo antes de terminar o passo 1, e não peça ajuda a quem já fez o exercício.

**Situação**

A Vetor (a plataforma fictícia de e-commerce B2B usada nesta sessão) também calcula frete, uma regra diferente da função de desconto vista no [Exemplo arquitetural](exemplo-arquitetural.md) — o exemplo não revela nada sobre como o frete funciona. Você vai gerar essa função do zero, medindo o próprio resultado contra critérios que só serão revelados depois do primeiro prompt.

**Seu papel**

Você é o desenvolvedor responsável por essa função antes que ela vá para o checkout de produção.

**Insumos disponíveis**

Seu agente de codificação configurado na Sessão 0.

**Como conduzir**

**Passo 1 — prompt vago.** Peça ao agente: "Escreva uma função que calcula o frete de um pedido com base no peso total." Guarde a saída completa e literal — não resuma, não edite, não complete de memória o que o agente respondeu.

**Passo 2 — abra a regra e reescreva o pedido.** Abra o bloco abaixo e reescreva o pedido incorporando a regra inteira — contexto de domínio, assinatura-alvo, faixas de peso, isenção condicional, recargo regional. Guarde a saída completa.

??? note "Regra completa da Vetor para frete — abra só depois de concluir o passo 1"
    Tabela de frete por peso total do pedido:

    | Peso total do pedido | Frete base |
    |---|---|
    | Até 5 kg | R$ 15,00 |
    | De 5,01 a 20 kg | R$ 35,00 |
    | De 20,01 a 50 kg | R$ 70,00 |
    | Acima de 50 kg | R$ 120,00 |

    Duas exceções que **interagem** entre si, não duas regras isoladas:

    - Pedidos com valor de produtos ≥ R$ 800,00 têm frete grátis — **exceto** se o pedido contiver item da categoria "frágil": nesse caso a isenção é negada, e o frete nunca é menor que R$ 50,00, mesmo que a faixa de peso indicasse um valor menor.
    - Entregas para a região Norte recebem recargo de 30% sobre o frete **já calculado** — depois de aplicar a isenção e o piso de item frágil, nunca sobre o frete base isolado.

**Passo 3 — rode os casos de teste.** Rode a tabela abaixo contra as duas saídas.

| # | Peso total | Valor de produtos | Item frágil? | Região | Frete esperado |
|---|---|---|---|---|---|
| 1 | 3 kg | R$ 200,00 | Não | Sudeste | R$ 15,00 |
| 2 | 3 kg | R$ 900,00 | Não | Sudeste | R$ 0,00 (isenção) |
| 3 | 3 kg | R$ 900,00 | Sim | Sudeste | R$ 50,00 (isenção negada, piso aplicado) |
| 4 | 25 kg | R$ 200,00 | Não | Norte | R$ 91,00 (faixa 20–50 kg + recargo) |
| 5 | 3 kg | R$ 900,00 | Sim | Norte | R$ 65,00 (piso de frágil + recargo, nessa ordem) |

**Entrega esperada**

As duas saídas (passos 1 e 2), sem edição, e uma tabela marcando quais dos cinco casos cada versão passa. Cole a saída bruta do agente, não uma descrição do que ele fez.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Execução dos dois prompts, na ordem, sem espiar a regra antes do passo 1 | 20% | As duas saídas foram geradas e preservadas, sem edição manual, e a saída do passo 1 não usa nenhum termo da regra que só aparece no bloco oculto (ex.: "frágil", "Norte", "30%") |
| Verificação dos cinco casos | 40% | Cada caso foi de fato testado contra as duas saídas, não estimado |
| Diagnóstico | 40% | Aponta com precisão qual caso revela a diferença e por que — em especial o caso 5, o único em que as duas exceções se cruzam |

**Como verificar antes de entregar:** confira se o caso 5 (o único em que isenção negada, piso e recargo regional se compõem ao mesmo tempo) foi mesmo testado, não só assumido como correto. Se a sua saída do passo 1 já continha a palavra "frágil" ou tratava a região Norte de forma diferente, você provavelmente abriu a regra antes da hora — refaça o passo 1 puro, porque o dado da comparação ficou contaminado.

!!! tip "Reforço para o facilitador"
    Peça a duas ou três pessoas para lerem em voz alta, sem preparar, a saída do passo 1. Quem abriu a regra antes da hora tende a produzir uma função "genérica correta demais" para não ter visto nada — vocabulário de domínio (peso, frágil, região) aparecendo sem que a regra tenha sido mostrada é o sinal de alerta.

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

### 7. Dois tipos de lacuna de contexto

O [Exemplo arquitetural](exemplo-arquitetural.md) (desconto) e o exercício-âncora (exercício 5, frete) perdem regra de negócio por motivos diferentes. No desconto, o prompt vago esquece uma faixa e ignora um teto: falta uma informação isolada, fácil de apontar depois. No frete, mesmo um prompt que trate isenção de valor e recargo regional corretamente, cada regra por si, ainda erra o caso 5 ao tratar as duas regras como independentes — a lacuna está na forma como elas se combinam, não em nenhuma delas isolada.

Compare as duas lacunas: qual delas você acha que uma revisão de código manual pegaria mais fácil, só de ler a função? E qual delas só um teste automatizado (rodando o caso 5 de verdade) pegaria com confiança? Justifique.

## Avaliar

### 8. A proibição total

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: a Vetor deveria proibir vibe coding para todo tipo de tarefa, incluindo scripts internos de uso único? Justifique com o critério de reversibilidade e tempo de vida, não com preferência pessoal.

## Criar

### 9. Checklist de time

Escreva um checklist de no máximo cinco itens que qualquer prompt de geração de código na Vetor deveria atender antes de ser aceito em produção. Cada item precisa ser verificável por outra pessoa, não uma intenção vaga como "ser claro".

### 10. Desafio: um ciclo avaliador-otimizador para a função de frete

**Nível:** mais exigente que os demais exercícios desta sessão. Combina o padrão avaliador-otimizador de [Sistemas agênticos e simplicidade](sistemas-agenticos.md#o-principio-de-simplicidade) com o cenário do exercício-âncora.

Você já gerou, no exercício 5, duas versões da função de frete: uma a partir do prompt intuitivo, outra do prompt estruturado. Neste desafio, você vai usar o próprio agente para descobrir os erros da primeira versão, sem revelar a ele quais casos falham.

**Execute:**

1. Volte à saída do prompt intuitivo (exercício 5, passo 1). Não abra de novo a tabela de 5 casos de teste.
2. Numa nova interação, peça ao agente para atuar como revisor crítico dessa função: cole a regra de negócio completa do bloco "Regra completa da Vetor para frete" (exercício 5) e peça que ele aponte todos os casos em que a função produz um valor errado. Não mencione o item frágil, a região Norte, nem que as duas exceções se compõem — deixe o agente encontrar sozinho.
3. Compare os casos que o agente encontrou sozinho com os 5 casos de teste oficiais do exercício 5. Ele achou o caso 3 (isenção negada por item frágil)? Achou o caso 5, em que as duas exceções se cruzam?
4. Peça ao agente para corrigir a função com base na própria crítica, sem que você aponte a correção.

**Entrega esperada:** a crítica do passo 2, a comparação do passo 3, e a versão corrigida do passo 4, testada contra os 5 casos oficiais.

**Por que isso é mais difícil:** nos exercícios anteriores, você forneceu a regra de negócio completa de uma vez. Aqui, o agente precisa descobrir sozinho onde a primeira versão falha, o papel de "avaliador" do padrão visto em Sistemas agênticos e simplicidade, e você precisa julgar se a autocrítica dele foi rigorosa ou só superficial — o caso 5 é o teste mais duro porque exige perceber que duas regras corretas isoladamente ainda podem compor errado.

<details>
<summary>O que evidencia um bom resultado</summary>

O agente identificou o caso 3 (isenção negada por item frágil) sem que isso fosse mencionado no prompt. O caso 5, que exige perceber a interação entre duas exceções, é o mais difícil de todos — não encontrá-lo sozinho também é um resultado válido para discutir: ciclo de autocrítica captura omissão melhor do que captura erro de composição entre regras, e é por isso que a verificação por teste automatizado continua necessária mesmo com um passo de revisão a mais.
</details>

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
