# Avaliação de modelos

Escolher um modelo para tarefas de engenharia de software exige ler *benchmark* com critério, porque o número divulgado depende tanto da forma como o teste foi conduzido quanto do modelo medido. Cinco critérios de leitura e um placar de referência.

<a id="como-avaliar-modelos-para-engenharia-de-software"></a>

Escolher um modelo pelo nome mais falado do momento é o mesmo erro de raiz do vibe coding: aceitar sem verificar. Cinco critérios tornam essa escolha uma decisão, não uma torcida.

**Use um benchmark que meça o trabalho real, não a função isolada.** O HumanEval (Chen et al., 2021) mede se o modelo escreve uma função correta a partir de um enunciado — útil, mas distante do que a Sessão 8 chama de engenharia agêntica. Um benchmark como o DeepSWE mede se o agente resolve uma tarefa real, de longo horizonte, dentro de um repositório existente: localizar a causa, editar os arquivos certos, passar num verificador automático. É o tipo de medida mais próximo do trabalho que um time de engenharia de software faz no dia a dia.

**Prefira tarefas verificadas por programa a julgamento humano de "parece bom".** O DeepSWE verifica cada uma das 113 tarefas por execução de programa, não por alguém lendo o diff e achando que ficou razoável. Isso remove subjetividade do resultado: ou o teste passa, ou não passa.

**Desconfie de benchmark saturado.** Quando os modelos de fronteira empatam a menos de um ponto percentual de diferença entre si, o benchmark provavelmente está perto do teto para aquela classe de modelo. O DeepSWE mostra os dois regimes ao mesmo tempo em 1º de setembro de 2026: os três primeiros colocados cabem dentro de 0,6 ponto, faixa em que a ordem entre eles não sustenta decisão nenhuma, enquanto do primeiro ao décimo ainda vão 6,8 pontos. A leitura útil é essa: no topo, trate como empate técnico; ao comparar o topo com o meio da tabela, a diferença ainda mede alguma coisa.

Vale a comparação com a edição anterior deste mesmo material, de 20 de agosto de 2026, quando a distância do primeiro ao quinto era de 4,6 pontos e hoje é de 4,1. O placar não mudou só de nomes; ele encolheu. Um *benchmark* que aperta a cada rodada é um *benchmark* caminhando para a aposentadoria.

**Desconfie de número autorreportado por quem vende o modelo.** Fabricantes escolhem qual benchmark divulgar no anúncio de lançamento, e às vezes trocam de benchmark de uma versão para a outra sem explicar por quê. Prefira leitores independentes que avaliam todos os fabricantes sob o mesmo arnês de teste, na mesma data — é exatamente o que o DeepSWE (mantido pela Datacurve, publicado em benchlm.ai) faz: roda Claude, GPT, Gemini e modelos abertos como o GLM lado a lado, sem depender do número que cada fabricante escolheu anunciar.

**Nota do placar não é a decisão inteira.** Custo por tarefa resolvida, latência, tamanho da janela de contexto e confiabilidade dentro do seu ambiente agêntico específico pesam tanto quanto a taxa de resolução — um modelo 3 pontos percentuais à frente, mas 5 vezes mais caro por tarefa, raramente compensa para o dia a dia de um time.

## Placar de referência — DeepSWE

| Modelo | Organização | DeepSWE |
|---|---|---|
| Gemini 3.8 Flash | Google | 73,8% |
| Claude Opus 5 | Anthropic | 73,6% |
| GPT-6 Astra | OpenAI | 73,2% |
| GPT-5.6 Sol | OpenAI | 72,7% |
| Claude Fable 5 | Anthropic | 69,7% |

Fonte: [benchlm.ai — DeepSWE](https://benchlm.ai/benchmarks/deepswe), atualizado em 1º de setembro de 2026, 28 modelos avaliados: 113 tarefas de longo horizonte, tiradas de 91 repositórios ativos de código aberto em 5 linguagens, verificadas por programa.

**Este placar envelhece rápido**: confira o [DeepSWE Leaderboard](https://benchlm.ai/benchmarks/deepswe) atualizado antes de decidir, não confie em número congelado numa página de workshop.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
