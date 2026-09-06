# O arnês do agente

As quatro peças da página anterior têm um nome coletivo na engenharia. Ele importa porque muda a ordem das decisões: reconstruir o que cerca o modelo costuma render mais do que trocar de modelo.

## Tudo o que cerca o modelo

A aplicação agêntica, o arquivo de instrução, o catálogo de ferramentas, o isolamento e o nível de autonomia não são acessórios do modelo. Eles formam o sistema que transforma um modelo em agente, e a engenharia deu um nome a esse sistema: **arnês**, o mesmo termo do equipamento que prende um alpinista à parede. A formulação vem de Vivek Trivedy, em [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness): *"if you're not the model, you're the harness"*. Arnês é todo código, configuração e lógica de execução que não é o modelo. A equação que resume o campo:

**agente = modelo + arnês**

Comparando com a página anterior: das quatro peças do ambiente agêntico, o modelo é uma; as outras três são o arnês.

!!! warning "Um cuidado de vocabulário"
    O termo em inglês é *harness*, e você vai reencontrá-lo nas Sessões 6 e 7 com outro sentido, o de *test harness*: a estrutura que prepara, executa e verifica uma suíte de testes. São conceitos diferentes. Neste material, **arnês** em português é sempre o do agente, e *harness* em inglês fica reservado ao de teste.

## Reconstruir o arnês rende mais que trocar de modelo

Trivedy relata que a mesma família de modelo sai de fora das trinta primeiras posições para as cinco primeiras do Terminal Bench 2.0 quando apenas o arnês muda, e que um mesmo modelo pontua diferente dentro e fora do arnês de um produto comercial. A posição específica num placar envelhece rápido e não vale decorar; o que dura é a direção da relação. Addy Osmani formula o mesmo achado em [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/): um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

Isso fecha um ponto aberto na Sessão 1. Em [Avaliação de modelos](../sessao-01-o-que-mudou/avaliacao-de-modelos.md) ficou dito que o número divulgado num *benchmark* depende tanto da forma como o teste foi conduzido quanto do modelo medido. O nome dessa forma é arnês. Quando dois fabricantes anunciam resultados no mesmo *benchmark*, parte da diferença está no modelo e parte está no arnês que cada um usou para rodá-lo, e é por isso que a leitura independente, que avalia todos sob o mesmo arnês, vale mais que o número do anúncio de lançamento.

A consequência prática é de ordem de gasto. Trocar de modelo é uma decisão cara e visível, que costuma vir primeiro na conversa. Reconstruir o arnês é barata e invisível, e frequentemente move mais o resultado.

!!! question "Antes de continuar"
    Da última vez que o seu time discutiu qualidade de agente, a conversa foi sobre qual modelo usar ou sobre o que estava em volta dele? Se foi sobre o modelo, o que no arnês nunca chegou a ser examinado?

## Diagnosticar pelo tipo de falha

A utilidade de decompor o arnês em peças é transformar "o agente errou" numa hipótese endereçável. Cada tipo de falha aponta para uma peça diferente, e mexer na peça errada consome tempo sem mover o resultado. As páginas seguintes desta sessão tratam de cada uma delas.

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

Três perguntas organizam o trabalho de melhoria. Onde este agente falha mais, e a que peça esse tipo de falha corresponde? Ele tem alguma forma de conferir o próprio trabalho, e se não tem, qual seria a mais barata de dar a ele? Que contexto ele não recebe hoje e deveria receber, que hoje existe só na cabeça de alguém? A ordem entre elas importa, e trocar de modelo é a última.

!!! tip "Aplique agora"
    Pense na última vez em que um agente errou de um jeito que irritou você. Classifique aquele erro numa linha da tabela acima. A intervenção sugerida já existe no seu ambiente, ou é justamente o que está faltando?

**Próxima página:** [Engenharia de contexto](engenharia-de-contexto.md).
