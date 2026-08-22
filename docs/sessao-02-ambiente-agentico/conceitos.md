# Conceitos

## Do ambiente individual ao ambiente compartilhado

Um ambiente agêntico é a combinação de quatro peças: o modelo, a aplicação agêntica que orquestra a conversa com ele (Claude Code, Codex CLI, Copilot, Cursor), o arquivo de configuração que carrega convenções do repositório, e o conjunto de ferramentas que o agente pode acionar. Quando cada desenvolvedor monta essa combinação à própria maneira, o time herda exatamente o sintoma "ad hoc" descrito na Sessão 1: nenhum vocabulário compartilhado sobre o que configurar, e o resultado de um prompt na máquina de alguém não se repete na do colega.

A correção não é escolher uma ferramenta única para todo o time. É compartilhar as três peças que independem da ferramenta escolhida: o arquivo de configuração, o protocolo de acesso a ferramentas externas, e a disciplina de isolamento de contexto.

## De prompt engineering para context engineering

A Anthropic, no guia de engenharia "Effective context engineering for AI agents" (setembro de 2025), descreve uma virada de foco: depois de alguns anos em que prompt engineering (encontrar as palavras certas para uma instrução) dominava a atenção, o problema real passou a ser outro: qual configuração de contexto tem mais chance de produzir o comportamento desejado do modelo. Prompt engineering cuida do texto da instrução. Context engineering cuida de tudo que chega à janela de contexto numa execução: instruções, histórico, resultados de ferramentas, arquivos lidos.

O guia é específico sobre o papel das ferramentas nessa mudança: elas são o contrato entre o agente e o espaço de informação e ação disponível, e precisam ser desenhadas para eficiência de token e para induzir comportamento eficiente do agente. Uma ferramenta mal desenhada consome espaço de contexto que poderia ir para informação relevante ao problema, além de ser mais incômoda de usar.

Context engineering virou o problema central, e não só mais uma etapa de prompt engineering, por um motivo técnico presente na própria arquitetura Transformer, apresentada por Vaswani et al. (2017) e já citada na Sessão 1: a atenção entre tokens cresce de forma quadrática com o tamanho do contexto. Quanto mais token na janela, mais relações de atenção o modelo precisa distribuir entre eles, e sua capacidade de recuperar com precisão uma informação específica cai de forma gradual conforme o contexto cresce — efeito que a própria Anthropic chama de degradação de contexto (*context rot*).

O guia recomenda duas técnicas concretas contra essa degradação. A primeira é recuperação just-in-time: em vez de pré-carregar todo dado relevante antes de começar, o agente mantém referências leves (caminho de arquivo, consulta salva, link) e usa ferramentas para carregar o conteúdo completo só no momento em que precisa dele. O Claude Code opera assim: escreve uma consulta direcionada e usa ferramentas de linha de comando para vasculhar uma base de código inteira sem carregar cada arquivo na janela de contexto de uma vez. A segunda é compactação: numa tarefa de muitas etapas, o agente resume o histórico de conversa com alta fidelidade antes de continuar, mantendo o que importa. A régua de qualidade é maximizar primeiro o que a compactação lembra, e só depois cortar o que sobrou de irrelevante.

Uma terceira técnica separa o problema por arquitetura: sub-agentes com contexto isolado. Um agente principal delega uma exploração extensa, por exemplo varrer um repositório grande atrás da causa de um bug, para um sub-agente, que devolve um resumo condensado, muitas vezes na casa de 1 a 2 mil tokens. O agente principal recebe só a conclusão da investigação.

O mesmo raciocínio vale para a instrução que configura o agente, seja um prompt de sistema ou um arquivo como o AGENTS.md discutido adiante: o guia chama de altitude certa o ponto de equilíbrio entre instrução específica demais, que quebra assim que a tarefa foge um pouco do previsto, e instrução genérica demais, que não muda decisão nenhuma. Uma instrução na altitude certa é específica o bastante para guiar o comportamento, e flexível o bastante para deixar o modelo aplicar critério nos casos que ela não previu.

## O problema M×N e o Model Context Protocol

Antes de novembro de 2024, conectar um agente a uma ferramenta externa (um banco de dados, um rastreador de issues, um sistema de arquivos) exigia uma integração específica para aquele par modelo-ferramenta. Com M modelos e N ferramentas, o time enfrentava M×N integrações para manter.

A Anthropic abriu o código do Model Context Protocol (MCP) para resolver exatamente essa conta: um protocolo aberto no qual cada modelo implementa o MCP uma vez, e cada ferramenta ou serviço implementa o MCP uma vez. A multiplicação vira soma. Um ano depois do lançamento, o protocolo já tinha adoção de OpenAI, Google e Microsoft, tornando-se o padrão de fato para conectar agentes a sistemas externos — não porque uma empresa impôs, mas porque resolvia um problema real de manutenção que todo mundo compartilhava.

O protocolo formaliza essa integração numa arquitetura cliente-servidor: a aplicação agêntica mantém um cliente MCP para cada servidor a que se conecta, e cada servidor expõe suas capacidades por três primitivas independentes. *Tools* são funções que o próprio modelo decide quando chamar, como consultar um rastreador de tarefas. *Resources* são dados que a aplicação injeta no contexto por conta própria, como o conteúdo de um arquivo específico. *Prompts* são modelos de instrução prontos, escolhidos por quem usa a ferramenta, não pelo modelo. Um servidor não precisa expor as três; a maioria expõe só *tools*.

O protocolo também define como a aplicação agêntica fala com cada servidor. Um servidor local, que roda como processo na mesma máquina do agente, se comunica por *stdio* (entrada e saída padrão do processo). Um servidor remoto, acessado pela rede e compartilhado por várias pessoas ao mesmo tempo, usa HTTP com streaming. A escolha de transporte não muda o que o servidor expõe, só como a aplicação agêntica conversa com ele: servidor de uso individual costuma rodar em *stdio*; servidor de uso compartilhado pelo time inteiro tende a rodar como serviço HTTP.

Na prática, conectar um servidor MCP a uma aplicação agêntica como o Claude Code ou o Cursor é uma questão de configuração, não de código novo:

```json
{
  "mcpServers": {
    "rastreador-de-tarefas": {
      "command": "npx",
      "args": ["-y", "@exemplo/mcp-server-tarefas"],
      "env": {
        "API_TOKEN": "..."
      }
    }
  }
}
```

A aplicação agêntica lê essa configuração, inicia o processo do servidor e passa a oferecer as ferramentas que ele expõe como parte do conjunto disponível ao modelo. O `AGENTS.md` do repositório não precisa mudar uma linha para isso funcionar. As duas peças são independentes.

## Um arquivo de instrução, qualquer ferramenta: AGENTS.md

Se MCP resolve como um agente acessa uma ferramenta, falta resolver como um agente aprende as convenções do repositório em que está trabalhando. Em agosto de 2025, OpenAI, Google, Cursor, Factory e Sourcegraph formalizaram juntos o AGENTS.md: um arquivo markdown simples, na raiz do repositório, sem esquema obrigatório, que qualquer agente de codificação lê para saber como construir, testar e alterar o projeto. Diferente do README, que fala com uma pessoa, o AGENTS.md fala com o agente: comandos de build e teste, convenções de estilo, regras de segurança, formato de commit.

Um AGENTS.md mínimo, mas real, costuma ter esta forma:

```markdown
## Comandos de build e teste
- Instalar dependências: `npm install`
- Rodar em desenvolvimento: `npm run dev`
- Rodar testes: `npm test`

## Convenções de código
- TypeScript em modo strict
- Aspas simples, sem ponto e vírgula
```

Cada linha responde uma pergunta que o agente teria de adivinhar sem o arquivo. Nenhuma linha é uma boa intenção genérica.

Em um monorepo, com vários pacotes ou serviços no mesmo repositório, o padrão permite mais de um AGENTS.md: cada pasta pode ter o próprio arquivo, e o agente lê o mais próximo do diretório em que está trabalhando. O arquivo da raiz vale como regra geral; o arquivo de um pacote específico sobrepõe a regra geral quando os dois conflitam. O próprio repositório da OpenAI usa esse padrão, com mais de 80 arquivos AGENTS.md espalhados pelos pacotes, cada um documentando só o que aquele pacote precisa.

O padrão hoje é mantido pela Agentic AI Foundation, um projeto da Linux Foundation — não pertence a um único fornecedor. Mais de 20 mil repositórios já adotaram o formato, e ferramentas de fornecedores concorrentes (GitHub Copilot, Codex, Cursor, Gemini) leem o mesmo arquivo. O `CLAUDE.md` que este próprio workshop usa para configurar convenções do repositório cumpre esse mesmo papel, num formato específico do Claude Code.

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

## As quatro peças, lado a lado

| Peça | O que resolve | Compartilhado entre ferramentas? |
|---|---|---|
| Arquivo de configuração (AGENTS.md / CLAUDE.md) | O agente conhece as convenções do repositório | Sim — mesmo arquivo, qualquer agente que o leia |
| MCP | O agente acessa uma ferramenta externa sem integração específica | Sim — protocolo aberto, adotado por múltiplos fornecedores |
| Isolamento por ramo (worktree) | Duas sessões não corrompem o trabalho uma da outra | Sim — é uma prática de git, não de uma ferramenta de IA específica |
| Aplicação agêntica (Claude Code, Copilot, Cursor) | Orquestra a conversa entre humano, modelo e ferramentas | Não — cada equipe escolhe a própria, o método é agnóstico |

!!! question "Antes de continuar"
    Das quatro peças da tabela, qual o seu time já tem hoje? Qual está completamente ausente?

## Autonomia e supervisão: o que o ambiente deixa o agente decidir sozinho

As quatro peças anteriores decidem o que o agente sabe e a que ele tem acesso. Falta uma decisão diferente, que nenhuma delas cobre: quanto o agente decide e executa sozinho antes de um humano olhar. Essa decisão também é uma propriedade do ambiente, não do modelo: o mesmo modelo, no mesmo repositório, pode operar sob supervisão apertada ou com autonomia ampla, dependendo de como a aplicação agêntica foi configurada para aquela sessão.

A maioria das aplicações agênticas de codificação oferece pelo menos três posições nesse espectro: perguntar antes de cada ação, em que o agente propõe e o humano aprova cada edição ou comando antes de executar; aprovar edições automaticamente mas confirmar comandos com efeito fora do repositório, como rede ou banco de dados; e autonomia ampla dentro de um ambiente isolado, como um worktree descartável, onde o risco de um erro é menor porque o raio de impacto está contido.

Essa régua se conecta direto ao princípio de simplicidade da Sessão 1: a Anthropic recomenda teste extensivo em ambiente controlado, com salvaguardas apropriadas, antes de liberar autonomia total em produção. Autonomia ampla sem isolamento correspondente é exatamente o cenário que o guia desaconselha: o risco de um erro numa etapa se propagar, sem supervisão, pelas etapas seguintes.

Algumas aplicações agênticas vão além do modo de permissão e oferecem hooks: pontos de interceptação que rodam antes ou depois de o agente executar uma ferramenta, e podem bloquear a ação, registrar um log, ou pedir confirmação extra para comandos específicos, por exemplo qualquer comando que toque um arquivo de credenciais ou qualquer push direto para a branch principal. Um hook não substitui o arquivo de instrução, nem o MCP: o AGENTS.md documenta a convenção esperada; o hook aplica um limite na camada de execução, que continua valendo mesmo se o agente ignorar a convenção documentada.

!!! tip "Aplique agora"
    No ambiente que você usa hoje, o agente pede confirmação antes de cada ação, ou já roda edições automaticamente? Isso foi uma decisão deliberada, calibrada pelo risco da tarefa, ou é só o padrão de fábrica que ninguém revisitou?

**Próxima página:** [Padrões e decisões](padroes-e-decisoes.md).
