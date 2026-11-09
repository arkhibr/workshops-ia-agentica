# Síntese e referências

## Nove ideias essenciais

1. **O ciclo é explorar, perguntar, propor, especificar, nessa ordem.** Pular uma etapa transfere o custo dela para a fase em que corrigir já significa reescrever.
2. **Um pedido vago contém decisões que quem pediu já tomou sem registrar.** As perguntas registram essas decisões por escrito antes que o agente as preencha com suposições próprias.
3. **A intervenção socrática atrasa a convergência prematura.** Uma pergunta de cada vez, escolhida em função da resposta anterior, mantém mais de uma leitura de um pedido em consideração por mais tempo do que uma lista de perguntas escrita de uma vez só.
4. **BR, FR e NFR respondem perguntas diferentes.** A regra de negócio existiria sem o sistema, o requisito funcional descreve o comportamento do sistema que cumpre a regra, e o requisito não funcional define o critério de qualidade desse comportamento.
5. **Regra de negócio disfarçada de requisito funcional é o antipadrão mais comum.** Quando a regra muda, ninguém encontra o número certo para trocar, porque ele nunca teve linha própria.
6. **Especificação executável traz valor de entrada e resultado esperado.** O critério é verificar se alguém que nunca ouviu falar do domínio consegue escrever os casos de conferência sem perguntar mais nada?
7. **Uma especificação fiel ao pedido depende de uma elicitação que tenha feito todas as perguntas relevantes.** O incidente do pedido acumulado, na página de decomposição de requisitos, mostrou isso: a falha estava na pergunta que nunca foi feita, com BR e FR perfeitamente fiéis um ao outro.
8. **O ciclo completo nem sempre compensa.** Uma mudança pequena, reversível e sem regra nova pode ser resolvida com perguntas informais, sem registro escrito. O ciclo formal compensa o esforço quando a regra é nova ou quando mais de uma pessoa vai manter o código depois.
9. **O critério de decisão desta sessão prepara a próxima.** A Sessão 4 parte da separação entre regra de negócio e requisito funcional feita aqui e formaliza a regra com o vocabulário controlado do SBVR, as sentenças do RuleSpeak e tabelas de decisão, aplicados a um exemplo didático de IRPF com valores hipotéticos, a exercícios sobre o cashback do IBS e da CBS que terminam em casos de teste escritos em TDD e à recuperação de regras implícitas numa consulta SQL.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue nomear as quatro etapas do ciclo e explicar por que pular uma delas custa mais caro depois.
- [ ] Cada participante conduziu uma intervenção socrática completa, com o contrato de uma pergunta por mensagem respeitado, até um dossiê com registro de proveniência.
- [ ] Cada participante classifica um requisito real como BR, FR ou NFR sem hesitar.
- [ ] Cada participante rodou o exercício-âncora do seu tema e verificou os casos novos por execução de teste ou por retrotradução.
- [ ] O grupo reconhece que uma especificação só está pronta quando cada requisito tem um caso concreto que permite verificá-lo.

## Autoavaliação

1. Consigo escrever uma especificação executável para um pedido vago do meu próprio backlog, com pelo menos um caso concreto e um caso de fronteira?
2. Sei conduzir uma entrevista socrática respeitando o contrato de uma pergunta por mensagem, sem sugerir a resposta?
3. Sei separar, numa frase que recebi de alguém, o que é regra de negócio do que é requisito funcional?
4. Diante de um pedido vago, sei dizer se o ciclo completo compensa ou se é exagero para aquele caso?

Se duas ou mais respostas forem "ainda não", releia [Intervenção socrática e divergência do pensamento](intervencao-socratica-conceitos.md) e [Decomposição de requisitos: BR, FR e NFR](decomposicao-de-requisitos-conceitos.md) antes da Sessão 4.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 4 assume que o time já sabe separar regra de negócio de requisito funcional e já pratica o hábito de perguntar antes de especificar. Ela aprofunda a regra de negócio com vocabulário controlado (SBVR), sentenças sem ambiguidade (RuleSpeak) e tabelas de decisão com política de acerto (DMN), aplicados a um exemplo didático de IRPF com valores hipotéticos e a dois exercícios sobre o cashback do IBS e da CBS da Lei Complementar nº 214/2025, o segundo deles concluído com casos de teste escritos em TDD. A sessão termina com a arqueologia de regras em SQL, na qual o agente recupera as regras implícitas de uma consulta existente e cita as linhas que sustentam cada uma, sem autoridade para decidir qual regra vale.
