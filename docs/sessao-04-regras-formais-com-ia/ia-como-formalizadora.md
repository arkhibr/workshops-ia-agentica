# IA como formalizadora

Um agente de codificação é rápido para transformar prosa em vocabulário SBVR, sentença RuleSpeak ou tabela DMN — rápido demais para confiar sem verificar. O papel do agente aqui é formalizar, não decidir; quem decide se a formalização preservou a intenção continua sendo humano.

## O que muda quando o agente formaliza, não implementa

Nas sessões anteriores, o agente recebia uma especificação e produzia código. Aqui a direção se inverte: o agente recebe prosa ambígua ("o desconto de atacado nunca ultrapassa o teto") e devolve uma regra formal (SBVR, RuleSpeak ou uma linha de tabela DMN). O risco muda de natureza. Um código errado costuma falhar num teste. Uma formalização errada pode *parecer* certa (ler bem, usar os termos certos) e ainda assim ter mudado o escopo da regra original sem que ninguém notasse, porque não existe teste automatizado que verifique se uma frase captura a intenção de outra frase.

## Formalizando a partir do código, não só da prosa

A prosa ambígua não é a única entrada possível: o caso mais comum na prática é código legado, sem especificação nenhuma, em que a regra só existe dentro de um `if`. Formalizar a partir de código pede uma disciplina que formalizar a partir de prosa não exige: **não parafrasear a estrutura do código, traduzir a lógica para o vocabulário do domínio**. Parafrasear repete a variável; traduzir explica a decisão de negócio que a variável representa.

```text
if (pedido.status === 'PENDENTE' && pedido.criadoEm < agora - 30 * 60000) {
  cancelarPedido(pedido);
}
```

Parafrasear (ruim): "Se o status do pedido é PENDENTE e a diferença entre agora e criadoEm for maior que 30 minutos, cancela o pedido." Isso só reescreve o código em português, sem ganhar nada.

Traduzir (correto): "**RN-004**: Todo Pedido no estado Pendente **deve** ser cancelado se permanecer nesse estado por mais de 30 minutos. Evidência: `processarPedidos`, linha 42. Confiança: 🟢 confirmada."

A diferença entre as duas é a mesma de todo este material: a primeira ainda pensa em termos de variável e comparação; a segunda já pensa em termos de Pedido, Estado e prazo — os termos que sobrevivem a uma refatoração do código, porque descrevem o negócio, não a implementação atual dele.

## Verificação por retrotradução

A técnica mais confiável para essa checagem chama-se retrotradução: peça para uma segunda pessoa (ou para o próprio agente, numa conversa nova, sem ver a formalização) reescrever a regra formal de volta em prosa comum, sem consultar o original. Se a retrotradução bater com a intenção de quem escreveu a regra em primeiro lugar, a formalização provavelmente preservou o significado. Se a retrotradução disser outra coisa, a formalização mudou o escopo — silenciosamente.

Um exemplo: a prosa original diz "o desconto de atacado nunca ultrapassa o teto". O agente formaliza como RuleSpeak: "o desconto de um Pedido **não deve** exceder R$ 1.000,00". A retrotradução, pedida a quem não viu a prosa original, devolve: "nenhum pedido pode ter desconto maior que R$ 1.000,00" — e aqui já apareceu uma diferença: a prosa original falava só do desconto de *atacado*; a retrotradução generalizou para *qualquer* pedido. O agente ampliou o escopo da regra sem avisar, e só a retrotradução expôs isso.

!!! question "Antes de continuar"
    Pense numa vez em que você aceitou uma reformulação do agente (de código, de regra, de especificação) sem checar se o significado continuava o mesmo. Como você teria percebido, se tivesse percebido, que algo mudou?

## Onde o agente costuma errar sozinho

Três erros se repetem quando um agente formaliza sem supervisão:

- **Generalizar o escopo.** Uma regra que valia só para um tipo de cliente vira uma regra para "todo pedido", porque a formalização mais simples é a mais genérica, e o agente não sabe que a restrição de escopo era intencional.
- **Inventar a política de acerto.** Ao montar uma tabela de decisão, o agente escolhe uma política (geralmente First ou Unique) sem que ninguém tenha decidido isso — e a escolha errada só aparece quando duas linhas realmente se sobrepõem em produção.
- **Confundir regra estrutural com operativa.** "Todo Pedido tem um Cliente" (estrutural) e "o desconto não ultrapassa o teto" (operativa) podem sair da mesma formalização com o mesmo operador modal, se o agente não tiver sido instruído a distinguir as duas.

## O antipadrão de aceitar a formalização porque "parece certa"

O sintoma: a regra formalizada usa os termos certos, tem a forma gramatical certa de RuleSpeak, e ainda assim ninguém comparou com a intenção original, porque "parece profissional" foi confundido com "está correta". A formalização de uma regra de negócio não é uma tarefa de estilo — é uma tarefa de fidelidade semântica, e a única forma barata de checar fidelidade semântica é o back-translation, não a leitura de quem já sabe o que queria dizer e por isso lê a própria intenção onde ela não está escrita.

!!! tip "Aplique agora"
    Na próxima vez que pedir a um agente para formalizar uma regra, peça também, numa conversa separada, para retrotraduzir o resultado sem contexto adicional. Compare as duas frases antes de aceitar a formalização como pronta.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
