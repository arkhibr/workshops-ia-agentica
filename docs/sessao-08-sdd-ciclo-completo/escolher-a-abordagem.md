# Escolher a abordagem e a profundidade

Duas decisões diferentes costumam ser confundidas numa só. A primeira é qual abordagem de desenvolvimento guiado por especificação adotar, e depende do artefato que o time precisa preservar. A segunda é quanta cerimônia aplicar a uma mudança específica, e depende do risco dela. Uma organização pode acertar a primeira e ainda assim afundar na segunda, aplicando o pacote completo a toda correção de texto.

## Método, artefato, ferramenta e governança

Antes da comparação, uma distinção que evita confundir adoção com instalação:

- **método** é o conjunto de decisões sobre como o trabalho deve avançar.
- **artefato** é o registro durável de intenção, design, tarefas ou evidências.
- **ferramenta** instala comandos, modelos e automações que ajudam o agente a seguir o método.
- **governança** define quem aprova, quais portões são obrigatórios e o que acontece quando um portão falha.

Um agente pode preencher todos os modelos de uma ferramenta e ainda produzir uma especificação vaga. Na direção oposta, um time pode praticar SDD com arquivos de texto simples, desde que trate a especificação como contrato revisável e mantenha a disciplina de atualizá-la. A ferramenta acelera o método já escolhido.

## Comparação sob dez critérios

| Critério | OpenSpec | GitHub Spec Kit | SPDD | Superpowers |
|---|---|---|---|---|
| Natureza | fluxo de mudança orientado por especificação | conjunto extensível de comandos orientados por intenção | método com implementação de referência, centrado no prompt | conjunto de habilidades e metodologia de execução |
| Unidade principal | mudança | funcionalidade sob princípios de projeto | incremento descrito por um Painel REASONS | tarefa ou plano de implementação |
| Artefato central | especificação atual e delta da mudança | constitution, especificação, plano e tarefas | prompt ou Painel versionado | design, plano, código e testes |
| Relação com SDD | predominantemente *spec-anchored* | de *spec-first* a *spec-anchored* | *spec-anchored* com sincronização nos dois sentidos | adjacente, disciplina a execução de uma spec externa |
| Governança transversal | não é o padrão, mas pode ser customizada | constitution e checagens explícitas | normas e salvaguardas dentro do Painel | regras do fluxo, sem constitution de domínio |
| Manutenção da intenção | deltas sincronizados na especificação principal | depende do uso contínuo dos artefatos | atualização nos dois sentidos entre prompt e código | documentos por mudança, testes sustentam o comportamento |
| Estratégia de verificação | validação de artefatos e verificação da implementação | checklist, análise cruzada e convergência | revisões do Painel, da interface e do código | TDD, revisão em duas etapas e verificação antes de concluir |
| Custo dominante | manter deltas e especificação consolidada coerentes | produzir e governar uma cadeia maior de artefatos | modelagem detalhada e experiência sênior antecipada | disciplina operacional e testabilidade da base |
| Melhor encaixe | produto longevo com mudanças incrementais | múltiplos times e políticas compartilhadas | lógica complexa, repetição e restrições fortes | execução confiável em bases testáveis |
| Falha típica | arquivar sem sincronizar | constitution genérica e aprovação mecânica | Painel detalhado sobre premissa errada | teste confirmar interpretação incompleta |

Duas conclusões dessa tabela merecem atenção, porque contrariam a intuição.

A primeira é que **documentação e rigor operacional são eixos diferentes**. O Spec Kit pode ser pesado em documento e leve em exigência de execução. O Superpowers é o inverso. Dizer que uma abordagem é "leve" ou "pesada" sem dizer em qual eixo esconde onde o custo aparece de verdade.

A segunda é que as abordagens podem ser combinadas. Uma organização pode usar a constitution do Spec Kit para princípios transversais, o delta do OpenSpec para manter o comportamento do domínio legível, e a disciplina de teste e verificação do Superpowers na execução. Combinar dessa forma exige reconhecer que são camadas distintas e evitar que dois artefatos disputem a mesma decisão. Instalar as três ferramentas juntas resolve pouco.

!!! question "Antes de continuar"
    Qual artefato do seu projeto atual precisa sobreviver mais tempo: a intenção do produto, os princípios de engenharia, ou a evidência de que a mudança funciona? A resposta indica qual abordagem encaixa melhor.

## A régua de profundidade proporcional

Escolhida a abordagem, resta calibrar quanta cerimônia cada mudança recebe. Aplicar o mesmo pacote a toda alteração transforma o método em fila de aprovação. Aplicar só a mudanças grandes deixa riscos pequenos e frequentes se acumularem.

Três classes resolvem a maior parte dos casos:

| Classe | Situação | Contrato mínimo |
|---|---|---|
| S, localizada | comportamento conhecido, baixo alcance, reversível | problema, teste de regressão, diferença e revisão |
| M, funcionalidade | comportamento novo, mais de um componente ou decisão | especificação, critérios, plano, fatias e testes |
| L, iniciativa | múltiplos domínios, migração, risco material ou vários times | constitution aplicável, especificação, plano, decisões registradas e portões |

A classificação é pelo maior risco, não pelo número de linhas. Corrigir um texto de interface em três telas é classe S, porque não há regra associada e o retorno é trivial. Permitir que o cliente cancele um pedido até a separação começar é classe L, mesmo sendo poucas linhas, porque a regra de cancelamento hoje só existe no código e ninguém sabe recitá-la. Migrar duzentos arquivos para um formato novo é classe M apesar do tamanho, porque a transformação é mecânica e reversível arquivo a arquivo.

A segunda é a que mais se subestima. Uma linha que altera autorização carrega mais risco do que duzentos arquivos que mudam formato.

## Cinco perguntas que definem a classe

A Sessão 1 apresentou os critérios de escolha entre vibe coding, assistência de codificação e SDD. As mesmas cinco perguntas calibram a profundidade dentro do SDD:

1. **Reversibilidade.** Se a decisão estiver errada, dá para descartar sem migração de dados, indisponibilidade ou quebra de contrato?
2. **Tempo de vida esperado.** O código será usado por horas, por um ciclo, ou por anos?
3. **Número de futuros mantenedores.** A conversa original estará acessível para quem precisar alterar o sistema depois?
4. **Criticidade da regra.** O comportamento envolve dinheiro, identidade, autorização, privacidade ou obrigação regulatória?
5. **Familiaridade com o sistema.** A mudança ocorre em projeto novo ou em base madura, com restrições que não estão todas documentadas?

Uma resposta que aponta risco alto obriga a cobrir aquele risco específico, sem obrigar a adotar a ferramenta mais pesada. Uma alteração irreversível num serviço pequeno pede plano de migração rigoroso, e costuma dispensar uma constitution de projeto.

!!! tip "Aplique agora"
    Classifique como S, M ou L as três últimas mudanças que você entregou. Registre o motivo de cada classificação em uma linha. Se alguma classificação depender do tamanho da diferença em vez do risco, reclassifique.

**Próxima página:** [Manter os artefatos vivos](artefatos-vivos.md).
