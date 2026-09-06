# Sistemas agênticos e simplicidade

Nem toda automação construída sobre um modelo de linguagem é um sistema agêntico, e nem todo sistema agêntico precisa da autonomia que consegue exercer. Onde fica a fronteira entre os dois casos, e a recomendação de simplicidade que decorre dela.

## O que torna um sistema agêntico

Antes de intercalar ação, um agente precisa raciocinar de forma explícita. Wei et al. (2022) mostraram que pedir ao modelo para expor o raciocínio passo a passo antes de responder, a técnica de cadeia de pensamento, melhora sensivelmente o desempenho em tarefas com múltiplas etapas de lógica. Yao et al. deram o passo seguinte, no artigo que introduziu o framework ReAct (2023): ligaram esse raciocínio explícito a ações reais e verificáveis, formalizando o ciclo que intercala raciocínio e ação, lendo o resultado de uma ferramenta, decidindo o próximo passo, agindo de novo.

Um chat comum recebe um pedido como "corrija os testes que estão falhando" e devolve uma sugestão de texto. Um agente lê a saída real do executor de testes, decide qual arquivo abrir com base nela, edita o arquivo, roda os testes de novo, lê a nova saída e só para quando o resultado bate — ou quando decide que precisa perguntar algo a quem o acionou. É esse ciclo de raciocínio e ação, mais do que o tamanho do modelo, que separa Claude Code ou Codex de um chat comum, e o que torna possível a engenharia agêntica.

Willison define engenharia agêntica como "the practice of developing software with the assistance of coding agents" (Claude Code, Codex, Gemini CLI), sustentada por três responsabilidades que continuam humanas mesmo com o código escrito por um agente:

- **Especificar o problema.** O pedido descreve o comportamento esperado nos casos de borda, ou só o caminho feliz?
- **Prover as ferramentas certas.** O agente tem acesso ao terminal, ao executor de testes, ao linter — ou só gera texto sem verificar nada contra o sistema real?
- **Verificar e iterar.** Alguém rodou o resultado antes de aceitar, ou o código entrou porque "parecia certo"?

![Ciclo da engenharia agêntica conectando contexto, raciocínio, ação, evidência e ajuste. As responsabilidades humanas de especificar, prover ferramentas e verificar e iterar alimentam o ciclo. Uma régua lateral distingue piso, teto e julgamento.](../assets/images/s1-ciclo-engenharia-agentica.png)

## O princípio de simplicidade

A peça básica de qualquer sistema agêntico, segundo o mesmo guia da Anthropic, é o *augmented LLM*: um modelo aumentado com acesso a busca, ferramentas e memória, capaz de decidir sozinho que consulta fazer, qual ferramenta acionar e o que vale a pena reter. Workflow e agente são duas formas diferentes de organizar esse mesmo bloco básico — a diferença está em quem controla o caminho, o código ou o próprio modelo.

A partir desse bloco, a Anthropic, no guia de engenharia "Building Effective Agents" (dezembro de 2024), recomenda encontrar a solução mais simples possível, aumentando a complexidade apenas quando o problema exigir. O guia é explícito sobre o preço dessa escolha: sistemas agênticos trocam latência e custo por desempenho melhor na tarefa, e cabe a quem projeta decidir quando essa troca compensa. Um agente com autonomia plena carrega, além do custo mais alto, o risco de um erro numa etapa inicial se propagar sem supervisão pelas etapas seguintes; por isso o guia recomenda teste extensivo em ambiente controlado, com salvaguardas apropriadas, antes de liberar autonomia total em produção.

!!! tip "Aplique agora"
    Antes de adicionar mais uma etapa autônoma a um agente que seu time já usa, responda: essa etapa resolve um problema real de desempenho que a etapa anterior não resolvia, ou só parece mais sofisticada? Se não houver um problema real por trás, o guia recomenda não adicionar.

O guia também recomenda cautela com frameworks de agente antes de entender bem o problema: eles costumam criar camadas extras de abstração que escondem o prompt e a resposta reais, dificultando a depuração quando algo sai errado. A recomendação é começar direto pela API do modelo — muitos dos padrões abaixo cabem em poucas linhas de código, sem framework nenhum.

O guia distingue **workflows** (código orquestra o modelo em um caminho predefinido) de **agentes** (o modelo decide dinamicamente os próprios passos): workflows entregam previsibilidade e consistência para tarefas bem definidas, enquanto agentes fazem mais sentido quando o problema pede flexibilidade e decisão do próprio modelo em escala. Antes de recomendar autonomia plena, o guia cataloga cinco padrões de workflow:

- **Encadeamento de prompts.** A saída de uma chamada vira a entrada da próxima, numa sequência fixa.
- **Roteamento.** Uma primeira chamada classifica o pedido e direciona para o caminho especializado certo.
- **Paralelização.** Várias chamadas rodam ao mesmo tempo sobre partes independentes do problema, e os resultados se combinam no final.
- **Orquestrador-trabalhadores.** Uma chamada central decompõe a tarefa e distribui pedaços para outras chamadas especializadas.
- **Avaliador-otimizador.** Uma chamada gera, outra critica o resultado contra um critério definido, e o ciclo repete até passar.

!!! question "Antes de continuar"
    Pense num agente ou numa automação de IA que seu time usa hoje. Ele decide o próprio caminho a cada execução, ou segue, na prática, uma sequência fixa de passos vestida de "agente"? Isso muda o quanto você revisa o resultado antes de confiar nele?

O mesmo princípio vale para a escolha entre vibe coding, assistência e SDD: comece pelo modo mais simples que a linha da tabela permitir, e suba de nível só quando a tarefa concreta, não a vontade de usar a ferramenta mais avançada, exigir.

![Trajetória de complexidade crescente que parte de uma chamada direta, passa por workflows previsíveis e chega a um agente que decide os próprios passos. A autonomia aumenta junto com o custo de verificação, enquanto um alerta destaca o anti-padrão de tratar protótipo como produto.](../assets/images/s1-simplicidade-risco.png)

**Próxima página:** [Avaliação de modelos](avaliacao-de-modelos.md).
