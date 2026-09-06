# Vetor — projeto de exemplo do workshop

A Vetor é uma plataforma fictícia de e-commerce B2B que atravessa as dez sessões do workshop. Este diretório é a versão executável dela: o mínimo necessário para as oficinas terem um ponto de partida idêntico para todo mundo.

## Pré-requisitos

Node.js 20 ou superior. Nada além disso: o projeto **não tem dependências** e usa o executor de testes embutido no próprio Node, então não existe `npm install` nem espera de instalação no meio da aula.

```bash
node --version   # precisa mostrar v20 ou superior
npm test         # deve terminar com 6 testes passando
```

## O que tem aqui

| Arquivo | Conteúdo |
|---|---|
| `src/desconto.js` | A regra de desconto por faixa de valor, com teto de R$ 1.000,00 por pedido |
| `test/desconto.test.js` | Seis testes cobrindo as quatro faixas, o teto e a entrada inválida |
| `package.json` | Os comandos `npm test` e `npm run verificar`, sem dependências |

## Uma lacuna proposital

`calcularDesconto` recebe `tipoCliente` e não usa esse parâmetro. Isso não é um defeito esquecido: a regra completa da Vetor prevê uma faixa adicional de 20% para clientes de atacado acima de R$ 10.000,00, ainda respeitando o teto, e essa faixa **não está implementada de propósito**. É a lacuna que as oficinas pedem ao agente para preencher, e é o que permite comparar o resultado de um pedido vago com o de um pedido feito num ambiente configurado.

A regra completa, com a tabela de faixas, está em [Exemplo arquitetural da Sessão 1](https://arkhibr.github.io/workshops-ia-agentica/sessao-01-o-que-mudou/exemplo-arquitetural/).

## Convenções que o agente precisa saber

Estas são as convenções reais do projeto, e algumas delas não dá para deduzir lendo o código. Elas existem aqui para a Sessão 2 ter o que colocar num arquivo de instrução:

- O comando de teste é `npm test`. Não existe script de compilação.
- `tipoCliente` chega sempre em minúsculas: `'padrao'` ou `'atacado'`.
- O teto de desconto por pedido se aplica a todas as faixas, inclusive à de atacado.
- Valores monetários são números em reais, não centavos.
