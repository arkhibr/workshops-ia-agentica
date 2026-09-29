# Exercício de IA — Especialista: casos de teste em TDD

Este exercício parte do mapa de regras do cashback do IBS e da CBS produzido no exercício geral, formalizado a partir dos arts. 112, 113, 116, 117 e 118 do [texto compilado da Lei Complementar nº 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm), consultado em 29 de setembro de 2026. O objetivo é converter regras verificadas em casos de teste antes de qualquer implementação, seguindo TDD (*Test-Driven Development*, prática em que o teste é escrito e visto falhando antes do código que o satisfaz).

## Entrada obrigatória

Use o mapa com conceitos, fatos, regras estruturais, regras operativas, exceções, conflitos, lacunas, evidência e confiança. Se o mapa ainda chama de regra operativa uma derivação de percentual ou uma classificação de pessoa, corrija o tipo e o prefixo do ID antes do Passo 1, porque cada teste herda o ID da regra de origem.

![Fluxo em duas faixas. Na faixa do exercício geral, a fonte pública (LC 214/2025, texto compilado) segue para a marcação inicial feita pelo participante, o mapa de regras gerado pelo agente com RC, RD, RN, evidência e LACUNA, a revisão por camada e a tabela de decisão com política de acerto e precedência. O mapa revisado é a entrada da faixa do exercício especialista, que segue por regras testáveis, matriz de testes gerada pelo agente, crítica da matriz e ciclo TDD de vermelho, verde e refatorar, e termina em test.todo para cada caso INDETERMINADO.](assets/fluxo-regra-tributaria.png)

*Leitura da figura: esta página cobre a faixa inferior, que recebe o mapa revisado no exercício geral. A etiqueta de cada caixa indica quem executa o passo, e o último quadro, pontilhado, recebe os casos INDETERMINADO registrados como `test.todo`.*

## Passo 1 — selecione regras testáveis

Escolha regras com saída observável:

- classificação de pessoa destinatária pelos quatro critérios cumulativos do art. 113
- exclusão por cada critério não satisfeito
- classificação da categoria da aquisição
- exclusão de item sujeito ao Imposto Seletivo
- escolha dos percentuais de CBS e IBS
- momento da devolução quando a fonte o determina

Dependência de regulamento continua como dependência na matriz. Quando a fonte não determinar o resultado, registre um teste pendente com a questão de domínio que o desbloqueia, e **não invente** valor, data ou comportamento para completar o caso.

## Passo 2 — peça uma matriz de testes

```text
Você receberá um mapa de regras formalizado a partir dos arts. 112, 113,
116, 117 e 118 da LC 214/2025 compilada. Proponha casos de teste antes de
qualquer implementação, seguindo TDD.

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

## Passo 3 — critique a matriz

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

## Passo 4 — execute o ciclo TDD

O ciclo usa JavaScript com o executor de testes nativo do Node.js (`node:test`), que dispensa instalação de pacotes e roda com Node 20 ou superior. Todos os participantes partem do mesmo esqueleto, publicado nesta página, para que as saídas das duplas sejam comparáveis.

**Passo 4.1:** crie a pasta do exercício com os comandos abaixo, que funcionam no PowerShell do Windows, no macOS e no Linux.

```bash
mkdir cashback-tdd
cd cashback-tdd
mkdir src
mkdir test
```

**Passo 4.2:** crie `src/cashback.mjs` com o conteúdo abaixo. As duas funções começam sem comportamento.

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

**Passo 4.3:** crie `test/cashback.test.mjs` com o primeiro caso da matriz e um caso indeterminado registrado como `todo`.

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

**Passo 4.4:** rode a suíte e confirme que T-01 falha com a mensagem “ainda não foi implementada” e que T-90 aparece como `todo`.

```bash
node --test
```

**Passo 4.5:** implemente e passe pelo ciclo vermelho, verde e refatorar três casos confirmados da matriz, um de cada vez. Para cada caso, escreva o teste com o ID da regra e o artigo no comentário, rode `node --test` e confirme a falha, implemente em `src/cashback.mjs` apenas o necessário para o caso passar, rode a suíte inteira de novo e refatore sem alterar o resultado.

A implementação se limita às duas funções do esqueleto: `classificarDestinatario` recebe a pessoa e o salário-mínimo hipotético e devolve `DESTINATARIO`, `NAO_DESTINATARIO` ou `INDETERMINADO`. `percentuaisDevolucao` recebe a aquisição e devolve os percentuais de CBS e IBS, `FORA_DO_CALCULO` ou `INDETERMINADO`. O restante da matriz permanece como especificação, e todo caso INDETERMINADO entra como `test.todo` com a pergunta que o desbloqueia.

## Evidência a entregar

Entregue a matriz revisada, a saída de `node --test` com os três casos verdes e os casos `todo`, e uma explicação de por que a ordem escolhida para os três casos reduz risco. Inclua ao menos um caso que permaneceu INDETERMINADO por lacuna real da fonte e o caso de precedência entre o Imposto Seletivo e o art. 118, I.

**Próxima página:** [Arqueologia de regras em SQL](arqueologia-de-regras-sql.md).
