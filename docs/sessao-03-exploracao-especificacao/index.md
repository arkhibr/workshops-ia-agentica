# S3 — Exploração e especificação

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que um pedido tecnicamente correto ainda produz o sistema errado?

## Problema

Um pedido vago ao agente ("ative o desconto de atacado") produz código que compila, passa nos testes que já existiam e ainda assim resolve o problema errado. A regra de negócio inteira nunca chegou a ser escrita em lugar nenhum, só existia na cabeça de quem pediu.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática, e cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Aplicar** o ciclo explorar → perguntar → propor → especificar a um pedido vago antes de acionar o agente.
2. **Classificar** um requisito como regra de negócio (BR), requisito funcional (FR) ou requisito não funcional (NFR).
3. **Escrever** um requisito não funcional como cenário de qualidade verificável, com a função de aptidão que o mantém verdadeiro.
4. **Formular** perguntas de elicitação que expõem ambiguidade antes que ela vire código.
5. **Escrever** uma especificação que um agente segue sem precisar decidir sozinho o que o pedido queria dizer.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem uma lacuna conhecida: a função `calcularDesconto` recebe um `tipoCliente` que não usa, e a faixa de 20% para clientes de atacado acima de R$ 10.000,00 nunca foi implementada. Esta sessão fecha essa lacuna pelo caminho longo. O pedido chega vago, e o trabalho aqui é transformá-lo numa especificação antes de qualquer linha de código.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ciclo de especificação](ciclo-de-especificacao.md) | Teoria | 6 min | As quatro etapas do ciclo e o custo de pular direto para o código |
| 2 | [BR, FR e NFR](br-fr-nfr.md) | Teoria | 7 min | Classificar um requisito pelas três categorias e reconhecer quando confundem |
| 3 | [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md) | Teoria | 8 min | Catálogo de atributos de qualidade, cenário de qualidade e função de aptidão arquitetural |
| 4 | [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) | Teoria | 6 min | Um repertório de perguntas que expõe requisito implícito antes da implementação |
| 5 | [Entrevista socrática](entrevista-socratica.md) | Teoria | 7 min | As cinco fases, o contrato de uma pergunta por vez e o ledger epistemológico |
| 6 | [Especificação executável](especificacao-executavel.md) | Teoria | 7 min | O critério que separa especificação seguível de resumo do pedido |
| 7 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 9 min | Ver, com a Vetor, o ciclo inteiro aplicado a um pedido vago até a especificação completa |
| 8 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 11 min | Julgar de quem é a responsabilidade quando a especificação "tecnicamente" cobria o pedido |
| — | Intervalo | — | 5 min | — |
| 9 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 18 min | Conduzir o ciclo completo e fechar a lacuna de atacado da Vetor de verdade |
| 10 | [Oficina de entrevista socrática](oficina-entrevista-socratica.md) | Prática guiada | 16 min | Ser entrevistado pelo agente e sair com o dossiê, o ledger e as perguntas abertas |
| 11 | [Exercícios](exercicios.md) | Prática avaliada | 15 min | Exercício-âncora: especificação escrita, implementada e verificada por teste |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As seis páginas de teoria têm caixas de destaque embutidas no texto. Pare de verdade nesses pontos, em vez de ler a pergunta e seguir em frente.

Ao chegar na oficina, todos clonam `exemplo/vetor`, o mesmo projeto usado na Sessão 1. A demonstração da Sessão 1 apenas mostrou a lacuna de atacado. Aqui ela é fechada de verdade, com teste escrito e passando. Peça que clonem o repositório antes de a sessão começar.

**Próxima página:** [O ciclo de especificação](ciclo-de-especificacao.md).
