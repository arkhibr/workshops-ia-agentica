# Estudo de caso: a proibição total

**Tempo:** 15 min · **Formato:** 8 min em grupos de 3–4 pessoas, 7 min de plenária.

## Situação

A Vetor, plataforma fictícia de e-commerce B2B usada como caso desta sessão, acabou de ter dois incidentes causados por código gerado sem revisão. O tech lead do time propõe em reunião: "a partir de hoje, proibido vibe coding no time. Toda linha gerada por IA passa por especificação completa, com plano e tarefas revisados antes de qualquer código." A proposta vale para tudo — desde a correção de um script interno de uma linha até uma nova rota de pagamento.

Parte do time apoia, cansada de código quebrado sem explicação. Outra parte teme que a burocracia mate exatamente a velocidade que trouxe a IA para o time em primeiro lugar.

## Como usar este estudo de caso

Não existe uma resposta única aqui. O objetivo é praticar o critério da tabela de [Padrões e decisões](padroes-e-decisoes.md#quando-cada-modo-se-justifica) num caso ambíguo de verdade, antes de aplicá-lo num código real na oficina.

## Perguntas para orientar a análise

1. Usando a tabela de critérios (reversibilidade, tempo de vida, quantas pessoas mexem depois, regra de negócio envolvida), existe alguma tarefa do dia a dia da Vetor para a qual vibe coding continua sendo a escolha certa mesmo depois do incidente?
2. O tech lead está resolvendo o problema certo? Os dois incidentes foram causados pela ausência de especificação, ou pela ausência de revisão antes do merge? A resposta muda a solução proposta?
3. Que critério objetivo (não "bom senso") o time poderia usar para decidir, tarefa por tarefa, se exige SDD completo, assistência de codificação, ou permite vibe coding?
4. Se você fosse a pessoa que precisa aplicar essa política amanhã de manhã, o que perguntaria ao tech lead antes de concordar?

## Depois da discussão

Compare a posição que o grupo chegou com a tabela de [Padrões e decisões](padroes-e-decisoes.md#quando-cada-modo-se-justifica). A esteira completa de engenharia agêntica (Sessão 10) volta a esse mesmo dilema com uma ferramenta mais precisa: decisões arquiteturais registradas em ADR, permitindo que a proporcionalidade fique explícita em vez de depender de memória ou de regra geral.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
