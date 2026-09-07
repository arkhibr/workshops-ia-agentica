# O ciclo de especificação

Entre o pedido vago e o código, existe um trabalho que a maioria dos times pula: transformar "ative o desconto de atacado" numa descrição que não deixa nada para o agente inventar sozinho. Quatro etapas fazem esse trabalho, e pular qualquer uma delas custa mais caro depois do que custaria antes.

## Explorar, perguntar, propor, especificar

Um pedido chega quase sempre incompleto, não porque quem pediu foi descuidado, mas porque a cabeça de quem pediu já resolveu metade do problema sem perceber que resolveu. "Ative o desconto de atacado" pressupõe uma faixa de valor, um teto, uma data de início — tudo isso existe na cabeça de quem escreveu a frase, e nada disso está na frase.

O ciclo tem quatro etapas, nessa ordem:

- **Explorar.** Antes de perguntar qualquer coisa, olhe o que já existe: código, teste, documentação, conversa anterior. Um parâmetro que a função já recebe e nunca usa, um campo que o banco já guarda e a tela não mostra — isso é pista de intenção não implementada, não um requisito em si.
- **Perguntar.** Levante as perguntas cuja resposta muda o comportamento do sistema. A página seguinte trata só disso.
- **Propor.** Depois de reunir as respostas, escreva uma proposta curta — três ou quatro frases — e devolva para quem pediu, antes de especificar tudo em detalhe. É o ponto mais barato para descobrir que a proposta pegou o problema errado.
- **Especificar.** Só agora, com a proposta validada, escreva a especificação completa: regra de negócio (BR), requisito funcional (FR) e requisito não funcional (NFR), no padrão da próxima página.

!!! question "Antes de continuar"
    Pense no último pedido que você recebeu e resolveu sem perguntar nada. Quantas das quatro etapas você pulou, e qual delas, se tivesse acontecido, teria mudado o resultado?

## Por que pular direto para o código custa mais caro depois

[Boehm](../referencia/bibliografia.md#boehm-software-engineering-economics-1981) documentou, décadas antes de qualquer LLM, que o custo de corrigir uma ambiguidade cresce a cada fase do desenvolvimento — já visto na Sessão 1 a propósito da escolha entre vibe coding, assistência e SDD. O ciclo de especificação aplica a mesma lógica dentro de uma única tarefa: a etapa de explorar e perguntar é a fase mais barata para corrigir uma ambiguidade, porque ainda não existe código escrito que dependa dela. Pular para a implementação empurra o mesmo custo para depois, quando corrigir significa reescrever, não só reler.

A pressa de "só implementar logo" tem uma armadilha específica com agentes de codificação: o agente não vai parar para perguntar, a menos que seja instruído a fazer isso. Ele completa a lacuna com a suposição mais provável estatisticamente, não com a suposição certa para aquele negócio. O resultado compila, passa nos testes que já existiam, e resolve um problema ligeiramente diferente do que foi pedido — o mesmo padrão que a Sessão 1 chamou de piso alto e teto baixo.

## Quando o ciclo compensa e quando é exagero

Nem todo pedido precisa das quatro etapas por extenso. Um ajuste de uma linha, reversível, sem regra de negócio nova, resolve-se explorando e perguntando de cabeça, sem formalizar proposta nem especificação: o mesmo critério de [reversibilidade e tempo de vida](../sessao-01-o-que-mudou/modos-de-trabalho.md#quando-cada-modo-se-justifica) da Sessão 1 decide isso. O ciclo completo se paga quando a regra de negócio é nova, quando mais de uma pessoa vai manter o código depois, ou quando o pedido já revelou, na primeira leitura, mais de uma interpretação possível — como "ative o desconto de atacado", que não diz onde a faixa começa nem se o teto de R$ 1.000,00 continua valendo.

!!! tip "Aplique agora"
    Pegue um pedido real que está no seu backlog. Você consegue nomear pelo menos uma pergunta cuja resposta mudaria o código gerado? Se não conseguir nenhuma, o ciclo completo é exagero para esse caso — assistência de codificação direta já resolve.

**Próxima página:** [BR, FR e NFR](br-fr-nfr.md).
