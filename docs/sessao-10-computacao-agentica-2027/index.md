# S10 — Computação agêntica em 2027

**Bloco:** 4 — Skills, agentes e computação agêntica

> **Pergunta-guia:** quais capacidades da computação agêntica merecem investimento da equipe em 2027, e que evidência sustenta cada uma delas?

## Problema

As nove sessões anteriores construíram uma prática de engenharia agêntica dentro da equipe: ambiente compartilhado, especificação verificável, regras formais, teste antes do código, casos de uso por papel, skills, agentes e governança antes do compartilhamento. O mercado anuncia, ao mesmo tempo, agentes persistentes, assistentes proativos, protocolos entre agentes e pagamentos mediados por agentes, quase sempre com números de adoção e de retorno misturados em uma mesma apresentação. Sem um critério para separar pesquisa, caso relatado, piloto, capacidade de produto e previsão de analista, a equipe tende a escolher o próximo investimento pela notícia mais recente, e a experiência acumulada no curso fica sem aplicação na decisão.

## Integração do curso com o horizonte de 2027

A sessão fecha o curso em duas partes. A primeira parte retoma o percurso das Sessões 1 a 9 e o confronta com o relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026), com dados consultados até 10/11/2026, que reúne as leituras de McKinsey, Gartner e Forrester, estudos empíricos, onze tendências para 2027 a 2030, assistentes pessoais proativos e casos relatados por empresas. A segunda parte transforma esse panorama numa decisão prática: a arquitetura que mantém a autonomia sob controle, a métrica de custo por resultado aceito e um plano de 90 dias para testar um processo antes de ampliar a delegação.

A tabela abaixo mostra a correspondência que organiza a sessão inteira. Cada prática construída no curso aparece no relatório como capacidade que as empresas precisarão operar em escala.

| Prática construída no curso | Sessão | Capacidade correspondente no horizonte de 2027 |
|---|---|---|
| Arnês, engenharia de contexto, MCP e arquivo de instrução | S2 | Contexto, memória e skills como ativos de engenharia, e interoperabilidade por protocolo |
| Especificação BR/FR/NFR e critério de aceite verificável | S3 e S5 | Engenharia de software por delegação, com critérios de aceite executáveis |
| Regras formais e tabelas de decisão | S4 | Processos híbridos, com regras explícitas nos passos determinísticos |
| Teste antes do código e análise da spec | S6 | Validação proporcional à capacidade de produzir alterações |
| Casos de uso por papel com fonte de comparação | S7 | Resultado aceito como unidade de medida |
| Skills, agentes, custo e credenciais | S8 | Identidade própria, economia por resultado e combinação de modelos |
| Governança, controles fora do modelo e marketplace | S9 | Controles externos ao modelo e revisão da cadeia de suprimentos de skills |

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** as quatro formas de delegação de trabalho (resposta assistida, fluxo de trabalho com IA, agente com autonomia delimitada e sistema com múltiplos agentes) pelo responsável pela escolha do próximo passo.
2. **Classificar** uma afirmação sobre agentes como evidência empírica, caso operacional relatado, piloto, capacidade de produto, previsão de analista ou hipótese.
3. **Relacionar** as onze tendências para 2027 a 2030 às práticas construídas nas Sessões 1 a 9.
4. **Identificar**, numa arquitetura de agente, onde ficam o estado do trabalho, a autorização, o sistema de registro e a intervenção humana.
5. **Calcular** o custo por resultado aceito de um processo e escolher as contramétricas que acompanham esse número.
6. **Elaborar** a ficha de um piloto de 90 dias, com linha de base, casos de avaliação, controles e critérios de passagem entre as fases.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O percurso do curso](percurso-do-curso.md) | Retomada | 8 min | As decisões que cada sessão deixou registradas e a capacidade de 2027 que cada uma antecipa |
| 2 | [Da interação à delegação](da-interacao-a-delegacao.md) | Teoria | 6 min | As quatro formas de delegação e o ciclo do objetivo ao resultado aceito |
| 3 | [Evidência e previsão](evidencia-e-previsao.md) | Teoria | 9 min | O que McKinsey, Gartner, Forrester e os estudos empíricos permitem afirmar |
| 4 | [Tendências para 2027 a 2030](tendencias-2027-2030.md) | Teoria | 12 min | As onze tendências em quatro frentes, com a condição crítica de cada uma |
| 5 | [Assistentes pessoais proativos](assistentes-proativos.md) | Teoria | 6 min | A hipótese de tendência prática e os pontos em que ela precisa ser contestada |
| 6 | [Casos reais](casos-reais.md) | Teoria | 6 min | O alcance da evidência em cada caso relatado |
| 7 | [Exercícios](exercicios.md) | Prática | 13 min | Classificação de afirmações e relação entre tendências e práticas do curso |
| | Intervalo às 11:00 | | 5 min | |
| 8 | [Arquitetura de referência](arquitetura-de-referencia.md) | Teoria | 10 min | Estado, arnês, ambiente, autorização e modos de falha |
| 9 | [Métricas e economia](metricas-e-economia.md) | Teoria | 9 min | Custo por resultado aceito, contramétricas e confiabilidade do processo |
| 10 | [Horizontes e plano de 90 dias](horizontes-e-90-dias.md) | Teoria | 7 min | Três cenários e as passagens de um piloto de 90 dias |
| 11 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 22 min | Ficha de piloto de 90 dias preenchida com o agente e revisada em conversa separada |
| 12 | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 7 min | Checklist do curso, sinais para reavaliar as tendências e fontes completas |
| | | | **120 min** | |

## Como conduzir

A primeira hora trata do panorama e a segunda trata da decisão. O risco de condução da primeira hora é a sessão se transformar em apresentação de produtos, e a página [Evidência e previsão](evidencia-e-previsao.md) existe para impedir isso: cada número citado depois dela é lido com a classificação de afirmações que ela apresenta. Os nomes de produtos mudam mais depressa do que as funções arquiteturais, e por isso a sessão organiza o conteúdo pela função (registrar o trabalho, conduzir a execução, oferecer ferramentas e controlar ações) e usa os produtos como exemplos datados.

A oficina usa a ACME, a universidade fictícia das Sessões 8 e 9, e três processos candidatos descritos na própria página. Nenhum exercício usa dado real, credencial real ou documento interno, e a transposição para um processo da equipe entra como extensão no fim da oficina, feita no ambiente interno e sem publicação.

!!! warning "Limite desta sessão"
    Os resultados de empresas citados nesta sessão são relatos públicos das organizações ou dos fornecedores e não passaram por auditoria independente. As previsões de analistas descrevem expectativas para datas futuras, e as classificações de confiança alta, média e baixa usadas no relatório são avaliações editoriais da direção de cada tendência, sem valor de probabilidade calculada. Os produtos e as versões mencionados correspondem à consulta de 10/11/2026.

**Próxima página:** [O percurso do curso](percurso-do-curso.md).
