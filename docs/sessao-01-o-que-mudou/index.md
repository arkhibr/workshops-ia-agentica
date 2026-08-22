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
| 2 | A tese: Software 3.0 — a janela de contexto virou o programa | 15 min | 15 min | 30 min |
| 3 | O que sobe e o que não sobe: piso, teto, julgamento humano | 10 min | 10 min | 20 min |
| 4 | Exercício-âncora ⭐ — mesmo problema, intuição vs. prompt estruturado | 15 min | 20 min | 35 min |
| — | Pulmão | | | 10 min |
| | **Total** | **55 min** | **55 min** | **120 min** |

---

## Bloco 1 — Diagnóstico: por que "a equipe já usa IA" não é método (25 min)

### Teoria (15 min)

O nome preciso para o que a maioria dos times já faz é *vibe coding* — termo cunhado por Andrej Karpathy, pesquisador que liderou IA da Tesla e cofundou a OpenAI, numa publicação de fevereiro de 2025. O glossário da disciplina de Arquitetura de Soluções com IA Generativa da Arkhi define vibe coding como "a prática de pedir implementação por linguagem natural sem tornar requisitos, testes e critérios de aceite artefatos explícitos" ([Glossário — Módulo 4, Agentes](../referencia/bibliografia.md)). Não é uma gíria pejorativa — é uma prática com uso legítimo, mas um uso específico.

Simon Willison — que documenta e nomeia práticas de desenvolvimento assistido por IA desde 2022 — é direto sobre onde esse uso legítimo termina: "vibe coding is more useful in its original definition — we need a term to describe unreviewed, prototype-quality LLM-generated code" (Willison, *Agentic Engineering Patterns*, 2026). Vibe coding é ótimo para um protótipo descartável. O problema começa quando o time trata esse protótipo como produto — porque ninguém tornou explícito, em nenhum momento, o que o código deveria fazer.

O próprio Karpathy documentou o limite na prática: os ganhos de velocidade do vibe coding "vanished shortly after getting local code running" (YC AI Startup School, jun. 2025) — a aceleração desaparece assim que o código precisa integrar, ser mantido ou sobreviver a um caso de borda que o prompt original não previu.

Esse é o diagnóstico do time hoje, em três sintomas que costumam coexistir:

- **Inconsistente.** Alguns desenvolvedores extraem resultados excelentes do mesmo modelo que outros usam apenas como um completador de código sofisticado — a diferença não está no modelo, está em como cada um pede.
- **Sem rede.** Código é aceito sem que quem aceitou entenda de fato o que ele faz. Quando esse código quebra em produção, não há protocolo de depuração — só tentativa e erro.
- **Ad hoc.** Não existe um fluxo, um vocabulário ou um critério de aceitação compartilhado entre o time para o que "um bom pedido à IA" significa.

O nome para a disciplina que resolve isso — assunto do resto do workshop — também já existe: **engenharia agêntica**. Willison a define como "the practice of developing software with the assistance of coding agents" (Claude Code, Codex, Gemini CLI), sustentada por três responsabilidades que continuam humanas mesmo quando o código é escrito por um agente: especificar o problema, prover as ferramentas certas, e verificar e iterar sobre o resultado. Essas três responsabilidades — especificação, ferramental, verificação — são o mapa dos Blocos 2, 3 e 4 desta sessão, e da estrutura inteira do workshop.

### Prática (10 min)

Autodiagnóstico individual, sem julgamento — o objetivo é ter um retrato honesto do ponto de partida, não uma nota.

→ [exercicios/exercicio-01-autodiagnostico.md](exercicios/exercicio-01-autodiagnostico.md)

---

## Bloco 2 — A tese: Software 3.0 — a janela de contexto virou o programa (30 min)

### Teoria (15 min)

Karpathy apresentou essa mudança como uma tese de fundo, na YC AI Startup School de 17 de junho de 2025: a programação sempre teve, ao longo da história, um único paradigma dominante por vez — e agora tem três coexistindo. **Software 1.0** é código explícito, escrito por humanos em linguagens de programação. **Software 2.0** são redes neurais: em vez de código, o programador ajusta pesos por treinamento. **Software 3.0** é o prompt em linguagem natural funcionando como o próprio programa, interpretado por um LLM. Karpathy resume a virada numa frase que já circula como definição: "the hottest new programming language is English."

O prompt não é mais um pedido informal para um assistente — é a especificação executável. Tecnicamente, o que o LLM processa em cada execução é limitado pela **janela de contexto** — "o limite de unidades de entrada e saída que o modelo consegue considerar" (glossário da disciplina de Arquitetura de Soluções com IA Generativa da Arkhi). Na prática do desenvolvedor, isso significa que tudo que o agente sabe sobre o problema — convenções do repositório, regra de negócio, casos de borda — precisa caber, de forma explícita, dentro dessa janela. É por isso que "a janela de contexto virou o programa": o que não está lá dentro simplesmente não existe para o agente. E a previsão de Karpathy para a década é direta: "Software 3.0 is eating 1.0/2.0" — não porque código explícito e modelos treinados deixam de existir, mas porque uma fração crescente do comportamento de um sistema passa a ser especificada em linguagem natural, e não em sintaxe de linguagem de programação.

Essa mudança sobe três coisas ao mesmo tempo, mas em ritmos diferentes:

- **O piso sobe para todos.** Se a linguagem de programação é o português ou o inglês, qualquer desenvolvedor — júnior, sênior, ou alguém fora da equipe de engenharia — consegue hoje produzir código que compila e roda. Isso já não é mais diferencial.
- **O teto sobe só com disciplina.** O próprio Karpathy nomeia a lacuna: "demo is works.any(), product is works.all()" — um protótipo só precisa funcionar uma vez, um produto precisa funcionar em todos os casos que importam. Fechar essa lacuna é o que ele chama de *generation-verification loop*: gerar, verificar, ajustar, repetir — e é exatamente o método que dá disciplina ao vibe coding do Bloco 1.
- **O julgamento humano sobe de valor.** As três responsabilidades de Willison — especificar, prover ferramentas, verificar — são decisões que o modelo não toma sozinho. Quanto mais poderoso o modelo, mais caro fica errar nelas.

Este workshop inteiro é sobre a segunda seta — como fechar a lacuna entre demo e produto.

### Prática (15 min)

Duas versões do mesmo pedido, lado a lado: uma intuitiva, uma com contexto explícito. O objetivo aqui não é ainda o exercício-âncora do fim da sessão — é sentir na mão, num caso pequeno, o que "contexto explícito" quer dizer antes de aplicá-lo num caso mais complexo.

→ [exercicios/exercicio-02-contexto-explicito.md](exercicios/exercicio-02-contexto-explicito.md)

---

## Bloco 3 — O que sobe e o que não sobe: piso, teto, julgamento humano (20 min)

### Teoria (10 min)

A tese do Bloco 2 só é útil se o time souber reconhecer, no próprio trabalho, onde cada seta age. Willison é específico sobre onde o valor humano se concentra: não em escrever código, mas em "figuring out *what* code to write" e em navegar as decisões de arquitetura que sobram depois que o agente gera uma proposta. Um ganho de piso (o código roda) não é o mesmo que um ganho de teto (o código está correto, testável e alinhado à arquitetura do sistema) — e nenhum dos dois substitui o julgamento sobre se aquele era o problema certo a resolver.

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

Este é o exercício que resume a sessão. O cenário é uma regra de negócio real — cálculo de desconto por volume de pedido — com uma pegadinha deliberada: a regra tem uma exceção (teto de desconto por pedido) e uma variação por tipo de cliente que um pedido vago não menciona, mas que qualquer sistema em produção precisa respeitar.

O exercício pede a mesma coisa duas vezes ao agente — primeiro com um prompt intuitivo (o tipo de pedido que qualquer desenvolvedor faria sem pensar duas vezes), depois com um prompt estruturado (contexto de domínio, assinatura-alvo, casos de borda, critério de aceitação). A comparação não é sobre estilo de código — é sobre quais requisitos da regra de negócio cada versão captura.

### Prática (20 min)

→ [exercicios/exercicio-04-intuicao-vs-estruturado/index.md](exercicios/exercicio-04-intuicao-vs-estruturado/index.md)

---

## Fontes desta sessão

- KARPATHY, Andrej. *Software Is Changing (Again)*. Palestra, YC AI Startup School, 17 jun. 2025.
- WILLISON, Simon. "What is agentic engineering?" — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026.
- DELIMARSKY, Den. "Spec-driven development with AI: Get started with a new open source toolkit". *The GitHub Blog*, 2 set. 2025.
- Glossário controlado, disciplina de Arquitetura de Soluções com IA Generativa (Arkhi) — definições de *vibe coding*, *janela de contexto*, *agente de codificação*.

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
