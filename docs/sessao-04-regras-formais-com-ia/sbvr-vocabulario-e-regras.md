# SBVR: vocabulário e regras

Antes de escrever uma regra sem ambiguidade, o time precisa concordar no que os termos da regra significam. SBVR separa essas duas coisas, vocabulário e regra, e distingue dois tipos de regra que se confundem na prosa comum.

## O que o SBVR é

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é uma especificação da OMG, a mesma organização por trás do DMN visto adiante nesta sessão, para representar vocabulário de negócio e regras de forma que uma máquina e uma pessoa leiam a mesma coisa. Ele não é uma linguagem de programação: é um jeito de dizer "estes são os termos que usamos, e estas são as regras que valem sobre eles" de forma estruturada.

Um vocabulário SBVR nomeia os **termos** do domínio ("Pedido", "Cliente", "Faixa de Desconto") e os **fatos** que os relacionam ("um Pedido tem um Valor Total", "um Cliente tem um Tipo"). Só depois de o vocabulário existir é que uma regra pode ser escrita sem ambiguidade — "o desconto do pedido" só é uma frase precisa se "pedido" e "desconto" já são termos definidos, não palavras do dia a dia.

## Regra estrutural e regra operativa

O SBVR distingue duas categorias de regra, e a diferença entre elas é a mesma que separa definição de comportamento:

**Regra estrutural** (ou definicional) diz como o negócio organiza seus próprios conceitos, usando operadores aléticos — "é necessário que", "é possível que". "É necessário que todo Pedido tenha exatamente um Cliente associado" é estrutural: define o que um Pedido *é*, não como alguém deve agir.

**Regra operativa** (ou comportamental) rege conduta, usando operadores deônticos: "é obrigatório que", "é permitido que". "É obrigatório que o desconto de um Pedido não ultrapasse o teto" é operativa: alguém, ou algum sistema, pode violá-la — e é exatamente essa possibilidade de violação que a torna operativa, não estrutural.

| | Regra estrutural | Regra operativa |
|---|---|---|
| Operador | Alético ("necessário", "possível") | Deôntico ("obrigatório", "permitido") |
| O que define | Como os conceitos do negócio se relacionam | Como alguém deve se comportar |
| Pode ser violada? | Não — é definição | Sim — é conduta |
| Exemplo genérico | Todo Pedido tem exatamente um Cliente | O desconto nunca ultrapassa o teto |

!!! question "Antes de continuar"
    Pegue uma regra da Sessão 3 (a de cliente recorrente ou a de lançamento). Ela é estrutural ou operativa? O teste: alguém pode violá-la, ou ela só descreve como o mundo do negócio é organizado?

## Por que isso importa antes de formalizar

Confundir as duas categorias produz uma tabela de decisão mal desenhada, tema da página seguinte. Regra estrutural não entra numa tabela de decisão — ela é verdade sobre o domínio, não uma condição a avaliar. Só a regra operativa, a que rege conduta e pode ser violada, é candidata a virar linha de tabela, porque só ela tem um "se isso, então aquilo" que faz sentido avaliar caso a caso.

O vocabulário também previne um erro comum na especificação BR/FR da Sessão 3: escrever "cliente" numa frase e "Cliente" (com tipo, com atributos) noutra, sem que as duas se refiram à mesma coisa. Um vocabulário SBVR, mesmo informal (uma lista curta de termos e o que cada um significa), resolve isso antes de a regra ser escrita.

!!! tip "Aplique agora"
    Escreva o vocabulário mínimo de uma regra de desconto por faixa de valor: liste os termos (Pedido, Cliente, Valor Total, Tipo de Cliente, Desconto, Teto) e, para cada um, uma frase que diga o que ele é. Se dois termos parecerem a mesma coisa com nomes diferentes, é aí que a ambiguidade mora.

**Próxima página:** [RuleSpeak: três formas de sentença](rulespeak-tres-formas.md).
