# Exercícios

Tente responder antes de abrir os blocos de resposta nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar).

## Situação compartilhada

Todos os exercícios desta página se referem à Vetor, plataforma fictícia de e-commerce B2B do workshop, e à faixa de desconto de atacado trabalhada na oficina: 20% acima de R$ 10.000,00 para cliente do tipo atacado, num código que já tem faixas de 0%, 5%, 10% e 15% por valor e um teto de R$ 1.000,00 por pedido.

## Recordar

### 1. Os quatro artefatos canônicos

Nomeie os quatro artefatos do ciclo e, em uma frase cada, o que decidem.

<details>
<summary>Ver resposta</summary>

Constitution: os princípios que nenhuma mudança pode violar. Especificação: o comportamento observável desta mudança, com critérios de aceitação. Plano: como a arquitetura realiza essa intenção, com as decisões técnicas. Tarefas: as fatias verticais que entregam comportamento demonstrável, com definição de pronto.
</details>

### 2. Os três níveis de compromisso com a especificação

Nomeie os três níveis da taxonomia de Böckeler e o que distingue cada um.

<details>
<summary>Ver resposta</summary>

*Spec-first*: a especificação orienta a primeira geração e pode ser abandonada depois, com o código voltando a ser a fonte de verdade. *Spec-anchored*: especificação e código evoluem juntos, e cada mudança reconcilia os dois lados. *Spec-as-source*: a especificação é o artefato primário editável, e o código é uma projeção regenerável dela.
</details>

### 3. Os dois eixos da verificação

Nomeie os dois eixos independentes de verificação e a pergunta que cada um responde.

<details>
<summary>Ver resposta</summary>

Aderência à especificação: requisitos, critérios e limites foram respeitados? Qualidade da implementação: o código segue padrões, arquitetura, segurança e operabilidade do repositório? Um "passa" num eixo não compensa falha no outro.
</details>

## Compreender

### 4. A constitution antes da especificação

Explique, em duas frases, por que faz diferença declarar os princípios do projeto antes da especificação de uma funcionalidade, em vez de revisá-los no final.

<details>
<summary>Ver resposta</summary>

Declarados antes, os princípios restringem o espaço de soluções que o plano pode propor, e a violação aparece no portão de arquitetura, quando corrigir custa pouco. Revisados no final, eles só conseguem reprovar trabalho já feito, o que cria pressão para aprovar com ressalva em vez de refazer.
</details>

### 5. Fatia vertical e fatia horizontal

A tarefa "criar a tabela de faixas no módulo de desconto" é fatia vertical ou horizontal? Justifique pelo critério de evidência.

<details>
<summary>Ver resposta</summary>

Horizontal. Ela não entrega comportamento observável por quem usa a função: ninguém consegue calcular um desconto diferente ao final dela. A versão vertical seria "atacado acima de R$ 10.000,00 recebe 20%, com teste de fronteira em R$ 10.000,00 exato", que atravessa estrutura e regra e termina com uma demonstração possível.

Ressalva: a tarefa T1 do exemplo arquitetural é deliberadamente uma troca de estrutura sem comportamento novo, e isso é legítimo como refatoração preparatória, desde que o critério de pronto seja a suíte existente continuar verde.
</details>

### 6. Documentação pesada e execução pesada

Explique por que dizer que o Superpowers é "mais leve" que o Spec Kit pode estar certo e errado ao mesmo tempo.

<details>
<summary>Ver resposta</summary>

Certo no eixo documental: ele não mantém constitution nem especificação consolidada do domínio. Errado no eixo operacional: exige design aprovado antes do código, plano granular, cópia isolada do repositório, teste antes da implementação, revisão em duas etapas e verificação antes de declarar conclusão. Os dois eixos são independentes, e "leve" sem dizer em qual deles esconde onde o custo aparece.
</details>

## Aplicar

### 7. Exercício-âncora: especifique, planeje, implemente e verifique

**O que é:** o ciclo completo sobre a faixa de atacado, a partir do projeto montado na oficina, terminando com a suíte verde e a decisão registrada.

**Antes de começar: a ordem importa.** O passo 2 só tem valor se acontecer antes do passo 4. Escrever a especificação depois de ver o código gerado produz um documento que descreve o que saiu, não um contrato que orienta o que deveria sair.

**Situação**

O pedido chegou assim: "ativa o desconto de atacado, 20% acima de dez mil". O código atual tem um teto de R$ 1.000,00 por pedido, aplicado a todas as faixas. Vinte por cento de R$ 12.000,00 são R$ 2.400,00.

**Seu papel**

Você conduz o ciclo e decide, com registro, o que acontece com o teto no atacado.

**Insumos disponíveis**

O projeto `oficina-sdd` montado na oficina, o agente que você já usa, e as cinco páginas de teoria desta sessão.

**Como conduzir**

1. **Classifique.** Aplique a régua de profundidade: essa mudança é S, M ou L? Registre o motivo em uma linha.
2. **Especifique.** Escreva dois requisitos numerados, cada um com caso concreto e caso de fronteira. O caso de fronteira de R$ 10.000,00 exato precisa estar lá.
3. **Decida o teto.** Registre na especificação, como regra de negócio numerada, o que acontece com o teto de R$ 1.000,00 no atacado, e o motivo da decisão. Qualquer das três saídas é aceitável desde que registrada e justificada.
4. **Planeje.** Escreva as decisões técnicas e pelo menos uma alternativa descartada, com o motivo da rejeição.
5. **Implemente.** Escreva o teste que falha primeiro, observe a mensagem de falha, e só então implemente. Guarde a mensagem de falha.
6. **Verifique nos dois eixos.** Confira aderência e qualidade separadamente, em duas leituras.

**Entrega esperada**

A classificação com motivo, a especificação com dois requisitos e a regra do teto, o plano com a alternativa descartada, a mensagem da primeira falha do teste, e as duas verificações.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decisão do teto registrada e justificada | 30% | A regra está numerada na especificação com o motivo, e o código a implementa. Qual das três saídas foi escolhida não pontua, o registro sim |
| Caso de fronteira presente e testado | 25% | R$ 10.000,00 exato aparece na especificação e tem teste correspondente que distingue a faixa anterior da nova |
| Falha observada antes da implementação | 25% | A mensagem de falha guardada mostra o valor errado esperado pela regra nova, não erro de sintaxe nem teste que já passava |
| Verificação em dois eixos separados | 20% | Existem duas leituras distintas registradas, uma de aderência e uma de qualidade, não um parecer único |

**Como verificar antes de entregar:** rode `npm test` e confirme que os três testes originais continuam passando. Uma implementação que quebra o comportamento do cliente padrão para acomodar o atacado falha no critério de aderência, mesmo que o requisito novo esteja atendido.

## Analisar

### 8. O portão que não pegou

No estudo de caso da Meridiano, os três portões aprovaram uma mudança cuja especificação estava errada. Analise a cadeia de rastreabilidade daquele caso e identifique em qual elo a verificação falhou, distinguindo o elo que estava íntegro do elo que não existia.

## Avaliar

### 9. Métrica que recomenda o contrário

Um time relata, no mesmo trimestre, aumento de integrações por semana de quatro para onze e aumento do retrabalho por defeito escapado de 8% para 21% das horas. A liderança quer ampliar o uso do agente com base no primeiro número.

Avalie a recomendação. Que terceira medida você pediria antes de decidir, e que decisão cada resultado possível dessa medida sustentaria?

## Criar

### 10. A constitution do seu time

Escreva a constitution do projeto em que você trabalha hoje, com no máximo cinco princípios. Cada princípio precisa ter a consequência nomeada, dizendo quem barra o quê.

Depois, aplique o teste de rejeição a cada um: descreva uma mudança plausível, que alguém do seu time poderia propor de boa-fé, que aquele princípio rejeitaria. Princípio para o qual você não consegue escrever essa mudança sai da lista.
