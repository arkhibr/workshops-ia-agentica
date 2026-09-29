# Arqueologia de regras: recuperar decisões de negócio do código

Sistemas em produção há muitos anos costumam conter decisões de negócio que nenhum documento atual registra, e a única descrição completa dessas decisões é o próprio código que as executa. A arqueologia de regras é a recuperação disciplinada dessas decisões, com o produto expresso em [SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*, especificação da OMG para vocabulário e regras de negócio com semântica controlada). Esta página apresenta a base conceitual da atividade, o método de seis movimentos usado na sessão e os limites de um agente de IA nessa tarefa.

## Engenharia reversa e arqueologia de software

[Chikofsky e Cross](../referencia/bibliografia.md#chikofsky-e-cross-reverse-engineering-and-design-recovery-1990) publicaram em 1990, na *IEEE Software*, uma taxonomia dos termos usados na manutenção e na compreensão de sistemas existentes. Eles definem **engenharia reversa** como o processo de analisar um sistema para identificar seus componentes e as relações entre eles e para criar representações desse sistema em outra forma ou num nível mais alto de abstração. A definição tem uma consequência prática que orienta toda esta sessão: a engenharia reversa é um processo de exame, e nada nela altera o sistema analisado.

A taxonomia distingue seis termos, engenharia direta, engenharia reversa, redocumentação, recuperação de projeto, reestruturação e reengenharia, e a tabela abaixo reúne os quatro que delimitam a recuperação de regras.

| Termo | Definição na taxonomia | Relação com a arqueologia de regras |
|---|---|---|
| Redocumentação | Subárea da engenharia reversa que recupera documentação perdida ou inexistente | Produz descrições do que o código faz, no mesmo nível de abstração |
| Recuperação de projeto (*design recovery*) | Subárea da engenharia reversa em que conhecimento de domínio, informação externa e dedução são acrescentados às observações do sistema para identificar abstrações de nível mais alto | Depende de conhecimento de domínio além do código, e por isso inclui a pergunta sobre o motivo de cada decisão |
| Reestruturação | Mudança da estrutura interna sem alteração do comportamento externo | Fica fora do escopo, porque altera o sistema |
| Reengenharia | Exame e alteração do sistema para reconstituí-lo numa forma nova | Consome o catálogo de regras recuperado, numa etapa posterior |

A arqueologia de regras é uma recuperação de projeto restrita às decisões de negócio. O porquê de cada decisão pertence ao domínio, e por isso a atividade termina numa conversa com o especialista, depois da leitura do código.

[Hunt e Thomas](../referencia/bibliografia.md#hunt-e-thomas-software-archaeology-2002) desenvolveram a analogia da arqueologia de software numa coluna da *IEEE Software* de março e abril de 2002, intitulada "Software Archaeology". A coluna abre com a queixa de um programador anônimo que, diante de código antigo e intrincado, reclamou que o trabalho dele era arqueologia. Os autores descrevem a arqueologia propriamente dita como a investigação de uma situação em que se procura entender o que se está vendo e como as partes se encaixam, e aplicam essa descrição à leitura de código herdado de outras pessoas. A analogia já circulava antes da coluna, e os próprios autores registram que eles, Brian Marick e Ward Cunningham conduziram um workshop sobre *Software Archaeology* na OOPSLA 2001, conferência anual da ACM sobre programação orientada a objetos.

## Regra de negócio e lógica técnica

[Sneed e Erdős](../referencia/bibliografia.md#sneed-e-erdos-extracting-business-rules-from-source-code-1996) trataram em 1996, no 4º Workshop on Program Comprehension, da extração de regras de negócio a partir de código-fonte. O trabalho revisa o estado da arte da aquisição de conhecimento de aplicação a partir de sistemas existentes, define o papel das regras de negócio nesse conhecimento e propõe um método que parte da identificação das saídas de dados e reduz o programa às instruções que contribuem para cada saída. O método foi implementado na ferramenta de engenharia reversa SOFT-REDOC, para programas COBOL, com o objetivo declarado de ajudar o analista de negócio a compreender programas legados.

A ideia de partir das saídas continua útil porque separa dois tipos de instrução que convivem no mesmo arquivo. A **regra de negócio** responde a uma pergunta do domínio, como quem é elegível, quanto se cobra ou em que ordem as exceções se aplicam, e continuaria valendo se a operação fosse feita à mão. A **lógica técnica** responde a uma necessidade da implementação, como paginação, nova tentativa após falha, conversão de formato, registro em log ou uso de índice.

| Pergunta de triagem | Indica regra de negócio | Indica lógica técnica |
|---|---|---|
| Um especialista do domínio saberia dizer se o trecho está certo? | Sim | Não |
| Mudar o trecho altera o resultado que o negócio recebe? | Sim | Somente o desempenho ou a forma |
| O trecho continuaria necessário numa operação manual? | Sim | Não |

Os casos difíceis são trechos com forma de lógica técnica que alteram o resultado entregue ao negócio. Uma conversão de valor ausente em zero tem a forma de tratamento de tipo e decide o resultado de quem não informou o dado, e um filtro de desempenho que exclui registros antigos pode retirar clientes de uma classificação. A regra de triagem da sessão manda classificar como regra candidata todo trecho que responde "sim" à segunda pergunta, qualquer que seja a aparência dele.

## Tipos de evidência e o peso de cada um

A recuperação de uma regra combina fontes de natureza diferente. Algumas descrevem o comportamento implementado, outras descrevem a intenção de alguém em algum momento, e o peso de cada fonte depende de qual das duas coisas ela sustenta. Hunt e Thomas advertem, na mesma coluna, que é perigoso supor que o código ou os comentários sejam inteiramente verdadeiros, e dão como exemplo uma rotina chamada `readSystem` que pode estar gravando dados em disco.

| Evidência | O que sustenta | Força | Risco típico |
|---|---|---|---|
| Código executável | Comportamento implementado | Alta para o que o sistema faz | Nada informa sobre a intenção do autor |
| Dados de produção | Quais ramos ocorrem e com que frequência | Alta para uso real | Um ramo sem ocorrência pode continuar vigente |
| Configuração e parâmetros | Valor vigente de limites e chaves | Alta para o valor atual | O literal do código pode diferir do valor configurado |
| Comentário no código | Intenção de quem escreveu, na data em que escreveu | Baixa | Desatualização em relação ao código, sem aviso ao leitor |
| Testes existentes | Expectativa registrada por alguém | Média | O teste pode ter sido ajustado para passar |
| Depoimento do especialista | Intenção atual do negócio | Única fonte direta de intenção | Memória incompleta e confusão entre regra e costume |

Duas evidências que sustentam resultados incompatíveis para o mesmo caso configuram um **conflito**, registrado com as duas localizações. O código executável é a evidência mais forte do comportamento e o depoimento do especialista é a evidência mais forte da intenção, e por isso todo conflito entre essas duas fontes segue para a validação de domínio, o movimento 4 do método descrito adiante nesta página.

## Comportamento implementado e intenção de negócio

O código registra o **comportamento implementado**, isto é, o que o sistema faz hoje para cada combinação de entradas. A **intenção de negócio** é o que a organização quer que aconteça, e ela pode ter mudado depois da última alteração do código. Um valor literal pode representar uma regra válida, uma correção emergencial que nunca foi revista ou um erro preservado por anos sem que ninguém percebesse o efeito.

A validação de domínio compara cada hipótese de regra com a intenção declarada pelo especialista e produz um de três desfechos:

| Desfecho | Significado | O que acontece com a regra |
|---|---|---|
| Confirmada | O comportamento implementado corresponde à intenção atual | Entra no catálogo com a evidência e o nome de quem confirmou |
| Refutada | O comportamento implementado contraria a intenção atual | Entra no catálogo como defeito ou regra obsoleta, e a correção é decisão do domínio |
| Em aberto | O especialista não sabe responder ou a resposta depende de outra área | Permanece como hipótese, com a pergunta e o responsável pela resposta |

O desfecho "em aberto" é resultado válido e recebe o tratamento de uma lacuna, nome dado na formalização de políticas escritas à pergunta que a fonte não responde e que fica registrada sem resposta inventada. O catálogo registra cada hipótese em aberto com a pergunta ao especialista, o nome do responsável pela resposta e a evidência capturada no movimento 2 do método.

## Precedência, filtros e ausência de dado

Três mecanismos concentram a maior parte das regras que o código contém sem declarar. Nenhum dos três tem a forma de uma condição de negócio declarada, e por isso a leitura linear do código tende a omiti-los.

**Precedência implícita por ordem de avaliação.** Num `CASE WHEN` do SQL, a primeira condição verdadeira determina o resultado e as seguintes deixam de ser avaliadas, e o mesmo vale para uma cadeia de `if` e `else if` em C# ou TypeScript. Uma condição posterior pode, portanto, nunca produzir efeito para os casos que uma condição anterior já capturou. Essa ordem equivale à política de acerto First do [DMN](../referencia/bibliografia.md#decision-model-and-notation-dmn) (*Decision Model and Notation*, padrão da OMG para modelagem de decisões), em que vale a primeira linha aplicável. A tabela de decisão recuperada, que organiza em linhas as combinações de condições e o resultado de cada uma, precisa declarar essa política para preservar o comportamento implementado.

**Filtros que removem casos antes da classificação.** Um `WHERE` ou um `INNER JOIN` retira linhas antes de qualquer `CASE`, e a regra de elegibilidade fica fora da expressão que parece conter todas as regras. Um `LEFT JOIN` seguido de condição no `WHERE` sobre coluna da tabela da direita descarta as linhas sem correspondência e passa a se comportar como `INNER JOIN`. A regra de exclusão resultante é registrada com a linha da junção e a linha da condição no `WHERE`, porque é a combinação das duas que produz o efeito.

**Tratamento de ausência de dado.** No SQL, a comparação com `NULL` produz o valor lógico desconhecido, e um `WHERE` descarta a linha nesse caso. Um `CASE WHEN coluna > limite` sem ramo específico para `NULL` envia o caso ao `ELSE`, e um `COALESCE(coluna, 0)` converte a ausência do dado em zero antes de qualquer comparação. Cada uma dessas formas é uma decisão sobre quem não informou o dado, e a regra recuperada registra essa decisão com a linha que a produz.

## O método em seis movimentos

![Diagrama horizontal intitulado Arqueologia de regras: seis movimentos. À esquerda, um painel de código-fonte lista, sem números de linha, as construções COALESCE, CASE, WHEN ... limite, ELSE, INNER JOIN em destaque, LEFT JOIN e WHERE. Setas ligam o painel a seis caixas numeradas. A caixa 1, inventário, cita tabelas, colunas, literais e resultados. A caixa 2, captura de evidência, cita arquivo, linhas, trecho literal e a forma arquivo:linha. A caixa 3, hipóteses de regra, cita JOIN, WHERE e ordem do CASE com confiança. A caixa 4, validação de domínio, cita perguntas fechadas ao especialista, que confirma, refuta ou mantém aberta. A caixa 5, formalização SBVR, cita RC, RD e RN e tabela de decisão com política de acerto. A caixa 6, derivação de testes, cita testes de precedência e de dados ausentes. Uma faixa inferior, alimentada pelo movimento 2, informa que a evidência por linha é citada nos movimentos 3 a 6.](assets/arqueologia-metodo.png)

*Leitura da figura: comece pelo painel de código-fonte e percorra os movimentos numerados da esquerda para a direita. A seta contínua do movimento 2 desce para a faixa de evidência, e as setas tracejadas que sobem dela indicam os movimentos que citam arquivo, linha e trecho literal.*

### 1. Inventário

O inventário lista tabelas, colunas, valores literais e resultados possíveis do artefato e converte nomes técnicos em candidatos a conceitos, sem apagar o vínculo com a coluna ou a variável de origem. Os fatos entre conceitos entram nesse movimento na forma de tipos de fato, como "Pessoa possui Documento", e nenhum item recebe ainda o rótulo de regra.

### 2. Captura de evidência

Antes de qualquer interpretação, cada predicado recebe o arquivo, o intervalo exato de linhas e o trecho literal que o contém, seja uma cláusula `JOIN`, uma condição de `WHERE`, um ramo de `CASE` ou uma chamada a `COALESCE`. A evidência capturada nesse movimento é a base que as hipóteses, a validação e os testes citam nos movimentos seguintes.

### 3. Hipóteses de regra

Cada evidência é lida como indício de uma regra candidata. Um `INNER JOIN` pode conter uma regra de elegibilidade, um `WHERE` pode suprimir casos, a ordem de um `CASE` estabelece precedência e um `COALESCE` decide o tratamento da ausência, e cada hipótese recebe um grau de confiança e a evidência capturada no movimento 2.

### 4. Validação de domínio

As hipóteses chegam ao especialista do domínio na forma de perguntas fechadas, uma por hipótese, redigidas com os termos do negócio e acompanhadas do caso concreto que o código produz. Cada resposta confirma a hipótese, a refuta ou a mantém em aberto, e a confiança é atualizada com o nome de quem respondeu e a data da resposta.

### 5. Formalização SBVR

Cada hipótese é classificada num dos três tipos de regra do SBVR usados na sessão. A **regra estrutural de classificação** (RC) define a que categoria uma coisa pertence, a **regra estrutural de derivação** (RD) define como um valor é calculado a partir de outros, e a **regra operativa** (RN) rege a conduta de um ator identificável, que pode cumpri-la ou violá-la. Na falta de evidência de obrigação dirigida a um ator, a formalização registra a regra como estrutural, porque a existência de código que executa um cálculo não prova que alguém tenha o dever de executá-lo. As combinações relevantes entram numa **tabela de decisão** com a política de acerto declarada, isto é, o critério que diz qual linha vale quando mais de uma se aplica ao mesmo caso. A tabela expõe os conflitos entre uma classificação que indica impedimento e um cálculo que continua a produzir valor para o mesmo caso.

### 6. Derivação de testes

Os testes derivam das regras recuperadas e confirmam o comportamento atual do artefato para cada combinação relevante, com prioridade para os casos de precedência e de dados ausentes. A decisão sobre manter ou corrigir esse comportamento pertence à validação de domínio do movimento 4, e cada teste conserva o ID da regra e a evidência de origem.

## Testes de caracterização

[Feathers](../referencia/bibliografia.md#feathers-working-effectively-with-legacy-code-2004), em *Working Effectively with Legacy Code* (2004), cunhou o termo **teste de caracterização** para o teste que descreve o comportamento real de um trecho de código. O procedimento inverte a ordem habitual do TDD: o teste é escrito depois do código, a primeira execução revela o resultado atual e esse resultado passa a ser a expectativa registrada. A finalidade é proteger o comportamento existente contra mudanças não intencionais durante a manutenção.

O teste de caracterização registra o comportamento implementado e nada afirma sobre a intenção de negócio. O teste de aceitação deriva de uma regra confirmada pelo domínio e verifica a intenção declarada. O desfecho da validação de domínio determina a relação entre os dois testes, e a tabela abaixo liga cada desfecho ao destino do teste de caracterização.

| Desfecho da validação | Destino do teste de caracterização |
|---|---|
| Confirmada | Passa a valer como teste de regressão da regra, com o ID da regra no nome |
| Refutada | Documenta o defeito até a correção e é substituído pelo teste de aceitação quando o domínio decidir corrigir |
| Em aberto | Permanece marcado com o ID da questão de domínio, e sua expectativa não é tratada como requisito |

## O que um LLM faz bem e mal nessa tarefa

[Diggs et al.](../referencia/bibliografia.md#diggs-et-al-llms-for-legacy-code-documentation-2024) avaliaram em 2024 quatro modelos de linguagem na geração de comentários linha a linha para código legado em MUMPS, de um sistema de prontuário eletrônico, e em linguagem de montagem de mainframe IBM. Avaliadores com experiência profissional nas duas linguagens julgaram os comentários por completude, legibilidade, utilidade e ausência de alucinação. Os comentários foram, em geral, livres de alucinação, completos, legíveis e úteis quando comparados com comentários escritos por desenvolvedores, com desempenho pior na linguagem de montagem. Nenhuma métrica automática testada, entre elas complexidade ciclomática, métricas de Halstead e métricas de referência como BLEU e ROUGE, apresentou correlação forte com a qualidade julgada pelos avaliadores.

O estudo avalia a redocumentação, isto é, a descrição do que cada linha faz, e essa tarefa corresponde ao comportamento implementado. A página trata a aplicação do resultado à recuperação da intenção de negócio como inferência própria, sem medição publicada que a sustente. Dois resultados do estudo orientam o uso do agente na sessão: os especialistas julgaram confiável a descrição local de código produzida pelos modelos avaliados, e nenhuma métrica automática testada apresentou correlação forte com esse julgamento.

| O agente tende a fazer bem | O agente tende a fazer mal |
|---|---|
| Descrever o efeito de cada linha ou cláusula | Atribuir motivo a um valor literal sem fonte |
| Listar ramos, filtros e conversões de ausência | Perceber que um filtro distante altera a classificação |
| Propor casos de teste para cada ramo | Distinguir regra vigente de correção emergencial |
| Redigir perguntas fechadas para o especialista | Decidir o desfecho da validação no lugar do domínio |

A tabela é uma síntese desta página, sem medição publicada que a sustente, e a coluna da direita reúne as falhas que a sessão trata como risco a controlar. O controle adotado é exigir, para cada afirmação do agente, o arquivo, o intervalo exato de linhas e o trecho literal que a sustenta. O revisor confere se o intervalo existe e se o trecho transcrito coincide com o arquivo, e uma afirmação sem citação conferível entra no catálogo com o desfecho "em aberto" e a pergunta correspondente.

**Próxima página:** [Exemplo de aplicação de IA: arqueologia de regras](arqueologia-de-regras-exemplo-de-aplicacao-de-ia.md).
