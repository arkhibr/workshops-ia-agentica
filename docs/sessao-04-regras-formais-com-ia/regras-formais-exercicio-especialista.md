# Exercício de IA — Especialista: casos de teste em TDD

Este exercício parte do mapa de cashback produzido no exercício geral. O objetivo é converter regras verificadas em casos de teste antes de qualquer implementação, seguindo TDD: primeiro explicitar o comportamento observável, depois escrever código.

## Entrada obrigatória

Use o mapa com conceitos, fatos, regras estruturais, regras operativas, exceções, conflitos, lacunas, evidência e confiança. Se essas camadas ainda estiverem misturadas, corrija o mapa antes de gerar testes. Um teste criado a partir de uma regra mal classificada apenas automatiza a confusão.

## Passo 1 — selecione regras testáveis

Escolha regras com saída observável:

- classificação de pessoa elegível;
- exclusão por cada critério não satisfeito;
- classificação da categoria da aquisição;
- exclusão de item sujeito ao Imposto Seletivo;
- escolha dos percentuais de CBS e IBS;
- momento da devolução quando a fonte o determina.

Não transforme dependência de regulamento em resultado esperado. Quando a fonte não determinar o resultado, escreva um teste pendente ou uma questão de domínio; **não invente** valor, data ou comportamento.

## Passo 2 — peça uma matriz de testes

```text
Você receberá um mapa de regras formalizado a partir dos arts. 112, 113,
116 e 118 da LC 214/2025 compilada. Proponha casos de teste antes de
qualquer implementação, seguindo TDD.

Para cada caso, devolva:
- ID do teste;
- ID da regra de origem;
- cenário em linguagem de negócio;
- dados de entrada mínimos;
- resultado esperado;
- partição ou fronteira coberta;
- evidência legal;
- justificativa;
- confiança.

Cubra: caminho nominal, cada critério cumulativo ausente, fronteiras de
renda, CPF irregular, residência fora do Brasil, documento não vinculado,
consumo não domiciliar, item sujeito ao Imposto Seletivo, botijão acima
de 13 kg, categorias com percentuais distintos, sobreposição e dado
ausente.

Para conflito ou lacuna, não invente resultado. Marque o caso como
INDETERMINADO e formule a pergunta que desbloqueia o teste.
```

## Passo 3 — critique a matriz

Procure quatro defeitos frequentes:

1. **teste sem regra de origem:** não há rastreabilidade;
2. **teste com dados demais:** a causa da mudança de resultado fica escondida;
3. **teste de fórmula sem classificação:** o percentual pode estar certo para a categoria errada;
4. **resultado inventado:** o agente fechou uma lacuna que dependia de regulamento ou validação jurídica.

## Passo 4 — organize o ciclo TDD

Escolha três casos confirmados. Para cada um:

1. escreva o teste e confirme que falha pela ausência do comportamento;
2. implemente apenas o necessário para fazê-lo passar;
3. execute a suíte inteira;
4. refatore sem alterar o comportamento;
5. registre o vínculo entre teste e regra.

Não é necessário implementar o motor tributário durante esta sessão. O produto é a especificação executável dos casos.

## Matriz mínima esperada

| Classe | Exemplo de caso | Resultado |
|---|---|---|
| Nominal | pessoa satisfaz os quatro critérios e compra energia domiciliar documentada | percentuais específicos |
| Fronteira | renda per capita exatamente igual a meio salário mínimo | elegível quanto à renda |
| Fora da fronteira | renda um centavo acima do limite | não elegível quanto à renda |
| Exceção | item sujeito ao Imposto Seletivo | fora do cálculo considerado |
| Sobreposição | categoria essencial e regra geral poderiam combinar | apenas a categoria específica |
| Ausência | categoria ou vínculo fiscal não informado | INDETERMINADO, sem inferência |

## Evidência a entregar

Entregue a matriz revisada, destaque três casos que entrariam primeiro no ciclo vermelho-verde-refatorar e explique por que a ordem reduz risco. Inclua ao menos um caso que permaneceu indeterminado por lacuna real.

**Próxima página:** [Arqueologia de regras em SQL](arqueologia-de-regras-sql.md).
