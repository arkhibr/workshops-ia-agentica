# SBVR: vocabulário e regras

Antes de escrever uma regra sem ambiguidade, o time precisa concordar no que os termos da regra significam. SBVR separa essas duas coisas, vocabulário e regra, e distingue formas de regra que se confundem na prosa comum — e que o código, sozinho, esconde umas dentro das outras.

## O que o SBVR é

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é uma especificação da OMG, a mesma organização por trás do DMN visto adiante nesta sessão, para representar vocabulário de negócio e regras de forma que uma máquina e uma pessoa leiam a mesma coisa. Ele não é uma linguagem de programação: é um jeito de dizer "estes são os termos que usamos, e estas são as regras que valem sobre eles" de forma estruturada.

## Vocabulário: termo, definição, sinônimo a evitar

Um vocabulário SBVR nomeia os **termos** do domínio ("Pedido", "Cliente", "Faixa de Desconto") e os **fatos** que os relacionam ("um Pedido tem um Valor Total", "um Cliente tem um Tipo"). Só depois de o vocabulário existir é que uma regra pode ser escrita sem ambiguidade — "o desconto do pedido" só é uma frase precisa se "pedido" e "desconto" já são termos definidos, não palavras do dia a dia.

Em código real, o mesmo conceito quase sempre aparece com mais de um nome (`valorTotal`, `total`, `valorPedido` no mesmo módulo), e cada variante é dívida terminológica, não sinônimo inofensivo. Um vocabulário maduro registra isso explicitamente:

| Termo | Definição | Sinônimos a evitar |
|---|---|---|
| Pedido | Solicitação de compra, com um Valor Total e um Cliente associado | "order", "compra" |
| Cliente | Quem faz o Pedido; tem um Tipo (padrão ou atacado) | "usuário", "conta" |
| Valor Total | Soma dos itens do Pedido, antes de qualquer desconto | "total", "valorPedido" |

A coluna de sinônimos não é estética: cada entrada nela é um lugar concreto do código onde alguém, no futuro, vai comparar a string errada ou ler a variável errada. Registrar o sinônimo é registrar onde a próxima ambiguidade provavelmente nasce.

## Regra estrutural: classificação e derivação

O SBVR distingue duas categorias amplas de regra. **Regra estrutural** (ou definicional) diz como o negócio organiza seus próprios conceitos, usando operadores aléticos — "é necessário que", "é possível que". Ela não pode ser violada: define o que algo *é*, não como alguém deve agir. Na prática, regra estrutural aparece quase sempre em duas formas concretas:

- **Classificação.** "Um Pedido cujo Cliente tem mais de 5 pedidos aprovados é um Pedido de Cliente Recorrente." Essa forma nomeia um subtipo a partir de uma condição — o `if` que, no código, decide silenciosamente que categoria de cliente está sendo tratada, sem que o conceito "Cliente Recorrente" jamais receba nome próprio na especificação.
- **Derivação.** "O Desconto de um Pedido é calculado como Valor Total multiplicado pelo percentual da Faixa correspondente." Essa forma explica de onde vem um valor computado — o cálculo que o código já faz, mas que raramente aparece como regra nomeada e numerada, só como implementação.

Confundir as duas com regra operativa é o erro mais comum ao formalizar: "o sistema deve calcular o desconto" soa como obrigação, mas o que está sendo descrito é uma derivação — não existe "violação" possível de uma fórmula, só um resultado certo ou errado.

## Regra operativa: obrigação, proibição, permissão

**Regra operativa** (ou comportamental) rege conduta, usando operadores deônticos: "é obrigatório que", "é permitido que". "É obrigatório que o desconto de um Pedido não ultrapasse o teto" é operativa: alguém, ou algum sistema, pode violá-la — e é exatamente essa possibilidade de violação que a torna operativa, não estrutural. A [RuleSpeak: três formas de sentença](rulespeak-tres-formas.md), próxima página, detalha as três formas que a regra operativa assume.

| | Estrutural — classificação | Estrutural — derivação | Operativa |
|---|---|---|---|
| Operador | Alético ("é") | Alético ("é calculado como") | Deôntico ("obrigatório", "permitido") |
| O que define | A que subtipo algo pertence | De onde vem um valor | Como alguém deve se comportar |
| Pode ser violada? | Não — é classificação | Não — é fórmula | Sim — é conduta |
| Exemplo genérico | Um Pedido com mais de 5 compras aprovadas é de Cliente Recorrente | O Desconto é o Valor Total vezes o percentual da faixa | O desconto nunca ultrapassa o teto |

!!! question "Antes de continuar"
    Pegue a regra de cliente recorrente da Sessão 3. Ela tem, escondida dentro dela, uma regra de classificação que nunca ganhou nome próprio ("Cliente Recorrente")? Nomeá-la muda alguma coisa em como você formaliza o resto da regra?

## Por que isso importa antes de formalizar

Confundir as três formas produz uma tabela de decisão mal desenhada, tema da página seguinte. Regra de classificação e regra de derivação não entram como linha de uma tabela de decisão sobre conduta — elas são o vocabulário e a fórmula que a tabela pressupõe, não uma condição a avaliar junto com as demais. Só a regra operativa, a que rege conduta e pode ser violada, é candidata a virar linha de tabela.

O vocabulário também previne um erro comum na especificação BR/FR da Sessão 3: escrever "cliente" numa frase e "Cliente" (com tipo, com atributos) noutra, sem que as duas se refiram à mesma coisa. Um vocabulário SBVR, mesmo informal, com a coluna de sinônimos a evitar, resolve isso antes de a regra ser escrita.

!!! tip "Aplique agora"
    Escreva o vocabulário mínimo de uma regra de desconto por faixa de valor, com a coluna de sinônimos a evitar: liste os termos (Pedido, Cliente, Valor Total, Tipo de Cliente, Desconto, Teto) e, para cada um, a definição e ao menos um sinônimo que já apareceu (ou apareceria) no código com outro nome.

**Próxima página:** [RuleSpeak: três formas de sentença](rulespeak-tres-formas.md).
