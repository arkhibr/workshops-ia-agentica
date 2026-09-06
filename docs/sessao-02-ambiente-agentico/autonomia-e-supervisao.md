# Autonomia e supervisão

Quanto o ambiente deixa o agente decidir sozinho é uma configuração, e ela se decide por tarefa. O vocabulário dos níveis de autonomia, e o critério para liberar cada um.

## Autonomia e supervisão: o que o ambiente deixa o agente decidir sozinho

As quatro peças anteriores decidem o que o agente sabe e a que ele tem acesso. Falta uma decisão diferente, que nenhuma delas cobre: quanto o agente decide e executa sozinho antes de um humano olhar. Essa decisão também é uma propriedade do ambiente, não do modelo: o mesmo modelo, no mesmo repositório, pode operar sob supervisão apertada ou com autonomia ampla, dependendo de como a aplicação agêntica foi configurada para aquela sessão.

A maioria das aplicações agênticas de codificação oferece pelo menos três posições nesse espectro: perguntar antes de cada ação, em que o agente propõe e o humano aprova cada edição ou comando antes de executar; aprovar edições automaticamente mas confirmar comandos com efeito fora do repositório, como rede ou banco de dados; e autonomia ampla dentro de um ambiente isolado, como um worktree descartável, onde o risco de um erro é menor porque o raio de impacto está contido.

Essa régua se conecta direto ao princípio de simplicidade da Sessão 1: a Anthropic recomenda teste extensivo em ambiente controlado, com salvaguardas apropriadas, antes de liberar autonomia total em produção. Autonomia ampla sem isolamento correspondente é exatamente o cenário que o guia desaconselha: o risco de um erro numa etapa se propagar, sem supervisão, pelas etapas seguintes.

A aritmética do erro composto, vista em [O arnês do agente](arnes.md#erro-composto-a-aritmetica-da-trajetoria), é o que dá tamanho a esse risco: numa trajetória de vinte etapas, 99% de acerto por etapa deixa a tarefa inteira em 81,8%. É por isso que autonomia ampla pede isolamento e verificação, não confiança no modelo.

Algumas aplicações agênticas vão além do modo de permissão e oferecem *hooks*: pontos de interceptação que rodam antes ou depois de o agente executar uma ferramenta, e podem bloquear a ação, registrar um log, ou pedir confirmação extra para comandos específicos, por exemplo qualquer comando que toque um arquivo de credenciais ou qualquer push direto para a branch principal. Um *hook* não substitui o arquivo de instrução, nem o MCP: o AGENTS.md documenta a convenção esperada; o hook aplica um limite na camada de execução, que continua valendo mesmo se o agente ignorar a convenção documentada.

!!! tip "Aplique agora"
    No ambiente que você usa hoje, o agente pede confirmação antes de cada ação, ou já roda edições automaticamente? Isso foi uma decisão deliberada, calibrada pelo risco da tarefa, ou é só o padrão de fábrica que ninguém revisitou?

## Quanto de autonomia liberar

A régua de autonomia e supervisão vista em [Autonomia e supervisão](autonomia-e-supervisao.md#autonomia-e-supervisao-o-que-o-ambiente-deixa-o-agente-decidir-sozinho) se decide caso a caso, não uma vez para o time inteiro. Três perguntas ajudam:

- A ação é fácil de reverter (editar um arquivo ainda não commitado) ou difícil (enviar um e-mail, fazer uma implantação, apagar dado em produção)? Ação fácil de reverter aceita mais autonomia; ação difícil de reverter pede confirmação antes de executar.
- O agente está rodando dentro de um ambiente isolado, como um worktree ou um contêiner descartável, ou direto no ambiente de produção? Isolamento reduz o raio de impacto de um erro, o que justifica liberar mais autonomia dentro dele.
- A tarefa se repete todo dia, do mesmo jeito? Se sim, vale configurar um *hook* uma vez, em vez de repetir a mesma confirmação manual centenas de vezes.

!!! tip "Aplique agora"
    Pense na última vez que um agente fez algo que você não esperava. A ação era fácil de reverter? Se não era, o nível de autonomia configurado hoje provavelmente está alto demais para aquele tipo de tarefa.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
