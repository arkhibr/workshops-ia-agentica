# Estudo de caso: o commit que sumiu

**Tempo:** 15 min · **Formato:** 8 min em grupos de 3–4 pessoas, 7 min de plenária.

## Situação

Dois desenvolvedores da Vetor, plataforma fictícia de e-commerce B2B usada como caso desta sessão, usaram o agente ao mesmo tempo no mesmo diretório de trabalho, sem worktree separado. Um estava corrigindo o cálculo de desconto; o outro, ajustando a mesma função para adicionar um log de auditoria. Os dois agentes leram o arquivo antes de o outro salvar, e a edição de um sobrescreveu silenciosamente parte da edição do outro. O bug só apareceu dias depois, em produção, quando o log de auditoria simplesmente não aparecia em alguns pedidos.

Na reunião de retrospectiva, uma pessoa sugere: "vamos exigir que todo mundo use worktree separado a partir de agora, para qualquer tarefa, mesmo pequena." Outra pessoa acha exagero: "isso só aconteceu porque os dois mexeram no mesmo arquivo ao mesmo tempo, é raro, basta avisar no chat quando for mexer em algo compartilhado."

![Linha do tempo de duas edições concorrentes: dois agentes leem a mesma versão, aplicam mudanças diferentes no mesmo diretório, uma sobrescrita silenciosa remove o log de auditoria e a falha aparece dias depois em produção. O diagrama separa contexto da conversa de estado em disco e mantém abertas duas políticas para decisão do grupo.](../assets/images/s2-commit-que-sumiu.png)

## Como usar este estudo de caso

Não existe uma resposta única aqui. O objetivo é praticar o critério da tabela de [Padrões e decisões](padroes-e-decisoes.md#quando-vale-configurar-um-ambiente-compartilhado) num caso ambíguo de verdade.

## Perguntas para orientar a análise

1. O incidente foi causado pela ausência de isolamento por ramo, ou por dois desenvolvedores editarem a mesma função sem se comunicar — algo que aconteceria mesmo sem agente nenhum envolvido?
2. Exigir worktree para toda tarefa, mesmo as pequenas e solo, resolve esse problema específico ou cria overhead para casos que nunca tiveram esse risco?
3. Que critério objetivo (não "seja mais cuidadoso") o time da Vetor poderia adotar para decidir quando o isolamento por ramo é obrigatório?
4. O `AGENTS.md` da Vetor poderia ter evitado esse problema? Por quê ou por que não?

## Depois da discussão

Compare a posição do grupo com o critério de "tamanho do time" e "frequência de uso" da tabela de Padrões e decisões. A Sessão 5 (Decomposição) volta a esse mesmo tipo de conflito com uma ferramenta mais precisa: dividir o trabalho em tarefas atômicas com fronteiras claras, reduzindo a chance de dois agentes precisarem tocar o mesmo arquivo ao mesmo tempo.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
