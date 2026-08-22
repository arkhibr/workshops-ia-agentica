# Exercício 4 — Exercício-âncora: intuição vs. prompt estruturado

**Duração:** 20 min · **Formato:** individual ou dupla

Este exercício resume a sessão: o mesmo problema, resolvido duas vezes pelo agente, com dois níveis de contexto diferentes. A diferença entre as duas saídas mede exatamente as duas primeiras setas da teoria — piso e teto.

## Passo 1 — Prompt intuitivo (5 min)

Sem abrir o [cenário.md](cenario.md) ainda, peça ao agente:

> Escreva uma função que calcula o desconto de um pedido baseado no valor total.

Rode na sua linguagem (C#, JavaScript ou TypeScript). Guarde a saída completa — vai precisar dela no Passo 3.

## Passo 2 — Prompt estruturado (10 min)

Agora abra o [cenário.md](cenario.md): ele contém a regra de negócio completa, incluindo duas exceções que um pedido vago dificilmente cobre. Reescreva o pedido ao agente incorporando a regra inteira — contexto de domínio, assinatura-alvo, faixas de desconto, teto de desconto, e a variação por tipo de cliente. Não copie o cenário literalmente para o agente; construa o prompt como se estivesse especificando para um colega que nunca viu essa regra.

Guarde a saída completa.

## Passo 3 — Verificar as duas saídas (5 min)

Abra [criterios-aceitacao.md](criterios-aceitacao.md) e rode os casos de teste contra as duas saídas — manualmente ou colando os valores de entrada. Marque quais casos cada versão passa.

## Fechamento da sessão

Compare o resultado com o que você registrou no Exercício 3. A pergunta que fecha a Sessão 1: quantos casos de teste o prompt intuitivo deixou passar batido — e qual desses casos só apareceu porque *você* conhecia a regra de negócio, não porque o agente adivinhou?

Essa mesma tensão — regra de negócio que a linguagem natural deixa ambígua — é o assunto central da Sessão 4 (Regras formais com IA).
