# Intervenção socrática e divergência do pensamento

Quem recebe um pedido vago ("ative o desconto de atacado") tende a adotar a primeira leitura que lhe ocorre. Essa convergência prematura fecha a interpretação antes de examinar se ela é a única plausível, e o efeito só aparece quando o sistema já faz o que foi pedido e resolve um problema diferente do que quem pediu tinha em mente. Esta página trata do ciclo de especificação e da intervenção socrática, que mantêm mais de uma leitura em consideração até que as respostas de quem pediu permitam escolher uma.

## Ciclo de especificação em quatro etapas

Quem pediu já tomou parte das decisões sem registrá-las. "Ative o desconto de atacado" pressupõe uma faixa de valor, um teto e uma data de início, e nenhuma dessas informações está escrita na frase. O ciclo de quatro etapas abaixo registra essas decisões por escrito antes que um agente as preencha com suposições próprias:

- **Explorar.** Antes da primeira pergunta, examine o que já existe: código, teste, documentação, conversa anterior. Um parâmetro que a função já recebe e nunca usa é pista de intenção não implementada, e ainda não vale como requisito.
- **Perguntar.** Levante as perguntas cuja resposta muda o comportamento do sistema. A seção seguinte trata só disso.
- **Propor.** Depois de reunir as respostas, escreva uma proposta curta, de três ou quatro frases, e devolva para quem pediu antes de especificar tudo em detalhe. Nesse ponto, corrigir uma proposta que entendeu mal o problema custa menos do que em qualquer etapa posterior.
- **Especificar.** Só agora, com a proposta validada, escreva a especificação completa, no padrão que a página de decomposição de requisitos desta sessão detalha.

[Boehm](../referencia/bibliografia.md#boehm-software-engineering-economics-1981) documentou que o custo de corrigir uma ambiguidade cresce a cada fase do desenvolvimento, décadas antes de qualquer agente de codificação existir. A etapa de explorar e perguntar é a mais barata para corrigir uma ambiguidade, porque ainda não existe código escrito que dependa dela, e pular direto para a implementação transfere a correção para a fase em que ela exige reescrever código. Um agente de codificação só para para perguntar quando é instruído a isso. Sem essa instrução, ele completa a lacuna com a suposição estatisticamente mais provável, que pode não corresponder à regra daquele negócio.

!!! question "Antes de continuar"
    No último pedido que você recebeu e resolveu sem perguntar nada, quantas das quatro etapas você pulou, e qual delas teria mudado o resultado se tivesse acontecido?

## Perguntas que revelam ambiguidade

Nem toda pergunta rende o mesmo, e perguntar "o que você quer?" devolve a mesma frase vaga que já foi dita. Cinco perguntas quase sempre valem a pena, porque cada uma trata uma classe de ambiguidade que um pedido vago costuma esconder:

- **Quando isso vale, e quando deixa de valer?** Toda regra tem fronteira, mesmo que quem pediu não tenha pensado nela.
- **O que acontece no valor exato da fronteira?** Se a faixa começa "acima de R$ 10.000,00", o pedido de exatamente R$ 10.000,00 entra ou fica de fora? Essa pergunta sozinha evita a classe de erro mais comum em regra de faixa: o limite contado do lado errado.
- **Existe uma regra que já vale para casos parecidos, e essa precisa segui-la ou é exceção?**
- **O que o sistema faz quando a entrada não é nenhum dos casos previstos?** Cliente sem tipo definido, valor negativo, valor zero. "Isso nunca vai acontecer" costuma estar errado, e "o sistema aceita qualquer coisa" já é uma decisão tomada por omissão.
- **Quem vai revisar isso antes de aceitar como pronto, e o que essa pessoa vai olhar?**

Nem toda pergunta é boa pergunta, e o teste é objetivo: a resposta, seja qual for, muda alguma linha do que vai ser entregue? "Você tem certeza que quer isso?" não revela ambiguidade nenhuma, só transfere a decisão de volta para quem já tinha decidido. Se as respostas possíveis produzem exatamente o mesmo comportamento, a pergunta não acrescenta informação à especificação.

## Convergência prematura e o papel da intervenção socrática

Uma lista de perguntas escritas de uma vez só, a partir apenas do pedido original, tem um limite: a quinta pergunta da lista não conhece a resposta da terceira. Quem escreve todas as perguntas de antemão converge sozinho para o que julga relevante, e a convergência acontece antes de qualquer resposta real ter chegado. A **intervenção socrática** é o mecanismo que atrasa esse fechamento: uma pergunta de cada vez, com a pergunta seguinte escolhida em função da resposta anterior, o que mantém mais de uma leitura do pedido em consideração por mais tempo do que uma lista fixa permitiria.

Isso vale em particular quando quem entrevista é um agente de linguagem. Um modelo tende a ser prestativo: recebe uma especificação ruim e oferece a versão corrigida, porque parece ajudar. O resultado é uma especificação melhor escrita e um analista que continua sem saber por que a original estava errada, e o mesmo defeito reaparece na funcionalidade seguinte, porque a causa dele nunca foi tratada.

## Regras de conduta e estrutura da entrevista socrática

O contrato de conduta da intervenção socrática tem três partes. **Uma pergunta por mensagem**: uma única interrogação, sempre, mesmo que duas perguntas curtas pareçam relacionadas. **Sem sugerir a resposta**: a pergunta não vem acompanhada da opção que quem pergunta acha certa. **Solução fica para depois**: pedido de solução técnica no meio da entrevista é registrado como anotação, e a conversa continua na pergunta pendente.

A conversa avança por cinco fases, cada uma com critério de saída observável: **enquadramento** (o entrevistado aceita a regra de uma pergunta por vez), **exploração** (o problema é reenunciado sem nenhum adjetivo vago), **aprofundamento** (cada afirmação-chave tem evidência citada ou está registrada como pressuposto pendente), **ampliação** (ao menos uma perspectiva contrária e um cenário de falha examinados) e **síntese** (as três perguntas canônicas — o que estamos construindo, para quem, e qual o critério de sucesso testável — têm resposta precisa).

Dentro de cada fase, as perguntas percorrem seis categorias: esclarecimento, pressupostos, evidências, implicações, perspectivas alternativas e meta-pensamento. Há uma regra automática ligada ao esclarecimento: adjetivo vago detectado (rápido, flexível, robusto, escalável, intuitivo, seguro, simples, moderno) força a próxima pergunta a ser de quantificação, convertendo o adjetivo em número, comportamento observável ou exemplo concreto.

## Registro de proveniência e o dossiê

Nem toda afirmação numa entrevista tem o mesmo peso, e o método classifica cada uma pela proveniência: `[FATO]` (confirmado por fonte identificável), `[EVIDÊNCIA]`, `[PRESSUPOSTO]` (hipótese ainda não validada), `[DECISÃO]` (com o nome de quem decidiu), `[RESTRIÇÃO]`, `[RISCO]`, `[ABERTA]` (com dono) e `[CONFLITO]`. A regra que mais protege a especificação: opinião de stakeholder nunca é `[FATO]` automaticamente. "Os gerentes usam isso todo dia", dito pelo próprio gerente, é pressuposto até alguém olhar o registro de acesso.

A entrevista termina num dossiê: as três canônicas respondidas, o registro de proveniência completo, os termos quantificados com o antes e o depois, os riscos examinados, as perspectivas consideradas, e as perguntas que ficaram abertas com o nome de quem deve respondê-las. Sem o dossiê, quem não participou da entrevista não tem registro das decisões tomadas nem das perguntas que ficaram abertas.

## Pensamento socrático e pensamento crítico

[Paul e Elder](../referencia/bibliografia.md#paul-e-elder-the-thinkers-guide-to-socratic-questioning-2019) tratam o questionamento socrático como a forma disciplinada de pensamento crítico aplicada em diálogo. Uma pergunta bem colocada expõe a estrutura lógica de um pensamento, isto é, o que ele pressupõe, que evidência o sustenta e que implicação decorre dele, antes que a primeira formulação seja aceita como definitiva. As seis categorias de pergunta usadas nesta sessão vêm diretamente da classificação que os autores propõem para o questionamento socrático, e o argumento deles é o mesmo que abre esta página: a pergunta bem formulada adia a escolha de uma única leitura e mantém mais de uma interpretação em consideração por mais tempo.

Nessa tradição, pensamento crítico é a disciplina de examinar uma afirmação pelos padrões intelectuais que a sustentam, como clareza, precisão, relevância, profundidade, amplitude e lógica, antes de aceitá-la ou rejeitá-la. A intervenção socrática aplica essa disciplina à elicitação de requisitos e produz a especificação por meio do próprio questionamento, o que expõe os pressupostos antes que eles sejam implementados em código.

!!! tip "Aplique agora"
    Pegue a última especificação que você recebeu de alguém. Ela responde as três canônicas — o que estamos construindo, para quem, e qual o critério de sucesso testável — com precisão suficiente para você distinguir o caso em que foi cumprida do caso em que não foi?

**Próxima página:** [Exemplo de aplicação de IA](intervencao-socratica-exemplo-de-aplicacao-de-ia.md).
