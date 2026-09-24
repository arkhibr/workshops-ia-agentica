# Vocabulário e sentenças de regra: SBVR e RuleSpeak

"O desconto de atacado nunca ultrapassa o teto" parece uma frase sem ambiguidade, até alguém perguntar se "o teto" é por pedido, por cliente ou por mês, e descobrir que cada pessoa do time já assumia uma resposta diferente, em silêncio. Antes de escrever uma regra assim sem ambiguidade, o time precisa concordar no que os termos da regra significam, e depois escolher a forma de sentença que não deixa a intenção para adivinhar. Esta página trata das duas coisas: o vocabulário controlado do SBVR e as três formas de sentença do RuleSpeak.

## O que o SBVR é

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é uma especificação da OMG para representar vocabulário de negócio e regras de forma que uma máquina e uma pessoa leiam a mesma coisa. Não é linguagem de programação: é um jeito de dizer "estes são os termos que usamos, e estas são as regras que valem sobre eles" de forma estruturada.

## Vocabulário: termo, definição, sinônimo a evitar

Um vocabulário SBVR nomeia os **termos** do domínio ("Pedido", "Cliente", "Faixa de Desconto") e os **fatos** que os relacionam ("um Pedido tem um Valor Total"). Só depois de o vocabulário existir é que uma regra pode ser escrita sem ambiguidade: "o desconto do pedido" só é uma frase precisa se "pedido" e "desconto" já são termos definidos, não palavras do dia a dia.

Em código real, o mesmo conceito quase sempre aparece com mais de um nome (`valorTotal`, `total`, `valorPedido` no mesmo módulo), e cada variante é dívida terminológica, não sinônimo inofensivo:

| Termo | Definição | Sinônimos a evitar |
|---|---|---|
| Pedido | Solicitação de compra, com um Valor Total e um Cliente associado | "order", "compra" |
| Cliente | Quem faz o Pedido; tem um Tipo (padrão ou atacado) | "usuário", "conta" |
| Valor Total | Soma dos itens do Pedido, antes de qualquer desconto | "total", "valorPedido" |

A coluna de sinônimos não é estética: cada entrada nela é um lugar concreto do código, ou da planilha, onde alguém, no futuro, vai comparar a string errada ou ler a célula errada.

## Regra estrutural: classificação e derivação

O SBVR distingue duas categorias amplas de regra. **Regra estrutural** (ou definicional) diz como o negócio organiza seus próprios conceitos, usando operadores aléticos — "é necessário que", "é possível que" — e não pode ser violada, porque define o que algo *é*, não como alguém deve agir. Ela aparece em duas formas concretas:

- **Classificação.** "Um Pedido cujo Cliente tem mais de 5 pedidos aprovados é um Pedido de Cliente Recorrente." Nomeia um subtipo a partir de uma condição — o `if` que, no código, decide silenciosamente que categoria está sendo tratada, sem que o conceito jamais receba nome próprio.
- **Derivação.** "O Desconto de um Pedido é calculado como Valor Total multiplicado pelo percentual da Faixa correspondente." Explica de onde vem um valor computado, o cálculo que o código já faz mas raramente aparece como regra nomeada.

Confundir as duas com regra operativa é o erro mais comum ao formalizar: "o sistema deve calcular o desconto" soa como obrigação, mas o que está sendo descrito é uma derivação, e não existe "violação" possível de uma fórmula, só um resultado certo ou errado.

## Regra operativa: obrigação, proibição, permissão

**Regra operativa** (ou comportamental) rege conduta, usando operadores deônticos: "é obrigatório que", "é permitido que". "É obrigatório que o desconto de um Pedido não ultrapasse o teto" é operativa, porque alguém, ou algum sistema, pode violá-la.

| | Estrutural — classificação | Estrutural — derivação | Operativa |
|---|---|---|---|
| Operador | Alético ("é") | Alético ("é calculado como") | Deôntico ("obrigatório", "permitido") |
| Pode ser violada? | Não | Não | Sim |
| Exemplo genérico | Um Pedido com mais de 5 compras aprovadas é de Cliente Recorrente | O Desconto é o Valor Total vezes o percentual da faixa | O desconto nunca ultrapassa o teto |

!!! question "Antes de continuar"
    Pegue uma regra de negócio conhecida do seu próprio domínio. Ela tem, escondida dentro dela, uma regra de classificação que nunca ganhou nome próprio? Nomeá-la muda alguma coisa em como você formaliza o resto da regra?

## RuleSpeak: as três formas que valem como regra

[Ross](../referencia/bibliografia.md#ross-rulespeak) organiza a regra operativa em torno de três palavras-chave fixas (originalmente "must", "must not", "may ... only"), aqui em português:

- **"Deve" — algo é exigido.** "O desconto de um Pedido **deve** respeitar o teto de R$ 1.000,00." Sem exceção implícita: se a regra usa "deve", toda instância precisa cumpri-la.
- **"Não deve" — algo é proibido.** "Um Pedido de cliente atacado **não deve** receber a faixa de 20% se o valor for R$ 10.000,00 ou menos." Também sem exceção implícita: se existir exceção, ela vira outra regra, explícita.
- **"Pode ... somente se" — algo é permitido, só sob condição.** "Um Pedido **pode** receber o desconto de cliente recorrente **somente se** `pedidosAprovados` for maior que 5." Nomeia a condição que abre a permissão: sem ela, a permissão não existe.

Só essas três formas contam como regra de negócio no vocabulário do RuleSpeak. "Deveria" não é nenhuma delas: é sugestão sem compromisso, e cada pessoa que a lê decide sozinha se ela vale sempre, às vezes, ou nunca. Quando alguém escreve "deveria", a régua é perguntar: isso é "deve", é "pode ... somente se", ou é só preferência que ainda não virou regra?

## Numeração, evidência e confiança

Uma regra solta, sem número, se perde entre a especificação e o código, e ninguém consegue apontar, meses depois, se ela ainda está implementada. Três disciplinas resolvem isso, e valem tanto para regra operativa quanto para as estruturais:

- **Numeração por tipo.** `RN` para regra operativa, `RD` para regra de classificação ou derivação. `RN-001`, `RD-001`: sequencial, sem reaproveitar número de regra removida.
- **Evidência obrigatória.** Toda regra formalizada a partir de um artefato existente cita a localização exata: arquivo e linha, se veio de código; aba e célula, se veio de planilha. Sem evidência, a regra permanece hipótese.
- **Confiança explícita.** 🟢 confirmada (o artefato confirma exatamente essa regra); 🟡 inferida (parece ser a regra, mas ninguém do domínio validou); 🔴 lacuna (o domínio espera essa regra, mas não há evidência dela em lugar nenhum).

```text
RN-003: Um Pedido pode receber o adicional de recorrência somente se
        o Cliente tiver mais de 5 pedidos aprovados.
Evidência: src/desconto.js, função calcularDesconto, ainda não implementada
Confiança: 🔴 lacuna
```

!!! tip "Aplique agora"
    Escreva o vocabulário mínimo de uma regra do seu próprio domínio, com a coluna de sinônimos a evitar, e classifique-a: é regra estrutural (classificação ou derivação) ou operativa? Se for operativa, qual das três formas do RuleSpeak ela assume?

**Próxima página:** [Exemplo de aplicação de IA](vocabulario-e-sentencas-exemplo-de-aplicacao-de-ia.md).
