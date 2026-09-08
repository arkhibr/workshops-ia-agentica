# RuleSpeak: três formas de sentença

SBVR diz que uma regra existe; [RuleSpeak](../referencia/bibliografia.md#ross-rulespeak) diz como escrevê-la em português ou inglês sem que ninguém precise adivinhar a intenção. Três formas de sentença cobrem praticamente toda regra operativa que aparece num sistema de negócio.

## As três formas que valem como regra

[Ross](../referencia/bibliografia.md#ross-rulespeak), no documento normativo do RuleSpeak, organiza a notação em torno de palavras-chave fixas, cada uma com um efeito preciso sobre o que a regra permite:

**"Must" — algo é exigido.** "O desconto de um Pedido **must** respeitar o teto de R$ 1.000,00." Não há exceção implícita: se a regra usa "must", toda instância do caso precisa cumpri-la.

**"Must not" — algo é proibido.** "Um Pedido de cliente atacado **must not** receber a faixa de 20% se o valor for R$ 10.000,00 ou menos." A proibição também não tem exceção implícita: se existir exceção, ela precisa virar outra regra, explícita.

**"May ... only" — algo é permitido, só sob condição.** "Um Pedido **may** receber o desconto de cliente recorrente **only if** `pedidosAprovados` for maior que 5." Diferente das duas anteriores, esta forma nomeia a condição que abre a permissão: sem a condição, a permissão não existe.

Essas três formas, e só elas, contam como regra de negócio no vocabulário do RuleSpeak. Duas outras formas existem no documento normativo ("may" isolado e "need not"), mas o próprio Ross as separa como *statements of advice*: orientação, não regra que alguém pode violar formalmente.

| Forma | Efeito | Exemplo genérico |
|---|---|---|
| must | Exigência sem exceção | O desconto de um Pedido **must** respeitar o teto fixo em reais |
| must not | Proibição sem exceção | Um Pedido de valor abaixo do mínimo **must not** receber a faixa de desconto por volume |
| may ... only | Permissão condicional | Um Pedido **may** receber o adicional de recorrência **only if** o histórico do Cliente atender à condição |

!!! question "Antes de continuar"
    Pegue a regra de lançamento da Sessão 3 ("primeiro pedido, se for baixinho, ganha desconto a mais"). Reescreva-a usando "may ... only" — qual é a condição exata que abre a permissão?

## Por que a forma certa evita ambiguidade

A escolha entre "must", "must not" e "may... only" não é estilística: cada uma responde a uma pergunta diferente sobre o que acontece quando a condição não se aplica. "Must" sem condição implícita força quem escreve a regra a admitir, por escrito, se existe exceção. "May ... only" torna a condição parte da regra, não um detalhe deixado para a implementação decidir — é a diferença entre "o sistema permite desconto de recorrência" (vago: permite quando?) e "o sistema permite desconto de recorrência **só se** houver mais de 5 pedidos aprovados" (a condição está na frase).

Um efeito prático: regra escrita em RuleSpeak vira caso de teste quase sem tradução. "Must not" sugere um teste que prova a proibição (um caso que tentaria violar e deveria falhar); "may ... only" sugere dois testes, um dentro da condição e um fora dela — exatamente os casos de fronteira que a Sessão 3 tratou como o ponto mais caro de esquecer.

## Numeração, evidência e confiança

Uma regra solta, sem número, se perde entre a especificação e o código: ninguém consegue apontar, seis meses depois, se ela ainda está implementada, se mudou, ou se nunca existiu de fato. Três disciplinas resolvem isso, e valem tanto para regra operativa quanto para as regras de classificação e derivação da página anterior:

- **Numeração por tipo.** Regras operativas (obrigação, proibição, permissão) recebem prefixo `RN` (regra de negócio comportamental); regras de classificação e derivação recebem `RD` (regra definitiva). `RN-001`, `RN-002`, `RD-001` — sequencial, sem reaproveitar número de regra removida.
- **Evidência obrigatória.** Toda regra formalizada a partir de código existente cita onde mora a evidência: arquivo, função, linha. Uma regra sem evidência não é regra confirmada, é hipótese sobre o que o sistema faz.
- **Confiança explícita.** 🟢 confirmada (o código ou o time confirma exatamente essa regra); 🟡 inferida (parece ser a regra, mas ninguém do domínio validou ainda); 🔴 lacuna (o domínio espera essa regra, mas não há evidência dela em lugar nenhum). A retrotradução da próxima página é exatamente a técnica que promove uma regra de 🟡 para 🟢, ou revela que ela precisa virar 🔴.

Formato de uma regra completa:

```text
RN-003: Um Pedido may receber o adicional de recorrência only if
        o Cliente tiver mais de 5 pedidos aprovados.
Evidência: src/desconto.js, função calcularDesconto, ainda não implementada
Confiança: 🔴 lacuna (regra existe na especificação da Sessão 3, sem código correspondente)
```

!!! question "Antes de continuar"
    De todas as regras que você já escreveu nesta sessão, quantas você marcaria 🟢, quantas 🟡 e quantas 🔴? Se a maioria for 🟡, o que falta para promovê-las?

## O antipadrão do "deveria"

"O sistema deveria dar desconto para cliente frequente" não é regra de negócio no vocabulário do RuleSpeak: "deveria" não é "must", não é "must not", não é "may ... only". É uma sugestão sem compromisso, e cada pessoa que a lê decide sozinha se ela vale sempre, às vezes, ou nunca. O RuleSpeak não inventou uma forma para "deveria" de propósito: se uma regra de negócio existe de verdade, ela é exigência, proibição ou permissão condicional — não existe meio-termo declarativo. Quando alguém escreve "deveria", a régua é perguntar: isso é "must", é "may ... only", ou na verdade é só uma preferência que ainda não virou regra?

!!! tip "Aplique agora"
    Encontre, no seu próprio backlog ou numa conversa recente do time, uma frase com "deveria" sobre uma regra de negócio. Reescreva-a como "must", "must not" ou "may ... only" — o que a reescrita força você a decidir que a frase original deixava em aberto?

**Próxima página:** [Tabelas de decisão e DMN](tabelas-de-decisao-dmn.md).
