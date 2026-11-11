# Oficina de ferramentas

Nesta oficina, cada dupla prepara com um agente de IA a ficha de um piloto de 90 dias para um processo da ACME, a universidade fictícia das Sessões 8 e 9, e depois pede a revisão da ficha numa conversa separada. Um piloto é um teste do agente num processo real, com prazo e escopo limitados, e a ficha de piloto é o documento que registra, antes do início, o que será testado, como será medido e o que decide a continuação, conforme a página [Plano de 90 dias para testar um agente](plano-de-90-dias.md).

## Roteiro sugerido para a sessão

| Experimento | Tempo | Papel na aula |
|---|---|---|
| Experimento A, escolher o processo | 4 min | Essencial, em dupla |
| Experimento B, preencher a ficha com o agente | 8 min | Essencial, em dupla |
| Experimento C, calcular o custo por resultado aceito | 5 min | Essencial, individual |
| Experimento D, revisar a ficha numa conversa separada | 5 min | Essencial, em dupla |
| Extensão, transpor para um processo da equipe | Depois da aula | Opcional, no ambiente interno da equipe |

## Pré-requisitos

A oficina usa um agente de linha de comando já configurado na Sessão 2, como Claude Code, Codex CLI ou Gemini CLI, e funciona também numa conversa de chat comum, com a ficha copiada para um arquivo local ao final. Os dados dos três processos e do Experimento C são fictícios, e nenhum experimento usa credencial real ou documento interno da equipe.

## Processos da ACME usados na oficina

Os processos abaixo são fictícios e foram escritos para esta oficina. As colunas de volume, tempo e qualidade formam a linha de base de cada processo, isto é, a medição de como o processo funciona hoje, sem o agente, com números inventados para o exercício. O processo P3 é inspirado no domínio administrativo de projetos de pesquisa e não reproduz regra vigente de nenhuma instituição.

| Código | Processo | Volume mensal | Tempo humano atual | Qualidade atual | Responsável |
|---|---|---|---|---|---|
| P1 | Revisão de pull requests (pedidos de integração de código) com a skill de revisão publicada na Sessão 9 | 140 pull requests | 35 minutos de revisão por pull request | 12% dos pull requests reabertos depois da integração | Líder técnico da equipe de sistemas acadêmicos |
| P2 | Preparação da pauta das reuniões de acompanhamento de projetos de pesquisa | 60 reuniões | 40 minutos de preparação por reunião | 15% das pautas apontadas como incompletas na própria reunião | Coordenação do escritório de projetos |
| P3 | Conferência das prestações de contas de projetos de pesquisa, em que o pesquisador comprova as despesas feitas com o dinheiro do projeto, com prazo interno de 30 dias | 220 prestações | 25 minutos de conferência por prestação | 4 conferências por mês reabertas por erro do conferente | Gerência financeira de projetos |

## Preparação

**Passo 1:** criar a pasta de trabalho e abrir o agente nela, com os comandos abaixo, que são iguais nos três sistemas. Troque `claude` por `codex` ou `gemini` conforme a ferramenta configurada.

```text
mkdir oficina-piloto
cd oficina-piloto
claude
```

O agente deve abrir a sessão interativa na pasta `oficina-piloto`, ainda vazia.

## Experimento A: escolher o processo

A dupla escolhe um dos processos aplicando os critérios de passagem do primeiro mês do [plano de 90 dias](plano-de-90-dias.md#fases-do-piloto): o resultado do processo pode ser observado, há um responsável pelo processo, o agente pode ter acesso aos dados necessários e o volume de trabalho é conhecido. A dupla anota também qual das [quatro formas de delegar trabalho à IA](formas-de-delegar-trabalho.md#quem-escolhe-o-proximo-passo) se aplica a cada etapa do processo, considerando que etapas previsíveis podem usar fluxo de trabalho com IA e etapas de investigação podem usar agente com autonomia delimitada.

O registro esperado é uma linha por critério, com a informação da tabela de partida que o atende ou com a lacuna que impediria o piloto. No processo P2, por exemplo, a dupla precisa definir os itens de uma pauta completa antes de medir o percentual de pautas incompletas.

## Experimento B: preencher a ficha com o agente

A tabela explica o que cada campo da ficha de piloto registra, e os termos dela aparecem no prompt que a dupla vai colar no agente.

| Campo | O que registra |
|---|---|
| 1. Processo e responsável | O processo escolhido e a pessoa que responde por ele |
| 2. Decisões delegáveis e forma de delegação | Quais decisões o agente pode tomar e qual das formas de delegar trabalho à IA vale para cada etapa |
| 3. Linha de base | Volume, tempo, custo e qualidade do processo hoje, sem o agente |
| 4. Casos de avaliação | Exemplos de entrada com o resultado esperado, incluindo casos típicos, exceções e ataques simulados, como um documento com instruções maliciosas |
| 5. Métrica principal e contramétricas | O custo por resultado aceito e as medidas de efeito colateral que o acompanham, como o número de entregas reabertas |
| 6. Controles fora do modelo e identidade do agente | As regras de permissão aplicadas por sistemas que o agente não altera e o usuário próprio do agente nos sistemas da ACME |
| 7. Recuperação | Onde fica gravada uma tarefa que espera aprovação, quais operações são idempotentes (produzem o mesmo efeito se repetidas) e como interromper o agente |
| 8. Faixa de risco e aprovação | A faixa de risco baixa, moderada ou alta da ficha de governança da Sessão 9 e quem aprova formalmente o início do piloto, etapa chamada de gate |
| 9. Critérios de passagem | O que precisa estar comprovado nos dias 30, 60 e 90 para continuar |

**Passo 1:** colar o prompt abaixo no agente, substituindo `<P1, P2 ou P3>` pelo código escolhido no Experimento A e colando a linha correspondente da tabela de partida no lugar indicado.

```text
Você vai me entrevistar para preencher a ficha de um piloto de 90 dias de uso
de agente no processo <P1, P2 ou P3> da ACME, uma universidade fictícia.

Dados do processo (fictícios):
<cole aqui a linha da tabela de partida>

Regras da entrevista:
- Faça uma pergunta por vez e espere a minha resposta.
- Não invente números, nomes nem controles. Quando eu não souber, registre
  "a definir" e diga quem na ACME deveria responder.
- Não proponha soluções antes de terminar as perguntas de um campo.

Ao final, grave o arquivo ficha-piloto.md com estes campos:
1. Processo e responsável
2. Decisões delegáveis e forma de delegação de cada etapa
3. Linha de base (volume, tempo, custo e qualidade)
4. Casos de avaliação (típicos, exceções e ataques simulados)
5. Métrica principal (custo por resultado aceito) e contramétricas
6. Controles aplicados fora do modelo e identidade do agente
7. Recuperação (estado pendente, operações idempotentes e interrupção)
8. Faixa de risco e aprovação no gate, conforme a ficha de governança
9. Critérios de passagem nos dias 30, 60 e 90
```

**Passo 2:** responder às perguntas do agente até que ele grave o arquivo `ficha-piloto.md` na pasta.

O resultado esperado é um arquivo com todos os campos preenchidos ou marcados como "a definir", com o responsável indicado para cada lacuna. Se o agente preencher um número que a dupla não forneceu, a dupla registra o campo como falha da entrevista e pede a correção, porque o campo 3 só tem valor quando os números vêm da medição do processo.

## Experimento C: calcular o custo por resultado aceito

O custo por resultado aceito é o custo total do mês dividido pelo número de entregas que o processo aceitou como corretas, como explica a página [Medição do custo e do resultado de um agente](medicao-de-custo-e-resultado.md). Este experimento usa o processo P3 para todos, para que os resultados sejam comparáveis. No segundo mês de um piloto fictício, o agente prepara a conferência das 220 prestações, e um conferente revisa cada uma antes do aceite. Os custos do mês são os da tabela abaixo, com hora de trabalho do conferente fixada em R$ 80 para o exercício.

| Item de custo | Valor no mês |
|---|---|
| Inferência, isto é, uso do modelo de IA, cobrado pelo volume de texto processado | R$ 900 |
| Ferramentas e infraestrutura | R$ 600 |
| Supervisão: 6 minutos de revisão por prestação, nas 220 prestações | 22 horas |
| Retrabalho: 18 conferências reabertas, com 30 minutos cada | 9 horas |
| Alocação mensal do custo fixo de integração | R$ 1.000 |

**Passo 1:** calcular o custo total do mês, o número de resultados aceitos (prestações conferidas menos conferências reabertas) e o custo por resultado aceito do piloto.

**Passo 2:** calcular o mesmo indicador para a linha de base da tabela de partida, com 25 minutos de conferência por prestação, a mesma hora de R$ 80 e as 4 conferências reabertas do processo atual.

**Passo 3:** comparar os dois resultados com a contramétrica de reaberturas e decidir, pelos critérios do terceiro mês, se o piloto deve ser ampliado, corrigido ou interrompido.

<details>
<summary>Resultado de referência</summary>

O custo total do piloto é R$ 4.980, somando R$ 900 de inferência, R$ 600 de ferramentas e infraestrutura, R$ 1.760 de supervisão (22 horas a R$ 80), R$ 720 de retrabalho (9 horas a R$ 80) e R$ 1.000 de custo fixo alocado. Com 202 resultados aceitos (220 menos 18 reabertas), o custo por resultado aceito é de cerca de R$ 24,65.

Na linha de base, 220 conferências de 25 minutos somam cerca de 91,7 horas, ou R$ 7.333 no mês. Com 216 resultados aceitos (220 menos 4 reabertas), o custo por resultado aceito é de cerca de R$ 33,95.

O custo por resultado aceito caiu cerca de 27%, enquanto as reaberturas subiram de 4 para 18 no mês, 4,5 vezes o valor da linha de base. Pelos critérios do terceiro mês, a decisão é corrigir o piloto antes de ampliá-lo, começando pela análise das 18 reaberturas para identificar se a causa está nos casos de avaliação, no contexto entregue ao agente ou na revisão feita pelo conferente.

</details>

## Experimento D: revisar a ficha numa conversa separada

Na [Sessão 4](../sessao-04-regras-formais-com-ia/index.md), a equipe usou a retrotradução: uma conversa nova, que não viu como uma regra foi escrita, reescreve a regra com as próprias palavras, e as diferenças mostram o que ficou ambíguo. Este experimento usa a mesma ideia com a ficha de piloto, porque a nova conversa conhece apenas o texto da ficha e aponta as informações que a dupla deixou de escrever por considerá-las óbvias.

**Passo 1:** sair do agente, abrir uma nova sessão na mesma pasta e colar o prompt abaixo.

```text
Leia o arquivo ficha-piloto.md desta pasta. Não altere o arquivo.

Aponte, campo por campo:
- afirmações sem número ou sem fonte de medição.
- critérios de passagem que não dá para verificar no dia indicado.
- controles que dependem apenas de instrução escrita ao modelo.
- casos de avaliação ausentes para exceções ou para ataques simulados.
- campos marcados "a definir" sem responsável.

Termine com as três correções que mais reduzem o risco do piloto.
```

**Passo 2:** comparar os apontamentos com a ficha e registrar, no fim do arquivo `ficha-piloto.md`, quais correções a dupla aceita e quais rejeita, com o motivo de cada rejeição.

O resultado esperado é uma lista de apontamentos com pelo menos um item sobre controle aplicado fora do modelo, conforme o critério da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/controles-e-evidencias.md), seguida da decisão da dupla sobre cada apontamento.

## Extensão: transpor para um processo da equipe

Depois da aula, a mesma ficha pode ser preenchida para um processo real da equipe, no ambiente interno e sem publicação. Os números da linha de base vêm da medição do processo atual, e a ficha preenchida serve como insumo para a política de uso de IA e para a decisão de piloto de 2027.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
