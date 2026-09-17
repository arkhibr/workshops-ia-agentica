# Isolamento por ramo

Duas sessões de agente no mesmo diretório de trabalho disputam os mesmos arquivos, e o resultado aparece como trabalho que some. Aqui você vê o que o `git worktree` isola e o cuidado que ele exige.

## O que o worktree isola

A última peça do ambiente é operacional. Pense no que acontece quando duas pessoas, ou a mesma pessoa em duas tarefas, usam um agente ao mesmo tempo no mesmo repositório. Sem isolamento, os dois agentes leem e escrevem no mesmo diretório de trabalho. Um sobrescreve a edição do outro, ou lê pela metade um arquivo que o outro está alterando.

O git worktree resolve isso na camada de sistema de arquivos, sem depender de nenhuma configuração do agente. Cada worktree é um diretório de trabalho separado, apontando para o mesmo repositório, cada um numa branch diferente. Um agente trabalhando num worktree não vê, e não pode corromper, o que outro agente está fazendo no worktree paralelo. Isso separa dois problemas que as pessoas costumam confundir: o contexto da conversa, que é o que o agente lembra, e o estado do sistema de arquivos, que é o que existe em disco. Você consegue isolar o segundo mesmo quando o primeiro continua específico de cada sessão.

Na prática, isolar duas sessões é um comando de git, repetido uma vez por tarefa:

```bash
git worktree add ../repo-tarefa-a -b tarefa/a
git worktree add ../repo-tarefa-b -b tarefa/b
```

Cada comando cria um diretório de trabalho novo, numa branch nova, apontando para o mesmo repositório. Fechar a aba de um chat com o agente não desfaz nada em disco. Remover o worktree (`git worktree remove ../repo-tarefa-a`) desfaz. É por isso que os dois problemas pedem soluções diferentes, mesmo aparecendo juntos no mesmo incidente.

!!! question "Antes de continuar"
    Pense na última vez que dois agentes (ou duas pessoas usando IA) mexeram no mesmo repositório ao mesmo tempo. Alguém percebeu um conflito antes ou depois de acontecer?

## Um cuidado prático com isolamento por ramo

Cada worktree é um diretório de trabalho completo, mas não duplica automaticamente tudo que um projeto precisa para rodar. O histórico do git é compartilhado entre todos os worktrees do mesmo repositório, mas a pasta de dependências instaladas fica em cada um. Um `npm install` rodado num worktree não aparece no outro. Cada worktree novo precisa da própria instalação, ou de um link simbólico para uma pasta de dependências compartilhada fora do controle do git.

Isso muda a conta de quando vale isolar por ramo. Se criar um worktree custa alguns minutos de instalação antes de começar a tarefa de verdade, ninguém cria, justamente nos casos em que o worktree mais evitaria um incidente como o do [Estudo de caso](estudo-de-caso.md). Times que isolam por ramo com frequência automatizam esse passo num script simples, que cria o worktree e já deixa o ambiente pronto para o agente trabalhar.

**Próxima página:** [Autonomia e supervisão](autonomia-e-supervisao.md).
