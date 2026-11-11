# Assistentes pessoais proativos

Um assistente pessoal proativo mantém contexto entre conversas, acompanha fontes de informação autorizadas pelo usuário e executa tarefas em vários aplicativos sem esperar um novo pedido, por exemplo ao avisar sobre um conflito de agenda ou ao preparar a pauta de uma reunião. O relatório [Computação agêntica para 2027 e além](../referencia/bibliografia.md#arkhi-computacao-agentica-para-2027-e-alem-2026) classifica a categoria como tendência prática forte para 2027 e registra que o lançamento de produtos está mais documentado do que o ganho econômico obtido por quem os usa.

## Quatro produtos lançados entre setembro e outubro de 2026

| Produto | Anúncio | Descrição do fornecedor | Limite registrado |
|---|---|---|---|
| [Claude Duet](../referencia/bibliografia.md#anthropic-introducing-claude-duet-2026), Anthropic | 21/10/2026, prévia com lista de espera nos Estados Unidos | Acompanha aplicativos conectados e trabalha numa máquina virtual própria, com exemplos como o alerta sobre uma visita a imóvel registrada na data errada | A Anthropic informa que a versão inicial pode interpretar conversas de forma incorreta e avaliar mal a urgência, e que as contas são verificadas periodicamente para não esgotar os limites do plano |
| [Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao), xAI | Documentação consultada em 10/11/2026 | Agente com computador na nuvem e rotinas como ler a agenda no domingo para preparar o planejamento da semana | Os bots de um usuário compartilham o mesmo computador, as telas de cada bot não isolam segurança, e a documentação prevê limites de uso e cobrança de consumo adicional |
| [dots](../referencia/bibliografia.md#openai-introducing-dots-2026), OpenAI | 29/09/2026 | Cada dot tem computador na nuvem, e o anúncio relata um dot que identificou uma cobrança esquecida, preparou a fatura e a enviou depois da aprovação do usuário | A pesquisa proativa em segundo plano usa apenas ferramentas de leitura, e as ações que alteram sistemas passam por regras e revisão |
| [Muse](../referencia/bibliografia.md#meta-introducing-muse-2026), Meta | 08/09/2026, distribuição inicial nos Estados Unidos | Aplicativo próprio com entrada pelo WhatsApp e computador dedicado na nuvem, com um componente separado, o Sentinel, que controla as ações com acesso à internet | A [Reuters noticiou](../referencia/bibliografia.md#reuters-muse-e-o-concierge-humano-2026) em setembro de 2026 um teste em que prestadores humanos faziam parte das chamadas atribuídas ao Muse, e a Meta suspendeu o recurso temporariamente |

Os exemplos de uso da tabela foram divulgados pelos próprios fornecedores, sem medição independente de produtividade.

![Arquitetura conceitual de uma responsabilidade acompanhada entre conversas, no exemplo de acompanhar uma conta, reunir pendências e preparar a próxima reunião. Sinais autorizados de agenda, e-mail e documentos alimentam uma rotina com contexto que agenda, recupera e decide, apoiada em histórico, permissões e consumo. A rotina produz briefing e rascunhos, com ações sensíveis sob revisão, que a pessoa aceita, corrige ou autoriza. Quatro cartões citam Claude Duet com conflito de agenda, Grok Bot com rotina entre aplicativos, OpenAI dots com cobrança esquecida e Meta Muse com compras e planejamento. A faixa inferior recomenda medir entregas aceitas, alertas descartados, revisão e custo total.](assets/responsabilidade-entre-conversas.png)

## Argumentos a favor da tendência

O primeiro argumento do relatório é a frequência das tarefas de coordenação, como preparar compromissos e acompanhar pendências, que se repetem várias vezes por semana e podem gerar ganho acumulado mesmo sem mudança no processo, hipótese que ainda depende de medição. O segundo é a mudança no que se delega, porque uma tarefa isolada depende de a pessoa lembrar de pedir e uma responsabilidade contínua transfere parte do acompanhamento ao assistente. O lançamento de quatro produtos semelhantes em dois meses mostra que a categoria existe, sem indicar quanto ela será adotada.

## Objeções à tendência

| Objeção | Descrição |
|---|---|
| Trabalho adicional | Um assistente que gera alertas em excesso, interpreta mal prioridades ou exige correções cria uma fila de revisão para o usuário, e a medida útil passa a ser o tempo líquido poupado, descontados a leitura dos alertas e as correções |
| Trabalho humano oculto | O caso do Muse exige registrar separadamente a execução por software, a operação assistida e a intervenção humana, porque cada uma tem custo e implicação de privacidade próprios |
| Custo e disponibilidade | Limites de execução, consumo por rotina e elegibilidade por plano podem impedir o uso diário dentro do orçamento da equipe |
| Capacidade do serviço | Se várias pessoas preparam propostas mais depressa e a aprovação continua concentrada numa só pessoa, a fila de aprovação cresce, e o efeito só aparece nas medidas do fluxo completo, como *lead time*, *throughput* aceito, trabalho em andamento e retrabalho |
| Incorporação às suítes | Agenda, e-mail, CRM e suítes de escritório podem incorporar a função, reduzindo o espaço para um assistente vendido separadamente |

## Teste da hipótese em piloto

![Três faixas em sequência. Oferta observável reúne produtos e capacidades, com Duet, Grok Bot, dots e Muse. Piloto acompanhado dura oito a doze semanas e registra aceites, alertas, falhas e supervisão. Prática sustentável exige comparação com a linha de base, com ganho recorrente, controle e orçamento. Um quadro de alerta lista as hipóteses concorrentes: uso de nicho, abandono, incorporação às suítes e automação simples equivalente.](assets/oferta-e-pratica-sustentavel.png)

O relatório propõe acompanhar a mesma responsabilidade por oito a doze semanas, com linha de base medida antes, critérios de passagem definidos antes do início e os cinco registros da lista abaixo.

- Entregas aceitas.
- Falhas.
- Alertas descartados pelo usuário.
- Minutos de supervisão.
- Gasto total.

O relatório considera a hipótese enfraquecida se o uso cair de forma persistente depois das primeiras semanas, se o tempo de revisão igualar ou superar o tempo poupado, se os limites de consumo impedirem a rotina, se houver falhas recorrentes de permissão ou se uma automação mais simples e mais barata produzir o mesmo resultado. O prazo de oito a doze semanas é uma proposta do relatório, sem base em limiar científico.

**Próxima página:** [Casos reais](casos-reais.md).
