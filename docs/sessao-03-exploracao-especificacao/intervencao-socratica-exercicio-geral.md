# Exercício de IA — Geral: sendo entrevistado por um agente

**Para quem não escreve código.** Este exercício não usa terminal, repositório nem execução de teste. Tudo o que ele pede acontece numa conversa com o agente, em interface de chat, exatamente como no exemplo de aplicação de IA desta sessão, mas sobre um pedido novo, que você conduz sozinho.

## O pedido

A Vetor, plataforma fictícia de e-commerce B2B usada nesta sessão, recebeu este pedido de um gerente de logística:

> "Quero que o sistema avise o time de logística quando um pedido atacado ficar parado demais. A gente perde cliente quando isso acontece e ninguém percebe a tempo."

Antes de continuar, registre por escrito quantos defeitos você enxerga sozinho, numa leitura só. Esse número é a sua linha de base.

## Passo 1 — instale o entrevistador

Abra uma conversa nova com o agente que você já usa e cole o [prompt de intervenção socrática](intervencao-socratica-exemplo-de-aplicacao-de-ia.md#o-prompt-de-intervencao-socratica) do exemplo desta sessão. O agente deve responder com a fase de enquadramento e uma única pergunta.

## Passo 2 — entregue o pedido e responda

Cole o pedido do gerente de logística e responda cada pergunta como se você fosse quem o escreveu. Improvise quando não souber, do mesmo jeito que um stakeholder real improvisaria, mantendo coerência entre as respostas.

## Passo 3 — conte as interrogações

A cada mensagem do agente, confira se veio uma única interrogação. Anote quantas mensagens, se alguma, violaram o contrato de uma pergunta por vez.

## Passo 4 — force um adjetivo vago

Em alguma resposta, use de propósito uma das palavras da regra do adjetivo vago: diga que o aviso precisa ser "rápido" ou que a tela de acompanhamento tem que ser "simples". A próxima pergunta do agente deveria ser de quantificação. Anote se foi.

## Passo 5 — feche e leia o dossiê

Depois de pelo menos seis respostas, escreva "fechar entrevista". Leia o dossiê e confira três coisas: as três canônicas estão respondidas de forma testável, o registro de proveniência tem pelo menos um `[PRESSUPOSTO]`, e alguma pergunta ficou aberta com dono.

## Passo 6 — compare com a sua linha de base

Quantos defeitos você havia registrado por escrito antes de começar? Quantos o dossiê registrou? A diferença é o que a entrevista comprou, e vale registrar especificamente qual informação do dossiê não estava na frase original nem podia ser deduzida dela por releitura.

**Questões exploratórias:**

- O agente tentou corrigir o pedido em algum momento, em vez de perguntar? O que na conversa provocou isso?
- Qual pergunta foi mais desconfortável de responder, e o que esse desconforto revela sobre o que o pedido original escondia?
- "Parado demais" e "a gente perde cliente" são dois adjetivos vagos disfarçados de fato. Alguma das perguntas do agente separou os dois, tratando um como critério de tempo e o outro como consequência de negócio a ser evitada?

## Evidência a entregar

Três itens, verificáveis pela conversa que você conduziu: a contagem de mensagens que violaram o contrato de uma única interrogação, o dossiê completo com registro de proveniência e perguntas abertas com dono, e a comparação entre a sua linha de base e o que o dossiê registrou.

**Próxima página:** [Exercício de IA — Especialista](intervencao-socratica-exercicio-especialista.md).
