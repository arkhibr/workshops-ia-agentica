# Do plano ao código: plan, tasks e implement

Esta página cobre a segunda metade do caminho básico do GitHub Spec Kit, ferramenta que conduz o agente de codificação por artefatos versionados em ordem fixa. Depois da constitution e da spec, três comandos levam ao código: `plan` decide a tecnologia, `tasks` decompõe o trabalho e `implement` executa. O assunto central é a decomposição, porque é nela que o humano decide onde vai intervir.

## O plano

O plano é o primeiro artefato em que a tecnologia aparece. O template da versão 1.1.1 pede três blocos:

| Bloco | Conteúdo | O que conferir |
|---|---|---|
| *Technical Context* | Linguagem, dependências, ferramenta de teste, plataforma, restrições | Bate com o que você informou no comando, sem acréscimos |
| *Constitution Check* | Cada princípio da constitution confrontado com o desenho | Cada linha traz evidência, além da marca de aprovado |
| *Project Structure* | Os arquivos que serão criados ou alterados | Nenhum arquivo existente aparece sem motivo |

Conforme o caso, o `plan` também gera documentos de apoio na mesma pasta: `research.md` com as decisões técnicas e as alternativas descartadas, `data-model.md`, `contracts/` e `quickstart.md`, um roteiro para verificar a feature à mão. Numa mudança pequena, esses documentos somam mais linhas que o código que vão produzir. Leia o *Constitution Check* e a lista de arquivos, e consulte o resto quando o plano tomar uma decisão que você não esperava.

O *Constitution Check* é declarado no template como portão: o desenho só segue se passar. Um portão preenchido só com marcas de aprovado não verificou nada. A versão útil diz como o desenho cumpre cada princípio, por exemplo listando qual teste cobre cada requisito.

## Tarefa atômica e tarefa composta

Uma **tarefa atômica** produz uma mudança que um comando verifica, cabe numa execução do agente sem que ele precise pedir uma decisão e tem critério de aceitação próprio. Uma **tarefa composta** junta mais de uma decisão ou mais de uma verificação, e por isso só pode ser julgada como um todo, depois de pronta.

O tamanho certo de uma tarefa depende de quem a executa. [Kwa et al. (2025)](../referencia/bibliografia.md#kwa-et-al-measuring-ai-ability-to-complete-long-software-tasks-2025), do METR, medem a capacidade de um agente pelo tempo que um humano leva para fazer as tarefas que o agente completa com 50% de sucesso. Em março de 2025, esse horizonte era de cerca de 50 minutos para o melhor modelo avaliado, e vinha dobrando a cada sete meses desde 2019. A taxa de sucesso cai à medida que a tarefa cresce, então uma tarefa composta grande demais falha mais, e falha num ponto que ninguém revisou.

Decompor demais também custa. [Prasad et al. (2024)](../referencia/bibliografia.md#prasad-et-al-adapt-as-needed-decomposition-and-planning-2024) mostram, com o método ADaPT, que decompor só quando o executor não consegue fazer a tarefa inteira supera tanto a execução direta quanto o plano fixo decomposto de antemão. No Spec Kit, a decomposição é feita uma vez, antes da execução, e vale a pena calibrá-la: uma tarefa que só manda rodar um comando e conferir a saída consome uma linha de plano e uma rodada de atenção sem decidir nada.

Para decidir onde cortar, o critério mais antigo continua valendo. [Parnas (1972)](../referencia/bibliografia.md#parnas-on-the-criteria-to-be-used-in-decomposing-systems-into-modules-1972) propôs dividir um sistema em módulos pelas decisões que provavelmente vão mudar, cada módulo escondendo uma delas. Aplicado a tarefas, o corte segue as regras de negócio: uma tarefa por regra, com o ID da regra no nome do teste. Quando a regra mudar, a tarefa que a implementou é encontrada por busca.

## Anatomia do `tasks.md`

O template organiza as tarefas em fases e dá a cada tarefa um formato fixo, `[ID] [P?] [Story] Descrição`:

| Elemento | Significado |
|---|---|
| `T001`, `T002`... | Identificador sequencial, na ordem de execução |
| `[P]` | Pode rodar em paralelo: arquivo diferente e nenhuma dependência pendente |
| `[US1]`, `[US2]`... | A história de usuário da spec a que a tarefa pertence |
| *Setup* e *Foundational* | Fases que preparam o terreno, antes de qualquer história |
| Uma fase por história | Na ordem de prioridade da spec, cada uma testável sozinha |
| *Polish* | Ajustes que atravessam histórias |
| `**Checkpoint**` | Linha no fim de cada fase dizendo o que precisa estar funcionando |

![Diagrama intitulado Anatomia do tasks.md: formato da tarefa, fases e paradas humanas. No alto, a tarefa T005 [P] [US1] Escrever o teste da RN-11, com cada parte rotulada: T005 é a ordem de execução, [P] indica que pode rodar em paralelo, [US1] é a história da spec e o resto é a descrição. Uma nota diz que não há campo de critério por tarefa e que a pergunta de revisão é qual comando prova que ela terminou. No meio, cinco fases em sequência, cada uma terminando numa barra de checkpoint: Setup, com T001 preparar o ambiente; Foundational, com T002 alterar módulo existente, marcada com o número 1, e T003 [P] validar entrada; US1 (P1), MVP, com T004 escrever o teste, T005 ver o teste falhar e T006 implementar; US2 (P2), com T007 escrever o teste, T008 ver o teste falhar e T009 implementar, com decisão fora da spec, marcada com o número 3; e Polish, com T010 verificação final. Uma barra vertical laranja com o número 2 separa US1 de US2. A legenda inferior explica os três pontos de parada humana: 1, antes de uma tarefa que altera código existente; 2, depois da primeira fatia completa, o MVP; 3, em tarefa cuja descrição contém uma decisão que a spec não tomou. Os demais checkpoints ficam com o agente, que só interrompe a execução quando uma tarefa falha.](assets/anatomia-tasks.png)

O template declara as tarefas de teste como *OPTIONAL*, incluídas "só se pedidas na especificação". Sem um princípio na constitution que exija testes, o `tasks.md` pode sair sem nenhum. Com o princípio, cada história ganha tarefas de escrever o teste, ver o teste falhar e só então implementar.

A rastreabilidade do template vai até a história, pelo rótulo `[US1]`. A ligação com o requisito funcional e com a regra de origem só aparece se a constitution exigir, como na página anterior.

## Critério de aceitação por tarefa

O template tem um campo de teste por história (*Independent Test*), mas nenhum campo por tarefa. O critério de cada tarefa fica implícito na descrição, quando fica. Ao revisar um `tasks.md`, a pergunta a fazer para cada tarefa é qual comando prova que ela terminou.

Um critério só serve se puder falhar. Um teste que já passa antes da implementação não distingue o código pronto do código ausente, e a tarefa que ele verifica pode ser marcada como concluída sem ter sido feita. É por isso que o ciclo de teste antes do código inclui o passo de ver o teste falhar, e é por isso que uma tarefa do tipo "rodar `npm test` e confirmar a falha" tem valor: ela prova que o critério da tarefa seguinte discrimina.

## Pontos de controle humano

O checkpoint do template marca o fim de uma fase. Ele diz ao agente o que verificar antes de seguir, e a instrução do `implement` manda validar cada fase antes da próxima. Quem valida é o próprio agente, que só interrompe a execução quando uma tarefa falha.

No modo básico, um único `/speckit-implement` executa o `tasks.md` inteiro. Para intervir no meio, use o argumento do comando, que aceita orientação ou filtro de tarefas: `/speckit-implement execute só a fase 3 e pare`. Revise o diff, rode os testes, faça o commit e chame a fase seguinte.

![Diagrama intitulado implement em etapas: o argumento do comando cria a parada humana. Na faixa superior, Modo básico: uma chamada de /speckit-implement leva a uma caixa que diz que o agente executa o tasks.md inteiro, valida cada checkpoint sozinho e só para quando uma tarefa falha. Na faixa inferior, Em etapas: cinco caixas em sequência. As duas primeiras são etapas do agente: 1, /speckit-implement execute só a fase 3 e pare; 2, o agente executa as tarefas da fase e valida o checkpoint. As três seguintes são pontos de controle humano: 3, o humano revisa o que a fase mudou com git diff --stat; 4, o humano roda os testes com npm test; 5, o humano registra a fase aprovada com git commit. Uma seta tracejada volta da caixa 5 para a caixa 1, com o rótulo chama a fase seguinte.](assets/implement-em-etapas.png)

Os pontos que merecem parada humana são três: antes de uma tarefa que altera código existente, depois da primeira fatia completa (o MVP que o template marca com 🎯) e em qualquer tarefa cuja descrição contenha uma decisão que a spec não tomou. Os demais checkpoints podem ficar com o agente.

**Próxima página:** [Exemplo de aplicação de IA](do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md).
