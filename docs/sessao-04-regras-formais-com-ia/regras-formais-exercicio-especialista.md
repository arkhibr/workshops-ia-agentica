# Exercício de IA — Especialista: casos de teste em TDD

Este exercício converte regras do cashback do IBS e da CBS em casos de teste antes de qualquer implementação, seguindo TDD (*Test-Driven Development*, prática em que o teste é escrito e visto falhando antes do código que o satisfaz). A trilha especialista corre no mesmo horário da trilha geral e parte do texto-base publicado nesta página, a partir do qual o agente gera um mapa reduzido no Passo 1 com as mesmas convenções do SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG que separa conceitos, fatos e regras) usadas na outra trilha.

## Fonte pública

Use o [texto compilado da Lei Complementar nº 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm), publicado pela Presidência da República com as alterações da Lei Complementar nº 227/2026 e consultado em 29 de setembro de 2026, com atenção aos artigos 112, 113, 116, 117 e 118 e ao artigo 124, que define “devolução geral” e “devolução específica”. O texto compilado é a única fonte do exercício, e em caso de divergência entre ele e qualquer síntese desta página prevalece o texto legal.

## Texto complexo para decompor

> [1] A devolução de IBS e CBS destina-se ao responsável por unidade familiar de baixa renda cadastrada no CadÚnico quando essa pessoa, cumulativamente, tiver renda familiar mensal per capita de até meio salário-mínimo, residir no território nacional e possuir inscrição regular no CPF. [2] No cálculo entra o consumo documentado por notas vinculadas ao CPF dos membros da unidade familiar, desde que a aquisição seja exclusivamente para consumo domiciliar, [3] “ressalvados os bens e serviços sujeitos ao Imposto Seletivo”. [4] Na aquisição de botijão de gás liquefeito de petróleo de até 13 kg, no fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e no fornecimento de telecomunicações, a devolução geral corresponde a 100% da CBS e 20% do IBS, e nos demais casos corresponde a 20% de cada tributo. [5] No fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e nos serviços de telecomunicações, a devolução é concedida no momento da cobrança, e nos demais casos no momento definido em regulamento. [6] Cada ente pode, por lei específica, fixar percentual superior para sua parcela, exceto no percentual da CBS aplicado às categorias da frase [4]. [7] A diferença entre o valor apurado com esse percentual próprio e a devolução geral chama-se devolução específica. [8] Os valores são disponibilizados ao agente financeiro no prazo máximo de 15 dias após a apuração, e o agente financeiro deve transferi-los às famílias destinatárias em até 10 dias após essa disponibilização.

!!! info "Natureza de cada frase"
    O bloco é uma **síntese didática** montada para a aula. A tabela indica, frase por frase, se o trecho é paráfrase ou transcrição e de que dispositivo ele vem, para que a evidência do mapa possa ser conferida no texto compilado.

| Frase | Natureza | Dispositivo da LC 214/2025 |
|---|---|---|
| [1] | paráfrase | art. 112, caput, e art. 113, caput e incisos I a III |
| [2] | paráfrase | art. 117, caput e §2º, II |
| [3] | transcrição literal | art. 117, §2º, I, com redação dada pela LC 227/2026 |
| [4] | paráfrase | art. 118, I e II, e art. 124, I |
| [5] | paráfrase | art. 116, caput e §1º |
| [6] | paráfrase | art. 118, §§1º e 3º |
| [7] | paráfrase | art. 124, II |
| [8] | paráfrase | art. 116, §§3º e 4º |

A lista da frase [5] tem cinco categorias e a da frase [4] tem seis, porque o art. 116, §1º, menciona energia elétrica, água, esgoto, gás canalizado e telecomunicações, enquanto o botijão de gás liquefeito de petróleo aparece apenas no art. 118, I. O mapa precisa representar essa diferença em duas regras distintas, uma para o percentual e outra para o momento da devolução.

![Fluxo em duas faixas independentes que partem da mesma caixa, Fonte pública (LC 214/2025, texto compilado). A faixa Geral segue pela marcação inicial feita pelo participante, pelo mapa completo das seções A a I gerado pelo agente, pela revisão por camada e pela tabela de decisão com política de acerto e precedência. A faixa Especialista segue pelo mapa reduzido às seções A, C, D, F e G gerado pelo agente, pelas regras testáveis, pela matriz de testes, pela crítica da matriz e pelo ciclo TDD de vermelho, verde e refatorar, e termina em test.todo para cada caso INDETERMINADO. Nenhuma seta liga as duas faixas.](assets/fluxo-regra-tributaria.png)

*Leitura da figura: esta página cobre a faixa Especialista, a inferior, que parte da mesma fonte pública da faixa Geral e gera o próprio mapa reduzido no Passo 1. A etiqueta de cada caixa indica quem executa o passo, e o último quadro, pontilhado, recebe os casos INDETERMINADO registrados como `test.todo`.*

## Passo 1 — gere o mapa reduzido (8 a 10 minutos)

O mapa reduzido traz apenas as seções de que a matriz de testes precisa: conceitos, classificação, derivação, exceções e controles. O prompt usa seis prefixos de identificação e quatro rótulos de controle, definidos na lista abaixo para que a saída de duplas com agentes diferentes possa ser comparada:

- **CT**: conceito do vocabulário, definido por gênero e diferença.
- **FT**: tipo de fato, que liga conceitos por meio de um verbo.
- **RC**: regra estrutural de classificação, que diz quando algo pertence a uma categoria.
- **RD**: regra estrutural de derivação, que diz como um valor é calculado.
- **RN**: regra operativa, que rege a conduta de um ator capaz de descumpri-la.
- **EX**: regra de exceção, que referencia o ID da regra que ela afeta.
- **T**: caso de teste, usado a partir do Passo 3 e ausente do prompt deste passo.
- **LACUNA**: ponto a que a fonte não responde.
- **REGULAMENTO**: ponto que a fonte remete a regulamento.
- **CONFLITO**: par de regras que não podem valer ao mesmo tempo.
- **INFERÊNCIA**: conclusão do agente que não consta da fonte.

Cole no agente o texto complexo, a tabela de natureza das frases, o link oficial e este prompt:

```text
Atue como analista de regras de negócio e formalize o texto fornecido no
vocabulário do SBVR (OMG), com sentenças no estilo RuleSpeak em português.

ENTRADA
- Frases numeradas [1] a [8]: síntese didática dos arts. 112, 113, 116, 117,
  118 e 124 da LC 214/2025, texto compilado. Só a frase [3] é transcrição
  literal, e as demais são paráfrases.
- Tabela que liga cada frase ao dispositivo legal.
- Link do texto compilado. Se não conseguir abri-lo, trabalhe só com o texto
  e a tabela e declare isso no início da resposta.

LIMITES
- Não ofereça orientação jurídica e não use artigos fora da lista acima.
- Não apresente paráfrase como texto de lei: transcreva trecho legal apenas
  se você o leu no link e, nos demais casos, cite a frase [n] e o dispositivo
  da tabela.
- Quando transcrever trecho legal lido no link, use o menor fragmento que
  sustenta a regra.
- Diante de lacuna, não invente resposta, data ou valor: registre LACUNA e
  formule a pergunta na seção G.

CONVENÇÕES
1. Vocabulário antes das regras. Toda regra usa apenas conceitos da seção A
   e tipos de fato da seção B. Termo novo entra primeiro em A.
2. Conceito (CT-nn): termo, definição por gênero e diferença ("X é um Y
   que ..."), sinônimos a evitar, frase de origem.
3. Tipo de fato (FT-nn): "<conceito> <verbo> <conceito>", leitura inversa e
   cardinalidade. Cardinalidade não informada pela fonte recebe LACUNA.
4. Regra estrutural, de modalidade alética, que nenhum ator descumpre:
   - classificação RC-nn: "Um <conceito> é um <conceito> se ..."
   - derivação RD-nn: "<valor> é calculado como ...".
   Percentuais, passos de cálculo, critérios de inclusão num total e limites
   de valor são sempre regras estruturais.
5. Regra operativa RN-nn, de modalidade deôntica, somente quando existe um
   ator que pode descumpri-la: "<ator> deve ...", "<ator> não deve ...",
   "<ator> pode ... somente se ...". Se a fonte não nomear o ator, registre
   LACUNA e não atribua ator por conta própria.
6. Uma regra por sentença, com um único efeito. Cláusulas com "salvo",
   "exceto" ou "desde que" são registradas como regra de exceção EX-nn, que
   referencia o ID da regra afetada.
7. Rótulos de controle: LACUNA (a fonte não responde), REGULAMENTO (a fonte
   remete a regulamento), CONFLITO (duas regras não podem valer juntas),
   INFERÊNCIA (conclusão sua, ausente da fonte).

SAÍDA reduzida, uma tabela por seção
A. Conceitos: ID | termo | definição | sinônimos a evitar | frase
C. Classificação: ID | sentença | evidência | confiança | pergunta de validação
D. Derivação: mesmas colunas de C
F. Exceções e precedência: ID | regra afetada | sentença | qual prevalece e
   por quê
G. Controles: rótulo | descrição | frase | pergunta

As seções B, E, H e I do mapa completo ficam fora desta saída. Quando uma
regra depender de um tipo de fato, escreva o fato por extenso na sentença.
Regras operativas RN ficam fora desta saída, porque a matriz de testes cobre
classificação, derivação e exceção.

Evidência: frase [n] e dispositivo (artigo, parágrafo, inciso).
Confiança: alta (texto explícito), média (uma inferência), baixa (depende de
interpretação).

Antes de responder, confira se nenhuma regra de C ou D descreve conduta de
um ator, se todo termo usado nas regras está em A e se toda cláusula de
exceção está em F.
```

Antes do Passo 2, confira se o mapa chama de regra operativa uma derivação de percentual ou uma classificação de pessoa e, nesse caso, corrija o tipo e o prefixo do ID, porque cada teste herda o ID da regra de origem. A partir do Passo 3, o prefixo T identifica caso de teste.

## Passo 2 — selecione regras testáveis

Escolha regras com saída observável:

- classificação de pessoa destinatária pelos quatro critérios cumulativos do art. 113
- exclusão por cada critério não satisfeito
- classificação da categoria da aquisição
- exclusão de item sujeito ao Imposto Seletivo
- escolha dos percentuais de CBS e IBS
- momento da devolução quando a fonte o determina

Dependência de regulamento continua como dependência na matriz. Quando a fonte não determinar o resultado, registre um teste pendente com a questão de domínio que o desbloqueia, e **não invente** valor, data ou comportamento para completar o caso.

## Passo 3 — peça uma matriz de testes

```text
Você receberá um mapa de regras formalizado a partir dos arts. 112, 113,
116, 117, 118 e 124 da LC 214/2025 compilada. Proponha casos de teste antes
de qualquer implementação, seguindo TDD.

Para cada caso, devolva:
- ID do teste;
- ID da regra de origem;
- cenário em linguagem de negócio;
- dados de entrada mínimos;
- resultado esperado;
- partição ou fronteira coberta;
- evidência legal, com o menor fragmento da fonte que a sustenta;
- justificativa;
- confiança.

Cubra: caminho nominal, cada critério cumulativo ausente, fronteiras de
renda, CPF irregular, residência fora do território nacional, documento
não vinculado ao CPF de membro da unidade familiar, consumo não
domiciliar, item sujeito ao Imposto Seletivo, botijão acima de 13 kg,
categorias com percentuais distintos, sobreposição, precedência entre a
ressalva do Imposto Seletivo (art. 117, §2º, I) e os percentuais do
art. 118, I, e dado ausente.

Para conflito ou lacuna, não invente resultado. Marque o caso como
INDETERMINADO e formule a pergunta que desbloqueia o teste.
```

## Passo 4 — critique a matriz

Procure na matriz os quatro defeitos abaixo:

1. **teste sem regra de origem**, que perde a rastreabilidade até o artigo
2. **teste com dados demais**, que esconde qual entrada mudou o resultado
3. **teste de fórmula sem classificação**, em que o percentual pode estar certo para a categoria errada
4. **resultado inventado**, em que o agente fechou uma lacuna que dependia de regulamento ou validação jurídica

## Matriz mínima esperada

| Classe | Exemplo de caso | Resultado |
|---|---|---|
| Nominal | pessoa satisfaz os quatro critérios e compra energia elétrica domiciliar documentada | 100% da CBS e 20% do IBS (art. 118, I) |
| Fronteira | renda per capita exatamente igual a meio salário-mínimo | destinatária quanto à renda |
| Fora da fronteira | renda um centavo acima do limite | não destinatária quanto à renda |
| Exceção | item sujeito ao Imposto Seletivo em categoria dos demais casos | fora do consumo considerado (art. 117, §2º, I) |
| Sobreposição | aquisição de energia elétrica domiciliar, que atende ao inciso I e poderia ser lida como “demais casos” do inciso II | percentuais do inciso I, pois o inciso II se aplica apenas aos casos não listados no inciso I |
| Precedência | item sujeito ao Imposto Seletivo que também pertence a uma categoria do art. 118, I | fora do consumo considerado, porque o art. 118 aplica o percentual “nos termos do art. 117”, e a ressalva delimita o consumo antes da escolha do percentual (confiança média, com pergunta para revisão jurídica) |
| Limite de ampliação | lei específica que tenta fixar percentual superior para a CBS de categoria do inciso I | percentual da CBS mantido em 100% (art. 118, §3º) |
| Ausência | categoria ou vínculo fiscal não informado | INDETERMINADO, sem inferência |

## Passo 5 — execute o ciclo TDD

O ciclo usa JavaScript com o executor de testes nativo do Node.js (`node:test`), que dispensa instalação de pacotes e roda com Node 20 ou superior. Todos os participantes partem do mesmo esqueleto, publicado nesta página, para que as saídas das duplas sejam comparáveis.

**Passo 5.1:** crie a pasta do exercício com os comandos abaixo, que funcionam no PowerShell do Windows, no macOS e no Linux.

```shell
mkdir cashback-tdd
cd cashback-tdd
mkdir src
mkdir test
```

**Passo 5.2:** crie `src/cashback.mjs` com o conteúdo abaixo. As duas funções começam sem comportamento.

```javascript
// Esqueleto do exercício especialista da Sessão 4.
// As duas funções começam sem comportamento: cada teste novo falha antes da implementação.

export function classificarDestinatario(pessoa, parametros) {
  throw new Error("classificarDestinatario ainda não foi implementada");
}

export function percentuaisDevolucao(aquisicao) {
  throw new Error("percentuaisDevolucao ainda não foi implementada");
}
```

**Passo 5.3:** crie `test/cashback.test.mjs` com o primeiro caso da matriz e um caso indeterminado registrado como `todo`.

```javascript
import { test } from "node:test";
import assert from "node:assert/strict";
import { classificarDestinatario, percentuaisDevolucao } from "../src/cashback.mjs";

// Valor hipotético, fixado para a aula. Não é o salário-mínimo vigente.
const parametros = { salarioMinimo: 1600.0 };

// T-01 | regra RC-01 do seu mapa | art. 113, caput e incisos I a III | partição nominal
test("T-01 responsável que satisfaz os quatro critérios é destinatário", () => {
  const pessoa = {
    responsavelCadUnico: true,
    rendaPerCapita: 500.0,
    residenteNoBrasil: true,
    cpfRegular: true,
  };
  assert.equal(classificarDestinatario(pessoa, parametros), "DESTINATARIO");
});

// Casos INDETERMINADO ficam registrados como todo, com a pergunta que os desbloqueia.
test.todo("T-90 renda per capita ausente: a ausência impede a classificação ou exige consulta ao CadÚnico?");
```

**Passo 5.4:** rode a suíte e confirme que T-01 falha com a mensagem “ainda não foi implementada” e que T-90 aparece como `todo`.

```shell
node --test
```

**Passo 5.5:** implemente e passe pelo ciclo vermelho, verde e refatorar três casos confirmados da matriz, um de cada vez. Para cada caso, escreva o teste com o ID da regra e o artigo no comentário, rode `node --test` e confirme a falha, implemente em `src/cashback.mjs` apenas o necessário para o caso passar, rode a suíte inteira de novo e refatore sem alterar o resultado.

A implementação se limita às duas funções do esqueleto: `classificarDestinatario` recebe a pessoa e o salário-mínimo hipotético e devolve `DESTINATARIO`, `NAO_DESTINATARIO` ou `INDETERMINADO`. `percentuaisDevolucao` recebe a aquisição e devolve os percentuais de CBS e IBS, `FORA_DO_CALCULO` ou `INDETERMINADO`. O restante da matriz permanece como especificação, e todo caso INDETERMINADO entra como `test.todo` com a pergunta que o desbloqueia.

## Evidência a entregar

Entregue a matriz revisada, a saída de `node --test` com os três casos verdes e os casos `todo`, e uma explicação de por que a ordem escolhida para os três casos reduz risco. Inclua ao menos um caso que permaneceu INDETERMINADO por lacuna real da fonte e o caso de precedência entre o Imposto Seletivo e o art. 118, I.

**Próxima página:** [Conceitos: arqueologia de regras](arqueologia-de-regras-conceitos.md).
