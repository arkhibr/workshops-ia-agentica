# Exercício de IA — Especialista: engenharia reversa de regras em código

**Para quem lê código.** Este exercício não pede implementação nem execução de teste. O trabalho é ler um trecho de código legado da Vetor, sem nenhuma especificação escrita disponível, e extrair dele o vocabulário SBVR e as sentenças RuleSpeak que ele decide silenciosamente.

## O artefato: função de frete grátis

Este é o único artefato que descreve esta regra. Não existe especificação em nenhum outro lugar — nem documento, nem conversa registrada, só o código abaixo, em produção há mais de um ano:

```javascript
// src/frete.js — sem documentação, autor original já não está no time
function calcularFrete(pedido, cliente) {
  if (pedido.valorTotal >= 300 && cliente.regiao !== 'remota') {
    return 0;
  }
  if (cliente.tipo === 'atacado' && cliente.pedidosAprovados > 10 && cliente.regiao !== 'remota') {
    return 0;
  }
  if (cliente.regiao === 'remota') {
    return 45;
  }
  return 19.90;
}
```

## Passo 1 — leia antes de perguntar ao agente

Sem colar o código no agente ainda, leia as quatro ramificações e responda por escrito: quantas regras de negócio distintas você enxerga, e existe alguma condição que, sozinha, anula o efeito das outras? Esse número é a sua linha de base.

## Passo 2 — o prompt de engenharia reversa

Cole o código acima numa conversa nova com o agente, junto com este prompt:

```text
Este é o único artefato que descreve esta regra de negócio — não existe
especificação escrita em nenhum outro lugar, só este código.

Leia a função e extraia dela as regras de negócio, no vocabulário SBVR:

1. Liste o vocabulário mínimo (termos e definições) necessário para
   descrever as regras, com uma coluna de sinônimos a evitar.
2. Para cada regra encontrada, classifique-a como estrutural
   (classificação ou derivação) ou operativa. Escreva-a na forma
   RuleSpeak correspondente ("deve" / "não deve" / "pode ... somente
   se") se for operativa, ou como prosa declarativa se for estrutural.
3. Numere cada regra (RN- para operativa, RD- para estrutural), cite a
   evidência exata (nome da função e a ramificação do código de onde ela
   vem) e atribua confiança 🟢 (o código confirma a regra sem
   ambiguidade, já que é a única fonte disponível).
4. Preste atenção especial à ordem das condições: uma ramificação
   anterior pode anular silenciosamente o efeito das que vêm depois.
   Se existir uma regra de exceção assim, aponte-a explicitamente,
   separada das demais.

Não implemente nada, não sugira refatoração. Só extraia e formalize o
que o código já decide.
```

## Passo 3 — compare com a sua linha de base

Quantas regras o agente encontrou, contra as que você havia registrado no passo 1? A regra de exceção por região remota — que faz qualquer cliente de região remota pagar frete fixo de R$ 45,00, mesmo com valor alto ou histórico de atacado recorrente — apareceu na sua leitura inicial, ou só ficou explícita depois de ler o código com o critério do passo 2?

## Passo 4 — retrotraduza

Abra uma conversa nova, sem o código original. Cole só as sentenças RuleSpeak formalizadas pelo agente (sem os comentários de evidência) e peça: "descreva em prosa comum o comportamento que estas regras produzem, para alguém que nunca viu o código." Compare a prosa devolvida com o comportamento real da função: ela preservou a precedência da região remota sobre as demais condições?

**Questões exploratórias:**

- O agente numerou a regra de região remota como `RN` ou tratou como parte de outra regra? Qual das duas leituras está mais correta, considerando que ela pode ser violada (alguém decidiu cobrar frete de cliente remoto) e por isso é operativa?
- Se este código fosse refatorado amanhã sem a formalização em mãos, qual das quatro regras é a mais fácil de perder por acidente, e por quê?

## Evidência a entregar

Três itens: a contagem de regras da sua linha de base no passo 1, a formalização completa do agente (vocabulário, RN/RD numerados, evidência, confiança) do passo 2, e a comparação da retrotradução do passo 4 contra o comportamento real da função.

**Próxima página:** [Conceitos: Tabelas de decisão e IA formalizadora](tabelas-de-decisao-conceitos.md).
