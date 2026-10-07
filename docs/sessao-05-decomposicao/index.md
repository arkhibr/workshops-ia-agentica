# S5 — Spec Kit: da regra ao código

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** o que precisa estar escrito antes que um agente transforme uma regra de negócio em código, e onde o humano intervém no caminho?

## Problema

Uma regra de negócio bem formulada ainda pode chegar errada ao código. Entre a regra e o teste verde, o agente toma dezenas de decisões: o que acontece no valor exato do limite, que critério conta como sucesso, em quantas tarefas o trabalho se divide e em que ordem. Se essas decisões ficam só na conversa, ninguém consegue revisá-las, e a primeira chance de descobrir uma delas é um defeito em produção.

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo, sem leitura prévia obrigatória. O instrutor alterna explicação, demonstração e prática, e cada participante trabalha na própria máquina. A única tarefa antes da aula é a [preparação do ambiente](preparacao.md), que instala o GitHub Spec Kit 1.1.1.

## Os dois temas

A sessão percorre o caminho básico do GitHub Spec Kit, os cinco comandos que a ferramenta apresenta como sequência principal: `constitution`, `specify`, `plan`, `tasks` e `implement`. Os comandos opcionais, como `clarify` e `analyze`, ficam para a Sessão 6.

**Tema 1 — Da regra à especificação.** A constitution fixa os princípios do projeto, e a spec traduz um mapa de regras com IDs, no formato da Sessão 4, em histórias, requisitos e critérios de sucesso. O foco é encontrar o que o agente decidiu sozinho.

**Tema 2 — Do plano ao código.** O plano escolhe a tecnologia, as tarefas decompõem o trabalho e a implementação executa as tarefas até os testes passarem. O foco é a decomposição e o lugar dos pontos de controle humano.

A demonstração do instrutor usa o pedido mínimo de atacado da Vetor, a plataforma fictícia de e-commerce B2B do workshop. Os exercícios usam outra feature da Vetor, o cálculo de frete, e partem do projeto de exemplo executável do repositório.

## Objetivos de aprendizagem

Ao final da sessão, o participante será capaz de:

1. **Executar** o caminho básico do Spec Kit, da constitution ao código com testes passando.
2. **Escrever** princípios de constitution que mudam o que o agente gera.
3. **Identificar** numa spec as decisões que o agente tomou fora do mapa de regras.
4. **Classificar** tarefas como atômicas ou compostas, com o comando que prova a conclusão de cada uma.
5. **Posicionar** pontos de controle humano na execução, rodando o `implement` por etapa.
6. **Verificar** a rastreabilidade de uma regra de origem até o teste e o código.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Página | Produto do bloco |
|---|---:|---|---|---|
| Antes da aula | — | Preparação individual | [Preparação do ambiente](preparacao.md) | Spec Kit 1.1.1 instalado e testado com o agente |
| 10:00–10:15 | 15 | Kahoot | Nenhuma | Respostas registradas no Kahoot |
| 10:15–10:27 | 12 | Tema 1 — Conceitos | [Especificação com Spec Kit: constitution e spec](especificacao-com-spec-kit-conceitos.md) | Os cinco comandos e o critério para uma suposição que decide negócio |
| 10:27–10:35 | 8 | Tema 1 — Exemplo de aplicação de IA | [Exemplo de aplicação de IA](especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md) | Três achados na spec do pedido mínimo |
| 10:35–11:00 | 25 | Tema 1 — Exercício | [Exercício de IA: especificar o frete da Vetor](especificacao-com-spec-kit-exercicio.md) | `spec.md` do frete versionada e três respostas sobre ela |
| 11:00–11:05 | 5 | Intervalo | Nenhuma | Nenhum |
| 11:05–11:17 | 12 | Tema 2 — Conceitos | [Do plano ao código: plan, tasks e implement](do-plano-ao-codigo-conceitos.md) | Tarefa atômica, anatomia do `tasks.md` e pontos de controle |
| 11:17–11:25 | 8 | Tema 2 — Exemplo de aplicação de IA | [Exemplo de aplicação de IA](do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md) | Esqueleto de tarefas do pedido mínimo, anotado |
| 11:25–11:55 | 30 | Tema 2 — Exercício | [Exercício de IA: do plano ao frete funcionando](do-plano-ao-codigo-exercicio.md) | Frete implementado, testes passando e RN-12 localizada |
| 11:55–12:00 | 5 | Síntese e autoavaliação | [Síntese e referências](sintese-e-referencias.md) | Autoavaliação e ponte para a Sessão 6 |

O conteúdo soma 100 minutos depois do Kahoot, e o intervalo das 11:00 às 11:05 completa os 120 minutos de relógio.

## Como conduzir

Confirme durante o Kahoot que todos têm o `specify version` respondendo `1.1.1`. Quem chegou sem a instalação resolve com o instrutor nesse intervalo, seguindo a tabela de problemas comuns da preparação.

Os comandos do agente levam de 40 segundos a 2 minutos cada. Nos exercícios, use essa espera para as perguntas da página, em vez de deixar a turma olhando o terminal. Nas demonstrações, rode os comandos antes da aula e mostre os artefatos já gerados, se a rede da sala for lenta.

Os exercícios mandam ler seções específicas dos artefatos, nunca o arquivo inteiro. Uma `spec.md` passa de cem linhas e um `tasks.md` passa de cento e cinquenta. Segure a turma nas seções indicadas.

!!! warning "Limite da IA nesta sessão"
    O agente escreve todos os artefatos e decide tudo o que o mapa de regras deixou em aberto. O Spec Kit só garante que essas decisões fiquem gravadas em arquivo. Quem lê as seções indicadas e devolve ao dono da regra o que não era do agente decidir é o participante.

**Próxima página:** [Preparação do ambiente](preparacao.md).
