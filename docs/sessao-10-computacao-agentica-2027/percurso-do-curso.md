# O percurso do curso

As Sessões 1 a 9 do workshop trataram do uso de agentes de IA no trabalho de uma equipe de desenvolvimento, começando pelo uso individual sem método e terminando no compartilhamento governado de skills e agentes. Esta página lista a pergunta-guia de cada sessão e o artefato que ela deixou registrado, para que as páginas seguintes, sobre computação agêntica em 2027, possam se referir a esses artefatos pelo nome.

## Pergunta-guia e artefato de cada sessão

| Sessão | Pergunta-guia | Artefato ou decisão registrada |
|---|---|---|
| [S1 — O que mudou](../sessao-01-o-que-mudou/index.md) | Por que a equipe já usa IA todo dia e o resultado continua desigual? | Distinção entre vibe coding, assistência de codificação e SDD pelo artefato que governa a qualidade |
| [S2 — O ambiente agêntico](../sessao-02-ambiente-agentico/index.md) | O que muda quando o time passa a compartilhar um ambiente? | Arquivo de instrução comum, configuração de MCP e isolamento do trabalho por ramo |
| [S3 — Exploração e especificação](../sessao-03-exploracao-especificacao/index.md) | Por que um pedido tecnicamente correto ainda produz o sistema errado? | Especificação com requisitos classificados como BR, FR ou NFR |
| [S4 — Regras formais com IA](../sessao-04-regras-formais-com-ia/index.md) | Como transformar uma regra espalhada entre prosa e código em um modelo verificável? | Regras em RuleSpeak e tabelas de decisão com política de acerto explícita |
| [S5 — Spec Kit: da regra ao código](../sessao-05-decomposicao/index.md) | O que precisa estar escrito antes que um agente transforme uma regra em código? | Constitution, spec, plano e tarefas do GitHub Spec Kit |
| [S6 — Qualidade da spec e teste antes do código](../sessao-06-spec-kit-aprofundado/index.md) | Como saber que um teste verde testou alguma coisa? | Teste escrito antes da implementação e falhando pelo motivo esperado |
| [S7 — Casos de uso de IA por papel](../sessao-07-casos-de-uso-por-papel/index.md) | Em quais tarefas do meu papel a IA já entrega um resultado que eu consigo conferir? | Caso de uso com a fonte de comparação usada na conferência |
| [S8 — Skills e agentes](../sessao-08-skills-e-agentes/index.md) | O que uma skill ou um agente precisa declarar antes de ser construído? | Ficha de requisitos da skill ou do agente |
| [S9 — Governança de skills e agentes](../sessao-09-governanca-de-skills-e-agentes/index.md) | O que precisa estar decidido antes que outra pessoa instale uma skill de um colega? | Ficha de governança e plugin publicado num marketplace local |

## Decisão comum às nove sessões

Todas as sessões tratam da mesma decisão de projeto, que é definir quanto o agente executa sem aprovação humana e que evidência a equipe exige antes de aceitar o resultado dele, como mostram os quatro exemplos da tabela.

| Sessão | Onde a decisão foi tomada |
|---|---|
| S1 | Na escolha do modo de trabalho para cada tarefa |
| S3 | Na especificação que impede o agente de interpretar sozinho o pedido |
| S6 | No teste que precisa falhar antes da implementação |
| S9 | Na faixa de risco que define se o agente sugere, prepara para aprovação ou executa |

O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) trata da mesma decisão em escala de empresa. Segundo o relatório, a mudança mais relevante de 2027 será a delegação de trabalho a sistemas que executam tarefas sob controles operacionais, e o resultado de cada empresa dependerá de como ela integra modelo, processo, dados, verificação e responsabilidade.

## Correspondência entre o curso e o relatório

| Tema do curso | Sessão | Tratamento no relatório |
|---|---|---|
| Arnês e engenharia de contexto | S2 | O Gartner inclui *AI context platforms* e *AI coding agent harness* entre as tendências estratégicas de 2027 |
| Erro composto | S2 | O relatório usa o mesmo cálculo para mostrar que a confiabilidade de um passo difere da confiabilidade do processo |
| Princípio de simplicidade | S1 | O Google Research avaliou 180 configurações e recomenda acrescentar agentes somente quando houver necessidade demonstrada |
| Especificação e critério de aceite | S3, S5 e S6 | Na engenharia por delegação, a pessoa define o problema, especifica o comportamento e revisa a mudança |
| Regras formais | S4 | Nos processos híbridos, regras explícitas verificam a elegibilidade e o agente atua nos passos não determinísticos |
| Conferência do resultado | S7 | A unidade de medida proposta é o resultado aceito pelo processo |
| Ficha de requisitos e custo | S8 | A métrica proposta é o custo total por resultado aceito, com supervisão e correção incluídas |
| Credenciais e identidade do agente | S8 | Agentes em operação passam a ter identidade, proprietário, escopo de acesso e ciclo de vida próprios |
| Governança e marketplace | S9 | O Nubank relata a revisão de mais de 2.000 skills antes da distribuição interna |

A equipe praticou essas decisões em ferramentas de engenharia de software e em casos fictícios, enquanto o relatório trata de processos de negócio completos. A segunda hora desta sessão trata da aplicação a processos de negócio, com a arquitetura de referência, a métrica de custo por resultado aceito e o plano de 90 dias.

**Próxima página:** [Da interação à delegação](da-interacao-a-delegacao.md).
