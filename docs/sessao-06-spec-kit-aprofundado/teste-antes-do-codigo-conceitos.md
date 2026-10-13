# Teste antes do código: analyze e teste vermelho

Esta página trata da segunda metade do fluxo do GitHub Spec Kit, do `tasks` ao `implement`, quando a constitution do projeto exige que os testes de cada história falhem antes da implementação. O assunto é como o princípio de teste antes do código chega às tarefas, como o `analyze` confere essa ordem sem alterar nenhum arquivo e como saber que um teste verde testou alguma coisa.

## O princípio que gera as tarefas de teste

O modelo de tarefas da versão 1.1.1 trata os testes como opcionais. As instruções do comando `tasks` determinam que tarefas de teste só sejam geradas quando a spec as pede ou quando o usuário solicita a abordagem de desenvolvimento orientado por testes (TDD, *Test-Driven Development*). Sem esse pedido, o `tasks.md` pode chegar ao `implement` sem nenhuma tarefa de teste, e o agente escreve testes depois do código, se escrever.

Um princípio de constitution como "a implementação de uma história só começa depois que `npm test` mostra os testes dessa história falhando" muda essa saída. Com ele, o `tasks` organiza cada história em duas seções, os testes primeiro e a implementação depois, e o `implement` executa as tarefas nessa ordem. O teste da Sessão 5 para um princípio continua valendo: removido o princípio, as seções de teste desaparecem do `tasks.md`, e por isso ele muda a saída.

![Diagrama intitulado Teste vermelho conferido: o caminho de uma história até o verde. Uma linha de caixas mostra a sequência. Constitution, com o princípio II, a história só é implementada depois do vermelho. Tasks, em cada história, tarefas de teste antes das de implementação. Analyze, em caixa tracejada, portão somente leitura que aponta teste que nasce verde como CRITICAL. Implement, fase de testes da história, sem código de produção. Npm test vermelho, em vermelho, os testes da história falham. Do vermelho, uma seta desce para a caixa Parada humana: falhou pelo motivo certo? Sim, quando a asserção compara o valor esperado. Não, quando a falha é de importação, digitação ou de um teste que já passava antes. Da parada humana, uma seta marcada sim sobe para a última caixa, implement, código da história, até o npm test verde. À esquerda, abaixo, uma caixa tracejada com o título Fronteira protegida, depois do verde, diz para trocar menor ou igual por menor na comparação da regra e rodar npm test, e que, se algum teste falha, a suíte percebe a mudança na fronteira, e, se nenhum falha, falta o teste do valor exato do limite. Uma faixa inferior diz que o princípio II faz o tasks gerar os testes primeiro, o analyze confere a ordem antes da execução e a troca do operador mostra, depois do verde, se algum teste depende do valor exato do limite.](assets/teste-vermelho-conferido.png)

## Teste vermelho conferido

[Beck (2002)](../referencia/bibliografia.md#beck-test-driven-development-by-example-2002) descreve o TDD como um ciclo de três passos, vermelho, verde e refatoração, em que o teste é escrito antes do código e precisa falhar antes de passar. A falha inicial é a evidência de que o teste consegue detectar a ausência do comportamento que ele descreve. Um teste que passa desde a primeira execução não demonstrou essa capacidade, e o verde que ele mostra depois da implementação não informa nada sobre o código.

Com agentes de codificação, a ordem tem efeito medido. [Mathews e Nagappan (2024)](../referencia/bibliografia.md#mathews-e-nagappan-test-driven-development-and-llm-based-code-generation-2024) forneceram a modelos como GPT-4 e Llama 3 os casos de teste junto com o enunciado do problema, nos conjuntos de avaliação MBPP e HumanEval, e relataram que a inclusão dos testes aumentou de forma consistente a proporção de soluções corretas. Os dois conjuntos são formados por problemas do tamanho de uma função, e o resultado foi medido nessa escala de tarefa.

Conferir o vermelho exige ler o motivo da falha, além de contar as falhas. A falha esperada é a de uma asserção que compara o valor calculado com o valor que a regra determina, ou a de uma função que ainda não foi implementada. Três outras falhas indicam problema no próprio teste: erro de importação, que mostra um arquivo ou nome inexistente, erro de digitação no teste, e teste que passa enquanto os vizinhos falham, porque o comportamento que ele verifica já existia.

Dois antipadrões aparecem com frequência quando o agente conduz o ciclo. O primeiro é o teste que nunca falhou, gerado depois do código ou dependente de um valor que já estava pronto antes da história. O segundo é o agente que altera o teste para que ele passe, mantendo o código como estava, o que transforma a especificação executável numa descrição do que o código faz. A parada humana depois do vermelho existe para os dois casos, e o `git diff` dos arquivos de teste entre o commit do vermelho e o do verde mostra o segundo.

## Analyze

O `analyze` roda depois do `tasks` e antes do `implement` e lê a spec, o plano e as tarefas, conferindo-os contra a constitution. As instruções do comando o definem como estritamente somente leitura: ele produz um relatório, oferece sugestões de correção e não aplica nenhuma delas sem aprovação explícita.

O relatório classifica os achados em seis categorias, que são duplicação, ambiguidade, subespecificação, alinhamento com a constitution, lacunas de cobertura e inconsistência, com no máximo cinquenta achados. Cada achado recebe uma de quatro severidades:

| Severidade | Critério nas instruções do comando |
|---|---|
| CRITICAL | violação de um MUST da constitution, artefato central ausente ou requisito sem nenhuma tarefa que bloqueia a funcionalidade básica |
| HIGH | requisito duplicado ou conflitante, atributo de segurança ou desempenho ambíguo, critério de aceite que não pode ser testado |
| MEDIUM | variação de terminologia, requisito não funcional sem tarefa, caso de borda subespecificado |
| LOW | ajuste de redação e redundância que não afeta a ordem de execução |

Toda violação da constitution é classificada como CRITICAL, e as instruções afirmam que o princípio não pode ser diluído nem reinterpretado durante a análise. Com um princípio de teste vermelho, isso significa que o `analyze` aponta como crítica qualquer tarefa que coloque código de produção antes dos testes da história, ou um teste que já passaria no momento em que for escrito. O relatório traz também uma tabela de cobertura, com cada requisito e as tarefas que o atendem, e termina perguntando se o usuário quer sugestões concretas de correção.

## Implement por fase

As instruções do `implement` determinam a execução fase por fase, com as tarefas sequenciais em ordem e a marcação `[X]` de cada tarefa concluída no `tasks.md`. Como a parada humana não está no comando, ela entra pelo pedido: o `implement` aceita uma instrução junto com o comando, como executar só as fases de preparação e as tarefas de teste da primeira história e parar.

A execução em etapas cria o ponto de conferência do vermelho. O participante roda `npm test`, lê o motivo das falhas e só então pede ao agente que continue até o verde. A trava do checklist, tratada na página de conceitos do Tema 1, aparece antes da primeira tarefa e examina a escrita dos requisitos, enquanto a conferência do vermelho examina o resultado dos testes, e por isso uma não dispensa a outra.

## A fronteira protegida

Um teste verde mostra que o código atende aos casos que o teste verifica, e a pergunta seguinte é se a suíte detectaria uma mudança no código. Uma regra com limite numérico, como "valor até um teto", depende de um operador de comparação, e a troca de `<=` por `<` muda o resultado apenas no valor exato do limite. Se nenhum teste falha depois dessa troca, a suíte não tem o caso do valor exato, e um defeito nessa fronteira chegaria à produção sem aviso.

A troca manual de um operador, seguida de `npm test` e da restauração do código, é a versão de um caso só do teste de mutação, que a Sessão 7 automatiza com ferramentas que geram e executam centenas dessas alterações. Nesta sessão, a troca é feita à mão e numa única comparação, a da regra principal da história.

**Próxima página:** [Exemplo de aplicação de IA](teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md).
