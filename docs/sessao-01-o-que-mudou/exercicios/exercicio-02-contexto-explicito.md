# Exercício 2 — Contexto explícito

**Duração:** 15 min · **Formato:** individual ou dupla, com o agente configurado no Bloco 0 (ou o de sua preferência)

## Cenário

Uma função que formata um número de telefone brasileiro para exibição. Simples o bastante para caber nos 15 minutos, real o bastante para esconder decisões de negócio que um pedido vago não menciona: celular tem 9 dígitos, fixo tem 8, o DDD pode vir junto ou separado, e um número inválido precisa de um comportamento definido — não pode simplesmente quebrar.

## Passo 1 — Prompt intuitivo (5 min)

Peça ao agente, exatamente assim, sem adicionar nada:

> Escreva uma função que formata um número de telefone.

Rode em C#, JavaScript ou TypeScript — o seu stack do dia a dia. Guarde a saída completa (código gerado).

## Passo 2 — Prompt com contexto explícito (5 min)

Peça de novo, para a mesma função, agora com contexto:

> Escreva uma função `formatarTelefone(numero: string): string` [ou o equivalente na sua linguagem] que recebe um número de telefone brasileiro em dígitos (sem formatação) e devolve o formato de exibição.
>
> Regras:
> - Celular (9 dígitos após o DDD): `(DD) 9XXXX-XXXX`
> - Fixo (8 dígitos após o DDD): `(DD) XXXX-XXXX`
> - Se o número não tiver 10 ou 11 dígitos no total, lance uma exceção `NumeroInvalidoException` (ou o equivalente na sua linguagem) com a mensagem `"Número de telefone inválido"`.
>
> Exemplos:
> - `"11987654321"` → `"(11) 98765-4321"`
> - `"1132654321"` → `"(11) 3265-4321"`
> - `"123"` → lança exceção

Guarde a saída completa.

## Passo 3 — Comparar (5 min)

Sem ainda classificar em piso/teto/julgamento (isso é o Bloco 3) — só observe e anote:

- A primeira saída tratou o caso de número inválido? Tratou a diferença entre celular e fixo?
- A segunda saída seguiu exatamente a assinatura e as regras pedidas?
- Alguma das duas inventou uma regra que você não pediu?

Guarde as duas saídas — o Bloco 3 usa exatamente elas.
