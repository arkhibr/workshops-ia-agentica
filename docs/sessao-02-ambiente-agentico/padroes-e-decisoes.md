# Padrões e decisões

## Quando vale configurar um ambiente compartilhado

Montar um arquivo de instrução, conectar uma ferramenta via MCP e isolar contexto por ramo tem custo de configuração. Vale a pena quando pelo menos duas condições aparecem juntas:

| Critério | Baixo investimento suficiente | Investimento completo justificado |
|---|---|---|
| Tamanho do time | uma pessoa | mais de uma pessoa usando agente no mesmo repositório |
| Vida do repositório | protótipo descartável | projeto que vai durar meses ou anos |
| Frequência de uso do agente | esporádica | diária, múltiplas sessões em paralelo |
| Ferramentas externas necessárias | nenhuma, só leitura/escrita de arquivo | acesso a banco de dados, API interna, rastreador de tarefas |

Um repositório pessoal, de uso esporádico, não precisa de MCP nem de isolamento por worktree — um arquivo de instrução simples já resolve a maior parte do ganho. Um time de vários desenvolvedores usando agente todo dia num sistema de produção está do lado direito da tabela inteira.

O cálculo é o mesmo por trás de qualquer decisão de investir tempo em preparação antes de começar: o custo de configurar aparece agora, de uma vez, e o ganho aparece depois, espalhado por cada sessão futura de agente. Numa tarefa esporádica, esse ganho futuro não paga o custo presente. No repositório que o time usa todo dia, paga rápido: a segunda sessão de agente já reaproveita o mesmo arquivo de instrução, a mesma conexão MCP e o mesmo hábito de isolar por ramo, sem reconfigurar nada.

!!! tip "Aplique agora"
    Classifique o repositório em que você mais usa IA hoje contra as quatro linhas da tabela. Ele pede o ambiente completo, ou um arquivo de instrução simples já resolveria a maior parte do problema?

## Um cuidado prático com isolamento por ramo

Cada worktree é um diretório de trabalho completo, mas não duplica automaticamente tudo que um projeto precisa para rodar. O histórico do git é compartilhado entre todos os worktrees do mesmo repositório; a pasta de dependências instaladas, não. Um `npm install` rodado num worktree não aparece no outro — cada worktree novo precisa da própria instalação, ou de um link simbólico para uma pasta de dependências compartilhada fora do controle do git.

Isso muda o cálculo de quando vale isolar por ramo: se criar um worktree novo significa esperar alguns minutos de instalação antes de começar a tarefa de verdade, a fricção desestimula o hábito exatamente nos casos em que ele mais evitaria um incidente como o do [Estudo de caso](estudo-de-caso.md). Times que isolam por ramo com frequência costumam automatizar esse passo num script simples, que cria o worktree e já deixa o ambiente pronto para o agente trabalhar.

## O que colocar (e o que não colocar) no arquivo de instrução

Um AGENTS.md ou CLAUDE.md útil não é uma lista de boas intenções. Ele responde perguntas concretas que o agente precisa saber antes de agir: qual comando builda o projeto, qual comando roda os testes, que convenção de nomenclatura o time usa, o que nunca deve ser commitado. Um arquivo que só diz "escreva código limpo e siga boas práticas" não muda nenhum comportamento observável do agente, porque não dá nenhuma informação que ele não teria por padrão.

O anti-padrão simétrico é o arquivo enciclopédico: documentar cada decisão arquitetural histórica do projeto num único arquivo que o agente precisa processar em toda execução consome espaço de contexto sem, na maioria das tarefas, mudar o comportamento. A régua prática vem direto da definição de context engineering vista em [Conceitos](conceitos.md#de-prompt-engineering-para-context-engineering): cada linha do arquivo de instrução deveria mudar alguma decisão que o agente tomaria de outro jeito.

A diferença fica mais clara lado a lado. Uma linha inútil:

```markdown
- Escreva código limpo e siga boas práticas.
```

Uma linha útil, sobre o mesmo tema:

```markdown
- Funções com mais de 40 linhas precisam ser quebradas antes do merge (regra do ESLint `max-lines-per-function`, já configurada no projeto).
```

A segunda linha dá um número, uma ferramenta e uma consequência. A primeira não dá nenhuma informação que um agente não teria por padrão.

## Um arquivo ou vários: a decisão de estrutura

Repositório único, um serviço: um AGENTS.md na raiz basta. Monorepo com mais de um pacote ou serviço, cada um com convenção própria de build ou teste: vale um arquivo na raiz só com o que é comum a todos (segurança, formato de commit), e um arquivo por pacote só com o que aquele pacote tem de específico — o mecanismo de precedência do padrão, visto em [Conceitos](conceitos.md#um-arquivo-de-instrucao-qualquer-ferramenta-agentsmd), garante que o agente lê o arquivo mais próximo primeiro. A régua para decidir se compensa abrir um segundo arquivo é a mesma da seção anterior: existe uma linha que só faz sentido para aquele pacote, e que confundiria se aparecesse no arquivo de outro pacote? Se sim, separe. Se as diferenças são poucas, um arquivo único com uma seção por pacote resolve sem multiplicar arquivo para manter.

## MCP: quando conectar uma ferramenta externa vale a pena

Conectar uma ferramenta via MCP tem sentido quando o agente precisa de informação ou de capacidade de ação que não existe no próprio código do repositório: consultar o estado atual de um banco de dados, abrir uma issue num rastreador, buscar a versão vigente de uma política num sistema externo. Não faz sentido para informação que já cabe num arquivo do repositório — nesse caso, o próprio agente já lê o arquivo diretamente, sem precisar de um protocolo de acesso externo.

A pergunta que resume a decisão: essa informação muda independentemente do código, num sistema que o agente não teria como acessar de outra forma? Se sim, MCP. Se a informação já está versionada no repositório, um MCP é complexidade desnecessária.

As três primitivas do protocolo, vistas em [Conceitos](conceitos.md#o-problema-mn-e-o-model-context-protocol), ajudam a decidir que tipo de acesso pedir, não só se vale conectar. Se o agente precisa decidir sozinho quando buscar a informação, ela deveria chegar como *tool*. Se a informação é sempre necessária, e não depende de decisão do agente, faz mais sentido a aplicação injetar como *resource*, sem gastar uma chamada de ferramenta para buscar algo que já era certo que ia ser usado.

!!! tip "Aplique agora"
    Antes de conectar o próximo servidor MCP no seu ambiente, confira a origem: é mantido pelo fornecedor oficial da ferramenta, ou por um terceiro sem relação com quem construiu o sistema que ele acessa? Servidor de terceiro não é proibido, mas pede leitura do código, se for open source, e o menor escopo de permissão que a tarefa permitir.

## Antes de conectar: avaliar a origem do servidor MCP

Um servidor MCP roda como um processo à parte, com acesso ao que você autorizar: um banco de dados, um sistema de arquivos, uma API interna. Três critérios reduzem o risco de conectar algo que expõe mais do que deveria:

- **Origem.** Servidor mantido pelo próprio fornecedor da ferramenta (o rastreador de tarefas, o banco de dados) tem manutenção e segurança verificadas por quem construiu o sistema de origem. Servidor de terceiro, sem essa relação, pede mais cautela antes de conectar.
- **Escopo.** Peça o menor conjunto de permissões que a tarefa exige. Um servidor de banco de dados com acesso só de leitura remove uma categoria inteira de risco, mesmo quando o acesso de escrita está disponível.
- **Auditabilidade.** Se o servidor é open source, alguém do time já leu o código antes de conectar em produção? Um servidor fechado, sem essa possibilidade, exige mais confiança na origem para compensar.

## Anti-padrão: arquivo de instrução que ninguém mantém

O arquivo de instrução decai do mesmo jeito que qualquer documentação: escrito com cuidado na primeira semana, e nunca mais atualizado depois que uma convenção muda. O sintoma é sempre o mesmo — o agente sugere um comando de build que não existe mais, ou uma convenção de nomenclatura que o time abandonou há dois meses, e ninguém percebe até o terceiro ou quarto prompt confuso na mesma sessão.

A correção não é escrever um arquivo mais completo. É tratar o arquivo de instrução como parte do código: revisado no mesmo pull request que muda a convenção que ele documenta, não numa tarefa de documentação separada que sempre fica para depois.

## Como saber se o arquivo ainda funciona

Revisar o arquivo de instrução no mesmo PR que muda a convenção resolve a maior parte da decadência, mas não cobre o caso em que ninguém mudou a convenção de propósito: ela foi ficando obsoleta aos poucos, por exemplo quando uma dependência principal do projeto muda de versão e o comando de build muda junto, sem que isso pareça motivo suficiente para abrir um PR só para o arquivo de instrução. Um teste simples, rodado de vez em quando, pega isso antes que o agente sugira algo que não existe mais: executar, ao pé da letra, cada comando listado no arquivo.

```bash
# Verificação manual periódica do AGENTS.md
npm install    # comando documentado no arquivo — ainda funciona?
npm run dev    # idem
npm test       # idem
```

Se um comando falhar, ou não existir mais, o arquivo está desatualizado, mesmo tendo sido revisado num PR recente para outro motivo. Times maiores automatizam essa checagem como um passo da esteira de CI, que roda os comandos documentados contra o projeto real e falha o build se algum deles não existir mais — uma forma de o arquivo de instrução ser verificado por máquina, não só por revisão humana esporádica.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md) aplica esses critérios a um caso concreto.
