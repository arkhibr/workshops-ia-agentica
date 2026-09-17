# Oficina de ferramentas

**Objetivo Bloom:** Compreender e Aplicar.

Nos próximos 45 minutos cada participante executa o mesmo pedido cinco vezes, acrescentando uma peça de arnês por vez, e mede o que cada peça muda no resultado. O entregável de toda rodada é uma pasta de trabalho do Excel. Ninguém precisa ler nem escrever código para participar: a conferência é abrir o arquivo e comparar números.

A oficina tem dois pilares. O primeiro gera o caso, uma planilha de pedidos da Vetor. O segundo aplica as camadas de arnês sobre esse mesmo caso, uma de cada vez.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (**Claude Code, Codex CLI ou Gemini CLI**), o Node.js 20 ou superior e um programa de planilha (Excel, LibreOffice Calc ou Google Sheets). Tempo estimado: 45 minutos.

Todos os experimentos partem de uma **pasta vazia**, criada durante a própria oficina. Ninguém clona nada pronto:

```bash
mkdir oficina-arnes && cd oficina-arnes
git init
node --version   # precisa mostrar v20 ou superior
```

Onde os comandos diferem entre sistemas, a página traz as versões em abas. Escolha a do seu sistema antes de copiar. Onde diferem por ferramenta de agente, o mesmo vale para Claude Code, Codex CLI e Gemini CLI.

**Decisão em foco:** que peça do arnês é responsável por cada erro que o agente comete num fechamento mensal, e em que ordem vale a pena acrescentá-las.

## Roteiro sugerido para a sessão

- **Essencial em aula:** o Pilar 1 e as camadas 0 a 4 do Pilar 2, na ordem. A curva só é visível se as cinco rodadas usarem o mesmo pedido e forem medidas com a mesma régua.
- **Exploração em dupla:** a comparação das linhas do placar entre as duas pessoas ao fim da camada 4. Saídas diferentes para o mesmo arnês são o dado mais interessante da oficina.
- **Extensão para depois da aula:** a seção final, com isolamento por ramo, autonomia e a transposição para um repositório de verdade.

## A régua, fixada antes da primeira rodada

A Sessão 1 mostrou um agente sem nenhum contexto produzindo código tão bom quanto o de um pedido caprichado. Aquilo não foi acidente. Quando a tarefa é conhecida do mundo inteiro, o modelo já sabe a resposta e nenhuma peça de arnês acrescenta informação. A oficina de hoje escolhe de propósito uma tarefa do tipo oposto: a resposta certa depende de regras que só existem dentro da Vetor.

Três decisões de medição, valendo para as cinco rodadas:

1. **O critério está fixado antes de rodar.** O placar abaixo é preenchido logo depois de cada camada, sem voltar atrás para reinterpretar uma rodada anterior à luz da seguinte.
2. **Inventar conta como erro.** Uma faixa de desconto que ninguém pediu é dinheiro a menos no caixa da Vetor, então ela entra no placar como falha, e não como iniciativa.
3. **Duas rodadas por camada, em conversas novas.** Um acerto isolado pode ser sorte. Reprodutibilidade é o que o arnês compra, e ela só aparece na segunda rodada.

| Camada | Abriu no Excel? | Stack do time? | Faixas certas? | Armadilhas pegas (0–4) | Duas rodadas iguais? |
|---|---|---|---|---|---|
| 0 — modelo sozinho | | | | | |
| 1 — dados | | | | | |
| 2 — instrução | | | | | |
| 3 — ferramenta | | | | | |
| 4 — verificação | | | | | |

## O caso: fechamento de descontos da Vetor

A **Vetor** é uma plataforma fictícia de e-commerce B2B que atravessa o workshop, com clientes de dois tipos: padrão e atacado. O pedido ao agente é sempre este, palavra por palavra, nas cinco camadas:

> Faça o fechamento de descontos de setembro de 2026 da Vetor e me entregue uma pasta de trabalho do Excel com o valor final por pedido e um resumo por cliente.

**Passo 1 — salve os dados do caso.** Copie o bloco abaixo para um editor de texto e salve como `pedidos-setembro.csv` dentro da pasta `oficina-arnes`, em UTF-8. São 24 pedidos.

```text
pedido,cliente,tipo,quantidade,valor_unitario,data,status
VT-1001,Metalúrgica Andrade,atacado,60,82.40,2026-09-02,confirmado
VT-1002,Papelaria Sul,padrão,12,34.90,2026-09-02,confirmado
VT-1003,Construtora Lemos,atacado,200,15.75,2026-09-03,confirmado
VT-1004,Óptica Vieira,padrão,30,118.00,2026-09-04,confirmado
VT-1005,Farmácia Tavares,padrão,5,219.90,2026-09-05,cancelado
VT-1006,Metalúrgica Andrade,atacado,49,82.40,2026-09-08,confirmado
VT-1007,Papelaria Sul,padrão,29,34.90,2026-09-09,confirmado
VT-1008,Construtora Lemos,atacado,120,15.75,2026-09-10,confirmado
VT-1009,Óptica Vieira,padrão,8,-450.00,2026-09-11,confirmado
VT-1010,Farmácia Tavares,padrão,44,27.30,2026-09-12,confirmado
VT-1011,Metalúrgica Andrade,atacado,210,9.80,2026-09-15,confirmado
VT-1012,Papelaria Sul,padrão,60,34.90,2026-09-15,cancelado
VT-1013,Construtora Lemos,atacado,75,41.20,2026-09-16,confirmado
VT-1014,Óptica Vieira,padrão,3,890.00,2026-09-17,confirmado
VT-1015,Farmácia Tavares,padrão,130,12.45,2026-09-18,confirmado
VT-1016,Metalúrgica Andrade,atacado,18,82.40,2026-09-19,confirmado
VT-1017,Papelaria Sul,padrão,95,7.60,2026-09-22,confirmado
VT-1018,Construtora Lemos,atacado,340,15.75,2026-09-23,confirmado
VT-1019,Óptica Vieira,padrão,22,118.00,2026-09-24,cancelado
VT-1020,Farmácia Tavares,padrão,67,27.30,2026-09-25,confirmado
VT-1021,Metalúrgica Andrade,atacado,199,9.80,2026-09-26,confirmado
VT-1022,Papelaria Sul,padrão,40,34.90,2026-09-29,confirmado
VT-1023,Construtora Lemos,atacado,55,41.20,2026-09-30,confirmado
VT-1024,Óptica Vieira,padrão,25,118.00,2026-10-02,confirmado
```

**As quatro armadilhas.** Elas estão plantadas nas 24 linhas, e nenhuma delas é avisada ao agente em nenhuma camada. É a contagem de quantas cada camada captura que forma a coluna central do placar.

| # | Armadilha | Onde está |
|---|---|---|
| 1 | Três pedidos com `status` cancelado, que ficam fora do fechamento | VT-1005, VT-1012, VT-1019 |
| 2 | Um pedido na fronteira exata de faixa, com 200 unidades, e o vizinho com 199 | VT-1003 e VT-1021 |
| 3 | Um estorno com valor unitário negativo | VT-1009 |
| 4 | Um pedido de outubro no meio do arquivo de setembro | VT-1024 |

### O gabarito

O fechamento correto tem estes números. Confira contra eles depois de cada camada.

| Número de controle | Valor correto |
|---|---|
| Linhas lidas | 24 |
| Pedidos cancelados | 3 |
| Pedidos elegíveis | 21 |
| Clientes no resumo | 5 |
| Total bruto | R$ 43.981,70 |
| Total de desconto | R$ 4.216,57 |
| **Total final** | **R$ 39.762,00** |

Resumo por cliente:

| Cliente | Total final |
|---|---|
| Construtora Lemos | R$ 13.350,00 |
| Metalúrgica Andrade | R$ 13.274,50 |
| Óptica Vieira | R$ 5.347,50 |
| Farmácia Tavares | R$ 4.369,00 |
| Papelaria Sul | R$ 3.421,00 |

!!! warning "O gabarito fica fora do prompt"
    Nunca cole esta tabela no pedido. Ela é a régua de quem conduz o experimento. Colada no prompt, ela vira mais uma peça de contexto e destrói a comparação entre as camadas.

O total final sai idêntico independentemente de o agente arredondar o desconto intermediário para cima, para baixo ou ao mais próximo, porque o arredondamento final em múltiplos de R$ 0,50 absorve a diferença. Uma divergência no total é erro de regra, e nunca de implementação.

**Conferência rápida das faixas.** Em vez de verificar as 21 linhas, olhe três células da aba de fechamento:

| Pedido | Faixa correta | Por quê |
|---|---|---|
| VT-1003 | 18% | atacado com exatamente 200 unidades atinge a faixa superior |
| VT-1021 | 12% | atacado com 199 unidades fica na faixa anterior |
| VT-1006 | 0% | atacado com 49 unidades não atinge faixa nenhuma |

## Pilar 1 — gerar a pasta de trabalho do caso

**Peça do arnês:** ferramentas, na forma de permissão de executar comando e gravar arquivo.

**Objetivo:** produzir o artefato sobre o qual as cinco camadas vão trabalhar, e observar de saída que escrever um arquivo binário depende de o agente ter ferramenta para isso.

**Passo 1:** com a pasta `oficina-arnes` aberta no agente e o CSV salvo dentro dela, peça:

> Converta `pedidos-setembro.csv` numa pasta de trabalho do Excel chamada `pedidos-setembro.xlsx`, com uma única aba chamada `Pedidos`, preservando as 24 linhas e os nomes de coluna exatamente como estão. Não calcule nada.

**Passo 2:** abra `pedidos-setembro.xlsx` no seu programa de planilha e confira três coisas: o arquivo abre sem aviso de formato inválido, a aba se chama `Pedidos`, e as 24 linhas estão lá com os acentos corretos.

**Passo 3:** olhe como o agente resolveu. Ele instalou alguma biblioteca? Escreveu um script? Em que linguagem? Anote a resposta, porque a camada 2 vai mudar exatamente isso.

**Observe:** um agente sem permissão de executar comando não produz `.xlsx` nenhum, porque o formato é um pacote binário. Ele devolve um CSV renomeado, ou um texto explicando como você mesmo poderia fazer. Essa é a primeira lição de arnês da oficina, e ela acontece antes de qualquer regra de negócio entrar em cena.

**Questões exploratórias:**

- A escolha de linguagem do agente foi a mesma da pessoa ao lado? Se não, o que decidiu a escolha dele?
- Se o `.xlsx` tivesse saído corrompido, você descobriria por qual verificação?

## Pilar 2 — as camadas de arnês

As cinco rodadas usam o mesmo pedido em negrito da seção do caso. A única coisa que muda entre elas é o que existe em volta do modelo. Cada passo da oficina acrescenta uma peça, e cada peça decide uma pergunta diferente:

| Passo | Peça do arnês que entra | O que ela decide |
|---|---|---|
| Pilar 1 | Ferramentas (execução) | Se o agente consegue produzir o artefato |
| Camada 0 | Nenhuma | O que o modelo resolve sozinho |
| Camada 1 | Gestão de contexto | Quais fatos entram na janela |
| Camada 2 | Instrução de sistema | Qual política ele aplica aos fatos |
| Camada 3 | Ferramentas (alcance e escopo) | O que ele alcança sem depender de você |
| Camada 4 | Verificação | O que ele confere antes de dizer que terminou |

A coluna do meio usa os nomes da tabela de [componentes do arnês](arnes.md#os-componentes-do-arnes). Duas peças de lá ficam fora desta oficina de propósito, e a seção que fecha o Pilar 2 explica por quê.

### Camada 0 — o modelo sozinho

**Peça do arnês:** nenhuma. É a linha de base contra a qual as outras quatro são medidas.

**Objetivo:** estabelecer a linha de base e, no mesmo passo, separar o que o modelo já sabe do que depende do contexto da Vetor.

**Passo 1 — a tarefa de conhecimento comum.** Numa conversa nova, sem anexar arquivo nenhum, peça:

> Numa planilha do Excel, como eu formato a célula A1, que contém 1234.5, para exibir R$ 1.234,50?

Confira a resposta. Ela deve estar certa, completa e imediata.

**Passo 2 — a tarefa que depende da Vetor.** Na mesma conversa, sem anexar nada, faça o pedido do fechamento. O agente não tem o arquivo de pedidos nem as regras de desconto.

**Passo 3:** confira contra o gabarito e preencha a linha 0 do placar. Anote também em que ponto o agente avisou que estava supondo, se é que avisou.

**Observe:** as duas tarefas foram para o mesmo modelo, no mesmo minuto, com o mesmo arnês (nenhum). A primeira saiu perfeita porque a resposta certa está publicada em milhares de lugares. A segunda saiu inventada porque a resposta certa só existe dentro da Vetor. Essa é a fronteira que decide quando vale a pena investir em arnês, e ela vale para o resto do workshop.

**Questões exploratórias:**

- O agente sinalizou que estava chutando as faixas de desconto, ou apresentou os números com a mesma segurança da resposta do passo 1?
- Um modelo mais capaz melhoraria a resposta do passo 2? Em que direção ele ficaria mais perigoso?

### Camada 1 — dados

**Peça do arnês:** gestão de contexto. O arquivo de pedidos passa a entrar na janela.

**Objetivo:** ver o que muda quando o agente ganha o fato e continua sem a política.

**Passo 1:** numa conversa nova, na pasta `oficina-arnes`, com `pedidos-setembro.xlsx` presente, faça o mesmo pedido do fechamento. Deixe o agente encontrar o arquivo sozinho.

**Passo 2:** abra o resultado e confira contra o gabarito. Depois preencha a linha 1 do placar.

**Passo 3:** rode uma segunda vez, em outra conversa nova, e compare as duas saídas entre si.

**Observe:** os clientes e os valores brutos passam a ser os reais, porque agora eles estão no arquivo. As faixas de desconto continuam vindo de lugar nenhum. É comum a camada 1 pegar zero ou uma armadilha, e produzir um total confiante que erra por milhares de reais.

**Questões exploratórias:**

- As duas rodadas aplicaram as mesmas faixas? Se aplicaram faixas diferentes, o que isso diz sobre entregar esse fechamento para um cliente?
- Qual linha da tabela de [diagnóstico por tipo de falha](arnes.md#diagnosticar-pelo-tipo-de-falha) descreve o erro que você viu aqui?

### Camada 2 — instrução

**Peça do arnês:** instrução de sistema, por dois veículos: o `AGENTS.md`, que o agente lê, e a aba `Regras`, que quem cuida do negócio audita.

**Objetivo:** dar ao agente as regras que só existem dentro da empresa, por dois caminhos ao mesmo tempo, e ver qual deles ele usa.

**Passo 1 — o arquivo de instrução.** Crie `AGENTS.md` na raiz de `oficina-arnes` com este conteúdo:

```markdown
# AGENTS.md

## O que este projeto entrega
O fechamento mensal de descontos da Vetor. O entregável é sempre uma pasta de
trabalho do Excel (`.xlsx`), nunca um relatório em texto na conversa.

## Stack permitido
Scripts auxiliares em JavaScript, com Node.js 20 e a biblioteca `exceljs`.
Este projeto não usa Python em nenhuma hipótese.

## Regras de desconto de setembro de 2026
- Cliente padrão: 6% a partir de 30 unidades no pedido.
- Cliente atacado: 12% a partir de 50 unidades, e 18% a partir de 200 unidades.
- Uma faixa só por pedido, sempre a de maior quantidade atingida. Desconto não acumula.
- O desconto incide sobre o valor bruto, que é quantidade vezes valor unitário.
- O valor final é arredondado para baixo, em múltiplos de R$ 0,50.
- Pedido com status `cancelado` fica fora do fechamento.

## Formato da pasta de trabalho
Três abas, nesta ordem: `Pedidos` (os dados de origem, sem alteração),
`Fechamento` (uma linha por pedido elegível, com valor bruto, faixa aplicada,
desconto e valor final) e `Resumo` (uma linha por cliente, com o total final).
```

**Passo 2 — as mesmas regras dentro da planilha.** Peça ao agente:

> Acrescente a `pedidos-setembro.xlsx` uma aba chamada `Regras`, com uma linha por faixa de desconto: tipo de cliente, quantidade mínima e percentual. Use as faixas descritas no `AGENTS.md`. Não altere a aba `Pedidos`.

Abra a aba `Regras` e confira as quatro linhas. Quem cuida do negócio na Vetor audita a regra aqui, sem abrir arquivo de texto nenhum.

**Passo 3:** numa conversa nova, faça o pedido do fechamento. Confira contra o gabarito, começando pelas três células da conferência rápida de faixas, e preencha a linha 2 do placar.

**Passo 4:** rode uma segunda vez, em outra conversa nova. Compare o formato das duas saídas, e não apenas os números.

**Observe:** três coisas costumam mudar de uma vez. As faixas ficam certas, os cancelados saem do fechamento e a linguagem do script deixa de ser escolha do agente. A fronteira de 200 unidades continua sendo o erro mais frequente mesmo com a regra escrita, porque "a partir de" admite leitura estrita.

**Questões exploratórias:**

- O agente citou o `AGENTS.md`, a aba `Regras`, ou nenhum dos dois ao justificar as faixas? Se as duas fontes discordassem, qual delas você esperaria que prevalecesse?
- Que linha do `AGENTS.md` acima é específica da Vetor, e que linha valeria para qualquer projeto de planilha do seu time?

### Camada 3 — ferramenta

**Peça do arnês:** ferramentas outra vez, agora pelo alcance e pelo limite: um contrato declarado para ler e escrever, restrito a uma pasta.

**Objetivo:** dar ao agente acesso explícito e escopado aos arquivos do caso, e examinar a chamada de ferramenta em vez do resumo que o modelo escreve depois.

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

**Passo 6:** confira contra o gabarito e preencha a linha 3 do placar.

**Observe:** a correção do total tende a mexer pouco nesta camada, e a reprodutibilidade tende a subir, porque o agente para de depender do que você lembrou de colar na conversa. O ganho aqui é de alcance e de limite, e os dois aparecem no mesmo experimento.

**Questões exploratórias:**

- O que aconteceu no passo 5 confirma ou contradiz o critério de escopo mínimo de [MCP e ferramentas externas](mcp.md#avaliar-a-origem-do-servidor-mcp)?
- Desconecte o servidor ao fim da oficina se esta pasta não fizer parte do seu fluxo real de trabalho.

### Camada 4 — verificação

**Peça do arnês:** verificação, que a aritmética do erro composto aponta como a de maior retorno.

**Objetivo:** capturar as duas armadilhas que nenhuma regra previu, que é o retorno que [O arnês do agente](arnes.md#os-componentes-do-arnes) atribui à verificação.

**Passo 1:** acrescente esta seção ao fim do `AGENTS.md`:

```markdown
## Aba Conferência obrigatória
Toda entrega inclui uma quarta aba, `Conferência`, com estes seis números,
calculados a partir da aba `Pedidos`:
- linhas lidas
- pedidos cancelados
- pedidos elegíveis
- pedidos com data fora do mês de fechamento
- pedidos com valor unitário negativo
- soma da coluna de valor final da aba `Fechamento`

Se qualquer uma das duas contagens de anomalia for maior que zero, liste na
conversa os pedidos envolvidos e pare antes de declarar o fechamento pronto.
```

**Passo 2:** numa conversa nova, faça o pedido do fechamento pela última vez.

**Passo 3:** abra a aba `Conferência` e compare os seis números com o gabarito. O agente parou e listou VT-1009 e VT-1024, ou entregou o fechamento como se estivesse tudo normal?

**Passo 4:** preencha a linha 4 do placar e olhe a coluna de armadilhas de cima a baixo.

**Observe:** as duas anomalias estavam no arquivo desde a camada 0 e atravessaram três camadas em silêncio. Nenhuma regra do `AGENTS.md` falava delas, porque ninguém escreve instrução para o caso que não previu. O que as encontra é a obrigação de conferir e relatar, que custa seis linhas de texto.

**Questões exploratórias:**

- Das cinco linhas do placar, qual camada trouxe o maior salto na coluna de armadilhas? Isso bate com a ordem em que um time normalmente investe?
- A aba `Conferência` é uma proteção determinística, ou um pedido que o modelo pode ignorar? Compare com a distinção entre guiar e impor de [O arnês do agente](arnes.md#os-componentes-do-arnes).

### O que a oficina deixa em aberto

Duas peças da tabela de componentes ficaram fora das cinco camadas, e as duas merecem nome antes de a sessão terminar.

A aba `Conferência` da camada 4 pede um comportamento ao modelo. Ela guia, sem impor. Um agente pode ignorá-la, e alguns ignoram. A imposição determinística mora em *hook* e em permissão, na camada de execução, como separa a [distinção entre guiar e impor](arnes.md#os-componentes-do-arnes). Se o seu agente pular a conferência em alguma rodada, é essa peça que está faltando.

Memória fica fora da oficina, como já fica fora da sessão. Cada rodada começa em conversa nova de propósito, para que o placar meça o arnês montado e não o que o agente lembrou da tentativa anterior.

## Extensão para o seu repositório

As cinco camadas rodaram sobre um caso criado do zero para todo mundo partir do mesmo estado. Três desdobramentos, para depois da aula.

**Isolamento por ramo.** A partir da raiz de `oficina-arnes`, crie dois ambientes isolados e dê a cada agente uma tarefa diferente sobre o mesmo arquivo, ao mesmo tempo:

```bash
git worktree add ../oficina-a -b experimento/a
git worktree add ../oficina-b -b experimento/b
```

Num, peça para acrescentar uma faixa de 22% acima de 500 unidades para atacado. No outro, peça para incluir os pedidos cancelados no resumo com valor zero. As duas edições coexistem porque cada worktree tem a própria cópia de trabalho. O conflito aparece na hora de juntar, que é onde uma pessoa deve resolvê-lo. Ao terminar:

```bash
cd ../oficina-arnes
git worktree remove --force ../oficina-a
git worktree remove --force ../oficina-b
git branch -D experimento/a experimento/b
```

**Autonomia.** Repita a camada 4 no modo de menor autonomia da sua aplicação agêntica, contando quantas confirmações você precisou dar, e depois no modo de maior autonomia, dentro de um worktree descartável. Compare os dois tempos e responda se alguma edição saiu diferente do que você esperava.

**O seu projeto.** Escolha uma rotina de planilha que exista de verdade no seu time, uma conciliação ou um relatório mensal, e escreva o `AGENTS.md` dela com as regras que hoje só existem na cabeça de alguém. Depois acrescente a seção de conferência, com os números de controle que você usaria para saber que o resultado está certo. É essa tarefa que faz o arquivo de instrução sobreviver à aula.

## Evidência a entregar

1. O placar preenchido, com as cinco linhas e as cinco colunas.
2. Do Pilar 1, a linguagem em que o agente resolveu a conversão para `.xlsx`, antes de qualquer arquivo de instrução existir.
3. Da camada 0, a diferença entre a resposta do passo 1 e a do passo 2, e se o agente sinalizou que estava supondo.
4. Da camada 3, o nome da ferramenta chamada no passo 4 e o que aconteceu no passo 5.
5. Da camada 4, os seis números da aba `Conferência` e se o agente parou antes de declarar o fechamento pronto.

**Próxima página:** [Exercícios](exercicios.md).
