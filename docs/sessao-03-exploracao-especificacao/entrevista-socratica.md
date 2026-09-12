# O método da entrevista socrática

A página anterior trouxe o repertório: quais perguntas quase sempre valem a pena. Esta trata do resto do problema, que é como conduzir a conversa. O mesmo conjunto de perguntas, despejado de uma vez num formulário, produz respostas rasas. Feito uma pergunta por vez, com a seguinte escolhida em função da anterior, expõe o que ninguém tinha percebido que precisava dizer.

## A regra que sustenta o método

O entrevistador socrático **só pergunta**. Quem formula requisitos, pressupostos e conclusões é o entrevistado. O valor da entrevista está no que o analista descobre ao ser obrigado a explicitar o que estava implícito, e responder por ele destrói exatamente esse valor.

Isso vale em especial quando o entrevistador é um agente. Um modelo de linguagem tende a ser prestativo: recebe uma especificação ruim e oferece a versão corrigida, porque é o que parece ajudar. O resultado é uma especificação melhor escrita e um analista que continua sem saber por que ela estava errada. Na próxima funcionalidade, o mesmo defeito volta.

O contrato de conduta tem três partes, e a primeira é a que mais se viola:

1. **Uma pergunta por mensagem.** Uma única interrogação, sempre. Duas perguntas curtas e relacionadas continuam sendo duas, e sub-pergunta entre parênteses conta.
2. **Sem sugerir a resposta.** A pergunta não vem acompanhada da opção que o entrevistador acha certa. Quando o entrevistado trava, o recurso é oferecer duas a quatro alternativas de múltipla escolha, não apontar a preferida.
3. **Solução fica para depois.** Pedido de solução técnica no meio da entrevista vira anotação, e a conversa continua na pergunta pendente.

## As quatro fases

Cada fase tem um objetivo e um critério de saída observável. Pular fases é o que transforma a entrevista em transcrição.

| Fase | Objetivo | Sai quando |
|---|---|---|
| Enquadramento | acordar tema, quem responde e critério de encerramento, e explicar o formato | o entrevistado aceita a regra de uma pergunta por vez |
| Exploração | esclarecer problema, termos e público | você consegue reenunciar o problema sem nenhum adjetivo vago |
| Aprofundamento | expor pressupostos e pedir evidências | cada afirmação-chave tem evidência citada ou virou pressuposto pendente |
| Ampliação | perspectivas alternativas e cenários de falha | ao menos uma perspectiva contrária e um cenário de falha examinados |
| Síntese | o entrevistado formula as conclusões, o entrevistador só espelha | as três perguntas canônicas têm resposta precisa |

As **três perguntas canônicas** são o critério de encerramento, e nenhuma entrevista termina sem resposta precisa para as três: o que estamos construindo, para quem, e qual o critério de sucesso testável.

A terceira é a que mais falha. "O time comercial vai gostar" não é critério de sucesso, porque não existe teste que distinga o caso em que foi atingido do caso em que não foi.

!!! question "Antes de continuar"
    Pegue o último pedido de funcionalidade que você recebeu. Você consegue responder as três canônicas sobre ele agora, sem consultar ninguém?

## Seis categorias de pergunta

Uma entrevista que só usa a primeira categoria é formulário, não diálogo. O método pede que o entrevistador percorra as seis:

1. **Esclarecimento.** "O que 'flexível' significa aqui, em comportamento observável?"
2. **Pressupostos.** "O que precisa ser verdade sobre o gestor para essa tela fazer sentido?"
3. **Evidências.** "Que evidência temos de que os gestores pedem isso: chamados, planilhas paralelas, alguém pediu?"
4. **Implicações.** "Se essa premissa de volume estiver errada, o que acontece com a funcionalidade?"
5. **Perspectivas alternativas.** "Como o vendedor da ponta descreveria esse mesmo problema?"
6. **Meta-pensamento.** "Das respostas até aqui, qual te surpreendeu?"

Há uma regra automática ligada à primeira categoria. **Adjetivo vago detectado, próxima pergunta é de quantificação.** Rápido, flexível, robusto, escalável, intuitivo, seguro, simples e moderno são gatilhos: a resposta precisa virar número, comportamento observável ou exemplo concreto antes que a conversa siga.

## Escolher a próxima pergunta

Dentro de uma fase, a próxima pergunta não é a próxima da lista. É a que ataca a incerteza com maior combinação de quatro fatores: impacto se a resposta mudar, incerteza atual, quanto ela bloqueia outras decisões, e custo de descobrir tarde. Em caso de empate, prefira a mais próxima do problema e do resultado, antes de qualquer detalhe de solução.

A cada quatro respostas substantivas, ou ao trocar de fase, o entrevistador troca o espelhamento por uma **síntese curta** que separa três colunas: o que está confirmado, o que é suposto, e onde há conflito. A síntese termina com a única pergunta daquela mensagem, que pode ser o pedido de confirmação do entendimento.

## O ledger epistemológico

Nem toda afirmação numa entrevista tem o mesmo peso, e tratar todas como fato é como o pressuposto de alguém vira requisito do sistema. O método classifica cada afirmação relevante pela proveniência:

| Marca | Significado |
|---|---|
| `[FATO]` | confirmado por fonte identificável |
| `[EVIDÊNCIA]` | dado, métrica ou incidente que sustenta uma afirmação |
| `[PRESSUPOSTO]` | hipótese ainda não validada |
| `[DECISÃO]` | escolha de quem tem autoridade, com o nome de quem decidiu |
| `[RESTRIÇÃO]` | limite obrigatório de negócio, prazo, tecnologia ou regulação |
| `[RISCO]` | incerteza com consequência relevante |
| `[ABERTA]` | questão sem resposta, com dono |
| `[CONFLITO]` | afirmações incompatíveis aguardando decisão |

A regra que mais protege a especificação: **opinião de stakeholder nunca vira `[FATO]` automaticamente**. Sem fonte identificável, é `[PRESSUPOSTO]`, por mais confiante que a pessoa esteja. "Os gerentes usam isso todo dia" dito pelo gerente comercial é pressuposto até alguém olhar o registro de acesso.

!!! tip "Aplique agora"
    Classifique com as marcas acima as três últimas afirmações que você ouviu sobre um requisito em andamento. Se todas viraram `[FATO]`, releia o critério: quantas têm fonte identificável?

## O dossiê, e por que a entrevista precisa de saída escrita

Uma entrevista que termina sem documento produz entendimento na cabeça de quem participou e nada para quem não estava lá. O dossiê registra contexto, as três canônicas, o ledger completo, os termos que foram quantificados (com o antes e o depois), os riscos examinados, as perspectivas consideradas e as perguntas que ficaram abertas com o nome de quem deve respondê-las.

As perguntas abertas são a parte mais subestimada. Uma entrevista honesta quase sempre termina com questões que o entrevistado não tinha autoridade para decidir, e registrá-las com dono é o que impede que a especificação seguinte as resolva por omissão.

**Próxima página:** [Especificação executável](especificacao-executavel.md).
