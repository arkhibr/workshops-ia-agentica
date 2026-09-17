# Avaliação de modelos

Escolher um modelo para tarefas de engenharia de software exige ler *benchmark* com critério, porque o número divulgado depende tanto da forma como o teste foi conduzido quanto do modelo medido. Esta página reúne cinco critérios de leitura e um placar de referência.

<a id="como-avaliar-modelos-para-engenharia-de-software"></a>

Escolher um modelo pelo nome mais falado do momento é o mesmo erro de raiz do vibe coding: aceitar sem verificar. Os cinco critérios abaixo dão base para decidir.

**Use um benchmark que meça o trabalho real do repositório, em vez da função isolada.** O [HumanEval (Chen et al., 2021)](../referencia/bibliografia.md#chen-et-al-codex-e-humaneval-2021) mede se o modelo escreve uma função correta a partir de um enunciado, o que é útil e ainda assim distante do que a Sessão 8 chama de engenharia agêntica. Um benchmark como o [DeepSWE](../referencia/bibliografia.md#datacurve-deepswe-leaderboard) mede se o agente resolve uma tarefa real, de longo horizonte, dentro de um repositório existente: localizar a causa, editar os arquivos certos, passar num verificador automático. É o tipo de medida mais próximo do trabalho que um time de engenharia de software faz no dia a dia.

**Prefira tarefas verificadas por programa a julgamento humano de "parece bom".** O DeepSWE verifica cada uma das 113 tarefas rodando um programa. Ninguém lê o diff para decidir se ficou razoável, e por isso o resultado é objetivo: ou o teste passa, ou o teste falha.

**Desconfie de benchmark saturado.** Quando os modelos de fronteira empatam a menos de um ponto percentual de diferença entre si, o benchmark provavelmente está perto do teto para aquela classe de modelo. O DeepSWE mostra os dois regimes ao mesmo tempo em 1º de setembro de 2026: os três primeiros colocados cabem dentro de 0,6 ponto, faixa em que a ordem entre eles não sustenta decisão nenhuma, enquanto do primeiro ao décimo ainda vão 6,8 pontos. Leia assim: no topo, trate como empate técnico. Comparando o topo com o meio da tabela, a diferença ainda mede alguma coisa.

Compare com a edição anterior deste mesmo material, de 20 de agosto de 2026: a distância do primeiro ao quinto era de 4,6 pontos, e hoje é de 4,1. Além de trocar de nomes, o placar encolheu. Quando a faixa aperta a cada rodada, o benchmark está chegando ao fim da vida útil.

**Desconfie de número autorreportado por quem vende o modelo.** Fabricantes escolhem qual benchmark divulgar no anúncio de lançamento, e às vezes trocam de benchmark de uma versão para a outra sem explicar por quê. Prefira leitura independente, que avalia os fabricantes lado a lado e na mesma data, como a do DeepSWE publicada em benchlm.ai, que espelha o placar público e roda Claude, GPT, Gemini e modelos abertos como o GLM.

Saiba o que "independente" garante e o que ele não garante. O benchlm.ai declara usar, para cada modelo, a melhor configuração disponível do `mini-swe-agent`, em vez de uma configuração idêntica para todos. Essa configuração em volta do modelo tem nome, **arnês**, e a Sessão 2 trata dela por inteiro: é tudo que cerca o modelo numa execução, das ferramentas conectadas ao arquivo de instrução. A escolha do benchlm.ai é defensável e muda o que a nota significa. Ela mede o desempenho do par modelo mais arnês.

O Claude Fable 5.1 serve de caso concreto para os dois cuidados acima, e é por isso que ele **não** aparece na tabela abaixo. Ele ainda não tem linha na leitura independente. O número que circula para ele, 67,4% no DeepSWE v1.1, foi publicado pela OpenAI, uma concorrente, ao comparar o próprio GPT-6 Astra com ele. Três coisas para observar nesse arranjo antes de usar o número:

- Quem mede é parte interessada.
- A versão do teste é outra, v1.1, e por isso a comparação linha a linha com a tabela abaixo não se sustenta.
- No mesmo material a OpenAI reporta 74,1% para o próprio Astra, enquanto a leitura independente lê 73,2% para ele.

A divergência entre o número do fabricante e o do leitor independente é de 0,9 ponto. Parece pouco, e é exatamente o tamanho que decide posição num ranking apertado.

No mesmo material, o Terminal-Bench 4.0 dá o exemplo mais claro: a tabela da OpenAI mostra 57,7% para o Astra, e a legenda do gráfico dela mesma mostra 57,9%. Quando o fabricante diverge de si próprio dentro do mesmo documento, nenhum dos dois números serve para decidir.

**Nota do placar não é a decisão inteira.** Custo por tarefa resolvida, latência, tamanho da janela de contexto e confiabilidade dentro do seu ambiente agêntico específico pesam tanto quanto a taxa de resolução. Um modelo 3 pontos percentuais à frente, mas 5 vezes mais caro por tarefa, raramente compensa para o dia a dia de um time.

## Placar de referência do DeepSWE

| Modelo | Organização | DeepSWE |
|---|---|---|
| Gemini 3.8 Flash | Google | 73,8% |
| Claude Opus 5 | Anthropic | 73,6% |
| GPT-6 Astra | OpenAI | 73,2% |
| GPT-5.6 Sol | OpenAI | 72,7% |
| Claude Fable 5 | Anthropic | 69,7% |

Fonte: [benchlm.ai — DeepSWE](../referencia/bibliografia.md#datacurve-deepswe-leaderboard), atualizado em 1º de setembro de 2026, 28 modelos avaliados, cada um na melhor configuração disponível do `mini-swe-agent`: 113 tarefas de longo horizonte, tiradas de 91 repositórios ativos de código aberto em 5 linguagens, verificadas por programa.

**Este placar envelhece rápido.** Confira o [DeepSWE Leaderboard](../referencia/bibliografia.md#datacurve-deepswe-leaderboard) atualizado antes de decidir, em vez de usar o número congelado desta página.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
