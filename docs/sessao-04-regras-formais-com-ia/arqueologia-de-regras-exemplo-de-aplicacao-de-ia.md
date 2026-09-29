# Exemplo de aplicação de IA: arqueologia de regras

A arqueologia de regras é a recuperação disciplinada das decisões de negócio que um sistema em produção executa sem que nenhum documento atual as registre, com o produto expresso no vocabulário do SBVR (*Semantics of Business Vocabulary and Business Rules*, especificação da OMG para vocabulário e regras de negócio). Esta é uma demonstração conduzida pelo instrutor, que aplica a um método C# legado os seis movimentos descritos em [Conceitos: arqueologia de regras](arqueologia-de-regras-conceitos.md#o-metodo-em-seis-movimentos) e mostra onde a saída do agente precisa de correção antes de entrar no catálogo.

!!! warning "Código e valores fictícios"
    O método, a biblioteca, os tipos de leitor e todos os valores desta página são fictícios e foram criados para a aula. Nenhum número do exemplo representa regra real de biblioteca, e o artefato é diferente do usado no exercício seguinte, para que a demonstração não antecipe a resposta.

## O artefato

O método `CalcularMulta` calcula a multa por atraso na devolução de uma obra emprestada por uma biblioteca fictícia. O comentário ao fim de cada linha traz o número da linha, e todas as referências desta página, na forma L09 ou L18–L20, seguem essa numeração.

```csharp
using System;                                                     // 01
public static class Multas                                        // 02
{                                                                 // 03
    // Estudante paga metade de qualquer multa.                   // 04
    public static decimal CalcularMulta(                          // 05
        DateTime dataPrevista, DateTime? dataDevolucao,           // 06
        string tipoLeitor, decimal valorObra)                     // 07
    {                                                             // 08
        DateTime fim = dataDevolucao ?? DateTime.Today;           // 09
        int diasAtraso = (fim.Date - dataPrevista.Date).Days;     // 10
        if (diasAtraso <= 0)                                      // 11
        {                                                         // 12
            return 0m;                                            // 13
        }                                                         // 14
        decimal multa = 0m;                                       // 15
        if (tipoLeitor != "PROFESSOR")                            // 16
        {                                                         // 17
            if (diasAtraso > 30)                                  // 18
            {                                                     // 19
                multa = valorObra;                                // 20
            }                                                     // 21
            else                                                  // 22
            {                                                     // 23
                multa = diasAtraso * 2.50m;                       // 24
                if (tipoLeitor == "ESTUDANTE")                    // 25
                {                                                 // 26
                    multa = multa * 0.5m;                         // 27
                }                                                 // 28
            }                                                     // 29
        }                                                         // 30
        return multa;                                             // 31
    }                                                             // 32
}                                                                 // 33
```

O método tem 33 linhas, três valores mágicos (30 em L18, 2.50m em L24 e 0.5m em L27), um `if` aninhado em que a ordem das verificações define qual resultado prevalece e uma data de devolução ausente que L09 substitui pela data corrente. O comentário de L04 descreve uma intenção que o código não executa em todos os casos, e essa divergência é um dos pontos que a demonstração trata no movimento 3.

## O prompt usado

O prompt reaproveita as convenções do [exercício geral do Tema 1](regras-formais-exercicio-geral.md), adaptadas para evidência de código. Os prefixos são CT (conceito), FT (tipo de fato), RC (regra estrutural de classificação), RD (regra estrutural de derivação), RN (regra operativa, que rege a conduta de um ator capaz de descumpri-la) e EX (regra de exceção, que referencia o ID da regra afetada). Os rótulos de controle são LACUNA, REGULAMENTO, CONFLITO e INFERÊNCIA, e cada um recebe no prompt a definição própria do trabalho com código.

```text
Atue como analista de regras de negócio e recupere as regras de negócio do
método C# fornecido, com o produto no vocabulário do SBVR (OMG) e sentenças
no estilo RuleSpeak em português.

ENTRADA
- Arquivo Multas.cs, com o número de cada linha no comentário ao fim dela.
- Nenhuma outra fonte está disponível nesta etapa, nem documentação, nem
  teste, nem especialista do domínio.

LIMITES
- Não altere o código e não proponha correção.
- Toda afirmação cita o intervalo exato de linhas, na forma L09 ou L18-L20,
  e o trecho literal que a sustenta. Afirmação sem linha fica fora da resposta.
- Não atribua motivo a valor literal. O motivo de um número entra somente
  com evidência no próprio arquivo, e na falta dela registre LACUNA.
- Trate comentário como evidência de intenção, de peso baixo. Descreva o
  comportamento implementado somente a partir das instruções executáveis.

CONVENÇÕES
1. Vocabulário antes das regras. Toda regra usa apenas conceitos da seção A
   e tipos de fato da seção B. Termo novo entra primeiro em A.
2. Conceito (CT-nn): termo, definição por gênero e diferença ("X é um Y
   que ..."), sinônimos a evitar, linhas de origem.
3. Tipo de fato (FT-nn): "<conceito> <verbo> <conceito>", leitura inversa e
   cardinalidade. Cardinalidade que o código não determina recebe LACUNA.
4. Regra estrutural, de modalidade alética, que nenhum ator descumpre:
   - classificação RC-nn: "Um <conceito> é um <conceito> se ..."
   - derivação RD-nn: "<valor> é calculado como ...".
   Valores por dia, percentuais, limites de dias e passos de cálculo são
   sempre regras estruturais.
5. Regra operativa RN-nn, de modalidade deôntica, somente quando existe um
   ator que pode descumpri-la: "<ator> deve ...", "<ator> não deve ...".
   Código que executa um cálculo não prova que alguém tenha o dever de
   executá-lo. Se o arquivo não nomear o ator, registre LACUNA e não
   atribua ator por conta própria.
6. Uma regra por sentença, com um único efeito. Tratamento diferente para
   um subconjunto de casos é registrado como EX-nn, com o ID da regra afetada.
7. Precedência. A ordem e o aninhamento dos if definem qual regra prevalece.
   Para cada par de regras que pode valer no mesmo caso, diga qual prevalece
   e cite as linhas que provam a ordem.
8. Rótulos de controle: LACUNA (o código não responde), REGULAMENTO (o código
   remete a fonte externa que não foi fornecida), CONFLITO (duas evidências
   sustentam resultados incompatíveis para o mesmo caso), INFERÊNCIA
   (conclusão sua, sem trecho do arquivo que a sustente).

SAÍDA, uma tabela por seção
1. Inventário: entradas, literais com linha, resultados possíveis
2. Evidência: ID | linhas | trecho literal
3. Hipóteses: ID | hipótese | evidência | confiança
A. Conceitos: ID | termo | definição | sinônimos a evitar | linhas
B. Tipos de fato: ID | fato | leitura inversa | cardinalidade | linhas
C. Classificação: ID | sentença | evidência | confiança | pergunta de validação
D. Derivação: mesmas colunas de C
E. Operativas: ID | tipo | ator | sentença | evidência | confiança | pergunta
F. Exceções e precedência: ID | regra afetada | sentença | qual prevalece e
   por quê
G. Controles: rótulo | descrição | linhas | pergunta
H. Tabela de decisão com as condições dias de atraso e tipo de leitor e o
   resultado multa. Declare a política de acerto do DMN (Unique, First ou
   Priority) e justifique com as linhas.
I. Perguntas fechadas ao especialista, uma por hipótese, com o ID.
J. Casos de teste de caracterização: entradas, resultado atual, ID, linhas.

Evidência: intervalo de linhas e trecho literal.
Confiança: alta (trecho explícito), média (uma inferência), baixa (depende de
interpretação do domínio).

Antes de responder, confira se toda afirmação tem linha, se toda RN tem ator,
se nenhuma RN descreve cálculo e se toda precedência cita as linhas da ordem.
```

## Movimento 1: inventário

O instrutor cola o arquivo e o prompt numa conversa nova e mostra primeiro a seção de inventário, que ainda não contém nenhuma regra. O trecho abaixo reproduz a parte da saída do agente usada na demonstração.

```text
Entradas: dataPrevista (L06), dataDevolucao, anulável (L06), tipoLeitor (L07),
valorObra (L07).
Literais: "PROFESSOR" (L16), "ESTUDANTE" (L25), 30 (L18), 2.50m (L24),
0.5m (L27), 0m (L13, L15).
Resultados possíveis: 0 (L13 e L15 sem alteração), valorObra (L20),
diasAtraso * 2.50m (L24), metade desse produto (L27).
```

Os candidatos a conceito que o agente propõe a partir desse inventário são Leitor, Tipo de Leitor, Empréstimo, Obra, Valor da Obra, Data Prevista, Data de Devolução, Dias de Atraso e Multa. O tipo de fato central é "Leitor devolve Obra", e a cardinalidade dele fica marcada como LACUNA, porque o método recebe uma obra por chamada e nada informa sobre empréstimos com várias obras.

## Movimento 2: captura de evidência

O instrutor confere cada intervalo de linhas contra a listagem antes de aceitar a tabela, porque os movimentos seguintes citam estes IDs.

| ID | Linhas | Trecho literal |
|---|---|---|
| E1 | L09 | `DateTime fim = dataDevolucao ?? DateTime.Today;` |
| E2 | L11–L13 | `if (diasAtraso <= 0)` seguido de `return 0m;` |
| E3 | L16 | `if (tipoLeitor != "PROFESSOR")` |
| E4 | L18–L20 | `if (diasAtraso > 30)` seguido de `multa = valorObra;` |
| E5 | L24 | `multa = diasAtraso * 2.50m;` |
| E6 | L25–L27 | `if (tipoLeitor == "ESTUDANTE")` seguido de `multa = multa * 0.5m;` |
| E7 | L04 | `// Estudante paga metade de qualquer multa.` |
| E8 | L10 | `int diasAtraso = (fim.Date - dataPrevista.Date).Days;` |
| E9 | L22 | `else`, que fecha o `if` de L18 e abre o bloco de L23–L29 |

## Movimento 3: hipóteses de regra

Nesta seção aparecem os três erros que o instrutor corrige adiante, e a demonstração os deixa visíveis de propósito. O trecho abaixo reproduz a saída do agente sem edição.

```text
H1  Sem data de devolução, o atraso é contado até a data corrente.
    Evidência E1 (L09). Confiança alta.
H2  Professor não paga multa. Evidência E3 (L16). Confiança alta.
H3  Acima de 30 dias o atraso é tratado como extravio, e o leitor paga o
    valor da obra. O limite de 30 dias corresponde ao prazo regulamentar
    de declaração de extravio. Evidência E4 (L18-L20). Confiança alta.
H4  Estudante paga metade de qualquer multa, inclusive quando a multa é o
    valor da obra. Evidência E6 (L25-L27) e E7 (L04). Confiança alta.
H5  Multa diária de R$ 2,50 por dia de atraso. Evidência E5 (L24).
    Confiança alta.
```

H1 e H5 conferem com o código. H3 e H4 contêm os erros tratados na seção de correções, e o agente não registrou nenhuma hipótese sobre a combinação de L18 com L24, que produz o caso provavelmente não intencional do método. Para leitor de tipo diferente de PROFESSOR e ESTUDANTE, uma obra com valor de R$ 40,00 gera multa de R$ 75,00 no 30º dia de atraso (30 × R$ 2,50 em L24) e de R$ 40,00 no 31º dia (L20), de modo que esse leitor paga menos quando devolve mais tarde, e o instrutor acrescenta essa hipótese como H6. Para estudante, a multa do 30º dia é R$ 37,50 (L27), e a queda no 31º dia ocorre somente com obra de valor abaixo de R$ 37,50, enquanto o professor paga R$ 0,00 nos dois dias (L16).

## Movimento 4: validação de domínio

As hipóteses chegam ao especialista do domínio, neste caso a pessoa responsável pelo acervo da biblioteca fictícia, como perguntas fechadas geradas pelo agente e revisadas pelo instrutor. Cada pergunta traz o caso concreto que o código produz hoje.

| ID | Pergunta ao especialista | Caso produzido pelo código |
|---|---|---|
| Q1 (H1) | Um empréstimo sem data de devolução registrada deve acumular multa até a data em que a multa é consultada? | Obra prevista para dez dias atrás, ainda não devolvida, gera hoje R$ 25,00 para leitor de tipo diferente de PROFESSOR e ESTUDANTE (L09, L24) |
| Q2 (H2) | Professor fica isento também quando o atraso passa de 30 dias? | Professor com 90 dias de atraso paga R$ 0,00 (L16 antes de L18) |
| Q3 (H3) | Qual é a origem do limite de 30 dias, e ele deve continuar no código ou vir de configuração? | Atraso de 31 dias cobra o valor da obra (L18–L20) |
| Q4 (H4) | O estudante com mais de 30 dias de atraso deve pagar o valor integral da obra? | Estudante com 35 dias e obra de R$ 80,00 paga R$ 80,00 (L25 dentro do `else` de L22) |
| Q5 (H6) | A multa pode diminuir quando o atraso passa de 30 para 31 dias? | Para leitor de tipo diferente de PROFESSOR e ESTUDANTE, obra de R$ 40,00 gera R$ 75,00 no 30º dia e R$ 40,00 no 31º (L24, L20) |

A demonstração não apresenta respostas, porque o especialista é fictício, e todas as hipóteses permanecem com o desfecho "em aberto". Esse desfecho é o que os testes do movimento 6 registram no próprio nome.

## Movimento 5: formalização SBVR

O agente formaliza as hipóteses nas seções A a H do prompt. O trecho abaixo mostra as seções D, E e F antes da revisão, e a seção E contém o primeiro erro corrigido pelo instrutor.

```text
D. RD-01  Data de Referência é calculada como a Data de Devolução ou, na
          ausência dela, a data corrente. L09. Confiança alta.
   RD-02  Dias de Atraso é calculado como a Data de Referência menos a Data
          Prevista, em dias corridos. L10. Confiança alta.
   RD-03  A Multa por Extravio é calculada como o Valor da Obra. L20.
E. RN-01  Obrigação. Deve ser cobrada multa de R$ 2,50 por dia de atraso.
          L24. Confiança alta.
F. EX-01  Afeta RN-01. A multa de Leitor Estudante é metade da multa
          calculada, em qualquer faixa de atraso. L25-L27 e L04.
```

Depois da revisão, o catálogo fica com as regras abaixo e com a tabela de decisão correspondente.

| ID | Sentença | Linhas |
|---|---|---|
| RC-01 | Um Leitor é Leitor Isento se o Tipo de Leitor é PROFESSOR. | L16 |
| RC-02 | Um Empréstimo é Empréstimo em Atraso Longo se Dias de Atraso é maior que 30. | L18 |
| RC-03 | Um Empréstimo é Empréstimo em Atraso se Dias de Atraso é maior que 0. | L11–L13 |
| RD-01 | Data de Referência é calculada como a Data de Devolução ou, na ausência dela, a data corrente. | L09 |
| RD-02 | Dias de Atraso é calculado como a Data de Referência menos a Data Prevista, em dias corridos. | L10 |
| RD-03 | A Multa de Empréstimo em Atraso Longo é calculada como o Valor da Obra. | L18–L20 |
| RD-04 | A Multa Diária é calculada como Dias de Atraso multiplicado por R$ 2,50. | L24 |

As exceções e a precedência entre as regras ficam numa tabela própria, conforme as convenções 6 e 7 do prompt.

| ID | Regra afetada | Sentença | Qual prevalece e por quê |
|---|---|---|---|
| EX-01 | RD-04 | A Multa Diária de Leitor Estudante é calculada como metade do valor de RD-04. | EX-01 prevalece sobre RD-04 para estudante, porque L27 substitui o valor calculado em L24. RC-02 e RD-03 prevalecem sobre EX-01, porque L25–L27 estão no `else` de L22 e só executam quando o teste de L18 é falso. |
| EX-02 | RD-03, RD-04 e EX-01 | A Multa de Leitor Isento é calculada como R$ 0,00 em qualquer quantidade de Dias de Atraso. | EX-02 prevalece sobre RD-03, RD-04 e EX-01, porque o `if` de L16 envolve L17–L30 e o valor 0m atribuído em L15 chega a L31 sem alteração. RC-03 prevalece sobre EX-02, porque o `return` de L13 encerra o método antes de L16. |

**Política de acerto: First.** As linhas 2 e 3 valem ao mesmo tempo para um professor com mais de 30 dias de atraso, e as linhas 4 e 5 valem ao mesmo tempo para um estudante, de modo que a ordem das linhas reproduz a ordem de avaliação de L11, L16, L18 e L25.

| Linha | Dias de atraso | Tipo de leitor | Multa | Regras |
|---|---|---|---|---|
| 1 | até 0 | qualquer | R$ 0,00 | RC-03 (L11–L13) |
| 2 | 1 ou mais | PROFESSOR | R$ 0,00 | RC-01, EX-02 (L15–L16) |
| 3 | mais de 30 | qualquer | Valor da Obra | RC-02, RD-03 (L18–L20) |
| 4 | 1 a 30 | ESTUDANTE | Dias × R$ 1,25 | EX-01 (L25–L27) |
| 5 | 1 a 30 | qualquer | Dias × R$ 2,50 | RD-04 (L24) |

Os controles registrados são um CONFLITO entre o comentário de L04 e o comportamento de L18–L27, uma LACUNA sobre o ator responsável pela cobrança e uma LACUNA sobre a origem dos literais 30, 2.50m e 0.5m. A comparação `tipoLeitor != "PROFESSOR"` em L16 usa o operador de igualdade de `string` do C#, que compara de forma ordinal e distingue maiúsculas de minúsculas, e por isso o catálogo registra com evidência em L16 e confiança alta que o valor "professor" em minúsculas recebe multa. A ocorrência desse valor nos cadastros fica como LACUNA, porque a demonstração não recebeu dados de produção.

## Correções do instrutor

A tabela reúne as correções feitas sobre a saída do agente nos movimentos 3 e 5, cada uma com a evidência do arquivo que a sustenta.

| # | Saída do agente | Correção | Evidência |
|---|---|---|---|
| 1 | RN-01, obrigação: "Deve ser cobrada multa de R$ 2,50 por dia de atraso." | A sentença não tem ator e descreve um cálculo, e o prompt manda registrar cálculo como regra estrutural. A regra passa a RD-04, e o ator da cobrança fica como LACUNA. | L24 contém apenas `multa = diasAtraso * 2.50m;`, e nenhuma linha do arquivo nomeia quem cobra ou quem paga |
| 2 | H4 e EX-01: estudante paga metade de qualquer multa, inclusive o valor da obra | A precedência foi lida na ordem inversa da avaliação. O teste de L18 é avaliado antes do desconto, e o ramo de L20 retorna o valor da obra sem passar por L25. A exceção afeta somente RD-04, e H4 fica revisada como "estudante com até 30 dias de atraso paga metade da multa diária (linhas 25 a 27), e estudante com mais de 30 dias paga o valor integral da obra (linhas 18 a 20)". | L25–L27 estão dentro do `else` aberto em L22, que pertence ao `if` de L18 |
| 3 | H3: o limite de 30 dias corresponde ao prazo regulamentar de declaração de extravio | O motivo foi atribuído ao literal sem evidência. O arquivo não contém nome de constante, comentário ou leitura de configuração para esse valor. A explicação sai, a origem fica como LACUNA e a pergunta vai para Q3. O termo "extravio" também sai do vocabulário, que passa a usar Empréstimo em Atraso Longo. | L18 contém apenas `if (diasAtraso > 30)` |
| 4 | Nenhuma hipótese sobre a combinação de L18 e L24 | Para leitor de tipo diferente de PROFESSOR e ESTUDANTE, a combinação produz multa menor no 31º dia do que no 30º quando a obra vale menos de R$ 75,00. A hipótese entra como H6 e segue para Q5. | L24 dá 30 × 2.50m = 75,00 no 30º dia, e L20 devolve `valorObra` a partir do 31º |
| 5 | E7 citado como evidência de confiança alta em H4 | Comentário sustenta intenção, com peso baixo. O comentário de L04 contradiz L18–L27 e fica registrado como CONFLITO. | L04 afirma "qualquer multa", e o ramo de L20 não aplica desconto |

## Movimento 6: derivação de testes

Os dois testes abaixo são testes de caracterização em xUnit e registram o comportamento implementado, com a expectativa tirada da leitura do código. Eles aguardam a validação de domínio das perguntas Q4 e Q1, e o nome de cada teste traz o ID da regra e o desfecho "em aberto". A página apresenta os testes como leitura, e a execução deles fica fora da aula.

```csharp
using System;
using Xunit;

public class MultasCaracterizacaoTest
{
    // Comportamento implementado. Aguarda Q4 do especialista.
    [Fact]
    public void RC02_EmAberto_EstudanteComAtrasoLongoPagaValorIntegralDaObra()
    {
        var prevista = new DateTime(2026, 3, 1);
        var devolucao = new DateTime(2026, 4, 5); // 35 dias de atraso

        decimal multa = Multas.CalcularMulta(prevista, devolucao, "ESTUDANTE", 80.00m);

        Assert.Equal(80.00m, multa); // L18-L20 antes de L25-L27
    }

    // Comportamento implementado. Aguarda Q1 do especialista.
    [Fact]
    public void RD01_EmAberto_DevolucaoAusenteContaAtrasoAteHoje()
    {
        var prevista = DateTime.Today.AddDays(-10);

        decimal multa = Multas.CalcularMulta(prevista, null, "COMUM", 50.00m);

        Assert.Equal(25.00m, multa); // L09 e L24: 10 x 2.50m
    }
}
```

O primeiro teste fixa a precedência de L18 sobre L25, e o segundo fixa o efeito do `null` em L09. O segundo teste depende do relógio do sistema, porque o método lê `DateTime.Today` em L09, e essa dependência entra no catálogo como parte do comportamento implementado. Se o especialista responder sim a Q4, a H4 revisada é confirmada e o primeiro teste passa a valer como teste de regressão. Se responder não, isto é, se a intenção for que o estudante pague metade também do valor da obra, o comportamento atual é um defeito, e o primeiro teste documenta esse defeito até a correção e é substituído por um teste de aceitação com a expectativa de R$ 40,00, conforme o destino descrito em [Testes de caracterização](arqueologia-de-regras-conceitos.md#testes-de-caracterizacao).

## Leitura do exemplo

O método de 33 linhas produziu três classificações, quatro derivações, duas exceções com a precedência declarada, uma tabela de decisão com política First, cinco perguntas fechadas ao especialista e dois testes de caracterização, todos com o intervalo de linhas que os sustenta. As correções 1 e 3 retiraram afirmações do agente sem trecho do arquivo que as sustentasse, o ator da cobrança e o motivo do limite de 30 dias, e as correções 2, 4 e 5 vieram da conferência do aninhamento entre L18, L22 e L25, da combinação entre L20 e L24 e do peso dado ao comentário de L04.

**Próxima página:** [Exercício de IA: arqueologia de regras em SQL](arqueologia-de-regras-exercicio.md).
