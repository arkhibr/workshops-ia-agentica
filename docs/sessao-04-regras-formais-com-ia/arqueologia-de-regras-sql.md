# Arqueologia de regras em SQL

Arqueologia de regras é a recuperação disciplinada de decisões de negócio já incorporadas a um sistema. Aqui, o artefato é SQL realista, e o grupo usará uma ferramenta de IA capaz de ler arquivos e citar linhas para produzir regras em SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG para vocabulário e regras de negócio), uma tabela de decisão e casos de teste.

## O que o código prova

Código executável é evidência forte do comportamento implantado. A correspondência entre esse comportamento e a intenção atual do negócio depende de confirmação do domínio, porque um valor mágico pode ter sido regra válida, correção emergencial ou erro preservado por anos.

Por isso, cada descoberta recebe três campos:

- **evidência:** arquivo e linhas que sustentam a leitura
- **confiança:** força da inferência sobre a regra
- **questão de domínio:** o que ainda precisa de confirmação humana

## O artefato

Baixe ou abra [`assets/calculo-beneficio.sql`](assets/calculo-beneficio.sql), uma consulta de 32 linhas que contém `CASE` aninhado, valores mágicos, `JOIN`, `NULL`, filtros e sobreposição por ordem, sem nenhuma especificação paralela. Os limites 759,00 e 900,00 foram fixados para a aula, e a consulta não é uma implementação da Lei Complementar nº 214/2025, embora use categorias parecidas com as do cashback do IBS e da CBS.

Antes de usar IA, responda:

1. Quantas classificações você encontra?
2. Que linhas removem registros antes de qualquer classificação?
3. Qual condição anterior pode esconder uma condição posterior?
4. O que acontece quando a renda está ausente?

## O método em seis movimentos

### 1. Inventário

Liste tabelas, colunas, valores literais e resultados possíveis, e converta nomes técnicos em candidatos a conceitos sem apagar o vínculo com a coluna. Registre fatos como “Pessoa possui CPF” e “Documento Fiscal registra Categoria”, mas ainda sem chamar nenhum item de regra.

### 2. Captura de evidência

Antes de interpretar, registre para cada predicado o arquivo, o intervalo exato de linhas e o trecho literal, como `calculo-beneficio.sql:28`, `INNER JOIN cadastro_familiar c ON c.responsavel_id = p.pessoa_id`. A evidência capturada nesse movimento é a base que as hipóteses, a validação e os testes vão citar depois.

### 3. Hipóteses de regra

Leia cada evidência como indício de uma regra candidata. Um `INNER JOIN` pode conter uma regra de elegibilidade, um `WHERE` pode suprimir casos e a ordem do `CASE` estabelece precedência, e cada hipótese recebe confiança e a evidência capturada no movimento 2.

### 4. Validação de domínio

Leve as hipóteses ao especialista do domínio em forma de perguntas fechadas, como “a devolução deve ser calculada quando a situação é `BLOQUEADO`?”. Cada resposta confirma a hipótese, a refuta ou a mantém em aberto, e a confiança é atualizada com o nome de quem respondeu e a data da resposta.

### 5. Formalização SBVR

Classifique cada hipótese como regra estrutural de classificação, estrutural de derivação ou operativa. Se não houver evidência de obrigação dirigida a um ator, evite fabricar regra operativa apenas porque existe código. As combinações relevantes entram numa **tabela de decisão**, que organiza em linhas as condições e o resultado de cada uma, com a política de acerto declarada, e os conflitos aparecem nela: compare a coluna `situacao` com os cálculos de `devolucao_cbs` e `devolucao_ibs` e verifique se eles produzem valores mesmo quando a situação indica bloqueio.

### 6. Derivação de testes

Derive testes das regras recuperadas. Cada teste confirma o comportamento atual do SQL, e a decisão sobre manter esse comportamento pertence à validação de domínio do movimento 4.

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
9. casos de teste rastreados às regras;
10. perguntas fechadas para o especialista do domínio.

Para cada descoberta, cite arquivo e intervalo exato de linhas, transcreva
o trecho literal e atribua confiança.

Separe comportamento confirmado de intenção inferida. Não invente regra
para explicar um número mágico. Não proponha refatoração nesta etapa.
```

## Casos que não podem faltar

Peça ao agente uma matriz com ID do teste, regra de origem, entradas, saída observada, evidência e dúvida de domínio. Inclua:

- CPF irregular com aquisição elegível (linha 6)
- renda ausente, pois `COALESCE` a transforma em zero (linhas 4, 7 e 16)
- renda exatamente em 759,00 e logo acima (linha 7)
- item com Imposto Seletivo numa categoria das linhas 9 ou 11 (linhas 9 a 13)
- botijão de GLP com 13 kg e com mais de 13 kg (linhas 11 e 22)
- documento fiscal ausente após `LEFT JOIN` e filtro no `WHERE` (linhas 29 a 31)
- devolução calculada para situação bloqueada (linhas 6 e 20 a 26)
- faixa até 900,00 que leva à análise manual (linhas 16 e 17)

O caso do item com Imposto Seletivo numa categoria das linhas 9 ou 11 é o **teste de precedência**, porque a ordem do `CASE` faz a classificação por categoria prevalecer sobre a exclusão da linha 13. O caso de renda `NULL` é o teste de **dados ausentes**, porque o código converte ausência em renda zero e pode classificar a pessoa como elegível.

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
