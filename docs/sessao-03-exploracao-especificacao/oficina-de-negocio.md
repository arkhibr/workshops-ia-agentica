# Oficina de negócio

**Objetivo Bloom:** Aplicar.

**Esta é a oficina da trilha de negócio.** Ela não usa terminal, repositório nem execução de teste.
Tudo o que ela pede acontece numa conversa com o agente, em interface de chat. Quem implementa em
código faz a [Oficina de ferramentas](oficina-de-ferramentas.md), que parte do mesmo pedido e chega à
mesma especificação, com verificação por execução de teste em vez de retrotradução.

O trajeto vai de um pedido vago da Vetor, a plataforma fictícia de e-commerce B2B usada no workshop,
até uma especificação que descreve o comportamento sem deixar nenhum número por decidir.

## Ferramenta

Uma conversa nova com o agente que você já usa, em interface de chat. Tempo estimado: 15 minutos.

**Decisão em foco:** transformar um pedido vago numa especificação BR/FR verificável, e comprovar que
ela diz o que você quis dizer, antes que alguém a implemente.

## Regra de desconto em vigor

A Vetor calcula desconto por faixa de valor do pedido, com um teto por pedido. A regra em vigor é
esta, e é tudo o que você precisa saber para conduzir a oficina.

| Valor do pedido | Desconto |
|---|---|
| Até R$ 500,00 | Nenhum |
| Acima de R$ 500,00 até R$ 2.000,00 | 5% |
| Acima de R$ 2.000,00 até R$ 5.000,00 | 10% |
| Acima de R$ 5.000,00 | 15% |

Sobre qualquer faixa incide um teto de R$ 1.000,00 de desconto por pedido. O sistema registra o tipo
de cliente, que pode ser padrão ou atacado, e nenhuma regra em vigor usa essa informação.

## Experimento A-N

**Objetivo:** conduzir o ciclo explorar, perguntar, propor e especificar sobre um pedido novo, e
comprovar que a especificação escrita diz o que você quis dizer.

**Antes de começar: a ordem importa.** O bloco de respostas do passo 2 simula quem pediu a mudança.
Ele só cumpre a função de mostrar o efeito das perguntas se você escrever as suas antes de abri-lo.

**Passo 1 — o pedido.** É este, e nada além disso:

> "Dá pra dar um desconto extra pros clientes que compram muito com a gente?"

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de redigir a
especificação. Use o repertório de [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md)
como referência.

**Passo 2 — as respostas.** Abra o bloco e compare com as perguntas que você escreveu.

??? note "Respostas de quem pediu — abra só depois de escrever suas próprias perguntas"
    - O que conta como "compra muito"? Cliente do tipo atacado com mais de 5 pedidos aprovados nos últimos 12 meses.
    - Esse desconto extra é cumulativo com a faixa normal, ou substitui? Cumulativo: soma-se à faixa normal, em pontos percentuais.
    - O desconto extra é de quantos pontos percentuais? 5 pontos percentuais.
    - O teto de R$ 1.000,00 por pedido continua valendo com o desconto extra somado? Sim, sempre. Nenhuma regra nova revoga o teto.
    - Esse desconto vale para cliente padrão também? Não, só para atacado.

**Passo 3 — proponha e especifique.** Escreva a proposta em três frases, depois a especificação com a
regra de negócio e o requisito funcional separados, seguindo o formato de
[Exemplo arquitetural](exemplo-arquitetural.md). A regra de negócio declara o que vale no negócio, sem
mencionar tela nem sistema. O requisito funcional declara o que o sistema faz para cumpri-la.

**Passo 4 — retrotraduza.** Abra uma conversa nova, sem nenhum histórico desta sessão. Cole apenas a
regra e o requisito que você escreveu, sem o pedido original e sem as respostas do passo 2, e peça:
"descreva em prosa o comportamento que estas regras produzem, sem sugerir melhoria e sem corrigir
nada". Compare a descrição devolvida com a intenção que você tinha ao escrever. Toda diferença é
ambiguidade que sobreviveu à sua especificação.

**Passo 5 — confira os quatro casos.** Preencha a coluna de desconto esperado à mão, usando apenas a
regra em vigor e a especificação que você escreveu, antes de consultar o agente. Depois peça ao agente
o mesmo cálculo a partir da sua especificação, e compare linha a linha.

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 3.000,00 | atacado | 2 | |
| 2 | R$ 3.000,00 | atacado | 6 | |
| 3 | R$ 6.000,00 | atacado | 6 | |
| 4 | R$ 3.000,00 | padrão | 6 | |

??? note "Gabarito — abra só depois de preencher a tabela à mão"
    1. R$ 300,00. Faixa de 10%, e o cliente não atinge os 5 pedidos exigidos para o adicional.
    2. R$ 450,00. Faixa de 10% somada aos 5 pontos percentuais do adicional, o que dá 15%.
    3. R$ 1.000,00. Faixa de 15% somada ao adicional dá 20%, que seriam R$ 1.200,00, mas o teto prevalece.
    4. R$ 300,00. Faixa de 10%, e o adicional não vale para cliente padrão.

**Observe:** o caso 3 é o único em que a faixa normal, o adicional de recorrência e o teto se cruzam ao
mesmo tempo. Se a sua especificação não disser que o teto incide sobre a soma já feita dos dois
percentuais, ela deixa essa decisão para quem implementar.

**Questões exploratórias:**

- Alguma das suas perguntas do passo 1 não apareceu entre as respostas do passo 2? O que você teria
  feito sem essa resposta?
- A retrotradução do passo 4 descreveu o comportamento que você tinha em mente, ou revelou uma leitura
  que você não tinha previsto? Qual frase da sua especificação permitiu a leitura divergente?
- Se você tivesse encaminhado o pedido original direto para o time, sem o ciclo completo, qual das
  cinco respostas do passo 2 alguém teria decidido sozinho?

## Extensão do cenário de qualidade

Para quem terminar antes. A Vetor pede que o cálculo de desconto "continue rápido mesmo com muito
tráfego". Escreva o cenário de qualidade completo, com os seis campos de
[Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md), e acrescente as duas declarações que
transformam a medida em acordo: quem é avisado quando ela deixa de ser cumprida, e o que acontece a
partir desse aviso.

## Evidência a entregar

Quatro itens, verificáveis pela conversa que você conduziu:

1. As perguntas do passo 1, escritas antes de abrir as respostas.
2. A especificação do passo 3, com a regra de negócio e o requisito funcional separados.
3. A prosa devolvida pela retrotradução do passo 4, e a divergência que você encontrou, ou a
   afirmação explícita de que não houve divergência.
4. A tabela do passo 5 preenchida à mão, com a comparação contra a resposta do agente.

**Próxima página:** [Oficina de entrevista socrática](oficina-de-entrevista.md).
