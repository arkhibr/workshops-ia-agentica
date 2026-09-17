# Oficina de ferramentas

**Objetivo Bloom:** Compreender e Aplicar.

Nos próximos 45 minutos você vai fazer o mesmo pedido a um agente cinco vezes seguidas. O pedido não muda nenhuma palavra. O que muda é o que existe em volta do modelo a cada rodada: na primeira, nada. Depois os dados. Depois as regras escritas. Depois o acesso aos arquivos. Depois a obrigação de conferir o próprio trabalho.

O agente entrega uma planilha do Excel em toda rodada, e você compara as cinco. Não precisa ler nem escrever código para fazer esta oficina. Conferir é abrir o arquivo e olhar os números.

## Ferramenta

Você vai precisar do agente que já usa (**Claude Code, Codex CLI ou Gemini CLI**), do Node.js 20 ou superior e de um programa de planilha (Excel, LibreOffice Calc ou Google Sheets). Tempo estimado: 45 minutos.

Comece por uma pasta vazia, criada agora. Ninguém clona nada pronto:

```bash
mkdir oficina-arnes && cd oficina-arnes
git init
node --version   # precisa mostrar v20 ou superior
```

Quando o comando muda de um sistema para outro, a página traz as duas versões em abas. Escolha a sua antes de copiar. O mesmo vale quando o comando muda de uma ferramenta de agente para outra.

**Decisão em foco:** que peça do arnês é responsável por cada erro que o agente comete num fechamento mensal, e em que ordem vale a pena acrescentá-las.

## Roteiro sugerido para a sessão

- **Essencial em aula:** o Pilar 1 e as cinco rodadas do Pilar 2, na ordem. Use o mesmo pedido nas cinco, senão não dá para comparar nada.
- **Exploração em dupla:** ao fim da última rodada, compare o seu placar com o de quem está do lado. Quando duas pessoas com o mesmo arnês chegam a resultados diferentes, esse é o achado mais interessante do dia.
- **Extensão para depois da aula:** a seção final, com isolamento por ramo, autonomia e a transposição para um repositório de verdade.

## O que é arnês

Quando você pede alguma coisa a um agente, o modelo é só uma peça do que responde. Em volta dele estão a aplicação de linha de comando, o arquivo de instrução, as ferramentas conectadas, o isolamento entre sessões e o nível de permissão. Esse conjunto tem nome: **arnês**. [Vivek Trivedy](../referencia/bibliografia.md#trivedy-the-anatomy-of-an-agent-harness-2026) resume assim: *"if you're not the model, you're the harness"*. Arnês é todo código, configuração e lógica de execução que não é o modelo.

**agente = modelo + arnês**

Isso muda a ordem em que você ataca um problema com agente. Trocar de modelo é caro e aparece na fatura. Mexer no arnês é barato e ninguém vê. Trivedy conta que a mesma família de modelo sai de fora das trinta primeiras posições para as cinco primeiras do Terminal Bench 2.0 sem trocar o modelo, só o arnês. [Addy Osmani](../referencia/bibliografia.md#osmani-agent-harness-engineering-2026) diz o mesmo com outras palavras: um modelo mediano num bom arnês entrega mais que um bom modelo num arnês ruim.

### Por que a oficina é feita em rodadas

O agente executa uma tarefa em muitas etapas, e as chances de cada etapa se multiplicam. Se ele acerta 99% das etapas, uma tarefa de 10 etapas sai inteira certa em 90,4% das vezes. Uma de 50 etapas, em 60,5%. A conta é `0,99` elevado ao número de etapas.

Repare onde isso deixa você. Trocar o modelo não resolve, porque o problema vem do encadeamento, e não da qualidade de cada resposta isolada. O que resolve fica em volta: dar ao agente como conferir o próprio trabalho, parar a tarefa em pontos definidos, deixar cada etapa menos ambígua e manter limpa a janela de contexto. Cada rodada desta oficina acrescenta uma dessas coisas, para você ver quanto ela vale sozinha.

### As sete peças do arnês

Você mexe em quatro delas hoje. Leia a lista inteira antes de começar, porque é ela que transforma "o agente errou" numa pergunta que dá para responder.

| Peça | Pergunta que ela responde | Nesta oficina |
|---|---|---|
| Instrução de sistema | Que convenções e limites governam toda tarefa? | Rodada 2 |
| Ferramentas | O que o agente pode fazer, e com que contrato? | Pilar 1 e rodada 3 |
| Gestão de contexto | O que entra na janela agora, e o que é descartado? | Rodada 1 |
| Verificação | Como o agente confere o que fez antes de avançar? | Rodada 4 |
| Isolamento | Onde o agente roda sem alcançar o trabalho de outra pessoa? | Extensão |
| Autonomia | Que ações ele executa sem pedir aprovação? | Extensão |
| Memória | O que persiste entre execuções, com que autorização? | Fora da oficina |

As duas primeiras levam quase toda a atenção e são as que menos rendem sozinhas. A quarta, verificação, é a que mais rende, pelo motivo da conta acima. A discussão completa, com o diagnóstico por tipo de falha, está em [O arnês do agente](arnes.md).

## O caso: fechamento de descontos da Vetor

A **Vetor** é uma empresa fictícia de e-commerce B2B, usada nos exemplos deste workshop. Ela classifica cada cliente como padrão ou atacado, e dá desconto por faixa de valor do pedido. Estas são as regras:

- O valor bruto do pedido é a quantidade vezes o valor unitário.
- Até R$ 500,00 de valor bruto, nenhum desconto.
- De R$ 500,01 a R$ 2.000,00, 5%.
- De R$ 2.000,01 a R$ 5.000,00, 10%.
- Acima de R$ 5.000,00, 15%.
- Cliente atacado tem uma faixa a mais: 20% acima de R$ 10.000,00.
- O desconto nunca passa de **R$ 1.000,00** por pedido, em nenhuma faixa.
- Pedido com status `cancelado` fica fora do fechamento.

**Leia essas regras, mas não passe nenhuma delas ao agente ainda.** Elas existem só dentro da Vetor, e nenhuma está publicada em lugar nenhum. O agente só recebe esse texto na rodada 2. Até lá, ele trabalha sem saber que essas faixas existem, e é isso que você vai observar.

Nas cinco rodadas você faz este pedido, sem mudar uma palavra:

> Faça o fechamento de descontos de setembro de 2026 da Vetor e me entregue uma pasta de trabalho do Excel com o valor final por pedido e um resumo por cliente.

**Passo 1 — salve os dados do caso.** Copie o bloco abaixo para um editor de texto e salve como `pedidos-setembro.csv` dentro da pasta `oficina-arnes`, em UTF-8. São 22 pedidos de setembro de 2026.

```text
pedido,cliente,tipo,quantidade,valor_unitario,data,status
VT-1001,Metalúrgica Andrade,atacado,150,82.40,2026-09-02,confirmado
VT-1002,Papelaria Sul,padrão,12,34.90,2026-09-02,confirmado
VT-1003,Construtora Lemos,atacado,200,15.75,2026-09-03,confirmado
VT-1004,Óptica Vieira,padrão,30,118.00,2026-09-04,confirmado
VT-1005,Farmácia Tavares,padrão,5,219.90,2026-09-05,cancelado
VT-1006,Metalúrgica Andrade,atacado,100,100.00,2026-09-08,confirmado
VT-1007,Papelaria Sul,padrão,30,34.90,2026-09-09,confirmado
VT-1008,Construtora Lemos,atacado,120,15.75,2026-09-10,confirmado
VT-1010,Farmácia Tavares,padrão,44,27.30,2026-09-12,confirmado
VT-1011,Metalúrgica Andrade,atacado,210,9.80,2026-09-15,confirmado
VT-1012,Papelaria Sul,padrão,60,34.90,2026-09-15,cancelado
VT-1013,Construtora Lemos,atacado,75,41.20,2026-09-16,confirmado
VT-1014,Óptica Vieira,padrão,8,890.00,2026-09-17,confirmado
VT-1015,Farmácia Tavares,padrão,132,12.45,2026-09-18,confirmado
VT-1016,Metalúrgica Andrade,atacado,18,82.40,2026-09-19,confirmado
VT-1017,Papelaria Sul,padrão,95,7.60,2026-09-22,confirmado
VT-1018,Construtora Lemos,atacado,700,15.75,2026-09-23,confirmado
VT-1019,Óptica Vieira,padrão,22,118.00,2026-09-24,cancelado
VT-1020,Farmácia Tavares,padrão,68,27.30,2026-09-25,confirmado
VT-1021,Metalúrgica Andrade,atacado,510,20.00,2026-09-26,confirmado
VT-1022,Papelaria Sul,padrão,40,12.50,2026-09-29,confirmado
VT-1023,Construtora Lemos,atacado,55,41.20,2026-09-30,confirmado
```

## Como conferir cada rodada

Repare que as regras de desconto da Vetor são arbitrárias. Nenhum padrão de mercado manda cortar o desconto em R$ 1.000,00 por pedido, nem dar uma faixa extra de 20% ao atacado acima de R$ 10.000,00. O agente não tem como acertar isso antes de alguém escrever a regra para ele, e um modelo mais capaz só chuta com mais convicção. Foi por isso que escolhi este caso para a oficina.

Tome cuidado com um erro de avaliação aqui. Se você julgar as saídas por qual parece melhor, a rodada sem arnês nenhum costuma ganhar, porque um agente sem regra escreve mais: inventa faixas, acrescenta colunas e devolve um relatório mais completo que o correto. Compare sempre contra o [gabarito](#gabarito), no fim desta página.

Duas regras para preencher o placar.

Faixa que o agente inventou conta como erro, mesmo quando é defensável e mesmo quando um analista humano teria suposto a mesma coisa. Em fechamento, desconto que ninguém aprovou sai do caixa.

Faça cada rodada duas vezes, em conversas separadas. A segunda custa colar o mesmo pedido de novo, e é ela que mostra se o resultado se repete.

| Rodada | Abriu no Excel? | Stack do time? | Faixas certas? | Total bate com o gabarito? | As duas iguais? |
|---|---|---|---|---|---|
| 0 — modelo sozinho | | | | | |
| 1 — dados | | | | | |
| 2 — instrução | | | | | |
| 3 — ferramenta | | | | | |
| 4 — verificação | | | | | |

## Pilar 1 — gerar a pasta de trabalho do caso

**Peça do arnês: ferramentas.** Ferramenta é uma coisa que o agente pode fazer além de escrever texto, com um contrato declarado: um nome, os parâmetros que ela aceita e o que ela devolve. Rodar um comando no terminal é uma ferramenta. Gravar um arquivo é outra. Você vai precisar das duas aqui, porque um arquivo do Excel é um conjunto de documentos XML dentro de um zip, e nenhum modelo escreve isso digitando na conversa.

**Objetivo:** montar a planilha que as cinco rodadas vão usar, e descobrir logo se o seu agente consegue gravar um arquivo.

**Passo 1:** com a pasta `oficina-arnes` aberta no agente e o CSV salvo dentro dela, peça:

> Converta `pedidos-setembro.csv` numa pasta de trabalho do Excel chamada `pedidos-setembro.xlsx`, com uma única aba chamada `Pedidos`, preservando as 22 linhas e os nomes de coluna exatamente como estão. Não calcule nada.

**Passo 2:** abra `pedidos-setembro.xlsx` no seu programa de planilha e confira três coisas: o arquivo abre sem aviso de formato inválido, a aba se chama `Pedidos`, e as 22 linhas estão lá com os acentos corretos.

**Passo 3:** olhe como o agente resolveu. Ele instalou alguma biblioteca? Escreveu um script? Em que linguagem? Anote a resposta, porque a rodada 2 vai mudar exatamente isso.

**Observe:** um agente sem permissão de executar comando não entrega `.xlsx` nenhum. Ele devolve um CSV renomeado, ou um texto explicando como você mesmo poderia fazer. Repare que isso não tem nada a ver com as regras de desconto, que ainda nem apareceram. É só ferramenta.

**Questões exploratórias:**

- A escolha de linguagem do agente foi a mesma da pessoa ao lado? Se não, o que decidiu a escolha dele?
- Se o `.xlsx` tivesse saído corrompido, você descobriria por qual verificação?

## Pilar 2 — uma peça de arnês por rodada

As cinco rodadas usam o mesmo pedido em negrito da seção do caso. A única coisa que muda entre elas é o que existe em volta do modelo. Cada passo da oficina acrescenta uma peça, e cada peça decide uma pergunta diferente:

| Passo | Peça do arnês que entra | O que ela decide |
|---|---|---|
| Pilar 1 | Ferramentas (execução) | Se o agente consegue gravar o arquivo |
| Rodada 0 | Nenhuma | O que o modelo resolve sozinho |
| Rodada 1 | Gestão de contexto | Quais fatos entram na janela |
| Rodada 2 | Instrução de sistema | Qual política ele aplica aos fatos |
| Rodada 3 | Ferramentas (alcance e escopo) | O que ele alcança sem depender de você |
| Rodada 4 | Verificação | O que ele confere antes de dizer que terminou |

A coluna do meio usa os nomes da tabela de [componentes do arnês](arnes.md#os-componentes-do-arnes). Duas peças de lá ficam fora desta oficina de propósito, e a seção que fecha o Pilar 2 explica por quê.

### Rodada 0 — o modelo sozinho

**Peça do arnês: nenhuma.** Esta é a rodada contra a qual você vai comparar as outras quatro. Ela também serve para separar duas situações que as pessoas confundem. Quando a resposta certa está publicada na internet, o modelo já a conhece e nenhum arnês acrescenta nada. Quando a resposta certa só existe dentro de uma empresa, o modelo não tem de onde tirá-la, e é aí que vale gastar tempo com as rodadas seguintes.

**Objetivo:** ver o que o modelo faz sem nenhuma ajuda, em duas tarefas de tipos diferentes.

**Passo 1 — a tarefa de conhecimento comum.** Numa conversa nova, sem anexar arquivo nenhum, peça:

> Numa planilha do Excel, como eu formato a célula A1, que contém 1234.5, para exibir R$ 1.234,50?

Confira a resposta. Ela deve estar certa, completa e imediata.

**Passo 2 — a tarefa que depende da Vetor.** Na mesma conversa, sem anexar nada, faça o pedido do fechamento. O agente não tem o arquivo de pedidos nem as regras de desconto.

**Passo 3:** confira contra o [gabarito](#gabarito) e preencha a linha 0 do placar. Anote também em que ponto o agente avisou que estava supondo, se é que avisou.

**Observe:** você mandou as duas perguntas para o mesmo modelo, no mesmo minuto, sem arnês nenhum. A primeira saiu perfeita porque a resposta está publicada em milhares de lugares. A segunda saiu inventada porque a resposta só existe dentro da Vetor. Guarde essa diferença, porque ela é que diz quando vale a pena montar arnês e quando não vale.

**Questões exploratórias:**

- O agente sinalizou que estava chutando as faixas de desconto, ou apresentou os números com a mesma segurança da resposta do passo 1?
- Um modelo mais capaz melhoraria a resposta do passo 2? Em que direção ele ficaria mais perigoso?

### Rodada 1 — dados

**Peça do arnês: gestão de contexto.** Janela de contexto é tudo que chega ao modelo numa execução: a instrução, o histórico da conversa, o conteúdo dos arquivos que ele leu e o resultado das ferramentas que ele chamou. Gerir contexto é escolher o que entra aí e o que fica de fora. Nesta rodada entra o arquivo de pedidos, e mais nada. Você vai dar a ele os dados sem dar as regras, e o resultado mostra que uma coisa não substitui a outra.

**Objetivo:** ver o que muda quando o agente recebe os dados e continua sem as regras.

**Passo 1:** numa conversa nova, na pasta `oficina-arnes`, com `pedidos-setembro.xlsx` presente, faça o mesmo pedido do fechamento. Deixe o agente encontrar o arquivo sozinho.

**Passo 2:** abra o resultado e confira contra o [gabarito](#gabarito). Depois preencha a linha 1 do placar.

**Passo 3:** rode uma segunda vez, em outra conversa nova, e compare as duas saídas entre si.

**Observe:** os clientes e os valores brutos passam a ser os reais, porque agora eles estão no arquivo. As faixas de desconto continuam vindo de lugar nenhum. O total sai com aparência impecável e erra por milhares de reais.

**Questões exploratórias:**

- As duas rodadas aplicaram as mesmas faixas? Se aplicaram faixas diferentes, o que isso diz sobre entregar esse fechamento para um cliente?
- Qual linha da tabela de [diagnóstico por tipo de falha](arnes.md#diagnosticar-pelo-tipo-de-falha) descreve o erro que você viu aqui?

### Rodada 2 — instrução

**Peça do arnês: instrução de sistema.** É um texto que o agente lê antes de cada pedido, e que vale para todas as tarefas do projeto. Ele existe para responder o que os dados sozinhos não respondem. Aqui você escreve as regras em dois lugares ao mesmo tempo. O `AGENTS.md` fica na raiz da pasta, e é o que o agente lê. A aba `Regras` fica dentro da planilha, onde quem cuida do negócio consegue conferir a faixa sem abrir arquivo de texto. Nenhum dos dois obriga o agente a nada, os dois só pedem, e é isso que você vai observar.

**Objetivo:** escrever as regras da Vetor em dois lugares e ver qual deles o agente usa.

**Passo 1 — o arquivo de instrução.** Crie `AGENTS.md` na raiz de `oficina-arnes` com este conteúdo:

```markdown
# AGENTS.md

## O que este projeto entrega
O fechamento mensal de descontos da Vetor. O entregável é sempre uma pasta de
trabalho do Excel (`.xlsx`), nunca um relatório em texto na conversa.

## Stack permitido
Scripts auxiliares em JavaScript, com Node.js 20 e a biblioteca `exceljs`.
Este projeto não usa Python em nenhuma hipótese.

## Regras de desconto da Vetor
- O valor bruto do pedido é a quantidade vezes o valor unitário.
- Até R$ 500,00 de valor bruto, nenhum desconto.
- De R$ 500,01 a R$ 2.000,00, 5%.
- De R$ 2.000,01 a R$ 5.000,00, 10%.
- Acima de R$ 5.000,00, 15%.
- Cliente atacado tem uma faixa a mais: 20% acima de R$ 10.000,00.
- O desconto nunca passa de R$ 1.000,00 por pedido, em nenhuma faixa.
- Pedido com status `cancelado` fica fora do fechamento.

## Formato da pasta de trabalho
Três abas, nesta ordem: `Pedidos` (os dados de origem, sem alteração),
`Fechamento` (uma linha por pedido elegível, com valor bruto, faixa aplicada,
desconto e valor final) e `Resumo` (uma linha por cliente, com o total final).
```

**Passo 2 — as mesmas regras dentro da planilha.** Peça ao agente:

> Acrescente a `pedidos-setembro.xlsx` uma aba chamada `Regras`, com uma linha por faixa de desconto: tipo de cliente, quantidade mínima e percentual. Use as faixas descritas no `AGENTS.md`. Não altere a aba `Pedidos`.

Abra a aba `Regras` e confira as quatro linhas. Quem cuida do negócio na Vetor audita a regra aqui, sem abrir arquivo de texto nenhum.

**Passo 3:** numa conversa nova, faça o pedido do fechamento. Confira contra o [gabarito](#gabarito), começando pelas três células da conferência rápida de faixas, e preencha a linha 2 do placar.

**Passo 4:** rode uma segunda vez, em outra conversa nova. Compare o formato das duas saídas, e não apenas os números.

**Observe:** três coisas costumam mudar de uma vez. As faixas ficam certas, os pedidos cancelados saem do fechamento e o agente para de escolher a linguagem por conta própria. Fique de olho no pedido de 200 unidades, que continua sendo o erro mais comum mesmo com a regra escrita. "A partir de" também pode ser lido como "acima de", e aí 200 unidades cai na faixa de baixo.

**Questões exploratórias:**

- O agente citou o `AGENTS.md`, a aba `Regras`, ou nenhum dos dois ao justificar as faixas? Se as duas fontes discordassem, qual delas você esperaria que prevalecesse?
- Que linha do `AGENTS.md` acima é específica da Vetor, e que linha valeria para qualquer projeto de planilha do seu time?

### Rodada 3 — ferramenta

**Peça do arnês: ferramentas de novo, agora com alcance e limite.** O Model Context Protocol é um padrão aberto. Cada agente e cada ferramenta implementam a mesma interface uma vez só, em vez de uma integração feita sob medida para cada par. Quando você conecta um servidor MCP, o agente ganha um conjunto de operações novas, e você decide a que pastas elas se aplicam. Nesta rodada você mede as duas pontas disso: o que o agente passa a alcançar sozinho e onde ele é barrado.

**Objetivo:** dar ao agente acesso aos arquivos do caso, restrito a uma pasta, e olhar a chamada de ferramenta em vez de só ler o resumo que ele escreve depois.

**Ferramenta usada:** o servidor de referência `@modelcontextprotocol/server-filesystem`, mantido pelo próprio projeto do MCP. Ele expõe operações de leitura e escrita restritas às pastas que você autorizar, o mesmo princípio de escopo mínimo de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp).

**Passo 1:** descubra o caminho completo da pasta `oficina-arnes`.

=== "macOS/Linux"
    ```bash
    pwd -P   # ex.: /Users/seu-usuario/oficina-arnes
    ```

=== "Windows (PowerShell)"
    ```powershell
    Resolve-Path .   # ex.: C:\Users\seu-usuario\oficina-arnes
    ```

**Passo 2:** conecte o servidor apontando só para essa pasta, trocando `/caminho/completo/oficina-arnes` pelo caminho que apareceu.

=== "Claude Code"
    ```bash
    claude mcp add --transport stdio arquivos-vetor -- npx -y @modelcontextprotocol/server-filesystem /caminho/completo/oficina-arnes
    ```
    Grava a configuração em `.mcp.json` (projeto) ou `~/.claude.json` (usuário), na chave `mcpServers`.

=== "Codex CLI"
    ```bash
    codex mcp add arquivos-vetor -- npx -y @modelcontextprotocol/server-filesystem /caminho/completo/oficina-arnes
    ```
    Grava em `~/.codex/config.toml`, num bloco `[mcp_servers.arquivos-vetor]`.

=== "Gemini CLI"
    ```bash
    gemini mcp add arquivos-vetor npx -y @modelcontextprotocol/server-filesystem /caminho/completo/oficina-arnes
    ```
    Grava em `.gemini/settings.json` ou `~/.gemini/settings.json`, na chave `mcpServers`.

Em Windows, se editar o arquivo de configuração à mão em vez de usar o comando acima, lembre que caminho dentro de JSON ou TOML precisa da barra invertida duplicada (`C:\\Users\\seu-usuario\\oficina-arnes`).

**Passo 3:** recarregue, se a sua ferramenta pedir. A maioria aplica o servidor na próxima mensagem.

**Passo 4:** numa conversa nova, faça o pedido do fechamento. Antes de olhar o resultado, expanda a chamada de ferramenta na conversa: qual nome ele chamou primeiro, `list_directory` ou direto `read_text_file`? Ele abriu a aba `Regras` ou só a aba `Pedidos`?

**Passo 5:** teste o limite do escopo. Peça ao agente para listar a sua pasta de Documentos inteira. O servidor deve recusar, porque só `oficina-arnes` está autorizada.

**Passo 6:** confira contra o [gabarito](#gabarito) e preencha a linha 3 do placar.

**Observe:** o total provavelmente não muda muito nesta rodada. O que melhora é a repetição entre as duas execuções, porque o agente para de depender do que você lembrou de colar na conversa. E a recusa do passo 5 mostra que o limite da pasta é real, e não uma promessa no arquivo de instrução.

**Questões exploratórias:**

- O que aconteceu no passo 5 confirma ou contradiz o critério de escopo mínimo de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp)?
- Desconecte o servidor ao fim da oficina se esta pasta não fizer parte do seu fluxo real de trabalho.

### Rodada 4 — verificação

**Peça do arnês: verificação.** É dar ao agente um jeito de conferir o próprio trabalho antes de dizer que terminou. Pela conta do começo da página, é a peça que mais rende das sete, e a que quase ninguém configura.

**Objetivo:** parar de ser você a conferir o resultado à mão.

Nas quatro rodadas anteriores quem conferiu o fechamento foi você, comparando o total contra o [gabarito](#gabarito). Setembro de 2026 é o único mês da Vetor que tem gabarito. Em outubro não vai ter, nem em novembro. A pergunta vira outra: como você confia num número que ninguém conferiu?

**Passo 1:** acrescente esta seção ao fim do `AGENTS.md`:

```markdown
## Aba Conferência obrigatória
Toda entrega inclui uma quarta aba, `Conferência`, com estes cinco números,
recalculados a partir da aba `Pedidos` e sem copiar nada da aba `Fechamento`:
- linhas lidas
- pedidos cancelados
- pedidos elegíveis
- clientes distintos entre os pedidos elegíveis
- soma da coluna de valor final da aba `Fechamento`

Reporte os cinco números na conversa antes de declarar o fechamento pronto.
Se a soma da aba `Conferência` divergir do total da aba `Resumo`, pare e
diga onde está a diferença.
```

**Passo 2:** numa conversa nova, faça o pedido do fechamento pela última vez.

**Passo 3:** leia os cinco números que o agente reportou na conversa, antes de abrir a planilha. Só depois abra o arquivo e confira contra o [gabarito](#gabarito).

**Passo 4:** preencha a linha 4 do placar.

**Observe:** o total provavelmente já estava certo na rodada 3. O que muda aqui é quem descobre isso, e em que momento. Uma conferência que o próprio agente faz e relata continua funcionando em outubro e em novembro, sem ninguém de fora refazendo a conta. Lembre da conta do começo da página: numa tarefa longa, o erro precisa ser pego na etapa em que ele nasce, senão ele atravessa todas as seguintes.

**Passo 5, para ver a conferência trabalhar:** abra o CSV, troque a quantidade do pedido VT-1013 de 75 para 45 e peça o fechamento de novo. O valor bruto cai de R$ 3.090,00 para R$ 1.854,00, e o pedido desce da faixa de 10% para a de 5%. O total correto passa a ser R$ 67.648,74, e o agente relata o novo número sem você ter calculado nada. Desfaça a alteração depois.

**Questões exploratórias:**

- O agente recalculou os cinco números a partir da aba `Pedidos`, ou copiou o que já tinha escrito na aba `Fechamento`? Como você sabe?
- A aba `Conferência` é uma proteção determinística, ou um pedido que o modelo pode ignorar? Compare com a distinção entre guiar e impor de [O arnês do agente](arnes.md#os-componentes-do-arnes).

### Ler o placar

Agora use o placar para diagnosticar. Cada resposta negativa aponta para uma peça do arnês, e a tabela abaixo diz qual. A Sessão 9 retoma esse mesmo raciocínio na depuração de agentes.

| O que você observou | Peça provável | Primeira intervenção |
|---|---|---|
| O `.xlsx` nunca saiu, ou saiu corrompido | ferramentas | conferir permissão de execução e escrita do agente |
| As faixas de desconto mudaram entre duas rodadas | instrução de sistema | tornar a regra explícita, com o número e a fronteira |
| O agente usou clientes que não existem no arquivo | gestão de contexto | garantir que o dado entra na janela, em vez de ser lembrado |
| Ele pediu que você colasse o conteúdo da planilha | ferramentas | dar acesso de leitura escopado à pasta |
| Você só soube que o total estava certo porque tinha o gabarito à mão | verificação | exigir números de controle recalculados da fonte e relatados |
| Ele leu a regra e mesmo assim não aplicou | *hooks* e permissões | impor o limite na camada de execução |

A última linha é a que esta oficina não resolve, e a seção seguinte explica por quê.

### O que a oficina deixa em aberto

Duas peças da tabela de componentes ficaram de fora das cinco rodadas. Vale saber quais são antes de encerrar.

A aba `Conferência` da rodada 4 pede um comportamento ao modelo, e pedido é coisa que dá para ignorar. Alguns agentes ignoram. Quem impõe de verdade é *hook* e permissão, na camada de execução, como separa a [distinção entre guiar e impor](arnes.md#os-componentes-do-arnes). Se o agente pulou a conferência em alguma rodada, foi essa peça que faltou.

Memória fica fora da oficina e fora da sessão. Cada rodada começa em conversa nova justamente para isso: o placar precisa medir o arnês que você montou, e não o que o agente lembrou da tentativa anterior.

## Extensão para o seu repositório

As cinco rodadas usaram um caso criado do zero, para todo mundo partir do mesmo estado. Três coisas para fazer depois da aula.

**Isolamento por ramo.** A partir da raiz de `oficina-arnes`, crie dois ambientes isolados e dê a cada agente uma tarefa diferente sobre o mesmo arquivo, ao mesmo tempo:

```bash
git worktree add ../oficina-a -b experimento/a
git worktree add ../oficina-b -b experimento/b
```

Num deles, peça para acrescentar uma faixa de 22% acima de 500 unidades para atacado. No outro, peça para incluir os pedidos cancelados no resumo com valor zero. As duas edições convivem, porque cada worktree tem a própria cópia de trabalho. O conflito só aparece na hora de juntar os dois ramos, e é lá que uma pessoa resolve. Ao terminar:

```bash
cd ../oficina-arnes
git worktree remove --force ../oficina-a
git worktree remove --force ../oficina-b
git branch -D experimento/a experimento/b
```

**Autonomia.** Repita a rodada 4 no modo de menor autonomia da sua aplicação agêntica, contando quantas confirmações você precisou dar, e depois no modo de maior autonomia, dentro de um worktree descartável. Compare os dois tempos e responda se alguma edição saiu diferente do que você esperava.

**O seu projeto.** Escolha uma rotina de planilha que exista de verdade no seu time, uma conciliação ou um relatório mensal. Escreva o `AGENTS.md` dela com as regras que hoje só existem na cabeça de alguém, e acrescente a seção de conferência com os números de controle que você usaria para saber que o resultado está certo. Essa é a tarefa que faz o arquivo de instrução sobreviver à aula.

## Gabarito

Estes são os números do fechamento correto. Consulte esta seção depois de cada rodada, na hora de conferir, e não antes: quem lê os números certos primeiro deixa de reparar no que o agente inventou.

??? note "Abrir para conferir"

    **Nunca cole esta tabela no pedido ao agente.** Ela é a sua conferência. Dentro do prompt, ela vira mais uma peça de contexto e acaba com a comparação entre as rodadas.

    | Número de controle | Valor correto |
    |---|---|
    | Linhas lidas | 22 |
    | Pedidos cancelados | 3 |
    | Pedidos elegíveis | 19 |
    | Clientes no resumo | 5 |
    | Total bruto | R$ 75.571,00 |
    | Total de desconto | R$ 6.902,56 |
    | **Total final** | **R$ 68.668,44** |

    Resumo por cliente:

    | Cliente | Total final |
    |---|---|
    | Metalúrgica Andrade | R$ 32.821,24 |
    | Construtora Lemos | R$ 19.475,90 |
    | Óptica Vieira | R$ 9.306,00 |
    | Farmácia Tavares | R$ 4.465,95 |
    | Papelaria Sul | R$ 2.599,35 |

    Os 22 pedidos foram escolhidos para que todo desconto caia num número exato de centavos, então não existe arredondamento no meio do caminho e o total só tem um valor certo. Se o total divergir, o erro está na regra que o agente aplicou.

    **Conferência rápida das faixas.** Em vez de verificar as 19 linhas, olhe três células da aba de fechamento:

    | Pedido | Desconto correto | Por quê |
    |---|---|---|
    | VT-1022 | R$ 0,00 | bruto de exatamente R$ 500,00, e a faixa de 5% só começa acima disso |
    | VT-1006 | R$ 1.000,00 | atacado com bruto de exatamente R$ 10.000,00 fica em 15%, porque a faixa de 20% é acima de R$ 10.000,00. Os 15% dariam R$ 1.500,00, e o teto corta em R$ 1.000,00 |
    | VT-1014 | R$ 1.000,00 | cliente padrão, 15% sobre R$ 7.120,00 daria R$ 1.068,00, e o teto corta |

## Evidência a entregar

1. O placar preenchido, com as cinco linhas e as cinco colunas.
2. Do Pilar 1, a linguagem em que o agente resolveu a conversão para `.xlsx`, antes de qualquer arquivo de instrução existir.
3. Da rodada 0, a diferença entre a resposta do passo 1 e a do passo 2, e se o agente sinalizou que estava supondo.
4. Da rodada 2, se o agente citou o `AGENTS.md`, a aba `Regras` ou nenhum dos dois ao justificar as faixas.
5. Da rodada 3, o nome da ferramenta chamada no passo 4 e o que aconteceu no passo 5.
6. Da rodada 4, os cinco números que o agente reportou na conversa e se eles batiam com a planilha.

**Próxima página:** [Exercícios](exercicios.md).
