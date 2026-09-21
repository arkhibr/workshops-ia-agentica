# S3 — Exploração e especificação

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que um pedido tecnicamente correto ainda produz o sistema errado?

## Problema

Um pedido vago ao agente ("ative o desconto de atacado") produz código que compila, passa nos testes que já existiam e ainda assim resolve o problema errado. A regra de negócio inteira não chegou a ser escrita em nenhum documento, e permanecia apenas com quem fez o pedido.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática, e cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## As duas trilhas desta sessão

A sessão é conduzida para uma turma única, com duas trilhas na parte prática. A **trilha técnica** é de quem implementa em código, usa terminal, git e Node.js 20 ou superior, e verifica a especificação executando testes. A **trilha de negócio** é de quem escreve a demanda e conversa com a área cliente, trabalha numa interface de chat, e verifica a mesma especificação por retrotradução e conferência de casos.

A teoria é comum às duas. Cada página de teoria fecha com dois blocos de audiência, "Para o time de desenvolvimento" e "Para o time de negócio", e cada participante lê o da própria trilha. Na parte prática as páginas são distintas: a [Oficina de ferramentas](oficina-de-ferramentas.md) é da trilha técnica e a [Oficina de negócio](oficina-de-negocio.md) é da trilha de negócio. A [Oficina de entrevista socrática](oficina-de-entrevista.md) atende as duas, porque não usa código, com duplas formadas dentro de cada trilha.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Aplicar** o ciclo explorar → perguntar → propor → especificar a um pedido vago antes de acionar o agente.
2. **Classificar** um requisito como regra de negócio (BR), requisito funcional (FR) ou requisito não funcional (NFR).
3. **Escrever** um requisito não funcional como cenário de qualidade verificável, com a função de aptidão que o mantém verdadeiro.
4. **Formular** perguntas de elicitação que expõem ambiguidade antes que ela vire código.
5. **Escrever** uma especificação que um agente segue sem precisar decidir sozinho o que o pedido queria dizer.

## O caso Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem uma lacuna conhecida: a função `calcularDesconto` recebe um `tipoCliente` que não usa, e a faixa de 20% para clientes de atacado acima de R$ 10.000,00 nunca foi implementada. Esta sessão fecha essa lacuna pelo caminho longo. O pedido chega vago, e o trabalho aqui é transformá-lo numa especificação antes de qualquer linha de código.

## Roteiro da sessão (2h, das 10h às 12h)

Oito blocos, e nenhum bloco mistura tipos de atividade. Onde a trilha muda o material, a tabela traz uma linha por trilha.

| Horário | Min | Bloco | Tipo | Trilha | Página |
|---|---:|---|---|---|---|
| 10:00–10:06 | 6 | O ciclo de especificação | Teoria | Comum | [O ciclo de especificação](ciclo-de-especificacao.md) |
| 10:06–10:20 | 14 | Categorias de requisito | Teoria | Comum | [BR, FR e NFR](br-fr-nfr.md) e [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md) |
| 10:20–10:32 | 12 | Elicitação e entrevista socrática | Teoria | Comum | [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) e [Entrevista socrática](entrevista-socratica.md) |
| 10:32–10:37 | 5 | Especificação executável | Teoria | Comum | [Especificação executável](especificacao-executavel.md) |
| 10:37–10:48 | 11 | Demonstração do ciclo completo | Demonstração | Comum | [Exemplo arquitetural](exemplo-arquitetural.md) |
| 10:48–11:00 | 12 | Estudo de caso | Discussão | Grupos dentro de cada trilha | [Estudo de caso](estudo-de-caso.md) |
| 11:00–11:05 | 5 | Intervalo | Sem material | Todos | Nenhuma |
| 11:05–11:20 | 15 | Oficina do ciclo de especificação | Prática guiada | Técnica | [Oficina de ferramentas](oficina-de-ferramentas.md) |
| 11:05–11:20 | 15 | Oficina do ciclo de especificação | Prática guiada | Negócio | [Oficina de negócio](oficina-de-negocio.md) |
| 11:20–11:30 | 10 | Oficina de entrevista socrática | Prática guiada | Duplas dentro de cada trilha | [Oficina de entrevista socrática](oficina-de-entrevista.md) |
| 11:30–11:55 | 25 | Exercícios | Prática avaliada | Técnica | [Exercícios](exercicios.md), exercício-âncora 6 |
| 11:30–11:55 | 25 | Exercícios | Prática avaliada | Negócio | [Exercícios](exercicios.md), exercício-âncora 6N |
| 11:55–12:00 | 5 | Síntese e autoavaliação | Fechamento | Comum | [Síntese e referências](sintese-e-referencias.md) |

O conteúdo soma 115 minutos, e o intervalo consome os 5 restantes.

## Como conduzir

As seis páginas de teoria têm caixas de destaque embutidas no texto. Pare nesses pontos, em lugar de ler a pergunta e seguir em frente.

Ao chegar na oficina, a trilha técnica monta o projeto do zero a partir dos blocos de código da página, o que leva poucos minutos e garante que todos partam do mesmo estado. A demonstração da Sessão 1 apenas mostrou a lacuna de atacado. Aqui ela é fechada com teste escrito e passando. A trilha de negócio parte da regra descrita em texto na própria página da oficina dela, e fecha a mesma lacuna com especificação escrita e conferida por retrotradução.

**Próxima página:** [O ciclo de especificação](ciclo-de-especificacao.md).
