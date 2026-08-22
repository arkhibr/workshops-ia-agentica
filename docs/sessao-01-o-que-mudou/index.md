# S1 — O que mudou: Software 3.0 e Engenharia Agêntica

**Bloco:** 1 — Fundamentos

## Problema

A equipe usa IA como completador de código glorificado — e não sabe o que está perdendo ao não ir além disso.

## Ao final desta sessão, o participante consegue

Diferenciar o uso ad hoc de IA (prompt improvisado, resultado imprevisível) do uso disciplinado (LLM como parceiro de execução controlado, saída previsível), e reconhecer nas próprias mãos onde o contexto explícito muda o resultado.

## Agenda da sessão (2h)

| # | Bloco | Teoria | Prática | Total |
|---|---|---|---|---|
| 1 | Diagnóstico: por que "a equipe já usa IA" não é método | 15 min | 10 min | 25 min |
| 2 | A tese do Software 3.0: a janela de contexto virou o programa | 15 min | 15 min | 30 min |
| 3 | O que sobe e o que não sobe: piso, teto, julgamento humano | 10 min | 10 min | 20 min |
| 4 | Exercício-âncora ⭐ — mesmo problema, intuição vs. prompt estruturado | 15 min | 20 min | 35 min |
| — | Pulmão | | | 10 min |
| | **Total** | **55 min** | **55 min** | **120 min** |

---

## Bloco 1 — Diagnóstico: por que "a equipe já usa IA" não é método (25 min)

### Teoria (15 min)

A disciplina de Arquitetura de Soluções com IA Generativa da Arkhi separa três modos de trabalho que a maioria dos times de desenvolvimento mistura num só:

| Modo | Artefato que governa | Como a qualidade é julgada | Risco dominante |
|---|---|---|---|
| Vibe coding | conversa corrente e resultado aparente | "parece funcionar" | intenção implícita, regressão, dívida invisível |
| Assistência de codificação | ticket, código existente, revisão do desenvolvedor | testes e revisão depois de gerar | contexto fragmentado, decisões não registradas |
| SDD (Sessão 8) | constitution, spec, plano, tarefas, testes e gates versionados | rastreabilidade entre intenção, implementação e evidência | custo de especificar sem manter os artefatos vivos |

O termo *vibe coding* vem de Andrej Karpathy, pesquisador fundador da OpenAI e ex-diretor de IA da Tesla, numa publicação de fevereiro de 2025. O motivo técnico para essa prática funcionar já existia antes do nome: Brown et al. demonstraram, no artigo que apresentou o GPT-3, que um modelo de linguagem executa uma tarefa nova a partir só da descrição em linguagem natural e de alguns exemplos no próprio texto de entrada, sem qualquer ajuste de peso. Esse mecanismo, chamado aprendizado em contexto, é o que torna um prompt capaz de funcionar como programa.

Simon Willison, que documenta práticas de desenvolvimento assistido por IA desde 2022, é específico sobre onde o uso legítimo do vibe coding termina: "vibe coding is more useful in its original definition — we need a term to describe unreviewed, prototype-quality LLM-generated code". Serve para prototipagem descartável. O problema aparece quando o time atravessa, sem perceber, a fronteira entre protótipo e produto: a conversa carrega decisões que nunca chegam ao repositório, o teste confirma só o que foi implementado, e a próxima sessão do agente não herda o raciocínio da anterior.

O próprio Karpathy documentou o limite na prática: os ganhos de velocidade do vibe coding "vanished shortly after getting local code running". A aceleração desaparece quando o código precisa integrar, ser mantido, ou sobreviver a um caso de borda fora do que o prompt original previu.

O time hoje opera majoritariamente na primeira linha da tabela, com três sintomas que costumam coexistir:

- **Inconsistente.** Alguns desenvolvedores extraem resultados excelentes do mesmo modelo que outros usam apenas como um completador de código sofisticado. A causa está em como cada um pede ao modelo.
- **Sem rede.** Código é aceito sem que quem aceitou entenda de fato o que ele faz. Quando esse código quebra em produção, não há protocolo de depuração, só tentativa e erro.
- **Ad hoc.** Não existe fluxo, vocabulário ou critério de aceitação compartilhado entre o time para o que "um bom pedido à IA" significa.

A disciplina que move o time da primeira linha para as demais também já tem nome: **engenharia agêntica**. Willison a define como "the practice of developing software with the assistance of coding agents" (Claude Code, Codex, Gemini CLI), sustentada por três responsabilidades que continuam humanas mesmo com o código escrito por um agente: especificar o problema, prover as ferramentas certas, verificar e iterar sobre o resultado. Esse é o mapa do resto do workshop: da assistência de codificação (Blocos 2 a 7) ao SDD completo (Sessão 8).

### Prática (10 min)

Autodiagnóstico individual, sem julgamento — o objetivo é ter um retrato honesto do ponto de partida, não uma nota.

→ [exercicios/exercicio-01-autodiagnostico.md](exercicios/exercicio-01-autodiagnostico.md)

---

## Bloco 2 — A tese do Software 3.0: a janela de contexto virou o programa (30 min)

### Teoria (15 min)

A arquitetura Transformer, descrita por Vaswani et al. em 2017, é a base técnica de todo LLM usado hoje em ferramentas agênticas de codificação. Ela é o que torna prática a aprendizagem em contexto do Bloco 1, e é sobre essa maturidade técnica que Karpathy constrói uma tese de fundo, apresentada na YC AI Startup School de 17 de junho de 2025: a programação teve, ao longo da história, um paradigma dominante por vez — e agora tem três coexistindo. **Software 1.0** é código explícito, escrito por humanos em linguagens de programação. **Software 2.0** são redes neurais: em vez de código, o time ajusta pesos por treinamento. **Software 3.0** é o prompt em linguagem natural funcionando como o próprio programa, interpretado por um LLM. Karpathy resume a virada numa frase que já circula como definição: "the hottest new programming language is English."

O prompt deixa de ser um pedido informal para um assistente e passa a ser a especificação executável. Tecnicamente, o que o LLM processa em cada execução é limitado pela **janela de contexto**: o limite de unidades de entrada e saída que o modelo consegue considerar. Convenções do repositório, regra de negócio e casos de borda precisam caber, de forma explícita, dentro dessa janela. O que não está lá dentro não existe para o agente — daí o título deste bloco: a janela de contexto virou o programa.

A previsão de Karpathy para a década segue a mesma lógica: "Software 3.0 is eating 1.0/2.0". Código explícito e modelos treinados não desaparecem; uma fração crescente do comportamento de um sistema passa a ser especificada diretamente em linguagem natural.

Uma segunda peça técnica separa um agente de um LLM respondendo uma pergunta isolada: a capacidade de intercalar raciocínio e ação, lendo o resultado de uma ferramenta, decidindo o próximo passo, agindo de novo. Yao et al., no artigo que introduziu o framework ReAct (2023), formalizaram esse ciclo combinando cadeia de raciocínio com execução verificável de ações. É esse ciclo de raciocínio e ação, mais do que o tamanho do modelo, que separa Claude Code ou Codex de um chat comum — e o que torna possível a *engenharia agêntica* nomeada no Bloco 1.

Essa mudança sobe três coisas ao mesmo tempo, em ritmos diferentes:

- **O piso sobe para todos.** Se a linguagem de programação é o português ou o inglês, qualquer desenvolvedor produz hoje código que compila e roda. Isso já não é diferencial.
- **O teto sobe só com disciplina.** Karpathy nomeia a lacuna: "demo is works.any(), product is works.all()". Um protótipo só precisa funcionar uma vez; um produto precisa funcionar em todos os casos que importam. Fechar essa lacuna é o *generation-verification loop* — gerar, verificar, ajustar, repetir.
- **O julgamento humano sobe de valor.** As três responsabilidades de Willison (especificar, prover ferramentas, verificar) são decisões que o modelo não toma sozinho.

Este workshop inteiro é sobre a segunda seta — fechar a lacuna entre demo e produto.

### Prática (15 min)

Duas versões do mesmo pedido, lado a lado: uma intuitiva, uma com contexto explícito. Antes do exercício-âncora do fim da sessão, este bloco serve para sentir na mão, num caso pequeno, o que "contexto explícito" quer dizer.

→ [exercicios/exercicio-02-contexto-explicito.md](exercicios/exercicio-02-contexto-explicito.md)

---

## Bloco 3 — O que sobe e o que não sobe: piso, teto, julgamento humano (20 min)

### Teoria (10 min)

A tese do Bloco 2 só é útil se o time souber reconhecer, no próprio trabalho, onde cada seta age. Willison localiza o valor humano em "figuring out *what* code to write" — navegar as decisões de arquitetura que sobram depois que o agente gera uma proposta. Um ganho de piso (o código roda) não é o mesmo que um ganho de teto (o código está correto, testável e alinhado à arquitetura do sistema), e nenhum dos dois substitui o julgamento sobre se aquele era o problema certo a resolver.

As três responsabilidades de Willison mapeiam diretamente nas três setas:

| Seta (Karpathy/Willison) | Responsabilidade que sobe de valor | Pergunta que ela responde |
|---|---|---|
| Piso sobe para todos | — | O código compila e roda? |
| Teto sobe com disciplina | Especificação + ferramental (*problem specification*, *tool provisioning*) | O código resolve exatamente o problema, nos casos de borda que importam? |
| Julgamento humano sobe de valor | Verificação (*verification and iteration*) | Esse era o problema certo? O resultado está pronto para produção, ou é só um demo que passou uma vez? |

Esse é o critério que acompanha o time no resto do workshop: diante de qualquer saída de IA, perguntar qual dessas três coisas ela resolveu — e qual ela deixou para o humano decidir.

### Prática (10 min)

Sem código novo: revisitar as duas saídas geradas no Bloco 2 e classificar, junto com a dupla, onde cada seta apareceu.

→ [exercicios/exercicio-03-onde-entrou-julgamento.md](exercicios/exercicio-03-onde-entrou-julgamento.md)

---

## Bloco 4 — Exercício-âncora: mesmo problema, intuição vs. prompt estruturado (35 min)

### Teoria / setup (15 min)

Este é o exercício que resume a sessão. O cenário é uma regra de negócio real: cálculo de desconto por volume de pedido, com uma pegadinha deliberada. A regra tem uma exceção (teto de desconto por pedido) e uma variação por tipo de cliente que um pedido vago não menciona, mas que qualquer sistema em produção precisa respeitar.

O exercício pede a mesma coisa duas vezes ao agente: primeiro com um prompt intuitivo (o tipo de pedido que qualquer desenvolvedor faria sem pensar duas vezes), depois com um prompt estruturado (contexto de domínio, assinatura-alvo, casos de borda, critério de aceitação). A comparação foca em quais requisitos da regra de negócio cada versão captura.

### Prática (20 min)

→ [exercicios/exercicio-04-intuicao-vs-estruturado/index.md](exercicios/exercicio-04-intuicao-vs-estruturado/index.md)

---

## Fontes desta sessão

- VASWANI, Ashish et al. *Attention Is All You Need*. NeurIPS, 2017.
- BROWN, Tom B. et al. *Language Models are Few-Shot Learners*. NeurIPS, 2020.
- YAO, Shunyu et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR, 2023.
- KARPATHY, Andrej. *Software Is Changing (Again)*. Palestra, YC AI Startup School, 17 jun. 2025.
- WILLISON, Simon. "What is agentic engineering?" — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026.
- Disciplina de Arquitetura de Soluções com IA Generativa (Arkhi), Módulo 4 — Agentes: distinção vibe coding / assistência de codificação / SDD, definição de janela de contexto.

Citações completas em [referencia/bibliografia.md](../referencia/bibliografia.md).

## Inventário de arquivos

| Arquivo | Descrição |
|---|---|
| `exercicios/exercicio-01-autodiagnostico.md` | Worksheet individual — classificar o próprio uso de IA hoje |
| `exercicios/exercicio-02-contexto-explicito.md` | Mesmo pedido pequeno, rodado com e sem contexto explícito |
| `exercicios/exercicio-03-onde-entrou-julgamento.md` | Reflexão em dupla sobre as saídas do Exercício 2 |
| `exercicios/exercicio-04-intuicao-vs-estruturado/index.md` | Instruções do exercício-âncora |
| `exercicios/exercicio-04-intuicao-vs-estruturado/cenario.md` | Regra de negócio completa (gabarito do instrutor) — desconto por volume |
| `exercicios/exercicio-04-intuicao-vs-estruturado/criterios-aceitacao.md` | Casos de teste para verificar as duas saídas geradas |

---

*Linguagem: exercícios funcionam em C#, JavaScript ou TypeScript — cada participante usa o stack do próprio dia a dia. Nenhum exercício desta sessão exige o domínio FUNDEP; as variações de domínio entram a partir do Bloco 3 (Execução).*
