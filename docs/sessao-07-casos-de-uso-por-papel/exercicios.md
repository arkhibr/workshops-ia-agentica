# Exercícios

Tente responder antes de abrir os blocos de feedback. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar), e a sessão inteira treina duas habilidades: reconhecer se uma tarefa descrita é um caso de uso completo e derivar um caso de uso a partir de uma tarefa de trabalho. Os exercícios de Aplicar em diante usam situações da ACME, a universidade fictícia desta sessão, e o exercício-âncora do nível Criar é a atividade de 43 minutos do segundo bloco da sessão.

## Recordar

### 1. Os cinco elementos de um caso

Nomeie os cinco elementos que um caso de uso de IA precisa declarar e indique qual deles corresponde à coluna "Conferência" das páginas por papel.

<details>
<summary>Ver resposta</summary>

Os cinco elementos são entrada, saída, pedido, conferência e decisão humana, e a coluna "Conferência" das páginas por papel corresponde ao quarto, que é a fonte contra a qual o resultado é comparado antes de circular.

</details>

### 2. Os quatro critérios de escolha

Escreva os quatro critérios que a turma aplica para decidir se uma tarefa entra na rotina da equipe e a pergunta que cada um faz.

<details>
<summary>Ver resposta</summary>

Os critérios são conferência (existe uma fonte conhecida contra a qual comparar o resultado), custo do erro (quanto custa desfazer se o erro passar), frequência (a tarefa se repete na rotina, o que compensa escrever o pedido-base) e dados (o material de entrada contém dado pessoal ou sigiloso).

</details>

## Compreender

### 3. Hábito e caso de uso

Um colega afirma que já tem um caso de uso de IA, porque toda semana cola no agente a lista de defeitos abertos e escreve "organize isso". Explique, elemento por elemento, o que falta a esse hábito para ser um caso de uso completo.

<details>
<summary>Ver resposta</summary>

A entrada não declara se a lista pode ser compartilhada com o agente, e a saída não tem formato nem destinatário, de modo que cada semana o resultado vem diferente. O pedido não traz papel, tarefa nem restrição, e "organize" não diz por qual critério. Não existe conferência, porque nenhuma fonte é nomeada para comparar a lista organizada com a original, e não há decisão humana declarada sobre o que o resultado vira. O hábito vira caso quando os cinco elementos estão escritos e a equipe consegue repeti-lo com o mesmo resultado esperado.

</details>

### 4. O que fica fora do catálogo

Descreva as duas classes de tarefa que ficam fora do catálogo, qualquer que seja o papel, e dê um exemplo de cada uma tirado do trabalho de uma equipe de desenvolvimento de software.

<details>
<summary>Ver resposta</summary>

A primeira classe reúne as tarefas cujo resultado ninguém na equipe consegue conferir, como pedir ao agente uma estimativa de esforço para uma tecnologia que ninguém da equipe conhece, sem fonte de comparação. A segunda reúne as decisões que cabem a uma pessoa nomeada, como a severidade final de um defeito ou a aprovação de um pagamento, em que o agente pode propor e a pessoa decide.

</details>

## Aplicar

### 5. Reconhecer casos completos e incompletos

**Situação**

A coordenação da ACME, a universidade fictícia usada nesta sessão, reuniu cinco descrições de uso de IA que equipes relataram. Cada descrição pode ser um caso completo, um caso incompleto ou uma tarefa que fica fora do catálogo.

- **A.** Marina, product owner, cola no agente os chamados de suporte do mês, sem o nome de quem os abriu, e pede: "Agrupe por tema e cite o número de cada chamado". Ela sorteia oito chamados, confere se o tema atribuído confere com o texto original e só então envia a tabela ao time, que decide o que priorizar.
- **B.** Rafael, desenvolvedor, pede ao agente que "melhore os testes" de uma classe e faz o commit do que voltar.
- **C.** O time pede ao agente a data de entrega do próximo release e apresenta a data que ele escreveu à diretoria.
- **D.** Helena, analista de negócio, pede ao agente que defina a prioridade de dez itens do backlog e publica a ordem que ele devolver.
- **E.** Lucas, testador, cola no agente a planilha de notas dos alunos, com nome e matrícula, para gerar um resumo por turma, e confere o resumo contra a planilha.

**Passos**

1. Para cada descrição, escreva se ela é um caso completo, um caso incompleto ou uma tarefa fora do catálogo.
2. Quando for incompleto, indique qual dos cinco elementos falta ou está fraco.
3. Escolha uma das descrições incompletas e escreva a correção em duas linhas.

<details>
<summary>Conferir depois de responder</summary>

A descrição A é um caso completo: a entrada foi anonimizada, a saída é uma tabela com o número de cada chamado, o pedido traz uma restrição, a conferência compara uma amostra de oito chamados com o texto original e a decisão sobre prioridades fica com o time. A descrição B é incompleta, porque o pedido não diz o que significa melhorar, nenhuma fonte confere o resultado e o commit retira a decisão humana. A descrição C é incompleta na conferência, porque uma data de entrega é um número que precisa sair de simulação ou de planilha, e o agente escreve a faixa de datas sem tê-la calculado. A descrição D é uma tarefa fora do catálogo, porque a prioridade de um item cabe a uma pessoa nomeada, e o agente pode apenas propor. A descrição E é incompleta na entrada, porque a planilha contém nome e matrícula, e a conferência declarada não corrige o dado pessoal já compartilhado.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Classificação das cinco descrições | 50% | Pelo menos quatro das cinco classificações coincidem com o feedback |
| Elemento faltante nomeado | 30% | Cada descrição incompleta aponta o elemento específico, e não apenas "falta cuidado" |
| Correção proposta | 20% | A correção altera o elemento apontado e deixa a conferência com fonte nomeada |

### 6. Derivar um caso a partir de uma tarefa

**Situação**

Na ACME, a Scrum Master do time do portal de prestação de contas prepara toda segunda-feira o material da retrospectiva da sprint anterior. Ela lê quarenta cartões digitalizados do quadro da retrospectiva, agrupa-os por tema e escreve três propostas de melhoria para o time votar. A tarefa leva cerca de uma hora e se repete a cada duas semanas.

**Passos**

1. Declare a entrada, indicando se ela pode ser compartilhada com o agente e o que precisa mudar antes disso.
2. Declare a saída, com formato e destinatário.
3. Escreva o pedido, com papel, tarefa, formato e pelo menos uma restrição que impeça o agente de inventar tema.
4. Nomeie a fonte de comparação da conferência e diga se a conferência é integral ou por amostra, com a razão.
5. Declare qual parte da decisão fica com uma pessoa nomeada.
6. Repita os passos de 1 a 5 para uma tarefa do seu próprio papel, que você já faça na rotina.

<details>
<summary>Conferir depois de responder</summary>

Uma derivação possível: a entrada são os quarenta cartões, sem o nome de quem escreveu cada um, e anonimizar é a mudança necessária antes de compartilhar. A saída é uma tabela de temas com contagem e uma lista de três propostas de melhoria, destinada ao time. O pedido diz "Você é um facilitador de retrospectivas. Agrupe os cartões por tema, cite o texto de pelo menos dois cartões por tema e escreva *sem cartão correspondente* quando uma proposta não tiver origem nos cartões". A conferência compara a contagem de cada tema com os cartões originais, por amostra, porque um tema mal contado se corrige na própria reunião. A decisão sobre quais propostas entram na sprint fica com o time, e a pessoa que facilita a retrospectiva responde por registrá-la.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Cinco elementos declarados | 40% | Os cinco elementos aparecem escritos, sem ficar subentendidos |
| Pedido com restrição | 25% | A restrição é uma instrução verificável que impede o agente de preencher lacunas |
| Conferência com fonte e extensão | 25% | A fonte é nomeada e a escolha entre amostra e conferência integral tem razão ligada ao custo do erro |
| Tarefa do próprio papel | 10% | A tarefa do passo 6 é real, repetida na rotina e aceita os cinco elementos |

## Analisar

### 7. Qual tarefa entra primeiro

**Situação**

Uma analista de negócio da ACME tem três tarefas candidatas a caso de uso e tempo para estruturar uma delas nesta semana.

- **Tarefa 1.** Reescrever o glossário do módulo de bolsas com os termos padronizados, a partir do glossário atual de sessenta termos, que o especialista de domínio já usa. A tarefa será feita uma vez.
- **Tarefa 2.** Resumir toda semana as trinta mensagens do canal do projeto, que trazem nomes e e-mails de alunos e de professores. A tarefa se repete toda semana.
- **Tarefa 3.** Escrever o rascunho do relatório semanal de status a partir do quadro do time, cujos itens e datas ela conhece de cor. A tarefa se repete toda semana e o relatório é lido pela coordenação.

**Passos**

1. Monte uma tabela com as três tarefas nas linhas e os quatro critérios nas colunas, com uma avaliação curta em cada célula.
2. Indique qual tarefa entra primeiro e justifique em três linhas.
3. Indique o que a tarefa que ficou por último precisaria mudar para entrar depois.

<details>
<summary>Ver análise sugerida</summary>

A tarefa 3 entra primeiro: a fonte de comparação existe e é o próprio quadro, o erro é detectável antes de circular, a frequência é semanal e o material não traz dado pessoal. A tarefa 1 tem fonte e dados adequados, mas a frequência é de uma única execução, e o esforço de escrever o pedido-base dificilmente se paga. A tarefa 2 tem frequência alta e fonte conferível, e fica por último por causa dos dados, porque nomes e e-mails de terceiros não devem ser colados no agente. Ela entra depois que a entrada for anonimizada, com os nomes e e-mails substituídos por descrições genéricas antes do envio.

</details>

### 8. Famílias de casos no catálogo

Abra a página do seu papel nesta sessão e leia os dez primeiros casos do catálogo. Agrupe-os em famílias segundo o tipo de transformação que fazem sobre a entrada, como resumir, estruturar, gerar a partir de regra ou comparar. Para cada família, escreva a fonte de comparação mais comum entre os casos dela, e indique qual família tem a conferência mais fraca e por quê.

A resposta depende do papel escolhido, e por isso não há gabarito. O que se espera é que cada caso apareça numa família só, que a fonte de comparação citada conste do catálogo, e que a família indicada como mais fraca tenha uma razão ligada ao custo do erro ou à ausência de fonte.

## Avaliar

### 9. Adotar, ajustar ou descartar

**Situação**

Três colegas da ACME propuseram casos de uso e pedem à turma uma recomendação para cada um.

- **Caso X, Desenvolvimento.** Entrada: o diff de um pull request. Saída: comentários de revisão. Pedido: "Revise este código". Conferência: o autor do pull request lê os comentários. Decisão: o autor.
- **Caso Y, Testes.** Entrada: um requisito escrito e as regras de negócio dele em RuleSpeak. Saída: uma tabela de casos de teste. Pedido: papel de testador, formato de tabela e a restrição "marque como lacuna o que o requisito não diz". Conferência: o testador compara cada caso de teste com o requisito, e o especialista de domínio valida as lacunas. Decisão: o testador escolhe quais casos entram na suíte.
- **Caso Z, Product Owner.** Entrada: as respostas de uma pesquisa de clima, com o nome de quem respondeu. Saída: um ranking de prioridades do backlog. Pedido: "Ordene o que o time mais quer". Conferência: nenhuma. Decisão: o agente define a prioridade dos itens.

**Passos**

1. Recomende adotar, ajustar ou descartar cada caso.
2. Justifique cada recomendação em duas linhas, citando o elemento ou o critério que a sustenta.
3. Para os casos que você mandou ajustar, escreva a mudança mínima que o tornaria adotável.

<details>
<summary>Ver análise sugerida</summary>

O caso Y deve ser adotado: os cinco elementos estão declarados, o pedido traz uma restrição que impede o agente de preencher lacunas, a conferência tem fonte nomeada e a decisão fica com uma pessoa. O caso X deve ser ajustado, porque a conferência de o autor ler os comentários não compara o resultado com fonte nenhuma, e o pedido "Revise este código" não declara critério. A mudança mínima é nomear a fonte, como o padrão de código da equipe, e pedir que cada comentário cite a linha do diff. O caso Z deve ser descartado como está, porque a entrada tem dado pessoal e a prioridade cabe a uma pessoa nomeada, e o agente pode apenas propor. Uma versão adotável anonimiza as respostas, pede os temas com contagem e deixa a prioridade com o product owner.

</details>

## Criar

### 10. Derivar dois casos da sua semana

**Situação**

Cada participante parte do próprio trabalho, sem material real, e produz dois casos de uso que a equipe poderia estruturar na semana seguinte.

**Passos**

1. Liste cinco tarefas que você fez na última semana e que envolveram ler, escrever ou organizar texto, dados ou código.
2. Aplique os quatro critérios às cinco tarefas e elimine as que falham em conferência ou em dados.
3. Das que restaram, escolha duas e escreva, para cada uma, os cinco elementos num quadro de duas colunas, elemento e declaração.
4. Para cada caso, escreva em uma linha o erro mais provável do agente e a parte da conferência que o encontraria.

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Eliminação justificada | 25% | Cada tarefa descartada tem um critério nomeado como razão |
| Cinco elementos completos | 40% | Os dois quadros trazem os cinco elementos, com a fonte da conferência nomeada |
| Erro provável e conferência | 25% | O erro citado é plausível para o tipo de tarefa e a conferência o encontraria |
| Uso na rotina | 10% | Os dois casos são tarefas que se repetem e podem ser executados na semana seguinte |

### 11. Exercício-âncora: um caso real e o pitch

**O que é:** a equipe aplica um caso de uso a uma tarefa real, confere o resultado e apresenta o pitch de oitenta segundos descrito na página [Pitch de um caso de uso](pitch-de-caso-de-uso.md). A atividade ocupa 23 minutos de preparação e 20 minutos de apresentações.

**Situação**

Cada equipe escolhe uma tarefa que realizaria na semana seguinte, com material sem dado pessoal nem sigiloso, e um caso do catálogo, ou do Experimento C da oficina, que se aplique a ela.

**Passos**

1. Em cinco minutos, a equipe escolhe a tarefa e o caso e declara a fonte de comparação para a conferência.
2. Em dez minutos, uma pessoa da equipe escreve o pedido com papel, tarefa, formato e restrições, e executa o caso no agente.
3. Em cinco minutos, a equipe confere o resultado contra a fonte declarada e registra cada divergência.
4. Em três minutos, a equipe prepara as cinco partes do pitch e decide se adota, ajusta ou descarta o caso.

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Conferência executada e registrada | 40% | O pitch diz contra que fonte o resultado foi comparado e o que a comparação encontrou |
| Pedido com restrições | 25% | O pedido declara pelo menos uma restrição que impede o agente de preencher lacunas |
| Decisão com próximo passo | 20% | A equipe diz se adota, ajusta ou descarta o caso e declara um prazo |
| Respeito ao tempo | 15% | O pitch cabe nos oitenta segundos |

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
