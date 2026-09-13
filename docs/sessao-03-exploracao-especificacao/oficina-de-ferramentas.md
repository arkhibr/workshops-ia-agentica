# Oficina de ferramentas

**Objetivo Bloom:** Aplicar.

O trajeto desta oficina vai de um pedido vago da Vetor, a plataforma fictícia de e-commerce B2B usada no workshop, até uma especificação testada, com o agente implementando exatamente o que a especificação diz.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Codex CLI ou Gemini CLI), o git e o Node.js 20 ou superior. Tempo estimado: 18 minutos.

Todos os experimentos partem de um **projeto vazio**, montado durante a própria oficina. Ninguém clona nada pronto: cada pessoa cria os arquivos abaixo e parte exatamente do mesmo estado.

**Decisão em foco:** transformar um pedido vago numa especificação BR/FR/NFR verificável, antes de acionar o agente para implementar.

## Preparação

**Passo 1. Crie o projeto.**

```bash
mkdir oficina-especificacao && cd oficina-especificacao
git init
node --version   # precisa mostrar v20 ou superior
```

**Passo 2. Crie a regra de desconto.** Salve como `src/desconto.js`:

```javascript
export const TETO_DESCONTO = 1000;

export function calcularDesconto(valorTotal, tipoCliente) {
  if (typeof valorTotal !== 'number' || Number.isNaN(valorTotal) || valorTotal < 0) {
    throw new TypeError('valorTotal deve ser um numero nao negativo');
  }

  let percentual = 0;
  if (valorTotal > 5000) percentual = 0.15;
  else if (valorTotal > 2000) percentual = 0.1;
  else if (valorTotal > 500) percentual = 0.05;

  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
```

O parâmetro `tipoCliente` é recebido e nunca usado. A faixa de atacado nunca foi implementada, e essa é a lacuna que a sessão trabalha.

**Passo 3. Crie os testes.** Salve como `test/desconto.test.js`:

```javascript
import assert from 'node:assert/strict';
import { describe, it } from 'node:test';

import { calcularDesconto, TETO_DESCONTO } from '../src/desconto.js';

describe('calcularDesconto', () => {
  it('nao da desconto ate 500,00', () => {
    assert.equal(calcularDesconto(500, 'padrao'), 0);
  });

  it('da 5% na faixa de 500,01 a 2.000,00', () => {
    assert.equal(calcularDesconto(1000, 'padrao'), 50);
  });

  it('da 10% na faixa de 2.000,01 a 5.000,00', () => {
    assert.equal(calcularDesconto(3000, 'padrao'), 300);
  });

  it('da 15% acima de 5.000,00', () => {
    assert.equal(calcularDesconto(6000, 'padrao'), 900);
  });

  it('respeita o teto de desconto por pedido', () => {
    assert.equal(calcularDesconto(100000, 'padrao'), TETO_DESCONTO);
  });

  it('recusa valor negativo', () => {
    assert.throws(() => calcularDesconto(-1, 'padrao'), TypeError);
  });
});
```

**Passo 4. Confirme o estado inicial.**

```bash
npm init -y
npm pkg set type=module
npm pkg set scripts.test="node --test"
npm test
```

Os seis testes precisam passar antes de você continuar.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, o ciclo completo do pedido vago à implementação verificada, e Experimento C, a entrevista socrática sobre uma especificação ruim.
- **Exploração em dupla:** Experimento D, a mesma especificação analisada sem o contrato de entrevista.
- **Extensão para quem terminar antes:** Experimento B, sobre cenário de qualidade e função de aptidão, e Experimento E, o roteiro para entrevistar uma pessoa.

## Experimento A

**Objetivo:** conduzir o ciclo explorar → perguntar → propor → especificar sobre um pedido novo da Vetor, e comprovar que a especificação escrita é o que o agente de fato implementa.

**Antes de começar: a ordem importa.** O bloco de respostas abaixo simula quem pediu a mudança. Ele só cumpre a função de mostrar o efeito das perguntas se você escrever suas próprias perguntas antes de abri-lo. Abrir antes esvazia o experimento.

**Passo 1 — o pedido.** É este, e nada além disso:

> "Dá pra dar um desconto extra pros clientes que compram muito com a gente?"

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de especificar qualquer coisa. Use o repertório de [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) como referência.

**Passo 2 — as respostas.** Abra o bloco e compare com as perguntas que você escreveu.

??? note "Respostas de quem pediu — abra só depois de escrever suas próprias perguntas"
    - O que conta como "compra muito"? Cliente do tipo atacado com mais de 5 pedidos aprovados nos últimos 12 meses.
    - Esse desconto extra é cumulativo com a faixa normal, ou substitui? Cumulativo: soma-se à faixa normal, em pontos percentuais.
    - O desconto extra é de quantos pontos percentuais? 5 pontos percentuais.
    - O teto de R$ 1.000,00 por pedido continua valendo com o desconto extra somado? Sim, sempre. Nenhuma regra nova revoga o teto.
    - Esse desconto vale para cliente padrão também? Não, só para atacado.

**Passo 3 — proponha e especifique.** Escreva a proposta em três frases, depois a especificação em BR/FR, seguindo o formato de [Exemplo arquitetural](exemplo-arquitetural.md). `calcularDesconto` vai precisar de um terceiro parâmetro, `pedidosAprovados`, opcional, com valor padrão que preserve o comportamento dos seis testes já existentes.

**Passo 4 — peça a implementação.** Cole sua especificação para o agente e peça a implementação, com testes, dentro do projeto que você montou.

**Passo 5 — rode os casos abaixo contra o resultado.**

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 3.000,00 | atacado | 2 | R$ 300,00 (10%, não elegível ao adicional) |
| 2 | R$ 3.000,00 | atacado | 6 | R$ 450,00 (10% + 5% = 15%) |
| 3 | R$ 6.000,00 | atacado | 6 | R$ 1.000,00 (15% + 5% = 20% de R$ 6.000,00 seria R$ 1.200,00, mas o teto prevalece) |
| 4 | R$ 3.000,00 | padrão | 6 | R$ 300,00 (o adicional não vale para cliente padrão) |

Rode `node --test` e confira também que os seis testes originais continuam passando.

**Observe:** o caso 3 é o único em que a faixa normal, o adicional de recorrência e o teto se cruzam ao mesmo tempo. Se ele falhar, é sinal de que a especificação não deixou claro que o teto se aplica sobre a soma já feita dos dois percentuais.

**Questões exploratórias:**

- Alguma das suas perguntas do passo 1 não apareceu entre as respostas do passo 2? O que você teria feito sem essa resposta?
- Se você tivesse pedido direto ao agente "dá pra dar um desconto extra pros clientes que compram muito", sem o ciclo completo, qual das cinco respostas do passo 2 ele teria decidido sozinho?

## Experimento B

**Objetivo:** escrever um NFR como cenário de qualidade completo, e transformá-lo numa função de aptidão que continua rodando depois da aula.

**Execute:** a Vetor pede que `calcularDesconto` "continue rápida mesmo com muito tráfego". Escreva o cenário de qualidade completo (fonte, estímulo, ambiente, artefato, resposta, medida), seguindo o template de [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md#cenario-de-qualidade). Depois, peça ao agente uma função de aptidão simples: um teste em Node que chama `calcularDesconto` mil vezes com `console.time`/`console.timeEnd` ao redor, com o limiar da sua medida como condição de falha (`assert` ou `throw` se o tempo médio ultrapassar o limiar).

**Questões exploratórias:**

- O cenário que você escreveu seria o mesmo se a função fosse chamada uma vez por pedido, ou mil vezes por segundo no checkout? O que muda no estímulo e na medida?
- Sua função de aptidão tem responsável e reação declarados, ou só o teste técnico? Quem seria avisado se ela falhasse na esteira, daqui a seis meses?

## Insumos para os Experimentos C, D e E

Os três experimentos seguintes trocam o código pela conversa: usam o agente como entrevistador socrático, para expor os defeitos de uma especificação ruim sem que ele corrija nada por você.

### O prompt do entrevistador

Os Experimentos C, D e E partem deste prompt. Cole numa conversa nova, sempre no começo:

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
As três canônicas. O registro de proveniência classificando cada afirmação relevante como
[FATO], [EVIDÊNCIA], [PRESSUPOSTO], [DECISÃO], [RESTRIÇÃO], [RISCO],
[ABERTA] ou [CONFLITO]. Os termos quantificados, com antes e depois. Os
riscos examinados. E as perguntas que ficaram abertas, com o dono de cada
uma. Opinião sem fonte identificável é [PRESSUPOSTO], nunca [FATO].

Comece pela fase de enquadramento.
```

### A especificação ruim

Os Experimentos C e D usam este pedido, recebido de um gerente comercial da Vetor, a plataforma fictícia de e-commerce B2B do workshop:

> "Precisamos de um painel de relatórios de desconto pro time comercial. Ele deve ter um botão de exportar pra Excel, mostrar um gráfico de pizza com os descontos aplicados no mês, e ser bem intuitivo e moderno. Como os gerentes vão usar isso todo dia, o relatório precisa carregar rápido. Todo desconto aplicado aparece lá. Entrega até sexta, com testes completos e cobertura de 100%."

Antes de colar, marque no papel quantos defeitos você enxerga sozinho, numa leitura. O número serve de linha de base para o passo final.

## Experimento C

**Objetivo:** ser entrevistado sobre uma especificação ruim e observar o que a disciplina expõe.

**Passo 1 — instale o entrevistador.** Cole o prompt acima numa conversa nova. O agente deve responder com a fase de enquadramento e **uma** pergunta, provavelmente sobre quem responde e qual o critério de encerramento.

**Passo 2 — entregue a especificação e responda.** Cole o pedido do gerente e responda cada pergunta como se você fosse quem escreveu o pedido original. Improvise quando não souber, do mesmo jeito que um stakeholder real improvisaria, mas mantenha coerência entre as respostas.

**Passo 3 — conte as interrogações.** A cada mensagem do agente, confira se veio uma única interrogação. Anote quantas mensagens violaram o contrato. Essa contagem é um dado do experimento.

**Passo 4 — force um adjetivo vago.** Em alguma resposta, use de propósito uma das palavras da regra: diga que o painel precisa ser "simples" ou que o carregamento tem que ser "rápido". A próxima pergunta do agente deveria ser de quantificação. Anote se foi.

**Passo 5 — feche e leia o dossiê.** Depois de pelo menos seis respostas, escreva "fechar entrevista". Leia o dossiê e confira três coisas: as três canônicas estão respondidas de forma testável, o registro de proveniência tem pelo menos um `[PRESSUPOSTO]`, e alguma pergunta ficou aberta com dono.

**Passo 6 — compare com a sua linha de base.** Quantos defeitos você tinha marcado no papel antes de começar? Quantos o dossiê registrou? A diferença é o que a entrevista comprou.

**Questões exploratórias:**

- O agente tentou corrigir a especificação em vez de perguntar? Em que momento, e o que na conversa provocou isso?
- Alguma opinião do gerente virou `[FATO]` no registro de proveniência sem fonte? "Os gerentes vão usar todo dia" tem evidência ou é pressuposto?
- Qual pergunta foi mais desconfortável de responder, e o que esse desconforto revela sobre o que o pedido original escondia?

## Experimento D

**Objetivo:** isolar o efeito da disciplina, separando o que veio do método e o que veio só de o agente ser competente.

**Antes de começar: por que a ordem importa.** Este experimento precisa de uma conversa nova, que não tenha visto a entrevista do Experimento C.

**Passo 1 — peça a análise direta.** Numa conversa limpa, cole a mesma especificação ruim e peça: "analise esta especificação e aponte os problemas dela".

**Passo 2 — compare as duas saídas.** Ponha lado a lado a resposta do passo 1 e o dossiê do Experimento C. Compare por três critérios: quantos defeitos cada um encontrou, quais decisões de negócio ficaram registradas em cada um, e quem tomou essas decisões nos dois casos.

**Passo 3 — identifique o que só a entrevista produziu.** Procure no dossiê ao menos uma informação que **não existia** na especificação original nem podia ser deduzida dela. Essa informação veio de você, extraída por uma pergunta. A análise direta não tinha como produzi-la, porque ninguém perguntou.

**Questões exploratórias:**

- A análise direta foi mais rápida. Em que tipo de tarefa essa velocidade compensa a perda, e em que tipo não compensa?
- Se você fosse implementar a partir de cada uma das duas saídas, qual decisão de negócio você ainda teria que tomar sozinho em cada caso?

## Experimento E

**Objetivo:** usar o agente no modo que gera roteiro, para quando a entrevista é com um humano e não com o modelo.

Nem toda entrevista acontece com o agente. Quando quem tem a resposta é uma pessoa do negócio, o agente serve para preparar o roteiro da conversa que você vai conduzir.

**Passo 1 — peça o roteiro.** Numa conversa nova, descreva em duas frases uma funcionalidade real do seu backlog e peça: "gere um roteiro de entrevista socrática que eu vou conduzir com o dono do produto, com a pergunta de abertura, as ramificações conforme o tipo de resposta que eu receber, e o sinal de que cada fase terminou".

**Passo 2 — avalie o roteiro pelas fases.** O roteiro cobre as cinco fases, ou só a de exploração? Tem pergunta de pressuposto e de evidência, ou só de esclarecimento?

**Passo 3 — teste a ramificação.** Escolha a pergunta de abertura e imagine duas respostas opostas que o dono do produto poderia dar. O roteiro prevê caminhos diferentes para as duas, ou segue igual de qualquer jeito? Roteiro que não ramifica é questionário.

**Questões exploratórias:**

- Qual pergunta do roteiro você não teria coragem de fazer ao dono do produto? O que isso diz sobre a pergunta, ou sobre a relação?
- O roteiro pressupõe alguma resposta? Uma pergunta que já embute a resposta esperada só serve para confirmar o que você já achava.

## Evidência a entregar

Cinco itens, verificáveis contra o mesmo projeto de exemplo:

1. As perguntas do passo 1 do Experimento A, escritas antes de abrir as respostas.
2. A especificação BR/FR escrita no passo 3 do Experimento A, e o resultado de `node --test` no passo 5, com os seis testes originais e os casos novos.
3. O cenário de qualidade do Experimento B (os seis elementos) e a função de aptidão correspondente.
4. O dossiê do Experimento C, com o registro de proveniência e as perguntas abertas, mais a contagem de violações do contrato de mensagem.
5. Uma frase respondendo qual informação o dossiê registrou que a análise direta do Experimento D não tinha como produzir.

**Próxima página:** [Exercícios](exercicios.md).
