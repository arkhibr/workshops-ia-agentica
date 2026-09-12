# Perguntas que revelam ambiguidade

Nem toda pergunta vale o mesmo. Perguntar "o que você quer?" devolve a mesma frase vaga que já foi dita. Um repertório pequeno de perguntas, feitas na ordem certa, expõe a regra de negócio que ninguém tinha percebido que precisava dizer.

## Cinco perguntas que quase sempre valem a pena

**Quando isso vale, e quando deixa de valer?** Toda regra tem fronteira, mesmo que quem pediu não tenha pensado nela. "Ative o desconto de atacado" não diz a partir de que valor a faixa começa — e é exatamente aí que mora a regra que falta.

**O que acontece no valor exato da fronteira?** Se a faixa começa "acima de R$ 10.000,00", o pedido de R$ 10.000,00 exato entra ou fica de fora? Essa pergunta sozinha evita a classe de erro mais comum em regra de faixa: o limite contado do lado errado.

**Existe uma regra que já vale para casos parecidos, e essa precisa segui-la ou é exceção?** Um sistema de desconto por faixa costuma ter um teto por pedido que vale para as faixas já existentes. Um pedido para "ativar uma faixa nova" raramente diz se esse teto continua valendo para ela ou se a faixa nova é uma exceção — as duas leituras são plausíveis, e só quem pediu sabe qual é a certa.

**O que o sistema faz quando a entrada não é nenhum dos casos previstos?** Cliente sem tipo definido, valor negativo, valor zero — a resposta "isso nunca vai acontecer" costuma estar errada, e "o sistema aceita qualquer coisa" é uma decisão, não a ausência de uma.

**Quem vai revisar isso antes de aceitar como pronto, e o que essa pessoa vai olhar?** Essa pergunta não é sobre o sistema, é sobre o processo — e frequentemente revela que ninguém tinha pensado em critério de aceitação nenhum, só em "parece que funciona".

!!! question "Antes de continuar"
    Escolha uma das cinco perguntas acima e aplique ao próprio pedido "ative o desconto de atacado". A resposta muda o código que um agente geraria?

## Por que perguntar é mais barato que descobrir depois

Cada uma dessas perguntas custa uma frase e alguns segundos de quem já sabe a resposta. Descobrir a mesma informação depois de o código estar escrito custa uma investigação: alguém precisa notar que o comportamento está errado, reproduzir o caso, e só então voltar à pergunta que deveria ter sido feita antes. A [Sessão 9](../sessao-09-depuracao-sistematica/index.md) trata desse protocolo de investigação em profundidade — a régua desta sessão é simples: toda pergunta que evita uma investigação futura vale o tempo de ser feita agora.

## O antipadrão da pergunta que não muda nada

Nem toda pergunta é boa pergunta. "Você tem certeza que quer isso?" não revela ambiguidade nenhuma — só transfere a decisão de volta para quem já tinha decidido, sem acrescentar informação nova. O teste de uma boa pergunta de elicitação é objetivo: a resposta, seja qual for, muda alguma linha do código que o agente vai gerar? Se as duas respostas possíveis produzem exatamente o mesmo comportamento, a pergunta era decorativa, e o tempo gasto nela poderia ter ido para uma das cinco categorias acima.

!!! tip "Aplique agora"
    Pense na próxima vez que alguém do seu time fizer um pedido vago de mudança. Antes de abrir o agente, escreva as perguntas que você faria — não as respostas, só as perguntas — e veja quantas delas caem numa das cinco categorias acima.

## Isso vira código assim

A segunda pergunta da lista ("o que acontece no valor exato da fronteira?") parece teórica até se olhar o código de faixa por valor:

```javascript
if (valorTotal > 5000) {
  percentual = 0.15;
} else if (valorTotal > 2000) {
  percentual = 0.1;
} else if (valorTotal > 500) {
  percentual = 0.05;
}
```

Cada `>` foi uma resposta a essa pergunta, já dada: R$ 500,00 exato fica na faixa de baixo, sem desconto, porque o teste que acompanha a função confirma isso, não a leitura do código:

```javascript
it('nao da desconto ate 500,00', () => {
  assert.equal(calcularDesconto(500, 'padrao'), 0);
});
```

Se a resposta certa fosse "R$ 500,00 exato já entra na faixa de 5%", o código teria `>=` em vez de `>`, e o teste acima teria que mudar para esperar `25`, não `0` — uma diferença de um caractere no operador, que só a pergunta feita antes evita descobrir depois, com um cliente reclamando de um desconto que faltou por um centavo de diferença.

Quando a fronteira nunca foi perguntada, o agente escolhe `>` ou `>=` pela convenção mais comum na linguagem, não pela regra de negócio real — e as duas opções compilam, passam em qualquer teste que não cubra exatamente o valor de corte, e divergem silenciosamente da intenção de quem pediu.

**Próxima página:** [O método da entrevista socrática](entrevista-socratica.md).
