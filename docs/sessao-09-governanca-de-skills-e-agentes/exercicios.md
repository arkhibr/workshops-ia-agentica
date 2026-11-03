# Exercícios — triagem e riscos dos protótipos

Os exercícios aplicam a ficha de governança a uma skill da ACME, universidade fictícia.

## O caso

A ACME tem uma skill que revisa pull requests contra padrões de arquitetura e escreve um parecer, com critérios de aprovação ainda não definidos. Por conveniência, a skill usa a credencial pessoal de quem a executa, com escrita em todos os repositórios dessa pessoa.

## 1. Dono e finalidade

1. Quem responde pela skill e quem é afetado pelo parecer?
2. Como a revisão seria feita sem IA?

??? note "Resposta esperada"
    1. A equipe de arquitetura responde, e os autores dos pull requests são afetados.
    2. Um arquiteto revisaria o pull request com uma lista de verificação.

## 2. Dados e autonomia

1. Em que classe de dado está o código revisado?
2. Que permissão a credencial dá e que permissão a finalidade exige?
3. A skill sugere, prepara para aprovação ou executa?

??? note "Resposta esperada"
    1. O código revisado é dado interno.
    2. A credencial dá escrita em todos os repositórios, e a finalidade exige leitura de um repositório e escrita do parecer.
    3. A skill sugere, porque uma pessoa decide o merge.

## 3. Faixa e fator decisivo

Na forma estrita da regra, um fator crítico leva o caso direto à faixa alta, sem soma de pontos.

1. Em que faixa a skill fica e qual fator decide a faixa?
2. Qual seria o impacto se a solução fosse usada fora da finalidade?
3. Que premissa não verificada torna a faixa preliminar?

??? note "Resposta esperada"
    1. A faixa é alta pela credencial com escrita, e desce para moderada com token próprio de leitura.
    2. A skill poderia alterar qualquer repositório da pessoa que a executa.
    3. Ninguém verificou se o parecer é usado como aprovação, e essa verificação passa a ser condição do gate de publicação.

## 4. Risco como evento e consequência

O [cartão B](riscos-de-agentes.md#tres-incidentes) descreve uma permissão maior que a finalidade.

1. Que evento esse incidente produz nesta skill e qual é o dano?
2. Em que fronteira de confiança o evento ocorre?

??? note "Resposta esperada"
    1. A skill escreve em outro repositório com a credencial pessoal e altera código sem revisão humana.
    2. O evento ocorre quando o código do pull request, que não é confiável, chega à ferramenta de escrita.

## 5. Controle preventivo e evidência

1. Que controle preventivo, aplicado fora do modelo, reduz o risco do exercício 4?
2. Qual teste de aceite entre [T01 e T07](controles-e-evidencias.md#testes-de-aceite-t01-a-t07) serve de evidência?
3. Por que pedir no `SKILL.md` que a credencial seja usada só para leitura reprova a linha?

??? note "Resposta esperada"
    1. Um token próprio, somente de leitura e restrito ao repositório revisado.
    2. O teste T03, em que a API rejeita a escrita feita com token de leitura.
    3. Um controle que depende só de instrução no prompt pode ser ignorado pelo modelo, e o portão da [oficina](oficina-de-ferramentas.md) reprova o plugin `revisando-pull-requests` por isso.

## 6. Discussão com a turma

As perguntas vêm do guia [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026) e se aplicam à skill do caso.

1. Se o PO aprovou o caso, o time pode usar qualquer dado?
2. Um agente que apenas lê tem risco baixo?
3. E se a avaliação atingir 95% de acerto?

??? note "Resposta esperada"
    1. O uso dos dados depende de classificação, autorização de acesso e LGPD.
    2. O risco depende do que o agente lê e do uso da resposta, e um parecer errado pode orientar um merge.
    3. Os 5% restantes podem conter a escrita indevida, e a severidade dos erros também conta.

## Extensão

Depois da sessão, as mesmas perguntas podem ser respondidas para um protótipo real da equipe, no ambiente interno e sem registrar credencial.

**Próxima página:** [Controles e evidências](controles-e-evidencias.md).
