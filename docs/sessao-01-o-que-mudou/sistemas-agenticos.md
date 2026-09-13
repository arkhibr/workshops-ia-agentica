# Sistemas agênticos e simplicidade

Nem toda automação construída sobre um modelo de linguagem é um sistema agêntico, e nem todo sistema agêntico precisa da autonomia que consegue exercer. Esta página traça a fronteira entre os dois casos e chega à recomendação de simplicidade que decorre dela.

## O que torna um sistema agêntico

Antes de intercalar ação, um agente precisa raciocinar de forma explícita. [Wei et al. (2022)](../referencia/bibliografia.md#wei-et-al-chain-of-thought-prompting-2022) mostraram que pedir ao modelo para expor o raciocínio passo a passo antes de responder, a técnica de cadeia de pensamento, melhora sensivelmente o desempenho em tarefas com múltiplas etapas de lógica. [Yao et al.](../referencia/bibliografia.md#yao-et-al-react-2023) deram o passo seguinte, no artigo que introduziu o framework ReAct (2023): ligaram esse raciocínio explícito a ações reais e verificáveis, formalizando o ciclo que intercala raciocínio e ação, lendo o resultado de uma ferramenta, decidindo o próximo passo, agindo de novo.

Um chat comum recebe um pedido como "corrija os testes que estão falhando" e devolve uma sugestão de texto. Um agente lê a saída real do executor de testes, decide qual arquivo abrir com base nela, edita o arquivo, roda os testes de novo, lê a nova saída e só para quando o resultado bate, ou quando decide que precisa perguntar algo a quem o acionou. É esse ciclo de raciocínio e ação, mais do que o tamanho do modelo, que separa Claude Code ou Codex de um chat comum, e o que torna possível a engenharia agêntica.

[Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026) define engenharia agêntica como "the practice of developing software with the assistance of coding agents" (Claude Code, Codex, Gemini CLI), sustentada por três responsabilidades que continuam humanas mesmo com o código escrito por um agente:

- **Especificar o problema.** O pedido descreve o comportamento esperado nos casos de borda, ou só o caminho feliz?
- **Prover as ferramentas certas.** O agente tem acesso ao terminal, ao executor de testes, ao analisador estático, ou só gera texto sem verificar nada contra o sistema real?
- **Verificar e iterar.** Alguém rodou o resultado antes de aceitar, ou o código entrou porque "parecia certo"?

![Ciclo da engenharia agêntica conectando contexto, raciocínio, ação, evidência e ajuste. As responsabilidades humanas de especificar, prover ferramentas e verificar e iterar alimentam o ciclo. Uma régua lateral distingue piso, teto e julgamento.](../assets/images/s1-ciclo-engenharia-agentica.png)

## O princípio de simplicidade

A peça básica de qualquer sistema agêntico, segundo o guia da [Anthropic, "Building Effective Agents"](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), é o *augmented LLM*: um modelo aumentado com acesso a busca, ferramentas e memória, capaz de decidir sozinho que consulta fazer, qual ferramenta acionar e o que vale a pena reter.

A partir desse bloco básico, quatro formas de controle operacional se distinguem por uma única pergunta: quem escolhe a próxima transição. Um **chatbot** responde por conhecimento paramétrico, contexto fornecido ou busca aumentada. Vários turnos de conversa não implicam, por si só, seleção de ferramenta ou efeito sobre um sistema externo. Um **copiloto** apoia uma pessoa numa tarefa (resume, sugere, rascunha, propõe uma ação), mas a autoridade de decisão continua com quem opera a ferramenta, e chamar uma ferramenta de leitura não basta para virar agente.

Um **fluxo de trabalho determinístico** tem passos, transições, condições e tratamento de erro definidos pela aplicação. O modelo pode classificar ou gerar conteúdo dentro de uma etapa, mas não escolhe qual é a próxima etapa. Só o **agente** é o sistema em que o modelo escolhe pelo menos parte do próximo passo (qual ferramenta, em que ordem, como decompor a tarefa, quando interromper) para perseguir um objetivo dentro de limites definidos ([Mendes, *Controle e Autonomia*](../referencia/bibliografia.md#mendes-controle-e-autonomia-modulo-4-agentes)).

A distinção classifica grau de controle, e não grau de maturidade. Um fluxo de trabalho bem desenhado pode superar um agente mal supervisionado. Um agente pode manter conversa. Um copiloto pode chamar ferramenta de leitura sem deixar de ser copiloto. Diante de um sistema desses, as perguntas que decidem a classificação são quem escolhe a transição, quem executa o efeito e quem responde pelo resultado.

A partir desse mesmo bloco básico, a [Anthropic, no guia de engenharia "Building Effective Agents"](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) (dezembro de 2024), foca a distinção seguinte — entre fluxo de trabalho e agente — e recomenda encontrar a solução mais simples possível, aumentando a complexidade apenas quando o problema exigir. O guia é explícito sobre o preço dessa escolha: sistemas agênticos trocam latência e custo por desempenho melhor na tarefa, e cabe a quem projeta decidir quando essa troca compensa. Um agente com autonomia plena carrega, além do custo mais alto, o risco de um erro numa etapa inicial se propagar sem supervisão pelas etapas seguintes. Por isso o guia recomenda teste extensivo em ambiente controlado, com salvaguardas apropriadas, antes de liberar autonomia total em produção.

!!! tip "Aplique agora"  
    Antes de adicionar mais uma etapa autônoma a um agente que seu time já usa, responda: essa etapa resolve um problema real de desempenho que a etapa anterior não resolvia, ou só parece mais sofisticada? Se não houver um problema real por trás, o guia recomenda não adicionar.

O guia também recomenda cautela com frameworks de agente antes de entender bem o problema: eles costumam criar camadas extras de abstração que escondem o prompt e a resposta reais, dificultando a depuração quando algo sai errado. A recomendação é começar direto pela API do modelo. Muitos dos padrões abaixo cabem em poucas linhas de código, sem framework nenhum.

O guia distingue **fluxos de trabalho** (código orquestra o modelo em um caminho predefinido) de **agentes** (o modelo decide dinamicamente os próprios passos): fluxos de trabalho entregam previsibilidade e consistência para tarefas bem definidas, enquanto agentes fazem mais sentido quando o problema pede flexibilidade e decisão do próprio modelo em escala. Antes de recomendar autonomia plena, o guia cataloga cinco padrões de fluxo de trabalho:

- **Encadeamento de prompts.** A saída de uma chamada vira a entrada da próxima, numa sequência fixa.
- **Roteamento.** Uma primeira chamada classifica o pedido e direciona para o caminho especializado certo.
- **Paralelização.** Várias chamadas rodam ao mesmo tempo sobre partes independentes do problema, e os resultados se combinam no final.
- **Orquestrador-trabalhadores.** Uma chamada central decompõe a tarefa e distribui pedaços para outras chamadas especializadas.
- **Avaliador-otimizador.** Uma chamada gera, outra critica o resultado contra um critério definido, e o ciclo repete até passar.

!!! question "Antes de continuar"  
    Pense num agente ou numa automação de IA que seu time usa hoje. Ele decide o próprio caminho a cada execução, ou segue, na prática, uma sequência fixa de passos vestida de "agente"? Isso muda o quanto você revisa o resultado antes de confiar nele?

O mesmo princípio vale para a escolha entre vibe coding, assistência e SDD: comece pelo modo mais simples que a linha da tabela permitir, e suba de nível quando a tarefa concreta exigir, sem deixar que a vontade de usar a ferramenta mais avançada decida no lugar dela.

![Trajetória de complexidade crescente que parte de uma chamada direta, passa por fluxos de trabalho previsíveis e chega a um agente que decide os próprios passos. A autonomia aumenta junto com o custo de verificação, enquanto um alerta destaca o anti-padrão de tratar protótipo como produto.](../assets/images/s1-simplicidade-risco.png)

**Próxima página:** [Avaliação de modelos](avaliacao-de-modelos.md).
