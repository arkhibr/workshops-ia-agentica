# O que cada sessão do curso produziu

As Sessões 1 a 9 do workshop trataram do uso de agentes de IA no trabalho de uma equipe de desenvolvimento, começando pelo uso individual e sem método e terminando no compartilhamento de skills e agentes com regras definidas pela equipe. Esta página lembra o que cada sessão produziu e relaciona esses resultados às mudanças que as páginas seguintes descrevem para 2027 a 2030, com cada termo explicado novamente para quem não participou de alguma sessão.

## Resultado de cada sessão

| Sessão | Pergunta que a sessão respondeu | O que a equipe passou a ter |
|---|---|---|
| [S1 — O que mudou](../sessao-01-o-que-mudou/index.md) | Por que a equipe já usa IA todo dia e o resultado continua desigual? | Modos de trabalho com IA para escolher conforme a tarefa: pedir código sem especificar (vibe coding), pedir ajuda pontual sobre código existente (assistência de codificação) e escrever a especificação antes de pedir o código (SDD, desenvolvimento guiado por especificação) |
| [S2 — O ambiente agêntico](../sessao-02-ambiente-agentico/index.md) | O que muda quando o time passa a compartilhar um ambiente? | Um arquivo de instrução comum, lido pelo agente no início de cada conversa, a conexão do agente a ferramentas externas pelo MCP (*Model Context Protocol*, protocolo padrão para essa conexão) e o hábito de isolar o trabalho de cada agente num ramo próprio do repositório |
| [S3 — Exploração e especificação](../sessao-03-exploracao-especificacao/index.md) | Por que um pedido tecnicamente correto ainda produz o sistema errado? | Especificações em que cada requisito é classificado como regra de negócio, requisito funcional (o que o sistema faz) ou requisito não funcional (como o sistema deve se comportar, por exemplo em desempenho) |
| [S4 — Regras formais com IA](../sessao-04-regras-formais-com-ia/index.md) | Como transformar uma regra espalhada entre prosa e código em um modelo verificável? | Regras de negócio escritas em frases padronizadas e em tabelas de decisão, que listam todas as combinações de condições e o resultado de cada uma |
| [S5 — Spec Kit: da regra ao código](../sessao-05-decomposicao/index.md) | O que precisa estar escrito antes que um agente transforme uma regra em código? | O uso do GitHub Spec Kit, ferramenta que conduz o agente por princípios do projeto, especificação, plano e lista de tarefas antes de escrever código |
| [S6 — Qualidade da spec e teste antes do código](../sessao-06-spec-kit-aprofundado/index.md) | Como saber que um teste verde testou alguma coisa? | O teste escrito antes do código, que precisa falhar enquanto o código não existe e passar depois que ele é escrito |
| [S7 — Casos de uso de IA por papel](../sessao-07-casos-de-uso-por-papel/index.md) | Em quais tarefas do meu papel a IA já entrega um resultado que eu consigo conferir? | Casos de uso de IA por papel, cada um com a fonte usada para conferir a resposta da IA |
| [S8 — Skills e agentes](../sessao-08-skills-e-agentes/index.md) | O que uma skill ou um agente precisa declarar antes de ser construído? | A ficha de requisitos, preenchida antes de construir uma skill (pacote de instruções reutilizável pelo agente) ou um agente, com modelo, custo estimado, permissões e credenciais |
| [S9 — Governança de skills e agentes](../sessao-09-governanca-de-skills-e-agentes/index.md) | O que precisa estar decidido antes que outra pessoa instale uma skill de um colega? | A ficha de governança, que registra responsável, riscos, controles e aprovação antes de compartilhar uma skill, e a publicação de skills num catálogo local da equipe |

## Decisão presente em todas as sessões

Todas as sessões tratam da mesma decisão de projeto, que é definir quanto o agente executa sem aprovação humana e que evidência a equipe exige antes de aceitar o resultado dele, como mostram os exemplos da tabela.

| Sessão | Como a decisão apareceu |
|---|---|
| S1 | Na escolha do modo de trabalho, que define quanto do comportamento do código fica escrito antes de o agente começar |
| S3 | Na especificação, que impede o agente de interpretar sozinho o que o pedido queria dizer |
| S6 | No teste escrito antes do código, que define quando o resultado do agente pode ser aceito |
| S9 | Na faixa de risco da ficha de governança, que define se o agente apenas sugere, prepara algo para uma pessoa aprovar ou executa sozinho |

As empresas que adotam agentes tomam essa mesma decisão para processos inteiros, como atendimento, conferência de documentos e pagamentos, e as páginas seguintes tratam das mudanças esperadas nessa escala.

## Relação entre o curso e as mudanças esperadas para 2027

| O que a equipe praticou | Sessão | Mudança esperada no mercado |
|---|---|---|
| Arnês, nome dado no curso a tudo o que cerca o modelo de IA dentro de um agente (instruções, ferramentas, memória e regras de execução) | S2 | A consultoria Gartner incluiu entre as tendências de 2027 plataformas para fornecer contexto aos agentes e para controlar a execução de agentes de programação |
| Cálculo do erro acumulado: quando um agente executa vários passos em sequência, a chance de todos darem certo é o produto das chances de cada passo, e por isso cai depressa com o número de passos | S2 | A confiabilidade de um processo com agentes passa a ser medida no processo inteiro, porque 99% de acerto por passo resultam em cerca de 82% de acerto em vinte passos |
| Começar pela solução mais simples e só acrescentar agentes quando necessário | S1 | Uma avaliação do Google Research com 180 configurações mostrou que vários agentes cooperando pioram o resultado em tarefas sequenciais |
| Especificação e critério de aceite escritos antes do código | S3, S5 e S6 | Com agentes que escrevem e alteram código, o trabalho das pessoas se concentra em definir o problema, especificar o comportamento e revisar a mudança |
| Regras de negócio em tabelas de decisão | S4 | Processos que combinam agentes e regras fixas usam regras explícitas nas etapas em que a resposta precisa ser sempre a mesma |
| Conferência da resposta da IA contra uma fonte | S7 | O resultado de um agente passa a ser medido pelas entregas que o processo aceitou como corretas |
| Ficha de requisitos com custo e credenciais | S8 | Agentes em operação passam a ter identidade própria nos sistemas da empresa, com responsável e permissões definidas |
| Ficha de governança e catálogo local de skills | S9 | O banco Nubank relata a revisão de mais de 2.000 skills antes de liberá-las para os seus times |

A equipe praticou essas decisões em ferramentas de desenvolvimento de software e em casos fictícios, enquanto as empresas citadas aplicam agentes a processos de negócio completos. A segunda hora desta sessão trata da aplicação a processos de negócio, com os componentes de um agente que age com controle, a medição de custo e resultado e o plano de 90 dias.

**Próxima página:** [Formas de delegar trabalho à IA](formas-de-delegar-trabalho.md).
