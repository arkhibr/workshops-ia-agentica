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

A pergunta que resume a tabela: se esse código quebrar em produção, alguém vai conseguir reconstruir por que ele foi escrito daquele jeito? Vibe coding não deixa rastro para responder. Assistência de codificação deixa o código e o ticket. SDD deixa a especificação inteira.

## O que a evidência empírica recomenda

A última linha da tabela não é intuição: vem do contraste entre os dois estudos de [Conceitos](conceitos.md#a-evidencia-empirica-ganhos-que-aparecem-e-ganhos-que-desaparecem). Peng et al. mediram ganho real numa tarefa nova e bem delimitada, sem histórico prévio: o cenário em que vibe coding ou assistência leve já entregam a maior parte do valor. O METR mediu perda real numa tarefa de manutenção, em sistema grande, com convenções que só existem na cabeça de quem já trabalha nele há anos. Nesse cenário, pular direto para vibe coding cobra caro, porque o tempo economizado na geração é gasto em dobro revisando uma proposta que ignorou contexto nunca explicitado.

A régua prática: quanto mais o problema depende de conhecimento tácito do sistema, maior a dose de especificação explícita que compensa.

## O princípio de simplicidade

A Anthropic, no guia de engenharia "Building Effective Agents" (dezembro de 2024), recomenda encontrar a solução mais simples possível, aumentando a complexidade apenas quando o problema exigir. Isso pode significar preferir um fluxo determinístico com uma ou duas chamadas ao modelo, mais simples que um agente autônomo. O guia distingue **workflows** (código orquestra o modelo em um caminho predefinido) de **agentes** (o modelo decide dinamicamente os próprios passos), e cataloga cinco padrões de workflow antes de recomendar autonomia plena: encadeamento de prompts, roteamento, paralelização, orquestrador-trabalhadores, avaliador-otimizador.

O mesmo princípio vale para a escolha entre vibe coding, assistência e SDD: comece pelo modo mais simples que a linha da tabela permitir, e suba de nível só quando a tarefa concreta, não a vontade de usar a ferramenta mais avançada, exigir.

## Anti-padrão: vibe coding tratado como produto

O anti-padrão não é usar vibe coding. É usar vibe coding e depois esquecer que foi usado. Os sintomas aparecem sempre na mesma ordem: o protótipo funciona na demonstração, alguém decide "já está pronto, só falta subir", ninguém escreve a especificação que existia apenas na cabeça de quem conversou com o agente, e o próximo bug custa uma investigação inteira porque não há teste, não há decisão registrada e não há ninguém que lembre por que aquele caso de borda foi ignorado.

A correção não é proibir vibe coding. É decidir o modo antes de começar, não depois que o protótipo já virou dependência de outras equipes.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md) aplica esta tabela a um caso concreto.
