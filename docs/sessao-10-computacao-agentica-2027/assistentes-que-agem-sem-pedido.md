# Assistentes que agem sem receber pedido

Um assistente proativo é um agente de IA que acompanha, com permissão do usuário, fontes como agenda, e-mail e documentos, guarda o histórico entre conversas e toma a iniciativa de avisar ou agir, por exemplo ao perceber um conflito de agenda ou ao preparar a pauta de uma reunião antes de alguém pedir. A diferença em relação a um assistente comum é o que o usuário entrega: no assistente comum ele faz um pedido de cada vez, e no proativo ele entrega uma responsabilidade contínua, como acompanhar as pendências de um projeto. Quatro fornecedores lançaram produtos desse tipo entre setembro e outubro de 2026, e ainda não há medição independente do ganho obtido por quem os usa.

## Quatro produtos lançados em 2026

| Produto | Lançamento | O que o fornecedor descreve | Limite informado |
|---|---|---|---|
| [Claude Duet](../referencia/bibliografia.md#anthropic-introducing-claude-duet-2026), da Anthropic | 21/10/2026, versão de teste com lista de espera nos Estados Unidos | Acompanha os aplicativos conectados pelo usuário e trabalha num computador virtual próprio, com exemplos como o aviso sobre uma visita a imóvel marcada na data errada | A Anthropic informa que a versão inicial pode entender conversas de forma errada e avaliar mal a urgência de um assunto, e que consulta as contas do usuário de tempos em tempos para não esgotar o limite de uso do plano |
| [Grok Bot](../referencia/bibliografia.md#xai-grok-bot-documentacao), da xAI | Documentação consultada em 10/11/2026 | Agente com computador na nuvem que executa rotinas, como ler a agenda no domingo e preparar o planejamento da semana | Todos os bots de um mesmo usuário trabalham no mesmo computador, sem separação de segurança entre eles, e o uso tem limite e cobrança adicional |
| [dots](../referencia/bibliografia.md#openai-introducing-dots-2026), da OpenAI | 29/09/2026 | Cada dot tem computador na nuvem, e o anúncio relata um dot que notou uma cobrança esquecida, preparou a fatura e a enviou depois da aprovação do usuário | Quando age por iniciativa própria, o dot só pode ler informações, e qualquer ação que altere um sistema passa por regras e revisão |
| [Muse](../referencia/bibliografia.md#meta-introducing-muse-2026), da Meta | 08/09/2026, lançamento inicial nos Estados Unidos | Aplicativo próprio com acesso também pelo WhatsApp, com computador na nuvem e um componente separado, chamado Sentinel, que controla as ações que acessam a internet | A agência [Reuters noticiou](../referencia/bibliografia.md#reuters-muse-e-o-concierge-humano-2026) em setembro de 2026 um teste em que pessoas contratadas faziam parte das ligações atribuídas ao Muse, e a Meta suspendeu esse recurso temporariamente |

Os exemplos de uso da tabela foram escolhidos e divulgados pelos próprios fornecedores.

![Arquitetura conceitual de uma responsabilidade acompanhada entre conversas, no exemplo de acompanhar uma conta, reunir pendências e preparar a próxima reunião. Sinais autorizados de agenda, e-mail e documentos alimentam uma rotina com contexto que agenda, recupera e decide, apoiada em histórico, permissões e consumo. A rotina produz briefing e rascunhos, com ações sensíveis sob revisão, que a pessoa aceita, corrige ou autoriza. Quatro cartões citam Claude Duet com conflito de agenda, Grok Bot com rotina entre aplicativos, OpenAI dots com cobrança esquecida e Meta Muse com compras e planejamento. A faixa inferior recomenda medir entregas aceitas, alertas descartados, revisão e custo total.](assets/responsabilidade-entre-conversas.png)

## Motivos para esperar que esses assistentes se espalhem

Tarefas de coordenação, como preparar compromissos, reunir informações espalhadas em vários sistemas e acompanhar pendências, se repetem várias vezes por semana, e um ganho pequeno em cada repetição pode somar um ganho relevante no mês, o que ainda precisa ser medido. Além disso, entregar uma responsabilidade contínua dispensa a pessoa de lembrar de pedir cada tarefa. O lançamento de quatro produtos parecidos em dois meses mostra que os fornecedores apostam na categoria, sem indicar quantas empresas vão adotá-la.

## Motivos para desconfiar

| Objeção | Explicação |
|---|---|
| O assistente pode criar trabalho | Um assistente que avisa demais, entende mal as prioridades ou erra nas entregas obriga o usuário a revisar tudo o que ele produz, e o ganho real é o tempo poupado menos o tempo gasto lendo avisos e corrigindo entregas |
| Pode haver pessoas por trás da automação | O caso do Muse mostra que parte do trabalho atribuído a um agente pode ser feita por pessoas, o que muda o custo e expõe dados do usuário a terceiros |
| O custo pode impedir o uso diário | Limites de uso por plano e cobrança por rotina executada podem tornar o uso diário caro demais para a equipe |
| Produtividade individual não acelera o processo | Se várias pessoas preparam propostas mais depressa e a aprovação continua dependendo de uma única pessoa, a fila de aprovação cresce, e só a medição do processo inteiro mostra o efeito real |
| As ferramentas atuais podem absorver a função | Agenda, e-mail e sistemas de gestão de clientes podem incorporar avisos proativos, e o assistente separado perde utilidade |

A objeção sobre o processo usa medidas que voltam nas páginas seguintes: *lead time*, que é o tempo total entre o pedido e a entrega, *throughput*, que é a quantidade de entregas concluídas por período, e trabalho em andamento, que é a quantidade de itens iniciados e ainda não concluídos.

## Como testar um assistente proativo antes de adotá-lo

![Três faixas em sequência. Oferta observável reúne produtos e capacidades, com Duet, Grok Bot, dots e Muse. Piloto acompanhado dura oito a doze semanas e registra aceites, alertas, falhas e supervisão. Prática sustentável exige comparação com a linha de base, com ganho recorrente, controle e orçamento. Um quadro de alerta lista as hipóteses concorrentes: uso de nicho, abandono, incorporação às suítes e automação simples equivalente.](assets/oferta-e-pratica-sustentavel.png)

Um teste útil acompanha uma única responsabilidade, por exemplo preparar as pautas de reunião de um projeto, durante oito a doze semanas. Antes de começar, a equipe mede como a tarefa é feita sem o assistente, o que se chama linha de base, e define o resultado que justificaria continuar, e durante as semanas de teste registra os cinco itens da lista.

- Entregas do assistente aceitas sem correção.
- Falhas do assistente.
- Avisos descartados pelo usuário por serem desnecessários.
- Minutos gastos revisando o trabalho do assistente.
- Gasto total com o produto.

O teste indica que o assistente não compensa se o uso cair depois das primeiras semanas, se o tempo de revisão igualar ou superar o tempo poupado, se o limite de uso impedir a rotina, se houver falhas repetidas de permissão ou se uma automação simples, como uma regra de e-mail, produzir o mesmo resultado com menor custo. O prazo de oito a doze semanas é uma sugestão prática, sem base em estudo científico.

**Próxima página:** [Resultados publicados por empresas](resultados-publicados-por-empresas.md).
