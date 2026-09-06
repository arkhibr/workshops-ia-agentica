# Isolamento por ramo

Duas sessões de agente no mesmo diretório de trabalho disputam os mesmos arquivos, e o resultado aparece como trabalho que some. O que o `git worktree` isola, e o cuidado que ele exige.

## Isolamento de contexto por ramo

A última peça é operacional: o que acontece quando duas pessoas, ou a mesma pessoa em duas tarefas, usam um agente ao mesmo tempo no mesmo repositório. Sem isolamento, os dois agentes leem e escrevem no mesmo diretório de trabalho — um pode sobrescrever a edição do outro, ou um terminar de ler arquivos que o outro está no meio de alterar.

O git worktree resolve isso na camada de sistema de arquivos, não de configuração de agente: cada worktree é um diretório de trabalho separado, apontando para o mesmo repositório, cada um numa branch diferente. Um agente trabalhando num worktree não vê, e não pode corromper, o que outro agente está fazendo no worktree paralelo. Isso separa dois problemas que costumam ser confundidos: contexto de conversa (o que o agente lembra) e estado do sistema de arquivos (o que existe em disco). O segundo pode ser isolado mesmo quando o primeiro continua específico de cada sessão.

Na prática, isolar duas sessões é um comando de git, repetido uma vez por tarefa:

```bash
git worktree add ../repo-tarefa-a -b tarefa/a
git worktree add ../repo-tarefa-b -b tarefa/b
```

Cada comando cria um diretório de trabalho novo, numa branch nova, apontando para o mesmo repositório. Fechar a aba de um chat com o agente não desfaz nada em disco; remover o worktree (`git worktree remove ../repo-tarefa-a`) sim. É por isso que os dois problemas pedem soluções diferentes, mesmo aparecendo juntos no mesmo incidente.

!!! question "Antes de continuar"
    Pense na última vez que dois agentes (ou duas pessoas usando IA) mexeram no mesmo repositório ao mesmo tempo. Alguém percebeu um conflito antes ou depois de acontecer?

## Um cuidado prático com isolamento por ramo

Cada worktree é um diretório de trabalho completo, mas não duplica automaticamente tudo que um projeto precisa para rodar. O histórico do git é compartilhado entre todos os worktrees do mesmo repositório; a pasta de dependências instaladas, não. Um `npm install` rodado num worktree não aparece no outro — cada worktree novo precisa da própria instalação, ou de um link simbólico para uma pasta de dependências compartilhada fora do controle do git.

Isso muda o cálculo de quando vale isolar por ramo: se criar um worktree novo significa esperar alguns minutos de instalação antes de começar a tarefa de verdade, a fricção desestimula o hábito exatamente nos casos em que ele mais evitaria um incidente como o do [Estudo de caso](estudo-de-caso.md). Times que isolam por ramo com frequência costumam automatizar esse passo num script simples, que cria o worktree e já deixa o ambiente pronto para o agente trabalhar.

**Próxima página:** [Autonomia e supervisão](autonomia-e-supervisao.md).
