# Modos de trabalho com IA

Times que adotam IA no desenvolvimento costumam operar em três modos ao mesmo tempo, sem nomear nenhum deles. O que distingue os três, de onde veio o mais recente, e o critério para escolher um por tarefa.

## Três modos de trabalho que a maioria dos times mistura num só

Três modos de trabalho com IA se destacam na prática atual de desenvolvimento de software:

| Modo | Artefato que governa | Como a qualidade é julgada | Risco dominante |
|---|---|---|---|
| Vibe coding | conversa corrente e resultado aparente | "parece funcionar" | intenção implícita, regressão, dívida invisível |
| Assistência de codificação | ticket, código existente, revisão do desenvolvedor | testes e revisão depois de gerar | contexto fragmentado, decisões não registradas |
| SDD (Sessão 8) | constitution, spec, plano, tarefas, testes e gates versionados | rastreabilidade entre intenção, implementação e evidência | custo de especificar sem manter os artefatos vivos |

![Três colunas comparam vibe coding, assistência de codificação e SDD pelos artefatos que governam o trabalho, pela forma de verificação e pelo risco dominante. Uma seta inferior mostra a progressão de conversa para código e ticket, até artefatos versionados.](../assets/images/s1-tres-modos-trabalho.png)

Este workshop move o time da primeira linha para a terceira ao longo de dez sessões: assistência de codificação disciplinada do Bloco 2 ao Bloco 3, SDD completo na Sessão 8.

## De onde vem o vibe coding

O termo vem de Andrej Karpathy, pesquisador fundador da OpenAI e ex-diretor de IA da Tesla, numa publicação de fevereiro de 2025. O motivo técnico para essa prática funcionar já existia antes do nome: Brown et al. demonstraram, no artigo que apresentou o GPT-3, que um modelo de linguagem executa uma tarefa nova a partir só da descrição em linguagem natural e de alguns exemplos no próprio texto de entrada, sem qualquer ajuste de peso. Esse mecanismo, chamado aprendizado em contexto, é o que torna um prompt capaz de funcionar como programa.

Simon Willison, que documenta práticas de desenvolvimento assistido por IA desde 2022, é específico sobre onde o uso legítimo do vibe coding termina: "vibe coding is more useful in its original definition — we need a term to describe unreviewed, prototype-quality LLM-generated code". Serve para prototipagem descartável. O problema aparece quando o time atravessa, sem perceber, a fronteira entre protótipo e produto: a conversa carrega decisões que nunca chegam ao repositório, o teste confirma só o que foi implementado, e a próxima sessão do agente não herda o raciocínio da anterior.

O próprio Karpathy documentou o limite na prática: os ganhos de velocidade do vibe coding "vanished shortly after getting local code running". A aceleração desaparece quando o código precisa integrar, ser mantido, ou sobreviver a um caso de borda fora do que o prompt original previu.

## Quando cada modo se justifica

Os três modos acima não são degraus de maturidade que todo código precisa subir. São famílias de risco: a pergunta não é "qual modo é melhor", é "qual risco esta tarefa específica carrega".

| Critério | Favorece vibe coding | Favorece assistência de codificação | Favorece SDD |
|---|---|---|---|
| Reversibilidade | fácil de descartar | custo médio de retrabalho | difícil ou caro de desfazer |
| Tempo de vida esperado | horas, um experimento | semanas, uma feature | meses ou anos, parte do produto |
| Quantas pessoas vão mexer depois | só quem escreveu | o time atual | times futuros, sem contexto da decisão original |
| Regra de negócio envolvida | nenhuma, ou trivial | alguma, conhecida pelo time | crítica, com exceções que um prompt vago esquece |
| Familiaridade com o código existente | código novo, sem histórico | sistema conhecido pelo time atual | sistema grande e maduro, com convenções implícitas |

![Cinco réguas mostram como reversibilidade, tempo de vida, quantidade de mantenedores, criticidade da regra de negócio e conhecimento tácito aumentam a necessidade de contexto explícito e deslocam a escolha de vibe coding para assistência e SDD.](../assets/images/s1-regua-escolha.png)

A pergunta que resume a tabela: se esse código quebrar em produção, alguém vai conseguir reconstruir por que ele foi escrito daquele jeito? Vibe coding não deixa rastro para responder. Assistência de codificação deixa o código e o ticket. SDD deixa a especificação inteira.

!!! tip "Aplique agora"
    Pense numa tarefa real do seu backlog desta semana. Percorra as cinco linhas da tabela e classifique-a: ela puxa para vibe coding, assistência ou SDD? Compare com a pessoa ao lado — vocês chegaram no mesmo modo para tarefas parecidas?

## O peso econômico de reversibilidade e tempo de vida

Boehm, em *Software Engineering Economics* (1981), documentou algo que antecede qualquer LLM: o custo de corrigir um defeito cresce a cada fase do desenvolvimento. Em sistemas pequenos, o crescimento é suave; em sistemas grandes e críticos, um problema descoberto depois da entrega pode custar da ordem de 100 vezes mais para corrigir do que o mesmo problema pego na fase de requisitos. A proporção exata varia por contexto (pesquisa mais recente questiona se o multiplicador de Boehm ainda vale em times ágeis com integração contínua), mas a direção não mudou em quatro décadas: quanto mais tarde uma ambiguidade aparece, mais caro fica resolvê-la.

É essa lógica que sustenta as duas primeiras linhas da tabela. Vibe coding empurra toda ambiguidade para depois, para quando o código já está em produção. SDD força a ambiguidade a aparecer antes, na especificação, onde ela ainda é barata de corrigir.

## Anti-padrão: vibe coding tratado como produto

O anti-padrão não é usar vibe coding. É usar vibe coding e depois esquecer que foi usado. Os sintomas aparecem sempre na mesma ordem: o protótipo funciona na demonstração, alguém decide "já está pronto, só falta subir", ninguém escreve a especificação que existia apenas na cabeça de quem conversou com o agente, e o próximo bug custa uma investigação inteira porque não há teste, não há decisão registrada e não há ninguém que lembre por que aquele caso de borda foi ignorado.

A correção não é proibir vibe coding. É decidir o modo antes de começar, não depois que o protótipo já virou dependência de outras equipes.

**Próxima página:** [Evidência empírica de produtividade](evidencia-empirica.md).
