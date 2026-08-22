# Padrões e decisões

## Quando vale configurar um ambiente compartilhado

Montar um arquivo de instrução, conectar uma ferramenta via MCP e isolar contexto por ramo tem custo de configuração. Vale a pena quando pelo menos duas condições aparecem juntas:

| Critério | Baixo investimento suficiente | Investimento completo justificado |
|---|---|---|
| Tamanho do time | uma pessoa | mais de uma pessoa usando agente no mesmo repositório |
| Vida do repositório | protótipo descartável | projeto que vai durar meses ou anos |
| Frequência de uso do agente | esporádica | diária, múltiplas sessões em paralelo |
| Ferramentas externas necessárias | nenhuma, só leitura/escrita de arquivo | acesso a banco de dados, API interna, rastreador de tarefas |

Um repositório pessoal, de uso esporádico, não precisa de MCP nem de isolamento por worktree — um arquivo de instrução simples já resolve a maior parte do ganho. A Vetor, com quatro desenvolvedores usando agente todo dia num sistema de produção, está do lado direito da tabela inteira.

!!! tip "Aplique agora"
    Classifique o repositório em que você mais usa IA hoje contra as quatro linhas da tabela. Ele pede o ambiente completo, ou um arquivo de instrução simples já resolveria a maior parte do problema?

## O que colocar (e o que não colocar) no arquivo de instrução

Um AGENTS.md ou CLAUDE.md útil não é uma lista de boas intenções. Ele responde perguntas concretas que o agente precisa saber antes de agir: qual comando builda o projeto, qual comando roda os testes, que convenção de nomenclatura o time usa, o que nunca deve ser commitado. Um arquivo que só diz "escreva código limpo e siga boas práticas" não muda nenhum comportamento observável do agente, porque não dá nenhuma informação que ele não teria por padrão.

O anti-padrão simétrico é o arquivo enciclopédico: documentar cada decisão arquitetural histórica do projeto num único arquivo que o agente precisa processar em toda execução consome espaço de contexto sem, na maioria das tarefas, mudar o comportamento. A régua prática vem direto da definição de context engineering vista em [Conceitos](conceitos.md#de-prompt-engineering-para-context-engineering): cada linha do arquivo de instrução deveria mudar alguma decisão que o agente tomaria de outro jeito.

## MCP: quando conectar uma ferramenta externa vale a pena

Conectar uma ferramenta via MCP tem sentido quando o agente precisa de informação ou de capacidade de ação que não existe no próprio código do repositório: consultar o estado atual de um banco de dados, abrir uma issue num rastreador, buscar a versão vigente de uma política num sistema externo. Não faz sentido para informação que já cabe num arquivo do repositório — nesse caso, o próprio agente já lê o arquivo diretamente, sem precisar de um protocolo de acesso externo.

A pergunta que resume a decisão: essa informação muda independentemente do código, num sistema que o agente não teria como acessar de outra forma? Se sim, MCP. Se a informação já está versionada no repositório, um MCP é complexidade desnecessária.

## Anti-padrão: arquivo de instrução que ninguém mantém

O arquivo de instrução decai do mesmo jeito que qualquer documentação: escrito com cuidado na primeira semana, e nunca mais atualizado depois que uma convenção muda. O sintoma é sempre o mesmo — o agente sugere um comando de build que não existe mais, ou uma convenção de nomenclatura que o time abandonou há dois meses, e ninguém percebe até o terceiro ou quarto prompt confuso na mesma sessão.

A correção não é escrever um arquivo mais completo. É tratar o arquivo de instrução como parte do código: revisado no mesmo pull request que muda a convenção que ele documenta, não numa tarefa de documentação separada que sempre fica para depois.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md) aplica esses critérios à Vetor.
