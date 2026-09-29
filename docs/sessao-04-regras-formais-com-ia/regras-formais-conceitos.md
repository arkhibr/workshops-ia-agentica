# Conceitos, fatos e regras: do vocabulário à decisão

Formalizar uma regra começa antes da frase normativa. O time precisa definir os conceitos, registrar os fatos que os relacionam e só então dizer o que deve valer. Esta página apresenta o percurso completo do SBVR à tabela de decisão e fornece o esquema usado no restante da sessão.

## O mapa tem cinco camadas

[SBVR](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules) (*Semantics of Business Vocabulary and Business Rules*) é a especificação da OMG para expressar vocabulário e regras de negócio com semântica controlada. O mapa separa cinco camadas:

1. **conceitos** nomeiam coisas do domínio;
2. **fatos** relacionam conceitos;
3. **regras estruturais** definem classificações ou derivações;
4. **regras operativas** regem conduta;
5. **controles** registram exceções, conflitos, lacunas, evidência e confiança.

Misturar as camadas produz sentenças difíceis de testar. “Contribuinte elegível recebe devolução” contém ao menos um conceito indefinido, um fato e uma consequência.

## Conceitos: o que precisa de nome

Um **conceito** representa uma coisa ou categoria relevante para o negócio. A definição informa o critério que permite reconhecer suas instâncias.

| Conceito | Definição | Sinônimos a evitar |
|---|---|---|
| Pessoa destinatária | Pessoa física à qual uma devolução pode ser atribuída | beneficiário, usuário |
| Unidade familiar | Grupo usado para avaliar renda e cadastro | família, núcleo |
| Renda mensal per capita | Renda mensal considerada dividida pelo número de integrantes | renda média |

O campo “sinônimos a evitar” denuncia lugares em que duas palavras podem indicar conceitos diferentes ou em que a mesma coisa recebeu nomes incompatíveis.

## Fatos: como os conceitos se relacionam

Um **tipo de fato** é uma relação que pode ser afirmada sobre instâncias dos conceitos. “Pessoa integra unidade familiar” é um tipo de fato; “Ana integra a unidade familiar 42” é uma instância desse fato.

| ID | Tipo de fato | Leitura inversa útil |
|---|---|---|
| FT-01 | Pessoa integra Unidade Familiar | Unidade Familiar possui integrante Pessoa |
| FT-02 | Unidade Familiar possui Renda Mensal Per Capita | Renda Mensal Per Capita pertence à Unidade Familiar |
| FT-03 | Documento Fiscal registra Aquisição | Aquisição é registrada por Documento Fiscal |

Escrever a leitura inversa expõe cardinalidades e pressupostos. Se a fonte não informa quantidades ou exclusividade, registre a lacuna.

## Regras estruturais: classificação e derivação

Uma **regra estrutural** define como o domínio é organizado. Ela usa modalidade alética, ligada ao que necessariamente é dentro do modelo, e não descreve uma conduta que alguém possa cumprir ou violar.

- **Classificação:** “Uma pessoa que satisfaz os critérios C1, C2 e C3 é uma Pessoa Elegível.”
- **Derivação:** “A Renda Mensal Per Capita é calculada como a Renda Mensal Familiar dividida pelo número de integrantes.”

O teste prático é perguntar se existe infração. Uma fórmula pode produzir valor errado e uma classificação pode ser aplicada incorretamente; nenhuma das duas é obrigação dirigida a um ator.

## Regras operativas: obrigação, proibição e permissão

Uma **regra operativa** rege conduta e pode ser violada. Nesta sessão, as sentenças controladas seguem as formas do RuleSpeak:

- **deve** para obrigação;
- **não deve** para proibição;
- **pode ... somente se** para permissão condicionada.

“A devolução deve ser atribuída à pessoa responsável pela unidade familiar” cria obrigação. “Uma aquisição pode compor o cálculo somente se estiver vinculada ao CPF de integrante” limita uma permissão.

!!! question "Teste de classificação"
    “Pessoa com CPF regular é Pessoa Habilitada” e “a devolução deve ser paga à Pessoa Habilitada” pertencem ao mesmo tipo? A primeira classifica; a segunda rege uma ação.

## Atomicidade: uma condição verificável por sentença

Uma regra atômica tem um único efeito normativo. Se uma sentença contém “e”, “exceto”, “salvo”, “quando” ou “desde que”, verifique se ela comprime outra regra, exceção ou definição.

Considere: “A pessoa cadastrada, residente no Brasil, com CPF regular e renda por pessoa até o limite recebe devolução, salvo aquisição sujeita ao imposto seletivo.” Para torná-la verificável:

1. classifique Pessoa Elegível pelos quatro critérios cumulativos;
2. derive Aquisição Considerada do documento fiscal e da finalidade domiciliar;
3. proíba a inclusão de item sujeito ao Imposto Seletivo;
4. obrigue o cálculo da devolução para a Pessoa Elegível;
5. registre a exceção como precedência.

## Quando a tabela de decisão entra

Sentenças atômicas esclarecem cada regra. Uma **tabela de decisão** mostra como várias condições se combinam.

| Regra | Elegível? | Categoria | Documento vinculado? | Resultado |
|---|---|---|---|---|
| T1 | Sim | serviço essencial | Sim | percentual específico |
| T2 | Sim | demais casos | Sim | percentual geral |
| T3 | Sim | Imposto Seletivo | Sim | fora do cálculo |
| T4 | Não | qualquer | qualquer | sem devolução |

A tabela declara sua política de acerto. **Unique** exige uma única linha; **First** faz a primeira aplicável prevalecer; **Priority** usa prioridade explícita. Sem essa decisão, a ordem visual pode virar comportamento acidental.

## Evidência, confiança e lacuna

| ID | Tipo | Sentença | Evidência | Confiança | Questão em aberto |
|---|---|---|---|---|---|
| RD-01 | Estrutural: classificação | ... | artigo, parágrafo ou linha | alta, média ou baixa | ... |
| RN-01 | Operativa: obrigação | ... | artigo, parágrafo ou linha | alta, média ou baixa | ... |

- **Evidência** aponta para a menor localização que sustenta a leitura.
- **Confiança alta** indica correspondência direta; média sinaliza inferência; baixa marca hipótese frágil.
- **Lacuna** é ausência de resposta na fonte e não recebe texto inventado.
- **Conflito** ocorre quando duas evidências sustentam resultados incompatíveis para o mesmo caso.

## Prompt-base de decomposição

```text
Analise o texto como material de regras de negócio. Não implemente nada.

Entregue, em seções separadas:
1. conceitos, definição e sinônimos ambíguos;
2. tipos de fato e, quando existirem, instâncias de fato;
3. regras estruturais de classificação;
4. regras estruturais de derivação;
5. regras operativas: obrigação, proibição ou permissão condicionada;
6. exceções e relações de precedência;
7. conflitos, lacunas e perguntas para o especialista;
8. tabela de decisão, apenas se houver combinações de condições.

Para cada item, cite a menor evidência disponível e atribua confiança.
Não complete uma lacuna com conhecimento presumido.
```

!!! tip "Critério de revisão"
    Faça a retrotradução: entregue apenas o mapa a uma segunda pessoa e peça que reconstrua a política. Compare escopo, exceções e precedência com a fonte.

**Próxima página:** [Exemplo: decomposição do IRPF](regras-formais-exemplo-irpf.md).
