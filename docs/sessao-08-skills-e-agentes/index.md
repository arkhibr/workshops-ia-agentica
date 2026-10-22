# S8 — Skills e agentes

**Bloco:** 3 — Execução

## Problema

A equipe já usa agentes de IA, mas cria skills e agentes por tentativa e erro: o custo de tokens surge só na fatura, o modelo é escolhido por hábito, e permissões, segurança e coordenação entre vários agentes ficam implícitas.

## Intenção metodológica

Esta sessão ensina a projetar skills e agentes como artefatos de engenharia, com requisitos funcionais e não funcionais declarados antes da construção. Os eixos previstos são custo de tokens, escolha de modelo, desempenho, segurança, multiagentes, observabilidade e avaliação do resultado.

Na parte de segurança, a sessão discute a atenção às credenciais que uma skill ou um agente recebe. O agente não deve usar as credenciais pessoais da pessoa que o executa, como a conta do Windows, e sim credenciais próprias e restritas, como tokens de acesso pessoal (PATs) com escopo mínimo e validade curta. A sessão trata ainda de onde guardar o segredo (fora do repositório, do arquivo de instruções e do texto da skill), de como revogá-lo e de como impedir que o agente o exiba em logs ou artefatos gerados. Esta lista é o escopo previsto e será detalhada, com fontes, quando a página de segurança for escrita.

A geração de artefatos entra na teoria e na dinâmica da sessão. A teoria trata de o que uma skill ou um agente produz (documentos, código, relatórios, páginas), em que formato, e de que modo o artefato gerado se torna a fonte de comparação para a conferência. A dinâmica pede que cada equipe construa uma skill ou um agente que gere um artefato real e confira esse artefato contra critérios declarados antes da construção.

## Ao final desta sessão, o participante consegue

Criar uma skill e um agente com escopo, modelo, ferramentas e permissões justificados, fazer cada um gerar um artefato e conferir esse artefato contra critérios declarados.

---

> Conteúdo completo a desenvolver. Escopo ainda em definição com o instrutor.
