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

**Objetivo:** sentir, num caso pequeno, o que "contexto explícito" muda antes de aplicar no exercício-âncora.

**Cenário:** uma função que formata um número de telefone brasileiro. Celular tem 9 dígitos, fixo tem 8, e um número inválido precisa de comportamento definido.

**Execute — parte 1.** Peça ao agente, exatamente assim:

```text
Escreva uma função que formata um número de telefone.
```

**Execute — parte 2.** Peça de novo, agora com contexto:

```text
Escreva uma função formatarTelefone(numero: string): string que recebe um
número de telefone brasileiro em dígitos (sem formatação) e devolve o
formato de exibição.

Regras:
- Celular (9 dígitos após o DDD): (DD) 9XXXX-XXXX
- Fixo (8 dígitos após o DDD): (DD) XXXX-XXXX
- Se o número não tiver 10 ou 11 dígitos, lance uma exceção
  NumeroInvalidoException com a mensagem "Número de telefone inválido".

Exemplos:
- "11987654321" -> "(11) 98765-4321"
- "1132654321" -> "(11) 3265-4321"
- "123" -> lança exceção
```

**Compare:** a primeira saída tratou o caso de número inválido? Distinguiu celular de fixo? A segunda seguiu exatamente a assinatura e as regras pedidas? Alguma das duas inventou uma regra que você não pediu?

**Questões exploratórias:**

- Qual das duas saídas você aceitaria em produção sem revisão adicional?
- O que fez a segunda saída ser melhor: o modelo, ou o pedido?

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
