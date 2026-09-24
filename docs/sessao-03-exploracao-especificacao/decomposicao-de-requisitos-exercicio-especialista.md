# Exercício de IA — Especialista: especifique, implemente, verifique

**Para quem implementa em código.** Este exercício usa o agente de codificação já configurado, o git e o Node.js 20 ou superior. Todos os experimentos partem de um projeto vazio, montado nesta oficina.

## Preparação

**Passo 1. Crie o projeto.**

```bash
mkdir oficina-decomposicao && cd oficina-decomposicao
git init
node --version   # precisa mostrar v20 ou superior
```

**Passo 2. Crie a regra de desconto.** Salve como `src/desconto.js`:

```javascript
export const TETO_DESCONTO = 1000;

export function calcularDesconto(valorTotal, tipoCliente) {
  if (typeof valorTotal !== 'number' || Number.isNaN(valorTotal) || valorTotal < 0) {
    throw new TypeError('valorTotal deve ser um numero nao negativo');
  }

  let percentual = 0;
  if (valorTotal > 5000) percentual = 0.15;
  else if (valorTotal > 2000) percentual = 0.1;
  else if (valorTotal > 500) percentual = 0.05;

  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
```

**Passo 3. Crie os testes.** Salve como `test/desconto.test.js`:

```javascript
import assert from 'node:assert/strict';
import { describe, it } from 'node:test';

import { calcularDesconto, TETO_DESCONTO } from '../src/desconto.js';

describe('calcularDesconto', () => {
  it('nao da desconto ate 500,00', () => {
    assert.equal(calcularDesconto(500, 'padrao'), 0);
  });
  it('da 5% na faixa de 500,01 a 2.000,00', () => {
    assert.equal(calcularDesconto(1000, 'padrao'), 50);
  });
  it('da 10% na faixa de 2.000,01 a 5.000,00', () => {
    assert.equal(calcularDesconto(3000, 'padrao'), 300);
  });
  it('da 15% acima de 5.000,00', () => {
    assert.equal(calcularDesconto(6000, 'padrao'), 900);
  });
  it('respeita o teto de desconto por pedido', () => {
    assert.equal(calcularDesconto(100000, 'padrao'), TETO_DESCONTO);
  });
});
```

**Passo 4. Confirme o estado inicial.**

```bash
npm init -y
npm pkg set type=module
npm pkg set scripts.test="node --test"
npm test
```

Os cinco testes precisam passar antes de continuar.

## O pedido

> "Quero um desconto de lançamento pra atrair cliente novo: primeiro pedido dele, se for baixinho, ganha um desconto a mais."

## Passo 1 — perguntas

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de redigir a especificação, aplicando a disciplina da [intervenção socrática](intervencao-socratica-conceitos.md): uma de cada vez, sem a resposta embutida na formulação.

## Passo 2 — respostas

??? note "Respostas de quem pediu — abra só depois do passo 1"
    - O que conta como "primeiro pedido"? Cliente com `pedidosAprovados` igual a zero, e vale para cliente padrão e atacado, sem distinção de tipo.
    - O que conta como "baixinho"? Valor do pedido menor que R$ 1.000,00. Pedidos grandes de cliente novo não se qualificam.
    - Quanto é o desconto a mais? 3 pontos percentuais, somados à faixa normal.
    - O teto de R$ 1.000,00 continua valendo? Sim, sempre.

## Passo 3 — especifique

Escreva a regra de negócio (BR) e o requisito funcional (FR), no formato do [Exemplo de aplicação de IA](decomposicao-de-requisitos-exemplo-de-aplicacao-de-ia.md). `calcularDesconto` vai precisar de um terceiro parâmetro, `pedidosAprovados`, opcional, com valor padrão que preserve o comportamento dos cinco testes já existentes.

## Passo 4 — implemente e verifique

Cole sua especificação para o agente e peça a implementação, com testes, dentro do projeto que você montou. Rode os quatro casos abaixo contra o resultado, com `node --test`:

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 800,00 | padrão | 0 | R$ 64,00 (5% + 3% = 8%) |
| 2 | R$ 1.500,00 | padrão | 0 | R$ 75,00 (5%, sem bônus, valor não é "baixinho") |
| 3 | R$ 800,00 | atacado | 0 | R$ 64,00 (o bônus não distingue tipo de cliente) |
| 4 | R$ 400,00 | padrão | 3 | R$ 0,00 (faixa de 0%, sem bônus, não é primeiro pedido) |

Confira também que os cinco testes originais continuam passando.

## Passo 5 — escreva a função de aptidão

A Vetor pede que `calcularDesconto` "continue rápida mesmo com muito tráfego". Escreva o cenário de qualidade completo (fonte, estímulo, ambiente, artefato, resposta, medida), seguindo o template de [decomposição de requisitos](decomposicao-de-requisitos-conceitos.md#cenario-de-qualidade-e-funcao-de-aptidao). Depois peça ao agente uma função de aptidão: um teste em Node que chama `calcularDesconto` quinhentas vezes, mede o tempo com `performance.now()`, e falha se a média ultrapassar o limiar que você declarou no cenário.

**Observe:** o caso 2, de valor grande, e o caso 4, que não é primeiro pedido, são os dois que provam que o bônus tem fronteira, em vez de nunca se aplicar. Se qualquer um dos dois falhar, é sinal de que a especificação do passo 3 não deixou a fronteira explícita o bastante para o agente implementar sem adivinhar.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Perguntas antes da resposta | 20% | As perguntas do passo 1 foram escritas e preservadas antes de abrir o bloco de respostas |
| Especificação no padrão BR/FR | 40% | A regra de negócio e o requisito funcional estão separados, com valores concretos, não uma frase genérica |
| Verificação real executada | 40% | Executou `node --test` contra os quatro casos novos, os cinco originais, e a função de aptidão do passo 5 |

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
