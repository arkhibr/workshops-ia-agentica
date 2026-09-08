# Síntese e referências

## Nove ideias essenciais

1. **Vocabulário vem antes de regra.** "O desconto do pedido" só é uma frase precisa se "pedido" e "desconto" já são termos definidos, não palavras do dia a dia.
2. **Regra estrutural define; regra operativa rege conduta.** O teste que separa as duas: alguém pode violá-la, ou ela só descreve como o negócio organiza seus conceitos?
3. **RuleSpeak tem três formas que contam como regra: "deve", "não deve" e "pode ... somente se".** "Deveria" não é nenhuma das três — é sugestão sem compromisso, não regra de negócio.
4. **Tabela de decisão torna combinação visível.** Quando duas ou mais condições combinam, prosa esconde a combinação que ninguém tratou; tabela expõe a linha que falta.
5. **Toda tabela de decisão precisa de uma política de acerto declarada.** Sem ela, alguém decide sozinho — geralmente o agente que implementa, tratando a tabela como First por padrão, sem que ninguém tenha pedido isso.
6. **Um agente formaliza rápido, e isso não é garantia de fidelidade.** Formalização errada pode ler bem e ainda ter mudado o escopo da regra original, porque não existe teste automatizado que verifique se uma frase captura a intenção de outra.
7. **Retrotradução é a verificação mais barata.** Peça para reescrever a regra formal de volta em prosa, numa conversa que não viu a formalização, e compare com a intenção original.
8. **O [Estudo de caso](estudo-de-caso.md) mostrou o custo de pular a política de acerto.** Cada linha da tabela estava certa isoladamente; a falha foi não decidir o que fazer quando duas se aplicam ao mesmo pedido.
9. **A régua desta sessão prepara a Sessão 5.** Regra formalizada, com vocabulário e tabela de decisão, é o insumo que a decomposição em planos executáveis vai fatiar em tarefas — sem essa formalização, o plano herdaria a mesma ambiguidade que esta sessão eliminou.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue distinguir regra estrutural de operativa usando o teste de violação, não só decorando os nomes.
- [ ] Cada participante reescreve uma regra vaga do próprio backlog numa das três formas do RuleSpeak.
- [ ] O grupo discutiu o Estudo de caso e chegou a um critério (não a uma opinião) sobre quando revisar sobreposição de tabela é obrigatório.
- [ ] Cada participante formalizou uma regra com o agente e verificou por retrotradução, numa conversa separada, se o escopo se manteve.
- [ ] Ninguém saiu achando que uma formalização "que parece profissional" é o mesmo que uma formalização verificada.

## Autoavaliação

1. Consigo explicar a diferença entre regra estrutural e operativa com um exemplo próprio, não só com o da Vetor?
2. Sei reescrever uma regra vaga do meu backlog em "deve", "não deve" ou "pode ... somente se"?
3. Diante de uma tabela de decisão com mais de uma dimensão de condição, sei procurar sobreposição antes de aceitar a implementação?
4. Consigo, na minha própria formalização do exercício-âncora, dizer exatamente o que a retrotradução confirmou ou expôs como divergente?

Se duas ou mais respostas forem "ainda não", releia [SBVR: vocabulário e regras](sbvr-vocabulario-e-regras.md) e [RuleSpeak: três formas de sentença](rulespeak-tres-formas.md) antes da Sessão 5.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 5 assume que o time já sabe formalizar uma regra de negócio em vocabulário controlado e verificar a formalização por retrotradução. Ela avança para a decomposição: transformar a especificação BR/FR/NFR e a regra formalizada num plano executável, fatiado em tarefas que um agente consegue atacar uma de cada vez — o mesmo cuidado de "nada fica implícito", visto aqui para a regra, reaparece lá para o plano inteiro.
