# S4 — Regras formais com IA

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** por que a mesma regra de negócio, escrita em prosa, é lida de um jeito pelo desenvolvedor e de outro pelo agente?

## Problema

"O desconto de atacado nunca ultrapassa o teto" parece uma frase sem ambiguidade — até alguém perguntar se "o teto" é por pedido, por cliente ou por mês, e descobrir que cada pessoa do time já assumia uma resposta diferente, em silêncio.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática — cada bloco de teoria tem uma atividade correspondente logo em seguida. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** regra estrutural de regra operativa no vocabulário do SBVR.
2. **Reescrever** uma regra de negócio em prosa usando as formas de sentença do RuleSpeak.
3. **Construir** uma tabela de decisão DMN para uma regra com mais de uma condição, escolhendo a política de acerto correta.
4. **Usar** um agente de codificação como formalizador de regra — e verificar se a formalização dele preservou a intenção original.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B que atravessa o workshop, chega a esta sessão com duas regras de desconto especificadas em BR/FR na Sessão 3 (atacado e cliente recorrente), mas nenhuma delas formalizada em vocabulário controlado. Esta sessão fecha essa lacuna: da prosa BR/FR para SBVR, RuleSpeak e uma tabela de decisão que qualquer pessoa do time lê sem ambiguidade.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [SBVR: vocabulário e regras](sbvr-vocabulario-e-regras.md) | Teoria | 10 min | Distinguir regra estrutural de operativa e nomear os termos do vocabulário de um domínio |
| 2 | [RuleSpeak: três formas de sentença](rulespeak-tres-formas.md) | Teoria | 10 min | Reescrever uma regra em "deve", "não deve" ou "pode ... somente se", sem ambiguidade |
| 3 | [Tabelas de decisão e DMN](tabelas-de-decisao-dmn.md) | Teoria | 10 min | Montar uma tabela de decisão e escolher a política de acerto certa |
| 4 | [IA como formalizadora](ia-como-formalizadora.md) | Teoria | 7 min | Usar o agente para formalizar uma regra, e verificar se ele preservou a intenção |
| 5 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 10 min | Ver a regra de desconto da Vetor virar vocabulário, RuleSpeak e tabela de decisão |
| 6 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 13 min | Julgar o que aconteceu quando duas linhas de uma tabela de decisão se sobrepuseram |
| — | Intervalo | — | 5 min | — |
| 7 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 30 min | Formalizar, com IA, uma regra da Vetor ainda em prosa |
| 8 | [Exercícios](exercicios.md) | Prática avaliada | 20 min | Exercício-âncora: formalização verificada por back-translation |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As quatro páginas de teoria têm caixas de destaque embutidas no texto. Pare de verdade nesses pontos, em vez de ler a pergunta e seguir em frente.

A oficina desta sessão é inteiramente sobre formalização de regra e não exige projeto executável. Quem quiser conferir o código, monta o projeto como na oficina da Sessão 3.

**Próxima página:** [SBVR: vocabulário e regras](sbvr-vocabulario-e-regras.md).
