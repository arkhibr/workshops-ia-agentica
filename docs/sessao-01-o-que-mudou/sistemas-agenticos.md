# Sistemas agênticos e simplicidade

Nem toda automação construída sobre um modelo de linguagem é um sistema agêntico. E mesmo um sistema agêntico de verdade raramente precisa de toda a autonomia que ele consegue exercer. Esta página mostra onde fica essa fronteira e por que a recomendação prática é começar simples.

## O que torna um sistema agêntico

Antes de intercalar ação, um agente precisa raciocinar de forma explícita. [Wei et al. (2022)](../referencia/bibliografia.md#wei-et-al-chain-of-thought-prompting-2022) mostraram que pedir ao modelo para expor o raciocínio passo a passo antes de responder, a técnica de cadeia de pensamento, melhora sensivelmente o desempenho em tarefas com múltiplas etapas de lógica. [Yao et al.](../referencia/bibliografia.md#yao-et-al-react-2023) deram o passo seguinte, no artigo que introduziu o framework ReAct (2023): ligaram esse raciocínio explícito a ações reais e verificáveis, e formalizaram o ciclo que intercala raciocínio e ação: o agente lê o resultado de uma ferramenta, decide o próximo passo e age de novo.

Um chat comum recebe um pedido como "corrija os testes que estão falhando" e devolve uma sugestão de texto. Um agente lê a saída real do executor de testes, decide qual arquivo abrir com base nela, edita o arquivo, roda os testes de novo, lê a nova saída e só para quando o resultado bate, ou quando decide que precisa perguntar algo a quem o acionou. Esse ciclo de raciocínio e ação separa Claude Code ou Codex de um chat comum, e pesa mais nessa separação do que o tamanho do modelo. É ele que torna possível a engenharia agêntica.

[Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026) define engenharia agêntica como "the practice of developing software with the assistance of coding agents" (Claude Code, Codex, Gemini CLI), sustentada por três responsabilidades que continuam humanas mesmo com o código escrito por um agente:

- **Especificar o problema.** O pedido descreve o comportamento esperado nos casos de borda, ou só o caminho feliz?
- **Prover as ferramentas certas.** O agente tem acesso ao terminal, ao executor de testes, ao analisador estático, ou só gera texto sem verificar nada contra o sistema real?
- **Verificar e iterar.** Alguém rodou o resultado antes de aceitar, ou o código entrou porque "parecia certo"?

![Ciclo da engenharia agêntica conectando contexto, raciocínio, ação, evidência e ajuste. As responsabilidades humanas de especificar, prover ferramentas e verificar e iterar alimentam o ciclo. Uma régua lateral distingue piso, teto e julgamento.](../assets/images/s1-ciclo-engenharia-agentica.png)

## O princípio de simplicidade

A peça básica de qualquer sistema agêntico, segundo o guia da [Anthropic, "Building Effective Agents"](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), é o *augmented LLM*: um modelo aumentado com acesso a busca, ferramentas e memória, capaz de decidir sozinho que consulta fazer, qual ferramenta acionar e o que vale a pena reter.

A partir desse bloco básico, você separa quatro formas de controle com uma pergunta só: quem escolhe a próxima transição. Um **chatbot** responde por conhecimento paramétrico, contexto fornecido ou busca aumentada. Conversar por vários turnos não significa escolher ferramenta nem produzir efeito em sistema externo. Um **copiloto** apoia uma pessoa numa tarefa: resume, sugere, rascunha, propõe uma ação. Quem decide continua sendo quem opera a ferramenta. Chamar uma ferramenta de leitura não basta para o copiloto virar agente.

Num **fluxo de trabalho determinístico**, a aplicação define os passos, as transições, as condições e o tratamento de erro. O modelo classifica ou gera conteúdo dentro de uma etapa, e não escolhe qual etapa vem depois. Só o **agente** é o sistema em que o modelo escolhe pelo menos parte do próximo passo (qual ferramenta, em que ordem, como decompor a tarefa, quando interromper) para perseguir um objetivo dentro de limites definidos ([Mendes, *Controle e Autonomia*](../referencia/bibliografia.md#mendes-controle-e-autonomia-modulo-4-agentes)).

Essa classificação mede grau de controle. Ela não diz nada sobre qualidade: um fluxo de trabalho bem desenhado entrega mais que um agente mal supervisionado. Um agente também conversa. Um copiloto também chama ferramenta de leitura e continua copiloto. Para classificar um sistema desses, responda três perguntas. Quem escolhe a transição? Quem executa o efeito? Quem responde pelo resultado?

O mesmo guia da Anthropic, de dezembro de 2024, recomenda procurar a solução mais simples que resolva o problema, e só aumentar a complexidade quando o problema exigir. Ele diz o preço dessa escolha com todas as letras: sistema agêntico troca latência e custo por desempenho melhor na tarefa, e quem projeta decide se a troca compensa. Um agente com autonomia plena custa mais caro e ainda corre outro risco: um erro numa etapa inicial atravessa todas as seguintes sem ninguém ver. Por isso o guia manda testar bastante em ambiente controlado, com salvaguardas, antes de liberar autonomia total em produção.

!!! tip "Aplique agora"  
    Antes de adicionar mais uma etapa autônoma a um agente que seu time já usa, responda: essa etapa resolve um problema real de desempenho que a etapa anterior não resolvia, ou só parece mais sofisticada? Se não houver um problema real por trás, o guia recomenda não adicionar.

Ele também pede cautela com framework de agente antes de você entender bem o problema. Framework costuma criar camadas de abstração que escondem o prompt e a resposta reais, e aí fica difícil depurar quando algo sai errado. Comece direto pela API do modelo. Muitos dos padrões abaixo cabem em poucas linhas, sem framework nenhum.

O guia separa **fluxo de trabalho**, onde o código orquestra o modelo por um caminho predefinido, de **agente**, onde o modelo decide os próprios passos. Fluxo de trabalho entrega previsibilidade e consistência em tarefas bem definidas. Agente faz mais sentido quando o problema pede flexibilidade e decisão do próprio modelo em escala. Antes de recomendar autonomia plena, o guia cataloga cinco padrões de fluxo de trabalho:

- **Encadeamento de prompts.** A saída de uma chamada vira a entrada da próxima, numa sequência fixa.
- **Roteamento.** Uma primeira chamada classifica o pedido e direciona para o caminho especializado certo.
- **Paralelização.** Várias chamadas rodam ao mesmo tempo sobre partes independentes do problema, e os resultados se combinam no final.
- **Orquestrador-trabalhadores.** Uma chamada central decompõe a tarefa e distribui pedaços para outras chamadas especializadas.
- **Avaliador-otimizador.** Uma chamada gera, outra critica o resultado contra um critério definido, e o ciclo repete até passar.

!!! question "Antes de continuar"  
    Pense num agente ou numa automação de IA que seu time usa hoje. Ele decide o próprio caminho a cada execução, ou segue, na prática, uma sequência fixa de passos vestida de "agente"? Isso muda o quanto você revisa o resultado antes de confiar nele?

O mesmo princípio vale para a escolha entre vibe coding, assistência de codificação e SDD, os três modos de trabalho da próxima página. Comece pelo mais simples que a tarefa permitir e suba de nível quando ela exigir, sem deixar a vontade de usar a ferramenta mais avançada decidir no seu lugar. Os critérios estão em [Quando cada modo se justifica](modos-de-trabalho.md#quando-cada-modo-se-justifica).

![Trajetória de complexidade crescente que parte de uma chamada direta, passa por fluxos de trabalho previsíveis e chega a um agente que decide os próprios passos. A autonomia aumenta junto com o custo de verificação, enquanto um alerta destaca o anti-padrão de tratar protótipo como produto.](../assets/images/s1-simplicidade-risco.png)

**Próxima página:** [Avaliação de modelos](avaliacao-de-modelos.md).
