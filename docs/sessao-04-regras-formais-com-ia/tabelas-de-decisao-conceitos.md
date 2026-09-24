# Tabelas de decisão e IA como formalizadora

Uma regra isolada em RuleSpeak funciona bem quando existe uma condição por vez. Quando várias condições combinam — tipo de cliente, valor do pedido, histórico do cliente — a prosa começa a esconder combinação que ninguém tratou, e é aí que a tabela de decisão entra. Esta página trata de quando montar uma tabela, como escolher a política que resolve sobreposição, e do papel do agente como formalizador dessas duas coisas, nunca como quem decide por conta própria.

## Por que mais de uma dimensão de condição pede tabela

Um sistema de desconto que combina faixa de valor (quatro possibilidades) com tipo de cliente (duas, cada uma com regra adicional) já tem oito combinações. Escrever isso em frases soltas de RuleSpeak produz oito ou mais sentenças, e não fica óbvio, só de ler, se alguma combinação ficou de fora. Uma tabela de decisão lista as mesmas combinações em linhas, com as condições nas colunas de entrada e o resultado na coluna de saída: qualquer combinação ausente aparece como uma linha que falta, não como um silêncio.

[DMN](../referencia/bibliografia.md#decision-model-and-notation-dmn) (*Decision Model and Notation*), padrão da OMG, formaliza essa tabela. A régua prática: quando uma regra combina **três ou mais condições**, prosa deixa de escalar e tabela vira a forma mais segura de escrever a regra.

## Política de acerto: o que fazer quando duas linhas combinam

DMN define sete políticas de acerto (*hit policies*). As três que aparecem com mais frequência em regra de negócio:

- **Unique.** As linhas nunca se sobrepõem — só uma pode ser verdadeira para qualquer combinação. A política mais segura, porque sobreposição vira erro de tabela, detectável antes de rodar.
- **First.** A tabela é avaliada de cima para baixo, e vale a primeira linha que combinar. Útil quando uma exceção precisa vir antes da regra geral, mas exige disciplina de ordem.
- **Priority.** Linhas podem se sobrepor; quando mais de uma combina, vale a de maior prioridade declarada, explícita na tabela, não implícita na posição da linha.

As outras quatro (Any, Collect, Rule Order, Output Order) servem para casos em que mais de um resultado é esperado ao mesmo tempo, não para decisão de valor único como desconto.

| Situação | Política mais indicada |
|---|---|
| Cada combinação de entrada tem exatamente uma resposta certa | Unique |
| Existe exceção que precisa ser checada antes da regra geral | First |
| Várias regras podem valer ao mesmo tempo, uma vencendo por prioridade | Priority |
| Mais de um resultado é esperado ao mesmo tempo | Collect |

Quando uma terceira condição entra, a tabela precisa de uma linha para toda combinação, inclusive as que o domínio proíbe de existir. Nessas, a saída recebe "—", não "0": zero seria resposta válida sobre o valor do desconto; "—" declara que a combinação não deveria existir no domínio, e se ela aparecer em produção, o erro está em outro lugar do sistema, não na tabela.

!!! question "Antes de continuar"
    Pense numa regra do seu domínio com mais de uma condição combinando. Existe alguma combinação em que duas linhas poderiam, por engano, se aplicar ao mesmo caso? Que política de acerto evitaria o problema?

## O antipadrão da tabela sem política declarada

O erro mais caro em tabela de decisão não é uma linha errada: é nenhuma política declarada, com a suposição implícita de que "é óbvio qual linha vale". Duas pessoas lendo a mesma tabela sem política escrita podem assumir Unique (e tratar sobreposição como bug) ou First (e tratar como esperado), e só descobrir a divergência quando o sistema já estiver em produção.

## O agente como formalizador, não como decisor

Nas sessões anteriores, o agente recebia uma especificação e produzia código. Aqui a direção se inverte: o agente recebe prosa ambígua, ou código legado, ou uma planilha, e devolve vocabulário SBVR, sentença RuleSpeak ou linha de tabela DMN. O risco muda de natureza — uma formalização errada pode *parecer* certa (usar os termos certos, ler bem) e ainda assim ter mudado o escopo da regra original sem que ninguém perceba, porque não existe teste automatizado que verifique se uma frase captura a intenção de outra frase.

Três erros se repetem quando um agente formaliza sem supervisão: **generalizar o escopo** (uma regra que valia só para um tipo de cliente vira regra para "todo pedido"), **inventar a política de acerto** (o agente escolhe First ou Unique sem que ninguém tenha decidido isso) e **confundir regra estrutural com operativa** (o mesmo operador modal sai para as duas, se o agente não foi instruído a distinguir).

## Verificação por retrotradução

A técnica que expõe os três erros acima chama-se retrotradução: peça para uma segunda pessoa, ou para o próprio agente numa conversa nova, sem ver a formalização, reescrever a regra formal de volta em prosa comum, sem consultar o original. Se a retrotradução bater com a intenção de quem escreveu a regra, a formalização provavelmente preservou o significado; se disser outra coisa, o escopo mudou silenciosamente.

Um exemplo: a prosa original diz "o desconto de atacado nunca ultrapassa o teto". O agente formaliza como "o desconto de um Pedido **não deve** exceder R$ 1.000,00". A retrotradução, pedida a quem não viu a prosa original, devolve "nenhum pedido pode ter desconto maior que R$ 1.000,00" — e aqui já apareceu a diferença: a prosa original falava só do desconto de *atacado*, e a retrotradução generalizou para *qualquer* pedido, um escopo ampliado sem aviso que só a retrotradução expôs.

!!! tip "Aplique agora"
    Na próxima vez que pedir a um agente para formalizar uma regra ou montar uma tabela de decisão, peça também, numa conversa separada, para retrotraduzir o resultado sem contexto adicional, e para declarar a política de acerto que ele escolheu, se houver mais de uma linha.

**Próxima página:** [Exemplo de aplicação de IA](tabelas-de-decisao-exemplo-de-aplicacao-de-ia.md).
