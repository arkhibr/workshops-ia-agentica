# A tese do Software 3.0

[Andrej Karpathy](../referencia/bibliografia.md#karpathy-software-is-changing-again-2025) deu o nome de Software 3.0 à mudança em que o prompt em linguagem natural passa a governar o comportamento do sistema. Esta página cobre a tese, a curva de capacidade que a tornou prática e o que ela muda no trabalho de quem desenvolve.

## Os três paradigmas

Todo LLM que você usa hoje numa ferramenta agêntica de codificação roda sobre a arquitetura Transformer, descrita por [Vaswani et al. em 2017](../referencia/bibliografia.md#vaswani-et-al-attention-is-all-you-need-2017). Essa arquitetura torna prática a aprendizagem em contexto, e Karpathy montou a tese sobre essa base, apresentada na YC AI Startup School em 17 de junho de 2025.

Karpathy já vinha nessa linha desde antes. Em 2017, no mesmo ano do artigo de Vaswani et al., ele publicou o ensaio ["Software 2.0"](../referencia/bibliografia.md#karpathy-software-20-2017), onde defende que uma rede neural treinada é um programa de outro tipo: ninguém a escreve à mão em Python ou C++, porque ela é compilada a partir de dados por um processo de otimização. Software 3.0 dá mais um passo na mesma direção. A programação teve um paradigma dominante por vez ao longo da história, e agora tem três convivendo:

- **Software 1.0** é código explícito, escrito por humanos em linguagens de programação.
- **Software 2.0** são redes neurais: em vez de código, o time ajusta pesos por treinamento.
- **Software 3.0** é o prompt em linguagem natural funcionando como o próprio programa, interpretado por um LLM. Karpathy resume a mudança numa frase que já circula como definição: "the hottest new programming language is English."

O prompt passa a funcionar como especificação executável. Tudo que o LLM considera numa execução precisa caber na **janela de contexto**, que é o limite de unidades de entrada e saída que o modelo consegue considerar. Convenção do repositório, regra de negócio e caso de borda precisam estar escritos ali dentro, porque o agente não tem acesso a nada que ficou fora da janela. Por isso esta sessão trata o conteúdo da janela de contexto como o programa que o agente executa.

Karpathy prevê o resto da década na mesma linha: "Software 3.0 is eating 1.0/2.0". Código explícito e modelos treinados continuam existindo, e a parcela que cresce é a do comportamento do sistema escrito diretamente em linguagem natural.

![Evolução de Software 1.0, no qual humanos escrevem regras em código, para Software 2.0, no qual dados e otimização produzem pesos, e Software 3.0, no qual linguagem natural, regras, convenções, exemplos e casos de borda entram na janela de contexto de um LLM.](../assets/images/s1-software-1-2-3.png)

## A curva de capacidade que tornou isso prático

Karpathy explica o que está mudando, e o [SWE-bench, apresentado por Jimenez et al. em 2024](../referencia/bibliografia.md#jimenez-et-al-swe-bench-2024), mostra quando a mudança passou a valer na prática. O benchmark pega problemas reais, registrados como *issues* em repositórios populares do GitHub, e pede ao agente o patch que resolve cada um. Gerar uma função isolada é bem mais simples do que isso: aqui o agente precisa achar a causa no repositório inteiro e passar nos testes que a própria comunidade usa para aceitar contribuição.

No artigo original, o melhor resultado (Claude 2 com recuperação por palavras-chave) resolveu 1,96% dos problemas. Em 2026, os agentes de codificação mais avançados resolvem cerca de 97% dos mesmos problemas na versão revisada do benchmark (SWE-bench Verified). Essa curva mede o amadurecimento da disciplina em volta do modelo: navegação melhor do repositório, uso real de ferramentas, verificação antes de declarar a tarefa concluída. Essas três práticas correspondem às responsabilidades humanas descritas na próxima seção, observadas aqui ao longo de dois anos de evolução do benchmark.

## Efeitos sobre o trabalho de quem desenvolve

Esta sessão usa três termos para separar os efeitos do Software 3.0 sobre o trabalho de desenvolvimento, e cada um deles muda em ritmo próprio:

- **Piso** é o resultado mínimo que qualquer desenvolvedor obtém com um agente: código que compila e roda. Quando a linguagem de programação é o português ou o inglês, esse resultado fica ao alcance de toda a equipe e deixa de diferenciar quem desenvolve.
- **Teto** é a qualidade máxima que a equipe alcança: código que resolve o problema em todos os casos que importam. Karpathy descreve a distância entre os dois níveis com a frase "demo is works.any(), product is works.all()", porque um protótipo precisa funcionar uma vez e um produto precisa funcionar em todos os casos relevantes. O teto só sobe quando a equipe adota o *generation-verification loop*, ciclo em que o agente gera o código, a equipe verifica o resultado e o agente ajusta até a verificação passar.
- **Julgamento humano** é a parte do trabalho que o modelo não executa sozinho, formada pelas três responsabilidades de [Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026): especificar, prover ferramentas e verificar. O valor dessa parte aumenta à medida que o piso fica acessível a toda a equipe.

[Willison](../referencia/bibliografia.md#willison-what-is-agentic-engineering-2026) localiza esse julgamento em "figuring out *what* code to write": navegar as decisões de arquitetura que sobram depois que o agente gera uma proposta. Um código pode rodar e ainda falhar em correção, em testabilidade ou em aderência à arquitetura do sistema, e nenhuma dessas propriedades indica se o problema resolvido era o problema que a equipe precisava resolver.

| Termo             | Responsabilidade humana associada | Pergunta que o termo responde                                                                       |
| ----------------- | --------------------------------- | --------------------------------------------------------------------------------------------------- |
| Piso              | —                                 | O código compila e roda?                                                                            |
| Teto              | Especificação + ferramental       | O código resolve exatamente o problema, nos casos de borda que importam?                            |
| Julgamento humano | Verificação                       | Esse era o problema certo? O resultado está pronto para produção ou passou uma única vez num demo?  |

!!! question "Antes de continuar"  
    Pense num código aceito recentemente sem revisão cuidadosa. Ele passou pela coluna "piso" (rodou) ou também pela coluna "teto" (foi verificado nos casos que importam)?

**Próxima página:** [Sistemas agênticos e simplicidade](sistemas-agenticos.md).
