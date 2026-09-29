# Exercício de IA — Geral: mapa de regras do cashback

Neste exercício, você transformará um recorte da nova tributação brasileira em um mapa de regras no vocabulário do SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG que separa conceitos, fatos e regras). O objeto é o cashback do IBS e da CBS para famílias de baixa renda, disciplinado pela Lei Complementar nº 214/2025 e alterado pela Lei Complementar nº 227/2026.

## Fonte pública

Use o [texto compilado da Lei Complementar nº 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm), publicado pela Presidência da República com as alterações da Lei Complementar nº 227/2026 e consultado em 29 de setembro de 2026, com atenção aos artigos 112, 113, 116, 117 e 118 e ao artigo 124, que define “devolução geral” e “devolução específica”. O texto compilado é a única fonte do exercício, e em caso de divergência entre ele e qualquer síntese desta página prevalece o texto legal.

## Texto complexo para decompor

> [1] A devolução de IBS e CBS destina-se ao responsável por unidade familiar de baixa renda cadastrada no CadÚnico quando essa pessoa, cumulativamente, tiver renda familiar mensal per capita de até meio salário-mínimo, residir no território nacional e possuir inscrição regular no CPF. [2] No cálculo entra o consumo documentado por notas vinculadas ao CPF dos membros da unidade familiar, desde que a aquisição seja exclusivamente para consumo domiciliar, [3] “ressalvados os bens e serviços sujeitos ao Imposto Seletivo”. [4] Na aquisição de botijão de gás liquefeito de petróleo de até 13 kg, no fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e no fornecimento de telecomunicações, a devolução geral corresponde a 100% da CBS e 20% do IBS, e nos demais casos corresponde a 20% de cada tributo. [5] No fornecimento domiciliar de energia elétrica, água, esgoto e gás canalizado e nos serviços de telecomunicações, a devolução é concedida no momento da cobrança, e nos demais casos no momento definido em regulamento. [6] Cada ente pode, por lei específica, fixar percentual superior para sua parcela, exceto no percentual da CBS aplicado às categorias da frase [4]. [7] A diferença entre o valor apurado com esse percentual próprio e a devolução geral chama-se devolução específica. [8] Os valores são disponibilizados ao agente financeiro no prazo máximo de 15 dias após a apuração, e o agente financeiro deve transferi-los às famílias destinatárias em até 10 dias após essa disponibilização.

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
| [8] | paráfrase | art. 116, §§3º e 4º |

A lista da frase [5] tem cinco categorias e a da frase [4] tem seis, porque o art. 116, §1º, menciona energia elétrica, água, esgoto, gás canalizado e telecomunicações, enquanto o botijão de gás liquefeito de petróleo aparece apenas no art. 118, I. O mapa precisa representar essa diferença em duas regras distintas, uma para o percentual e outra para o momento da devolução.

![Fluxo em duas faixas independentes que partem da mesma caixa, Fonte pública (LC 214/2025, texto compilado). A faixa Geral segue pela marcação inicial feita pelo participante, pelo mapa completo das seções A a I gerado pelo agente, pela revisão por camada e pela tabela de decisão com política de acerto e precedência. A faixa Especialista segue pelo mapa reduzido às seções A, C, D, F e G gerado pelo agente, pelas regras testáveis, pela matriz de testes, pela crítica da matriz e pelo ciclo TDD de vermelho, verde e refatorar, e termina em test.todo para cada caso INDETERMINADO. Nenhuma seta liga as duas faixas.](assets/fluxo-regra-tributaria.png)

*Leitura da figura: esta página cobre a faixa Geral, a superior, lida da esquerda para a direita a partir da fonte pública até a tabela de decisão. A etiqueta de cada caixa indica quem executa o passo, e a faixa Especialista, abaixo, corre no mesmo horário a partir da mesma fonte e gera o próprio mapa reduzido.*

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

O prompt usa seis prefixos de identificação e quatro rótulos de controle, definidos na lista abaixo para que a saída de duplas com agentes diferentes possa ser comparada:

- **CT**: conceito do vocabulário, definido por gênero e diferença.
- **FT**: tipo de fato, que liga conceitos por meio de um verbo.
- **RC**: regra estrutural de classificação, que diz quando algo pertence a uma categoria.
- **RD**: regra estrutural de derivação, que diz como um valor é calculado.
- **RN**: regra operativa, que rege a conduta de um ator capaz de descumpri-la.
- **EX**: regra de exceção, que referencia o ID da regra que ela afeta.
- **LACUNA**: ponto a que a fonte não responde.
- **REGULAMENTO**: ponto que a fonte remete a regulamento.
- **CONFLITO**: par de regras que não podem valer ao mesmo tempo.
- **INFERÊNCIA**: conclusão do agente que não consta da fonte.

Cole no agente o texto complexo, a tabela de natureza das frases, o link oficial e este prompt:

```text
Atue como analista de regras de negócio e formalize o texto fornecido no
vocabulário do SBVR (OMG), com sentenças no estilo RuleSpeak em português.

ENTRADA
- Frases numeradas [1] a [8]: síntese didática dos arts. 112, 113, 116, 117,
  118 e 124 da LC 214/2025, texto compilado. Só a frase [3] é transcrição
  literal, e as demais são paráfrases.
- Tabela que liga cada frase ao dispositivo legal.
- Link do texto compilado. Se não conseguir abri-lo, trabalhe só com o texto
  e a tabela e declare isso no início da resposta.

LIMITES
- Não ofereça orientação jurídica e não use artigos fora da lista acima.
- Não apresente paráfrase como texto de lei: transcreva trecho legal apenas
  se você o leu no link e, nos demais casos, cite a frase [n] e o dispositivo
  da tabela.
- Quando transcrever trecho legal lido no link, use o menor fragmento que
  sustenta a regra.
- Diante de lacuna, não invente resposta, data ou valor: registre LACUNA e
  formule a pergunta na seção I.

CONVENÇÕES
1. Vocabulário antes das regras. Toda regra usa apenas conceitos da seção A
   e tipos de fato da seção B. Termo novo entra primeiro em A.
2. Conceito (CT-nn): termo, definição por gênero e diferença ("X é um Y
   que ..."), sinônimos a evitar, frase de origem.
3. Tipo de fato (FT-nn): "<conceito> <verbo> <conceito>", leitura inversa e
   cardinalidade. Cardinalidade não informada pela fonte recebe LACUNA.
4. Regra estrutural, de modalidade alética, que nenhum ator descumpre:
   - classificação RC-nn: "Um <conceito> é um <conceito> se ..."
   - derivação RD-nn: "<valor> é calculado como ...".
   Percentuais, passos de cálculo, critérios de inclusão num total e limites
   de valor são sempre regras estruturais.
5. Regra operativa RN-nn, de modalidade deôntica, somente quando existe um
   ator que pode descumpri-la: "<ator> deve ...", "<ator> não deve ...",
   "<ator> pode ... somente se ...". Se a fonte não nomear o ator, registre
   LACUNA e não atribua ator por conta própria.
6. Uma regra por sentença, com um único efeito. Cláusulas com "salvo",
   "exceto" ou "desde que" são registradas como regra de exceção EX-nn, que
   referencia o ID da regra afetada.
7. Rótulos de controle: LACUNA (a fonte não responde), REGULAMENTO (a fonte
   remete a regulamento), CONFLITO (duas regras não podem valer juntas),
   INFERÊNCIA (conclusão sua, ausente da fonte).

SAÍDA, uma tabela por seção
A. Conceitos: ID | termo | definição | sinônimos a evitar | frase
B. Tipos de fato: ID | fato | leitura inversa | cardinalidade | frase
C. Classificação: ID | sentença | evidência | confiança | pergunta de validação
D. Derivação: mesmas colunas de C
E. Operativas: ID | tipo | ator | sentença | evidência | confiança | pergunta
F. Exceções e precedência: ID | regra afetada | sentença | qual prevalece e
   por quê
G. Controles: rótulo | descrição | frase | pergunta
H. Tabela de decisão. Condições: pessoa destinatária, documento vinculado ao
   CPF de membro, consumo domiciliar, sujeição ao Imposto Seletivo, categoria
   da aquisição. Resultados: percentual de CBS, percentual de IBS, momento da
   devolução. Declare a política de acerto do DMN (Unique, First ou Priority)
   e justifique. Se duas linhas puderem valer ao mesmo tempo, a política não
   pode ser Unique.
I. Perguntas para revisão jurídica, numeradas, cada uma com o ID a que se refere.

Evidência: frase [n] e dispositivo (artigo, parágrafo, inciso).
Confiança: alta (texto explícito), média (uma inferência), baixa (depende de
interpretação).

Antes de responder, confira se toda RN tem ator, se nenhuma RN descreve
cálculo, se todo termo usado nas regras está em A e se toda cláusula de
exceção está em F.
```

## Passo 3 — revise por camada

| Verificação | Pergunta de controle |
|---|---|
| Vocabulário | Toda regra usa apenas conceitos da seção A e fatos da seção B? |
| Conceitos | “Responsável familiar” e “membro da unidade familiar” ficaram distintos? |
| Fatos | A ligação entre documento fiscal, CPF e membro da unidade familiar foi representada? |
| Classificação | Os quatro critérios cumulativos da pessoa destinatária aparecem juntos? |
| Derivação | Percentual do tributo foi separado do valor monetário devolvido? |
| Operação | O mapa registrou como regra operativa a obrigação do agente financeiro de transferir os valores às famílias destinatárias em até 10 dias após a disponibilização (frase [8], art. 116, §§3º e 4º), e só marcou como LACUNA o ator da concessão no momento da cobrança depois de confirmar que o recorte não o nomeia? |
| Exceção | Itens sujeitos ao Imposto Seletivo ficaram fora do consumo considerado? |
| Categorias | O botijão ficou com os percentuais da frase [4] e com o momento definido em regulamento da frase [5]? |
| Limite de ampliação | A exceção da frase [6] impede ampliar o percentual da CBS das categorias da frase [4]? |
| Terminologia | O mapa reserva “devolução específica” para a diferença da frase [7] e chama de devolução geral os percentuais da frase [4]? |
| Evidência | Cada regra transcreve apenas o fragmento mínimo, com artigo, parágrafo e inciso? |
| Regulamento | O momento definido em regulamento da frase [5] recebeu o rótulo REGULAMENTO, sem data inventada, e LACUNA ficou reservado ao que a fonte deixa sem resposta? |

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
