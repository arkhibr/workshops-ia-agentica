# Triagem por criticidade

Esta página apresenta o inventário dos casos de uso como primeiro passo da governança, a triagem em três faixas de criticidade e a regra que decide a faixa pelo fator mais grave. A página preenche, na [ficha de governança](index.md#a-ficha-de-governanca), as linhas "Dados e ferramentas" e "Faixa de risco". A ficha de governança é a tabela de oito linhas que esta sessão usa para registrar o que precisa estar decidido antes de outra pessoa da equipe instalar uma skill ou um agente.

## O inventário vem antes da triagem

A triagem só classifica os casos que a equipe conhece, e por isso o primeiro passo recomendado pelo guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026) é inventariar os pilotos, agentes, skills e provedores em uso. O inventário corresponde à função de mapear do [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023), que pede a descrição da finalidade, dos usuários, dos dados, das partes afetadas, dos fornecedores e do contexto de uso antes de qualquer medição.

Numa equipe de desenvolvimento, o inventário inclui itens que raramente aparecem numa lista de sistemas. Entram as skills guardadas na pasta pessoal de cada pessoa, os subagentes versionados nos repositórios, os servidores MCP configurados localmente, os tokens criados para o agente e os scripts que chamam a API de um provedor de modelo. Cada item recebe ao menos três campos, o nome do dono, a finalidade em uma frase e as classes de dado que ele lê, e um item sem dono identificado já é uma pendência registrada.

![Fluxo em quatro etapas, do inventário à faixa: inventariar skills, subagentes, servidores MCP, tokens e scripts de API, registrar os campos mínimos de dono, finalidade e classes de dado, descrever dados e ferramentas pela classe de dado e pelo nível de permissão e chegar à faixa de risco com o fator decisivo e as premissas. As duas primeiras etapas correspondem à função Map do NIST AI RMF, e um item sem dono vira pendência registrada.](assets/do-inventario-a-faixa.png)

## Dados e ferramentas

A linha "Dados e ferramentas" da ficha registra o que o agente lê e o que ele pode fazer. O guia usa quatro classes de dado e quatro níveis de permissão, e a combinação das duas listas é a matéria-prima da triagem.

| Classes de dado | Níveis de permissão |
|---|---|
| Público: documentação aberta, código de repositório público | Ler: consultar sem alterar |
| Interno: código privado, itens de trabalho, documentação interna | Recomendar: produzir sugestão que uma pessoa avalia |
| Pessoal: dado que identifica uma pessoa, tratado conforme a [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) | Escrever: criar ou alterar registro, arquivo ou cadastro |
| Sensível: dado pessoal sensível, segredo, dado financeiro ou outro dado cuja exposição cause dano grave à pessoa ou à organização | Executar: disparar ação com efeito externo, como pagamento, envio ou implantação |

Além das classes e das permissões, a linha registra o modelo e o provedor, as skills, os servidores MCP e as APIs chamadas pelo agente. A lista de ferramentas importa porque cada ferramenta amplia o que o modelo consegue fazer em resposta a uma instrução, e a página [Riscos de agentes](riscos-de-agentes.md) mostra que essa instrução pode vir de um documento lido pelo agente.

## As três faixas

O guia propõe três faixas de criticidade, cada uma com características típicas e um tratamento mínimo.

| Faixa | Características típicas | Tratamento mínimo |
|---|---|---|
| Baixa | Conteúdo público, sem dado pessoal, somente leitura e revisão humana de toda saída | Registro na ficha, testes básicos e aprovação do PO e do líder técnico |
| Moderada | Conteúdo interno, recuperação de documentos (RAG), integração limitada ou decisão assistida | Avaliação de riscos, revisão de segurança e privacidade conforme os dados e testes adversariais |
| Alta | Dado sensível, efeito relevante sobre pessoas, escrita em sistemas ou execução financeira | Avaliação aprofundada, aprovações formais, restrições fortes e a possibilidade de não implementar |

A figura abaixo aplica as três faixas a um mesmo agente genérico cuja configuração muda em dois momentos e mostra, a cada mudança, o fator que passa a decidir a faixa, o tratamento mínimo acrescentado e quem entra na revisão.

![Um mesmo agente em três configurações. Na faixa baixa, ele lê documentação aberta, só com permissão de leitura, e toda saída passa por revisão humana, sem fator de faixa moderada ou alta, com registro na ficha, testes básicos e revisão do PO e do líder técnico. Quando muda o dado e o agente passa a ler itens de trabalho internos por recuperação de documentos, o conteúdo interno e o RAG levam à faixa moderada, que acrescenta avaliação de riscos, testes adversariais e a revisão de segurança e privacidade conforme os dados. Quando muda a permissão e o agente passa a fechar os itens de trabalho, a escrita em sistemas é um fator crítico que leva sozinho à faixa alta, que acrescenta avaliação aprofundada, restrições fortes, a possibilidade de não implementar, aprovações formais e a aceitação do risco residual pelo patrocinador ou gestor competente. Antes de cada mudança, a ficha é revista.](assets/mesmo-agente-tres-faixas.png)

As faixas são uma ferramenta pedagógica adaptada do guia, sem valor de classificação normativa oficial. A faixa de um caso real depende do apetite a risco aprovado pela organização e, quando há dado pessoal, da avaliação jurídica e de privacidade, e a ficha registra a faixa como "preliminar" até essa avaliação.

## A regra do fator crítico

O guia do facilitador afirma que um único fator crítico pode levar o caso diretamente à faixa alta, e esta sessão adota, como decisão de método, a forma estrita dessa regra: um fator crítico leva o caso direto à faixa alta. Se o agente tem permissão de escrita em sistema financeiro, a faixa é alta, mesmo que ele leia apenas conteúdo interno e que toda saída passe por revisão humana. A justificativa registrada na ficha nomeia o fator que decidiu a faixa, e as demais características entram como contexto.

![Árvore de decisão da forma estrita da regra: se há algum fator crítico, como dado sensível, efeito relevante sobre pessoas, escrita em sistemas ou execução financeira, a faixa é alta. Sem fator crítico, um fator de faixa moderada leva à moderada, e sem nenhum dos dois a faixa é baixa. Ao lado, o exemplo da página compara a soma de pontos, excluída, com a regra estrita, que dá faixa alta pela escrita em sistema financeiro.](assets/regra-do-fator-critico.png)

A regra exclui a soma de pontos por um motivo de método. Numa pontuação aditiva, três fatores de baixo risco compensam um fator de consequência severa, e o resultado médio esconde justamente o fator que causaria o pior dano. A função de gerenciar do NIST AI RMF pede a priorização dos riscos, e o guia do facilitador fixa o critério dessa priorização na triagem ao proibir o uso de soma para "compensar" consequências severas.

A regra também cobre a mudança de faixa ao longo do tempo. Um agente que hoje lê itens de trabalho e amanhã recebe permissão para fechá-los muda de "ler" para "escrever", e a ficha precisa ser revista antes da mudança, junto com a troca de modelo, de base de documentos ou de finalidade, gatilhos registrados na linha "Revisão e retirada" da página [Compartilhamento governado](compartilhamento-governado.md).

## Leitura também tem risco

A permissão somente de leitura reduz o alcance da ação do agente e deixa intactos dois riscos. A leitura pode expor dado pessoal ou interno a quem não deveria vê-lo, inclusive ao provedor do modelo, e pode produzir uma conclusão equivocada que uma pessoa usa para decidir. O guia trata essa pergunta nas discussões orientadas e responde que o risco de um agente que apenas lê depende do que ele lê e do uso que se faz da resposta.

## Perguntas-guia da triagem

A ficha de triagem do guia, chamada ficha A, traz quatro perguntas para orientar a classificação e uma quinta, usada na dinâmica de grupo, que costuma mudar a faixa escolhida.

1. Quem sofreria com o pior erro plausível?
2. Há algum dado ou integração que não deveria chegar ao modelo?
3. O modelo poderia escolher uma ação que o usuário não autorizou?
4. Qual evidência falta para decidir?
5. Qual seria o impacto se a solução fosse usada fora da finalidade?

A quinta pergunta inclui na análise os usos possíveis que a finalidade declarada não prevê. Uma skill feita para resumir atas de reunião lê qualquer texto que receber, e o impacto do uso fora da finalidade depende do que mais o agente consegue ler e fazer com as ferramentas que tem.

## Premissas não verificadas

A ficha separa o que é fato verificado, o que é hipótese e o que é decisão pendente. Uma triagem feita no início do projeto depende de premissas, como "o token tem só escopo de leitura" ou "a base de documentos não contém dado pessoal", e cada premissa fica escrita na ficha com o nome de quem vai verificá-la. Como recomendação desta sessão, sem origem no guia, a premissa não verificada que mudaria a faixa caso fosse falsa torna a faixa preliminar, e a verificação dessa premissa passa a ser condição do gate de publicação registrado na linha "Evidência e gate" da ficha.

![Fluxo de uma premissa escrita na ficha com o nome de quem vai verificá-la. Se a faixa mudaria caso a premissa fosse falsa, a faixa fica preliminar e a verificação passa a ser condição do gate de publicação, e quando a faixa não mudaria a premissa continua registrada com responsável. Acima, os três estados que a ficha separa: fato verificado, hipótese e decisão pendente.](assets/premissa-nao-verificada.png)

## O que evitar na primeira semana

O guia lista o que não implantar no início de um programa de governança: um catálogo com dezenas de políticas, uma pontuação pseudoquantitativa detalhada, uma comissão que revise toda resposta gerada, a compra antecipada de plataforma de observabilidade e a promessa de conformidade com a [ISO/IEC 42001:2023](../referencia/bibliografia.md#isoiec-420012023). O ponto de partida recomendado são as fronteiras de confiança e as decisões irreversíveis, com evidências reproduzíveis, que são o assunto das páginas [Riscos de agentes](riscos-de-agentes.md) e [Controles e evidências](controles-e-evidencias.md).

!!! abstract "Linha da ficha"
    Dados e ferramentas, e faixa de risco:

    - Que classes de dado o agente lê, e que modelo, skills, servidores MCP e APIs ele usa?
    - O agente lê, recomenda, escreve ou executa?
    - Qual é a faixa, qual fator decidiu a faixa e que premissas ainda não foram verificadas?

**Próxima página:** [Riscos de agentes](riscos-de-agentes.md).
