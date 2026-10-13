# Qualidade da spec: clarify e checklist

Esta página trata dos dois comandos opcionais do GitHub Spec Kit que atuam sobre a spec antes das tarefas: o `clarify`, que leva ao dono da regra as lacunas que a spec ainda tem, e o `checklist`, que avalia se os requisitos estão bem escritos. A Sessão 5 percorreu o caminho básico da ferramenta, em que a spec gerada pelo agente segue direto para o plano, e esta página trata do que pode ser verificado nesse intervalo.

## Onde os comandos opcionais entram

Ao terminar o `specify init`, a versão 1.1.1 imprime dois painéis. O painel *Next Steps* lista o caminho básico com seis comandos: os cinco que a Sessão 5 usou e o `converge`, que avalia o código existente para acrescentar as tarefas que faltam e por isso fica fora deste workshop. O painel *Enhancement Skills* lista três comandos marcados como opcionais, cada um com a posição em que deve rodar.

![Diagrama intitulado Comandos opcionais do Spec Kit 1.1.1: onde cada um entra no fluxo. Uma linha de seis caixas ligadas por setas mostra o caminho básico: constitution, com os princípios, specify, que grava spec.md, plan, que grava plan.md e documentos de apoio, tasks, que grava tasks.md, implement, que produz código e testes, e converge, em cinza, com a nota tarefas restantes, fora do workshop. Três caixas tracejadas em laranja mostram os comandos opcionais. Acima, clarify faz até 5 perguntas ao PO, uma por vez, altera spec.md e aponta para o intervalo entre specify e plan. Acima, analyze confere spec, plan e tasks contra a constitution, não altera nenhum arquivo e aponta para o intervalo entre tasks e implement. Abaixo, checklist testa a escrita dos requisitos, com itens CHK, cria a pasta checklists e aponta para o intervalo entre plan e tasks. Uma linha tracejada vermelha liga o checklist ao implement, com o rótulo trava: item não marcado, o implement para e pergunta. Uma faixa inferior diz que o clarify altera a spec, o checklist cria um arquivo próprio e o analyze não altera nenhum arquivo do projeto.](assets/opcionais-no-fluxo.png)

| Comando | Posição | O que examina | O que grava |
|---|---|---|---|
| `clarify` | depois do `specify`, antes do `plan` | a spec, em busca de decisões ainda em aberto | respostas dentro da própria `spec.md` |
| `checklist` | depois do `plan` | a escrita dos requisitos, contra spec, plano e constitution | um arquivo novo em `checklists/` |
| `analyze` | depois do `tasks`, antes do `implement` | a coerência entre spec, plano e tarefas | nenhum arquivo |

Os três comandos são opcionais no sentido de que o fluxo roda sem eles. O que eles acrescentam é uma leitura feita por quem não escreveu o artefato, já que cada um examina o que os comandos anteriores gravaram, e o `analyze` fica para a página de conceitos do Tema 2, junto com o teste antes do código.

## Clarify

O `clarify` lê a spec da funcionalidade em andamento e classifica cada categoria de ambiguidade como clara, parcial ou ausente. As instruções que o `specify init` instala para o comando (`.claude/skills/speckit-clarify/SKILL.md`, no Claude Code) listam as categorias: escopo e comportamento, modelo de dados, fluxos de usuário, requisitos não funcionais, integrações, casos de borda, restrições técnicas, terminologia, critérios de aceite e marcadores pendentes na spec.

A partir dessa varredura, o comando monta uma fila de no máximo cinco perguntas e as apresenta uma de cada vez. Cada pergunta traz uma frase sobre o que muda na aceitação ou na entrega, uma opção recomendada pelo agente com a justificativa e uma tabela de alternativas. A resposta pode ser a letra da opção, a palavra "yes" para aceitar a recomendação ou uma resposta curta. Depois de cada resposta, o agente cria ou atualiza uma seção `## Clarifications` na spec, com a pergunta e a resposta da sessão, e reescreve os requisitos, cenários e suposições afetados.

A Sessão 3 apresentou a [intervenção socrática](../sessao-03-exploracao-especificacao/intervencao-socratica-conceitos.md#uma-pergunta-por-mensagem-cinco-fases-seis-categorias), com um contrato de três partes: uma pergunta por mensagem, sem sugerir a resposta, e solução técnica deixada para depois. O `clarify` cumpre a primeira e a terceira partes e descumpre a segunda por desenho, já que toda pergunta vem com a opção que o agente considera certa. A recomendação reduz o esforço de quem responde e traz o risco de que a decisão de negócio volte ao agente sem que ninguém perceba.

O antipadrão correspondente é responder "yes" a todas as perguntas. Cada aceitação sem leitura grava na spec, como resposta do PO, uma decisão tomada pelo agente, e a seção `## Clarifications` passa a dar aparência de validação a algo que ninguém validou. A pergunta que deve ser feita diante de cada recomendação é se quem responde tem autoridade sobre aquela regra e se a opção recomendada altera o que o pedido original dizia.

O limite principal do comando está no ponto de partida da varredura. O `clarify` pergunta sobre o que considera parcial ou ausente na spec, e pode tratar como resolvida uma decisão que o `specify` já registrou como suposição ou como item fora do escopo. O comportamento varia de uma execução para outra: no ensaio de 13/10/2026, o `clarify` perguntou sobre uma suposição que o `specify` tinha pedido para confirmar e não perguntou sobre outras duas, a reprovação, declarada fora do escopo, e a definição de quem pode aprovar, registrada como suposição. Por isso a leitura das seções de suposições e de escopo continua necessária depois do `clarify`, e é nela que aparecem as decisões que o agente tomou sem perguntar.

## Checklist

As instruções do `checklist` definem o comando como "testes de unidade para o inglês": se a spec é código escrito em língua natural, o checklist é a suíte de testes dela. Cada item avalia se um requisito está completo, claro, coerente e mensurável, e nenhum item verifica se o código funciona. "Verificar se o botão responde ao clique" está fora do escopo do comando, e "a spec define o que acontece quando dois aprovadores agem ao mesmo tempo" está dentro.

O comando recebe um foco em texto livre, pode fazer até três perguntas para delimitá-lo e grava um arquivo em `checklists/` com itens numerados a partir de `CHK001`. Cada item cita a seção de origem ou recebe uma marcação como `[Gap]`, `[Ambiguity]` ou `[Conflict]`, o que permite ir do item ao trecho da spec que ele questiona. O comando nunca marca um item como `[x]`, porque a marcação registra a decisão de quem revisa que aquele critério foi atendido.

O arquivo `checklists/requirements.md`, criado pelo próprio `specify`, é diferente dos arquivos que o `checklist` gera. Ele é mantido pelo `specify` e pelo `clarify` e verifica a forma da spec, como a ausência de marcadores pendentes e de detalhes de implementação. Os arquivos do `checklist` pertencem a quem revisa os requisitos e examinam o conteúdo de um domínio escolhido.

## A trava do implement

O `implement` lê todos os arquivos de `checklists/` antes de executar qualquer tarefa. Se algum item estiver desmarcado, o comando mostra uma tabela com o total de itens marcados e desmarcados em cada arquivo e para com a pergunta se a implementação deve seguir assim mesmo, que aceita "sim" para liberar a execução e "não" para interrompê-la sem alterar nenhum arquivo.

A trava liga a revisão dos requisitos à execução: um checklist gerado e nunca lido aparece no momento de implementar como uma lista de itens em aberto. Responder "sim" é uma decisão legítima quando os itens desmarcados não afetam a história em curso, desde que a pessoa tenha lido quais são esses itens antes de responder.

**Próxima página:** [Exemplo de aplicação de IA](qualidade-da-spec-exemplo-de-aplicacao-de-ia.md).
