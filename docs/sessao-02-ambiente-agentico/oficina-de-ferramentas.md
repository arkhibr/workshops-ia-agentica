# Oficina de ferramentas — montando o ambiente compartilhado

**Objetivo Bloom:** Compreender e Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Copilot ou Cursor), o git e o Node.js 20 ou superior. Tempo estimado: 30 minutos.

Todos os experimentos rodam sobre o **mesmo projeto de exemplo**, para que cada pessoa parta do mesmo estado e possa comparar o resultado com o do colega ao lado. Antes de começar, clone o repositório do workshop e confirme que os testes passam:

```bash
git clone https://github.com/arkhibr/workshops-ia-agentica.git
cd workshops-ia-agentica/exemplo/vetor
node --version   # precisa mostrar v20 ou superior
npm test         # deve terminar com 6 testes passando
```

O projeto não tem dependências, então não existe `npm install` nem espera de instalação. `exemplo/vetor` é a versão executável da Vetor, a plataforma fictícia de e-commerce B2B que acompanha o workshop: a regra de desconto por faixa de valor, seis testes e nada mais. A função `calcularDesconto` recebe um parâmetro `tipoCliente` que ela não usa, e essa lacuna é proposital — a faixa de 20% para clientes de atacado acima de R$ 10.000,00 é justamente o que os experimentos vão pedir ao agente.

Quem preferir trabalhar no próprio repositório encontra, no fim da página, a extensão que leva o resultado para lá. Faça isso depois de rodar os experimentos no exemplo, para não perder a base de comparação.

Onde os comandos diferem entre sistemas, a página traz as duas versões em abas — escolha a do seu sistema antes de copiar.

**Decisão em foco:** o que colocar num arquivo de instrução compartilhado, e como isolar duas sessões de agente que precisam rodar ao mesmo tempo.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimentos A, B e C, para sair da sessão com um arquivo de instrução real, um servidor MCP conectado e testado, e um worktree testado.
- **Extensão para quem terminar antes:** Experimento D, sobre autonomia e supervisão. Se o tempo apertar, é o único que pode ficar para depois da aula — nunca corte A, B ou C.

## Experimento A — escreva o AGENTS.md do projeto Vetor

**Objetivo:** produzir um arquivo de instrução que muda comportamento real do agente, e comprovar a mudança comparando duas saídas para o mesmo pedido.

**Passo 1:** confirme o ponto de partida. Dentro de `workshops-ia-agentica/exemplo/vetor`:

```bash
npm test
```

Devem passar seis testes. Se algum falhar, resolva antes de seguir: os passos seguintes comparam contra este estado.

**Passo 2:** peça a mudança **sem** arquivo de instrução. Abra o agente nesta pasta e envie exatamente este pedido:

> Implemente a faixa de desconto de atacado na função `calcularDesconto`.

Anote quatro coisas da resposta, porque são elas que você vai comparar no Passo 5:

- Qual valor ele assumiu para o tipo de cliente: `'atacado'`, `'Atacado'`, `'ATACADO'` ou outro?
- Ele aplicou o teto de R$ 1.000,00 também à faixa de atacado?
- A partir de que valor ele começou a faixa? A regra da Vetor diz acima de R$ 10.000,00.
- Ele rodou algum comando para verificar o resultado, e qual?

**Passo 3:** desfaça a alteração, para o próximo passo começar do mesmo lugar:

```bash
git checkout -- src/desconto.js
npm test
```

**Passo 4:** escreva o arquivo de instrução. Crie `AGENTS.md` dentro de `exemplo/vetor`, com no máximo quatro seções. Escreva as linhas abaixo com suas palavras, sem copiar literalmente — o exercício é decidir o que entra:

- o comando de teste é `npm test`, e não existe script de compilação;
- `tipoCliente` chega sempre em minúsculas, `'padrao'` ou `'atacado'`;
- o teto de desconto por pedido vale para todas as faixas, inclusive a de atacado;
- os arquivos em `test/` não devem ser alterados sem pedido explícito.

Para cada linha escrita, pergunte: o agente tomaria uma decisão diferente sem ela? Se não, apague a linha.

**Passo 5:** repita o pedido do Passo 2, palavra por palavra, e compare contra as quatro anotações.

**Observe:** a diferença mais provável não é o desconto sair certo ou errado, e sim a quantidade de suposições que o agente precisou fazer sozinho. Conte quantas das quatro anotações mudaram.

**Questões exploratórias:**

- Alguma linha do seu `AGENTS.md` é genérica o suficiente para valer para qualquer projeto? Isso é sinal de que ela não diz nada específico.
- A convenção de `tipoCliente` em minúsculas não está escrita em lugar nenhum do código. Que outras convenções do seu projeto real vivem só na cabeça das pessoas?

## Experimento B — conecte e examine um servidor MCP real

**Objetivo:** conectar um servidor MCP real, sem precisar de conta nem de credencial, e examinar exatamente qual ferramenta o agente chamou e o que voltou dessa chamada — não só o resumo final que o modelo escreve para você.

**Ferramenta usada:** o servidor de referência `@modelcontextprotocol/server-filesystem`, mantido pelo próprio projeto do MCP. Ele expõe operações de leitura e escrita de arquivo (`read_text_file`, `list_directory`, `search_files`, `write_file`, entre outras) restritas a uma ou mais pastas que você escolhe — o mesmo princípio de escopo mínimo visto em [MCP e ferramentas externas](mcp.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp).

**Execute:**

**Passo 1:** crie a pasta de teste. Fora do repositório atual, com dois arquivos dentro. Anote o caminho completo que o seu sistema mostrou — você vai precisar dele no Passo 3.

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

**Passo 3:** conecte o servidor. Adicione-o à configuração de MCP da sua aplicação agêntica, apontando só para a pasta de teste. Use o caminho completo anotado no Passo 1 — em JSON, caminho de Windows precisa da barra invertida duplicada:

=== "macOS/Linux"
    ```json
    {
      "mcpServers": {
        "arquivos-teste": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/seu-usuario/mcp-teste"]
        }
      }
    }
    ```

=== "Windows"
    ```json
    {
      "mcpServers": {
        "arquivos-teste": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\seu-usuario\\mcp-teste"]
        }
      }
    }
    ```

**Passo 4:** recarregue. Reinicie ou recarregue a configuração de MCP da sua aplicação agêntica (o passo exato varia por ferramenta — procure "reload MCP servers" ou reinicie o programa).

**Passo 5:** repita a pergunta e examine a chamada. A mesma pergunta do Passo 2. Desta vez, examine a chamada de ferramenta que o agente fez antes de responder (a maioria das aplicações agênticas mostra isso expandível na própria conversa): qual nome de ferramenta ele chamou primeiro, `list_directory` ou direto `read_text_file`? O conteúdo bruto que voltou da chamada bate com o arquivo que você criou?

**Passo 6:** teste o limite do escopo. Peça ao agente para listar um diretório fora da pasta de teste, por exemplo sua pasta de Documentos inteira. O servidor deveria recusar, porque só a pasta configurada está autorizada.

**Questões exploratórias:**

- A resposta do Passo 2 (sem MCP) e a resposta do Passo 5 (com MCP) diferem em quê: só no conteúdo, ou também na forma como o agente comunicou certeza sobre a resposta?
- O que aconteceu no Passo 6 confirma ou contradiz o critério de escopo mínimo de [MCP e ferramentas externas](mcp.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp)?
- Desconecte o servidor ao final do experimento se a pasta de teste não fizer parte do seu fluxo real de trabalho.

## Experimento C — isole duas sessões por worktree

**Objetivo:** sentir na prática por que isolamento por ramo evita o incidente do [Estudo de caso](estudo-de-caso.md), com dois agentes mexendo no mesmo arquivo ao mesmo tempo.

**Passo 1:** crie os dois ambientes isolados. A partir da raiz do repositório clonado (`workshops-ia-agentica`, não de dentro de `exemplo/vetor`):

```bash
git worktree add ../vetor-a -b experimento/a
git worktree add ../vetor-b -b experimento/b
```

**Passo 2:** abra um agente em cada worktree, em duas janelas de terminal, e dê a cada um uma tarefa diferente **sobre o mesmo arquivo** `exemplo/vetor/src/desconto.js`:

- No agente de `../vetor-a`: *"Implemente a faixa de atacado de 20% acima de R$ 10.000,00 em `calcularDesconto`, respeitando o teto."*
- No agente de `../vetor-b`: *"Faça `calcularDesconto` recusar `tipoCliente` diferente de 'padrao' e 'atacado', lançando TypeError, e acrescente um teste para isso."*

Rode os dois ao mesmo tempo, sem esperar o primeiro terminar.

**Passo 3:** confira que nenhum atrapalhou o outro:

```bash
cd ../vetor-a && npm test --prefix exemplo/vetor
cd ../vetor-b && npm test --prefix exemplo/vetor
```

**Observe:** as duas edições coexistem porque cada worktree tem a própria cópia de trabalho do mesmo repositório. O conflito só aparece na hora de juntar os dois ramos, e é lá que ele deve ser resolvido por uma pessoa.

**Passo 4:** provoque o encontro das duas versões, para ver onde o problema realmente mora:

```bash
cd ../vetor-a
git merge experimento/b
```

Se o git acusar conflito em `desconto.js`, era exatamente esse conflito que, sem worktree, teria acontecido em silêncio dentro do arquivo, com um agente sobrescrevendo o trabalho do outro.

**Limpeza:** o Passo 4 deixa um merge em aberto, então abandone-o antes de remover os worktrees.

```bash
git merge --abort
cd ../workshops-ia-agentica
git worktree remove --force ../vetor-a
git worktree remove --force ../vetor-b
git branch -D experimento/a experimento/b
```

**Questões exploratórias:**

- Em que situação do seu time de verdade esse isolamento evitaria um problema como o do Estudo de caso?
- Isolar por worktree substitui a necessidade de comunicação entre quem mexe em partes relacionadas do sistema, ou reduz um tipo específico de risco?

## Experimento D — compare dois níveis de autonomia

**Objetivo:** medir a diferença de tempo e de supervisão entre dois modos de permissão da mesma aplicação agêntica, aplicando o critério de [Autonomia e supervisão](autonomia-e-supervisao.md#quanto-de-autonomia-liberar).

As duas tarefas abaixo são da mesma classe de risco, ambas fáceis de reverter, e diferentes o bastante para o agente não repetir a resposta anterior.

**Passo 1:** em `exemplo/vetor`, no modo de **menor** autonomia da sua aplicação agêntica, o que pede confirmação antes de cada edição ou comando, peça:

> Acrescente um teste que cubra exatamente o valor de fronteira R$ 500,01.

Cronometre do envio do pedido até `npm test` passar, e conte quantas vezes você precisou confirmar algo.

**Passo 2:** volte ao estado inicial:

```bash
git checkout -- test/desconto.test.js
```

**Passo 3:** no modo de **maior** autonomia disponível, com edições automáticas, e de preferência dentro de um worktree descartável como os do Experimento C, peça:

> Crie a função `descricaoFaixa(valorTotal)`, que devolve o nome da faixa de desconto do pedido, com testes.

Cronometre do mesmo jeito e conte as confirmações.

**Passo 4:** compare os dois números e responda: alguma edição saiu diferente do que você esperava? Você percebeu no momento, ou só ao ler o resultado no fim?

**Questões exploratórias:**

- As duas tarefas eram mesmo fáceis de reverter? Se uma delas tocasse código de produção, você manteria o modo do Passo 3?
- Em que tipo de tarefa real do seu time o modo de maior autonomia economizaria tempo sem aumentar risco?

## Extensão: leve o resultado para o seu repositório

Os quatro experimentos rodaram sobre a Vetor para todo mundo partir do mesmo estado. O ganho só se realiza quando o mesmo trabalho acontece num repositório que você usa de verdade.

Depois da aula, repita o Experimento A no seu próprio projeto: escreva o `AGENTS.md` dele, com no máximo quatro seções, e submeta o arquivo no mesmo *pull request* da próxima mudança de convenção. Se o seu projeto é privado, a evidência a entregar é a lista de quantas linhas você escreveu e quantas você apagou por não mudarem decisão nenhuma do agente.

## Evidência a entregar

Quatro itens, todos verificáveis contra o mesmo projeto de exemplo:

1. O `AGENTS.md` escrito no Experimento A, e quantas das quatro anotações do Passo 2 mudaram no Passo 5.
2. Do Experimento B, o nome da ferramenta que o agente chamou no Passo 5 e o que aconteceu no Passo 6.
3. Do Experimento C, se o `git merge` do Passo 4 acusou conflito em `desconto.js`.
4. Do Experimento D, os dois tempos e as duas contagens de confirmação.

**Próxima página:** [Exercícios](exercicios.md).
