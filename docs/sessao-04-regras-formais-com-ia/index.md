# S4 — Regras formais com IA

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que a mesma regra de negócio, escrita em prosa, é lida de um jeito pelo desenvolvedor e de outro pelo agente?

## Problema

"O desconto de atacado nunca ultrapassa o teto" parece uma frase sem ambiguidade, até alguém perguntar se "o teto" é por pedido, por cliente ou por mês, e descobrir que cada pessoa do time já assumia uma resposta diferente, em silêncio.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática, e cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## Dois temas, duas profundidades

A sessão organiza o conteúdo em dois temas, cada um com a mesma progressão: **conceitos** (teoria comum a todos), **exemplo de aplicação de IA** (demonstração conduzida pelo instrutor, comum a todos), e dois exercícios de engenharia reversa — **geral**, para quem lê planilha, e **especialista**, para quem lê código. Os dois exercícios de cada tema partem de um artefato real da Vetor, sem nenhuma especificação escrita disponível, e extraem dele as regras de negócio que ele esconde.

- **Tema 1 — Vocabulário e sentenças de regra.** SBVR (vocabulário, regra estrutural e operativa) e RuleSpeak (as três formas de sentença), com numeração, evidência e confiança.
- **Tema 2 — Tabelas de decisão e IA como formalizadora.** DMN (política de acerto), o papel do agente como formalizador em vez de decisor, e a retrotradução que verifica se a formalização preservou a intenção.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** regra estrutural de regra operativa no vocabulário do SBVR.
2. **Reescrever** uma regra de negócio em prosa usando as formas de sentença do RuleSpeak.
3. **Extrair** regras de negócio de um artefato existente (código ou planilha), sem especificação prévia, no vocabulário SBVR.
4. **Construir** uma tabela de decisão DMN para uma regra com mais de uma condição, escolhendo a política de acerto correta.
5. **Usar** um agente de codificação como formalizador de regra, verificando por retrotradução se ele preservou a intenção original.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B que atravessa o workshop, chega a esta sessão com duas regras de desconto especificadas em BR/FR na Sessão 3 (atacado e cliente recorrente), mas nenhuma delas formalizada em vocabulário controlado. Esta sessão fecha essa lacuna, e acrescenta dois artefatos legados sem especificação nenhuma: uma função de frete grátis em código e uma planilha de comissão de vendedores.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Trilha | Página |
|---|---:|---|---|---|
| 10:00–10:15 | 15 | Tema 1 — Conceitos | Comum | [Vocabulário e sentenças de regra: SBVR e RuleSpeak](vocabulario-e-sentencas-conceitos.md) |
| 10:15–10:26 | 11 | Tema 1 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](vocabulario-e-sentencas-exemplo-de-aplicacao-de-ia.md) |
| 10:26–11:00 | 34 | Tema 1 — Exercício | Geral | [Exercício de IA — Geral](vocabulario-e-sentencas-exercicio-geral.md) |
| 10:26–11:00 | 34 | Tema 1 — Exercício | Especialista | [Exercício de IA — Especialista](vocabulario-e-sentencas-exercicio-especialista.md) |
| 11:00–11:05 | 5 | Intervalo | Todos | Nenhuma |
| 11:05–11:18 | 13 | Tema 2 — Conceitos | Comum | [Tabelas de decisão e IA como formalizadora](tabelas-de-decisao-conceitos.md) |
| 11:18–11:30 | 12 | Tema 2 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](tabelas-de-decisao-exemplo-de-aplicacao-de-ia.md) |
| 11:30–11:55 | 25 | Tema 2 — Exercício | Geral | [Exercício de IA — Geral](tabelas-de-decisao-exercicio-geral.md) |
| 11:30–11:55 | 25 | Tema 2 — Exercício | Especialista | [Exercício de IA — Especialista](tabelas-de-decisao-exercicio-especialista.md) |
| 11:55–12:00 | 5 | Síntese e autoavaliação | Comum | [Síntese e referências](sintese-e-referencias.md) |

O conteúdo soma 115 minutos, e o intervalo consome os 5 restantes.

## Como conduzir

As quatro páginas de conceitos e exemplo têm caixas de destaque embutidas no texto. Pare nesses pontos, em lugar de ler a pergunta e seguir em frente.

Nenhum exercício desta sessão exige terminal, projeto executável ou execução de teste. O trabalho inteiro é ler um artefato existente (código, planilha ou prosa) e formalizar a regra que ele esconde. A trilha especialista trabalha sobre uma função de frete grátis, apresentada no próprio exercício; a trilha geral trabalha sobre a planilha de comissão, disponível em [assets/planilha-comissoes-vetor.xlsx](assets/planilha-comissoes-vetor.xlsx).

**Próxima página:** [Vocabulário e sentenças de regra: SBVR e RuleSpeak](vocabulario-e-sentencas-conceitos.md).
