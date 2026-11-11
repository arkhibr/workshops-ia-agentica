# Oficina de ferramentas

Nesta oficina, cada dupla prepara com o agente a ficha de um piloto de 90 dias para um processo da ACME, a universidade fictícia das Sessões 8 e 9, e depois submete a ficha a uma revisão numa conversa separada. A ficha reúne num só documento o que o curso construiu: o critério de aceite da Sessão 3, a ficha de requisitos da Sessão 8, a ficha de governança da Sessão 9 e a métrica de custo por resultado aceito da página [Métricas e economia](metricas-e-economia.md).

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

## Material de partida: três processos da ACME

Os três processos abaixo são fictícios e foram escritos para esta oficina, com números de linha de base inventados. O processo P3 é inspirado no domínio administrativo de projetos de pesquisa e não reproduz regra vigente de nenhuma instituição.

| Código | Processo | Volume mensal | Tempo humano atual | Qualidade atual | Responsável |
|---|---|---|---|---|---|
| P1 | Revisão de pull requests com a skill de revisão publicada na Sessão 9 | 140 pull requests | 35 minutos de revisão por pull request | 12% dos pull requests reabertos depois da integração | Líder técnico da equipe de sistemas acadêmicos |
| P2 | Preparação da pauta das reuniões de acompanhamento de projetos de pesquisa | 60 reuniões | 40 minutos de preparação por reunião | 15% das pautas apontadas como incompletas na própria reunião | Coordenação do escritório de projetos |
| P3 | Conferência das prestações de contas de despesas de projetos de pesquisa, com prazo interno de 30 dias | 220 prestações | 25 minutos de conferência por prestação | 4 conferências por mês reabertas por erro do conferente | Gerência financeira de projetos |

## Preparação

**Passo 1:** criar a pasta de trabalho e abrir o agente nela, com os comandos abaixo, que são iguais nos três sistemas. Troque `claude` por `codex` ou `gemini` conforme a ferramenta configurada.

```text
mkdir oficina-piloto
cd oficina-piloto
claude
```

O agente deve abrir a sessão interativa na pasta `oficina-piloto`, ainda vazia.

## Experimento A: escolher o processo

A dupla escolhe um dos três processos aplicando os quatro critérios de passagem do primeiro mês do [plano de 90 dias](horizontes-e-90-dias.md#o-plano-de-90-dias): resultado observável, responsável pelo processo, acesso viável e volume conhecido. Para o processo escolhido, a dupla anota também qual das [quatro formas de delegação](da-interacao-a-delegacao.md#as-quatro-formas-de-delegacao) se aplica a cada etapa, já que um mesmo processo costuma combinar fluxo de trabalho com IA nas etapas previsíveis e agente com autonomia delimitada nas etapas de investigação.

O registro esperado é uma linha por critério, com a informação da tabela de partida que o atende ou com a lacuna que impediria o piloto. No processo P2, por exemplo, o resultado observável depende de definir o que torna uma pauta completa antes de medir.

## Experimento B: preencher a ficha com o agente

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

Ao final, grave o arquivo ficha-piloto.md com estes nove campos:
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

O resultado esperado é um arquivo com os nove campos preenchidos ou marcados como "a definir", com o responsável indicado para cada lacuna. Se o agente preencher um número que a dupla não forneceu, a dupla registra o campo como falha da entrevista e pede a correção, porque o campo 3 só tem valor quando os números vêm da medição do processo.

## Experimento C: calcular o custo por resultado aceito

Este experimento usa o processo P3 para todos, para que os resultados sejam comparáveis. No segundo mês de um piloto fictício, o agente prepara a conferência das 220 prestações, e um conferente revisa cada uma antes do aceite. Os custos do mês são os da tabela abaixo, com hora de trabalho do conferente fixada em R$ 80 para o exercício.

| Item de custo | Valor no mês |
|---|---|
| Inferência | R$ 900 |
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

O custo por resultado aceito caiu cerca de 27%, e as reaberturas subiram de 4 para 18 no mês, mais de quatro vezes o valor da linha de base. Pelos critérios do terceiro mês, a ampliação depende de ganho líquido com recuperação funcional, e o aumento das reaberturas indica que o piloto precisa ser corrigido antes de ampliado, com a análise das 18 reaberturas para identificar se a falha está nos casos de avaliação, no contexto entregue ao agente ou na revisão do conferente.

</details>

## Experimento D: revisar a ficha numa conversa separada

A revisão numa conversa que não participou da entrevista aplica o mesmo princípio da retrotradução da [Sessão 4](../sessao-04-regras-formais-com-ia/index.md): quem revisa não conhece as intenções que ficaram fora do texto e por isso encontra as lacunas que a dupla já não enxerga.

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

O resultado esperado é uma lista de apontamentos em que pelo menos um trata de controle aplicado fora do modelo, o critério de reprovação da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/controles-e-evidencias.md), e uma seção final com a decisão da dupla sobre cada apontamento.

## Extensão: transpor para um processo da equipe

Depois da aula, a mesma ficha pode ser preenchida para um processo real da equipe, no ambiente interno e sem publicação. Os números da linha de base vêm da medição do processo atual, e a ficha preenchida serve como insumo para a política de uso de IA e para a decisão de piloto de 2027.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
