# BR, FR e NFR

Três perguntas diferentes escondidas numa especificação mal escrita: qual é a regra que o negócio impõe, o que o sistema precisa fazer, e sob que restrição de qualidade ele precisa fazer isso. Confundir as três produz uma especificação de aparência completa, com decisões de negócio ausentes do texto escrito.

## As três categorias

**Regra de negócio (BR, *business rule*)** é uma declaração sobre como o negócio funciona, independente de haver software ou não. [Ross](../referencia/bibliografia.md#ross-ed-business-rules-manifesto-2003), no *Business Rules Manifesto*, é categórico: "regras não são processo nem procedimento" e devem ser expressas de forma declarativa, sem sequenciamento implícito. Uma regra declara *o que vale* em qualquer momento, sem prescrever *em que ordem fazer*. "O desconto de um pedido nunca ultrapassa um teto fixo em reais" é uma regra de negócio: valeria mesmo que o cálculo fosse feito numa planilha, sem nenhum sistema.

**Requisito funcional (FR, *functional requirement*)** é o que o software precisa fazer para que a regra de negócio se cumpra. "O sistema calcula o desconto de um pedido a partir do valor total e do tipo de cliente" é funcional: descreve comportamento observável do sistema, não existe fora dele.

**Requisito não funcional (NFR, *non-functional requirement*)**, no vocabulário da norma [ISO/IEC/IEEE 29148](../referencia/bibliografia.md#isoiecieee-291482018), não descreve uma ação específica, mas um critério para julgar como o sistema executa a ação: desempenho, usabilidade, segurança. "O cálculo de desconto responde em menos de 100ms" é não funcional. O sistema já calcula desconto, e isso é o FR. A norma de qualidade diz o quão rápido isso precisa acontecer.

| Categoria | Pergunta que responde | Existiria sem o sistema? | Exemplo genérico |
|---|---|---|---|
| BR | O que o negócio permite, exige ou proíbe? | Sim | Desconto por volume nunca passa de um teto fixo |
| FR | O que o sistema precisa fazer? | Não | Calcular o desconto a partir de valor e tipo de cliente |
| NFR | Sob que critério de qualidade? | Não | Responder em menos de 100ms, sob qualquer carga |

## O que a distinção muda na prática

[Wiegers e Beatty](../referencia/bibliografia.md#wiegers-e-beatty-software-requirements-2013) tratam regra de negócio como categoria anterior aos requisitos de software, em vez de um requisito em si. Uma regra de negócio também vale para operação manual, fora de qualquer sistema, e é dela que os requisitos funcionais derivam. Essa ordem importa para quem escreve um pedido a um agente, porque a regra de negócio é a fonte de verdade da qual o requisito funcional deriva como tradução em comportamento de sistema, e o requisito não funcional entra depois dos dois, como restrição de qualidade sobre esse comportamento.

Confundir as três produz sintomas previsíveis. Uma regra de negócio escrita como requisito funcional ("o sistema deve limitar o desconto a R$ 1.000,00") esconde que o limite é uma decisão de negócio, e não uma escolha de implementação. Se o negócio mudar o teto amanhã, ninguém vai procurar essa mudança na especificação funcional. Um requisito não funcional escrito como regra de negócio ("o sistema deve ser rápido") não diz nada verificável, porque "rápido" é uma medida de engenharia que só significa alguma coisa com um número junto.

!!! question "Antes de continuar"
    Releia a última especificação que você escreveu ou recebeu. Alguma frase que parecia requisito funcional era, na verdade, regra de negócio disfarçada, algo que valeria mesmo sem o sistema existir?

## O antipadrão do requisito funcional que esconde uma regra

O sintoma mais comum é uma frase só, funcional na forma, carregando três regras de negócio dentro dela: "o sistema deve aplicar desconto de 20% para pedidos de atacado acima de R$ 10.000,00, respeitando o teto de R$ 1.000,00". As três regras são a existência da faixa de atacado, o valor de corte e a prevalência do teto. Quando a regra de negócio muda, e o corte passa para R$ 8.000,00, alguém precisa reabrir a especificação funcional inteira para encontrar o número certo a trocar, porque a regra nunca teve linha própria.

A correção é prática. Regra de negócio ganha frase própria, numerada, antes do requisito funcional que a implementa. É isso que permite ao agente tratar "o teto é R$ 1.000,00" como restrição válida para qualquer faixa nova, em vez de detalhe da faixa de atacado que ele pode reinterpretar.

## Para o time de negócio

As três categorias moram em artefatos diferentes do seu lado, e confundi-las faz com que uma decisão
comercial seja registrada como detalhe técnico dentro de um item de backlog.

| Categoria | Onde ela vive | Quem aprova mudança | O que acontece se ela mudar |
|---|---|---|---|
| Regra de negócio | Política comercial escrita, numerada e datada | Área demandante | O número muda num lugar só, e todo item que a referencia continua válido |
| Requisito funcional | Item de backlog, com critério de aceitação | Produto, com a área demandante | O item é reescrito, e a regra permanece como está |
| Requisito não funcional | Acordo de nível de serviço do produto | Produto, com quem opera o sistema | A medida é renegociada, com prazo e responsável |

O teste que separa a regra de negócio do requisito funcional é perguntar se a frase continuaria
verdadeira caso o trabalho fosse feito numa planilha, sem sistema nenhum. "O desconto de um pedido
nunca ultrapassa R$ 1.000,00" continuaria. "A tela de fechamento exibe o desconto aplicado antes da
confirmação" não continuaria, porque depende da existência da tela.

O antipadrão aparece quando a regra chega ao time embutida na descrição do item, sem número próprio.
A frase "o sistema deve aplicar desconto de 20% para atacado acima de R$ 10.000,00, respeitando o teto
de R$ 1.000,00" carrega três regras distintas, e nenhuma delas tem identificador. Quando a gerência
comercial decidir mudar o valor de corte, alguém vai precisar abrir os itens de backlog um a um para
descobrir onde o número está escrito.

## Para o time de desenvolvimento

As três categorias não param na especificação. Cada uma aponta para uma parte diferente do código e do teste.

```text
BR-02: O desconto de um pedido nunca ultrapassa R$ 1.000,00,
       qualquer que seja a faixa aplicada.
FR-02: calcularDesconto aplica Math.min entre o valor calculado
       e o teto, antes de retornar.
NFR-01: calcularDesconto responde em menos de 100ms mesmo com
        500 chamadas concorrentes.
```

BR-02 não menciona `Math.min` nem `TETO_DESCONTO`, porque valeria mesmo numa planilha. FR-02 já é a tradução dela em comportamento de sistema, e aparece como uma linha específica do código:

```javascript
export const TETO_DESCONTO = 1000;

export function calcularDesconto(valorTotal, tipoCliente) {
  // ...
  return Math.min(valorTotal * percentual, TETO_DESCONTO); // FR-02
}
```

NFR-01 aparece num teste separado, fora do corpo da função. Um requisito não funcional se verifica medindo o tempo de execução, e a medição precisa do seu próprio arquivo:

```javascript
// test/desconto.perf.test.js
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { calcularDesconto } from '../src/desconto.js';

test('NFR-01: calcula 500 descontos em menos de 100ms', () => {
  const inicio = performance.now();
  for (let i = 0; i < 500; i += 1) {
    calcularDesconto(12000, 'atacado');
  }
  const duracaoMs = performance.now() - inicio;
  assert.ok(duracaoMs < 100, `levou ${duracaoMs}ms`);
});
```

Cada categoria tem seu próprio lugar natural: BR na frase de negócio, FR na linha do código de produção, NFR num teste que mede tempo em vez de comparar valor. Um pedido como "o sistema deve ser rápido" não contém o limiar, a quantidade de amostras nem o critério de falha, que são os três dados de que o teste acima depende.

**Próxima página:** [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md).
