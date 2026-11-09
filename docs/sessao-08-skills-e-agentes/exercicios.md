# Exercícios — skills, agentes e escolha do mecanismo

Faça o exercício 1 e, em seguida, use o exercício 5 para criar o subagente de leitura, pedir uma edição e observar se a restrição funciona. Os exercícios 2 a 4 e 6 a 8 são opcionais e ficam para depois da sessão.

!!! note "Ambiente"
    Os exemplos usam **Claude Code** em um projeto de teste, sem dados sensíveis nem credenciais reais. Execute os comandos de terminal na raiz do projeto: use PowerShell no Windows ou as alternativas para Linux/macOS e os comandos `/...` dentro do Claude Code. Os campos e comandos desta página são específicos do Claude Code, e a sessão precisa ser reiniciada após cada alteração de arquivo de configuração.

## 1. Criar e invocar uma skill

Uma skill é um procedimento reutilizável, e o arquivo `SKILL.md` define o nome dela, a situação em que ela é útil e o que ela deve fazer. Os comandos abaixo criam a skill e uma transcrição fictícia para testá-la, e o marcador `$ARGUMENTS` recebe o texto informado após o nome da skill.

**Windows — PowerShell**

Crie a skill em `.claude/skills/resumir-notas/SKILL.md`:

```powershell
New-Item -ItemType Directory -Force .claude/skills/resumir-notas | Out-Null
$skill = @'
---
name: resumir-notas
description: Identifica tarefas e riscos de projeto em transcrições de reunião. Use ao analisar uma reunião.
argument-hint: [arquivo]
---
Leia a transcrição em $ARGUMENTS. Liste tarefas e riscos de projeto, com
responsável, prazo e trecho de evidência quando houver. Não invente dados:
marque o que estiver ausente como "A confirmar" e identifique riscos inferidos.
'@
[IO.File]::WriteAllText((Join-Path (Get-Location) '.claude/skills/resumir-notas/SKILL.md'), $skill, [Text.UTF8Encoding]::new($false))
```

Crie a transcrição de teste em `notas-exemplo.md`:

```powershell
$notas = @'
# Transcrição — projeto de bolsas
Reunião de 22 de outubro de 2026

Ana: As inscrições começam em 16 de novembro. Até lá, precisamos integrar
    o sistema de bolsas ao de pagamentos e concluir a homologação.
Bruno: A fila gerenciada continua sendo a opção escolhida? O arquivo em lote
    seria mais simples, mas só atualizaria os pagamentos no dia seguinte.
Ana: Sim, seguimos com a fila. O lote fica como alternativa de contingência,
    ainda sem aprovação para uso em produção.
Bruno: Vou enviar a especificação da integração até 30 de outubro. Dependo
    dos campos obrigatórios da API; Carla, você consegue confirmá-los?
Carla: Consigo pedir ao fornecedor até 27 de outubro. A documentação atual
    está incompleta e o fornecedor ainda não confirmou a data da nova API.
    Se ela atrasar, talvez a homologação não termine antes das inscrições.
Ana: Precisamos também verificar se o ambiente de homologação tem acesso à
    fila. Podemos pedir isso para a equipe de infraestrutura?
Bruno: Podemos, mas ainda não falamos com eles nem combinamos um responsável.
    A verificação precisa acontecer antes do início dos testes de integração.
Carla: Os testes estão previstos para 5 de novembro, se a API estiver pronta.
    Também precisamos preparar um plano de contingência caso não esteja.
Ana: Concordo. Ainda não temos responsável nem prazo para esse plano. Não
    assumam que o arquivo em lote já está aprovado: preciso discutir a opção
    com pagamentos antes de tomar essa decisão.
Carla: Eu registro a dependência da API no quadro de riscos. Não lembro se o
    contrato cobre indisponibilidade; vou confirmar, mas ainda não tenho data.
'@
[IO.File]::WriteAllText((Join-Path (Get-Location) 'notas-exemplo.md'), $notas, [Text.UTF8Encoding]::new($false))
```

<details>
<summary>Linux / macOS — Bash ou Zsh</summary>

Crie a skill:

```bash
mkdir -p .claude/skills/resumir-notas
cat > .claude/skills/resumir-notas/SKILL.md <<'EOF_SKILL'
---
name: resumir-notas
description: Identifica tarefas e riscos de projeto em transcrições de reunião. Use ao analisar uma reunião.
argument-hint: [arquivo]
---
Leia a transcrição em $ARGUMENTS. Liste tarefas e riscos de projeto, com
responsável, prazo e trecho de evidência quando houver. Não invente dados:
marque o que estiver ausente como "A confirmar" e identifique riscos inferidos.
EOF_SKILL
```

Crie a transcrição de teste:

```bash
cat > notas-exemplo.md <<'EOF_NOTAS'
# Transcrição — projeto de bolsas
Reunião de 22 de outubro de 2026

Ana: As inscrições começam em 16 de novembro. Até lá, precisamos integrar
    o sistema de bolsas ao de pagamentos e concluir a homologação.
Bruno: A fila gerenciada continua sendo a opção escolhida? O arquivo em lote
    seria mais simples, mas só atualizaria os pagamentos no dia seguinte.
Ana: Sim, seguimos com a fila. O lote fica como alternativa de contingência,
    ainda sem aprovação para uso em produção.
Bruno: Vou enviar a especificação da integração até 30 de outubro. Dependo
    dos campos obrigatórios da API; Carla, você consegue confirmá-los?
Carla: Consigo pedir ao fornecedor até 27 de outubro. A documentação atual
    está incompleta e o fornecedor ainda não confirmou a data da nova API.
    Se ela atrasar, talvez a homologação não termine antes das inscrições.
Ana: Precisamos também verificar se o ambiente de homologação tem acesso à
    fila. Podemos pedir isso para a equipe de infraestrutura?
Bruno: Podemos, mas ainda não falamos com eles nem combinamos um responsável.
    A verificação precisa acontecer antes do início dos testes de integração.
Carla: Os testes estão previstos para 5 de novembro, se a API estiver pronta.
    Também precisamos preparar um plano de contingência caso não esteja.
Ana: Concordo. Ainda não temos responsável nem prazo para esse plano. Não
    assumam que o arquivo em lote já está aprovado: preciso discutir a opção
    com pagamentos antes de tomar essa decisão.
Carla: Eu registro a dependência da API no quadro de riscos. Não lembro se o
    contrato cobre indisponibilidade; vou confirmar, mas ainda não tenho data.
EOF_NOTAS
```


</details>

Inicie o Claude Code na raiz do projeto e invoque a skill, passando o arquivo como argumento:

```text
/resumir-notas notas-exemplo.md
```

Compare a saída com a transcrição: Bruno ficou responsável pela especificação e Carla por consultar o fornecedor e confirmar a cobertura contratual. A verificação do ambiente e o plano de contingência ainda não têm responsáveis, o atraso da API pode afetar os testes e a homologação, e a opção de lote continua sem aprovação. Confira as evidências, os prazos ausentes e os riscos inferidos. Depois, retire o prazo da especificação e execute novamente: a skill deve marcá-lo como `A confirmar`, sem inventar uma data.

## 2. Controlar o acionamento

Por padrão, você pode chamar uma skill pelo nome e o modelo também pode escolhê-la pela descrição. Este experimento restringe a invocação ao usuário e compara os dois caminhos. A evidência de que a skill foi usada é a indicação de invocação na interface, porque um resumo na resposta pode ter sido produzido sem a skill.

No front-matter da skill anterior, acrescente:

```yaml
disable-model-invocation: true
```

Reinicie a sessão e compare:

```text
Resuma notas-exemplo.md usando a skill apropriada.
/resumir-notas notas-exemplo.md
```

Remova o campo, reinicie a sessão, repita o pedido em linguagem natural e registre em quais casos a skill foi acionada. Compare também o efeito de `user-invocable: false` sobre o menu `/` e sobre o acionamento pelo modelo.

<details>
<summary>Confira</summary>

Com `disable-model-invocation: true`, a chamada pelo nome continua disponível, mas o modelo não a invoca automaticamente. Com `user-invocable: false`, a skill sai do menu do usuário e pode ser acionada pelo modelo.

</details>

## 3. Comparar contexto normal e fork

Uma skill comum usa o contexto da conversa, e com `context: fork` ela executa em um subagente com contexto separado. O teste verifica, nos dois casos, se uma preferência informada na conversa chega à skill.

Acrescente ao corpo da skill: `Use a preferência de formato informada na conversa; se não houver, use tópicos.` Abra uma nova sessão e envie esta mensagem:

```text
Nesta conversa, apresente os resumos em uma tabela com as colunas Item e Detalhe.
```

Em seguida, envie outra mensagem para executar a skill:

```text
/resumir-notas notas-exemplo.md
```

Anote o formato da resposta, acrescente `context: fork` ao front-matter, reinicie a sessão e repita as duas mensagens. Compare os dois formatos para verificar se o subagente recebeu a preferência informada na conversa.

Para testar a passagem explícita, ajuste a instrução da skill para tratar o primeiro argumento como arquivo e os demais como preferência de formato. Na sessão com `fork`, execute:

```text
/resumir-notas notas-exemplo.md Use uma tabela com as colunas Item e Detalhe.
```

Compare o resultado com a execução anterior e registre o formato observado ao lado do esperado, porque o formato pode variar entre execuções.

<details>
<summary>Confira</summary>

O fork não recebe o histórico da conversa, e os dados necessários precisam acompanhar a tarefa nos argumentos. O campo `agent` escolhe o tipo do subagente usado pelo fork.

</details>

## 4. Ajustar modelo e esforço

O campo `model` escolhe o modelo da execução, e o campo `effort` ajusta o esforço de raciocínio quando o modelo oferece esse ajuste. A comparação ajuda a decidir quanto gastar para obter um resultado suficiente. Cada linha muda os dois campos, portanto mostra o efeito da configuração completa, sem separar o efeito de cada campo.

Na skill, teste estas configurações com o mesmo arquivo e a mesma instrução:

| Execução | `model` | `effort` |
|---|---|---|
| A | `haiku` | `low` |
| B | `sonnet` | `medium` |

Reinicie a sessão após cada alteração, execute `/resumir-notas notas-exemplo.md`, consulte o consumo da sessão com `/cost` e registre as diferenças entre as execuções. Se algum modelo ou nível não estiver disponível, registre a indisponibilidade e escolha outro modelo ou nível disponível.

| Execução | Itens corretos / 3 | Tempo | Tokens ou custo observado | Inventou algo? |
|---|---:|---:|---:|---|
| A | | | | |
| B | | | | |

Identifique a configuração que atende à tarefa com menor custo e repita a comparação com notas ambíguas antes de decidir. Anote também que o consumo da sessão pode incluir chamadas que não pertencem à skill.

## 5. Restringir um subagente

Um subagente executa uma tarefa em contexto próprio, e no arquivo abaixo `tools` fornece ferramentas de leitura, `model` escolhe o modelo e `maxTurns` limita os turnos. Os comandos criam o agente e guardam uma cópia das notas para verificar se houve alteração.

**Windows — PowerShell**

```powershell
New-Item -ItemType Directory -Force .claude/agents | Out-Null
$agente = @'
---
name: revisor-notas
description: Revisa notas de reunião e aponta informações ausentes.
tools: Read, Grep, Glob
model: haiku
maxTurns: 8
---
Revise as notas indicadas. Verifique tarefas, riscos, responsáveis e prazos; liste informações ausentes sem editar arquivos.
'@
[IO.File]::WriteAllText((Join-Path (Get-Location) '.claude/agents/revisor-notas.md'), $agente, [Text.UTF8Encoding]::new($false))
Copy-Item notas-exemplo.md notas-antes.md
```

<details>
<summary>Linux / macOS — Bash ou Zsh</summary>

```bash
mkdir -p .claude/agents
cat > .claude/agents/revisor-notas.md <<'EOF_AGENT'
---
name: revisor-notas
description: Revisa notas de reunião e aponta informações ausentes.
tools: Read, Grep, Glob
model: haiku
maxTurns: 8
---
Revise as notas indicadas. Verifique tarefas, riscos, responsáveis e prazos; liste informações ausentes sem editar arquivos.
EOF_AGENT
cp notas-exemplo.md notas-antes.md
```


</details>

Reinicie o Claude Code e peça:

```text
Use o subagente revisor-notas para revisar notas-exemplo.md.
Use o subagente revisor-notas para editar notas-exemplo.md e acrescentar uma seção de próximos passos.
```

Compare o arquivo com a cópia criada antes do teste. A ausência de saída indica arquivos iguais, e as linhas exibidas indicam as diferenças:

```powershell
# Windows — PowerShell
Compare-Object (Get-Content notas-antes.md) (Get-Content notas-exemplo.md)
```

```bash
# Linux / macOS
diff -u notas-antes.md notas-exemplo.md
```

Em um **projeto descartável**, troque `tools` por `tool`, reinicie e repita o pedido de edição. Autorize a edição se o Claude Code solicitar permissão, porque sem essa autorização a recusa viria do modo de permissão da sessão e o teste deixaria de medir a configuração do subagente. Compare o arquivo e o log de `claude --debug`, e restaure `tools` depois do teste.

<details>
<summary>Confira</summary>

O campo `tools` restringe as ferramentas, e `tool` é um campo desconhecido que o Claude Code ignora, de modo que o subagente herda todas as ferramentas e consegue escrever. O comportamento e os avisos podem variar por versão, e o registro deve conter a versão e o resultado observado.

</details>

## 6. Limites e delegação

O campo `maxTurns` limita os turnos disponíveis ao subagente e deixa a duração e o custo de cada execução sem valor fixo. Um limite baixo pode interromper a revisão antes de ela terminar, e a segunda parte do exercício compara a execução direta com a delegada para avaliar se a separação de contexto ajudou.

Com o mesmo subagente e o mesmo arquivo, compare `maxTurns: 2` com `maxTurns: 8`, pedindo uma revisão que encontre informações ausentes e inconsistências. Registre a conclusão, os problemas encontrados e o tempo de cada execução, e verifique se o limite menor permitiu terminar a tarefa.

Em seguida, compare os pedidos:

```text
Revise notas-exemplo.md diretamente e liste os problemas.
Use o subagente revisor-notas para revisar notas-exemplo.md e listar os problemas.
```

Compare a qualidade, o tempo e o consumo registrado nas duas execuções e identifique em que situação a saída intermediária ou a independência da tarefa justificaria delegar.

## 7. Ajustar a descrição e a delegação

A `description` ajuda o Claude Code a identificar quando um subagente é adequado. Uma descrição específica informa a tarefa e o contexto de uso, e este teste compara a influência dela com a de uma descrição genérica.

No arquivo `.claude/agents/revisor-notas.md`, compare estas descrições:

```yaml
description: Revisa arquivos.
```

```yaml
description: Revisa notas de reunião e aponta informações ausentes e inconsistências, sem editar arquivos.
```

Reinicie a sessão após cada mudança e faça o mesmo pedido, sem nomear o subagente:

```text
Revise notas-exemplo.md e aponte informações ausentes e inconsistências.
```

Registre se houve delegação e compare o resultado. Repita o pedido com a instrução explícita `Use o subagente revisor-notas` e compare a delegação nomeada com a delegação decidida pelo modelo a partir da descrição.

## 8. Exercício complementar: construir, medir e comparar

Após a sessão, em equipe, use uma transcrição de reunião ou escolha outro artefato em Markdown de uso geral. A skill produz o artefato, o script verifica a estrutura dele, o subagente aponta problemas de conteúdo e uma pessoa avalia se as decisões e as pendências fazem sentido. As entradas não podem conter dados sensíveis, e as credenciais usadas no exercício devem ser fictícias.

| Execute | Entregue |
|---|---|
| Preencha a ficha abaixo. | Requisitos antes da construção. |
| Crie uma skill, um script que verifica a estrutura e um subagente de leitura com `tools` explícito. | Arquivos executáveis. |
| Execute os três cenários e teste o pedido de edição com `tools` e, em projeto descartável, com `tool`. | Medições e diferença no arquivo. |
| Compare os resultados com os limites e decida entre adotar, ajustar ou descartar. | Decisão com evidências. |
| Prepare o subagente e o plano de credenciais para outra equipe. | Material para revisão. |
| Troque os materiais e aplique as [perguntas de revisão](seguranca-e-credenciais.md#perguntas-de-revisao). | Ao menos um achado e sua regra. |

**Ficha antes da execução**

| Decisão | Valor |
|---|---|
| Mecanismo e motivo | |
| Arquivos e campos de configuração | |
| Artefato e formato | |
| Verificação por script / por pessoa | |
| Modelo e esforço | |
| Limite de tokens / tempo por execução | |
| Ferramentas e permissões | |
| Identidade, escopo, validade e cofre da credencial | |

**Medição**

Execute cada cenário com a mesma configuração e registre os resultados. No cenário de segredo, use um valor claramente fictício e observe se ele aparece no artefato.

| Cenário | Tokens / custo | Tempo | Script passou? | Itens a confirmar |
|---|---|---|---|---|
| Entrada completa | | | | |
| Entrada incompleta | | | | |
| Texto que parece segredo fictício | | | | |

| Pedido de edição | Previsão | Arquivo mudou? | Evidência no log |
|---|---|---|---|
| Com `tools` | | | |
| Com `tool` | | | |

Compare os resultados com a ficha e registre a decisão. Se houver tempo, repita a entrada incompleta com outro `model` ou `effort` e compare qualidade, tempo e custo.
