# S3 — Exploração e especificação

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que um pedido tecnicamente correto ainda produz o sistema errado?

## Problema

Um pedido vago ao agente ("ative o desconto de atacado") produz código que compila, passa nos testes que já existiam e ainda assim resolve o problema errado — porque a regra de negócio inteira nunca chegou a ser escrita em lugar nenhum, só existia na cabeça de quem pediu.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática — cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Aplicar** o ciclo explorar → perguntar → propor → especificar a um pedido vago antes de acionar o agente.
2. **Classificar** um requisito como regra de negócio (BR), requisito funcional (FR) ou requisito não funcional (NFR).
3. **Formular** perguntas de elicitação que expõem ambiguidade antes que ela vire código.
4. **Escrever** uma especificação que um agente segue sem precisar decidir sozinho o que o pedido queria dizer.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem uma lacuna conhecida: a função `calcularDesconto` recebe um `tipoCliente` que não usa — a faixa de 20% para clientes de atacado acima de R$ 10.000,00 nunca foi implementada. Esta sessão fecha essa lacuna, mas o caminho é o que importa: o pedido chega vago, e o trabalho desta sessão é transformá-lo numa especificação antes de qualquer linha de código.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ciclo de especificação](ciclo-de-especificacao.md) | Teoria | 8 min | As quatro etapas do ciclo e por que pular direto para código custa mais caro depois |
| 2 | [BR, FR e NFR](br-fr-nfr.md) | Teoria | 12 min | Classificar um requisito pelas três categorias e reconhecer quando confundem |
| 3 | [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) | Teoria | 8 min | Um repertório de perguntas que expõe requisito implícito antes da implementação |
| 4 | [Especificação executável](especificacao-executavel.md) | Teoria | 9 min | O critério que separa especificação seguível de resumo do pedido |
| 5 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 10 min | Ver, com a Vetor, o ciclo inteiro do pedido vago à especificação completa |
| 6 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 13 min | Julgar de quem é a responsabilidade quando a especificação "tecnicamente" cobria o pedido |
| — | Intervalo | — | 5 min | — |
| 7 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 30 min | Conduzir o ciclo completo e fechar a lacuna de atacado da Vetor de verdade |
| 8 | [Exercícios](exercicios.md) | Prática avaliada | 20 min | Exercício-âncora: especificação escrita, implementada e verificada por teste |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As quatro páginas de teoria têm caixas de destaque embutidas no texto. Pare de verdade nesses pontos, em vez de ler a pergunta e seguir em frente.

Ao chegar na oficina, todos clonam `exemplo/vetor`, o mesmo projeto usado na Sessão 1 — a lacuna de atacado que a demonstração da Sessão 1 apenas mostrou, esta sessão fecha de verdade, com teste escrito e passando. Peça que clonem o repositório antes de a sessão começar.

**Próxima página:** [O ciclo de especificação](ciclo-de-especificacao.md).
