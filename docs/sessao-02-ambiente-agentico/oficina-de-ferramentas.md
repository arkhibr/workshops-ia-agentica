# Oficina de ferramentas

**Objetivo Bloom:** Compreender e Aplicar.

Nos próximos 30 minutos cada participante monta o ambiente compartilhado da sessão na própria máquina: arquivo de instrução, servidor MCP conectado e isolamento por ramo.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (**Claude Code, Codex CLI ou Gemini CLI**), o git e o Node.js 20 ou superior. Tempo estimado: 30 minutos.

Todos os experimentos partem de um **projeto vazio**, criado durante a própria oficina. Ninguém clona nada pronto: cada pessoa cria os três comandos abaixo e parte exatamente do mesmo estado.

```bash
mkdir oficina-arnes && cd oficina-arnes
git init
node --version   # precisa mostrar v20 ou superior
```

Onde os comandos diferem entre sistemas, a página traz as versões em abas — escolha a do seu sistema antes de copiar. Onde diferem por ferramenta de agente, o mesmo vale para Claude Code, Codex CLI e Gemini CLI.

**Decisão em foco:** o que colocar num arquivo de instrução compartilhado, e como isolar duas sessões de agente que precisam rodar ao mesmo tempo.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimentos A, B e C, para sair da sessão com um arquivo de instrução testado nas duas versões, um servidor MCP conectado e um worktree testado.
- **Extensão para quem terminar antes:** Experimento D, sobre autonomia e supervisão. Se o tempo apertar, é o único que pode ficar para depois da aula. Nunca corte A, B ou C.

## Experimento A

**Objetivo:** pedir a mesma função simples duas vezes, sem arquivo de instrução e depois com um arquivo de instrução robusto, e comparar o *processo* que produziu cada resultado, em vez do valor que o cálculo devolveu.

**Passo 1 — peça a função sem AGENTS.md.** No projeto vazio criado no início da oficina, abra o agente e envie exatamente este pedido:

> Escreva uma função `calcularJurosAtraso(valorPedido, diasAtraso)` que calcula os juros de atraso de um pedido da Vetor: 0,1% ao dia sobre o valor do pedido, sem juros se não houver atraso, e nunca ultrapassando 20% do valor do pedido.

Rode o que o agente gerou. Se ele criou um arquivo de teste, rode com `node --test`. Se não criou nenhum, escreva você mesmo três ou quatro chamadas de exemplo e confira o resultado à mão. Anote três coisas, porque são elas que você vai comparar no passo 4:

- O agente escreveu algum teste antes de escrever a implementação, ou só entregou a implementação?
- A função tem documentação no formato nativo da linguagem (bloco JSDoc `/** ... */` com `@param` e `@returns`), só um comentário de texto solto, ou nenhuma documentação?
- Quantos arquivos o agente criou?

Registre esse estado antes de seguir, para poder comparar depois sem depender da memória:

```bash
git add -A && git commit -m "baseline sem AGENTS.md"
```

**Passo 2 — instale o AGENTS.md robusto.** Crie `AGENTS.md` na raiz do projeto com este conteúdo, copiado exatamente (desta vez o exercício não é escrever o arquivo, é sentir o efeito de um já pronto e sério):

```markdown
# AGENTS.md

## Processo obrigatório: TDD
Toda função nova segue o ciclo vermelho-verde-refatoração:
1. Escreva o teste que falha antes de qualquer código de implementação.
2. Escreva o mínimo de código necessário para o teste passar.
3. Refatore mantendo os testes verdes.
Nunca entregue a implementação sem o teste correspondente já escrito primeiro.

## Documentação nativa obrigatória
Toda função pública recebe documentação no formato nativo da linguagem:
- JavaScript/TypeScript: bloco JSDoc (`/** ... */`) com `@param` e `@returns`.
- C#: comentário XML (`/// <summary>`, `<param>`, `<returns>`).
Comentário de texto solto, fora desse formato, não conta como documentação.

## Comando de teste
`node --test` roda toda a suíte. Não existe passo de compilação.
```

**Passo 3 — repita o pedido, numa conversa nova.** Abra uma conversa nova com o agente (não continue a do passo 1, porque o objetivo é ver o efeito do arquivo, não de um agente que já lembra o que respondeu) e envie exatamente o mesmo pedido do passo 1, palavra por palavra.

**Passo 4 — rode de novo e compare.** Rode `node --test`. Confira as mesmas três perguntas do passo 1 contra esta segunda saída, e responda: o que mudou foi o resultado do cálculo, ou foi o processo que produziu o resultado?

Registre este segundo estado também:

```bash
git add -A && git commit -m "com AGENTS.md robusto"
```

**Observe:** os dois cálculos provavelmente chegam a um resultado correto e equivalente. A diferença que importa está em ter um teste que prova o número antes da implementação, e uma documentação que qualquer pessoa do time lê sem abrir o código.

**Questões exploratórias:**

- Alguma linha do `AGENTS.md` acima é específica da Vetor, ou ela valeria, palavra por palavra, para qualquer projeto JavaScript do seu time?
- E se o `AGENTS.md` só dissesse "escreva código de qualidade, com boas práticas e testes"? Reescreva mentalmente as duas seções acima nessa versão vaga, e responda se ela mudaria alguma decisão real do agente.

## Experimento B

**Objetivo:** conectar um servidor MCP real, sem precisar de conta nem de credencial, e examinar exatamente qual ferramenta o agente chamou e o que voltou dessa chamada, em vez de só o resumo final que o modelo escreve para você.

**Ferramenta usada:** o servidor de referência `@modelcontextprotocol/server-filesystem`, mantido pelo próprio projeto do MCP. Ele expõe operações de leitura e escrita de arquivo (`read_text_file`, `list_directory`, `search_files`, `write_file`, entre outras) restritas a uma ou mais pastas que você escolhe — o mesmo princípio de escopo mínimo visto em [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp).

**Execute:**

**Passo 1:** crie a pasta de teste, fora do projeto `oficina-arnes`, com dois arquivos dentro. Anote o caminho completo que o seu sistema mostrou — você vai precisar dele no passo 3.

=== "macOS/Linux"
    ```bash
    mkdir -p ~/mcp-teste
    echo "Senha do cofre de testes: abacate-37." > ~/mcp-teste/anotacoes.txt
    printf "produto,preco\nteclado,150\nmonitor,900\n" > ~/mcp-teste/precos.csv
    pwd -P  # confirme o caminho completo (ex.: /Users/seu-usuario/mcp-teste)
    ```

=== "Windows (PowerShell)"
    ```powershell
    New-Item -ItemType Directory -Force -Path "$HOME\mcp-teste" | Out-Null
    "Senha do cofre de testes: abacate-37." | Out-File -Encoding utf8 "$HOME\mcp-teste\anotacoes.txt"
    "produto,preco`nteclado,150`nmonitor,900" | Out-File -Encoding utf8 "$HOME\mcp-teste\precos.csv"
    Resolve-Path "$HOME\mcp-teste"  # confirme o caminho completo (ex.: C:\Users\seu-usuario\mcp-teste)
    ```

**Passo 2:** pergunte antes de conectar. Ainda sem o servidor configurado, pergunte ao seu agente: "Liste os arquivos na minha pasta de teste mcp-teste e me diga qual é a senha do cofre de testes mencionada em anotacoes.txt." Guarde a resposta. Ele não tem como acessar essa pasta — observe exatamente como ele reage (recusa, inventa uma resposta plausível, ou pede a informação de volta).

**Passo 3:** conecte o servidor, apontando só para a pasta de teste. Use o caminho completo anotado no passo 1 no lugar de `/caminho/completo/mcp-teste`:

=== "Claude Code"
    ```bash
    claude mcp add --transport stdio arquivos-teste -- npx -y @modelcontextprotocol/server-filesystem /caminho/completo/mcp-teste
    ```
    Grava a configuração em `.mcp.json` (projeto) ou `~/.claude.json` (usuário), na chave `mcpServers`.

=== "Codex CLI"
    ```bash
    codex mcp add arquivos-teste -- npx -y @modelcontextprotocol/server-filesystem /caminho/completo/mcp-teste
    ```
    Grava em `~/.codex/config.toml`, num bloco `[mcp_servers.arquivos-teste]`.

=== "Gemini CLI"
    ```bash
    gemini mcp add arquivos-teste npx -y @modelcontextprotocol/server-filesystem /caminho/completo/mcp-teste
    ```
    Grava em `.gemini/settings.json` ou `~/.gemini/settings.json`, na chave `mcpServers`.

Em Windows, se editar o arquivo de configuração manualmente em vez de usar o comando acima, lembre que caminho dentro de JSON ou TOML precisa da barra invertida duplicada (`C:\\Users\\seu-usuario\\mcp-teste`).

**Passo 4:** recarregue, se a sua ferramenta pedir. A maioria aplica o servidor na próxima mensagem. Se não aplicar, reinicie a sessão do agente.

**Passo 5:** repita a pergunta do passo 2 e examine a chamada. Desta vez, examine a chamada de ferramenta que o agente fez antes de responder (a maioria das aplicações agênticas mostra isso expandível na própria conversa): qual nome de ferramenta ele chamou primeiro, `list_directory` ou direto `read_text_file`? O conteúdo bruto que voltou da chamada bate com o arquivo que você criou?

**Passo 6:** teste o limite do escopo. Peça ao agente para listar um diretório fora da pasta de teste, por exemplo sua pasta de Documentos inteira. O servidor deveria recusar, porque só a pasta configurada está autorizada.

**Questões exploratórias:**

- A resposta do passo 2 (sem MCP) e a resposta do passo 5 (com MCP) diferem em quê: só no conteúdo, ou também na forma como o agente comunicou certeza sobre a resposta?
- O que aconteceu no passo 6 confirma ou contradiz o critério de escopo mínimo de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp)?
- Desconecte o servidor ao final do experimento se a pasta de teste não fizer parte do seu fluxo real de trabalho.

## Experimento C

**Objetivo:** sentir na prática por que isolamento por ramo evita o incidente do [Estudo de caso](estudo-de-caso.md), com dois agentes mexendo no mesmo arquivo ao mesmo tempo.

**Passo 1:** crie os dois ambientes isolados. A partir da raiz do projeto `oficina-arnes` criado no Experimento A:

```bash
git worktree add ../oficina-a -b experimento/a
git worktree add ../oficina-b -b experimento/b
```

**Passo 2:** abra um agente em cada worktree, em duas janelas de terminal, e dê a cada um uma tarefa diferente **sobre o mesmo arquivo**, o que contém `calcularJurosAtraso`:

- No agente de `../oficina-a`: *"Acrescente um parâmetro opcional `taxaDiaria` a `calcularJurosAtraso`, com valor padrão de 0,1% ao dia, e ajuste os testes."*
- No agente de `../oficina-b`: *"Faça `calcularJurosAtraso` lançar um erro se `valorPedido` for negativo, e acrescente um teste para isso."*

Rode os dois ao mesmo tempo, sem esperar o primeiro terminar.

**Passo 3:** confira que nenhum atrapalhou o outro:

```bash
cd ../oficina-a && node --test
cd ../oficina-b && node --test
```

**Observe:** as duas edições coexistem porque cada worktree tem a própria cópia de trabalho do mesmo repositório. O conflito só aparece na hora de juntar os dois ramos, e é lá que ele deve ser resolvido por uma pessoa.

**Passo 4:** provoque o encontro das duas versões, para ver onde o problema realmente mora:

```bash
cd ../oficina-a
git merge experimento/b
```

Se o git acusar conflito no arquivo da função, era exatamente esse conflito que, sem worktree, teria acontecido em silêncio dentro do arquivo, com um agente sobrescrevendo o trabalho do outro.

**Limpeza:** o passo 4 deixa um merge em aberto, então abandone-o antes de remover os worktrees.

```bash
git merge --abort
cd ../oficina-arnes
git worktree remove --force ../oficina-a
git worktree remove --force ../oficina-b
git branch -D experimento/a experimento/b
```

**Questões exploratórias:**

- Em que situação do seu time de verdade esse isolamento evitaria um problema como o do Estudo de caso?
- Isolar por worktree substitui a necessidade de comunicação entre quem mexe em partes relacionadas do sistema, ou reduz um tipo específico de risco?

## Experimento D

**Objetivo:** medir a diferença de tempo e de supervisão entre dois modos de permissão da mesma aplicação agêntica, aplicando o critério de [Autonomia e supervisão](autonomia-e-supervisao.md#quanto-de-autonomia-liberar).

As duas tarefas abaixo são da mesma classe de risco, ambas fáceis de reverter, e diferentes o bastante para o agente não repetir a resposta anterior.

**Passo 1:** no projeto `oficina-arnes`, no modo de **menor** autonomia da sua aplicação agêntica, o que pede confirmação antes de cada edição ou comando, peça:

> Acrescente um teste que cubra o caso de diasAtraso igual a zero em calcularJurosAtraso.

Cronometre do envio do pedido até `node --test` passar, e conte quantas vezes você precisou confirmar algo.

**Passo 2:** volte ao estado inicial:

```bash
git checkout -- juros.test.js
```

**Passo 3:** no modo de **maior** autonomia disponível, com edições automáticas, e de preferência dentro de um worktree descartável como os do Experimento C, peça:

> Crie a função `formatarValorEmReais(valor)`, que formata um número como string no padrão "R$ 0.000,00", com testes.

Cronometre do mesmo jeito e conte as confirmações.

**Passo 4:** compare os dois números e responda: alguma edição saiu diferente do que você esperava? Você percebeu no momento, ou só ao ler o resultado no fim?

**Questões exploratórias:**

- As duas tarefas eram mesmo fáceis de reverter? Se uma delas tocasse código de produção, você manteria o modo do passo 3?
- Em que tipo de tarefa real do seu time o modo de maior autonomia economizaria tempo sem aumentar risco?

## Extensão para o seu repositório

Os quatro experimentos rodaram sobre um projeto criado do zero para todo mundo partir do mesmo estado. O ganho só se realiza quando o mesmo cuidado acontece num repositório que você usa de verdade.

Depois da aula, repita o Experimento A no seu próprio projeto: peça uma função pequena e real do seu domínio sem nenhum arquivo de instrução, depois adapte o `AGENTS.md` robusto usado aqui (ou o que já existir no seu repositório) e peça de novo, numa conversa nova. Se o seu projeto já tem um `AGENTS.md`, compare-o contra o robusto e decida se as duas seções (processo de TDD e documentação nativa) merecem entrar nele.

## Evidência a entregar

Quatro itens, todos verificáveis contra o mesmo projeto criado no início da oficina:

1. Do Experimento A, as respostas às três perguntas do passo 1 contra as do passo 4, e o que mudou entre a saída sem `AGENTS.md` e a saída com ele.
2. Do Experimento B, o nome da ferramenta que o agente chamou no passo 5 e o que aconteceu no passo 6.
3. Do Experimento C, se o `git merge` do passo 4 acusou conflito no arquivo de `calcularJurosAtraso`.
4. Do Experimento D, os dois tempos e as duas contagens de confirmação.

**Próxima página:** [Exercícios](exercicios.md).
