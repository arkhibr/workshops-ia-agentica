# Estudo de caso

Um dilema sem resposta prescrita, para discussão em grupo. O caso é fictício, e a situação é comum o bastante para que alguém do grupo reconheça alguma parte dela.

## O incidente

A Meridiano é uma empresa de logística com quatro times de produto. Há oito meses adotou desenvolvimento guiado por especificação com o Spec Kit, com constitution, especificação, plano e tarefas versionados, e três portões humanos por mudança relevante.

A adoção foi considerada um sucesso interno. As métricas do trimestre mostram 94% das mudanças com especificação aprovada antes da implementação, 100% dos planos aprovados no portão de arquitetura e nenhuma mudança relevante integrada sem revisão de aderência. A liderança apresentou os números na reunião trimestral.

Na quinta-feira, um cliente contesta uma cobrança. A investigação mostra que o cálculo de frete para entregas interestaduais com carga refrigerada estava errado desde a implementação, cinco meses antes. O erro afetou 1.847 entregas, com prejuízo estimado em R$ 210 mil.

O ciclo daquela mudança está todo lá. A especificação tem catorze requisitos funcionais numerados, cada um com caso concreto. O plano registra três decisões e duas alternativas descartadas. As tarefas são fatias verticais, com definição de pronto. Os três portões têm aprovação nominal, com data e responsável. A revisão de aderência registra "todos os requisitos verificados, sem desvio".

O requisito FR-009 dizia: "o sistema deve aplicar a taxa de refrigeração sobre o valor base do frete". O código aplica a taxa sobre o valor base. O teste verifica que a taxa é aplicada sobre o valor base, e passa.

A regra de negócio real, que consta na tabela de preços acordada com o cliente e nunca foi lida por ninguém do time, aplica a taxa de refrigeração sobre o valor base **mais** o adicional interestadual.

## O ponto de falha

Nenhuma etapa foi pulada. Nenhum artefato está desatualizado. O rastro de FR-009 até o teste está íntegro e navegável nos dois sentidos. A revisão de aderência fez exatamente o que deveria: conferiu o código contra a especificação, e eles correspondem.

O erro entrou na especificação, e o processo inteiro se encarregou de implementá-lo com fidelidade.

## Perguntas para orientar a discussão

1. Qual portão deveria ter pegado esse erro? Se a resposta for "nenhum dos três", que portão estaria faltando, e qual seria o custo de tê-lo em toda mudança?

2. As métricas do trimestre diziam que a adoção foi bem-sucedida. Elas estavam erradas, ou estavam medindo a coisa certa e a coisa certa não é suficiente? Que indicador teria sinalizado esse risco antes do incidente?

3. A revisão de aderência aprovou porque código e especificação correspondiam. Quem, no fluxo descrito, tinha a responsabilidade de revisar a especificação contra a realidade do negócio? Essa autoridade estava nomeada em algum lugar?

4. O time usou um agente para redigir a especificação a partir de uma conversa com a área comercial. Se um humano tivesse escrito os catorze requisitos, o erro seria menos provável? O que muda, e o que não muda?

5. A tabela de preços acordada com o cliente existia como documento, e ninguém do time a leu. Isso é falha de processo de especificação, de acesso à informação, ou de outra coisa? Onde essa fonte deveria ter entrado no ciclo?

6. Depois do incidente, alguém propõe acrescentar um quarto portão, de validação da especificação por uma pessoa da área de negócio, em toda mudança. Quais mudanças passariam a esperar por essa validação, e o que acontece com o tempo de entrega das que não têm risco financeiro?

7. Cinco meses se passaram entre a implementação e a descoberta. Que mecanismo, fora do ciclo de desenvolvimento, teria encurtado esse intervalo?

## Para fechar a discussão

Uma cadeia de artefatos coerente prova que a implementação corresponde à intenção registrada. Ela não prova, e não tem como provar, que a intenção registrada corresponde à necessidade real.

A pergunta que fica para o grupo é onde, no fluxo de cada um, essa segunda verificação acontece hoje, e quem tem autoridade para reprovar por esse motivo.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
