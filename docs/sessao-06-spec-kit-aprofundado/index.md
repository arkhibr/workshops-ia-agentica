# S6 — Spec Kit: qualidade da spec e teste antes do código

**Bloco:** 3 — Execução

> **Pergunta-guia:** o que a spec ainda não decidiu quando o agente começa a planejar, e como saber que um teste verde testou alguma coisa?

## Problema

A Sessão 5 mostrou que o agente preenche sozinho o que o pedido do PO deixa em aberto e que o Spec Kit grava essas decisões em arquivo. Gravar não basta quando ninguém pergunta ao PO antes do plano, quando ninguém confere se os requisitos estão bem escritos antes das tarefas e quando o teste que deveria provar a regra já nasce verde. Os três comandos opcionais do Spec Kit e um princípio de teste vermelho na constitution atacam esses três pontos, cada um numa posição diferente do fluxo.

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo, sem leitura prévia obrigatória. A aula alterna explicação, demonstração e prática, e cada participante trabalha na própria máquina, com o GitHub Spec Kit 1.1.1 instalado na Sessão 5. Quem ainda não tem a ferramenta segue a [preparação do ambiente da Sessão 5](../sessao-05-decomposicao/preparacao.md).

## Os dois temas

A sessão retoma o fluxo da Sessão 5 com os três comandos que o Spec Kit apresenta como opcionais, `clarify`, `checklist` e `analyze`, e com o teste vermelho como princípio da constitution.

**Tema 1 — Qualidade da spec.** O `clarify` leva ao PO, uma pergunta por vez, as lacunas que a spec ainda tem, e o `checklist` avalia se os requisitos estão bem escritos antes de qualquer tarefa. O foco é separar a recomendação do agente da decisão de quem é dono da regra.

**Tema 2 — Teste antes do código.** A constitution exige que os testes de cada história falhem antes da implementação, o `analyze` confere a coerência entre spec, plano e tarefas sem alterar nada, e o `implement` roda por fase, com parada no vermelho. O foco é saber se o teste falhou pelo motivo certo e se ele protege a fronteira da regra.

Os exemplos e exercícios usam pedidos de um sistema de pagamentos de projetos, inspirados no domínio administrativo e financeiro da FUNDEP. A demonstração usa a dupla aprovação de pagamentos e os exercícios usam o saldo da rubrica. O [contexto da prática](contexto-da-pratica.md) reúne os pedidos do PO, a constitution da sessão e o objetivo de cada página prática.

## Objetivos de aprendizagem

Ao final da sessão, o participante será capaz de:

1. **Executar** o fluxo do Spec Kit com `clarify`, `checklist` e `analyze` nas posições que a ferramenta indica.
2. **Distinguir** a recomendação do agente da decisão do PO numa pergunta do `clarify`.
3. **Avaliar** a escrita dos requisitos com um checklist, sem confundi-lo com teste do código.
4. **Interpretar** o relatório do `analyze` pela severidade dos achados.
5. **Verificar** que o teste falha antes da implementação e pelo motivo certo.
6. **Demonstrar** que um teste protege a fronteira de uma regra, alterando a comparação e vendo o teste falhar.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Página | Produto do bloco |
|---|---:|---|---|---|
| Durante a prática | — | Consulta | [Contexto da prática](contexto-da-pratica.md) | Pedidos do PO, constitution e objetivo de cada página prática |
| 10:00–10:15 | 15 | Kahoot | Nenhuma | Respostas registradas no Kahoot |
| 10:15–10:27 | 12 | Tema 1 — Conceitos | [Qualidade da spec: clarify e checklist](qualidade-da-spec-conceitos.md) | Posição dos comandos opcionais, limite do `clarify` e checklist como teste de requisitos |
| 10:27–10:35 | 8 | Tema 1 — Exemplo de aplicação de IA | [Exemplo de aplicação de IA](qualidade-da-spec-exemplo-de-aplicacao-de-ia.md) | Duas perguntas do `clarify` e as decisões que ficaram fora delas |
| 10:35–11:00 | 25 | Tema 1 — Exercício | [Exercício de IA: a spec do saldo da rubrica](qualidade-da-spec-exercicio.md) | Spec esclarecida, checklist gerado e três respostas |
| 11:00–11:05 | 5 | Intervalo | Nenhuma | Nenhum |
| 11:05–11:17 | 12 | Tema 2 — Conceitos | [Teste antes do código: analyze e teste vermelho](teste-antes-do-codigo-conceitos.md) | Princípio de teste vermelho, `analyze` como portão e fronteira protegida |
| 11:17–11:25 | 8 | Tema 2 — Exemplo de aplicação de IA | [Exemplo de aplicação de IA](teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md) | Achado crítico do `analyze`, vermelho conferido e verde |
| 11:25–11:55 | 30 | Tema 2 — Exercício | [Exercício de IA: do vermelho à fronteira do saldo](teste-antes-do-codigo-exercicio.md) | Saldo implementado, vermelho conferido e fronteira testada |
| 11:55–12:00 | 5 | Síntese e autoavaliação | [Síntese e referências](sintese-e-referencias.md) | Autoavaliação e apresentação da tarefa |
| Depois da aula | — | Tarefa obrigatória | [Tarefa entre sessões](tarefa-entre-sessoes.md) | Relatório do `analyze` e diff do `clarify` da ordem de compra |

O conteúdo soma 100 minutos depois do Kahoot, e o intervalo das 11:00 às 11:05 completa os 120 minutos de relógio.

## Como conduzir

Durante o Kahoot, cada participante confere se o `specify version` responde `1.1.1`. Quem chegou sem a instalação resolve nesse intervalo, com a tabela de problemas comuns da preparação da Sessão 5.

No ensaio de 13/10/2026, os comandos levaram de 20 segundos a pouco mais de 3 minutos cada. O exercício do Tema 1 somou cerca de 9 minutos e meio de espera do agente, e o do Tema 2 cerca de 11 minutos. Nos exercícios, a espera é o tempo de responder às perguntas da página. O ciclo completo da demonstração passa de 18 minutos, e por isso os exemplos mostram os artefatos gerados antes da aula nos comandos mais longos.

Os exercícios pedem a leitura de seções específicas dos artefatos, nunca do arquivo inteiro, porque a spec passa de cem linhas e o `tasks.md` passa de duzentas.

!!! warning "Limite da IA nesta sessão"
    O `clarify` pergunta apenas o que o agente considera em aberto. Uma decisão que a spec já tomou sozinha, como declarar um caso fora do escopo, não passa pelo `clarify`, e só a leitura das suposições e do escopo a encontra. O `analyze` aponta incoerências entre os artefatos, e quem decide quais delas corrigir é o participante.

**Próxima página:** [Contexto da prática](contexto-da-pratica.md).
