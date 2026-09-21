# Especificação executável

Uma especificação pode estar tecnicamente completa e ainda assim não permitir nenhuma conferência, porque não há como determinar, examinando o código gerado, se ele a cumpriu. O critério desta página separa especificação que um agente consegue seguir sem interpretar de resumo do pedido reescrito com letras maiúsculas.

## O critério de verificabilidade

Uma especificação executável responde, para cada requisito, a mesma pergunta: existe um teste, um caso concreto, que prova se este requisito foi atendido ou não? "O sistema deve calcular o desconto corretamente" não passa nesse critério. "Correto" não tem caso de teste, é uma opinião disfarçada de requisito. "Para um pedido de R$ 12.000,00 de um cliente atacado, o desconto é R$ 1.000,00" passa: existe um valor de entrada e um valor de saída esperado, verificável por qualquer pessoa, inclusive por um agente que nunca viu a regra antes.

O [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit) formaliza esse critério na prática: cada requisito funcional do `spec.md` recebe um identificador (`FR-001`, `FR-002`) e uma frase no padrão "o sistema deve...", e a especificação só é aceita como pronta quando todo requisito tem essa forma verificável. [Delimarsky](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025), no post de lançamento do Spec Kit, chama a especificação de "contrato para como seu código deve se comportar". O termo contrato indica que o cumprimento pode ser verificado por qualquer das partes, com base no texto e sem consulta a quem o escreveu.

## Estrutura mínima de uma especificação executável

Três elementos, para cada requisito:

- **A regra ou o requisito em si**, na forma declarativa (BR) ou funcional (FR) da página anterior.
- **Pelo menos um caso concreto** que ilustra a regra em ação: um valor de entrada e o resultado esperado, não uma descrição do comportamento em abstrato.
- **O caso de fronteira**, sempre que a regra tiver faixa, teto ou condição, porque é nesse ponto que as duas leituras possíveis divergem, como um teto de desconto ou uma faixa de valor por volume costumam revelar.

Uma especificação sem exemplo concreto deixa a interpretação do valor de fronteira para quem lê depois. E "quem lê depois", quando o pedido vai para um agente, é o próprio agente, decidindo sozinho.

Para um requisito não funcional, o "caso concreto" é o [cenário de qualidade completo](atributos-de-qualidade-e-ras.md#cenario-de-qualidade), com fonte, estímulo, ambiente, artefato, resposta e medida, em vez de um par entrada/saída simples. Um NFR sem esses seis elementos tem o mesmo problema de um FR sem caso concreto: parece uma especificação, mas não dá para saber se foi cumprido.

!!! question "Antes de continuar"
    Pegue a última especificação que você escreveu. Para o requisito mais importante dela, existe um valor de entrada e um valor de saída esperado escritos, ou só uma descrição do comportamento?

## Especificação sem informação nova

O sintoma é fácil de reconhecer: a especificação tem a mesma quantidade de informação que o pedido original, só que organizada em tópicos e com títulos em negrito. "Ative o desconto de atacado" é reescrito como "**Requisito:** ativar o desconto de atacado", sem nenhum valor concreto, sem faixa, sem teto, sem caso de fronteira. O trabalho de explorar e perguntar da primeira página desta sessão não aconteceu, e o texto recebeu apenas a formatação de uma especificação.

O teste rápido para detectar esse antipadrão: dê a especificação para alguém que nunca ouviu falar do domínio e pergunte se essa pessoa consegue escrever os casos de teste sem fazer nenhuma pergunta adicional. Se a resposta for não, a especificação ainda não é executável, porque a informação que faltava no pedido original continua faltando.

!!! tip "Aplique agora"
    Escreva, em três linhas, a especificação executável para um pedido vago do seu próprio backlog (ou, na falta de um, "adicione um limite de tentativas de login"): a regra, um caso concreto e o caso de fronteira. Compare com o que a oficina da sua trilha vai pedir: a [Oficina de ferramentas](oficina-de-ferramentas.md) para quem implementa em código, e a [Oficina de negócio](oficina-de-negocio.md) para quem conduz o mesmo ciclo sem escrever código.

## Para o time de negócio

Fora do código, a especificação executável assume a forma do critério de aceitação do item de backlog,
e ele só está pronto quando alguém consegue conferir o resultado sem perguntar nada a quem o escreveu. O critério
mínimo tem os mesmos três elementos desta página, escritos em linguagem de negócio.

A regra vem primeiro, numerada, na forma que valeria mesmo sem sistema. Depois vem pelo menos um caso
concreto, com um valor de entrada e o resultado esperado. Por último vem o caso de fronteira, que é o
valor exatamente no limite da faixa, onde as duas leituras possíveis divergem.

| Elemento | Escrito assim |
|---|---|
| Regra | Pedido entre R$ 2.000,01 e R$ 5.000,00 recebe 10% de desconto |
| Caso concreto | Pedido de R$ 3.000,00 de cliente padrão recebe R$ 300,00 de desconto |
| Caso de fronteira | Pedido de R$ 2.000,00 exatos recebe R$ 100,00, pela faixa de 5%, e não R$ 300,00 |

Um critério de aceitação sem o caso de fronteira transfere a decisão para quem implementa, e essa
transferência acontece sem que ninguém perceba, porque o item parece completo. Quem estiver
implementando vai escolher entre incluir ou excluir o valor de corte, e as duas escolhas produzem
código que funciona e passa em qualquer conferência que não teste justamente esse valor.

O antipadrão mais comum é o item de backlog que repete o pedido original com formatação melhor. Se a
descrição tem a mesma quantidade de informação da frase que você ouviu na reunião, com o acréscimo de
títulos em negrito, o trabalho de perguntar não aconteceu. A conferência rápida é entregar o item a
alguém que desconhece o assunto e perguntar se essa pessoa consegue listar os casos de conferência sem
fazer nenhuma pergunta.

## Para o time de desenvolvimento

"FR-03: calcularDesconto aplica 10% na faixa de R$ 2.000,01 a R$ 5.000,00" já é um requisito funcional, mas ainda não é executável, porque falta o caso concreto e o caso de fronteira. A versão executável tem os três elementos desta página:

```text
FR-03: calcularDesconto aplica 10% na faixa de R$ 2.000,01 a R$ 5.000,00.
  Caso concreto: valorTotal = 3000, tipoCliente = 'padrao' → desconto = 300.
  Caso de fronteira: valorTotal = 2000 (limite de baixo, exclusivo) → desconto = 100 (faixa de 5%, não 10%).
```

Cada linha da especificação executável corresponde, sem reinterpretação, a uma linha do arquivo de teste, na correspondência de um para um que caracteriza uma especificação verificável:

```javascript
// test/desconto.test.js
it('da 10% na faixa de 2.000,01 a 5.000,00', () => {
  assert.equal(calcularDesconto(3000, 'padrao'), 300);       // caso concreto de FR-03
});

it('nao da 10% em 2.000,00 exato', () => {
  assert.equal(calcularDesconto(2000, 'padrao'), 100);        // caso de fronteira de FR-03
});
```

Se a especificação tivesse ficado só em "FR-03: calcularDesconto aplica 10% na faixa de R$ 2.000,01 a R$ 5.000,00", sem os dois casos, um agente gerando o teste teria que inventar os valores de entrada sozinho. E inventar o valor de fronteira é, estatisticamente, o ponto em que ele mais erra, porque não há informação na frase que diga se R$ 2.000,00 exato entra ou fica de fora.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
