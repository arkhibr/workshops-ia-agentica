# Exercícios — triagem e riscos dos protótipos

Este bloco aplica a triagem por criticidade e a análise de riscos a cinco casos da ACME, a universidade fictícia usada na Sessão 8 e nesta sessão. Os exercícios preenchem quatro linhas da ficha de governança, a tabela de oito linhas que registra o que precisa estar decidido antes de outra pessoa da equipe instalar uma skill ou um agente: "Dados e ferramentas", "Autonomia", "Faixa de risco" e "Riscos e controles".

A turma trabalha em grupos de três a cinco pessoas, e cada grupo escolhe um caso diferente da tabela abaixo. O exercício 1 classifica o caso numa faixa, o exercício 2 registra um risco e os controles para o mesmo caso e o exercício 3 reúne a turma nas seis discussões orientadas do guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026).

!!! note "Ambiente"
    Os três exercícios dispensam computador e terminal, e cada grupo registra as respostas num editor de texto ou numa folha de papel. Os casos são fictícios, e nenhum dos exercícios usa dado real, credencial real ou o repositório privado do participante.

## Material de partida: os casos da ACME

Cada caso descreve uma skill ou um agente em construção numa equipe de desenvolvimento da ACME. A coluna "Premissas do enunciado" traz fatos que o grupo aceita como dados do exercício, e a ficha os registra na linha de premissas, com o nome de quem os verificaria num caso real.

| Caso | Descrição | Premissas do enunciado |
|---|---|---|
| 1 | Skill que revisa pull requests contra padrões de arquitetura da ACME e escreve um parecer para a pessoa revisora | A skill usa a credencial pessoal de quem a executa, que tem permissão de escrita em todos os repositórios da pessoa. Os critérios de aprovação de um pull request ainda não foram definidos. |
| 2 | Fluxo com vários agentes que implementa uma funcionalidade a partir de uma especificação e abre o pull request | O código gerado chegou ao pull request com testes de ponta a ponta falhando. Nenhuma revisão de arquitetura foi feita sobre o código produzido pelo fluxo. |
| 3 | Skill que prioriza itens de trabalho lidos de uma ferramenta de gestão e sugere a ordem da próxima iteração | O token da skill lê todos os itens da equipe, inclusive comentários com nomes de pessoas. A equipe pediu que a skill passe a reordenar e fechar itens diretamente na ferramenta. |
| 4 | Agente que levanta onde um campo é usado num sistema legado, lendo o código de vários repositórios internos | O agente entrega a lista em minutos, e a lista só é confiável depois da conferência pelas equipes donas de cada repositório. Duas equipes usam o resultado para estimar uma mudança de esquema. |
| 5 | Skill `identificando-tarefas-e-riscos` da Sessão 8, que extrai tarefas e riscos de transcrições de reunião | As transcrições citam nomes de pessoas e podem conter instrução embutida no texto falado. Ninguém verificou ainda a premissa de que as transcrições não contêm dado sensível. O relatório gerado circula para a equipe do projeto depois de uma revisão humana. |

O caso 5 é o mesmo plugin que a [oficina](oficina-de-ferramentas.md) empacota num marketplace local, com a ficha `governanca.json` já preenchida, e o grupo que o escolher pode comparar a própria triagem com a ficha publicada lá.

## 1. Triagem do caso

O grupo preenche a ficha de triagem, adaptada da ficha A do guia, para o caso escolhido, e defende a faixa pelo fator mais grave. A página [Triagem por criticidade](triagem-por-criticidade.md) traz as três faixas, as quatro classes de dado e a regra de que um fator crítico leva o caso direto à faixa alta, sem soma de pontos, na forma estrita adotada nesta sessão.

| Campo da ficha | Resposta do grupo |
|---|---|
| Nome do caso e dono | |
| Problema resolvido e benefício esperado | |
| Usuário e pessoa impactada pelo resultado | |
| Dados lidos (público, interno, pessoal, sensível) | |
| Modelo, skills, servidores MCP e APIs | |
| Permissão (ler, recomendar, escrever, executar) | |
| Autonomia (sugere, prepara para aprovação, executa) e quem interrompe | |
| Revisão humana e efeito de um erro | |
| Faixa preliminar e fator que a decidiu | |
| Premissas não verificadas e quem as verifica | |

Depois de preencher a ficha, o grupo responde às quatro perguntas-guia da ficha A e à pergunta crucial da dinâmica, e registra se alguma resposta mudou a faixa.

1. Quem sofreria com o pior erro plausível?
2. Há algum dado ou integração que não deveria chegar ao modelo?
3. O modelo poderia escolher uma ação que o usuário não autorizou?
4. Qual evidência falta para decidir?
5. Qual seria o impacto se a solução fosse usada fora da finalidade?

**Rubrica**

| Critério | Atende | Não atende |
|---|---|---|
| Fator decisivo | A justificativa nomeia um fator da ficha e a regra que o liga à faixa | A faixa resulta de média, soma ou impressão geral do caso |
| Premissas | Cada premissa aparece separada dos fatos, com o nome de quem a verifica | A premissa entra como fato, ou a ficha omite as premissas do enunciado |
| Uso fora da finalidade | A resposta à pergunta 5 confirma ou altera a faixa, com o motivo escrito | A pergunta 5 recebe resposta genérica, sem efeito sobre a ficha |
| Autonomia | A ficha diz quem interrompe o agente e em que momento | A linha de autonomia fica sem responsável |

??? info "Pontos de chegada para o instrutor"
    As faixas abaixo decorrem das premissas do enunciado e da regra do fator crítico adotada nesta sessão. Um grupo que chegar a outra faixa com um fator nomeado e uma premissa explícita atende à rubrica.

    | Caso | Faixa esperada | Fator que decide |
    |---|---|---|
    | 1 | Alta enquanto a credencial pessoal ampla for usada | A credencial permite escrita em sistemas, mesmo que a skill só precise ler o pull request. Com um token próprio e somente de leitura, a faixa desce para moderada. |
    | 2 | Moderada se uma pessoa aprova o merge, alta se o fluxo integra o código sozinho | A autonomia decide a faixa, e os testes falhando mostram que a revisão humana ainda não está funcionando como controle. |
    | 3 | Moderada para a leitura, alta depois do pedido de reordenar e fechar itens | O pedido muda a permissão de ler para escrever, e a ficha precisa ser revista antes da mudança. |
    | 4 | Moderada | O código é interno e a saída é recomendação, e a pergunta 1 mostra que o pior erro é uma estimativa errada usada por duas equipes. |
    | 5 | Moderada, preliminar até a verificação da premissa | Os dados são internos e pessoais. A premissa de ausência de dado sensível levaria o caso à faixa alta se fosse falsa, e por isso a faixa fica preliminar e a verificação dessa premissa passa a ser condição do gate de publicação. |

## 2. Riscos e controles

Para o mesmo caso do exercício 1, o instrutor entrega a cada grupo um dos três cartões de incidente da página [Riscos de agentes](riscos-de-agentes.md): A, instrução escondida no documento, B, permissão maior que a finalidade, ou C, resposta plausível e incorreta. A distribuição sugerida associa o cartão B aos casos 1 e 3, o cartão C aos casos 2 e 4 e o cartão A ao caso 5.

O grupo transpõe o incidente para o próprio caso e preenche uma linha da ficha de registro de riscos, adaptada da ficha B do guia. O risco é escrito como evento e consequência, no formato "documento malicioso induz chamada a API externa e expõe dados do usuário", e cada célula marca o que é fato do enunciado, o que é hipótese do grupo e o que é decisão pendente.

| Campo | Resposta do grupo |
|---|---|
| Risco, como evento e consequência | |
| Fronteira de confiança em que o evento ocorre | |
| Impacto e hipótese | |
| Controle preventivo e onde ele é aplicado | |
| Controle detectivo e resposta prevista | |
| Evidência que prova o controle e onde ela fica guardada | |
| Teste de aceite correspondente, entre T01 e T07 | |

**Critério de reprovação.** O controle preventivo que depende só de instrução no prompt ou no `SKILL.md` reprova a linha, porque o modelo pode deixar de segui-la diante de um conteúdo que diga o contrário. A página [Controles e evidências](controles-e-evidencias.md) lista os mecanismos aplicados fora do modelo que atendem ao critério: permissão de ferramenta, hook, validação de esquema e política na API.

**Rubrica**

| Critério | Atende | Não atende |
|---|---|---|
| Formulação do risco | Evento e consequência numa frase, com o dano nomeado | Categoria genérica, como "segurança" ou "vazamento" |
| Controle preventivo | Executado por componente que o modelo não altera | Instrução textual dirigida ao modelo |
| Controle detectivo | Diz o que é registrado e quem recebe o alerta | Revisão sem responsável ou sem periodicidade |
| Evidência | Nomeia o teste ou o registro e o local de guarda | Afirma que o controle existe sem indicar a prova |

??? info "Pontos de chegada para o instrutor"
    | Caso e cartão | Risco esperado | Controle preventivo aceitável |
    |---|---|---|
    | 1 e B | A credencial pessoal ampla permite ao agente alterar repositórios além do pull request revisado, e uma alteração indevida chega a um repositório sem pedido de ninguém | Token próprio do agente, somente de leitura e restrito ao repositório revisado, com o teste T03 como evidência |
    | 2 e C | O fluxo abre um pull request com código que parece correto e testes falhando, e o código entra na base se a revisão confiar na descrição do pull request | Esteira que bloqueia o merge com teste falhando e exige revisão de arquitetura registrada |
    | 3 e B | A skill recebe permissão de escrita e fecha itens que a equipe ainda trabalharia, e o histórico de prioridade se perde | Token de leitura até a revisão da ficha e confirmação humana para cada escrita, com auditoria das ações |
    | 4 e C | O agente omite um uso do campo num repositório pouco citado, e a mudança de esquema quebra esse sistema em produção | Conferência obrigatória pela equipe dona de cada repositório antes do uso da lista, registrada na própria lista |
    | 5 e A | Uma frase da transcrição é lida como instrução e insere um responsável inventado no relatório | Script que confere o formato do relatório e exige um trecho de evidência por item, com a revisão humana como controle detectivo |

    O plugin `revisando-pull-requests` da oficina parte do cenário do caso 1 e reproduz só o risco e o controle reprovado, porque a ficha dele declara como preventivo o pedido ao modelo para usar a credencial só para leitura e o portão da oficina reprova a publicação por esse motivo. A faixa moderada declarada nessa ficha diverge do ponto de chegada do caso 1 no exercício 1, e o Experimento B da oficina registra que o portão não detecta essa divergência.

## 3. Discussões orientadas

A turma volta ao grupo inteiro, e cada grupo apresenta a faixa e o risco do próprio caso. O instrutor conduz a socialização com as seis perguntas das discussões orientadas do guia, escolhendo para cada pergunta o caso da turma que melhor a ilustra, e usa o ponto de chegada como gabarito.

1. Se o PO aprovou o caso, o time pode usar qualquer dado?
2. Se o prompt pede para não vazar dados, já existe controle?
3. Um agente que apenas lê tem risco baixo?
4. Qual é o perigo de dar ao agente permissão ampla por conveniência?
5. E se a avaliação atingir 95% de acerto?
6. O que a equipe deve fazer quando trocar o modelo?

??? info "Pontos de chegada"
    | Pergunta | Ponto de chegada | Caso que ilustra |
    |---|---|---|
    | 1 | A aprovação da finalidade deixa em aberto a autorização dos dados, que depende da classificação, da autorização de acesso e das condições legais, como as da LGPD para dado pessoal | 3 e 5 |
    | 2 | A instrução textual é insuficiente sem um mecanismo externo verificável, como o bloqueio de rede ou o escopo do token, que o teste T01 confere | 5 |
    | 3 | O risco depende do que o agente lê e do uso da resposta, porque a leitura pode expor dado e produzir uma decisão equivocada | 4 |
    | 4 | A permissão ampla aumenta o impacto de uma falha, de uma injeção de prompt e do uso indevido das ferramentas, risco que o OWASP chama de agência excessiva (LLM03, 2026) | 1 |
    | 5 | Uma métrica isolada não cobre os casos graves, e a equipe observa a severidade e a cauda dos erros, porque os 5% restantes podem conter a escrita indevida | 2 |
    | 6 | A equipe reavalia o comportamento, a compatibilidade, a segurança, o custo e os critérios de release, e a troca de modelo é um gatilho de revisão da ficha | Todos |

## Extensão: o protótipo real do grupo

Depois da sessão, cada grupo repete os exercícios 1 e 2 com o protótipo real em que trabalha, no ambiente interno da equipe. A ficha preenchida fica no repositório ou no espaço de documentação interno da equipe, sem publicação neste site e sem cópia para o repositório público do workshop, e a ficha descreve a credencial pelo tipo e pelo escopo, sem conter o valor de nenhuma credencial.

A turma consolida as fichas dos grupos numa proposta de três controles mínimos para a política de uso de IA da organização, cada um com o risco que trata, o mecanismo fora do modelo que o aplica e a evidência que fica guardada. A página [Controles e evidências](controles-e-evidencias.md) traz a ficha C do guia, que transforma cada controle em história, critério de aceite e teste.

**Próxima página:** [Controles e evidências](controles-e-evidencias.md).
