# Arquitetura de referência

Um agente que continua trabalhando depois da conversa precisa de uma arquitetura que preserve o estado do trabalho, restrinja as ações e produza evidência de resultado. Esta página apresenta a arquitetura de referência proposta no relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026), que não corresponde a um produto específico, e a forma como os fornecedores distribuem as mesmas responsabilidades entre seus componentes.

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

A observabilidade dessa arquitetura se apoia em evidências operacionais, como ações executadas, resultados de ferramentas e mudanças de estado, e dispensa acesso à cadeia de raciocínio interna do modelo. O *gateway* é o mesmo controle aplicado fora do modelo que a [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/controles-e-evidencias.md) distinguiu da instrução textual: a política que ele aplica vale independentemente da resposta do modelo.

## Sessão, arnês e ambiente nos produtos atuais

Os fornecedores de agentes persistentes convergem em quatro responsabilidades: registrar o trabalho, conduzir a execução, oferecer um ambiente de ferramentas e controlar ações. O infográfico usa o termo *harness* do original em inglês, que este curso traduz como arnês desde a [Sessão 2](../sessao-02-ambiente-agentico/arnes.md).

![Três colunas com responsabilidades e ciclos de vida diferentes. Sessão ou estado reúne histórico de eventos, checkpoint e artefatos e espera persistente, e preserva o trabalho registrado. Harness, que este curso chama de arnês, monta o contexto, chama modelo e ferramentas e observa e continua, conduzindo a execução e aplicando limites. Ambiente reúne código e processos, navegador, arquivos e APIs, e rede e recursos limitados, oferecendo as ferramentas de trabalho. Abaixo, Claude Managed Agents separa sessão, harness e sandbox com contêiner novo por sessão no ambiente gerenciado, Grok Bot usa um computador por usuário compartilhado pelos bots, com telas que não isolam segurança, e LangChain com Temporal oferece execução durável e espera humana. A faixa final cita microVM por sessão na AWS, runtime, sessões e memória no Google e checkpoints na Microsoft.](assets/sessao-arnes-e-ambiente.png)

| Fornecedor | Como distribui as responsabilidades |
|---|---|
| Anthropic | No [Claude Managed Agents](../referencia/bibliografia.md#anthropic-scaling-managed-agents-2026), a sessão é um registro de eventos, o arnês conduz as chamadas ao modelo e encaminha ferramentas, e o *sandbox* executa código e manipula arquivos, com interfaces que permitem trocar cada componente |
| xAI | No [Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao), cada membro recebe um computador hospedado em que todos os seus bots trabalham, com arquivos e sessões de navegador compartilhados |
| LangChain | A infraestrutura de Deep Agents separa a lógica que orienta o modelo da camada que mantém *checkpoints*, memória, concorrência e observabilidade |
| Temporal | O [fluxo de trabalho durável](../referencia/bibliografia.md#temporal-durable-ai-documentacao) mantém coordenação e histórico, chamadas de modelo e ferramentas rodam como *Activities*, e uma decisão humana chega por *Signal* ou *Update* |
| AWS | O AgentCore oferece uma microVM por sessão nesse modo de execução, com contexto efêmero e armazenamento de sessão para arquivos que sobrevivem a paradas |
| Google e Microsoft | A Gemini Enterprise Agent Platform separa runtime, sessões e banco de memória, e o Microsoft Agent Framework salva o estado em *checkpoints* e pausa ferramentas que exigem aprovação |

Três propriedades parecidas precisam ser distinguidas ao avaliar um produto: persistir uma conversa, preservar arquivos e recuperar uma execução interrompida. No Grok Bot, por exemplo, a recriação controlada do computador preserva o disco, o que recupera arquivos e logins sem garantir que um processo em andamento retome do ponto anterior. Nome, prompt ou tela próprios não constituem isolamento técnico, e responsabilidades que exigem fronteira entre dados ou privilégios precisam de uma implantação que imponha essa separação.

## O exemplo da fatura com aprovação

No cenário ilustrativo do relatório, um agente recebe uma divergência de faturamento, consulta contrato e pedido, produz uma proposta de correção e aguarda aprovação. O histórico registra evidências, decisões e resultados das ferramentas, o arnês decide a próxima consulta ou verificação, o ambiente oferece navegador, arquivos e APIs, o fluxo de trabalho durável registra a decisão pendente e retoma quando ela chega, e a ferramenta de negócio verifica a permissão e usa uma chave idempotente antes de registrar a correção.

Três falhas mostram por que cada componente é necessário. Se o ambiente de ferramentas falhar, os recursos precisam ser restaurados e os dados pertinentes recuperados. Se a aprovação levar dois dias, o estado pendente precisa sobreviver à espera. Se a resposta da API se perder depois de uma correção bem-sucedida, a retomada precisa consultar o resultado ou reutilizar a chave da operação, e uma máquina virtual persistente, sozinha, não resolve nenhuma das três situações.

## Modos de falha a tornar visíveis

| Modo de falha | Exemplo | Resposta de engenharia |
|---|---|---|
| Instrução maliciosa em conteúdo externo | Um documento tenta induzir o envio de dados | Separar conteúdo de instrução e restringir capacidades |
| Privilégio excessivo | Um agente de consulta também consegue apagar registros | Menor privilégio e ferramentas específicas |
| Duplicação após nova tentativa | Repetição de uma operação já concluída | Chaves idempotentes e reconciliação |
| Memória incorreta | Uma regra antiga é recuperada como vigente | Origem, versionamento e validade de cada memória |
| Cadeia de suprimentos comprometida | Uma skill introduz comandos indevidos | Revisão, testes, distribuição controlada e revogação |
| Critério de sucesso inadequado | Maximizar tickets fechados piora a resolução real | Resultado de negócio com a reabertura como contramétrica |

A seleção se apoia no caso do Nubank, no [OWASP Top 10 para aplicações agênticas](../referencia/bibliografia.md#owasp-top-10-for-agentic-applications-2026) e na [iniciativa de padrões para agentes do NIST](../referencia/bibliografia.md#nist-ai-agent-standards-initiative-2026), lançada em fevereiro de 2026, que não equivale a uma certificação de agentes. Os dois primeiros modos de falha correspondem à instrução escondida no documento e à permissão maior que a finalidade, dois dos três incidentes estudados em [Riscos de agentes](../sessao-09-governanca-de-skills-e-agentes/riscos-de-agentes.md), na Sessão 9.

A unidade de engenharia passa a incluir uma execução identificável, com estado, permissões, orçamento e evidência de conclusão. O desenho dessa execução responde a cinco perguntas: o que sobrevive à falha do ambiente, onde ficam arquivos e credenciais, como uma pessoa intervém, quais ações podem ser repetidas e como interromper ou revogar a delegação.

**Próxima página:** [Métricas e economia](metricas-e-economia.md).
