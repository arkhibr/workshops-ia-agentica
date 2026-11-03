# Governança de IA

Esta página define o que se entende por governança de IA nesta sessão, separa a governança de quatro atividades com que ela costuma ser confundida e apresenta as quatro decisões que precisam estar tomadas antes do compartilhamento de uma skill ou de um agente. A página preenche, na [ficha de governança](index.md#a-ficha-de-governanca), as linhas "Dono e finalidade" e "Autonomia". A ficha de governança é a tabela de oito linhas que esta sessão usa para registrar o que precisa estar decidido antes de outra pessoa da equipe instalar uma skill ou um agente.

## Definição operacional

O guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026) define governança de IA como o conjunto de responsabilidades, políticas, decisões, controles e mecanismos de supervisão que orientam quais sistemas podem ser criados ou usados, com quais dados, com quais poderes, dentro de quais limites e com qual prestação de contas. A finalidade declarada pelo guia é permitir o benefício com o risco tratado de forma proporcional ao dano possível, e a definição exclui duas leituras comuns, a de que governar se resume a revisar prompts e a de que governar se resume a comprar uma ferramenta de monitoramento.

A definição tem consequência prática para uma equipe de desenvolvimento. Cada termo da lista corresponde a um registro que alguém consegue apontar: a responsabilidade aparece como um nome, a política como um texto aprovado, a decisão como uma linha da ficha, o controle como um mecanismo que roda e a supervisão como uma pessoa com autoridade para interromper. Quando um desses registros não existe, a governança daquele caso está incompleta naquele ponto, e a ficha de governança desta sessão tem uma linha para cada registro.

## Cinco distinções

A primeira confusão a evitar é tratar governança, gestão de riscos, segurança, qualidade e operação como a mesma atividade. As cinco respondem a perguntas diferentes e deixam evidências diferentes, conforme a adaptação abaixo do guia do facilitador.

| Atividade | Pergunta que responde | Evidência que deixa |
|---|---|---|
| Governança | Quem pode aprovar o caso e aceitar o risco residual? | Ficha de decisão com o nome do responsável |
| Gestão de riscos | O que pode dar errado e qual seria a gravidade? | Registro de risco com a resposta escolhida |
| Segurança e privacidade | A quais dados e a quais ações o agente tem acesso? | Matriz de permissões e testes de acesso |
| Qualidade e avaliação | Como a equipe sabe que o comportamento é adequado? | Conjunto de testes com critério de aprovação e métricas |
| Operação e supervisão | Como a equipe detecta a falha, interrompe a execução e recupera o estado? | Logs mínimos, alerta e procedimento de reversão |

![Cinco colunas lado a lado: governança, gestão de riscos, segurança e privacidade, qualidade e avaliação, e operação e supervisão. Cada coluna traz a pergunta que a atividade responde e a evidência que ela deixa, e a coluna da governança aparece destacada porque a ficha de decisão com o nome do responsável é a evidência que mais costuma faltar.](assets/cinco-distincoes.png)

A tabela serve como teste de diagnóstico numa conversa de projeto. Quando alguém afirma que um agente "está governado", a pergunta seguinte é qual das cinco evidências existe, e é comum que falte justamente a evidência da primeira linha, o nome de quem aceitou o risco residual. A coluna da evidência é a que a ficha de governança cobra, linha a linha, nas páginas [Riscos de agentes](riscos-de-agentes.md) e [Controles e evidências](controles-e-evidencias.md).

## Quatro decisões

O guia organiza a governança mínima de um caso de uso em quatro decisões de autorização. Cada uma tem uma pergunta e um dono, e a ficha de governança registra a resposta.

| Decisão | Pergunta | Linha da ficha que registra |
|---|---|---|
| 1. Autorizar o caso de uso | Existe problema legítimo, benefício esperado e alternativa sem IA analisada? | Dono e finalidade |
| 2. Autorizar dados e ferramentas | Quais dados, modelos, provedores, skills e integrações estão permitidos? | Dados e ferramentas |
| 3. Autorizar a autonomia | O agente sugere, prepara para aprovação ou executa, com qual limite e quem o interrompe? | Autonomia |
| 4. Autorizar produção e continuidade | Quais testes, responsáveis, métricas, critérios de parada e revisões são exigidos? | Evidência e gate, canal e versão, revisão e retirada |

![Quatro decisões de autorização numeradas, caso de uso, dados e ferramentas, autonomia, e produção e continuidade, ligadas às linhas da ficha de governança que registram cada uma. A quarta decisão se liga a três linhas, evidência e gate, canal e versão, e revisão e retirada, e as linhas faixa de risco e riscos e controles aparecem em cinza, sem decisão de autorização própria.](assets/quatro-decisoes.png)

A decisão 1 inclui a alternativa sem IA porque a comparação com essa alternativa é o critério que mostra se o benefício esperado justifica o risco novo. Um relatório gerado por consulta SQL agendada, por exemplo, resolve parte dos casos que chegam à equipe como pedido de agente, e o registro dessa comparação na linha "Dono e finalidade" evita que a pergunta volte a cada revisão.

A decisão 3 usa três níveis de autonomia. No primeiro, o agente sugere e a pessoa decide e executa. No segundo, o agente prepara a ação, como um rascunho de pull request ou uma mudança de cadastro, e a execução depende de aprovação explícita. No terceiro, o agente executa a ação sem aprovação prévia, e a supervisão passa a ser feita depois do fato, por log e alerta. A disciplina [Arquitetura de Soluções com IA Generativa](../referencia/bibliografia.md#mendes-controle-e-autonomia-modulo-4-agentes) distingue as formas de controle operacional pela pergunta "quem escolhe a próxima transição", e a linha "Autonomia" da ficha registra a resposta a essa pergunta junto com o nome de quem pode interromper a execução.

![Três cartões em degraus, em ordem de autonomia crescente: sugere, prepara para aprovação e executa. Cada cartão indica quem executa a ação e quando a pessoa supervisiona, antes da ação, antes da execução aprovada ou depois do fato por log e alerta, e o nível executa aparece destacado.](assets/niveis-de-autonomia.png)

## Papéis no modelo federado

Para equipes que começam a governar o uso de IA, o guia recomenda um modelo federado e leve. A área demandante responde pela finalidade e pelo impacto, a engenharia implementa as salvaguardas, segurança e privacidade apoiam os casos sensíveis e a operação acompanha a execução. O grau de revisão cresce com a faixa de risco do caso, o que dispensa um comitê para cada alteração trivial e concentra a revisão formal nos casos da faixa alta.

| Papel | Responde por |
|---|---|
| PO ou dono do processo | Finalidade, benefício, público, impacto, aceitação funcional e autorização de uso |
| Líder técnico ou engenharia | Arquitetura, identidade e permissões, avaliações, versionamento e reversão |
| Segurança e privacidade | Critérios de risco, tratamento de dados e revisão de casos sensíveis |
| Operação ou plataforma | Monitoramento, custos, incidentes, retenção técnica e desativação |
| Patrocinador ou gestor competente | Aceitação formal do risco residual relevante e arbitragem entre as áreas |

![Cinco papéis do modelo federado com aquilo por que cada um responde: PO ou dono do processo, líder técnico ou engenharia, segurança e privacidade, operação ou plataforma, e patrocinador ou gestor competente. O PO preenche a linha dono e finalidade e o líder técnico aprova na linha evidência e gate. Abaixo, três barras crescentes mostram que o grau de revisão aumenta da faixa baixa para a alta, onde se concentra a revisão formal.](assets/papeis-no-modelo-federado.png)

Numa equipe pequena, uma mesma pessoa acumula dois ou três papéis, e a matriz continua útil porque obriga a declarar quem acumula o quê. A linha "Dono e finalidade" da ficha recebe o nome do PO ou do dono do processo, e a linha "Evidência e gate" recebe o nome de quem aprova a publicação, que em geral é o líder técnico.

## Supervisão humana efetiva

A revisão humana aparece em quase toda proposta de controle para agentes, e o guia estabelece quatro condições para que ela funcione como controle. O revisor precisa ter informação suficiente sobre o que o agente fez, tempo para examinar o resultado, autoridade para recusar e possibilidade real de rejeitar antes que o efeito se torne irreversível. A aprovação automática, a conferência superficial e a revisão feita depois de um ato irreversível deixam de atender a essas condições, e por isso o guia não as considera supervisão humana efetiva.

![Quatro condições ligadas por “e”, todas necessárias para a supervisão humana efetiva: informação, tempo, autoridade e possibilidade real de rejeitar antes do efeito irreversível. Abaixo, em laranja, três práticas que não contam como supervisão: aprovação automática, conferência superficial e revisão depois de um ato irreversível, e uma nota sobre a revisão de Parasuraman e Manzey com a resposta de desenho do controle.](assets/supervisao-humana-efetiva.png)

A literatura de fatores humanos explica por que as condições de informação e de exame atento são frágeis num fluxo de aprovação repetitiva. A revisão de [Parasuraman e Manzey](../referencia/bibliografia.md#parasuraman-e-manzey-complacency-and-bias-in-human-use-of-automation-2010) sobre complacência e viés de automação conclui que os dois fenômenos ocorrem tanto em novatos quanto em especialistas e que treinamento e instruções não os evitam. Um fluxo em que o revisor aprova dezenas de sugestões corretas seguidas cria exatamente a condição descrita pelos autores, e o desenho do controle precisa reduzir o volume de aprovação ou exigir que o revisor registre o que conferiu.

A [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) traz uma exigência relacionada no art. 20, que garante ao titular o direito de solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais. Um agente que decide sozinho sobre pessoas, sem revisão humana prévia, aproxima o caso dessa hipótese legal, e a avaliação da aplicabilidade cabe à área jurídica e de privacidade da organização.

## Quadro de referência normativo

As referências abaixo entram como quadro de orientação, sem estudo aprofundado nesta sessão. Cada linha indica o que a referência é e o uso que esta sessão faz dela.

| Referência | O que é | Uso nesta sessão |
|---|---|---|
| [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023) | Framework voluntário de gestão de riscos de IA, publicado pelo NIST em janeiro de 2023 | Organiza o trabalho em quatro funções, descritas abaixo |
| [NIST AI 600-1](../referencia/bibliografia.md#nist-ai-600-1-generative-artificial-intelligence-profile-2024) | Perfil do AI RMF para IA generativa, de julho de 2024, também de uso voluntário | Lista riscos próprios da IA generativa que complementam o AI RMF |
| [ISO/IEC 42001:2023](../referencia/bibliografia.md#isoiec-420012023) | Norma de requisitos para um sistema de gestão de IA na organização, edição 1.0 de 18/12/2023 | Referência de estrutura de responsabilidade e política, sem promessa de conformidade ou certificação |
| [OWASP Top 10 para aplicações de LLM, edição 2026](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026) | Lista de riscos técnicos de aplicações com LLM, publicada em agosto de 2026 | Nomeia os três incidentes da página [Riscos de agentes](riscos-de-agentes.md): LLM01 (2026), LLM03 (2026) e LLM07 (2026) |
| [LGPD, Lei nº 13.709/2018](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) | Lei vigente de proteção de dados pessoais | Orienta o tratamento de dado pessoal lido ou gerado pelo agente, com os princípios do art. 6º, a revisão do art. 20 e a segurança do art. 46 |
| [PL 2338/2023](../referencia/bibliografia.md#camara-dos-deputados-pl-23382023-ficha-de-tramitacao) | Projeto de lei sobre desenvolvimento e uso de inteligência artificial, de autoria do Senado Federal | Projeto em tramitação, sem força de lei, citado apenas como referência de acompanhamento |

O NIST AI RMF 1.0 organiza a gestão de riscos em quatro funções, e a página do Core afirma que a função de governar é transversal às demais. O guia do facilitador acrescenta que as quatro funções não formam uma sequência obrigatória de fases.

- **Govern (governar):** estabelecer papéis, políticas, tolerância a risco, treinamento, revisão e responsabilização.
- **Map (mapear):** descrever finalidade, usuários, dados, partes afetadas, fornecedores e contexto de uso.
- **Measure (medir):** avaliar respostas, segurança, privacidade, robustez, custo, falhas e limitações.
- **Manage (gerenciar):** priorizar riscos, mitigar, aprovar ou impedir a entrada em produção, monitorar e corrigir.

![A função Govern, governar, aparece como moldura que envolve as outras três funções do NIST AI RMF 1.0, Map, Measure e Manage, cada uma com o que ela cobre. A nota de rodapé informa que as quatro funções não formam uma sequência obrigatória de fases.](assets/funcoes-do-nist-ai-rmf.png)

A situação do PL 2338/2023 muda a cada tramitação. Na consulta de 03/11/2026, a ficha de tramitação da Câmara dos Deputados exibia "Aguardando Parecer do(a) Relator(a) na Comissão Especial sobre Inteligência Artificial (PL 2338/23)", com última movimentação em 27/10/2026 e regime de prioridade, e qualquer repetição desse dado exige nova consulta à ficha. A aplicabilidade de cada norma a um caso concreto depende de avaliação jurídica e da área de privacidade, conforme a nota metodológica do guia do facilitador.

O OWASP mantém duas páginas com numerações diferentes, e o identificador sem o ano gera confusão. A página de índice do projeto ainda listava a edição 2025 na consulta de 03/11/2026, com agência excessiva em LLM06 (2025) e desinformação em LLM09 (2025), enquanto a publicação de 2026 usa LLM03 e LLM07 para os mesmos riscos, e por isso todo identificador citado nesta sessão traz o ano da edição.

!!! abstract "Linha da ficha"
    Dono e finalidade, e autonomia:

    - Quem responde pelo caso, que problema ele resolve e que alternativa sem IA foi considerada?
    - O agente sugere, prepara para aprovação ou executa, e quem pode interromper a execução?
    - O revisor humano tem informação, tempo, autoridade e possibilidade real de rejeitar antes do efeito irreversível?

**Próxima página:** [Triagem por criticidade](triagem-por-criticidade.md).
