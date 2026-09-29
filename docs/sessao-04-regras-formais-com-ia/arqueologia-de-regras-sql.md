# Arqueologia de regras em SQL

Arqueologia de regras é a recuperação disciplinada de decisões de negócio já incorporadas a um sistema. Aqui, o artefato é SQL realista: o grupo usará uma ferramenta de IA capaz de ler arquivos e citar linhas para produzir regras SBVR e casos de teste.

## O que o código prova

Código executável é evidência forte do comportamento implantado. Ele não prova que esse comportamento corresponde à intenção atual do negócio. Um valor mágico pode ter sido regra válida, correção emergencial ou erro preservado por anos.

Por isso, cada descoberta recebe três campos:

- **evidência:** arquivo e linhas que sustentam a leitura;
- **confiança:** força da inferência sobre a regra;
- **questão de domínio:** o que ainda precisa de confirmação humana.

## O artefato

Baixe ou abra [`assets/calculo-beneficio.sql`](assets/calculo-beneficio.sql). A consulta contém `CASE` aninhado, valores mágicos, `JOIN`, `NULL`, filtros e sobreposição por ordem. Não existe especificação paralela.

Antes de usar IA, responda:

1. Quantas classificações você encontra?
2. Que linhas removem registros antes de qualquer classificação?
3. Qual condição anterior pode esconder uma condição posterior?
4. O que acontece quando a renda está ausente?

## O método em seis movimentos

### 1. Inventário

Liste tabelas, colunas, valores literais e resultados possíveis. Ainda não chame cada item de regra.

### 2. Conceitos e fatos

Converta nomes técnicos em candidatos a conceitos, sem apagar o vínculo com a coluna. Registre fatos como “Pessoa possui CPF” e “Documento Fiscal registra Categoria”.

### 3. Hipóteses de regra

Leia cada predicado como evidência. Um `INNER JOIN` pode conter uma regra de elegibilidade; um `WHERE` pode suprimir casos; a ordem do `CASE` estabelece precedência.

### 4. Formalização SBVR

Classifique cada hipótese como regra estrutural de classificação, estrutural de derivação ou operativa. Se não houver evidência de obrigação dirigida a um ator, evite fabricar regra operativa apenas porque existe código.

### 5. Tabela e conflitos

Expanda combinações relevantes. Compare a coluna `situacao` com os cálculos de `devolucao_cbs` e `devolucao_ibs`: elas podem produzir valores mesmo quando a situação indica bloqueio?

### 6. Casos de teste

Derive testes das regras recuperadas. Um teste confirma o comportamento do SQL; a validação do domínio decide se esse comportamento deve continuar.

## Prompt para a ferramenta de arqueologia

```text
Analise o arquivo calculo-beneficio.sql como evidência de comportamento
implementado. Não presuma que o código representa a intenção correta.

Entregue:
1. conceitos e definições, ligados às tabelas e colunas;
2. tipos de fato entre os conceitos;
3. regras estruturais de classificação;
4. regras estruturais de derivação;
5. regras operativas de obrigação, proibição ou permissão somente quando
   o código oferecer evidência suficiente;
6. exceções e precedência causadas pela ordem de CASE, JOIN e WHERE;
7. conflitos, lacunas, valores mágicos e tratamento de NULL;
8. tabela de decisão com política de acerto;
9. casos de teste rastreados às regras.

Para cada descoberta, cite arquivo e intervalo exato de linhas, atribua
confiança e formule uma pergunta ao especialista do domínio.

Separe comportamento confirmado de intenção inferida. Não invente regra
para explicar um número mágico. Não proponha refatoração nesta etapa.
```

## Casos que não podem faltar

Peça ao agente uma matriz com ID do teste, regra de origem, entradas, saída observada, evidência e dúvida de domínio. Inclua:

- CPF irregular com aquisição elegível;
- renda ausente, pois `COALESCE` a transforma em zero;
- renda exatamente em 759,00 e logo acima;
- item com Imposto Seletivo dentro de uma categoria específica;
- botijão de GLP com 13 kg e com mais de 13 kg;
- documento fiscal ausente após `LEFT JOIN` e filtro no `WHERE`;
- devolução calculada para situação bloqueada;
- faixa até 900,00 que leva à análise manual.

O caso do item com Imposto Seletivo dentro de categoria específica é o **teste de precedência**: a ordem do `CASE` faz a categoria vencer a exclusão posterior. O caso de renda `NULL` é o teste de **dados ausentes**: o código converte ausência em renda zero e pode classificar a pessoa como elegível.

## Saída esperada

| Artefato | Conteúdo mínimo |
|---|---|
| Glossário | conceito, definição, coluna e sinônimo arriscado |
| Catálogo SBVR | ID, tipo, sentença, linhas, confiança e pergunta |
| Tabela de decisão | combinações, resultado e política de acerto |
| Matriz de testes | regra, entradas, saída atual e intenção pendente |

## Evidência a entregar

Entregue o catálogo, a tabela e a matriz. Destaque uma regra confirmada, uma intenção apenas inferida e um conflito que impeça validar o comportamento sem conversar com o domínio.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
