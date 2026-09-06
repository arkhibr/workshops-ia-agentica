# Avaliação de modelos

Escolher um modelo para tarefas de engenharia de software exige ler benchmark com critério, porque o número divulgado depende tanto da forma como o teste foi conduzido quanto do modelo medido. Cinco critérios de leitura e um placar de referência.

<a id="como-avaliar-modelos-para-engenharia-de-software"></a>

Escolher um modelo pelo nome mais falado do momento é o mesmo erro de raiz do vibe coding: aceitar sem verificar. Cinco critérios tornam essa escolha uma decisão, não uma torcida.

**Use um benchmark que meça o trabalho real, não a função isolada.** O HumanEval (Chen et al., 2021) mede se o modelo escreve uma função correta a partir de um enunciado — útil, mas distante do que a Sessão 8 chama de engenharia agêntica. Um benchmark como o DeepSWE mede se o agente resolve uma tarefa real, de longo horizonte, dentro de um repositório existente: localizar a causa, editar os arquivos certos, passar num verificador automático. É o tipo de medida mais próximo do trabalho que um time de engenharia de software faz no dia a dia.

**Prefira tarefas verificadas por programa a julgamento humano de "parece bom".** O DeepSWE verifica cada uma das 113 tarefas por execução de programa, não por alguém lendo o diff e achando que ficou razoável. Isso remove subjetividade do resultado: ou o teste passa, ou não passa.

**Desconfie de benchmark saturado.** Quando os modelos de fronteira empatam a menos de um ponto percentual de diferença entre si, o benchmark provavelmente está perto do teto para aquela classe de modelo. O DeepSWE, em agosto de 2026, ainda separa o primeiro colocado do quinto por 4,6 pontos e o top 10 inteiro por 8,3 pontos — sinal de que ainda há distinção real de capacidade para medir, não um empate técnico disfarçado de ranking.

**Desconfie de número autorreportado por quem vende o modelo.** Fabricantes escolhem qual benchmark divulgar no anúncio de lançamento, e às vezes trocam de benchmark de uma versão para a outra sem explicar por quê. Prefira leitores independentes que avaliam todos os fabricantes sob o mesmo arnês de teste, na mesma data — é exatamente o que o DeepSWE (mantido pela Datacurve, publicado em benchlm.ai) faz: roda Claude, GPT e modelos abertos como o GLM lado a lado, sem depender do número que cada fabricante escolheu anunciar.

**Nota do placar não é a decisão inteira.** Custo por tarefa resolvida, latência, tamanho da janela de contexto e confiabilidade dentro do seu ambiente agêntico específico pesam tanto quanto o resolve rate — um modelo 3 pontos percentuais à frente, mas 5 vezes mais caro por tarefa, raramente compensa para o dia a dia de um time.

## Placar de referência — DeepSWE

| Modelo | Organização | DeepSWE |
|---|---|---|
| Claude Opus 5 | Anthropic | 73,6% |
| GPT-5.6 Sol | OpenAI | 72,7% |
| Claude Fable 5 | Anthropic | 69,7% |
| GPT-5.6 Terra | OpenAI | 69,6% |
| GLM-5.3 | Z.AI | 69,0% |

Fonte: [benchlm.ai — DeepSWE](https://benchlm.ai/benchmarks/deepswe), atualizado em 20 de agosto de 2026, 25 modelos avaliados: 113 tarefas de longo horizonte, tiradas de 91 repositórios open source ativos em 5 linguagens, verificadas por programa.

**Este placar envelhece rápido**: confira o [DeepSWE Leaderboard](https://benchlm.ai/benchmarks/deepswe) atualizado antes de decidir, não confie em número congelado numa página de workshop.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
