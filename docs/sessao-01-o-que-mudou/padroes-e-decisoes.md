# Padrões e decisões

## Quando cada modo se justifica

Os três modos de [Conceitos](conceitos.md) não são degraus de maturidade que todo código precisa subir. São famílias de risco: a pergunta não é "qual modo é melhor", é "qual risco esta tarefa específica carrega".

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

## Por que reversibilidade e tempo de vida pesam tanto

Boehm, em *Software Engineering Economics* (1981), documentou algo que antecede qualquer LLM: o custo de corrigir um defeito cresce a cada fase do desenvolvimento. Em sistemas pequenos, o crescimento é suave; em sistemas grandes e críticos, um problema descoberto depois da entrega pode custar da ordem de 100 vezes mais para corrigir do que o mesmo problema pego na fase de requisitos. A proporção exata varia por contexto (pesquisa mais recente questiona se o multiplicador de Boehm ainda vale em times ágeis com integração contínua), mas a direção não mudou em quatro décadas: quanto mais tarde uma ambiguidade aparece, mais caro fica resolvê-la.

É essa lógica que sustenta as duas primeiras linhas da tabela. Vibe coding empurra toda ambiguidade para depois, para quando o código já está em produção. SDD força a ambiguidade a aparecer antes, na especificação, onde ela ainda é barata de corrigir.

## O que a evidência empírica recomenda

A última linha da tabela não é intuição: vem do contraste entre os dois estudos de [Conceitos](conceitos.md#a-evidencia-empirica-ganhos-que-aparecem-e-ganhos-que-desaparecem). Peng et al. mediram ganho real numa tarefa nova e bem delimitada, sem histórico prévio: o cenário em que vibe coding ou assistência leve já entregam a maior parte do valor. O METR mediu perda real numa tarefa de manutenção, em sistema grande, com convenções que só existem na cabeça de quem já trabalha nele há anos. Nesse cenário, pular direto para vibe coding cobra caro, porque o tempo economizado na geração é gasto em dobro revisando uma proposta que ignorou contexto nunca explicitado.

A régua prática: quanto mais o problema depende de conhecimento tácito do sistema, maior a dose de especificação explícita que compensa.

## O princípio de simplicidade

A Anthropic, no guia de engenharia "Building Effective Agents" (dezembro de 2024), recomenda encontrar a solução mais simples possível, aumentando a complexidade apenas quando o problema exigir. Isso pode significar preferir um fluxo determinístico com uma ou duas chamadas ao modelo, mais simples que um agente autônomo. O guia distingue **workflows** (código orquestra o modelo em um caminho predefinido) de **agentes** (o modelo decide dinamicamente os próprios passos), e cataloga cinco padrões de workflow antes de recomendar autonomia plena:

- **Encadeamento de prompts.** A saída de uma chamada vira a entrada da próxima, numa sequência fixa.
- **Roteamento.** Uma primeira chamada classifica o pedido e direciona para o caminho especializado certo.
- **Paralelização.** Várias chamadas rodam ao mesmo tempo sobre partes independentes do problema, e os resultados se combinam no final.
- **Orquestrador-trabalhadores.** Uma chamada central decompõe a tarefa e distribui pedaços para outras chamadas especializadas.
- **Avaliador-otimizador.** Uma chamada gera, outra critica o resultado contra um critério definido, e o ciclo repete até passar.

O mesmo princípio vale para a escolha entre vibe coding, assistência e SDD: comece pelo modo mais simples que a linha da tabela permitir, e suba de nível só quando a tarefa concreta, não a vontade de usar a ferramenta mais avançada, exigir.

![Trajetória de complexidade crescente que parte de uma chamada direta, passa por workflows previsíveis e chega a um agente que decide os próprios passos. A autonomia aumenta junto com o custo de verificação, enquanto um alerta destaca o anti-padrão de tratar protótipo como produto.](../assets/images/s1-simplicidade-risco.png)

## Como avaliar modelos para engenharia de software

Escolher um modelo pelo nome mais falado do momento é o mesmo erro de raiz do vibe coding: aceitar sem verificar. Cinco critérios tornam essa escolha uma decisão, não uma torcida.

**Use um benchmark que meça o trabalho real, não a função isolada.** O HumanEval (Chen et al., 2021) mede se o modelo escreve uma função correta a partir de um enunciado — útil, mas distante do que a Sessão 8 chama de engenharia agêntica. Um benchmark como o DeepSWE mede se o agente resolve uma tarefa real, de longo horizonte, dentro de um repositório existente: localizar a causa, editar os arquivos certos, passar num verificador automático. É o tipo de medida mais próximo do que a Vetor precisa.

**Prefira tarefas verificadas por programa a julgamento humano de "parece bom".** O DeepSWE verifica cada uma das 113 tarefas por execução de programa, não por alguém lendo o diff e achando que ficou razoável. Isso remove subjetividade do resultado: ou o teste passa, ou não passa.

**Desconfie de benchmark saturado.** Quando os modelos de fronteira empatam a menos de um ponto percentual de diferença entre si, o benchmark provavelmente está perto do teto para aquela classe de modelo. O DeepSWE, em agosto de 2026, ainda separa o primeiro colocado do quinto por 4,6 pontos e o top 10 inteiro por 8,3 pontos — sinal de que ainda há distinção real de capacidade para medir, não um empate técnico disfarçado de ranking.

**Desconfie de número autorreportado por quem vende o modelo.** Fabricantes escolhem qual benchmark divulgar no anúncio de lançamento, e às vezes trocam de benchmark de uma versão para a outra sem explicar por quê. Prefira leitores independentes que avaliam todos os fabricantes sob o mesmo arnês de teste, na mesma data — é exatamente o que o DeepSWE (mantido pela Datacurve, publicado em benchlm.ai) faz: roda Claude, GPT e modelos abertos como o GLM lado a lado, sem depender do número que cada fabricante escolheu anunciar.

**Nota do placar não é a decisão inteira.** Custo por tarefa resolvida, latência, tamanho da janela de contexto e confiabilidade dentro do seu ambiente agêntico específico pesam tanto quanto o resolve rate — um modelo 3 pontos percentuais à frente, mas 5 vezes mais caro por tarefa, raramente compensa para o dia a dia de um time.

### Placar de referência — DeepSWE

| Modelo | Organização | DeepSWE |
|---|---|---|
| Claude Opus 5 | Anthropic | 73,6% |
| GPT-5.6 Sol | OpenAI | 72,7% |
| Claude Fable 5 | Anthropic | 69,7% |
| GPT-5.6 Terra | OpenAI | 69,6% |
| GLM-5.3 | Z.AI | 69,0% |

Fonte: [benchlm.ai — DeepSWE](https://benchlm.ai/benchmarks/deepswe), atualizado em 20 de agosto de 2026, 25 modelos avaliados: 113 tarefas de longo horizonte, tiradas de 91 repositórios open source ativos em 5 linguagens, verificadas por programa.

**Este placar envelhece rápido**: confira o [DeepSWE Leaderboard](https://benchlm.ai/benchmarks/deepswe) atualizado antes de decidir, não confie em número congelado numa página de workshop.

## Anti-padrão: vibe coding tratado como produto

O anti-padrão não é usar vibe coding. É usar vibe coding e depois esquecer que foi usado. Os sintomas aparecem sempre na mesma ordem: o protótipo funciona na demonstração, alguém decide "já está pronto, só falta subir", ninguém escreve a especificação que existia apenas na cabeça de quem conversou com o agente, e o próximo bug custa uma investigação inteira porque não há teste, não há decisão registrada e não há ninguém que lembre por que aquele caso de borda foi ignorado.

A correção não é proibir vibe coding. É decidir o modo antes de começar, não depois que o protótipo já virou dependência de outras equipes.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md) aplica esta tabela a um caso concreto.
