# Exercício de IA — Geral: identifique a sobreposição

**Para quem não escreve código.** Este exercício não usa terminal nem execução de teste. O trabalho é usar o agente para listar combinações de regras que se sobrepõem, e decidir a política de acerto antes que alguém implemente qualquer coisa.

## Regras em vigor

Três regras de desconto da Vetor, já especificadas: a faixa por valor e tipo de cliente (até R$ 500,00 sem desconto, subindo em degraus até 15%, e 20% para atacado acima de R$ 10.000,00), o adicional de 5 pontos percentuais para cliente atacado recorrente (mais de 5 pedidos aprovados), e o desconto de lançamento de 3 pontos percentuais (primeiro pedido, valor menor que R$ 1.000,00, qualquer tipo de cliente). O teto de R$ 1.000,00 por pedido vale para todas as combinações.

## Passo 1 — peça ao agente para listar as combinações

Descreva as três regras acima para o agente, em prosa, e peça: "liste todas as combinações de Valor do Pedido, Tipo de Cliente, Pedidos Aprovados e 'é o primeiro pedido' que poderiam se aplicar ao mesmo tempo a um único pedido real — sem resolver a sobreposição, só identificá-la."

## Passo 2 — decida a política, sozinho

Sem pedir ao agente para decidir por você: a sobreposição que ele encontrou pede Unique (redesenhando as faixas para não se cruzarem), Priority (uma regra vence explicitamente sobre a outra) ou Collect (os descontos se somam)? Escreva a política escolhida e o motivo, numa frase que justifique por que essa política, e não outra, é a certa para este caso.

## Passo 3 — calcule um caso real com a sua política

Um pedido de R$ 800,00, de um cliente atacado com 6 pedidos aprovados que também é o primeiro pedido dele, combina com a regra de recorrência **e** com a regra de lançamento ao mesmo tempo. Aplique a política que você escolheu no passo 2 e calcule o desconto resultante. Depois peça ao agente o mesmo cálculo, a partir da mesma política, e compare.

**Questões exploratórias:**

- O agente encontrou sozinho a sobreposição entre recorrência e lançamento, ou precisou ser guiado a procurá-la especificamente?
- Sua política escolhida no passo 2 é a mesma que o incidente do exemplo de aplicação de IA desta sessão deveria ter tido desde o início?

## Evidência a entregar

Três itens: a lista de combinações sobrepostas do passo 1, a política de acerto do passo 2 com o motivo escrito, e o cálculo do passo 3 comparado com o resultado do agente.

**Próxima página:** [Exercício de IA — Especialista](tabelas-de-decisao-exercicio-especialista.md).
