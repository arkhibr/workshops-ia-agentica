# Exercícios

Tente responder antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Situação compartilhada

Os exercícios desta página se referem à regra de desconto da Vetor, a plataforma fictícia de e-commerce B2B usada no workshop, no estado em que a oficina desta sessão a deixou. A regra é a mesma nas duas trilhas.

Um pedido recebe desconto por faixa de valor: nenhum até R$ 500,00, 5% acima disso até R$ 2.000,00, 10% acima disso até R$ 5.000,00, e 15% acima de R$ 5.000,00. Sobre qualquer faixa incide um teto de R$ 1.000,00 de desconto por pedido. Cliente do tipo atacado com mais de 5 pedidos aprovados recebe um adicional de 5 pontos percentuais, somado à faixa normal, e o teto continua valendo sobre a soma.

**Na trilha técnica**, essa regra está implementada em `calcularDesconto(valorTotal, tipoCliente, pedidosAprovados)`, no projeto `oficina-especificacao` montado na [Oficina de ferramentas](oficina-de-ferramentas.md), e os exercícios que pedem execução rodam contra ele.

**Na trilha de negócio**, a descrição acima é tudo o que os exercícios exigem, e a verificação é feita por retrotradução e por conferência de casos, como na [Oficina de negócio](oficina-de-negocio.md).

## Recordar

### 1. As quatro etapas do ciclo

Nomeie as quatro etapas do ciclo de especificação, na ordem.

<details>
<summary>Ver resposta</summary>

Explorar, perguntar, propor, especificar.
</details>

### 2. As três categorias

Complete: uma regra de negócio existiria mesmo sem o sistema. Um requisito ______ descreve o que o sistema precisa fazer. Um requisito ______ descreve o critério de qualidade sob o qual ele faz isso.

<details>
<summary>Ver resposta</summary>

Funcional (FR). Não funcional (NFR).
</details>

## Compreender

### 3. RAS ou requisito local?

"O relatório de vendas mostra valores com duas casas decimais" e "o cálculo de desconto responde em menos de 100ms sob pico de 500 pedidos simultâneos" são dois requisitos não funcionais. Qual dos dois é um requisito arquiteturalmente significativo (RAS), e qual dos quatro critérios da página [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md#requisito-arquiteturalmente-significativo-ras) o torna significativo?

<details>
<summary>Ver resposta</summary>

O segundo. Ele atravessa mais de um componente (a função de cálculo e quem a chama sob carga), protege um atributo de qualidade prioritário (desempenho no checkout) e pode forçar decisão estrutural (cache, concorrência). O primeiro fica contido numa função de formatação, sem nenhum desses efeitos.
</details>

### 4. Regra disfarçada de requisito funcional

Um colega escreve: "o sistema deve aplicar desconto de 20% para atacado acima de R$ 10.000,00, respeitando o teto de R$ 1.000,00." Explique por que essa frase é um antipadrão, mesmo estando correta.

<details>
<summary>Ver resposta</summary>

Ela mistura três regras de negócio (a existência da faixa, o valor de corte, a prevalência do teto) dentro de um requisito funcional, sem que nenhuma tenha linha própria. Se o valor de corte mudar, alguém precisa reabrir o requisito funcional inteiro para encontrar o número, em vez de mudar uma regra numerada.
</details>

### 5. Especificação verificável ou não

"O sistema deve calcular o desconto de forma justa para todos os clientes." Essa frase é uma especificação executável? Justifique pelo [critério de verificabilidade](especificacao-executavel.md#o-criterio-de-verificabilidade).

<details>
<summary>Ver resposta</summary>

Não. Não existe caso de teste que prove ou refute "justa", porque não há valor de entrada nem saída esperada. Falta o que a página chama de caso concreto e, se houver faixa ou teto, o caso de fronteira.
</details>

## Aplicar

### 6. Exercício-âncora: especifique, implemente, verifique

**Trilha:** técnica. Quem está na trilha de negócio faz o exercício 6N, logo abaixo, com o mesmo pedido e verificação por retrotradução.

**O que é:** o mesmo ciclo do Experimento A da oficina, aplicado a um pedido novo, sem o apoio das respostas dadas. Desta vez você conduz o ciclo inteiro sozinho.

**Antes de começar: por que a ordem importa.** As respostas de quem pediu ficam num bloco recolhível, revelado só depois do passo 1. Abrir antes apaga a distância entre o que você perguntaria sozinho e o que a resposta revela, e essa distância é o que este exercício mede.

**Situação**

A Vetor recebeu este pedido:

> "Quero um desconto de lançamento pra atrair cliente novo: primeiro pedido dele, se for baixinho, ganha um desconto a mais."

**Seu papel**

Você é responsável por transformar esse pedido numa especificação que o agente implemente sem inventar nenhum dos números.

**Insumos disponíveis**

O projeto `oficina-especificacao` no estado deixado pela oficina, e o agente que você já usa. Se você não fez a oficina, a descrição da situação compartilhada acima é suficiente para responder por escrito.

**Como conduzir**

**Passo 1 — perguntas.** Escreva de três a cinco perguntas que exporiam a ambiguidade do pedido acima, sem abrir o bloco de respostas.

**Passo 2 — respostas.** Abra o bloco e compare.

??? note "Respostas de quem pediu — abra só depois do passo 1"
    - O que conta como "primeiro pedido"? Cliente com `pedidosAprovados` igual a zero, e vale para cliente padrão e atacado, sem distinção de tipo.
    - O que conta como "baixinho"? Valor do pedido menor que R$ 1.000,00. Pedidos grandes de cliente novo não se qualificam.
    - Quanto é o desconto a mais? 3 pontos percentuais, somados à faixa normal.
    - O teto de R$ 1.000,00 continua valendo? Sim, sempre.

**Passo 3 — especifique.** Escreva a regra de negócio (BR) e o requisito funcional (FR), no mesmo formato do [Exemplo arquitetural](exemplo-arquitetural.md).

**Passo 4 — implemente e verifique.** Peça ao agente a implementação a partir da sua especificação, e rode os quatro casos abaixo com `node --test`.

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 800,00 | padrão | 0 | R$ 64,00 (5% + 3% = 8%) |
| 2 | R$ 1.500,00 | padrão | 0 | R$ 75,00 (5%, sem bônus, valor não é "baixinho") |
| 3 | R$ 800,00 | atacado | 0 | R$ 64,00 (o bônus não distingue tipo de cliente) |
| 4 | R$ 400,00 | padrão | 3 | R$ 0,00 (faixa de 0%, sem bônus, não é primeiro pedido) |

**Entrega esperada**

As perguntas do passo 1, a especificação do passo 3, e o resultado de `node --test` do passo 4, incluindo os seis testes originais e os quatro casos novos.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Perguntas antes da resposta | 20% | As perguntas do passo 1 foram escritas e preservadas antes de abrir o bloco de respostas |
| Especificação no padrão BR/FR | 40% | A regra de negócio e o requisito funcional estão separados, com valores concretos, não uma frase genérica |
| Verificação real executada | 40% | Executou `node --test` contra os quatro casos novos e os seis originais, relatando o resultado |

**Como verificar antes de entregar:** confira se o caso 2 (valor grande, sem bônus) e o caso 4 (não é primeiro pedido, sem bônus) foram mesmo testados. São os dois casos que provam que o bônus tem fronteira, em vez de nunca se aplicar.

### 6N. Exercício-âncora: especifique e retrotraduza

**Trilha:** negócio. Quem está na trilha técnica faz o exercício 6, acima, com o mesmo pedido e verificação por execução de teste.

**O que é:** o mesmo ciclo do Experimento A-N da [Oficina de negócio](oficina-de-negocio.md), aplicado a um pedido novo, sem o apoio das respostas dadas. Desta vez você conduz o ciclo inteiro sozinho, sem terminal e sem execução de teste.

**Antes de começar: por que a ordem importa.** As respostas de quem pediu ficam num bloco recolhível, revelado só depois do passo 1. Abrir antes apaga a distância entre o que você perguntaria sozinho e o que a resposta revela, e essa distância é o que este exercício mede.

**Situação**

A Vetor, plataforma fictícia de e-commerce B2B usada nesta sessão, recebeu este pedido:

> "Quero um desconto de lançamento pra atrair cliente novo: primeiro pedido dele, se for baixinho, ganha um desconto a mais."

**Seu papel**

Você é responsável por transformar esse pedido numa especificação que o time implemente sem inventar nenhum dos números.

**Insumos disponíveis**

A regra de desconto descrita na situação compartilhada do topo desta página, e o agente que você já usa, em interface de chat.

**Como conduzir**

**Passo 1 — perguntas.** Escreva de três a cinco perguntas que exporiam a ambiguidade do pedido acima, sem abrir o bloco de respostas.

**Passo 2 — respostas.** Abra o bloco e compare.

??? note "Respostas de quem pediu — abra só depois do passo 1"
    - O que conta como "primeiro pedido"? Cliente sem nenhum pedido aprovado, e vale para cliente padrão e atacado, sem distinção de tipo.
    - O que conta como "baixinho"? Valor do pedido menor que R$ 1.000,00. Pedidos grandes de cliente novo não se qualificam.
    - Quanto é o desconto a mais? 3 pontos percentuais, somados à faixa normal.
    - O teto de R$ 1.000,00 continua valendo? Sim, sempre.

**Passo 3 — especifique.** Escreva a regra de negócio e o requisito funcional, separados, no mesmo formato do [Exemplo arquitetural](exemplo-arquitetural.md).

**Passo 4 — retrotraduza.** Abra uma conversa nova, sem histórico. Cole apenas a regra e o requisito que você escreveu, sem o pedido original e sem as respostas do passo 2, e peça a descrição em prosa do comportamento que eles produzem, sem sugestão de melhoria. Compare com a intenção que você tinha ao escrever, e registre toda diferença encontrada.

**Passo 5 — confira os quatro casos.** Preencha a coluna de desconto esperado à mão, usando apenas a regra em vigor e a sua especificação. Depois peça o mesmo cálculo ao agente, a partir da sua especificação, e compare linha a linha.

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 800,00 | padrão | 0 | |
| 2 | R$ 1.500,00 | padrão | 0 | |
| 3 | R$ 800,00 | atacado | 0 | |
| 4 | R$ 400,00 | padrão | 3 | |

??? note "Gabarito — abra só depois de preencher a tabela à mão"
    1. R$ 64,00. Faixa de 5% somada aos 3 pontos percentuais do bônus, o que dá 8%.
    2. R$ 75,00. Faixa de 5% sem bônus, porque R$ 1.500,00 não é considerado valor baixo.
    3. R$ 64,00. O bônus não distingue tipo de cliente, e o resultado é igual ao do caso 1.
    4. R$ 0,00. Faixa de 0% e sem bônus, porque não é o primeiro pedido do cliente.

**Entrega esperada**

As perguntas do passo 1, a especificação do passo 3, a prosa devolvida no passo 4 com a divergência registrada, e a tabela do passo 5 preenchida à mão com a comparação contra o agente.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Perguntas antes da resposta | 20% | As perguntas do passo 1 foram escritas e preservadas antes de abrir o bloco de respostas |
| Especificação no padrão BR/FR | 40% | A regra de negócio e o requisito funcional estão separados, com valores concretos, não uma frase genérica |
| Retrotradução executada e divergência registrada | 40% | A conversa nova foi efetivamente conduzida, e o resultado traz a divergência encontrada ou a afirmação explícita de que não houve nenhuma |

**Como verificar antes de entregar:** confira se o caso 2, de valor grande, e o caso 4, que não é primeiro pedido, foram mesmo conferidos. São os dois casos que provam que o bônus tem fronteira, em vez de nunca se aplicar.

## Analisar

### 7. Comparando as duas especificações

Compare a especificação que você escreveu no exercício-âncora da sua trilha com a do experimento de desconto de cliente recorrente da oficina que você fez: o [Experimento A](oficina-de-ferramentas.md#experimento-a) na trilha técnica, o [Experimento A-N](oficina-de-negocio.md#experimento-a-n) na trilha de negócio. As duas regras têm a mesma forma de composição com a faixa normal, que é a soma de pontos percentuais, e o mesmo comportamento diante do teto? Aponte uma diferença estrutural entre elas, além dos números.

### 8. O que a entrevista socrática expôs

Releia o dossiê do [Experimento C](oficina-de-entrevista.md#experimento-c). Escolha a afirmação que o registro de proveniência classificou como `[PRESSUPOSTO]` e que teria o maior impacto se estivesse errada. Esse pressuposto seria visível numa revisão manual rápida da especificação original, ou só apareceu porque alguém foi obrigado a responder uma pergunta específica sobre ele? O que isso diz sobre a diferença entre revisar uma especificação e ser entrevistado sobre ela?

## Avaliar

### 9. O incidente do pedido acumulado

Releia o [Estudo de caso](estudo-de-caso.md). Em até 100 palavras, defenda uma posição: toda especificação de regra de negócio envolvendo limite de valor deveria, por padrão, incluir a pergunta "por pedido ou por período acumulado?" Ou isso sobrecarregaria especificações que nunca precisariam dessa distinção? Justifique com um critério, não com preferência pessoal.

## Criar

### 10. Especifique a regra que falta

A Vetor quer que clientes atacado com mais de 5 pedidos aprovados **e** que sejam também o primeiro pedido do mês corrente recebam os dois bônus somados (o de cliente recorrente e o de lançamento), mas só até um limite de 25 pontos percentuais totais, mesmo que a soma das faixas ultrapasse isso. Escreva a especificação completa (BR e FR), incluindo pelo menos um caso de teste que force a comparação entre o limite de 25 pontos percentuais e o teto de R$ 1.000,00, os dois numa mesma composição.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
