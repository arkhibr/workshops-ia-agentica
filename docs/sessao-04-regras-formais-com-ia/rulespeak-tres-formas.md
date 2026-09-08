# RuleSpeak: três formas de sentença

SBVR diz que uma regra existe; [RuleSpeak](../referencia/bibliografia.md#ross-rulespeak) diz como escrevê-la sem que ninguém precise adivinhar a intenção. Três formas de sentença cobrem praticamente toda regra operativa que aparece num sistema de negócio.

## As três formas que valem como regra

[Ross](../referencia/bibliografia.md#ross-rulespeak), no documento normativo do RuleSpeak (escrito originalmente em inglês, com as palavras-chave "must", "must not" e "may ... only"), organiza a notação em torno de três palavras-chave fixas. Este material usa o equivalente em português, mantendo o efeito preciso de cada uma sobre o que a regra permite:

**"Deve" — algo é exigido.** "O desconto de um Pedido **deve** respeitar o teto de R$ 1.000,00." Não há exceção implícita: se a regra usa "deve", toda instância do caso precisa cumpri-la.

**"Não deve" — algo é proibido.** "Um Pedido de cliente atacado **não deve** receber a faixa de 20% se o valor for R$ 10.000,00 ou menos." A proibição também não tem exceção implícita: se existir exceção, ela precisa virar outra regra, explícita.

**"Pode ... somente se" — algo é permitido, só sob condição.** "Um Pedido **pode** receber o desconto de cliente recorrente **somente se** `pedidosAprovados` for maior que 5." Diferente das duas anteriores, esta forma nomeia a condição que abre a permissão: sem a condição, a permissão não existe.

Essas três formas, e só elas, contam como regra de negócio no vocabulário do RuleSpeak. Duas outras formas existem no documento normativo ("pode" isolado, sem condição, e "não precisa"), mas o próprio Ross as separa como orientação (*statement of advice*): sugestão, não regra que alguém pode violar formalmente.

| Forma | Efeito | Exemplo genérico |
|---|---|---|
| deve | Exigência sem exceção | O desconto de um Pedido **deve** respeitar o teto fixo em reais |
| não deve | Proibição sem exceção | Um Pedido de valor abaixo do mínimo **não deve** receber a faixa de desconto por volume |
| pode ... somente se | Permissão condicional | Um Pedido **pode** receber o adicional de recorrência **somente se** o histórico do Cliente atender à condição |

!!! question "Antes de continuar"
    Pegue a regra de lançamento da Sessão 3 ("primeiro pedido, se for baixinho, ganha desconto a mais"). Reescreva-a usando "pode ... somente se": qual é a condição exata que abre a permissão?

## Por que a forma certa evita ambiguidade

A escolha entre "deve", "não deve" e "pode ... somente se" não é estilística: cada uma responde a uma pergunta diferente sobre o que acontece quando a condição não se aplica. "Deve" sem condição implícita força quem escreve a regra a admitir, por escrito, se existe exceção. "Pode ... somente se" torna a condição parte da regra, não um detalhe deixado para a implementação decidir: é a diferença entre "o sistema permite desconto de recorrência" (vago, permite quando?) e "o sistema permite desconto de recorrência **somente se** houver mais de 5 pedidos aprovados" (a condição está na frase).

Um efeito prático: regra escrita em RuleSpeak vira caso de teste quase sem tradução. "Não deve" sugere um teste que prova a proibição, um caso que tentaria violar e deveria falhar; "pode ... somente se" sugere dois testes, um dentro da condição e um fora dela, exatamente os casos de fronteira que a Sessão 3 tratou como o ponto mais caro de esquecer.

## Numeração, evidência e confiança

Uma regra solta, sem número, se perde entre a especificação e o código: ninguém consegue apontar, seis meses depois, se ela ainda está implementada, se mudou, ou se nunca existiu de fato. Três disciplinas resolvem isso, e valem tanto para regra operativa quanto para as regras de classificação e derivação da página anterior:

- **Numeração por tipo.** Regras operativas (exigência, proibição, permissão) recebem prefixo `RN` (regra de negócio comportamental); regras de classificação e derivação recebem `RD` (regra definitiva). `RN-001`, `RN-002`, `RD-001`: sequencial, sem reaproveitar número de regra removida.
- **Evidência obrigatória.** Toda regra formalizada a partir de código existente cita onde mora a evidência: arquivo, função, linha. Uma regra sem evidência não é regra confirmada, é hipótese sobre o que o sistema faz.
- **Confiança explícita.** 🟢 confirmada (o código ou o time confirma exatamente essa regra); 🟡 inferida (parece ser a regra, mas ninguém do domínio validou ainda); 🔴 lacuna (o domínio espera essa regra, mas não há evidência dela em lugar nenhum). A retrotradução da próxima página é exatamente a técnica que promove uma regra de 🟡 para 🟢, ou revela que ela precisa virar 🔴.

Formato de uma regra completa:

```text
RN-003: Um Pedido pode receber o adicional de recorrência somente se
        o Cliente tiver mais de 5 pedidos aprovados.
Evidência: src/desconto.js, função calcularDesconto, ainda não implementada
Confiança: 🔴 lacuna (regra existe na especificação da Sessão 3, sem código correspondente)
```

!!! question "Antes de continuar"
    De todas as regras que você já escreveu nesta sessão, quantas você marcaria 🟢, quantas 🟡 e quantas 🔴? Se a maioria for 🟡, o que falta para promovê-las?

## O antipadrão do "deveria"

"O sistema deveria dar desconto para cliente frequente" não é regra de negócio no vocabulário do RuleSpeak: "deveria" não é "deve", não é "não deve", não é "pode ... somente se". É uma sugestão sem compromisso, e cada pessoa que a lê decide sozinha se ela vale sempre, às vezes, ou nunca. O RuleSpeak não inventou uma forma para "deveria" de propósito: se uma regra de negócio existe de verdade, ela é exigência, proibição ou permissão condicional, não existe meio-termo declarativo. Quando alguém escreve "deveria", a régua é perguntar: isso é "deve", é "pode ... somente se", ou na verdade é só uma preferência que ainda não virou regra?

!!! tip "Aplique agora"
    Encontre, no seu próprio backlog ou numa conversa recente do time, uma frase com "deveria" sobre uma regra de negócio. Reescreva-a como "deve", "não deve" ou "pode ... somente se": o que a reescrita força você a decidir que a frase original deixava em aberto?

**Próxima página:** [Tabelas de decisão e DMN](tabelas-de-decisao-dmn.md).
