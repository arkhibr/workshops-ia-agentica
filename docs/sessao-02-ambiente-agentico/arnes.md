# O arnês do agente

As quatro peças da página anterior têm um nome coletivo na engenharia. Ele importa porque muda a ordem das decisões: estabelecer o que cerca o modelo costuma render mais do que trocar de modelo.

## Tudo o que cerca o modelo

A aplicação agêntica, o arquivo de instrução, o catálogo de ferramentas, o isolamento e o nível de autonomia não são acessórios do modelo. Eles formam o sistema que transforma um modelo em agente, e a engenharia deu um nome a esse sistema: **arnês**, o mesmo termo do equipamento que prende um alpinista à parede. A formulação vem de [Vivek Trivedy, em "The Anatomy of an Agent Harness"](../referencia/bibliografia.md#trivedy-the-anatomy-of-an-agent-harness-2026): *"if you're not the model, you're the harness"*. Arnês é todo código, configuração e lógica de execução que não é o modelo. A equação que resume o campo:

**agente = modelo + arnês**

Comparando com a página anterior: das quatro peças do ambiente agêntico, o modelo é uma. As outras três são o arnês.

!!! warning "Um cuidado de vocabulário"
    O termo em inglês é *harness*, e você vai reencontrá-lo nas Sessões 6 e 7 com outro sentido, o de *test harness*: a estrutura que prepara, executa e verifica uma suíte de testes. São conceitos diferentes. Neste material, **arnês** em português é sempre o do agente, e *harness* em inglês fica reservado ao de teste.

## A aritmética do erro composto

Esta é a razão técnica pela qual o arnês existe, e ela é menos intuitiva do que parece.

Um agente é um processo de muitas etapas, e etapas se compõem por multiplicação, não por média. Suponha uma confiabilidade de 99% por etapa, um número que soaria excelente em qualquer outro contexto:

| Etapas na trajetória | Confiabilidade por etapa | Chance de a trajetória inteira dar certo |
|---:|---:|---:|
| 10 | 99% | 90,4% |
| 20 | 99% | 81,8% |
| 50 | 99% | 60,5% |

A conta é `0,99^n`. Uma taxa de acerto por passo que pareceria ótima num classificador isolado produz uma taxa de fracasso relevante numa trajetória longa. A [Anthropic registra o mesmo fenômeno no guia "Building Effective Agents"](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), já citado na Sessão 1: a autonomia dos agentes traz custo maior e **erros que se compõem**.

O ponto que decide onde investir é este: o modelo não é o lugar onde esse problema se resolve, porque o problema é estrutural do encadeamento. Ele se ataca no arnês, por quatro vias:

- **Verificação.** Dar ao agente uma forma de conferir o próprio trabalho antes de avançar, o que corta a propagação na origem.
- **Pontos de parada.** Interromper a trajetória em fronteiras definidas, para que um erro não atravesse dez etapas antes de aparecer.
- **Redução do espaço de decisão.** Menos ambiguidade por etapa significa menos chance de escolha errada.
- **Contexto limpo.** Menos ruído na janela significa menos chance de o modelo interpretar mal o estado atual.

A matemática também impõe um limite honesto, que contraria o reflexo de melhorar cada passo. Reduzir o número de etapas costuma ser mais eficaz que aumentar a confiabilidade de cada uma: um fluxo de dez passos com 99% é mais confiável que um de cinquenta passos com 99,5%.

!!! question "Antes de continuar"
    Pense na tarefa mais longa que você já entregou a um agente. Quantas etapas ela tinha, mais ou menos? Aplicando a tabela acima, qual era a chance de a trajetória inteira sair certa, e isso bate com o que aconteceu?

## Os componentes do arnês

A lista abaixo reúne os componentes que aparecem de forma recorrente nos ensaios de [Trivedy](../referencia/bibliografia.md#trivedy-the-anatomy-of-an-agent-harness-2026) e de [Addy Osmani](../referencia/bibliografia.md#osmani-agent-harness-engineering-2026) e na documentação da Anthropic. A coluna da direita mostra que esta sessão já trata quase todos eles, dispersos entre as páginas. O vocabulário de arnês é o que permite tratá-los como um sistema único e projetá-los juntos.

| Componente | Pergunta que ele responde | Onde esta sessão trata |
|---|---|---|
| Instrução de sistema | Que convenções e limites governam toda tarefa? | [O arquivo de instrução](arquivo-de-instrucao.md) |
| Ferramentas | O que o agente pode fazer, e com que contrato? | [MCP e ferramentas externas](mcp.md) |
| Gestão de contexto | O que entra na janela agora, e o que é descartado? | [Engenharia de contexto](engenharia-de-contexto.md) |
| Verificação | Como o agente confere o que fez antes de avançar? | [O arquivo de instrução](arquivo-de-instrucao.md#como-saber-se-o-arquivo-ainda-funciona), e a esteira de CI das Sessões 6 e 10 |
| Memória | O que persiste entre execuções, com que autorização? | Fora do escopo desta sessão |
| Isolamento | Onde o agente roda sem alcançar o trabalho de outra pessoa? | [Isolamento por ramo](isolamento-por-ramo.md) |
| *Hooks* | Em que ponto do ciclo um controle determinístico intervém? | [Autonomia e supervisão](autonomia-e-supervisao.md) |

Os dois primeiros itens costumam receber toda a atenção, e são os de menor retorno isolado. O quarto, verificação, é o de maior retorno comprovado, pelo motivo aritmético da seção anterior.

Vale registrar de onde vem esse vocabulário, para não importá-lo sem crítica. Ele nasceu na comunidade de agentes de codificação, que é exatamente o caso deste workshop, onde o arnês é um programa de linha de comando e os componentes têm nomes de arquivo concretos. A [Anthropic documenta essa camada em "Steering Claude Code"](../referencia/bibliografia.md#anthropic-steering-claude-code-2026), separando os mecanismos que **guiam** o modelo, como arquivos de contexto, dos que **impõem** comportamento, como *hooks* e permissões. A distinção sustenta uma regra que vale para o resto do workshop: uma proteção real precisa ser determinística. O arquivo de instrução pede um comportamento ao modelo, e o *hook* o impõe na camada de execução.

![Dois desenvolvedores seguem caminhos opostos. À esquerda, o GPT Astra opera num ambiente desorganizado, com erros, ferramentas soltas e baixo desempenho. À direita, o GPT Luna alcança desempenho superior conectado a um arnês organizado de instruções, ferramentas, contexto e verificação.](../assets/images/s2-astra-luna-arnes-performance.png)

## Estabelecer o arnês rende mais que trocar de modelo

[Trivedy](../referencia/bibliografia.md#trivedy-the-anatomy-of-an-agent-harness-2026) relata que a mesma família de modelo sai de fora das trinta primeiras posições para as cinco primeiras do Terminal Bench 2.0 quando apenas o arnês muda, e que um mesmo modelo pontua diferente dentro e fora do arnês de um produto comercial. A posição específica num placar envelhece rápido e não vale decorar. O que dura é a direção da relação. [Osmani formula o mesmo achado em "Agent Harness Engineering"](../referencia/bibliografia.md#osmani-agent-harness-engineering-2026): um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

Isso fecha um ponto aberto na Sessão 1. Em [Avaliação de modelos](../sessao-01-o-que-mudou/avaliacao-de-modelos.md) ficou dito que o número divulgado num *benchmark* depende tanto da forma como o teste foi conduzido quanto do modelo medido, e que a leitura independente do DeepSWE roda cada modelo na melhor configuração disponível do `mini-swe-agent`. O nome dessa configuração é arnês, e é por isso que a nota mede o par, não o modelo sozinho.

A consequência prática é de ordem de gasto. Trocar de modelo é uma decisão cara e visível, que costuma vir primeiro na conversa. Estabelecer o arnês é barato e invisível, e frequentemente move mais o resultado.

## Mais ferramentas não significa menos erro

A intuição diante de um agente que erra é ampliar a capacidade dele. A evidência aponta para o contrário. A [Vercel removeu 80% das ferramentas](../referencia/bibliografia.md#vercel-removing-80-of-agent-tools-2026) de um agente que traduzia texto para SQL, trocando dezesseis ferramentas especializadas por acesso a um sistema de arquivos com execução de comandos, e relatou a taxa de sucesso subindo de 80% para 100%, com 40% menos *tokens*, 40% menos passos e o tempo médio de resposta caindo de 274 para 77 segundos.

A explicação é a mesma do erro composto. Cada ferramenta adicional amplia o espaço de decisão de cada etapa, e ferramentas com fronteiras parecidas criam pontos de decisão ambíguos. A [orientação da Anthropic em "Writing effective tools for agents"](../referencia/bibliografia.md#anthropic-writing-effective-tools-for-agents-2025) formula o critério de um jeito que dá para verificar: se uma pessoa da engenharia não consegue dizer com segurança qual ferramenta usar numa situação, não dá para esperar que o modelo decida melhor. O corolário é consolidar ferramentas por fluxo de trabalho em vez de espelhar cada endpoint da API, e nomeá-las com prefixos que revelem a fronteira.

Existe um custo simétrico que a lição não deve esconder. Descrições de ferramenta ocupam contexto antes de qualquer requisição: a [Anthropic relata, em "Code execution with MCP"](../referencia/bibliografia.md#anthropic-code-execution-with-mcp-2025), um caso em que carregar definições sob demanda, em vez de todas de uma vez, reduziu o consumo de 150 mil para 2 mil *tokens*. Catálogo mínimo é, ao mesmo tempo, decisão de qualidade e decisão de custo.

Projetar um arnês é otimizar o caminho até o resultado certo, e a operação que mais frequentemente melhora esse caminho é uma remoção.

## Diagnosticar pelo tipo de falha

A utilidade de decompor o arnês em peças é transformar "o agente errou" numa hipótese endereçável. Cada tipo de falha aponta para uma peça diferente, e mexer na peça errada consome tempo sem mover o resultado.

| Sintoma observado | Peça provável | Primeira intervenção |
|---|---|---|
| Violou uma convenção que ninguém escreveu | arquivo de instrução | tornar explícitos os comandos, as convenções e o que nunca fazer |
| Escolheu a ferramenta errada entre opções parecidas | catálogo de ferramentas | consolidar o catálogo e descrever fronteiras |
| Buscou informação que não existe no repositório | acesso externo | avaliar se o caso pede um servidor MCP |
| Perdeu o fio numa tarefa longa | gestão de contexto | recortar o contexto por etapa e resumir o estado |
| Duas sessões se atrapalharam no mesmo diretório | isolamento | um ramo de trabalho por tarefa |
| Produziu efeito difícil de reverter sem ninguém aprovar | autonomia | baixar o nível de permissão para aquele tipo de ação |
| Ignorou a convenção documentada na hora de executar | *hooks* | impor o limite na camada de execução |
| O erro atravessou várias etapas antes de aparecer | verificação | dar ao agente um comando de verificação a cada etapa |

A última linha é a de maior retorno, e a Sessão 9 volta a ela: a depuração sistemática de um agente começa por perguntar em que etapa a verificação faltou.

Quatro perguntas organizam o trabalho de melhoria. Onde este agente falha mais, e a que peça esse tipo de falha corresponde? Ele tem alguma forma de conferir o próprio trabalho, e se não tem, qual seria a mais barata de dar a ele? Que contexto ele não recebe hoje e deveria receber, que hoje existe só na cabeça de alguém? E qual das tarefas que ele executa tem critério de sucesso inteiramente objetivo, porque essa é a candidata a receber mais autonomia. A ordem entre elas importa, e trocar de modelo é a última.

## O arnês é onde mora a autoridade

Há uma leitura arquitetural que o vocabulário de arnês torna nítida. Tudo o que decide **se** uma ação acontece vive no arnês, fora do modelo. O catálogo apresentado ao modelo é interface de descoberta. A permissão é avaliada por quem executa. A aprovação vincula uma pessoa a um objeto e a um prazo. O *hook* interrompe num ponto definido pelo projeto. Quando alguém diz que "o agente decidiu pedir confirmação", ou o arnês define esse ponto explicitamente, ou não existe ponto nenhum e o que houve foi coincidência.

Isso também delimita o que um bom arnês não faz. Ele reduz a probabilidade de erro e limita o raio de impacto. Ele não torna segura uma ação irreversível, não substitui a aceitação de risco por alguém com nome, e não produz autorização.

!!! tip "Aplique agora"
    Pense na última vez em que um agente errou de um jeito que irritou você. Classifique aquele erro numa linha da tabela de diagnóstico. A intervenção sugerida já existe no seu ambiente, ou é justamente o que está faltando?

**Próxima página:** [Engenharia de contexto](engenharia-de-contexto.md).
