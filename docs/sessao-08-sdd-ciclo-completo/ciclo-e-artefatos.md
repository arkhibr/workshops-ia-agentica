# O ciclo e os quatro artefatos

Desenvolvimento guiado por especificação, ou SDD (*Spec-Driven Development*), inverte uma hierarquia antiga. Por décadas a especificação foi andaime: escrita, aprovada e descartada assim que o código, o "trabalho de verdade", começava. O SDD trata a especificação como o artefato que gera a implementação, e o código como uma das implementações possíveis daquela intenção. Esta página percorre os quatro artefatos canônicos e o que cada um decide.

## A ordem entre os artefatos

Cada artefato do ciclo remove um tipo diferente de incerteza, e a ordem existe porque remover na sequência errada custa retrabalho. Decidir o banco de dados antes de saber qual comportamento o usuário precisa significa escolher a solução antes de entender o problema. Escrever tarefas antes de ter critério de aceitação produz uma lista de atividades, não compromissos de comportamento verificáveis.

O [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit) nomeia cada etapa por um comando, o que torna a sequência observável: `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement` e `verify`. Os quatro primeiros artefatos são os canônicos, e os demais comandos operam sobre eles.

## Constitution

A constitution é um arquivo versionado no repositório com os princípios que toda mudança precisa respeitar. Ela existe para que decisões válidas para o projeto inteiro não sejam repetidas em cada pedido ao agente, e para impedir que ele trate convenção fundamental como preferência local.

A comparação que ajuda: a especificação diz o que **esta** mudança deve fazer, a constitution diz o que **nenhuma** mudança pode violar. Uma vale por funcionalidade, a outra vale até ser explicitamente alterada.

Um princípio só governa se for capaz de rejeitar alguma coisa. "Escreva código limpo" e "priorize segurança" não dizem o que fazer diante de um conflito, e por isso nunca barram nada. O teste é direto: se você não consegue imaginar uma mudança plausível que o princípio rejeitaria, ele é decoração. Princípios que funcionam têm consequência nomeada, do tipo "interface pública só muda com compatibilidade ou plano de migração, e quebrar contrato sem plano exige decisão registrada do dono do produto".

!!! question "Antes de continuar"
    Pense numa convenção que o seu time repete em toda revisão de código. Ela está escrita em algum lugar que o agente consegue ler, ou vive na memória de quem revisa?

## Spec

A especificação descreve comportamento observável, critérios de aceitação, limites, riscos e questões em aberto. O foco permanece no que o usuário passa a poder fazer e por que isso importa, evitando escolher prematuramente framework, banco ou estrutura interna.

A separação é deliberada. Misturar tecnologia na especificação torna a intenção instável: "o usuário baixa o relatório em CSV" é requisito, "o endpoint usa fila e armazenamento de objetos" pertence ao plano. Manter os dois separados permite comparar arquiteturas sem reescrever o problema, trocar tecnologia preservando critérios e revisar produto e arquitetura por autoridades diferentes.

Há exceção legítima: uma restrição tecnológica vira requisito quando vem do ambiente, como "deve operar desconectado" ou "não pode transferir dados para fora do país". Nesse caso, a restrição e sua origem entram na especificação, e o plano decide como atendê-la.

## Plan

O plano traduz a especificação em decisões técnicas: componentes, dados, contratos, integrações, migração, segurança, observabilidade e estratégia de teste. É a etapa em que tecnologia entra explicitamente.

O plano não repete requisitos em linguagem técnica. Ele mostra como cada decisão atende requisitos e atributos de qualidade, quais alternativas foram descartadas e onde há risco. Quando uma escolha merece existência independente, vira um registro de decisão arquitetural. Quando falta evidência para decidir, vira experimento com hipótese, método e critério de parada.

Em código existente, planejar começa por ler o sistema. O agente precisa identificar interfaces estáveis, convenções, testes e dependências antes de propor. Um plano que ignora os padrões do repositório cria uma segunda arquitetura imaginária, que convive mal com a primeira.

## Tasks

As tarefas decompõem o plano em unidades executáveis. Uma boa tarefa informa área, comportamento, teste, dependência e definição de pronto. "Implementar backend" não é tarefa. "Aceitar solicitação autorizada e persistir o estado pendente, com teste de contrato" é.

As melhores unidades são fatias verticais: atravessam o mínimo necessário de interface, regra, persistência e teste para demonstrar comportamento. A decomposição horizontal, que faz primeiro todas as tabelas, depois todas as APIs, depois todas as telas, acumula trabalho sem trajetória verificável. Depois de quatro de cinco tarefas horizontais, ninguém consegue usar nada, e o primeiro erro de contrato só aparece na quinta.

!!! tip "Aplique agora"
    Pegue a última tarefa que você escreveu num quadro de trabalho. Ela descreve um comportamento demonstrável de ponta a ponta, ou uma camada que só faz sentido quando as outras chegarem?

## Implement e verify

A implementação percorre as tarefas e produz código e testes. O agente implementador tem autonomia estreita: escolhe detalhes locais dentro das decisões aprovadas, mas pausa quando encontra ambiguidade que altera contrato, arquitetura ou risco.

O ciclo mínimo por fatia é escrever um teste que expresse o comportamento, executar e observar a falha correta, escrever o mínimo para passar, refatorar mantendo o teste verde, e comparar o resultado com a tarefa, o plano e a especificação. Gerar teste e código na mesma resposta sem observar a falha perde uma evidência importante, porque o teste pode estar confirmando comportamento que já existia ou reproduzindo o mesmo erro conceitual do código.

A verificação tem dois eixos independentes. **Aderência à especificação** pergunta se requisitos, critérios e limites foram respeitados. **Qualidade da implementação** pergunta se o código segue padrões, arquitetura, segurança e operabilidade do repositório. Misturar os dois num único "aprovado" permite que força em um esconda fraqueza no outro: uma implementação pode ser tecnicamente elegante e resolver a necessidade errada.

## Isso vira arquivo assim

Os quatro artefatos são arquivos de texto versionados junto do código, não documentos num sistema à parte. Um ciclo do Spec Kit deixa esta estrutura no repositório:

```text
.specify/
  memory/
    constitution.md          # princípios que toda mudança respeita
specs/
  001-faixa-atacado/
    spec.md                  # o quê e por quê, com FR-001, FR-002...
    plan.md                  # como, com as decisões técnicas
    tasks.md                 # fatias verticais, em ordem, com definição de pronto
```

O identificador numérico da pasta liga o conjunto a um ramo de trabalho, e é o que permite responder, meses depois, à pergunta "por que esta validação existe?" sem depender da memória de quem escreveu.

**Próxima página:** [Abordagens de SDD](abordagens-sdd.md).
