# Exercícios — triagem e riscos dos protótipos

Em aula, cada grupo de três a cinco pessoas faz os exercícios 1 a 5 com um caso da ACME, a universidade fictícia usada na Sessão 8 e nesta sessão, e a turma faz junta o exercício 6, enquanto a extensão do fim da página fica para depois da sessão.

Os exercícios 1 a 5 preenchem cinco linhas da ficha de governança, a tabela de oito linhas que registra o que precisa estar decidido antes de outra pessoa da equipe instalar uma skill ou um agente: "Dono e finalidade", "Dados e ferramentas", "Autonomia", "Faixa de risco" e "Riscos e controles".

!!! note "Ambiente"
    Os exercícios dispensam computador e terminal, e cada grupo registra as respostas num editor de texto ou numa folha de papel. Os casos são fictícios e nenhum exercício usa dado real, credencial real ou o repositório privado do participante.

## Material de partida: os casos da ACME

Cada grupo escolhe um caso diferente e trata as premissas como dados do exercício, registrando cada uma na ficha com o nome de quem a verificaria num caso real.

| Caso | Skill ou agente | Premissas do enunciado |
|---|---|---|
| 1 | Skill que revisa pull requests contra padrões de arquitetura da ACME e escreve um parecer | Usa a credencial pessoal de quem a executa, com escrita em todos os repositórios dessa pessoa. Os critérios de aprovação não foram definidos. |
| 2 | Fluxo com vários agentes que implementa uma funcionalidade a partir de uma especificação e abre o pull request | O pull request chegou com testes de ponta a ponta falhando e sem revisão de arquitetura. |
| 3 | Skill que prioriza itens de trabalho de uma ferramenta de gestão e sugere a ordem da próxima iteração | O token lê todos os itens da equipe, inclusive comentários com nomes de pessoas. A equipe pediu que a skill passe a reordenar e fechar itens. |
| 4 | Agente que levanta onde um campo é usado num sistema legado, lendo vários repositórios internos | A lista só é confiável depois da conferência pelas equipes donas, e duas equipes a usam para estimar uma mudança de esquema. |
| 5 | Skill `identificando-tarefas-e-riscos` da Sessão 8, que extrai tarefas e riscos de transcrições de reunião | As transcrições citam nomes e podem conter instrução embutida. Ninguém verificou se há dado sensível nelas. O relatório circula depois de uma revisão humana. |

O caso 5 é o plugin que a [oficina](oficina-de-ferramentas.md) empacota com a ficha `governanca.json` preenchida, e o grupo que o escolher pode comparar a própria triagem com essa ficha.

## 1. Dono e finalidade

O grupo escreve quem responde pelo caso, que problema ele resolve, quem usa o resultado e quem é afetado por ele. A [decisão 1 da governança](governanca-de-ia.md#quatro-decisoes) pede também a alternativa sem IA, que mostra se o benefício esperado justifica o risco novo.

**Entregue:** a linha "Dono e finalidade" com dono, finalidade, pessoa impactada e alternativa sem IA.

**Critério:** o dono é uma área ou pessoa identificável, e a alternativa sem IA descreve como o trabalho seria feito hoje.

## 2. Dados e autonomia

O grupo classifica os dados que o caso lê nas quatro classes da [triagem](triagem-por-criticidade.md#dados-e-ferramentas), público, interno, pessoal e sensível, e registra as ferramentas com a permissão de cada uma (ler, recomendar, escrever ou executar). Em seguida, marca se o caso sugere, prepara para aprovação ou executa.

**Entregue:** as linhas "Dados e ferramentas" e "Autonomia", com o nome de quem interrompe o agente.

**Critério:** cada classe de dado vem de uma premissa do enunciado, e a linha de autonomia diz quem interrompe o agente e em que momento.

## 3. Faixa e fator decisivo

O grupo classifica o caso numa das três faixas pelo fator mais grave, com a regra do fator crítico na forma estrita adotada como decisão desta sessão: um fator crítico leva o caso direto à faixa alta, sem soma de pontos. Antes de fechar a faixa, o grupo responde à pergunta crucial do guia: "Qual seria o impacto se a solução fosse usada fora da finalidade?".

**Entregue:** a linha "Faixa de risco", com a faixa, o fator que a decidiu e as premissas não verificadas.

**Critério:** a justificativa nomeia um fator da ficha, sem média nem impressão geral. A premissa não verificada que mudaria a faixa se fosse falsa torna a faixa preliminar, e a verificação dela passa a ser condição do gate de publicação.

??? note "Ponto de chegada"
    Uma faixa diferente, com fator nomeado e premissa explícita, também atende ao critério.

    - Caso 1: alta enquanto a credencial pessoal ampla for usada, porque ela permite escrita. Com token próprio e somente de leitura, a faixa desce para moderada.
    - Caso 2: moderada se uma pessoa aprova o merge e alta se o fluxo integra o código sozinho, e os testes falhando mostram que a revisão humana ainda não funciona como controle.
    - Caso 3: moderada para a leitura e alta depois do pedido de reordenar e fechar itens, que muda a permissão de ler para escrever.
    - Caso 4: moderada, porque o código é interno, a saída é recomendação e o pior erro é uma estimativa errada usada por duas equipes.
    - Caso 5: moderada e preliminar, porque a premissa de ausência de dado sensível levaria o caso à faixa alta se fosse falsa.

## 4. Risco como evento e consequência

O instrutor entrega a cada grupo um cartão de incidente da página [Riscos de agentes](riscos-de-agentes.md#tres-incidentes): o cartão B, permissão maior que a finalidade, aos casos 1 e 3, o cartão C, resposta plausível e incorreta, aos casos 2 e 4, e o cartão A, instrução escondida no documento, ao caso 5. O grupo transpõe o incidente para o próprio caso.

**Entregue:** uma frase de risco no formato "documento malicioso induz chamada a API externa e expõe dados do usuário", com a fronteira de confiança em que o evento ocorre.

**Critério:** a frase nomeia o evento e o dano, sem categoria genérica como "segurança", e marca o que é fato do enunciado e o que é hipótese do grupo.

## 5. Controle preventivo e evidência

Para o risco do exercício 4, o grupo propõe um controle preventivo, um controle detectivo e a evidência que prova o controle, com o teste de aceite correspondente entre [T01 e T07](controles-e-evidencias.md#testes-de-aceite-t01-a-t07).

**Entregue:** a linha "Riscos e controles", com onde o preventivo é aplicado, quem recebe o alerta do detectivo e onde a evidência fica guardada.

**Critério:** o controle preventivo que depende só de instrução no prompt ou no `SKILL.md` reprova a linha, porque o modelo pode deixar de segui-la diante de um conteúdo que diga o contrário. Atendem ao critério a permissão de ferramenta, o hook, a validação de esquema e a política na API, conforme a página [Controles e evidências](controles-e-evidencias.md#controle-fora-do-modelo-e-instrucao-textual).

??? note "Ponto de chegada"
    - Caso 1: token próprio, somente de leitura e restrito ao repositório revisado, com o teste T03 como evidência.
    - Caso 2: esteira que bloqueia o merge com teste falhando e exige revisão de arquitetura registrada.
    - Caso 3: token de leitura até a revisão da ficha e confirmação humana para cada escrita, com auditoria das ações.
    - Caso 4: conferência obrigatória pela equipe dona de cada repositório antes do uso da lista, registrada na própria lista.
    - Caso 5: script que confere o formato do relatório e exige um trecho de evidência por item, com a revisão humana como controle detectivo.

    O plugin `revisando-pull-requests` da oficina parte do caso 1 e declara como preventivo o pedido ao modelo para usar a credencial só para leitura, e o portão da oficina reprova a publicação por esse motivo. A faixa moderada declarada nessa ficha diverge do ponto de chegada do exercício 3, e o Experimento B registra que o portão não detecta essa divergência.

## 6. Discussão com a turma

Cada grupo apresenta a faixa e o risco do próprio caso, e o instrutor conduz três das discussões orientadas do guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), escolhendo para cada pergunta o caso da turma que melhor a ilustra.

1. Se o PO aprovou o caso, o time pode usar qualquer dado?
2. Um agente que apenas lê tem risco baixo?
3. E se a avaliação atingir 95% de acerto?

??? note "Ponto de chegada"
    1. A aprovação da finalidade deixa em aberto a autorização dos dados, que depende da classificação, da autorização de acesso e das condições legais, como as da LGPD para dado pessoal (casos 3 e 5).
    2. O risco depende do que o agente lê e do uso da resposta, porque a leitura pode expor dado e produzir uma decisão equivocada (caso 4).
    3. Uma métrica isolada deixa de cobrir os casos graves, e a equipe observa a severidade e a cauda dos erros, porque os 5% restantes podem conter a escrita indevida (caso 2).

## Extensão: o protótipo real do grupo

Depois da sessão, o grupo repete os exercícios 1 a 5 com o protótipo real em que trabalha, no ambiente interno da equipe, sem publicação neste site e sem cópia para o repositório público do workshop. A ficha descreve a credencial pelo tipo e pelo escopo, sem conter o valor de nenhuma credencial.

**Próxima página:** [Controles e evidências](controles-e-evidencias.md).
