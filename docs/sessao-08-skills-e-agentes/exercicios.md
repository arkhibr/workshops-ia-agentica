# Exercícios

Tente responder antes de abrir os blocos de feedback. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar), e a sessão inteira treina uma habilidade: preencher a ficha de requisitos de uma skill ou de um agente e conferir se a medição a cumpre. Os exercícios de Aplicar em diante usam situações da ACME, a universidade fictícia desta sessão. Na aula, a atividade de 34 minutos é o exercício-âncora do nível Criar (exercício 12), seguido de 6 minutos de conferência cruzada, e os exercícios 1 a 11 ficam para estudo posterior, com gabarito.

## Recordar

### 1. Os três níveis de carga de uma skill

Nomeie os três níveis de carga de uma skill, diga quando cada um é carregado e informe o custo em tokens de cada nível.

<details>
<summary>Ver resposta</summary>

O nível 1, de metadados, contém `name` e `description`, é carregado sempre, na inicialização, e custa cerca de 100 tokens por skill. O nível 2, de instruções, é o corpo do `SKILL.md`, é carregado quando a skill é acionada e custa menos de 5 mil tokens. O nível 3, de recursos e código, reúne arquivos de referência, modelos e scripts, é carregado sob demanda e não custa nada até o acesso, e no caso dos scripts apenas a saída entra no contexto.

</details>

### 2. Campos obrigatórios e limites

Escreva os campos obrigatórios do `SKILL.md` e os do arquivo de um subagente, com os limites do `name` e do `description` da skill.

<details>
<summary>Ver resposta</summary>

A skill exige `name` e `description`. O `name` aceita até 64 caracteres, apenas letras minúsculas, números e hífens, e não pode conter "anthropic" nem "claude". O `description` não pode ficar vazio, aceita até 1.024 caracteres e diz o que a skill faz e quando usá-la. O subagente também exige apenas `name` e `description`, e os demais campos, como `tools`, `model`, `permissionMode` e `maxTurns`, são opcionais.

</details>

## Compreender

### 3. Skill, subagente ou agente principal

Para cada tarefa da ACME, a universidade fictícia desta sessão, indique o mecanismo mais adequado entre skill, subagente, skill com `context: fork` e agente principal, escreva a razão da escolha pela árvore da seção [Escolher o mecanismo](agentes-e-subagentes.md#escolher-o-mecanismo) e, nas escolhas que não sejam o agente principal, escreva as linhas de front-matter que as configuram. A tarefa A é escrever, a pedido da própria pessoa e toda semana, um resumo da fila de chamados no mesmo formato. A tarefa B é executar a suíte de 600 testes e relatar apenas as falhas, com o mesmo roteiro a cada vez e sem encher a conversa de saída. A tarefa C é decidir com a equipe, em conversa, se a integração entre bolsas e pagamentos usa fila ou arquivo em lote. A tarefa D é revisar uma alteração apenas lendo o código, sem poder editar nada, quando o modelo julgar útil.

<details>
<summary>Ver resposta</summary>

A tarefa A é uma skill de acionamento manual, com `disable-model-invocation: true`, porque se repete, tem procedimento conhecido e formato fixo, a pessoa decide o momento, e o procedimento só ocupa contexto quando acionado. A tarefa B gera muita saída intermediária que a conversa não precisa ler, e apenas o resumo das falhas retorna ao contexto principal, o que pede um subagente ou, como o roteiro é fixo, uma skill com `context: fork`, com `agent` escolhendo o tipo do subagente. A tarefa C fica com o agente principal, porque depende das decisões da equipe a cada passo, e delegar acrescentaria custo sem benefício, de modo que não há front-matter a escrever. A tarefa D é um subagente com `tools: Read, Grep, Glob`, porque a restrição de ferramentas pertence ao arquivo do agente e o modelo decide quando delegar pela `description`. Em cada escolha convém conferir um campo: na A, que o pedido em linguagem natural não aciona a skill, na B, que tudo o que a tarefa precisa chega pelos argumentos, porque o fork não enxerga o histórico, e na D, que o campo está escrito `tools` e não `tool`.

</details>

!!! note "Claude Code e Codex CLI"
    **Claude Code:** os campos usados nestes exercícios constam da [tabela de campos dos subagentes](https://code.claude.com/docs/en/sub-agents#frontmatter-reference) e da [tabela de campos das skills](https://code.claude.com/docs/en/skills#frontmatter-reference).
    **Codex CLI:** o agente é um arquivo TOML em `.codex/agents/`, e a skill fica em `.agents/skills/`, conforme [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) e [Build skills](https://learn.chatgpt.com/docs/build-skills). Nenhum exercício exige o Codex instalado, e os trechos que o executam são opcionais e declaram o pré-requisito.

### 4. Por que vários agentes custam mais

Explique por que um sistema com vários agentes consome mais tokens que um agente único e cite dois tipos de tarefa em que ele não compensa.

<details>
<summary>Ver resposta</summary>

Cada subagente tem uma janela de contexto própria, e os pedidos de todos contam para o consumo, de modo que o total é a soma dos contextos. O relato da Anthropic cita cerca de 4 vezes os tokens de um chat para um agente e cerca de 15 vezes para um sistema com vários agentes. Não compensam as tarefas em que todos os agentes precisam do mesmo contexto ou que têm muitas dependências entre as partes, e a maioria das tarefas de programação, que têm poucas partes realmente paralelas.

</details>

## Aplicar

### 5. Estimar o efeito do cache

**Situação**

Uma skill da ACME envia, em cada execução, um prefixo estável de 40 mil tokens, e a equipe executa a skill 8 vezes seguidas, dentro da vida de 5 minutos do cache. O modelo cobra a leitura do cache a 0,1 do preço-base de entrada, e a escrita de 5 minutos a 1,25.

**Passos**

1. Calcule, em unidades relativas ("1 = preço-base de um token de entrada"), o custo do prefixo nas 8 execuções sem cache.
2. Calcule o custo com cache, contando uma escrita e sete leituras.
3. Calcule a redução percentual e escreva uma frase que diga o que a conta não inclui.

<details>
<summary>Conferir depois de responder</summary>

Sem cache, o custo é 8 × 40 mil × 1 = 320 mil. Com cache, é 40 mil × 1,25 = 50 mil pela escrita, mais 7 × 40 mil × 0,1 = 28 mil pelas leituras, num total de 78 mil. A redução é 1 − 78/320 = 75,6%. A conta considera apenas o prefixo repetido e não inclui os tokens novos de cada execução, os tokens de saída nem a nova escrita quando a pausa entre execuções passa da vida do cache.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Cálculo sem cache | 25% | 320 mil unidades relativas |
| Cálculo com cache | 40% | 50 mil de escrita e 28 mil de leitura, total de 78 mil |
| Redução percentual | 15% | Aproximadamente 75,6% |
| Limite da conta | 20% | Cita ao menos um item fora do cálculo, como tokens de saída ou pausa maior que a vida do cache |

### 6. Escolher modelo e permissões de subagentes

**Situação**

A ACME quer três subagentes: o subagente A busca nos logs de integração as linhas com erro e devolve uma lista, o subagente B revisa a estrutura dos registros de decisão arquitetural e aponta as seções ausentes, e o subagente C avalia se uma decisão arquitetural contradiz as decisões anteriores e escreve uma recomendação.

**Passos**

1. Para cada subagente, escreva o campo `model` que você testaria primeiro e o campo `tools`.
2. Diga em uma frase como a equipe decidiria se o modelo escolhido basta.
3. Indique um subagente que precisa de revisão extra das permissões e o motivo.

<details>
<summary>Conferir depois de responder</summary>

Os subagentes A e B são tarefas de alto volume e saída simples, e o ponto de partida é `model: haiku` com `tools: Read, Grep, Glob`, sem ferramentas de escrita nem de shell. O subagente C exige raciocínio sobre várias decisões, e o ponto de partida é `sonnet`, com subida para `opus` se as avaliações não passarem, também somente com ferramentas de leitura, porque a saída é uma recomendação e não uma edição. A equipe decide com um conjunto próprio de tarefas reais conferidas, comparando o resultado e o custo dos modelos, como na oficina. A revisão extra recai sobre qualquer subagente que ganhe `Bash` ou ferramentas de escrita, porque o alcance de um erro passa a incluir arquivos e comandos.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Modelo por subagente | 30% | Haiku para A e B e Sonnet ou Opus para C, com justificativa por volume e complexidade |
| Ferramentas mínimas | 30% | `tools` explícito e sem escrita nem shell, nos três casos |
| Método de decisão | 25% | Menciona tarefas reais conferidas e comparação de resultado e custo |
| Risco apontado | 15% | Identifica o subagente com mais alcance e a razão |

## Analisar

### 7. Auditar o uso de credenciais

**Situação**

A coordenação da ACME reuniu cinco relatos de como agentes acessam o Azure DevOps da instituição.

- **A.** O agente roda com a autenticação integrada do Windows da pessoa que o iniciou, com a conta de domínio dela.
- **B.** O agente usa um PAT de escopo de organização com apenas leitura de código, válido por 14 dias, guardado no Azure Key Vault e lido pelo script por variável de ambiente.
- **C.** A equipe colou o PAT no texto do `SKILL.md` "para facilitar o uso", e o arquivo está versionado.
- **D.** O repositório local da equipe tem o remoto configurado como `https://usuario:TOKEN-FICTICIO@dev.azure.com/acme/projeto/_git/repo`.
- **E.** Um PAT de escopo total, sem expiração, é compartilhado por toda a equipe e usado por dois agentes e por três pessoas.

**Passos**

1. Classifique cada relato como aceitável ou inaceitável.
2. Para cada relato inaceitável, cite a regra violada.
3. Escreva a correção do relato C em até quatro linhas.

<details>
<summary>Conferir depois de responder</summary>

O relato B é aceitável: escopo de organização, escopo mínimo, vida curta e armazenamento em cofre. O relato A é inaceitável por usar a identidade pessoal integrada, que dá ao agente tudo o que a pessoa pode fazer, sem limite de escopo, e a correção é um PAT dedicado com escopos mínimos ou uma identidade de aplicação. O relato C viola a regra de não colocar o token em código-fonte nem em arquivos versionados, e a correção é revogar o token, criar outro, guardá-lo no cofre e fazer o script ler uma variável de ambiente, de modo que o `SKILL.md` cite apenas o nome da variável. O relato D viola a proibição de embutir o PAT em URL de remoto do Git, e a correção é usar o Git Credential Manager. O relato E viola três regras, escopo mínimo, vida curta e um token por ferramenta ou fluxo, e a correção é criar tokens separados por agente, com escopo mínimo e expiração.

</details>

### 8. Diagnosticar um sistema multiagente

**Situação**

A ACME criou um agente orquestrador que, a cada pedido de pesquisa sobre uma norma interna, cria 30 subagentes, cada um com a instrução "pesquise sobre a norma". Os resultados voltam repetidos, o tempo de resposta passa de 20 minutos e o gasto de tokens triplicou no mês.

**Passos**

1. Liste três problemas de projeto, citando o modo de falha correspondente do relato da Anthropic.
2. Proponha a correção de cada problema com um valor ou uma regra concreta.

<details>
<summary>Conferir depois de responder</summary>

O primeiro problema é a quantidade de subagentes desproporcional à complexidade, que corresponde à criação de 50 subagentes para uma consulta simples, e a correção é dimensionar o esforço, como 1 agente com 3 a 10 chamadas para uma busca simples e de 2 a 4 subagentes para uma comparação. O segundo é a instrução vaga, que causa trabalho duplicado e lacunas, e a correção é dar a cada subagente um objetivo, um formato de saída, orientação sobre ferramentas e limites da tarefa. O terceiro é a ausência de critério de parada, que se parece com a busca interminável por fontes inexistentes, e a correção é declarar `maxTurns` e o critério de suficiência do resultado. Um quarto ponto a registrar é que a tarefa pode nem exigir vários agentes, porque a pesquisa em fonte única tem pouca paralelização.

</details>

### 9. Três arquivos de subagente com erro

**Situação**

A equipe da ACME, a universidade fictícia desta sessão, escreveu três arquivos de subagente em `.claude/agents/` e nenhum deles se comporta como o esperado. O `claude --debug` está disponível, e a versão instalada é a 2.1.296 ou posterior.

```markdown
---
name: acme:revisor-de-bolsas
description: Revisa as regras do sistema de bolsas.
---
Revise as regras indicadas.
```

```markdown

---
name: revisor-de-pagamentos
description: Revisa as regras do sistema de pagamentos.
tools: Read, Grep, Glob
---
Revise as regras indicadas, sem editar arquivos.
```

```markdown
---
name: revisor-de-chamados
description: Revisa a fila de chamados.
tool: Read, Grep, Glob
color: magenta
---
Revise a fila indicada, sem editar arquivos.
```

**Passos**

1. Para cada arquivo, diga se o subagente carrega e onde o problema aparece: no log de depuração, num aviso ou em nenhum registro.
2. Aponte o arquivo com o efeito mais perigoso para a segurança e explique por quê.
3. Escreva a versão corrigida desse arquivo.

<details>
<summary>Conferir depois de responder</summary>

O primeiro arquivo não carrega, porque o `name` contém `:`, caractere reservado aos identificadores de plugin, e o log de depuração registra o erro. O segundo também não carrega, porque a primeira linha do arquivo está em branco e o Claude Code trata o arquivo como documentação, sem registrar nada no log. O terceiro carrega, e o log traz um aviso de campo desconhecido com a sugestão `tools`, porque `tool` está escrito errado. O valor `magenta` de `color` está fora da lista documentada e foi aceito sem aviso na versão 2.1.309. O efeito mais perigoso é o do terceiro arquivo, porque o subagente carrega sem o campo de restrição e herda todas as ferramentas, de modo que pode editar arquivos apesar de o texto pedir que não edite. A versão corrigida troca `tool` por `tools`, e uma escolha mais segura troca `magenta` por um valor da lista documentada, como `purple`.

</details>

## Avaliar

### 10. Aprovar, revisar ou rejeitar uma skill

**Situação**

A equipe da ACME recebeu esta skill de um colega para instalar no projeto.

```text
---
name: Claude-Helper
description: Eu ajudo você com documentos.
---

(corpo de 900 linhas com explicações do que é um PDF,
uma lista de oito bibliotecas "que você pode usar" e uma
instrução: "para publicar, use o PAT TOKEN-FICTICIO-123")
```

**Passos**

1. Liste os defeitos, citando a regra da documentação de cada um.
2. Decida entre aprovar, revisar ou rejeitar e justifique.
3. Escreva a ordem em que a equipe corrigiria os defeitos.

<details>
<summary>Conferir depois de responder</summary>

Os defeitos são: o `name` tem letra maiúscula e contém a palavra reservada "claude", o que o invalida. A descrição está em primeira pessoa e é vaga, sem dizer quando usar. O corpo excede as 500 linhas recomendadas e explica o que o modelo já conhece. A lista de oito bibliotecas viola a orientação de oferecer um caminho padrão e não várias opções. O token está no texto da skill, o que viola a regra de não guardar segredo em arquivo versionado e exige revogar o token. A decisão é rejeitar a versão atual e reescrevê-la, porque o `name` inválido impede o uso e o segredo exposto exige ação imediata. A ordem de correção é revogar o token, corrigir o `name` e a descrição, reduzir o corpo e mover o detalhe para arquivos de referência, definir um caminho padrão e criar três avaliações antes de reinstalar.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Defeitos encontrados | 40% | Pelo menos cinco dos seis defeitos, cada um com a regra associada |
| Decisão justificada | 30% | Rejeita ou exige revisão com base no `name` inválido e no segredo exposto |
| Ordem de correção | 30% | Revoga o token antes de qualquer outra correção |

### 11. O mesmo agente no Codex CLI

**Situação**

A equipe da ACME tem um subagente somente leitura para o Claude Code e recebeu de um colega uma versão para o Codex CLI.

```markdown
---
name: revisor-somente-leitura
description: Revisa a estrutura de um ADR sem editar arquivos.
tools: Read, Grep, Glob
---
Liste as seções ausentes do ADR indicado.
```

```toml
name = "revisor_somente_leitura"
description = "Revisa a estrutura de um ADR sem editar arquivos."
developer_instructions = """
Liste as seções ausentes do ADR indicado.
Não edite arquivos.
"""
```

**Passos**

1. Diga o que cada arquivo restringe e o que apenas orienta.
2. Avalie se o arquivo do Codex impede a edição, citando a documentação.
3. Decida entre aprovar, revisar ou rejeitar a versão do Codex e proponha a correção.
4. Opcional, para quem tem o Codex instalado e autenticado numa versão que aceite o modelo da conta: coloque o arquivo em `.codex/agents/` e peça ao Codex que o use para corrigir um ADR, registrando se o arquivo mudou.

<details>
<summary>Conferir depois de responder</summary>

No arquivo do Claude Code, o campo `tools` restringe as ferramentas e o corpo orienta. No arquivo do Codex, a instrução orienta, e a documentação adverte que instruções para evitar edições não criam um sandbox somente leitura, de modo que o sandbox e a aprovação são herdados da sessão que inicia o agente. A decisão é revisar: o arquivo é aceitável como orientação, e a restrição real exige iniciar a sessão com `sandbox_mode = "read-only"`, valor que consta da documentação de aprovações e segurança. Esse comportamento do Codex está documentado e, no ambiente desta sessão, não foi executado, porque o modelo padrão da conta exigia uma versão mais nova do Codex. O passo opcional pede a versão do Codex instalada e um modelo aceito pela conta, e o resultado entra no registro da equipe com a versão usada e o status observado.

</details>

## Criar

### 12. Exercício-âncora: uma skill, um subagente e um artefato conferido

**O que é:** cada equipe preenche a ficha de requisitos, constrói uma skill e um subagente que geram um artefato do trabalho da própria equipe, mede o resultado, prevê e verifica a restrição de ferramentas do subagente e submete as permissões e as credenciais à conferência da equipe vizinha. A atividade ocupa 34 minutos de construção e 6 minutos de conferência cruzada. A equipe pode reutilizar a skill `registrando-decisao-arquitetural` da oficina ou escolher outro artefato, desde que tenha estrutura verificável por script.

![Cinco passos de construção em sequência, com 6 minutos para preencher a ficha, 11 minutos para construir a skill, o script e o subagente, 8 minutos para executar os três cenários e verificar a restrição de ferramentas, 5 minutos para comparar a medição com a ficha e decidir, e 4 minutos para preparar o material do vizinho, seguidos de 6 minutos de conferência cruzada entre equipes.](assets/fluxo-do-exercicio-ancora.png)

**Situação**

O material de entrada não contém dado pessoal nem sigiloso, e nenhuma credencial real é usada. Onde o exercício pedir um token, a equipe descreve o plano e usa um valor fictício.

**Passos**

1. Em 6 minutos, a equipe preenche a ficha de requisitos abaixo, antes de qualquer construção.
2. Em 11 minutos, a equipe usa o agente para criar a skill, o script de conferência e o subagente de revisão, com `tools` explícito.
3. Em 8 minutos, a equipe executa a skill em três cenários: uma entrada completa, uma entrada incompleta e uma entrada com um texto que parece segredo. Cada execução registra tokens, tempo, resultado do script e itens a confirmar. Na mesma etapa, a equipe escreve a previsão do que acontece quando se pede ao subagente que edite um arquivo, executa o pedido e anota se o arquivo mudou, e repete o teste com `tool` no lugar de `tools`, localizando no log de depuração a linha que registra o campo desconhecido.
4. Em 5 minutos, a equipe compara a medição com a ficha, decide entre adotar, ajustar o modelo ou o esforço, ou descartar, e registra a decisão.
5. Em 4 minutos, a equipe prepara para o vizinho o arquivo do subagente e o plano da credencial.

| Linha da ficha | Declaração da equipe |
|---|---|
| Mecanismo e razão da escolha | |
| Arquivo e front-matter (campos e valores) | |
| Artefato e formato | |
| Conferência por script (o que o script verifica) | |
| Conferência por pessoa (o que só uma pessoa decide) | |
| Modelo e esforço, com a razão | |
| Orçamento de tokens por execução | |
| Tempo máximo por execução | |
| Ferramentas e permissões do subagente | |
| Identidade e credencial usadas, com escopo e validade | |
| Local de guarda do valor da credencial | |

| Verificação da restrição | Com `tools` | Com `tool` |
|---|---|---|
| Previsão da equipe | | |
| O arquivo mudou? | | |
| Linha do log que explica o resultado | | |

<details>
<summary>Conferir depois de executar a verificação</summary>

O resultado observado na versão 2.1.309 foi que o subagente com `tools: Read, Grep, Glob` respondeu que só tinha ferramentas de leitura e não editou o arquivo, e que o subagente com o campo `tool` editou o arquivo, porque sem `tools` ele herda todas as ferramentas. O log traz um aviso com `did you mean "tools"?` para o campo desconhecido. A decisão de processo esperada é incluir a verificação da restrição, com um pedido de edição, na revisão de todo arquivo de subagente.

</details>

**Conferência cruzada (6 minutos)**

Cada equipe troca o arquivo do subagente e o plano da credencial com a equipe vizinha, aplica a tabela de [perguntas de revisão](seguranca-e-credenciais.md#perguntas-de-revisao) e entrega por escrito ao menos um achado, com a regra correspondente. A equipe dona do material decide o que corrigir.

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Requisitos antes da construção | 20% | Ficha completa, com mecanismo, front-matter, orçamento de tokens e tempo declarados |
| Conferência em duas camadas | 25% | Script que verifica a estrutura e a lista do que só uma pessoa decide |
| Medição | 20% | Três cenários executados, com tokens, tempo e resultado do script registrados |
| Permissões e credencial | 25% | `tools` explícito, previsão e verificação da restrição registradas, identidade própria, escopo mínimo, validade e cofre indicados |
| Decisão | 10% | Adotar, ajustar ou descartar, justificada pela medição |

Para a equipe que terminar antes, a extensão é repetir o cenário com entrada incompleta em um segundo modelo e comparar o comportamento do campo "A confirmar".
