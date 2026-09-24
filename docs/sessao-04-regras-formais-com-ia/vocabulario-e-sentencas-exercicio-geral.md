# Exercício de IA — Geral: engenharia reversa de regras em planilha

**Para quem não lê código.** Este exercício não pede programação nem terminal. O trabalho é ler as fórmulas de uma planilha de cálculo de comissão da Vetor, sem nenhuma especificação escrita disponível, e extrair delas o vocabulário SBVR e as sentenças RuleSpeak que elas decidem silenciosamente — do mesmo jeito que um trecho de código esconde regra dentro de um `if`, uma planilha esconde regra dentro de uma fórmula.

## O artefato: planilha de comissão de vendedores

Baixe [planilha-comissoes-vetor.xlsx](assets/planilha-comissoes-vetor.xlsx). Ela tem uma aba, "Comissoes", com sete vendedores, e a coluna F (Comissão) é calculada por fórmula, não digitada à mão. Este é o único artefato que descreve a regra de comissionamento da Vetor: não existe documento nem conversa registrada, só esta planilha, usada pelo financeiro há mais de um ano.

## Passo 1 — leia antes de perguntar ao agente

Abra a planilha. Clique na célula F2 (a comissão de Ana) e leia a fórmula na barra de fórmulas, sem calculá-la de cabeça ainda. Repita para F4 (Carla) e F6 (Elis), duas linhas com combinações bem diferentes de Nível e Cliente Principal Atendido. Escreva por escrito quantas regras distintas você enxerga só de olhar as três fórmulas, e existe algum número fixo dentro delas que parece ser um teto?

## Passo 2 — o prompt de engenharia reversa

Copie o texto das fórmulas das células F2, F4 e F6 (não os valores calculados, o texto da fórmula) e cole numa conversa nova com o agente, junto com os nomes das seis colunas da planilha e este prompt:

```text
Este é o único artefato que descreve esta regra de comissionamento — não
existe especificação escrita em nenhum outro lugar, só estas fórmulas de
planilha. As colunas são: Vendedor, Nivel, Cliente Principal Atendido,
Valor Vendido no Mes, Meta do Mes, Comissao (a fórmula).

Leia as fórmulas e extraia delas as regras de negócio, no vocabulário SBVR:

1. Liste o vocabulário mínimo (termos e definições) necessário para
   descrever as regras, com uma coluna de sinônimos a evitar.
2. Para cada regra encontrada, classifique-a como estrutural
   (classificação ou derivação) ou operativa. Escreva-a na forma
   RuleSpeak correspondente ("deve" / "não deve" / "pode ... somente
   se") se for operativa, ou como prosa declarativa se for estrutural.
3. Numere cada regra (RN- para operativa, RD- para estrutural), cite a
   evidência exata (a função da fórmula de onde ela vem, por exemplo
   "o segundo termo somado dentro do MIN") e atribua confiança 🟢 (a
   fórmula confirma a regra sem ambiguidade, já que é a única fonte
   disponível).
4. Preste atenção especial a qualquer limite fixo dentro de uma função
   MIN ou MAX: ele costuma ser uma regra de teto que ninguém nomeou.

Não sugira mudar a fórmula. Só extraia e formalize o que ela já decide.
```

## Passo 3 — compare com a sua linha de base

Quantas regras o agente encontrou, contra as que você registrou no passo 1? O teto de R$ 5.000,00 dentro do `MIN(...)` apareceu na sua leitura inicial, ou só ficou explícito depois do critério do passo 2?

## Passo 4 — confira contra a linha da Elis

A linha 6 (Elis) tem valor vendido de R$ 500.000,00, muito acima da meta, é Senior e atende cliente Atacado — a combinação que deveria acionar todos os bônus ao mesmo tempo. Peça ao agente para calcular, regra por regra, o valor de cada componente da comissão dela (faixa base, bônus de senioridade, adicional de atacado) antes do teto, e depois confirmar que o teto de R$ 5.000,00 é o que efetivamente prevalece no resultado final. Compare com o valor que a própria planilha calcula para F6.

**Questões exploratórias:**

- Alguma das regras extraídas do passo 2 é uma regra de classificação que nunca teve nome próprio na planilha, do mesmo jeito que "Cliente Recorrente" não tinha nome no código da Sessão 3?
- Se o financeiro decidisse mudar o teto de R$ 5.000,00 para R$ 6.000,00 amanhã, a formalização em RN/RD do passo 2 aponta exatamente qual regra mudar, sem precisar reabrir a fórmula inteira?

## Evidência a entregar

Três itens: a contagem de regras da sua linha de base no passo 1, a formalização completa do agente (vocabulário, RN/RD numerados, evidência, confiança) do passo 2, e a conferência da linha da Elis do passo 4, com os três componentes calculados antes do teto e a confirmação de que ele prevalece.

**Próxima página:** [Exercício de IA — Especialista](vocabulario-e-sentencas-exercicio-especialista.md).
