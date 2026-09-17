# A tese do Software 3.0

[Andrej Karpathy](../referencia/bibliografia.md#karpathy-software-is-changing-again-2025) deu o nome de Software 3.0 à mudança em que o prompt em linguagem natural passa a governar o comportamento do sistema. Esta página cobre a tese, a curva de capacidade que a tornou prática e o que ela muda no trabalho de quem desenvolve.

## Os três paradigmas

Todo LLM que você usa hoje numa ferramenta agêntica de codificação roda sobre a arquitetura Transformer, descrita por [Vaswani et al. em 2017](../referencia/bibliografia.md#vaswani-et-al-attention-is-all-you-need-2017). É ela que torna prática a aprendizagem em contexto, e foi sobre essa base que Karpathy montou a tese, apresentada na YC AI Startup School em 17 de junho de 2025.

Karpathy já vinha nessa linha desde antes. Em 2017, no mesmo ano do artigo de Vaswani et al., ele publicou o ensaio ["Software 2.0"](../referencia/bibliografia.md#karpathy-software-20-2017), onde defende que uma rede neural treinada é um programa de outro tipo: ninguém a escreve à mão em Python ou C++, porque ela é compilada a partir de dados por um processo de otimização. Software 3.0 dá mais um passo na mesma direção. A programação teve um paradigma dominante por vez ao longo da história, e agora tem três convivendo:

- **Software 1.0** é código explícito, escrito por humanos em linguagens de programação.
- **Software 2.0** são redes neurais: em vez de código, o time ajusta pesos por treinamento.
- **Software 3.0** é o prompt em linguagem natural funcionando como o próprio programa, interpretado por um LLM. Karpathy resume a virada numa frase que já circula como definição: "the hottest new programming language is English."

O prompt sai da posição de pedido informal a um assistente e vira a especificação executável. Tudo que o LLM enxerga numa execução precisa caber na **janela de contexto**, que é o limite de unidades de entrada e saída que o modelo consegue considerar. Convenção do repositório, regra de negócio e caso de borda precisam estar escritos ali dentro. O que ficou de fora não existe para o agente. É daí que vem a ideia central desta sessão: a janela de contexto virou o programa.

Karpathy prevê o resto da década na mesma linha: "Software 3.0 is eating 1.0/2.0". Código explícito e modelos treinados continuam existindo. O que cresce é a fatia do comportamento do sistema escrita direto em linguagem natural.

![Evolução de Software 1.0, no qual humanos escrevem regras em código, para Software 2.0, no qual dados e otimização produzem pesos, e Software 3.0, no qual linguagem natural, regras, convenções, exemplos e casos de borda entram na janela de contexto de um LLM.](../assets/images/s1-software-1-2-3.png)

## A curva de capacidade que tornou isso prático

Karpathy explica o que está mudando. O [SWE-bench, apresentado por Jimenez et al. em 2024](../referencia/bibliografia.md#jimenez-et-al-swe-bench-2024), mostra quando a mudança passou a valer na prática. O benchmark pega problemas reais, registrados como *issues* em repositórios populares do GitHub, e pede ao agente o patch que resolve cada um. Gerar uma função isolada é bem mais simples do que isso: aqui o agente precisa achar a causa no repositório inteiro e passar nos testes que a própria comunidade usa para aceitar contribuição.

No artigo original, o melhor resultado (Claude 2 com recuperação por palavras-chave) resolveu 1,96% dos problemas. Em 2026, os agentes de codificação mais avançados resolvem cerca de 97% dos mesmos problemas na versão revisada do benchmark (SWE-bench Verified). Essa curva mede o amadurecimento da disciplina em volta do modelo: navegação melhor do repositório, uso real de ferramentas, verificação antes de declarar a tarefa concluída. São as mesmas três setas da próxima seção, numa escala de dois anos em vez de uma sessão de trabalho.

## O que sobe: piso, teto, julgamento

Três coisas sobem ao mesmo tempo, em ritmos diferentes:

- **O piso sobe para todos.** Se a linguagem de programação é o português ou o inglês, qualquer desenvolvedor produz hoje código que compila e roda. Isso já não é diferencial.
- **O teto sobe só com disciplina.** Karpathy nomeia a lacuna: "demo is works.any(), product is works.all()". Um protótipo só precisa funcionar uma vez. Um produto precisa funcionar em todos os casos que importam. Fechar essa lacuna é o *generation-verification loop*: gerar, verificar, ajustar, repetir.
- **O julgamento humano sobe de valor.** As três responsabilidades de [Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026) (especificar, prover ferramentas, verificar) são decisões que o modelo não toma sozinho.

[Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026) localiza esse julgamento em "figuring out *what* code to write": navegar as decisões de arquitetura que sobram depois que o agente gera uma proposta. Código que roda ainda está longe de código correto, testável e alinhado à arquitetura do sistema. E nenhum dos dois responde se aquele era o problema certo de resolver.

| Seta                            | Responsabilidade que sobe de valor | Pergunta que ela responde                                                                             |
| ------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Piso sobe para todos            | —                                  | O código compila e roda?                                                                              |
| Teto sobe com disciplina        | Especificação + ferramental        | O código resolve exatamente o problema, nos casos de borda que importam?                              |
| Julgamento humano sobe de valor | Verificação                        | Esse era o problema certo? O resultado está pronto para produção, ou é só um demo que passou uma vez? |

!!! question "Antes de continuar"  
    Pense num código aceito recentemente sem revisão cuidadosa. Ele passou pela coluna "piso" (rodou) ou também pela coluna "teto" (foi verificado nos casos que importam)?

**Próxima página:** [Sistemas agênticos e simplicidade](sistemas-agenticos.md).
