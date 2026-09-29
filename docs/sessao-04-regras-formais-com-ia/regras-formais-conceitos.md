# Conceitos, fatos e regras: do vocabulário à decisão

Formalizar uma regra começa antes da frase normativa. O time precisa definir os conceitos, registrar os fatos que os relacionam e só então dizer o que deve valer. Esta página apresenta o percurso completo do SBVR à tabela de decisão e fornece o esquema usado no restante da sessão.

## O mapa tem cinco camadas

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é a especificação da OMG para expressar vocabulário e regras de negócio com semântica controlada. O mapa separa cinco camadas:

1. **conceitos** nomeiam coisas do domínio
2. **fatos** relacionam conceitos
3. **regras estruturais** definem classificações ou derivações
4. **regras operativas** regem conduta
5. **controles** registram exceções, conflitos, lacunas, evidência e confiança

Misturar as camadas produz sentenças difíceis de testar: “Contribuinte elegível recebe devolução” contém ao menos um conceito indefinido, um fato e uma consequência normativa na mesma frase.

## Conceitos: o que precisa de nome

Um **conceito** representa uma coisa ou categoria relevante para o negócio, e sua definição informa o critério que permite reconhecer cada instância.

| Conceito | Definição | Sinônimos a evitar |
|---|---|---|
| Pessoa destinatária | Pessoa física à qual uma devolução pode ser atribuída | beneficiário, usuário |
| Unidade familiar | Grupo usado para avaliar renda e cadastro | família, núcleo |
| Renda mensal per capita | Renda mensal considerada dividida pelo número de integrantes | renda média |

O campo “sinônimos a evitar” denuncia lugares em que duas palavras podem indicar conceitos diferentes ou em que a mesma coisa recebeu nomes incompatíveis.

## Fatos: como os conceitos se relacionam

Um **tipo de fato** é uma relação que pode ser afirmada sobre instâncias dos conceitos. “Pessoa integra unidade familiar” é um tipo de fato, e “Ana integra a unidade familiar 42” é uma instância desse fato.

| ID | Tipo de fato | Leitura inversa útil |
|---|---|---|
| FT-01 | Pessoa integra Unidade Familiar | Unidade Familiar possui integrante Pessoa |
| FT-02 | Unidade Familiar possui Renda Mensal Per Capita | Renda Mensal Per Capita pertence à Unidade Familiar |
| FT-03 | Documento Fiscal registra Aquisição | Aquisição é registrada por Documento Fiscal |

Escrever a leitura inversa expõe cardinalidades e pressupostos, e quando a fonte não informa quantidade ou exclusividade o mapa registra a lacuna com a pergunta correspondente.

## Regras estruturais: classificação e derivação

Uma **regra estrutural** define como o domínio é organizado. Ela usa modalidade alética, ligada ao que necessariamente vale dentro do modelo, e por isso nenhum ator a cumpre ou a descumpre.

- **Classificação:** “Uma pessoa que satisfaz os critérios C1, C2 e C3 é uma Pessoa Elegível.”
- **Derivação:** “A Renda Mensal Per Capita é calculada como a Renda Mensal Familiar dividida pelo número de integrantes.”

O teste prático é perguntar se existe infração. Uma fórmula pode produzir valor errado e uma classificação pode ser aplicada incorretamente, mas em nenhum dos dois casos há obrigação dirigida a um ator que alguém tenha deixado de cumprir. Passos de cálculo, limites de um valor derivado e critérios de inclusão num total pertencem, portanto, às regras estruturais.

## Regras operativas: obrigação, proibição e permissão

Uma **regra operativa** rege a conduta de um ator identificável e pode ser violada. Nesta sessão, as sentenças controladas seguem as formas do [RuleSpeak](../referencia/bibliografia.md#ross-rulespeak):

- **deve** para obrigação
- **não deve** para proibição
- **pode** para permissão, com **somente se** quando a permissão depende de condição

“O órgão gestor deve atribuir a devolução à pessoa responsável pela unidade familiar” cria obrigação para o órgão gestor. “O destinatário pode solicitar a exclusão da sistemática de devolução a qualquer tempo” concede permissão ao destinatário, com base no art. 113, §1º, da [Lei Complementar nº 214/2025](../referencia/bibliografia.md#lei-complementar-2142025-ibs-cbs-e-imposto-seletivo).

!!! question "Teste de classificação"
    “Pessoa com CPF regular é Pessoa Habilitada” e “o órgão gestor deve pagar a devolução à Pessoa Habilitada” pertencem ao mesmo tipo? A primeira sentença classifica pessoas e a segunda rege a ação de quem paga, por isso a primeira é estrutural e a segunda é operativa.

## Atomicidade: uma condição verificável por sentença

Uma regra atômica tem um único efeito normativo. Se uma sentença contém “e”, “exceto”, “salvo”, “quando” ou “desde que”, verifique se ela comprime outra regra, exceção ou definição.

Considere: “A pessoa cadastrada, residente no Brasil, com CPF regular e renda por pessoa até o limite recebe devolução, salvo aquisição sujeita ao imposto seletivo.” Para torná-la verificável:

1. classifique Pessoa Elegível pelos quatro critérios cumulativos
2. classifique Aquisição Considerada a partir do documento fiscal e da finalidade domiciliar
3. retire da Aquisição Considerada o item sujeito ao Imposto Seletivo, também como regra de classificação
4. derive o valor da devolução para a Pessoa Elegível
5. atribua a obrigação de pagar a devolução ao ator que a fonte nomear, ou registre a lacuna quando a fonte não nomear nenhum
6. registre a ressalva do Imposto Seletivo como precedência sobre a regra de inclusão

## Quando a tabela de decisão entra

Sentenças atômicas esclarecem cada regra isoladamente, e uma **tabela de decisão** mostra, linha a linha, como várias condições se combinam para produzir um resultado.

**Política de acerto: First, na ordem das linhas.** As exclusões ficam no topo para que nenhuma linha de percentual se aplique a quem já foi excluído.

| Regra | Elegível? | Aquisição | Documento vinculado? | Resultado |
|---|---|---|---|---|
| T1 | Não | qualquer | qualquer | sem devolução |
| T2 | Sim | sujeita ao Imposto Seletivo | qualquer | fora do cálculo |
| T3 | Sim | categoria do inciso I do art. 118 | Sim | 100% da CBS e 20% do IBS |
| T4 | Sim | demais casos | Sim | 20% da CBS e 20% do IBS |

A tabela declara sua política de acerto. **Unique** exige que uma única linha se aplique a cada caso, **First** faz a primeira linha aplicável prevalecer e **Priority** usa prioridade explícita. Sem essa decisão, a ordem visual das linhas passa a determinar o resultado sem que ninguém tenha escolhido a precedência. A combinação “elegível, sem documento vinculado” não aparece em nenhuma linha, e o mapa a registra como lacuna.

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
- **Conflito** ocorre quando duas evidências sustentam resultados incompatíveis para o mesmo caso.

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

**Próxima página:** [Exemplo: decomposição do IRPF](regras-formais-exemplo-irpf.md).
