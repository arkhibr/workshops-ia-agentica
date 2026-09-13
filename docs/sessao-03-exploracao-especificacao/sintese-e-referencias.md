# Síntese e referências

## Nove ideias essenciais

1. **O ciclo é explorar, perguntar, propor, especificar, nessa ordem.** Pular uma etapa não elimina o trabalho, só empurra o custo dela para a fase em que corrigir já significa reescrever.
2. **Um pedido vago não é descuido de quem pediu.** A cabeça de quem pediu já resolveu a ambiguidade sem perceber. O trabalho de perguntar é externalizar essa resolução antes que o agente a externalize errado.
3. **BR, FR e NFR respondem perguntas diferentes.** Regra de negócio existiria sem o sistema. Requisito funcional só existe em relação a ele. Requisito não funcional é o critério de qualidade sob o qual o funcional acontece.
4. **Regra de negócio disfarçada de requisito funcional é o antipadrão mais comum.** Quando a regra muda, ninguém encontra o número certo para trocar, porque ele nunca teve linha própria.
5. **Nem toda pergunta vale o mesmo.** Uma boa pergunta de elicitação muda o código que o agente vai gerar. Se as duas respostas possíveis produzem o mesmo resultado, a pergunta era decorativa.
6. **Especificação executável traz valor de entrada e resultado esperado.** O teste: alguém que nunca ouviu falar do domínio consegue escrever os casos de teste sem perguntar mais nada?
7. **Uma especificação pode estar certa e ainda produzir o sistema errado.** O [Estudo de caso](estudo-de-caso.md) mostrou isso: a falha estava na pergunta que nunca foi feita, com BR e FR perfeitamente fiéis um ao outro.
8. **O ciclo completo nem sempre compensa.** Mudança pequena, reversível, sem regra nova: resolve-se perguntando de cabeça. O ciclo formal se paga quando a regra é nova ou mais de uma pessoa vai manter o código depois.
9. **A régua de decisão desta sessão prepara a próxima.** A Sessão 4 formaliza a regra de negócio em si — vocabulário controlado, três formas de sentença, tabela de decisão — usando o mesmo material que esta sessão aprendeu a extrair de um pedido vago.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue nomear as quatro etapas do ciclo e explicar por que pular uma delas custa mais caro depois.
- [ ] Cada participante classifica um requisito real como BR, FR ou NFR sem hesitar.
- [ ] O grupo discutiu o Estudo de caso e chegou a um critério (não a uma opinião) sobre de quem é a responsabilidade quando a especificação cumpre exatamente o que diz e ainda assim erra.
- [ ] Cada participante rodou o ciclo completo do exercício-âncora e verificou os quatro casos novos por teste de verdade, não por leitura do código.
- [ ] Ninguém saiu achando que "especificar" é só escrever mais texto. O que conta é o texto ser verificável.

## Autoavaliação

1. Consigo escrever uma especificação executável para um pedido vago do meu próprio backlog, com pelo menos um caso concreto e um caso de fronteira?
2. Sei separar, numa frase que recebi de alguém, o que é regra de negócio do que é requisito funcional?
3. Consigo apontar, na minha própria especificação do exercício-âncora, qual pergunta teria sido fácil de pular e por que não pulei?
4. Diante de um pedido vago, sei dizer se o ciclo completo compensa ou se é exagero para aquele caso?

Se duas ou mais respostas forem "ainda não", releia [O ciclo de especificação](ciclo-de-especificacao.md) e [BR, FR e NFR](br-fr-nfr.md) antes da Sessão 4.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 4 assume que o time já sabe separar regra de negócio de requisito funcional e já pratica o hábito de perguntar antes de especificar. Ela aprofunda exatamente a regra de negócio: como formalizá-la em vocabulário controlado (SBVR), em frases sem ambiguidade (RuleSpeak) e em tabela de decisão (DMN) — com a IA no papel de formalizadora, sem autoridade para decidir a regra.
