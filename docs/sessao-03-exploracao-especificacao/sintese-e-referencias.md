# Síntese e referências

## Nove ideias essenciais

1. **O ciclo é explorar, perguntar, propor, especificar, nessa ordem.** Pular uma etapa transfere o custo dela para a fase em que corrigir já significa reescrever.
2. **Um pedido vago não é descuido de quem pediu.** A cabeça de quem pediu já resolveu a ambiguidade sem perceber. Perguntar é externalizar essa resolução antes que o agente a externalize errado.
3. **A intervenção socrática atrasa a convergência prematura.** Uma pergunta de cada vez, escolhida em função da resposta anterior, mantém mais de uma leitura de um pedido viva por mais tempo do que uma lista de perguntas escrita de uma vez só.
4. **BR, FR e NFR respondem perguntas diferentes.** Regra de negócio existiria sem o sistema. Requisito funcional só existe em relação a ele. Requisito não funcional é o critério de qualidade sob o qual o funcional acontece.
5. **Regra de negócio disfarçada de requisito funcional é o antipadrão mais comum.** Quando a regra muda, ninguém encontra o número certo para trocar, porque ele nunca teve linha própria.
6. **Especificação executável traz valor de entrada e resultado esperado.** O teste: alguém que nunca ouviu falar do domínio consegue escrever os casos de conferência sem perguntar mais nada?
7. **Uma especificação pode estar certa e ainda produzir o sistema errado.** O incidente do pedido acumulado, na página de decomposição de requisitos, mostrou isso: a falha estava na pergunta que nunca foi feita, com BR e FR perfeitamente fiéis um ao outro.
8. **O ciclo completo nem sempre compensa.** Mudança pequena, reversível, sem regra nova: resolve-se perguntando de cabeça. O ciclo formal se paga quando a regra é nova ou mais de uma pessoa vai manter o código depois.
9. **O critério de decisão desta sessão prepara a próxima.** A Sessão 4 formaliza a regra de negócio em si — vocabulário controlado, três formas de sentença, tabela de decisão — usando o mesmo material que esta sessão aprendeu a extrair de um pedido vago.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue nomear as quatro etapas do ciclo e explicar por que pular uma delas custa mais caro depois.
- [ ] Cada participante conduziu uma intervenção socrática completa, com o contrato de uma pergunta por mensagem respeitado, até um dossiê com registro de proveniência.
- [ ] Cada participante classifica um requisito real como BR, FR ou NFR sem hesitar.
- [ ] Cada participante rodou o exercício-âncora do seu tema e verificou os casos novos por execução de teste ou por retrotradução, e não por leitura do texto.
- [ ] Ninguém saiu achando que "especificar" é só escrever mais texto. O que conta é o texto ser verificável.

## Autoavaliação

1. Consigo escrever uma especificação executável para um pedido vago do meu próprio backlog, com pelo menos um caso concreto e um caso de fronteira?
2. Sei conduzir uma entrevista socrática respeitando o contrato de uma pergunta por mensagem, sem sugerir a resposta?
3. Sei separar, numa frase que recebi de alguém, o que é regra de negócio do que é requisito funcional?
4. Diante de um pedido vago, sei dizer se o ciclo completo compensa ou se é exagero para aquele caso?

Se duas ou mais respostas forem "ainda não", releia [Intervenção socrática e divergência do pensamento](intervencao-socratica-conceitos.md) e [Decomposição de requisitos: BR, FR e NFR](decomposicao-de-requisitos-conceitos.md) antes da Sessão 4.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 4 assume que o time já sabe separar regra de negócio de requisito funcional e já pratica o hábito de perguntar antes de especificar. Ela aprofunda exatamente a regra de negócio: como formalizá-la em vocabulário controlado (SBVR), em frases sem ambiguidade (RuleSpeak) e em tabela de decisão (DMN) — com a IA atuando como formalizadora, sem autoridade para decidir a regra.
