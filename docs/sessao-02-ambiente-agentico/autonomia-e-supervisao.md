# Autonomia e supervisão

Quanto o agente decide sozinho é uma configuração do ambiente, e você escolhe por tarefa. Adiante estão o vocabulário dos níveis de autonomia e o critério para liberar cada um.

## O que o ambiente deixa o agente decidir sozinho

As quatro peças anteriores decidem o que o agente sabe e a que ele tem acesso. Falta uma decisão que nenhuma delas cobre: quanto ele decide e executa sozinho antes de alguém olhar. Essa decisão também vive no ambiente. O mesmo modelo, no mesmo repositório, trabalha sob supervisão apertada ou com autonomia ampla, dependendo de como a aplicação agêntica foi configurada para aquela sessão.

A maioria das aplicações agênticas de codificação oferece pelo menos três posições nesse espectro:

- **Perguntar antes de cada ação.** O agente propõe, e o humano aprova cada edição ou comando antes de executar.
- **Aprovar edições automaticamente.** Só comandos com efeito fora do repositório, como rede ou banco de dados, ainda pedem confirmação.
- **Autonomia ampla dentro de um ambiente isolado**, como um worktree descartável, onde o risco de um erro é menor porque o raio de impacto está contido.

Isso liga direto ao princípio de simplicidade da Sessão 1. A [Anthropic recomenda](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) testar bastante em ambiente controlado, com salvaguardas, antes de liberar autonomia total em produção. Autonomia ampla sem o isolamento correspondente é o cenário que o guia desaconselha, porque um erro numa etapa atravessa as seguintes sem ninguém ver.

A aritmética do erro composto, em [O arnês do agente](arnes.md#a-aritmetica-do-erro-composto), dá tamanho a esse risco. Numa trajetória de vinte etapas, 99% de acerto por etapa deixa a tarefa inteira em 81,8%. Por isso autonomia ampla pede isolamento e verificação, em vez de confiança no modelo.

Algumas aplicações agênticas vão além do modo de permissão e oferecem *hooks*: pontos de interceptação que rodam antes ou depois de o agente executar uma ferramenta, e podem bloquear a ação, registrar um log, ou pedir confirmação extra para comandos específicos, por exemplo qualquer comando que toque um arquivo de credenciais ou qualquer push direto para a branch principal. Um *hook* não substitui o arquivo de instrução, nem o MCP. O AGENTS.md documenta a convenção esperada. O hook aplica um limite na camada de execução, que continua valendo mesmo se o agente ignorar a convenção documentada.

!!! tip "Aplique agora"
    No ambiente que você usa hoje, o agente pede confirmação antes de cada ação, ou já roda edições automaticamente? Isso foi uma decisão deliberada, calibrada pelo risco da tarefa, ou é só o padrão de fábrica que ninguém revisitou?

## Quanto de autonomia liberar

Decida os níveis descritos em [O que o ambiente deixa o agente decidir sozinho](#o-que-o-ambiente-deixa-o-agente-decidir-sozinho) caso a caso, em vez de fixar um só para o time inteiro. Três perguntas ajudam:

- A ação é fácil de reverter (editar um arquivo ainda não commitado) ou difícil (enviar um e-mail, fazer uma implantação, apagar dado em produção)? Ação fácil de reverter aceita mais autonomia. Ação difícil de reverter pede confirmação antes de executar.
- O agente está rodando dentro de um ambiente isolado, como um worktree ou um contêiner descartável, ou direto no ambiente de produção? Isolamento reduz o raio de impacto de um erro, o que justifica liberar mais autonomia dentro dele.
- A tarefa se repete todo dia, do mesmo jeito? Se sim, vale configurar um *hook* uma vez, em vez de repetir a mesma confirmação manual centenas de vezes.

!!! tip "Aplique agora"
    Pense na última vez que um agente fez algo que você não esperava. A ação era fácil de reverter? Se não era, o nível de autonomia configurado hoje provavelmente está alto demais para aquele tipo de tarefa.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
