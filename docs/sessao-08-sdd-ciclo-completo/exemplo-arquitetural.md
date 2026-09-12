# Exemplo arquitetural

Esta demonstração percorre o ciclo completo na Vetor, plataforma fictícia de e-commerce B2B usada no workshop, fechando a lacuna da faixa de atacado. O instrutor conduz, e o participante observa onde cada artefato toma uma decisão que o anterior não tinha como tomar.

O estado inicial é o mesmo que a oficina monta do zero: a função `calcularDesconto` recebe `tipoCliente` e não usa esse parâmetro em lugar nenhum. Existe um teto de desconto de R$ 1.000,00 por pedido. As faixas atuais são 0% até R$ 500,00, 5% de R$ 500,01 a R$ 2.000,00, 10% de R$ 2.000,01 a R$ 5.000,00 e 15% acima de R$ 5.000,00.

O pedido que chega é o de sempre: "ativa o desconto de atacado, 20% acima de dez mil".

## Constitution: o que já vale antes deste pedido

A Vetor tem três princípios versionados. Repare que cada um nomeia quem barra o quê:

```markdown
# Constituição — Vetor
Versão 1.1 · dono: arquitetura

1. Regra de precificação nunca fica implícita no código.
   Consequência: mudança em desconto sem requisito escrito e caso de
   fronteira é devolvida na revisão de aderência.

2. Comportamento novo começa por um teste que falha pelo motivo esperado.
   Consequência: entrega cujo primeiro commit já traz implementação é
   devolvida, mesmo com a suíte verde no final.

3. Função pública de cálculo mantém assinatura compatível.
   Consequência: alterar a assinatura de calcularDesconto exige plano de
   migração e decisão registrada do dono do produto.
```

O terceiro princípio já elimina uma saída que o agente costuma propor sozinho: trocar a assinatura da função para receber um objeto de configuração. Não está proibido, está condicionado a um plano e uma decisão registrada.

## Specify: o que o usuário passa a poder fazer

A especificação descreve o comportamento, sem decidir estrutura interna:

```markdown
## FR-001
O sistema deve aplicar 20% de desconto a pedidos de cliente do tipo
atacado cujo valor total seja superior a R$ 10.000,00.

Caso concreto: valorTotal = 12000, tipoCliente = 'atacado' → desconto = 2400.
Caso de fronteira: valorTotal = 10000, tipoCliente = 'atacado' → faixa
anterior, não os 20%.

## FR-002
O sistema deve preservar as faixas atuais para cliente do tipo padrão.

Caso concreto: valorTotal = 12000, tipoCliente = 'padrao' → faixa de 15%.
```

O caso concreto de FR-001 diz `desconto = 2400`. Essa linha é a razão de a próxima etapa existir.

## Clarify: a ambiguidade que muda a solução

O teto de R$ 1.000,00 já existe e vale para todos os pedidos. Vinte por cento de R$ 12.000,00 são R$ 2.400,00. O pedido original não disse nada sobre isso, e há três respostas possíveis, todas defensáveis:

1. O teto continua valendo, e o desconto de atacado fica limitado a R$ 1.000,00. Nesse caso, a faixa de 20% quase nunca produz efeito diferente da faixa de 15%, e o pedido perde sentido prático.
2. O teto não se aplica ao atacado. Precisa ser dito explicitamente, porque muda o risco financeiro por pedido.
3. O teto sobe para o atacado, com um valor novo. Alguém precisa decidir qual.

Esta é a pergunta que separa o ciclo disciplinado do agente que escolhe sozinho. Sem clarificação, o modelo vai adotar uma das três, provavelmente a primeira, porque é a que exige menos alteração no código existente. E a decisão financeira do negócio terá sido tomada por um critério de conveniência de implementação.

A decisão registrada, para esta demonstração, é a segunda: o teto não se aplica ao atacado. O registro entra na especificação:

```markdown
## BR-004
O teto de desconto de R$ 1.000,00 aplica-se apenas a cliente do tipo padrão.
Decisão de 12/09/2026, dono do produto. Motivo: o teto foi criado para
limitar risco no varejo, e o contrato de atacado já tem limite por volume.
```

## Plan: como a arquitetura realiza isso

O plano registra as decisões técnicas e o que foi descartado:

```markdown
## Decisão: tabela de faixas por tipo de cliente
Substituir a cadeia de if por uma tabela de faixas indexada por tipoCliente.
Alternativa descartada: novo parâmetro booleano aplicarTeto — rejeitada
porque viola o princípio 3 da constituição (assinatura compatível) e
espalha a regra de teto para quem chama a função.

## Decisão: teto como propriedade da faixa
O teto deixa de ser constante global aplicada no final e passa a ser um
campo de cada faixa, com valor Infinity nas faixas de atacado.
Consequência: a regra BR-004 fica expressa na estrutura de dados, não
num if adicional.
```

A segunda decisão é a que um agente sem plano dificilmente tomaria. A saída mais direta seria um `if (tipoCliente !== 'atacado')` em volta do `Math.min`, que funciona e espalha a regra por mais um ponto do código.

## Tasks: fatias verticais

```markdown
- [ ] T1. Tabela de faixas para 'padrao' reproduzindo o comportamento atual,
      com a suíte existente passando sem alteração. Teste: os seis casos atuais.
- [ ] T2. Faixa de atacado acima de 10.000 a 20%, sem teto.
      Teste: 12000/'atacado' → 2400, e 10000/'atacado' → faixa anterior.
- [ ] T3. Atacado nas faixas abaixo de 10.000 herda o comportamento padrão.
      Teste: 3000/'atacado' → 300.
```

T1 não entrega comportamento novo, e ainda assim é a primeira: ela troca a estrutura mantendo o comportamento observável, o que torna T2 uma adição pequena e verificável. É refatoração antes da funcionalidade, e o critério de pronto é a suíte antiga continuar verde.

## Implement: o teste que falha primeiro

O princípio 2 da constitution exige observar a falha antes de escrever a implementação:

```javascript
// test/desconto.test.js
it('da 20% no atacado acima de 10.000, sem teto', () => {
  assert.equal(calcularDesconto(12000, 'atacado'), 2400);
});
```

Rodar e ver falhar com `2400 !== 1000` é a evidência de que o teste alcança a regra certa: o valor retornado é o teto antigo, exatamente o comportamento que BR-004 mudou. Uma falha com `2400 !== 1800` indicaria que a faixa foi aplicada errado, e uma falha de sintaxe indicaria que o teste não chegou a exercitar nada.

## Verify: os dois eixos

A revisão de **aderência** confere FR-001, FR-002 e BR-004 contra o código, e pergunta se alguma decisão de produto foi tomada durante a implementação sem passar pela especificação.

A revisão de **qualidade** confere se a tabela de faixas segue as convenções do repositório, se os nomes expressam o domínio e se os testes observam comportamento pela interface pública em vez de espelhar a estrutura interna.

Um "passa" na segunda não compensa uma falha na primeira. Um código elegante que aplica o teto ao atacado continua resolvendo o problema errado.

## Leitura do exemplo

O ponto de maior valor do ciclo inteiro não foi nenhum artefato, foi a pergunta da etapa de clarificação. O conflito entre o teto de R$ 1.000,00 e os 20% de R$ 12.000,00 estava presente desde o pedido original, invisível, e qualquer fluxo que fosse direto do pedido ao código teria resolvido esse conflito por acidente.

Um agente competente teria produzido código que passa em testes que ele mesmo escreveu, com o teto aplicado, e ninguém teria motivo para desconfiar. A regra financeira do negócio teria sido decidida pela ordem das linhas na função.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
