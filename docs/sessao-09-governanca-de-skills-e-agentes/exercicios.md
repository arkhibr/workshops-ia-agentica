# Exercícios — triagem e riscos de uma skill

Os exercícios analisam uma skill da ACME, uma universidade fictícia, antes que ela seja compartilhada com colegas.

## O caso

A ACME tem uma skill que revisa pull requests contra padrões de arquitetura e escreve um parecer, com critérios de aprovação ainda não definidos. Por conveniência, a skill usa a credencial pessoal de quem a executa, com escrita em todos os repositórios dessa pessoa.

![A skill de revisão da ACME lê o código do pull request, compara com os padrões de arquitetura e produz um parecer, com critérios de aprovação indefinidos. Em laranja, a credencial pessoal dá escrita em todos os repositórios de quem executa, alcance maior que o repositório revisado.](assets/caso-da-skill-de-revisao.png)

As respostas compõem a ficha de governança desta skill, um registro curto que a equipe preenche antes de compartilhar uma skill com colegas. A ficha diz quem responde pela skill, que dados ela lê, quanto ela age sozinha, qual é o risco e que controles o reduzem.

## 1. Dono e finalidade

1. O dono é a pessoa ou a equipe que responde pela skill quando ela erra, mantém a ficha e decide retirá-la de uso. Quem seria o dono desta skill, e quem sofre as consequências de um parecer errado?
2. Antes de autorizar uma skill, registra-se como o trabalho seria feito sem IA, para verificar se o ganho justifica o risco novo. Como a revisão de pull requests seria feita sem IA?

??? note "Resposta esperada"
    1. A equipe de arquitetura da ACME é a dona, e os autores dos pull requests sofrem as consequências.
    2. Uma pessoa da arquitetura revisaria cada pull request com uma lista de verificação dos padrões.

## 2. Dados e autonomia

1. Para decidir o cuidado com a skill, cada dado que ela lê é classificado como público, interno (código privado, documentação interna), pessoal (dado que identifica uma pessoa) ou sensível (segredo, dado financeiro ou dado pessoal cuja exposição cause dano grave). Em qual dessas classes está o código revisado, e por quê?
2. A credencial dá à skill acesso aos repositórios e deve permitir só o que a tarefa exige. Que permissão a credencial pessoal dá, e que permissão a revisão de fato exige?
3. A autonomia diz quanto a skill age sozinha, em três níveis: ela sugere e uma pessoa decide, ela prepara a ação para aprovação explícita, ou ela executa sem aprovação prévia. Neste caso, a skill sugere, prepara para aprovação ou executa, e quem decide o merge?

??? note "Resposta esperada"
    1. O código revisado é dado interno, porque é código privado da ACME sem dado pessoal nem segredo.
    2. A credencial dá escrita em todos os repositórios, e a revisão exige leitura de um repositório e escrita do parecer.
    3. A skill sugere, porque uma pessoa decide o merge.

## 3. Faixa e fator decisivo

1. A faixa de risco é baixa para conteúdo público e só leitura, moderada para conteúdo interno ou decisão assistida e alta para dado sensível, efeito relevante sobre pessoas, escrita em sistemas ou execução financeira. Na forma estrita da regra, um único fator da faixa alta leva o caso direto a ela. Em que faixa a skill fica, e qual fator decide?
2. O uso fora da finalidade é o uso da skill para algo não autorizado, como alterar código quando ela foi criada só para dar parecer. Qual seria o impacto se a solução fosse usada fora da finalidade, com a credencial atual?
3. Uma premissa não verificada é algo que se supõe verdadeiro sem conferência, e quando ela mudaria a faixa caso fosse falsa, a faixa fica preliminar até a verificação. Que premissa deixa a faixa desta skill preliminar?

??? note "Resposta esperada"
    1. A faixa é alta pela credencial com escrita, e desce para moderada com token próprio de leitura.
    2. A skill poderia alterar qualquer repositório da pessoa que a executa.
    3. Ninguém verificou se o parecer é usado como aprovação, e essa verificação passa a ser condição do gate de publicação, o ponto em que a publicação fica bloqueada até a prova existir.

## 4. Risco como evento e consequência

1. Um dos [incidentes típicos](riscos-de-agentes.md#tres-incidentes) de agentes é a permissão maior que a finalidade, quando a skill tem mais acesso do que a tarefa pede. Para escolher um controle, escreve-se o risco no formato "se este evento acontecer, esta consequência ocorre". Como fica o risco desta skill nesse formato?
2. Uma fronteira de confiança é o ponto em que o dado muda de nível de confiança, e num agente há três: o conteúdo lido entra no contexto do modelo, a saída do modelo vira chamada de ferramenta, e a resposta produz efeito fora do sistema. Em qual delas o evento desta skill ocorre?

??? note "Resposta esperada"
    1. Se a skill escrever em outro repositório com a credencial pessoal, o código será alterado sem revisão humana.
    2. Quando a saída do modelo vira chamada de ferramenta, e o código do pull request, que não é confiável, leva o modelo a chamar uma escrita.

## 5. Controle preventivo e evidência

1. Um controle preventivo age antes do evento, e um controle aplicado fora do modelo, como permissão, hook ou política da API, funciona mesmo quando o modelo decide errado. Que controle preventivo aplicado fora do modelo reduz o risco do exercício 4?
2. Um controle detectivo mostra que o evento ocorreu, e a evidência é o registro que prova que um controle funcionou, como o relatório de um teste. Que controle detectivo e que teste servem para esta skill?
3. O `SKILL.md` é o arquivo de instruções que o modelo lê ao usar a skill. Por que pedir nele que a credencial seja usada só para leitura não basta como controle preventivo?

??? note "Resposta esperada"
    1. Um token próprio, somente de leitura e restrito ao repositório revisado.
    2. Um alerta para toda tentativa de escrita com o token da skill, e um teste em que a skill tenta alterar um repositório com token de leitura e a API rejeita a operação.
    3. Um controle que depende só de instrução no prompt pode ser ignorado pelo modelo, em especial quando o código lido traz instrução em sentido contrário.

## 6. Discussão com a turma

1. O PO, dono do produto, aprova o caso de uso quando a skill resolve um problema legítimo. Se o PO aprovou o caso, o time pode usar qualquer dado?
2. A skill do caso só lê código e escreve um parecer, sem alterar repositórios diretamente. Um agente que apenas lê tem risco baixo?
3. Uma avaliação mede quantos pareceres a skill acerta num conjunto de teste com resposta conhecida. E se a avaliação atingir 95% de acerto?

??? note "Resposta esperada"
    1. O uso dos dados depende de classificação, autorização de acesso e LGPD.
    2. O risco depende do que o agente lê e do uso da resposta, e um parecer errado pode orientar um merge.
    3. Os 5% restantes podem conter a escrita indevida, e a severidade dos erros também conta.

**Próxima página:** [Controles e evidências](controles-e-evidencias.md).
