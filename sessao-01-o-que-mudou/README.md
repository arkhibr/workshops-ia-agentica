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

Todo time de desenvolvimento hoje já usa IA. Isso não é o problema — é o ponto de partida. O problema é que o uso é ad hoc: cada desenvolvedor improvisa o próprio jeito de pedir código ao LLM, sem vocabulário, ritual ou contrato compartilhados com o resto do time.

Esse uso ad hoc se manifesta de três formas, que costumam coexistir no mesmo time:

- **Inconsistente.** Alguns desenvolvedores extraem resultados excelentes do mesmo modelo que outros usam apenas como um completador de código sofisticado — a diferença não está no modelo, está em como cada um pede.
- **Sem rede.** Código é aceito sem que quem aceitou entenda de fato o que ele faz. Quando esse código quebra em produção, não há protocolo de depuração — só tentativa e erro.
- **Ad hoc.** Não existe um fluxo, um vocabulário ou um critério de aceitação compartilhado entre o time para o que "um bom pedido à IA" significa.

O resultado é desigual: a mesma ferramenta produz efeitos muito diferentes, dependendo de quem a usa. Esse workshop existe para fechar essa distância — não trazendo uma ferramenta nova, mas um método.

### Prática (10 min)

Autodiagnóstico individual, sem julgamento — o objetivo é ter um retrato honesto do ponto de partida, não uma nota.

→ [exercicios/exercicio-01-autodiagnostico.md](exercicios/exercicio-01-autodiagnostico.md)

---

## Bloco 2 — A tese: Software 3.0 — a janela de contexto virou o programa (30 min)

### Teoria (15 min)

A mudança de fundo é esta: o LLM é o interpretador, e o desenvolvedor escreve em linguagem natural. O que antes era arte ou intuição — saber pedir a coisa certa, da forma certa — agora é engenharia: especificação, decomposição, verificação. A janela de contexto do agente é, na prática, o programa que ele vai executar.

Essa mudança sobe três coisas ao mesmo tempo, mas em ritmos diferentes:

- **O piso sobe para todos.** Qualquer desenvolvedor, com qualquer nível de experiência, consegue hoje produzir código que compila e roda. Isso já não é mais diferencial.
- **O teto sobe só com disciplina.** Quem domina o método — dar contexto explícito, especificar antes de pedir, verificar antes de aceitar — extrai da mesma ferramenta um resultado muito superior. Essa diferença não aparece sozinha; ela é construída.
- **O julgamento humano sobe de valor.** Gosto, especificação e arquitetura são exatamente as decisões que o modelo não toma por conta própria. Quanto mais poderosa a ferramenta, mais caro fica um julgamento ruim sobre o que pedir a ela.

Este workshop inteiro é sobre a segunda seta — como construir o teto.

### Prática (15 min)

Duas versões do mesmo pedido, lado a lado: uma intuitiva, uma com contexto explícito. O objetivo aqui não é ainda o exercício-âncora do fim da sessão — é sentir na mão, num caso pequeno, o que "contexto explícito" quer dizer antes de aplicá-lo num caso mais complexo.

→ [exercicios/exercicio-02-contexto-explicito.md](exercicios/exercicio-02-contexto-explicito.md)

---

## Bloco 3 — O que sobe e o que não sobe: piso, teto, julgamento humano (20 min)

### Teoria (10 min)

A tese do Bloco 2 só é útil se o time souber reconhecer, no próprio trabalho, onde cada seta age. Nem todo ganho de produtividade é igual: um ganho de piso (o código funciona) não é o mesmo que um ganho de teto (o código está correto, testável e alinhado à arquitetura do sistema) — e nenhum dos dois substitui o julgamento sobre se aquele era o problema certo a resolver.

Esse é o critério que vai acompanhar o time no resto do workshop: perguntar, diante de qualquer saída de IA, qual dessas três coisas ela resolveu — e qual ela deixou para o humano decidir.

### Prática (10 min)

Sem código novo: revisitar as duas saídas geradas no Bloco 2 e classificar, junto com a dupla, onde cada seta apareceu.

→ [exercicios/exercicio-03-onde-entrou-julgamento.md](exercicios/exercicio-03-onde-entrou-julgamento.md)

---

## Bloco 4 — Exercício-âncora: mesmo problema, intuição vs. prompt estruturado (35 min)

### Teoria / setup (15 min)

Este é o exercício que resume a sessão. O cenário é uma regra de negócio real — cálculo de desconto por volume de pedido — com uma pegadinha deliberada: a regra tem uma exceção (teto de desconto por pedido) e uma variação por tipo de cliente que um pedido vago não menciona, mas que qualquer sistema em produção precisa respeitar.

O exercício pede a mesma coisa duas vezes ao agente — primeiro com um prompt intuitivo (o tipo de pedido que qualquer desenvolvedor faria sem pensar duas vezes), depois com um prompt estruturado (contexto de domínio, assinatura-alvo, casos de borda, critério de aceitação). A comparação não é sobre estilo de código — é sobre quais requisitos da regra de negócio cada versão captura.

### Prática (20 min)

→ [exercicios/exercicio-04-intuicao-vs-estruturado/README.md](exercicios/exercicio-04-intuicao-vs-estruturado/README.md)

---

## Inventário de arquivos

| Arquivo | Descrição |
|---|---|
| `exercicios/exercicio-01-autodiagnostico.md` | Worksheet individual — classificar o próprio uso de IA hoje |
| `exercicios/exercicio-02-contexto-explicito.md` | Mesmo pedido pequeno, rodado com e sem contexto explícito |
| `exercicios/exercicio-03-onde-entrou-julgamento.md` | Reflexão em dupla sobre as saídas do Exercício 2 |
| `exercicios/exercicio-04-intuicao-vs-estruturado/README.md` | Instruções do exercício-âncora |
| `exercicios/exercicio-04-intuicao-vs-estruturado/cenario.md` | Regra de negócio completa (gabarito do instrutor) — desconto por volume |
| `exercicios/exercicio-04-intuicao-vs-estruturado/criterios-aceitacao.md` | Casos de teste para verificar as duas saídas geradas |

---

*Linguagem: exercícios funcionam em C#, JavaScript ou TypeScript — cada participante usa o stack do próprio dia a dia. Nenhum exercício desta sessão exige o domínio FUNDEP; as variações de domínio entram a partir do Bloco 3 (Execução).*
