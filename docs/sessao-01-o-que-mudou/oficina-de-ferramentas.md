# Oficina de ferramentas — diagnóstico e contexto explícito

**Objetivo Bloom:** Compreender e Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Copilot, Cursor ou equivalente) e não exige nenhuma instalação nova. Tempo estimado: 30 minutos.

**Decisão em foco:** quando um pedido em linguagem natural precisa de contexto explícito para não perder regra de negócio, e quando o time está aceitando código sem entender o que ele faz.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A (autodiagnóstico) e Experimento B (contexto explícito), para sentir a diferença antes do exercício-âncora.
- **Exploração em dupla:** Experimento C, para nomear onde o julgamento humano entrou.

## Experimento A — autodiagnóstico

**Objetivo:** ter um retrato honesto do próprio uso de IA hoje, sem julgamento.

**Execute:** responda por escrito, individualmente:

1. Qual foi o último prompt que você escreveu para gerar ou alterar código de verdade? Reconstitua de memória.
2. Esse prompt tinha contexto (linguagem, formato esperado, regra de negócio, casos de borda) ou pedia só o resultado final?
3. Classifique seu uso de IA hoje: ad hoc, inconsistente, ou já tem rede de testes e revisão?
4. Da última vez que um código gerado por IA quebrou, você investigou sistematicamente ou foi tentativa e erro?

**Observe:** guarde as respostas. O Bloco 5 (exercícios) e a Sessão 9 (depuração sistemática) revisitam exatamente estas mesmas perguntas para medir o que mudou.

## Experimento B — contexto explícito

**Objetivo:** sentir, num caso com regras de negócio reais, o que "contexto explícito" muda antes de aplicar no exercício-âncora.

**Cenário:** validar se um cupom de desconto pode ser aplicado a um pedido de e-commerce. As quatro regras abaixo só devem ser usadas na parte 2 — leia a parte 1 e execute-a antes de olhar a lista de regras.

Regras:

- O cupom só vale dentro do prazo de validade (data de início e data de fim).
- O pedido precisa atingir o valor mínimo de R$ 150,00 para o cupom valer.
- Cada cliente só pode usar um cupom específico uma vez; um segundo uso do mesmo código é inválido.
- Cupom da categoria "frete grátis" não se acumula com cupom da categoria "percentual" no mesmo pedido.

**Execute — parte 1.** Peça ao agente, exatamente assim:

```text
Escreva uma função que valida se um cupom de desconto pode ser aplicado a um pedido.
```

**Execute — parte 2.** Peça de novo, agora com contexto:

```text
Escreva uma função validarCupom(cupom: Cupom, pedido: Pedido, cliente: Cliente): ResultadoValidacao
que decide se um cupom pode ser aplicado a um pedido, seguindo estas regras:

- O cupom só vale entre cupom.dataInicio e cupom.dataFim (inclusive).
- O valor total do pedido precisa ser de pelo menos R$ 150,00.
- Se cliente.cuponsJaUsados já contém o código do cupom, a validação falha.
- Se o pedido já tem um cupom de categoria "frete-gratis" aplicado e o novo
  cupom é da categoria "percentual" (ou vice-versa), a validação falha.

ResultadoValidacao deve indicar se o cupom é válido e, se não for, o motivo
específico da rejeição (não só um booleano).

Exemplos:
- Cupom "BEMVINDO10" com dataFim de ontem -> inválido, motivo: cupom expirado
- Pedido de R$ 90,00 com cupom que exige mínimo de R$ 150,00 -> inválido, motivo: valor mínimo não atingido
- Cliente com "BEMVINDO10" em cuponsJaUsados tentando usar "BEMVINDO10" de novo -> inválido, motivo: cupom já utilizado
- Pedido com cupom "FRETE-GRATIS" aplicado recebendo também "10OFF" (percentual) -> inválido, motivo: cupons não acumuláveis
```

**Compare:** a primeira saída validou alguma das quatro regras, ou só verificou se o cupom existe? A segunda tratou os quatro casos de exemplo corretamente, incluindo o motivo específico de rejeição? Alguma das duas inventou uma regra que você não pediu (por exemplo, um limite de uso diário que não existe no enunciado)?

**Questões exploratórias:**

- Qual das duas saídas você aceitaria em produção sem revisão adicional?
- O que fez a segunda saída ser melhor: o modelo, ou o pedido?
- A regra de não acumulação (frete grátis + percentual) foi a mais fácil de esquecer nas duas saídas? Por que essa costuma ser a regra que primeiro passa despercebida em revisão de código real?

Guarde as duas saídas: o Experimento C usa exatamente elas.

## Experimento C — onde entrou o julgamento

**Objetivo:** localizar, nas próprias saídas do Experimento B, onde cada seta de [Conceitos](conceitos.md#o-que-sobe-piso-teto-julgamento) apareceu.

**Execute:** em dupla, para cada seta, aponte um trecho concreto das duas saídas do Experimento B:

1. **Piso subiu para todos:** o que as duas saídas resolveram igualmente bem, sem esforço adicional?
2. **Teto subiu com disciplina:** o que só a segunda saída resolveu, e que exigiu saber de antemão quais regras de negócio existiam?
3. **Julgamento humano continuou necessário:** existe alguma decisão que nenhuma das duas saídas tomou sozinha?

**Questões exploratórias:**

- Qual foi a diferença mais cara que o prompt intuitivo deixou passar?
- Isso teria acontecido se o desenvolvedor não conhecesse a regra de negócio de antemão?

## Evidência a entregar

As respostas do Experimento A, as duas saídas do Experimento B e as três respostas do Experimento C. Sem essa evidência, o exercício-âncora da próxima página perde a comparação com um caso menor e mais simples.

**Próxima página:** [Exercícios](exercicios.md).
