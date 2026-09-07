# Tabelas de decisão e DMN

Uma regra isolada em RuleSpeak funciona bem quando existe uma condição por vez. Quando várias condições combinam (tipo de cliente, valor do pedido, histórico do cliente), a prosa começa a esconder combinação que ninguém tratou. Tabela de decisão resolve isso tornando toda combinação visível numa grade.

## Por que mais de uma dimensão de condição pede tabela

Um sistema de desconto que combina faixa de valor (quatro possibilidades) com tipo de cliente (duas possibilidades, cada uma com sua própria regra adicional) já tem oito combinações possíveis. Escrever isso em frases soltas de RuleSpeak ("must" para cada combinação) produz oito ou mais sentenças, e não fica óbvio, só de ler, se alguma combinação ficou de fora. Uma tabela de decisão lista as mesmas oito combinações em linhas, com as condições nas colunas de entrada e o resultado na coluna de saída: qualquer combinação ausente aparece como uma linha que falta, não como um silêncio.

[DMN](../referencia/bibliografia.md#decision-model-and-notation-dmn) (*Decision Model and Notation*), padrão da OMG, formaliza essa tabela. Cada linha combina valores das condições de entrada e determina uma saída; a notação inteira só funciona se ficar claro o que fazer quando mais de uma linha poderia se aplicar ao mesmo caso — e é aí que entra a política de acerto.

## Política de acerto: o que fazer quando duas linhas combinam

DMN define sete políticas de acerto (*hit policies*). As três que aparecem com mais frequência em regra de negócio:

- **Unique.** As linhas nunca se sobrepõem — para qualquer combinação de entrada, só uma linha pode ser verdadeira. É a política mais segura, porque uma sobreposição vira erro de tabela, detectável antes de rodar.
- **First.** A tabela é avaliada de cima para baixo, e vale a primeira linha que combinar. Útil quando uma exceção precisa vir antes da regra geral — mas exige disciplina de ordem, porque trocar duas linhas de posição muda o resultado.
- **Priority.** Linhas podem se sobrepor; quando mais de uma combina, vale a de maior prioridade declarada. Diferente de First, a prioridade é explícita na tabela, não implícita na posição da linha.

As outras quatro (Any, em que todas as linhas que combinarem devem concordar no resultado; Collect, que retorna todos os resultados com agregação opcional de soma, mínimo, máximo ou contagem; Rule Order e Output Order, que retornam todos os resultados em ordens diferentes) servem para casos em que mais de um resultado é esperado ao mesmo tempo, não para decisão de valor único como desconto.

| Situação | Política mais indicada |
|---|---|
| Cada combinação de entrada tem exatamente uma resposta certa | Unique |
| Existe uma exceção que precisa ser checada antes da regra geral | First |
| Várias regras podem valer ao mesmo tempo, com uma vencendo por prioridade | Priority |
| Mais de um resultado é esperado ao mesmo tempo, não um só | Collect |

!!! question "Antes de continuar"
    Pense numa regra de desconto ou de elegibilidade do seu próprio domínio, com mais de uma condição combinando. Existe alguma combinação em que duas linhas poderiam, por engano, se aplicar ao mesmo caso? Se sim, qual política de acerto evitaria o problema?

## Montando uma tabela com mais de uma dimensão

Uma tabela de decisão para faixa de valor combinada com tipo de cliente:

| Valor do Pedido | Tipo de Cliente | Desconto |
|---|---|---|
| ≤ R$ 500,00 | qualquer | 0% |
| R$ 500,01 a R$ 2.000,00 | qualquer | 5% |
| R$ 2.000,01 a R$ 5.000,00 | qualquer | 10% |
| > R$ 5.000,00 e ≤ R$ 10.000,00 | qualquer | 15% |
| > R$ 10.000,00 | atacado | 20% |
| > R$ 10.000,00 | padrão | 15% |

As faixas de valor não se sobrepõem entre si, mas as duas últimas linhas mostram por que "tipo de cliente" precisa ser coluna, não só a faixa de valor: sem ela, um pedido de R$ 12.000,00 combinaria com as duas últimas linhas ao mesmo tempo. Com a coluna, a política **Unique** se sustenta — nenhuma combinação real de valor e tipo aparece em mais de uma linha.

## O antipadrão da tabela sem política declarada

O erro mais caro em tabela de decisão não é uma linha errada: é nenhuma política de acerto declarada, com a suposição implícita de que "é óbvio qual linha vale". Duas pessoas lendo a mesma tabela sem política escrita podem assumir Unique (e tratar sobreposição como bug) ou First (e tratar como comportamento esperado), e só descobrir a divergência quando o sistema já estiver em produção — o mesmo tipo de falha que o [Estudo de caso](estudo-de-caso.md) desta sessão examina em detalhe.

!!! tip "Aplique agora"
    Monte a tabela de decisão para uma regra adicional do seu domínio que combine tipo de cliente, uma condição de histórico e uma faixa de valor. Alguma linha se sobrepõe a outra? Que política de acerto você declararia, e por quê?

**Próxima página:** [IA como formalizadora](ia-como-formalizadora.md).
