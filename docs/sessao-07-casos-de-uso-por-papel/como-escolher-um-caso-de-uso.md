# Como escolher um caso de uso de IA

Um caso de uso de IA é uma tarefa de trabalho com entrada, saída e verificação definidas, executada com apoio de um agente de IA generativa. Esta página apresenta os elementos que todo caso precisa declarar, a evidência de que o resultado da IA varia com o tipo de tarefa e com quem a executa, e quatro critérios que a turma usa nesta sessão para decidir quais casos do catálogo entram na rotina da equipe. As cinco páginas de papel aplicam esses critérios a quinze casos cada uma, num total de setenta e cinco casos.

## Os cinco elementos de um caso

Um caso fica completo quando declara cinco elementos. A tabela indica a pergunta que cada elemento responde, e a coluna de conferência das páginas por papel corresponde ao quarto elemento.

| Elemento | Pergunta que responde |
|---|---|
| Entrada | Que material o agente recebe, e esse material pode ser compartilhado? |
| Saída | Que formato o resultado tem, e quem o usa depois? |
| Pedido | Que papel, tarefa, formato e restrições o pedido declara? |
| Conferência | Contra que fonte o resultado é comparado antes de circular? |
| Decisão humana | Que parte da decisão permanece com uma pessoa nomeada? |

A conferência é parte do caso e não uma etapa que cada pessoa decide fazer ou não. Um caso sem fonte de comparação não tem como ser verificado, e o resultado dele circula na confiança de quem o gerou.

## O resultado depende da tarefa e de quem a executa

A evidência experimental publicada mostra efeitos que mudam de sinal conforme a tarefa. [Dell'Acqua et al. (2026)](../referencia/bibliografia.md#dellacqua-et-al-navigating-the-jagged-technological-frontier-2026) estudaram 758 profissionais de consultoria em 18 tarefas dentro da capacidade do modelo e relataram 12,2% mais tarefas concluídas e conclusão 25,1% mais rápida, enquanto numa tarefa fora dessa capacidade os participantes com IA tiveram 19% menos probabilidade de chegar à solução correta. Os autores chamam o limite entre os dois conjuntos de fronteira tecnológica irregular, porque ele não segue a dificuldade aparente da tarefa.

Outros experimentos medem ganhos em tarefas específicas. [Noy e Zhang (2023)](../referencia/bibliografia.md#noy-e-zhang-productivity-effects-of-generative-ai-2023) mediram, em 453 profissionais com tarefas de redação, redução de 40% no tempo e aumento de 18% na qualidade. [Brynjolfsson, Li e Raymond (2025)](../referencia/bibliografia.md#brynjolfsson-li-e-raymond-generative-ai-at-work-2025) analisaram 5.172 agentes de atendimento e relataram produtividade 15% maior, com melhora em velocidade e qualidade para os novatos e pequenas quedas de qualidade para os mais experientes. Em desenvolvimento de software, [Peng et al. (2023)](../referencia/bibliografia.md#peng-et-al-copilot-productivity-2023) mediram 55,8% de ganho de velocidade numa tarefa nova e delimitada, e o [METR (2025)](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025) mediu perda de tempo de desenvolvedores experientes em manutenção de sistema maduro, resultado apresentado na Sessão 1.

Cada estudo tem uma população, uma tarefa e uma métrica, e nenhum deles mede as tarefas da equipe que usa este material. O mural da oficina serve para a equipe registrar o que já experimentou, e o pitch do segundo bloco serve para medir um caso em tarefa real.

## A conferência exige desenho

A expectativa de que a pessoa perceba o erro durante o uso tem pouco apoio na pesquisa. [Parasuraman e Manzey (2010)](../referencia/bibliografia.md#parasuraman-e-manzey-complacency-and-bias-in-human-use-of-automation-2010), em revisão sobre automação em geral, concluem que a complacência e o viés de automação ocorrem em novatos e em especialistas e que treinamento e instruções não os evitam. [Lee et al. (2025)](../referencia/bibliografia.md#lee-et-al-impact-of-generative-ai-on-critical-thinking-2025) entrevistaram 319 trabalhadores do conhecimento sobre 936 usos de IA generativa e encontraram, em relatos dos próprios participantes, que maior confiança na IA se associa a menos pensamento crítico. Os dados desse estudo são autorrelatados pelos participantes, e a associação medida não permite concluir que a confiança cause a redução do pensamento crítico.

O que as duas fontes sustentam é uma decisão de projeto: a conferência fica no caso como passo explícito, com a fonte de comparação nomeada, como a comparação de cada decisão da ata com a fala na transcrição.

## Quatro critérios para escolher

A tabela reúne os critérios que a turma aplica ao classificar os cartões do mural. Os critérios de reversibilidade e de tempo de vida da [Sessão 1](../sessao-01-o-que-mudou/modos-de-trabalho.md) continuam valendo para os casos de código, e a tabela abaixo cobre as tarefas fora do código.

| Critério | Pergunta | Sinal favorável |
|---|---|---|
| Conferência | Existe uma fonte que a equipe conhece e contra a qual o resultado pode ser comparado? | Fonte nomeada e acessível a quem usa o resultado |
| Custo do erro | Se o erro passar, quanto custa desfazer? | Erro barato de corrigir, ou conferência integral antes de circular |
| Frequência | A tarefa se repete na rotina da equipe? | Repetição semanal ou mensal, que compensa o esforço de escrever o pedido-base |
| Dados | O material de entrada contém dado pessoal ou sigiloso? | Dado anonimizado ou ausente |

A conferência por amostra cabe quando o erro é barato de desfazer e a amostra representa o conjunto. Decisões, números e prazos que outras pessoas vão implementar pedem conferência integral, porque uma divergência isolada produz trabalho errado que ninguém questiona depois.

## Tarefas que ficam fora

Duas classes de tarefa ficam fora do catálogo, qualquer que seja o papel. A primeira reúne as tarefas cujo resultado ninguém na equipe consegue conferir, porque o critério de conferência não se cumpre. A segunda reúne as decisões que cabem a uma pessoa nomeada, como a prioridade de um item, a severidade final de um defeito ou a aprovação de um pagamento, em que o agente pode propor e a pessoa decide.

**Próxima página:** [Casos de uso para Product Owner](casos-product-owner.md).
