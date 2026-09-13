# Síntese e referências

## Nove ideias essenciais

1. **A especificação é o artefato que gera a implementação**, e o código é uma das implementações possíveis daquela intenção, condicionada por arquitetura e momento.
2. **A constitution diz o que nenhuma mudança pode violar**, enquanto a especificação diz o que esta mudança deve fazer. Um princípio que não rejeita nenhuma mudança plausível é decoração.
3. **A separação entre o quê e o como tem função prática.** Manter tecnologia fora da especificação permite comparar arquiteturas sem reescrever o problema e trocar a implementação preservando os critérios.
4. **A fatia vertical entrega evidência a cada passo.** A horizontal acumula trabalho sem trajetória verificável: depois de quatro de cinco tarefas horizontais, ninguém consegue demonstrar nada.
5. **A verificação tem dois eixos independentes.** Aderência à especificação e qualidade da implementação respondem perguntas diferentes, e força num eixo não compensa fraqueza no outro.
6. **O Spec Kit é uma implementação entre várias do padrão.** OpenSpec organiza por mudança, SPDD comprime tudo num prompt estruturado, Superpowers disciplina a execução sem manter especificação principal.
7. **Documentação e rigor operacional são eixos diferentes.** Chamar uma abordagem de leve ou pesada sem dizer em qual eixo esconde onde o custo aparece.
8. **Profundidade proporcional ao risco.** Classificar pelo maior risco, não pelo tamanho da diferença. Uma linha que altera autorização carrega mais risco que duzentos arquivos que mudam formato.
9. **A cadeia coerente prova que a implementação corresponde à intenção registrada.** Ela não prova que a intenção registrada corresponde à necessidade real, e essa segunda verificação precisa de dono.

## Checklist antes de encerrar a sessão

- [ ] Consigo nomear os quatro artefatos e o que cada um decide.
- [ ] Sei distinguir *spec-first*, *spec-anchored* e *spec-as-source* na prática de um time.
- [ ] Consigo classificar uma mudança como S, M ou L pelo risco, e justificar.
- [ ] Sei escrever um princípio de constitution com consequência nomeada.
- [ ] Reconheço os antipadrões, especialmente a aprovação automática pelo mesmo agente.
- [ ] Sei que indicadores observar num piloto, e por que volume gerado não é um deles.

## Autoavaliação

Responda para si, sem anotar:

1. No seu projeto atual, se alguém perguntasse por que uma regra de precificação existe, onde estaria a resposta? Em quanto tempo você a encontraria?
2. Quantas das mudanças que você entregou no último mês teriam sido classificadas como L pela régua de profundidade, e quantas receberam tratamento de L?
3. A última vez que você corrigiu o agente numa conversa, essa correção entrou em algum artefato versionado, ou valeu só para aquela sessão?
4. Qual dos nove antipadrões está mais perto de acontecer no seu time hoje?

## Conexão com a próxima sessão

Esta sessão fechou o ciclo do pedido ao código verificado. A [Sessão 9](../sessao-09-depuracao-sistematica/index.md) trata do que acontece quando o código verificado apresenta comportamento inesperado depois: depuração sistemática por hipótese e investigação, em vez de tentativa e erro conduzida pelo agente.

A ligação entre as duas é direta. Um defeito encontrado em produção não termina no remendo que restaura o serviço: ele volta para o requisito e para o teste de regressão, como a página sobre [artefatos vivos](artefatos-vivos.md) argumentou. A depuração produz a informação, e o ciclo desta sessão é onde ela se deposita.

## Fundamentação

O ciclo de oito etapas e os quatro artefatos canônicos seguem o [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit), com o post de lançamento de [Delimarsky](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025) para a formulação da especificação como contrato de comportamento.

A taxonomia *spec-first*, *spec-anchored* e *spec-as-source* é de [Böckeler](../referencia/bibliografia.md#bockeler-understanding-spec-driven-development-2025), que compara Kiro, Spec Kit e Tessl e argumenta que ferramentas distintas não são equivalentes só porque produzem Markdown.

As três abordagens comparadas ao Spec Kit vêm de suas fontes primárias: [OpenSpec](../referencia/bibliografia.md#fission-ai-openspec) para a mudança como unidade com especificação-delta, [Zhang e Xia](../referencia/bibliografia.md#zhang-e-xia-structured-prompt-driven-development-2026) para o SPDD e o Painel REASONS, com a implementação de referência em [OpenSPDD](../referencia/bibliografia.md#gszhangwei-openspdd), e [Vincent e Prime Radiant](../referencia/bibliografia.md#vincent-e-prime-radiant-superpowers-2026) para o Superpowers.

A distinção entre vibe coding, assistência de codificação e desenvolvimento guiado por especificação, retomada aqui, foi estabelecida na [Sessão 1](../sessao-01-o-que-mudou/modos-de-trabalho.md) a partir de [Karpathy](../referencia/bibliografia.md#karpathy-software-is-changing-again-2025) e [Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026).

Os exemplos de artefatos, o caso da Vetor e o caso da Meridiano no estudo de caso são fictícios, construídos para esta sessão. Os números do estudo de caso não correspondem a nenhuma organização real.
