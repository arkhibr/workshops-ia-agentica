# Intervenção socrática e divergência do pensamento

Um pedido vago ("ative o desconto de atacado") aceita, quase sempre, a primeira leitura que vem à cabeça de quem o recebe primeiro. Essa leitura converge cedo demais: fecha a interpretação antes de examinar se ela é a única plausível, e o efeito só aparece depois, quando o sistema faz exatamente o que foi pedido e ainda assim resolve o problema errado. Esta página trata do mecanismo que mantém mais de uma leitura viva por mais tempo antes de fechar numa só: o ciclo de especificação e a intervenção socrática que o sustenta.

## O ciclo: explorar, perguntar, propor, especificar

A cabeça de quem pediu já resolveu metade do problema sem perceber que resolveu. "Ative o desconto de atacado" pressupõe uma faixa de valor, um teto, uma data de início, e nada disso está escrito na frase. Um ciclo de quatro etapas externaliza essa resolução antes que um agente a externalize errado:

- **Explorar.** Antes da primeira pergunta, examine o que já existe: código, teste, documentação, conversa anterior. Um parâmetro que a função já recebe e nunca usa é pista de intenção não implementada, e ainda não vale como requisito.
- **Perguntar.** Levante as perguntas cuja resposta muda o comportamento do sistema. A seção seguinte trata só disso.
- **Propor.** Depois de reunir as respostas, escreva uma proposta curta, de três ou quatro frases, e devolva para quem pediu antes de especificar tudo em detalhe. É o ponto mais barato para descobrir que a proposta pegou o problema errado.
- **Especificar.** Só agora, com a proposta validada, escreva a especificação completa, no padrão que a página de decomposição de requisitos desta sessão detalha.

[Boehm](../referencia/bibliografia.md#boehm-software-engineering-economics-1981) documentou que o custo de corrigir uma ambiguidade cresce a cada fase do desenvolvimento, décadas antes de qualquer agente de codificação existir. A etapa de explorar e perguntar é a mais barata para corrigir uma ambiguidade, porque ainda não existe código escrito que dependa dela, e pular direto para a implementação empurra o mesmo custo para a fase em que corrigir já significa reescrever. Um agente de codificação não para para perguntar, a menos que seja instruído a isso: completa a lacuna com a suposição estatisticamente mais provável, que para aquele negócio costuma ser a errada.

!!! question "Antes de continuar"
    Pense no último pedido que você recebeu e resolveu sem perguntar nada. Quantas das quatro etapas você pulou, e qual delas, se tivesse acontecido, teria mudado o resultado?

## Perguntas que revelam ambiguidade

Nem toda pergunta rende o mesmo, e perguntar "o que você quer?" devolve a mesma frase vaga que já foi dita. Cinco perguntas quase sempre valem a pena, porque cada uma ataca uma classe de ambiguidade que um pedido vago costuma esconder:

- **Quando isso vale, e quando deixa de valer?** Toda regra tem fronteira, mesmo que quem pediu não tenha pensado nela.
- **O que acontece no valor exato da fronteira?** Se a faixa começa "acima de R$ 10.000,00", o pedido de exatamente R$ 10.000,00 entra ou fica de fora? Essa pergunta sozinha evita a classe de erro mais comum em regra de faixa: o limite contado do lado errado.
- **Existe uma regra que já vale para casos parecidos, e essa precisa segui-la ou é exceção?**
- **O que o sistema faz quando a entrada não é nenhum dos casos previstos?** Cliente sem tipo definido, valor negativo, valor zero. "Isso nunca vai acontecer" costuma estar errado, e "o sistema aceita qualquer coisa" já é uma decisão tomada por omissão.
- **Quem vai revisar isso antes de aceitar como pronto, e o que essa pessoa vai olhar?**

Nem toda pergunta é boa pergunta, e o teste é objetivo: a resposta, seja qual for, muda alguma linha do que vai ser entregue? "Você tem certeza que quer isso?" não revela ambiguidade nenhuma, só transfere a decisão de volta para quem já tinha decidido. Se as duas respostas possíveis produzem exatamente o mesmo comportamento, a pergunta era decorativa.

## Convergência prematura e o papel da intervenção socrática

Uma lista de perguntas escritas de uma vez só, a partir apenas do pedido original, tem um limite: a quinta pergunta da lista não conhece a resposta da terceira. Quem escreve todas as perguntas de antemão converge sozinho para o que julga relevante, e a convergência acontece antes de qualquer resposta real ter chegado. A **intervenção socrática** é o mecanismo que atrasa esse fechamento: uma pergunta de cada vez, com a pergunta seguinte escolhida em função da resposta anterior, mantendo mais de uma leitura do pedido viva por mais tempo do que uma lista fixa permitiria.

Isso vale em particular quando quem entrevista é um agente de linguagem. Um modelo tende a ser prestativo: recebe uma especificação ruim e oferece a versão corrigida, porque parece ajudar. O resultado é uma especificação melhor escrita e um analista que continua sem saber por que a original estava errada, e o mesmo defeito reaparece na funcionalidade seguinte, porque a causa dele nunca foi tratada.

## Uma pergunta por mensagem, cinco fases, seis categorias

O contrato de conduta da intervenção socrática tem três partes. **Uma pergunta por mensagem**: uma única interrogação, sempre, mesmo que duas perguntas curtas pareçam relacionadas. **Sem sugerir a resposta**: a pergunta não vem acompanhada da opção que quem pergunta acha certa. **Solução fica para depois**: pedido de solução técnica no meio da entrevista vira anotação, e a conversa continua na pergunta pendente.

A conversa avança por cinco fases, cada uma com critério de saída observável: **enquadramento** (o entrevistado aceita a regra de uma pergunta por vez), **exploração** (o problema é reenunciado sem nenhum adjetivo vago), **aprofundamento** (cada afirmação-chave tem evidência citada ou virou pressuposto pendente), **ampliação** (ao menos uma perspectiva contrária e um cenário de falha examinados) e **síntese** (as três perguntas canônicas — o que estamos construindo, para quem, e qual o critério de sucesso testável — têm resposta precisa).

Dentro de cada fase, a pergunta percorre seis categorias, em vez de se repetir na primeira: esclarecimento, pressupostos, evidências, implicações, perspectivas alternativas e meta-pensamento. Há uma regra automática ligada ao esclarecimento: adjetivo vago detectado (rápido, flexível, robusto, escalável, intuitivo, seguro, simples, moderno) força a próxima pergunta a ser de quantificação, convertendo o adjetivo em número, comportamento observável ou exemplo concreto.

## Registro de proveniência e o dossiê

Nem toda afirmação numa entrevista tem o mesmo peso, e o método classifica cada uma pela proveniência: `[FATO]` (confirmado por fonte identificável), `[EVIDÊNCIA]`, `[PRESSUPOSTO]` (hipótese ainda não validada), `[DECISÃO]` (com o nome de quem decidiu), `[RESTRIÇÃO]`, `[RISCO]`, `[ABERTA]` (com dono) e `[CONFLITO]`. A regra que mais protege a especificação: opinião de stakeholder nunca é `[FATO]` automaticamente. "Os gerentes usam isso todo dia", dito pelo próprio gerente, é pressuposto até alguém olhar o registro de acesso.

A entrevista termina num dossiê: as três canônicas respondidas, o registro de proveniência completo, os termos quantificados com o antes e o depois, os riscos examinados, as perspectivas consideradas, e as perguntas que ficaram abertas com o nome de quem deve respondê-las. Uma entrevista sem dossiê produz entendimento na cabeça de quem participou e nada para quem não estava lá.

## Pensamento socrático e pensamento crítico

[Paul e Elder](../referencia/bibliografia.md#paul-e-elder-the-thinkers-guide-to-socratic-questioning-2019) tratam o questionamento socrático como a forma disciplinada de pensamento crítico aplicada em diálogo, não como técnica de retórica: uma pergunta bem colocada expõe a estrutura lógica de um pensamento — o que ele pressupõe, que evidência sustenta, que implicação segue — em vez de aceitar a primeira formulação como definitiva. As seis categorias de pergunta usadas nesta sessão vêm diretamente da classificação que os autores propõem para o questionamento socrático, e o argumento deles é o mesmo que abre esta página: perguntar bem adia o fechamento numa única leitura, mantendo viva, por mais tempo, mais de uma interpretação possível.

Pensamento crítico, nessa tradição, não é ceticismo genérico nem contestação por hábito. É a disciplina de examinar uma afirmação pelos padrões que a sustentam — clareza, precisão, relevância, profundidade, amplitude, lógica — antes de aceitá-la ou rejeitá-la. A intervenção socrática é o pensamento crítico aplicado à elicitação de requisitos: em vez de avaliar uma especificação já escrita, ela produz a especificação através do próprio processo de questionamento, o que expõe pressupostos antes que eles virem código.

!!! tip "Aplique agora"
    Pegue a última especificação que você recebeu de alguém. Ela responde as três canônicas — o que estamos construindo, para quem, e qual o critério de sucesso testável — com precisão suficiente para você distinguir o caso em que foi cumprida do caso em que não foi?

**Próxima página:** [Exemplo de aplicação de IA](intervencao-socratica-exemplo-de-aplicacao-de-ia.md).
