# S8 — Skills e agentes

**Bloco:** 4 — Automação, qualidade e integração

> **Pergunta-guia:** o que uma skill ou um agente precisa declarar antes de ser construído para que o custo, a segurança e o resultado possam ser conferidos depois?

## Problema

As sessões anteriores usaram o agente como ferramenta de uso individual. A partir desta sessão, a equipe passa a construir as próprias ferramentas: skills que ensinam o agente a executar uma tarefa recorrente do mesmo modo e agentes que recebem uma parte do trabalho com contexto, modelo e permissões próprios. Quando essa construção é feita por tentativa e erro, o custo de tokens aparece só na fatura, o modelo é escolhido por hábito, o desempenho é medido pela impressão de quem usa, e as credenciais e as permissões do agente ficam implícitas.

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo, sem leitura prévia obrigatória. A sessão tem duas partes. Na primeira, o instrutor apresenta skills, agentes, subagentes, geração de artefatos, escolha de modelos, custo e desempenho, e cada participante constrói e mede uma skill na oficina. Na segunda, o instrutor trata de segurança e credenciais, e cada equipe constrói uma skill com um subagente que gera um artefato conferível. A sessão pressupõe o ambiente configurado nas Sessões 1 e 2 e o uso do Claude Code.

Os números citados nas páginas de teoria vêm das fontes listadas na [bibliografia do curso](../referencia/bibliografia.md), que descrevem o comportamento documentado pela Anthropic. Nomes de modelos, preços e limites mudam com frequência, e a equipe confere a documentação vigente antes de decidir, a partir do estado documentado em 22/10/2026.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** skill, subagente e agente principal e escolher o mecanismo adequado a uma tarefa.
2. **Escrever** uma skill com descrição, corpo e script de conferência, seguindo as regras de tamanho e de carga da documentação.
3. **Declarar** os requisitos funcionais e não funcionais de uma skill ou de um agente: artefato produzido, modelo, orçamento de tokens, tempo, permissões e credenciais.
4. **Estimar** o efeito do cache de prompt e da escolha do modelo sobre o custo de uma tarefa repetida.
5. **Aplicar** os cuidados com credenciais: identidade própria do agente, token com escopo mínimo e validade curta, armazenamento fora do repositório e rodízio.
6. **Conferir** o artefato gerado por um agente por meio de script e de critérios declarados antes da construção.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [Skills](skills.md) | Teoria | 7 min | Anatomia de uma skill, carga em três níveis e regras de escrita |
| 2 | [Agentes e subagentes](agentes-e-subagentes.md) | Teoria | 8 min | Quando usar skill, subagente ou vários agentes, e o que cada um custa |
| 3 | [Geração de artefatos](geracao-de-artefatos.md) | Teoria | 7 min | Modelo do artefato, conferência por script e laço de correção |
| 4 | [Escolha de modelos](escolha-de-modelos.md) | Teoria | 6 min | Critérios, estratégias de partida e o esforço como alavanca |
| 5 | [Custo de tokens](custo-de-tokens.md) | Teoria | 6 min | De onde o custo vem, o cache de prompt e as alavancas de redução |
| 6 | [Performance](performance.md) | Teoria | 5 min | Medidas de desempenho, paralelização e avaliação com casos reais |
| 7 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 21 min | Uma skill criada, executada e medida em dois modelos |
| | Intervalo | Pausa | 5 min | Nenhum |
| 8 | [Segurança e credenciais](seguranca-e-credenciais.md) | Teoria | 8 min | Permissões mínimas, identidade própria do agente e ciclo de vida do token |
| 9 | [Exercícios](exercicios.md) | Prática avaliada | 36 min | Skill e subagente que geram um artefato conferido por script |
| 10 | [Exercícios](exercicios.md) | Conferência cruzada | 6 min | Auditoria das credenciais e das permissões da equipe vizinha |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

O conteúdo soma 115 minutos, e o intervalo das 11h00 às 11h05 completa os 120 minutos de relógio. A primeira parte ocupa das 10h00 às 11h00, e a segunda, das 11h05 às 12h00.

## Como conduzir

Cada página de teoria apresenta um tema e termina numa tabela de decisão que a oficina e os exercícios reutilizam. O instrutor apresenta o tema em poucos minutos e não percorre as tabelas linha a linha, porque elas ficam à disposição da turma durante a prática.

A oficina e o exercício-âncora usam o mesmo exemplo, a skill `registrando-decisao-arquitetural`, que gera um registro de decisão arquitetural em Markdown para a ACME, uma universidade fictícia. O exemplo foi escolhido porque o artefato tem estrutura verificável por script e conteúdo que só uma pessoa confere, o que permite discutir as duas formas de conferência.

As equipes são formadas antes da sessão. Cada pessoa executa a oficina no próprio computador, numa pasta vazia, e nenhuma credencial real é usada: os exercícios de segurança trabalham com descrições e com tokens fictícios.

!!! warning "Limite desta sessão"
    Os números de custo, de ganho de desempenho e de consumo de tokens vêm de documentação e de relatos da própria Anthropic, medidos em tarefas e configurações específicas. Nenhum deles mede as tarefas da equipe. A decisão de adotar uma skill ou um agente depende da medição feita na oficina e no exercício, com as tarefas e os modelos da própria equipe.

**Próxima página:** [Skills](skills.md).
