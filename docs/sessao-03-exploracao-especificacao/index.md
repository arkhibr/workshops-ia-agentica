# S3 — Exploração e especificação

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que um pedido tecnicamente correto ainda produz o sistema errado?

## Problema

Um pedido vago ao agente ("ative o desconto de atacado") produz código que compila, passa nos testes que já existiam e ainda assim resolve o problema errado. A regra de negócio inteira não chegou a ser escrita em nenhum documento, e permanecia apenas com quem fez o pedido.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática, e cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## Dois temas, duas profundidades

A sessão organiza o conteúdo em dois temas, e cada tema percorre a mesma progressão de profundidade: **conceitos** (teoria comum a todos), **exemplo de aplicação de IA** (demonstração conduzida pelo instrutor, comum a todos), e dois exercícios finais — **geral**, para quem não escreve código, e **especialista**, para quem implementa. Os dois exercícios partem do mesmo pedido e chegam à mesma especificação, um verificando por retrotradução e conferência manual, o outro por execução de teste.

- **Tema 1 — Intervenção socrática.** O ciclo de especificação e o método que mantém mais de uma leitura de um pedido vago viva por mais tempo, antes de convergir cedo demais para a primeira interpretação.
- **Tema 2 — Decomposição de requisitos.** O vocabulário que separa regra de negócio, requisito funcional e requisito não funcional, e o critério que torna cada um verificável.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Aplicar** o ciclo explorar → perguntar → propor → especificar a um pedido vago antes de acionar o agente.
2. **Conduzir** uma intervenção socrática que mantém mais de uma leitura de um pedido viva, em vez de convergir para a primeira interpretação.
3. **Classificar** um requisito como regra de negócio (BR), requisito funcional (FR) ou requisito não funcional (NFR).
4. **Escrever** um requisito não funcional como cenário de qualidade verificável, com a função de aptidão que o mantém verdadeiro.
5. **Escrever** uma especificação que um agente segue sem precisar decidir sozinho o que o pedido queria dizer.

## O caso Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem uma lacuna conhecida: a função `calcularDesconto` recebe um `tipoCliente` que não usa, e a faixa de 20% para clientes de atacado acima de R$ 10.000,00 nunca foi implementada. Esta sessão fecha essa lacuna pelo caminho longo, em dois temas: primeiro elicitando a regra por intervenção socrática, depois decompondo-a em BR, FR e NFR.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Trilha | Página |
|---|---:|---|---|---|
| 10:00–10:16 | 16 | Tema 1 — Conceitos | Comum | [Intervenção socrática e divergência do pensamento](intervencao-socratica-conceitos.md) |
| 10:16–10:28 | 12 | Tema 1 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](intervencao-socratica-exemplo-de-aplicacao-de-ia.md) |
| 10:28–11:00 | 32 | Tema 1 — Exercício | Geral | [Exercício de IA — Geral](intervencao-socratica-exercicio-geral.md) |
| 10:28–11:00 | 32 | Tema 1 — Exercício | Especialista | [Exercício de IA — Especialista](intervencao-socratica-exercicio-especialista.md) |
| 11:00–11:05 | 5 | Intervalo | Todos | Nenhuma |
| 11:05–11:20 | 15 | Tema 2 — Conceitos | Comum | [Decomposição de requisitos: BR, FR e NFR](decomposicao-de-requisitos-conceitos.md) |
| 11:20–11:33 | 13 | Tema 2 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](decomposicao-de-requisitos-exemplo-de-aplicacao-de-ia.md) |
| 11:33–11:55 | 22 | Tema 2 — Exercício | Geral | [Exercício de IA — Geral](decomposicao-de-requisitos-exercicio-geral.md) |
| 11:33–11:55 | 22 | Tema 2 — Exercício | Especialista | [Exercício de IA — Especialista](decomposicao-de-requisitos-exercicio-especialista.md) |
| 11:55–12:00 | 5 | Síntese e autoavaliação | Comum | [Síntese e referências](sintese-e-referencias.md) |

O conteúdo soma 115 minutos, e o intervalo consome os 5 restantes.

## Como conduzir

As quatro páginas de conceitos e exemplo têm caixas de destaque embutidas no texto. Pare nesses pontos, em lugar de ler a pergunta e seguir em frente.

Ao chegar no exercício, a trilha especialista monta o projeto do zero a partir dos blocos de código da própria página, o que leva poucos minutos e garante que todos partam do mesmo estado. A trilha geral parte da regra descrita em texto na própria página do exercício, e verifica o resultado por retrotradução e conferência manual, sem terminal.

**Próxima página:** [Intervenção socrática e divergência do pensamento](intervencao-socratica-conceitos.md).
