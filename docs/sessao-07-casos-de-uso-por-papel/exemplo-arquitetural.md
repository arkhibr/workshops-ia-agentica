# Exemplo arquitetural: da transcrição à ata conferida

Esta demonstração executa o caso "Processar reuniões", do catálogo de Product Owner, sobre a transcrição de uma reunião de refinamento da ACME, a universidade fictícia usada nesta sessão. A reunião, os nomes e as regras citadas são inventados e não reproduzem norma vigente de nenhuma instituição. O objetivo é mostrar o que a conferência humana encontra numa saída que, à primeira leitura, parece correta.

## A reunião

A transcrição tem dezoito falas e cinco armadilhas plantadas antes da execução. Cada armadilha corresponde a um erro que uma ata gerada por IA pode cometer sem avisar.

```text
Marina (PO): Vamos fechar o refinamento do relatório trimestral de prestação de contas. Primeiro ponto: o prazo para o coordenador enviar o relatório depois do fechamento do trimestre. Eu proponho cinco dias úteis.
Rafael (desenvolvimento): Cinco dias úteis combina com o agendamento que o sistema já tem. Por mim está bom.
Caio (financeiro): Cinco é pouco. A conciliação bancária só termina por volta do oitavo dia útil, e se o coordenador enviar antes o saldo está errado.
Marina: Então dez dias úteis. Fechado, dez.
Beatriz (testes): Segundo ponto, a dispensa de segunda aprovação para despesas pequenas. Qual é o limite?
Caio: Até oito mil reais a despesa dispensa a segunda aprovação, desde que a rubrica seja de custeio.
Marina: Certo, então até oitocentos reais.
Caio: Não, oito mil. Oito mil reais.
Marina: Oito mil, anotado.
Rafael: E se a rubrica for de capital?
Caio: Capital sempre exige segunda aprovação, sem exceção.
Beatriz: Terceiro ponto, o relatório rejeitado pelo financeiro. O coordenador pode reenviar quantas vezes?
Marina: Isso a gente não decide hoje. Fica para a próxima reunião.
Rafael: Tem uma dúvida de LGPD sobre guardar o CPF do bolsista no relatório. Alguém precisa falar com o jurídico antes da sprint começar.
Beatriz: Concordo, precisa ser antes da sprint.
Marina: Beatriz, você escreve os cenários de teste do limite de oito mil até quarta-feira?
Beatriz: Escrevo, até quarta.
Marina: Rafael, a estimativa do envio automático fica para sexta.
Rafael: Sexta, combinado.
```

| Armadilha | Onde aparece | O que uma ata correta registra |
|---|---|---|
| Decisão que mudou | Prazo de envio, de cinco para dez dias úteis | Dez dias úteis, com a mudança anotada |
| Número dito errado e corrigido | Limite de oito mil reais, repetido como "oitocentos" | R$ 8.000, somente para rubrica de custeio |
| Ponto sem decisão | Quantidade de reenvios do relatório rejeitado | Pendente para a próxima reunião |
| Ação sem responsável | Conversa com o jurídico sobre LGPD | "Sem responsável citado" |
| Prazo que não é data | "Quarta" e "sexta" | A expressão dita, sem data inventada |

## O pedido

O pedido segue o método da Sessão 3: papel, tarefa, formato da saída e restrições que impedem o agente de preencher lacunas por conta própria.

```text
Papel: você apoia a product owner de um time de desenvolvimento.

Tarefa: transformar a transcrição abaixo em ata de reunião.

Formato da saída, em português do Brasil e em Markdown:
1. Uma tabela de decisões, com as colunas Decisão e Condição ou observação.
2. Uma tabela de ações, com as colunas Ação, Responsável e Prazo.
3. Uma lista de pontos que a reunião deixou sem decisão.

Restrições:
- Registre apenas o que está na transcrição.
- Quando uma decisão mudou durante a reunião, registre só a decisão final e anote a mudança na coluna de observação.
- Se uma ação não tem responsável citado, escreva "sem responsável citado" em vez de escolher uma pessoa.
- Se um prazo não é uma data, copie a expressão dita e não converta em data.
```

As quatro restrições correspondem às quatro últimas armadilhas da tabela. Sem elas, o agente decide sozinho como tratar cada uma, e a ata não indica que houve decisão.

## A saída

O texto abaixo é a saída integral da execução, sem edição.

```markdown
**Decisões**

| Decisão | Condição ou observação |
| --- | --- |
| O coordenador tem 10 dias úteis, após o fechamento do trimestre, para enviar o relatório trimestral de prestação de contas. | Mudou durante a reunião: Marina propôs 5 dias úteis, Rafael concordou, e Caio objetou porque a conciliação bancária termina por volta do oitavo dia útil e o saldo fica errado se o envio for antes. Marina fechou em 10 dias úteis. |
| Despesa de até R$ 8.000 dispensa a segunda aprovação. | Vale somente se a rubrica for de custeio. Houve um erro de transcrição durante a reunião: Marina repetiu o limite como "oitocentos reais", Caio corrigiu para oito mil, e Marina confirmou "oito mil, anotado". |
| Despesa em rubrica de capital sempre exige segunda aprovação. | Caio afirmou que não há exceção, em resposta à pergunta de Rafael. |

**Ações**

| Ação | Responsável | Prazo |
| --- | --- | --- |
| Escrever os cenários de teste do limite de oito mil reais. | Beatriz | até quarta-feira |
| Entregar a estimativa do envio automático. | Rafael | sexta |
| Falar com o jurídico sobre a dúvida de LGPD quanto a guardar o CPF do bolsista no relatório. | sem responsável citado | antes da sprint começar |

**Pontos sem decisão**

- Quantas vezes o coordenador pode reenviar o relatório rejeitado pelo financeiro. Marina adiou o ponto para a próxima reunião.
- Se o CPF do bolsista pode ser guardado no relatório, pois há uma dúvida de LGPD. A reunião não definiu quem consulta o jurídico, e a resposta do jurídico ainda não existe.
```

A execução foi única, feita em 21/10/2026 por um agente do Claude Code com o modelo configurado como `sonnet` e sem acesso a ferramentas. Uma segunda execução do mesmo pedido pode produzir texto diferente.

## A conferência

A conferência compara cada armadilha da tabela com a linha correspondente da ata, na ordem em que a transcrição as apresenta.

| Item | Na transcrição | Na ata | Resultado |
|---|---|---|---|
| Prazo de envio | Cinco dias úteis, depois dez | Dez dias úteis, com a mudança anotada | Correto |
| Limite de dispensa | "Oitocentos" corrigido para oito mil | R$ 8.000, somente custeio | Correto, com ressalva abaixo |
| Rubrica de capital | Segunda aprovação sempre | Registrada como decisão | Correto |
| Reenvio do relatório | Adiado para a próxima reunião | Listado em pontos sem decisão | Correto |
| Conversa com o jurídico | Ninguém foi indicado | "Sem responsável citado" | Correto |
| Prazos | "Quarta" e "sexta" | "até quarta-feira" e "sexta", sem data | Correto |

Duas falhas passam pela tabela de armadilhas e aparecem só na leitura da ata inteira contra a transcrição.

1. **Causa errada atribuída à divergência.** A ata escreve "erro de transcrição" para o episódio do limite, mas o texto de entrada é a transcrição fiel de um lapso de fala de Marina. A explicação não consta na reunião, e uma ata que a registra atribui à pessoa que transcreveu um erro que foi de quem falou.
2. **Item duplicado em duas listas.** A dúvida de LGPD aparece como ação, sem responsável, e de novo como ponto sem decisão. A reunião tratou a questão uma vez, e a repetição faz a ata contar dois pendentes onde há um.

Nenhuma das duas falhas muda uma decisão, e as duas passariam por um revisor que apenas conferisse números e prazos.

## O que a demonstração mostra

- A saída acertou os cinco pontos que as restrições do pedido cobriam e errou nos dois que o pedido não cobria. A restrição "registre apenas o que está na transcrição" não impediu o agente de acrescentar uma explicação que ninguém disse.
- A conferência levou menos tempo do que escrever a ata do zero, porque a tabela de armadilhas indica onde olhar. Sem essa lista, o revisor lê a ata inteira sem saber qual divergência procurar.
- O critério de aceite da ata é a decisão registrada que um participante reconhece como o que foi dito. Qualquer item que o participante não reconhece volta para a transcrição antes de a ata circular.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
