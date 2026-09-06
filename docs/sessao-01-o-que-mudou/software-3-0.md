# A tese do Software 3.0

Andrej Karpathy chamou de Software 3.0 a mudança em que o prompt em linguagem natural passa a ser o artefato que governa o comportamento do sistema. A tese, a curva de capacidade que a tornou prática, e o que ela move no trabalho de quem desenvolve.

## A tese do Software 3.0

A arquitetura Transformer, descrita por Vaswani et al. em 2017, é a base técnica de todo LLM usado hoje em ferramentas agênticas de codificação. Ela é o que torna prática a aprendizagem em contexto descrita acima, e é sobre essa maturidade técnica que Karpathy constrói uma tese de fundo, apresentada na YC AI Startup School de 17 de junho de 2025.

A tese não nasceu isolada. Em 2017, no mesmo ano do artigo de Vaswani et al., Karpathy já havia publicado o ensaio "Software 2.0", propondo que uma rede neural treinada é um tipo de programa diferente: em vez de escrito à mão em Python ou C++, ele é compilado a partir de dados por um processo de otimização. Software 3.0 estende essa mesma lógica um passo adiante — a programação teve, ao longo da história, um paradigma dominante por vez, e agora tem três coexistindo.

**Software 1.0** é código explícito, escrito por humanos em linguagens de programação. **Software 2.0** são redes neurais: em vez de código, o time ajusta pesos por treinamento. **Software 3.0** é o prompt em linguagem natural funcionando como o próprio programa, interpretado por um LLM. Karpathy resume a virada numa frase que já circula como definição: "the hottest new programming language is English."

O prompt deixa de ser um pedido informal para um assistente e passa a ser a especificação executável. Tecnicamente, o que o LLM processa em cada execução é limitado pela **janela de contexto**: o limite de unidades de entrada e saída que o modelo consegue considerar. Convenções do repositório, regra de negócio e casos de borda precisam caber, de forma explícita, dentro dessa janela. O que não está lá dentro não existe para o agente — daí a ideia central desta sessão: a janela de contexto virou o programa.

A previsão de Karpathy para a década segue a mesma lógica: "Software 3.0 is eating 1.0/2.0". Código explícito e modelos treinados não desaparecem; uma fração crescente do comportamento de um sistema passa a ser especificada diretamente em linguagem natural.

![Evolução de Software 1.0, no qual humanos escrevem regras em código, para Software 2.0, no qual dados e otimização produzem pesos, e Software 3.0, no qual linguagem natural, regras, convenções, exemplos e casos de borda entram na janela de contexto de um LLM.](../assets/images/s1-software-1-2-3.png)

## A curva de capacidade por trás do momento atual

A tese de Karpathy explica o que está mudando. O SWE-bench, apresentado por Jimenez et al. em 2024, mede quando essa mudança passou a valer na prática. O benchmark pega problemas reais, reportados como issues em repositórios populares do GitHub, e pede ao agente que produza o patch que resolve o problema. Diferente de gerar uma função isolada, a tarefa exige localizar a causa no repositório inteiro e passar nos testes que a própria comunidade usa para aceitar contribuições.

No artigo original, o melhor resultado (Claude 2 com recuperação por palavras-chave) resolveu 1,96% dos problemas. Em 2026, os agentes de codificação mais avançados resolvem cerca de 97% dos mesmos problemas na versão revisada do benchmark (SWE-bench Verified). Essa curva não mede um modelo ficando mais esperto sozinho, mede a disciplina em volta do modelo amadurecendo: melhor navegação do repositório, uso real de ferramentas, verificação antes de declarar a tarefa concluída. É a mesma equação de piso, teto e julgamento vista a seguir, só que numa escala de dois anos em vez de uma sessão de trabalho.

## O que sobe: piso, teto, julgamento

A mudança sobe três coisas ao mesmo tempo, em ritmos diferentes:

- **O piso sobe para todos.** Se a linguagem de programação é o português ou o inglês, qualquer desenvolvedor produz hoje código que compila e roda. Isso já não é diferencial.
- **O teto sobe só com disciplina.** Karpathy nomeia a lacuna: "demo is works.any(), product is works.all()". Um protótipo só precisa funcionar uma vez; um produto precisa funcionar em todos os casos que importam. Fechar essa lacuna é o *generation-verification loop*: gerar, verificar, ajustar, repetir.
- **O julgamento humano sobe de valor.** As três responsabilidades de Willison (especificar, prover ferramentas, verificar) são decisões que o modelo não toma sozinho.

Willison localiza esse julgamento em "figuring out *what* code to write": navegar as decisões de arquitetura que sobram depois que o agente gera uma proposta. Um ganho de piso (o código roda) não é o mesmo que um ganho de teto (o código está correto, testável e alinhado à arquitetura do sistema), e nenhum dos dois substitui o julgamento sobre se aquele era o problema certo a resolver.

| Seta | Responsabilidade que sobe de valor | Pergunta que ela responde |
|---|---|---|
| Piso sobe para todos | — | O código compila e roda? |
| Teto sobe com disciplina | Especificação + ferramental | O código resolve exatamente o problema, nos casos de borda que importam? |
| Julgamento humano sobe de valor | Verificação | Esse era o problema certo? O resultado está pronto para produção, ou é só um demo que passou uma vez? |

!!! question "Antes de continuar"
    Pense num código aceito recentemente sem revisão cuidadosa. Ele passou pela coluna "piso" (rodou) ou também pela coluna "teto" (foi verificado nos casos que importam)?

**Próxima página:** [Sistemas agênticos e simplicidade](sistemas-agenticos.md).
