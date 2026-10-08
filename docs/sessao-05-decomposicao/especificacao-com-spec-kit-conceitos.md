# Especificação com Spec Kit: constitution e spec

Esta página apresenta o GitHub Spec Kit, ferramenta de linha de comando que conduz um agente de codificação por uma sequência fixa de artefatos versionados, e trata dos dois primeiros: a constitution, que guarda os princípios do projeto, e a spec, que descreve o que uma mudança precisa fazer e por quê. O código vem depois, na segunda metade da sessão.

## Onde o Spec Kit entra

A [Sessão 1](../sessao-01-o-que-mudou/modos-de-trabalho.md) separou três modos de trabalho com IA pelo artefato que governa a qualidade. No vibe coding, o que governa é a conversa e o resultado aparente. Na assistência de codificação, é a revisão do desenvolvedor sobre uma tarefa pontual. No desenvolvimento orientado por especificação (SDD, *Spec-Driven Development*), é uma especificação versionada, que existe antes do código e sobrevive à conversa que o produziu.

O [Spec Kit](../referencia/bibliografia.md#github-spec-kit) é uma implementação desse terceiro modo, publicada pelo GitHub em setembro de 2025. No post de lançamento, [Delimarsky](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025) descreve a especificação como o contrato de como o código deve se comportar. Por dentro, a ferramenta tem três peças:

| Peça | Onde fica | O que faz |
|---|---|---|
| Templates | `.specify/templates/` | Esqueleto de cada artefato, com seções obrigatórias e instruções ao agente em comentários |
| Scripts | `.specify/scripts/` | Criam a pasta da mudança, numeram a feature e localizam os arquivos |
| Comandos | `.claude/skills/`, `.agents/skills/` ou `.github/skills/`, conforme o agente | Prompts estruturados que leem o template, chamam o script e preenchem o artefato |

Nenhuma dessas peças executa raciocínio próprio. Quem escreve cada artefato é o agente que você já usa, e o Spec Kit impõe a ordem, o formato e o lugar onde o resultado fica gravado.

## O caminho básico

Ao terminar o `specify init`, a versão 1.1.1 imprime dois painéis. O primeiro, *Next Steps*, lista o caminho básico. O segundo, *Enhancement Skills*, lista comandos opcionais que entram na Sessão 6.

| Comando | Decide | Grava |
|---|---|---|
| `constitution` | Os princípios que nenhuma mudança pode violar | `.specify/memory/constitution.md` |
| `specify` | O que a mudança faz e por quê, sem tecnologia | `specs/NNN-nome/spec.md` |
| `plan` | Como a mudança será construída, e se o desenho respeita a constitution | `plan.md` e documentos de apoio |
| `tasks` | A sequência de tarefas executáveis | `tasks.md` |
| `implement` | Nada novo: executa as tarefas na ordem | código e testes |

A ordem importa porque cada comando lê o que os anteriores gravaram. O `plan` lê a spec e a constitution, o `tasks` lê o plano e a spec, e o `implement` lê as tarefas. Um erro que entra na spec chega ao código pelo caminho mais curto possível, passando por três comandos que o tratam como premissa.

![Diagrama horizontal intitulado Caminho básico do Spec Kit: cada comando lê o que os anteriores gravaram. Cinco caixas numeradas ligadas por setas: 1, constitution, princípios que nenhuma mudança pode violar, grava .specify/memory/constitution.md; 2, specify, o que a mudança faz e por quê, sem tecnologia, grava specs/NNN-nome/spec.md; 3, plan, como construir e se respeita os princípios, grava plan.md e documentos de apoio; 4, tasks, a sequência de tarefas executáveis, grava tasks.md; 5, implement, nenhuma decisão nova, executa as tarefas e produz código e testes. Um arco tracejado acima liga a constitution ao plan, com o rótulo Constitution Check. Outro arco abaixo liga a spec ao tasks, com o rótulo tasks relê a spec para montar as histórias. Chaves agrupam constitution e specify no Tema 1 e plan, tasks e implement no Tema 2. Uma faixa inferior diz que um erro gravado na spec chega ao código passando por plan, tasks e implement, que o tratam como premissa.](assets/caminho-basico-spec-kit.png)

O prefixo do comando muda com o agente. Claude Code e GitHub Copilot usam `/speckit-specify`, e o Codex CLI usa `$speckit-specify`. A documentação do projeto ainda mostra a forma antiga, com ponto (`/speckit.specify`), e o nome que vale é o que o painel imprimiu na sua máquina.

## Constitution

A constitution reúne os princípios do projeto que valem para todas as mudanças. Ela fica num arquivo próprio e é relida por todos os comandos seguintes. O template do plano tem uma seção, *Constitution Check*, marcada como portão: o agente precisa confrontar o desenho com cada princípio antes de seguir, e registrar a justificativa quando algum deles for violado.

Um princípio útil muda o que o agente gera. "O código deve ser limpo e bem testado" não muda nada, porque qualquer saída pode alegar que cumpre. "Cada requisito funcional ganha um teste que falha antes da implementação" muda: o `tasks` passa a gerar tarefas de teste e uma tarefa de ver o teste falhar, que o template, sozinho, trata como opcionais.

O teste prático para um princípio é removê-lo e perguntar o que deixaria de aparecer na spec, no plano ou nas tarefas. Se a resposta for nada, o princípio é decoração.

Três princípios bem escolhidos rendem mais que dez genéricos. Cada princípio a mais é um item a confrontar em todo plano, e uma lista longa ensina o agente a passar pelo portão sem ler.

## Spec

A spec descreve o comportamento esperado na linguagem do negócio, sem nomear arquivo, linguagem ou biblioteca. O template da versão 1.1.1 tem seis partes:

| Seção | Conteúdo | O que conferir |
|---|---|---|
| Histórias de usuário | Jornadas priorizadas (P1, P2, P3), cada uma testável sozinha, com cenários *Given/When/Then* | Cada história entrega algo que se demonstra sem as outras |
| Casos de borda | Limites e situações de erro | Os limites numéricos aparecem com o valor exato |
| Requisitos funcionais | `FR-001`, `FR-002`, no padrão "o sistema deve..." | Cada FR tem uma origem identificável |
| Entidades | Os conceitos do domínio e suas relações | Os nomes batem com o vocabulário do negócio |
| Critérios de sucesso | `SC-001`, mensuráveis e sem tecnologia | Cada critério se verifica com um teste ou uma medida |
| Suposições | Decisões tomadas onde o pedido foi omisso | Nenhuma decide uma regra de negócio |

O template também prevê o marcador `[NEEDS CLARIFICATION]` para o requisito que o agente não conseguiu fechar. Na prática ele aparece pouco, porque o agente costuma preferir decidir e registrar a decisão em *Assumptions*.

## Onde a spec decide sozinha

O comentário do template para a seção *Assumptions* pede ao agente que registre os "padrões razoáveis escolhidos quando a descrição não especificou" algum detalhe. É uma instrução honesta, e cria um efeito previsível: tudo o que o pedido deixou em aberto vira suposição, e a suposição é escrita no mesmo tom das regras.

Algumas suposições são técnicas e inofensivas, como assumir que o tipo de cliente chega em minúsculas porque o projeto já convenciona assim. Outras decidem o negócio. Se a regra diz "acima de R$ 3.000,00" e a spec registra que o valor exato não conta, alguém decidiu o que acontece no limite. Pode ser a leitura certa, mas quem decidiu foi o agente.

O critério para separar as duas é o efeito sobre um resultado calculado. Uma suposição que muda um valor de saída, um limite ou quem tem direito a quê é regra de negócio, e volta para quem é dono da regra antes de seguir para o plano. As demais podem ficar.

O mesmo vale para os critérios de sucesso. O template pede métricas mensuráveis, e um agente sem métrica no pedido tende a inventar uma plausível. Um critério que não tem origem no pedido nem no mapa de regras precisa sair da spec ou ganhar um dono.

## Da regra ao requisito

A [Sessão 4](../sessao-04-regras-formais-com-ia/sintese-e-referencias.md) terminou com regras atômicas identificadas por ID (`RC` para regra de classificação, `RD` para regra de derivação, `RN` para regra operativa) e prometeu que a decomposição preservaria a ligação de cada tarefa com a regra de origem. O Spec Kit não conhece esses IDs. Ele numera requisitos funcionais (`FR-001`) e histórias (`US1`), e a cadeia termina aí.

A ligação só existe se a constitution exigir. Um princípio de rastreabilidade, como "toda regra implementada cita o ID de origem no requisito, no teste e no comentário do código", obriga o agente a escrever `FR-003 (RN-11)` na spec e a repetir o ID no nome do teste e no código. Depois disso, verificar a cadeia é uma busca textual.

![Diagrama intitulado Rastreabilidade por ID: a constitution cria a cadeia e a busca a percorre. Quatro caixas em sequência: Regra de origem, do mapa de regras da Sessão 4, com o ID RN-11; Requisito, na spec.md, escrito FR-003 (RN-11); Teste, com o nome test("RN-11: ..."); e Código, com o comentário // RN-11. Acima, uma faixa com o princípio de rastreabilidade da constitution, que exige o ID no requisito, no teste e no código, ligada por setas tracejadas a esses três elos. Uma nota à esquerda diz que, sem o princípio, a numeração do Spec Kit para em FR-003 e US1 e o ID da regra se perde. Abaixo, uma caixa diz que, quando a regra muda, uma busca textual pelo ID devolve os três elos, com os comandos grep -rn "RN-11" specs test src e Get-ChildItem specs, test, src -Recurse -File | Select-String "RN-11", e setas sobem dela até o requisito, o teste e o código.](assets/rastreabilidade-por-id.png)

O ganho aparece quando a regra muda. Se o negócio altera um limite, a busca pelo ID devolve o requisito, o teste e a linha de código que dependem dele. Sem o ID, alguém precisa reler a spec inteira e adivinhar.

**Próxima página:** [Exemplo de aplicação de IA](especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md).
