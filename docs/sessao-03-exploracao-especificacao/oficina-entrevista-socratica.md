# Oficina de entrevista socrática

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (**Claude Code, Codex CLI ou Gemini CLI**). Não exige código, instalação nem projeto: o trabalho é inteiramente conversa. Tempo estimado: 16 minutos.

**Decisão em foco:** fazer o agente conduzir uma entrevista em vez de entregar a resposta pronta, e medir o que a disciplina de uma pergunta por vez expõe que uma revisão rápida não expõe.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, validação de uma especificação ruim.
- **Exploração em dupla:** Experimento B, o mesmo pedido com o contrato quebrado, para ver a diferença.
- **Extensão opcional:** Experimento C, roteiro para entrevistar uma pessoa.

## O prompt do entrevistador

Os três experimentos partem deste prompt. Cole numa conversa nova, sempre no começo:

```text
Você é um entrevistador socrático de requisitos. Seu trabalho é PERGUNTAR,
nunca responder, sugerir solução ou corrigir o que eu escrevi.

CONTRATO DE MENSAGEM, obrigatório em toda mensagem sua:
- no máximo 1 frase espelhando o que acabei de dizer
- UMA única pergunta, uma única interrogação na mensagem inteira
- opcionalmente 2 a 4 opções de múltipla escolha, que não contam como
  perguntas adicionais
Duas interrogações na mesma mensagem violam o contrato, mesmo que as
perguntas sejam curtas ou relacionadas.

FASES, nesta ordem: enquadramento, exploração, aprofundamento (pressupostos
e evidências), ampliação (perspectivas alternativas e cenários de falha),
síntese. Só avance de fase quando o critério da fase estiver satisfeito.

CATEGORIAS que você deve percorrer, não só a primeira: esclarecimento,
pressupostos, evidências, implicações, perspectivas alternativas,
meta-pensamento.

REGRA DO ADJETIVO VAGO: se eu usar rápido, flexível, robusto, escalável,
intuitivo, seguro, simples ou moderno, sua próxima pergunta é de
quantificação — número, comportamento observável ou exemplo concreto.

A cada 4 respostas minhas, substitua o espelhamento por uma síntese curta
separando confirmado, suposto e conflitos, e termine com a única pergunta.

CRITÉRIO DE ENCERRAMENTO: as três canônicas respondidas com precisão —
o que estamos construindo, para quem, e qual o critério de sucesso testável.

Quando eu disser "fechar entrevista", produza o dossiê com cinco seções.
As três canônicas. O ledger classificando cada afirmação relevante como
[FATO], [EVIDÊNCIA], [PRESSUPOSTO], [DECISÃO], [RESTRIÇÃO], [RISCO],
[ABERTA] ou [CONFLITO]. Os termos quantificados, com antes e depois. Os
riscos examinados. E as perguntas que ficaram abertas, com o dono de cada
uma. Opinião sem fonte identificável é [PRESSUPOSTO], nunca [FATO].

Comece pela fase de enquadramento.
```

## A especificação ruim

Os experimentos A e B usam este pedido, recebido de um gerente comercial da Vetor, a plataforma fictícia de e-commerce B2B do workshop:

> "Precisamos de um painel de relatórios de desconto pro time comercial. Ele deve ter um botão de exportar pra Excel, mostrar um gráfico de pizza com os descontos aplicados no mês, e ser bem intuitivo e moderno. Como os gerentes vão usar isso todo dia, o relatório precisa carregar rápido. Todo desconto aplicado aparece lá. Entrega até sexta, com testes completos e cobertura de 100%."

Antes de colar, marque no papel quantos defeitos você enxerga sozinho, numa leitura. O número serve de linha de base para o passo final.

## Experimento A — validação de uma especificação existente

**Objetivo:** ser entrevistado sobre uma especificação ruim e observar o que a disciplina expõe.

**Passo 1 — instale o entrevistador.** Cole o prompt acima numa conversa nova. O agente deve responder com a fase de enquadramento e **uma** pergunta, provavelmente sobre quem responde e qual o critério de encerramento.

**Passo 2 — entregue a especificação e responda.** Cole o pedido do gerente e responda cada pergunta como se você fosse quem escreveu o pedido original. Improvise quando não souber, do mesmo jeito que um stakeholder real improvisaria, mas mantenha coerência entre as respostas.

**Passo 3 — conte as interrogações.** A cada mensagem do agente, confira se veio uma única interrogação. Anote quantas mensagens violaram o contrato. Essa contagem é um dado do experimento.

**Passo 4 — force um adjetivo vago.** Em alguma resposta, use de propósito uma das palavras da regra: diga que o painel precisa ser "simples" ou que o carregamento tem que ser "rápido". A próxima pergunta do agente deveria ser de quantificação. Anote se foi.

**Passo 5 — feche e leia o dossiê.** Depois de pelo menos seis respostas, escreva "fechar entrevista". Leia o dossiê e confira três coisas: as três canônicas estão respondidas de forma testável, o ledger tem pelo menos um `[PRESSUPOSTO]`, e alguma pergunta ficou aberta com dono.

**Passo 6 — compare com a sua linha de base.** Quantos defeitos você tinha marcado no papel antes de começar? Quantos o dossiê registrou? A diferença é o que a entrevista comprou.

**Questões exploratórias:**

- O agente tentou corrigir a especificação em vez de perguntar? Em que momento, e o que na conversa provocou isso?
- Alguma opinião do gerente virou `[FATO]` no ledger sem fonte? "Os gerentes vão usar todo dia" tem evidência ou é pressuposto?
- Qual pergunta foi mais desconfortável de responder, e o que esse desconforto revela sobre o que o pedido original escondia?

## Experimento B — o mesmo pedido, sem o contrato

**Objetivo:** isolar o efeito da disciplina, separando o que veio do método e o que veio só de o agente ser competente.

**Antes de começar: por que a ordem importa.** Este experimento precisa de uma conversa nova, que não tenha visto a entrevista do experimento A.

**Passo 1 — peça a análise direta.** Numa conversa limpa, cole a mesma especificação ruim e peça: "analise esta especificação e aponte os problemas dela".

**Passo 2 — compare as duas saídas.** Ponha lado a lado a resposta do passo 1 e o dossiê do experimento A. Compare por três critérios: quantos defeitos cada um encontrou, quais decisões de negócio ficaram registradas em cada um, e quem tomou essas decisões nos dois casos.

**Passo 3 — identifique o que só a entrevista produziu.** Procure no dossiê ao menos uma informação que **não existia** na especificação original nem podia ser deduzida dela. Essa informação veio de você, extraída por uma pergunta. A análise direta não tinha como produzi-la, porque ninguém perguntou.

**Questões exploratórias:**

- A análise direta foi mais rápida. Em que tipo de tarefa essa velocidade compensa a perda, e em que tipo não compensa?
- Se você fosse implementar a partir de cada uma das duas saídas, qual decisão de negócio você ainda teria que tomar sozinho em cada caso?

## Experimento C — roteiro para entrevistar uma pessoa

**Objetivo:** usar o agente no modo que gera roteiro, para quando a entrevista é com um humano e não com o modelo.

Nem toda entrevista acontece com o agente. Quando quem tem a resposta é uma pessoa do negócio, o agente serve para preparar o roteiro da conversa que você vai conduzir.

**Passo 1 — peça o roteiro.** Numa conversa nova, descreva em duas frases uma funcionalidade real do seu backlog e peça: "gere um roteiro de entrevista socrática que eu vou conduzir com o dono do produto, com a pergunta de abertura, as ramificações conforme o tipo de resposta que eu receber, e o sinal de que cada fase terminou".

**Passo 2 — avalie o roteiro pelas fases.** O roteiro cobre as cinco fases, ou só a de exploração? Tem pergunta de pressuposto e de evidência, ou só de esclarecimento?

**Passo 3 — teste a ramificação.** Escolha a pergunta de abertura e imagine duas respostas opostas que o dono do produto poderia dar. O roteiro prevê caminhos diferentes para as duas, ou segue igual de qualquer jeito? Roteiro que não ramifica é questionário.

**Questões exploratórias:**

- Qual pergunta do roteiro você não teria coragem de fazer ao dono do produto? O que isso diz sobre a pergunta, ou sobre a relação?
- O roteiro pressupõe alguma resposta? Uma pergunta que já embute a resposta esperada só serve para confirmar o que você já achava.

## Evidência a entregar

Cada dupla entrega:

1. O dossiê do experimento A, com ledger e perguntas abertas.
2. A contagem de violações do contrato de mensagem, e em que fase aconteceram.
3. Uma frase respondendo: qual informação o dossiê registrou que a análise direta do experimento B não tinha como produzir?

**Próxima página:** [Exercícios](exercicios.md).
