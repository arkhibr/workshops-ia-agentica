# O percurso do curso

O workshop conduziu a equipe, ao longo de nove sessões de duas horas, do uso individual e sem método de assistentes de IA até um ambiente em que o agente executa trabalho sob especificação, verificação e governança definidas pela própria equipe. Esta página retoma a pergunta-guia de cada sessão e a decisão que ela deixou registrada, para que o panorama de 2027 tratado nas páginas seguintes seja lido a partir do que a equipe já pratica.

## As nove sessões e o que cada uma deixou registrado

| Sessão | Pergunta-guia | Decisão ou artefato que permanece |
|---|---|---|
| [S1 — O que mudou](../sessao-01-o-que-mudou/index.md) | Por que a equipe já usa IA todo dia e o resultado continua desigual? | A distinção entre vibe coding, assistência de codificação e SDD pelo artefato que governa a qualidade, e o princípio de começar pela solução mais simples |
| [S2 — O ambiente agêntico](../sessao-02-ambiente-agentico/index.md) | O que muda quando o time passa a compartilhar um ambiente? | A equação agente igual a modelo mais arnês, o arquivo de instrução comum, o MCP e o isolamento do trabalho por ramo |
| [S3 — Exploração e especificação](../sessao-03-exploracao-especificacao/index.md) | Por que um pedido tecnicamente correto ainda produz o sistema errado? | O ciclo explorar, perguntar, propor e especificar, com requisitos classificados como BR, FR ou NFR |
| [S4 — Regras formais com IA](../sessao-04-regras-formais-com-ia/index.md) | Como transformar uma regra espalhada entre prosa e código em um modelo verificável? | Regras em SBVR e RuleSpeak, tabelas de decisão com política de acerto explícita e a verificação por retrotradução |
| [S5 — Spec Kit: da regra ao código](../sessao-05-decomposicao/index.md) | O que precisa estar escrito antes que um agente transforme uma regra em código? | O caminho constitution, spec, plano e tarefas, com pontos de controle humano na implementação |
| [S6 — Qualidade da spec e teste antes do código](../sessao-06-spec-kit-aprofundado/index.md) | Como saber que um teste verde testou alguma coisa? | O uso de `clarify`, `checklist` e `analyze`, e o teste que falha antes da implementação pelo motivo certo |
| [S7 — Casos de uso de IA por papel](../sessao-07-casos-de-uso-por-papel/index.md) | Em quais tarefas do meu papel a IA já entrega um resultado que eu consigo conferir? | Os cinco elementos de um caso de uso, com a fonte de comparação usada na conferência |
| [S8 — Skills e agentes](../sessao-08-skills-e-agentes/index.md) | O que uma skill ou um agente precisa declarar antes de ser construído? | A ficha de requisitos com artefato, modelo, orçamento de tokens, tempo, permissões e credenciais |
| [S9 — Governança de skills e agentes](../sessao-09-governanca-de-skills-e-agentes/index.md) | O que precisa estar decidido antes que outra pessoa instale uma skill de um colega? | A ficha de governança, os controles aplicados fora do modelo e o ciclo de vida do plugin num marketplace |

## O fio que atravessa as sessões

As nove sessões repetem a mesma decisão em escalas diferentes: o que o agente pode decidir sozinho, com que contexto, e qual evidência mostra que o resultado está correto. Na Sessão 1 essa decisão aparece na escolha do modo de trabalho, na Sessão 3 ela aparece na especificação que impede o agente de decidir sozinho o que o pedido queria dizer, na Sessão 6 ela aparece no teste que falha pelo motivo certo, e na Sessão 9 ela aparece na faixa de risco que define se o agente sugere, prepara para aprovação ou executa.

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) descreve a evolução do mercado na mesma unidade. A tese central do relatório é que, em 2027, a mudança mais relevante será a capacidade de delegar trabalho a sistemas que mantêm contexto, usam ferramentas e concluem tarefas sob controles operacionais, e que a vantagem de uma empresa dependerá da integração entre capacidade do modelo, desenho do trabalho, dados, verificação e responsabilidade.

## Correspondência entre a prática e o horizonte de 2027

| Tema do curso | Onde foi praticado | Como o relatório trata o mesmo tema |
|---|---|---|
| Arnês e engenharia de contexto | S2 | O Gartner lista *AI context platforms* e *AI coding agent harness* entre as tendências estratégicas de 2027, e o relatório descreve a separação entre sessão, arnês e ambiente nos produtos de agentes persistentes |
| Erro composto | S2 | O relatório usa a mesma aritmética para mostrar que a confiabilidade de um passo difere da confiabilidade do processo |
| Princípio de simplicidade | S1 | A avaliação do Google Research com 180 configurações sustenta a recomendação de acrescentar agentes somente quando houver necessidade demonstrável |
| Especificação e critério de aceite | S3, S5 e S6 | Na engenharia por delegação, o trabalho humano se concentra em definir o problema, especificar o comportamento e revisar a mudança |
| Regras formais | S4 | Nos processos híbridos, a elegibilidade é verificada por regras explícitas, e o agente atua nos passos adaptativos |
| Conferência do resultado | S7 | A unidade econômica proposta é o resultado aceito pelo processo, e a atividade produzida pelo agente fica fora dessa conta |
| Ficha de requisitos e custo | S8 | A métrica recomendada é o custo total por resultado aceito, incluindo supervisão e correção |
| Credenciais e identidade do agente | S8 | Agentes operacionais passam a ter identidade, proprietário, escopo de acesso e ciclo de vida explícitos |
| Governança e marketplace | S9 | O Nubank relata a revisão de mais de 2.000 skills antes da distribuição, e a cadeia de suprimentos de skills aparece entre os modos de falha da arquitetura de referência |

A correspondência tem um limite que convém registrar: a equipe praticou essas decisões em ferramentas de engenharia de software e em casos fictícios, enquanto o relatório trata de processos empresariais inteiros. A transposição de uma escala para a outra é o assunto da segunda hora desta sessão, com a arquitetura de referência, a métrica de custo por resultado aceito e o plano de 90 dias.

**Próxima página:** [Da interação à delegação](da-interacao-a-delegacao.md).
