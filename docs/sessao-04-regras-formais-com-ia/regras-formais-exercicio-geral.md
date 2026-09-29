# Exercício de IA — Geral: mapa de regras do cashback

Neste exercício, você transformará um recorte da nova tributação brasileira em um mapa de regras no vocabulário do SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG que separa conceitos, fatos e regras). O objeto é o cashback do IBS e da CBS para famílias de baixa renda, disciplinado pela Lei Complementar nº 214/2025 e alterado pela Lei Complementar nº 227/2026.

## Fonte pública

Use o [texto compilado da Lei Complementar nº 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm), publicado pela Presidência da República com as alterações da Lei Complementar nº 227/2026 e consultado em 29 de setembro de 2026, com atenção aos artigos 112, 113, 116, 117 e 118 e ao artigo 124, que define “devolução geral” e “devolução específica”. O texto compilado é a única fonte do exercício, e em caso de divergência entre ele e qualquer síntese desta página prevalece o texto legal.

## Texto complexo para decompor

> [1] A devolução de IBS e CBS destina-se ao responsável por unidade familiar de baixa renda cadastrada no CadÚnico quando essa pessoa, cumulativamente, tiver renda familiar mensal per capita de até meio salário-mínimo, residir no território nacional e possuir inscrição regular no CPF. [2] No cálculo entra o consumo documentado por notas vinculadas ao CPF dos membros da unidade familiar, desde que a aquisição seja exclusivamente para consumo domiciliar, [3] “ressalvados os bens e serviços sujeitos ao Imposto Seletivo”. [4] Na aquisição de botijão de gás liquefeito de petróleo de até 13 kg, no fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e no fornecimento de telecomunicações, a devolução geral corresponde a 100% da CBS e 20% do IBS, e nos demais casos corresponde a 20% de cada tributo. [5] No fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e nos serviços de telecomunicações, a devolução é concedida no momento da cobrança, e nos demais casos no momento definido em regulamento. [6] Cada ente pode, por lei específica, fixar percentual superior para sua parcela, exceto no percentual da CBS aplicado às categorias da frase [4]. [7] A diferença entre o valor apurado com esse percentual próprio e a devolução geral chama-se devolução específica.

!!! info "Natureza de cada frase"
    O bloco é uma **síntese didática** montada para a aula. A tabela indica, frase por frase, se o trecho é paráfrase ou transcrição e de que dispositivo ele vem, para que a evidência do mapa possa ser conferida no texto compilado.

| Frase | Natureza | Dispositivo da LC 214/2025 |
|---|---|---|
| [1] | paráfrase | art. 112, caput, e art. 113, caput e incisos I a III |
| [2] | paráfrase | art. 117, caput e §2º, II |
| [3] | transcrição literal | art. 117, §2º, I, com redação dada pela LC 227/2026 |
| [4] | paráfrase | art. 118, I e II, e art. 124, I |
| [5] | paráfrase | art. 116, caput e §1º |
| [6] | paráfrase | art. 118, §§1º e 3º |
| [7] | paráfrase | art. 124, II |

A lista da frase [5] tem cinco categorias e a da frase [4] tem seis, porque o art. 116, §1º, menciona energia elétrica, água, esgoto, gás canalizado e telecomunicações, enquanto o botijão de gás liquefeito de petróleo aparece apenas no art. 118, I. O mapa precisa representar essa diferença em duas regras distintas, uma para o percentual e outra para o momento da devolução.

![Fluxo em duas faixas. Na faixa do exercício geral, a fonte pública (LC 214/2025, texto compilado) segue para a marcação inicial feita pelo participante, o mapa de regras gerado pelo agente com RC, RD, RN, evidência e LACUNA, a revisão por camada e a tabela de decisão com política de acerto e precedência. O mapa revisado é a entrada da faixa do exercício especialista, que segue por regras testáveis, matriz de testes gerada pelo agente, crítica da matriz e ciclo TDD de vermelho, verde e refatorar, e termina em test.todo para cada caso INDETERMINADO.](assets/fluxo-regra-tributaria.png)

*Leitura da figura: esta página cobre a faixa superior, lida da esquerda para a direita. A etiqueta de cada caixa indica quem executa o passo, e a seta de retorno mostra que o mapa revisado nesta página é a entrada do exercício especialista, na faixa inferior.*

## Passo 1 — marque antes de perguntar

Em três minutos, use anotações diferentes para:

- conceitos
- fatos entre conceitos
- condições de classificação
- cálculos ou derivações
- obrigações, proibições e permissões, com o ator de cada uma
- exceções, precedência e pontos ainda dependentes de regulamento

Sua marcação é a linha de base para comparar a saída do agente.

## Passo 2 — gere o mapa

Cole no agente o texto complexo, a tabela de natureza das frases, o link oficial e este prompt:

```text
Atue como analista de regras de negócio. O texto fornecido é uma síntese
didática dos arts. 112, 113, 116, 117, 118 e 124 da LC 214/2025, em seu
texto compilado. Consulte o link apenas para conferir evidência. Não ofereça
orientação jurídica e não amplie o escopo para outros artigos.

Produza um mapa com seções independentes:
A. conceitos, definições e sinônimos perigosos;
B. tipos de fato que relacionam os conceitos;
C. regras estruturais de classificação (ID RC-nn);
D. regras estruturais de derivação (ID RD-nn);
E. regras operativas, separadas em obrigação, proibição e permissão
   (ID RN-nn), cada uma com o ator cuja conduta ela rege;
F. exceções e precedência;
G. conflitos, lacunas e dependências de regulamento;
H. tabela de decisão com política de acerto declarada;
I. perguntas para revisão jurídica.

Para cada regra:
- atribua ID estável;
- escreva uma sentença atômica em SBVR/RuleSpeak;
- cite artigo, parágrafo e inciso como evidência;
- transcreva no máximo o menor fragmento da fonte que sustenta a regra;
- marque confiança alta, média ou baixa;
- escreva uma pergunta de validação quando houver inferência.

Ao tratar lacunas, não invente resposta. Não transforme ausência de
disposição na fonte em regra. Não escolha interpretação jurídica quando
duas leituras forem possíveis. Use o rótulo LACUNA e formule a pergunta
necessária na seção I.
```

## Passo 3 — revise por camada

| Verificação | Pergunta de controle |
|---|---|
| Conceitos | “Responsável familiar” e “membro da unidade familiar” ficaram distintos? |
| Fatos | A ligação entre documento fiscal, CPF e membro da unidade familiar foi representada? |
| Classificação | Os quatro critérios cumulativos da pessoa destinatária aparecem juntos? |
| Derivação | Percentual do tributo foi separado do valor monetário devolvido? |
| Operação | A concessão no momento da cobrança recebeu um ator, ou ficou como LACUNA porque os artigos do recorte não o nomeiam? |
| Exceção | Itens sujeitos ao Imposto Seletivo ficaram fora do consumo considerado? |
| Categorias | O botijão ficou com os percentuais da frase [4] e com o momento definido em regulamento da frase [5]? |
| Limite de ampliação | A exceção da frase [6] impede ampliar o percentual da CBS das categorias da frase [4]? |
| Terminologia | O mapa reserva “devolução específica” para a diferença da frase [7] e chama de devolução geral os percentuais da frase [4]? |
| Evidência | Cada regra transcreve apenas o fragmento mínimo, com artigo, parágrafo e inciso? |
| Lacuna | A expressão “momento definido em regulamento” permaneceu sem data inventada? |

## Passo 4 — confronte a tabela

Uma **tabela de decisão** organiza em linhas as combinações de condições e o resultado de cada uma, com uma política de acerto que diz qual linha vale quando mais de uma se aplica. A tabela deste recorte precisa distinguir ao menos pessoa elegível, documento vinculado, consumo domiciliar, incidência de Imposto Seletivo e categoria da aquisição. Se duas linhas puderem combinar, o agente deve explicar a precedência, e uma política `Unique` só é defensável depois que as categorias forem tornadas mutuamente exclusivas.

## Evidência a entregar

Entregue:

1. sua marcação inicial
2. o mapa do agente com conceitos, fatos e tipos de regra separados
3. a tabela de decisão
4. três correções feitas por você
5. duas lacunas ou perguntas que precisam de validação jurídica

**Próxima página:** [Exercício de IA — Especialista](regras-formais-exercicio-especialista.md).
