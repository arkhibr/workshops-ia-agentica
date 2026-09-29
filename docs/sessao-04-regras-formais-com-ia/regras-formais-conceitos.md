# Conceitos, fatos e regras: do vocabulário à decisão

Para formalizar uma regra, o time precisa definir os conceitos e registrar os fatos que os relacionam antes de escrever a frase normativa que diz o que deve valer. Esta página apresenta o percurso completo do SBVR à tabela de decisão e fornece o esquema usado no restante da sessão. Os exemplos usam o regulamento de inscrição de um congresso fictício, criado apenas para ilustrar os conceitos e sem relação com o conteúdo dos exercícios da sessão.

## O mapa tem cinco camadas

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é a especificação da OMG para expressar vocabulário e regras de negócio com semântica controlada. O mapa separa cinco camadas:

1. **conceitos** nomeiam coisas do domínio
2. **fatos** relacionam conceitos
3. **regras estruturais** definem classificações ou derivações
4. **regras operativas** regem conduta
5. **controles** registram exceções, conflitos, lacunas, evidência e confiança

Misturar as camadas produz sentenças difíceis de testar: “Participante estudante paga meia inscrição” contém ao menos um conceito indefinido, um fato e um valor derivado na mesma frase.

![Diagrama horizontal do mapa de regras. Conceitos seguem para fatos, e fatos seguem para as regras estruturais de classificação e derivação (RC, RD) e para as regras operativas de obrigação, proibição e permissão (RN). As duas famílias de regra convergem na tabela de decisão, da qual derivam os testes. Uma faixa inferior de controles, com exceções, conflitos, lacunas, evidência e confiança, liga-se por linhas tracejadas a conceitos, fatos, regras e tabela.](assets/mapa-de-regras.png)

*Leitura da figura: siga as setas da esquerda para a direita, das camadas 1 a 4 até a tabela e os testes, e depois leia a faixa 5, cujas linhas tracejadas indicam as camadas em que cada controle é registrado.*

## Conceitos: o que precisa de nome

Um **conceito** representa uma coisa ou categoria relevante para o negócio, e sua definição informa o critério que permite reconhecer cada instância.

| Conceito | Definição | Sinônimos a evitar |
|---|---|---|
| Participante | Pessoa física com inscrição registrada no congresso | inscrito, usuário |
| Vínculo acadêmico | Matrícula ativa em curso de graduação ou pós-graduação na data da inscrição | vínculo estudantil, matrícula |
| Lote de inscrição | Período de inscrição com valor-base fixado pelo regulamento | fase, etapa |

O campo “sinônimos a evitar” denuncia lugares em que duas palavras podem indicar conceitos diferentes ou em que a mesma coisa recebeu nomes incompatíveis.

## Fatos: como os conceitos se relacionam

Um **tipo de fato** é uma relação que pode ser afirmada sobre instâncias dos conceitos. “Participante possui vínculo acadêmico” é um tipo de fato, e “Ana possui o vínculo acadêmico de matrícula 2026-0042” é uma instância desse fato.

| ID | Tipo de fato | Leitura inversa útil |
|---|---|---|
| FT-01 | Participante possui Vínculo Acadêmico | Vínculo Acadêmico pertence a Participante |
| FT-02 | Inscrição pertence a Lote de Inscrição | Lote de Inscrição agrupa Inscrição |
| FT-03 | Comprovante atesta Vínculo Acadêmico | Vínculo Acadêmico é atestado por Comprovante |

Escrever a leitura inversa expõe cardinalidades e pressupostos, e quando a fonte não informa quantidade ou exclusividade o mapa registra a lacuna com a pergunta correspondente.

## Regras estruturais: classificação e derivação

Uma **regra estrutural** define como o domínio é organizado. Ela usa modalidade alética, ligada ao que necessariamente vale dentro do modelo, e por isso nenhum ator a cumpre ou a descumpre.

- **Classificação:** “Um participante que satisfaz os critérios C1 e C2 é um Participante Estudante.”
- **Derivação:** “O valor da inscrição é calculado como o valor-base do lote multiplicado pelo fator da categoria do participante.”

O teste prático é perguntar se existe infração. Uma fórmula pode produzir valor errado e uma classificação pode ser aplicada incorretamente, mas em nenhum dos dois casos há obrigação dirigida a um ator que alguém tenha deixado de cumprir. Passos de cálculo, limites de um valor derivado e critérios de inclusão num total pertencem, portanto, às regras estruturais.

## Regras operativas: obrigação, proibição e permissão

Uma **regra operativa** rege a conduta de um ator identificável e pode ser violada, e nesta sessão as sentenças controladas que a expressam seguem as formas do [RuleSpeak](../referencia/bibliografia.md#ross-rulespeak):

- **deve** para obrigação
- **não deve** para proibição
- **pode** para permissão, com **somente se** quando a permissão depende de condição

“A comissão organizadora deve confirmar a inscrição em até dois dias úteis após a compensação do pagamento” cria obrigação para a comissão organizadora. “O participante pode cancelar a inscrição somente se o pedido for registrado até 15 dias antes da abertura do congresso” concede ao participante uma permissão condicionada, que o regulamento fictício prevê no item 7.

!!! question "Teste de classificação"
    “Participante com comprovante validado é Participante Estudante” e “a comissão organizadora deve aplicar o desconto ao Participante Estudante” pertencem ao mesmo tipo? A primeira sentença classifica participantes e a segunda rege a ação de quem cobra a inscrição, por isso a primeira é estrutural e a segunda é operativa.

## Atomicidade: uma condição verificável por sentença

Uma regra atômica tem um único efeito normativo. Se uma sentença contém “e”, “exceto”, “salvo”, “quando” ou “desde que”, verifique se ela comprime outra regra, exceção ou definição.

Considere: “O participante com matrícula ativa e comprovante validado que se inscrever no primeiro lote paga metade do valor-base, salvo a taxa de minicurso, cobrada integralmente.” Para torná-la verificável:

1. classifique Participante Estudante pelos dois critérios cumulativos, vínculo acadêmico ativo e comprovante validado
2. classifique Inscrição de Primeiro Lote a partir da data de registro da inscrição
3. retire da base do desconto a taxa de minicurso, também como regra de classificação
4. derive o valor da inscrição para o Participante Estudante com Inscrição de Primeiro Lote
5. atribua a obrigação de cobrar o valor ao ator que a fonte nomear, ou registre a lacuna quando a fonte não nomear nenhum
6. registre a ressalva da taxa de minicurso como precedência sobre a regra de desconto

## Quando a tabela de decisão entra

Sentenças atômicas esclarecem cada regra isoladamente, e uma **tabela de decisão** mostra, linha a linha, como várias condições se combinam para produzir um resultado. As políticas de acerto usadas a seguir são definidas pelo [DMN](../referencia/bibliografia.md#decision-model-and-notation-dmn) (*Decision Model and Notation*), padrão da OMG para modelagem de decisões, e indicam qual linha vale quando mais de uma se aplica ao mesmo caso.

**Política de acerto: First, na ordem das linhas.** A linha de pagamento pendente fica no topo para que nenhuma linha de valor se aplique a uma inscrição ainda não paga.

| Regra | Pagamento compensado? | Categoria declarada | Comprovante validado? | Resultado |
|---|---|---|---|---|
| L1 | Não | qualquer | qualquer | inscrição pendente |
| L2 | Sim | estudante | Não | valor-base integral |
| L3 | Sim | estudante | Sim | 50% do valor-base |
| L4 | Sim | profissional | qualquer | valor-base integral |

A tabela declara sua política de acerto. **Unique** exige que uma única linha se aplique a cada caso, **First** faz a primeira linha aplicável prevalecer e **Priority** usa prioridade explícita. Sem essa decisão, a ordem visual das linhas passa a determinar o resultado sem que ninguém tenha escolhido a precedência.

A combinação “pagamento compensado, categoria palestrante” não aparece em nenhuma linha, e o mapa a registra como **combinação não coberta pela tabela**. O regulamento fictício responde a esse caso no item 4, que isenta o palestrante do valor-base, e por isso a correção consiste em acrescentar a linha L5 com o resultado “isento”. O rótulo de lacuna fica reservado para a ausência de resposta na fonte, como no caso de um comprovante de matrícula que perde a validade entre a inscrição e a abertura do congresso, situação que o regulamento não trata.

## Evidência, confiança e lacuna

O esquema abaixo é o contrato de saída da sessão. O prefixo do ID indica o tipo: **RC** para regra estrutural de classificação, **RD** para regra estrutural de derivação e **RN** para regra operativa.

| ID | Tipo | Sentença | Evidência | Confiança | Questão em aberto |
|---|---|---|---|---|---|
| RC-01 | Estrutural: classificação | ... | artigo, parágrafo ou linha | alta, média ou baixa | ... |
| RD-01 | Estrutural: derivação | ... | artigo, parágrafo ou linha | alta, média ou baixa | ... |
| RN-01 | Operativa: obrigação | ... | artigo, parágrafo ou linha | alta, média ou baixa | ... |

- **Evidência** aponta para a menor localização que sustenta a leitura.
- **Confiança alta** indica correspondência direta, média sinaliza inferência e baixa marca hipótese frágil.
- **Lacuna** é ausência de resposta na fonte e não recebe texto inventado.
- **Conflito** ocorre quando duas regras não podem valer ao mesmo tempo para o mesmo caso. Duas evidências que sustentam resultados incompatíveis são o sinal que leva o mapa a registrar esse conflito.

## Prompt-base de decomposição

```text
Analise o texto como material de regras de negócio. Não implemente nada.

Entregue, em seções separadas:
1. conceitos, definição e sinônimos ambíguos;
2. tipos de fato e, quando existirem, instâncias de fato;
3. regras estruturais de classificação (ID RC-nn);
4. regras estruturais de derivação (ID RD-nn);
5. regras operativas de obrigação, proibição ou permissão condicionada
   (ID RN-nn), somente quando houver um ator cuja conduta a regra rege;
6. exceções e relações de precedência;
7. conflitos, lacunas e perguntas para o especialista;
8. tabela de decisão, apenas se houver combinações de condições.

Para cada item, cite o menor fragmento da fonte que o sustenta e atribua
confiança. Não complete uma lacuna com conhecimento presumido.
```

!!! tip "Critério de revisão"
    Faça a retrotradução: entregue apenas o mapa a uma segunda pessoa, peça que ela reconstrua a política em prosa e compare o escopo, as exceções e a precedência da reconstrução com os artigos ou linhas citados na coluna Evidência.

**Próxima página:** [Exemplo de aplicação de IA](regras-formais-exemplo-de-aplicacao-de-ia.md).
