# O arquivo de instrução

O arquivo de instrução do repositório (AGENTS.md, CLAUDE.md) faz o agente conhecer as convenções do projeto sem alguém repeti-las a cada sessão. O que colocar nele, como estruturá-lo, e como saber que ele ainda funciona.

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

## O que colocar (e o que não colocar) no arquivo de instrução

Um AGENTS.md ou CLAUDE.md útil não é uma lista de boas intenções. Ele responde perguntas concretas que o agente precisa saber antes de agir: qual comando builda o projeto, qual comando roda os testes, que convenção de nomenclatura o time usa, o que nunca deve ser commitado. Um arquivo que só diz "escreva código limpo e siga boas práticas" não muda nenhum comportamento observável do agente, porque não dá nenhuma informação que ele não teria por padrão.

O anti-padrão simétrico é o arquivo enciclopédico: documentar cada decisão arquitetural histórica do projeto num único arquivo que o agente precisa processar em toda execução consome espaço de contexto sem, na maioria das tarefas, mudar o comportamento. A régua prática vem direto da definição de context engineering vista em [Context engineering](context-engineering.md): cada linha do arquivo de instrução deveria mudar alguma decisão que o agente tomaria de outro jeito.

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

Repositório único, um serviço: um AGENTS.md na raiz basta. Monorepo com mais de um pacote ou serviço, cada um com convenção própria de build ou teste: vale um arquivo na raiz só com o que é comum a todos (segurança, formato de commit), e um arquivo por pacote só com o que aquele pacote tem de específico — o mecanismo de precedência do padrão, visto em [O arquivo de instrução](arquivo-de-instrucao.md#um-arquivo-de-instrucao-qualquer-ferramenta-agentsmd), garante que o agente lê o arquivo mais próximo primeiro. A régua para decidir se compensa abrir um segundo arquivo é a mesma da seção anterior: existe uma linha que só faz sentido para aquele pacote, e que confundiria se aparecesse no arquivo de outro pacote? Se sim, separe. Se as diferenças são poucas, um arquivo único com uma seção por pacote resolve sem multiplicar arquivo para manter.

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

**Próxima página:** [Isolamento por ramo](isolamento-por-ramo.md).
