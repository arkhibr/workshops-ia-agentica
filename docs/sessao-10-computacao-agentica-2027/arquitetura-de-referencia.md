# Arquitetura de referência

Esta página apresenta a arquitetura de referência proposta no relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) para agentes que continuam executando depois que o usuário encerra a conversa. A arquitetura não corresponde a um produto específico, e a segunda seção mostra como seis fornecedores distribuem as mesmas responsabilidades entre os componentes dos seus produtos.

## Responsabilidades da arquitetura

![Arquitetura ilustrativa para reconciliar uma fatura e registrar uma correção aprovada. No topo, o contrato da execução reúne identidade e escopo, identificador da execução com objetivo e critério de aceite, e orçamento com cancelamento. Na linha principal, o contexto com contrato, pedido e fatura, verificados quanto a origem, acesso e validade, alimenta o fluxo de trabalho com o arnês, em que o modelo escolhe passos com estado e limites explícitos. Em seguida, o gateway valida esquema e autorização com política fora do prompt, e os sistemas de registro permitem consultar e corrigir, mantendo o estado oficial e o comprovante. Abaixo, o estado persistente guarda eventos, checkpoints e artefatos, a pessoa responsável trata exceções, aprovação e devolução, e a avaliação e observabilidade registram ações, custo e evidência de aceite.](assets/arquitetura-de-referencia.png)

| Componente | Responsabilidade |
|---|---|
| Fluxo de trabalho | Mantém o estado da execução e pode esperar por uma decisão |
| Agente | Escolhe ações dentro do conjunto de capacidades exposto a ele |
| *Gateway* | Valida permissões e condições antes de cada ação |
| Sistema de registro | Mantém o estado oficial do negócio |
| Pessoa responsável | Trata exceções e decisões que excedem a delegação |
| Observabilidade | Registra ações, resultados e mudanças de estado |

A observabilidade registra as ações executadas, os resultados das ferramentas e as mudanças de estado, sem precisar de acesso ao raciocínio interno do modelo. O *gateway* corresponde ao controle aplicado fora do modelo da [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/controles-e-evidencias.md), cuja política vale independentemente da resposta do modelo.

## Sessão, arnês e ambiente nos produtos atuais

Os produtos de agentes persistentes analisados no relatório separam quatro responsabilidades, que são registrar o trabalho, conduzir a execução, oferecer o ambiente de ferramentas e controlar as ações. O infográfico usa o termo *harness* do original em inglês, que este curso traduz como arnês desde a [Sessão 2](../sessao-02-ambiente-agentico/arnes.md).

![Três colunas com responsabilidades e ciclos de vida diferentes. Sessão ou estado reúne histórico de eventos, checkpoint e artefatos e espera persistente, e preserva o trabalho registrado. Harness, que este curso chama de arnês, monta o contexto, chama modelo e ferramentas e observa e continua, conduzindo a execução e aplicando limites. Ambiente reúne código e processos, navegador, arquivos e APIs, e rede e recursos limitados, oferecendo as ferramentas de trabalho. Abaixo, Claude Managed Agents separa sessão, harness e sandbox com contêiner novo por sessão no ambiente gerenciado, Grok Bot usa um computador por usuário compartilhado pelos bots, com telas que não isolam segurança, e LangChain com Temporal oferece execução durável e espera humana. A faixa final cita microVM por sessão na AWS, runtime, sessões e memória no Google e checkpoints na Microsoft.](assets/sessao-arnes-e-ambiente.png)

| Fornecedor | Como distribui as responsabilidades |
|---|---|
| Anthropic | No [Claude Managed Agents](../referencia/bibliografia.md#anthropic-scaling-managed-agents-2026), a sessão é um registro de eventos, o arnês conduz as chamadas ao modelo e encaminha ferramentas, e o *sandbox* executa código e manipula arquivos, com interfaces que permitem trocar cada componente |
| xAI | No [Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao), cada membro recebe um computador hospedado em que todos os seus bots trabalham, com arquivos e sessões de navegador compartilhados |
| LangChain | A infraestrutura de Deep Agents separa a lógica que orienta o modelo da camada que mantém *checkpoints*, memória, concorrência e observabilidade |
| Temporal | O [fluxo de trabalho durável](../referencia/bibliografia.md#temporal-durable-ai-documentacao) mantém coordenação e histórico, chamadas de modelo e ferramentas rodam como *Activities*, e uma decisão humana chega por *Signal* ou *Update* |
| AWS | O AgentCore oferece uma microVM por sessão nesse modo de execução, com contexto efêmero e armazenamento de sessão para arquivos que permanecem disponíveis depois de uma parada |
| Google e Microsoft | A Gemini Enterprise Agent Platform separa runtime, sessões e banco de memória, e o Microsoft Agent Framework salva o estado em *checkpoints* e pausa ferramentas que exigem aprovação |

Na avaliação de um produto, persistir a conversa, preservar os arquivos e recuperar uma execução interrompida são propriedades diferentes, que precisam ser verificadas uma a uma. No Grok Bot, a recriação controlada do computador preserva o disco e recupera arquivos e logins, sem garantia de que um processo em andamento continue do ponto em que parou. Um nome, um prompt ou uma tela próprios não isolam dados nem privilégios, e esse isolamento exige uma implantação que separe os ambientes.

## O exemplo da fatura com aprovação

No cenário do relatório, um agente recebe uma divergência de faturamento, consulta o contrato e o pedido, prepara uma proposta de correção e aguarda aprovação, com os componentes da arquitetura nos papéis da tabela.

| Componente | Papel no cenário da fatura |
|---|---|
| Histórico da sessão | Registra evidências, decisões e resultados das ferramentas |
| Arnês | Decide a próxima consulta ou verificação |
| Ambiente | Oferece navegador, arquivos e APIs |
| Fluxo de trabalho durável | Registra a decisão pendente e continua a execução quando a aprovação chega |
| Ferramenta de negócio | Verifica a permissão e usa uma chave idempotente antes de registrar a correção |

O relatório descreve três falhas desse cenário. Se o ambiente de ferramentas falhar, os recursos precisam ser restaurados e os dados recuperados. Se a aprovação levar dois dias, o estado pendente precisa ficar gravado durante esse período. Se a resposta da API se perder depois de uma correção bem-sucedida, a retomada precisa consultar o resultado ou reutilizar a chave da operação para não registrar a correção duas vezes. O relatório observa que manter uma máquina virtual persistente não resolve nenhuma das três falhas, porque nenhuma delas depende apenas da preservação do ambiente.

## Modos de falha

| Modo de falha | Exemplo | Resposta de engenharia |
|---|---|---|
| Instrução maliciosa em conteúdo externo | Um documento tenta induzir o envio de dados | Separar conteúdo de instrução e restringir capacidades |
| Privilégio excessivo | Um agente de consulta também consegue apagar registros | Menor privilégio e ferramentas específicas |
| Duplicação após nova tentativa | Repetição de uma operação já concluída | Chaves idempotentes e reconciliação |
| Memória incorreta | Uma regra antiga é recuperada como vigente | Origem, versionamento e validade de cada memória |
| Cadeia de suprimentos comprometida | Uma skill introduz comandos indevidos | Revisão, testes, distribuição controlada e revogação |
| Critério de sucesso inadequado | Maximizar tickets fechados piora a resolução real | Resultado de negócio com a reabertura como contramétrica |

A tabela foi montada a partir do caso do Nubank, do [OWASP Top 10 para aplicações agênticas](../referencia/bibliografia.md#owasp-top-10-for-agentic-applications-2026) e da [iniciativa de padrões para agentes do NIST](../referencia/bibliografia.md#nist-ai-agent-standards-initiative-2026), lançada em fevereiro de 2026 e sem valor de certificação de agentes. Os dois primeiros modos de falha correspondem à instrução escondida no documento e à permissão maior que a finalidade, dois dos três incidentes estudados em [Riscos de agentes](../sessao-09-governanca-de-skills-e-agentes/riscos-de-agentes.md), na Sessão 9.

Segundo o relatório, cada execução de agente passa a ter identificador, estado, permissões, orçamento e evidência de conclusão próprios, e o desenho dela responde às perguntas abaixo.

- Que dados permanecem disponíveis depois de uma falha do ambiente?
- Onde ficam os arquivos e as credenciais?
- Em que ponto e de que forma uma pessoa intervém?
- Quais ações podem ser repetidas sem efeito duplicado?
- Como a delegação é interrompida ou revogada?

**Próxima página:** [Métricas e economia](metricas-e-economia.md).
