# Estudo de caso

**Tempo:** 15 min · **Formato:** 8 min em grupos de 3–4 pessoas, 7 min de plenária.

Na Vetor, parte de uma alteração se perdeu num conflito entre dois agentes, e a decisão em aberto é se o time passa a exigir isolamento por ramo em toda tarefa.

## Situação

Dois desenvolvedores da Vetor, empresa fictícia de e-commerce B2B usada nos exemplos deste workshop, usaram o agente ao mesmo tempo no mesmo diretório de trabalho, sem worktree separado. Um corrigia o cálculo de desconto, e o outro ajustava a mesma função para adicionar um log de auditoria. Os dois agentes leram o arquivo antes de o outro salvar, e a edição de um sobrescreveu silenciosamente parte da edição do outro. O bug só apareceu dias depois, em produção, quando o log de auditoria simplesmente não aparecia em alguns pedidos.

Na reunião de retrospectiva, uma pessoa sugere: "vamos exigir que todos usem worktree separado a partir de agora, para qualquer tarefa, mesmo pequena." Outra pessoa acha exagero: "isso só aconteceu porque os dois mexeram no mesmo arquivo ao mesmo tempo, é raro, basta avisar no chat quando for mexer em algo compartilhado."

![Linha do tempo de duas edições concorrentes: dois agentes leem a mesma versão, aplicam mudanças diferentes no mesmo diretório, uma sobrescrita silenciosa remove o log de auditoria e a falha aparece dias depois em produção. O diagrama separa contexto da conversa de estado em disco e mantém abertas duas políticas para decisão do grupo.](../assets/images/s2-commit-que-sumiu.png)

## Como usar este estudo de caso

O caso não tem resposta única e serve para praticar o critério da tabela de [O ambiente compartilhado](ambiente-compartilhado.md#quando-vale-configurar-um-ambiente-compartilhado) numa situação ambígua.

## Perguntas para orientar a análise

1. O incidente veio da falta de isolamento por ramo, ou de dois desenvolvedores editarem a mesma função sem se comunicar? A segunda causa aconteceria mesmo sem agente nenhum envolvido.
2. Exigir worktree para toda tarefa, mesmo as pequenas e solo, resolve esse problema específico ou cria overhead para casos que nunca tiveram esse risco?
3. Que critério objetivo o time da Vetor poderia adotar para decidir quando o isolamento por ramo é obrigatório? "Seja mais cuidadoso" não conta como critério.
4. O `AGENTS.md` da Vetor poderia ter evitado esse problema? Por quê ou por que não?

## Depois da discussão

Compare a posição do grupo com o critério de "tamanho do time" e "frequência de uso" da tabela de [O ambiente compartilhado](ambiente-compartilhado.md#quando-vale-configurar-um-ambiente-compartilhado). A Sessão 5, sobre decomposição, volta a esse tipo de conflito com uma ferramenta mais precisa: dividir o trabalho em tarefas atômicas de fronteira clara, para que dois agentes raramente precisem tocar o mesmo arquivo ao mesmo tempo.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
