# O arquivo de instrução

Com um arquivo de instrução no repositório (AGENTS.md, CLAUDE.md), o agente conhece as convenções do projeto sem ninguém repeti-las a cada sessão. Esta página mostra o que colocar nele, como organizá-lo e como saber se ele ainda funciona.

## O padrão AGENTS.md

O MCP resolve o acesso do agente a uma ferramenta. Falta resolver como ele aprende as convenções do repositório onde está trabalhando. [Em agosto de 2025, OpenAI, Google, Cursor, Factory e Sourcegraph formalizaram juntos o AGENTS.md](../referencia/bibliografia.md#agentic-ai-foundation-agentsmd-standard): um arquivo markdown simples, na raiz do repositório, sem esquema obrigatório, que qualquer agente de codificação lê para saber como construir, testar e alterar o projeto. O README fala com uma pessoa. O AGENTS.md fala com o agente, e por isso traz comando de compilação e de teste, convenção de estilo, regra de segurança e formato de commit.

Um AGENTS.md mínimo, mas real, costuma ter esta forma:

```markdown
## Comandos de compilação e teste
- Instalar dependências: `npm install`
- Rodar em desenvolvimento: `npm run dev`
- Rodar testes: `npm test`

## Convenções de código
- TypeScript em modo strict
- Aspas simples, sem ponto e vírgula
```

Cada linha responde uma pergunta que o agente teria de adivinhar sem o arquivo.

Em um monorepo, com vários pacotes ou serviços no mesmo repositório, o padrão permite mais de um AGENTS.md: cada pasta pode ter o próprio arquivo, e o agente lê o mais próximo do diretório em que está trabalhando. O arquivo da raiz vale como regra geral, e o arquivo de um pacote específico sobrepõe a regra geral quando os dois conflitam. O próprio repositório da OpenAI usa esse padrão, com mais de 80 arquivos AGENTS.md espalhados pelos pacotes, cada um documentando só o que aquele pacote precisa.

Hoje quem mantém o padrão é a Agentic AI Foundation, um projeto da Linux Foundation, e nenhum fornecedor é dono dele. Mais de 20 mil repositórios já adotaram o formato, e ferramentas de fornecedores concorrentes (GitHub Copilot, Codex, Cursor, Gemini) leem o mesmo arquivo. O `CLAUDE.md` que este próprio workshop usa para configurar convenções do repositório cumpre esse mesmo papel, num formato específico do Claude Code.

## O que colocar (e o que não colocar) no arquivo de instrução

Um AGENTS.md ou CLAUDE.md útil responde perguntas concretas que o agente precisa saber antes de agir: qual comando compila o projeto, qual comando roda os testes, que convenção de nomenclatura o time usa, o que nunca deve ser commitado. Um arquivo que só diz "escreva código limpo e siga boas práticas" não muda comportamento nenhum, porque não informa nada que o agente já não tentasse fazer.

O erro oposto é o arquivo enciclopédico. Documentar cada decisão arquitetural histórica num arquivo que o agente processa em toda execução gasta espaço de contexto e, na maioria das tarefas, não muda comportamento nenhum. O critério sai direto de [Engenharia de contexto](engenharia-de-contexto.md): cada linha do arquivo precisa mudar alguma decisão que o agente tomaria de outro jeito.

A diferença fica mais clara lado a lado. Uma linha inútil:

```markdown
- Escreva código limpo e siga boas práticas.
```

Uma linha útil, sobre o mesmo tema:

```markdown
- Funções com mais de 40 linhas precisam ser quebradas antes do merge (regra do ESLint `max-lines-per-function`, já configurada no projeto).
```

A segunda linha dá um número, uma ferramenta e uma consequência verificável.

## Um arquivo ou vários

Repositório único, um serviço: um AGENTS.md na raiz basta. Monorepo com mais de um pacote ou serviço, cada um com convenção própria de compilação ou teste: vale um arquivo na raiz só com o que é comum a todos (segurança, formato de commit), e um arquivo por pacote só com o que aquele pacote tem de específico. A precedência descrita em [O padrão AGENTS.md](#o-padrao-agentsmd) garante que o agente lê o arquivo mais próximo primeiro. Para decidir se compensa abrir um segundo arquivo, use o mesmo critério da seção anterior: existe uma linha que só faz sentido para aquele pacote, e que confundiria se aparecesse no arquivo de outro? Se existe, separe. Se as diferenças são poucas, um arquivo único com uma seção por pacote resolve sem multiplicar arquivo para manter.

## Anti-padrão: arquivo de instrução que ninguém mantém

O arquivo de instrução decai do mesmo jeito que qualquer documentação: escrito com cuidado na primeira semana, e nunca mais atualizado depois que uma convenção muda. O sintoma costuma ser o mesmo. O agente sugere um comando de compilação que não existe mais, ou uma convenção de nomenclatura que o time abandonou há dois meses, e ninguém percebe até o terceiro ou quarto prompt confuso na mesma sessão.

Trate o arquivo de instrução como parte do código: revise-o no mesmo pull request que muda a convenção que ele documenta, em vez de deixá-lo para uma tarefa de documentação que fica sempre para depois. Escrever um arquivo mais completo não resolve isso.

## Como saber se o arquivo ainda funciona

Revisar o arquivo no mesmo PR que muda a convenção resolve a maior parte da decadência. Sobra o caso em que ninguém mudou a convenção de propósito e ela foi ficando obsoleta aos poucos, como quando uma dependência principal muda de versão e leva junto o comando de compilação, sem que ninguém ache que isso merece um PR só para o arquivo de instrução. Um teste simples pega esse caso: execute, ao pé da letra, cada comando listado no arquivo.

```bash
# Verificação manual periódica do AGENTS.md
npm install    # comando documentado no arquivo — ainda funciona?
npm run dev    # idem
npm test       # idem
```

Se um comando falhar, ou não existir mais, o arquivo está desatualizado, mesmo tendo sido revisado num PR recente para outro motivo. Times maiores automatizam essa checagem como um passo da esteira de CI, que roda os comandos documentados contra o projeto real e falha a compilação se algum deles não existir mais. Com isso a máquina verifica o arquivo toda vez, sem depender de alguém lembrar.

**Próxima página:** [Isolamento por ramo](isolamento-por-ramo.md).
