# Exercício de IA — Geral: mapa de regras do cashback

Neste exercício, você transformará um recorte da nova tributação brasileira em um mapa de regras. O objeto é o cashback do IBS e da CBS para famílias de baixa renda, disciplinado pela Lei Complementar nº 214/2025 e alterado pela Lei Complementar nº 227/2026.

## Fonte pública

Use o [texto compilado da Lei Complementar nº 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm), especialmente os arts. 112, 113, 116 e 118. Consulte também a página da Receita Federal sobre os [principais marcos regulatórios](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/reforma-tributaria-do-consumo/marcos), que registra a LC 214/2025 e a LC 227/2026. Acesso verificado em 29 de setembro de 2026.

!!! info "Como o texto abaixo foi produzido"
    O bloco é uma **síntese didática**, não uma transcrição. Ele combina regras dos artigos indicados para criar um ninho examinável em aula. Em caso de divergência, prevalece o texto legal compilado.

## Texto complexo para decompor

> A devolução de IBS e CBS destina-se ao responsável por unidade familiar de baixa renda cadastrada no CadÚnico quando essa pessoa, cumulativamente, tiver renda familiar mensal por pessoa de até meio salário mínimo, residir no Brasil e estiver com o CPF regular. No cálculo entram aquisições para consumo domiciliar documentadas por notas vinculadas ao CPF dos integrantes, mas ficam ressalvados os bens e serviços sujeitos ao Imposto Seletivo. Para botijão de gás liquefeito de petróleo de até 13 kg, energia elétrica domiciliar, água, esgoto, gás canalizado e telecomunicações, a devolução geral corresponde a 100% da CBS e 20% do IBS; nos demais casos, corresponde a 20% de cada tributo. Nos fornecimentos domiciliares indicados, a devolução ocorre no momento da cobrança; nos outros, no momento definido em regulamento. Lei específica de cada ente pode fixar percentual superior para sua parcela.

## Passo 1 — marque antes de perguntar

Em três minutos, use anotações diferentes para:

- conceitos;
- fatos entre conceitos;
- condições de classificação;
- cálculos ou derivações;
- obrigações, proibições e permissões;
- exceções, precedência e pontos ainda dependentes de regulamento.

Sua marcação é a linha de base para comparar a saída do agente.

## Passo 2 — gere o mapa

Cole no agente o texto complexo, os links oficiais e este prompt:

```text
Atue como analista de regras de negócio. O texto fornecido é uma síntese
didática dos arts. 112, 113, 116 e 118 da LC 214/2025, em seu texto
compilado. Consulte os links apenas para conferir evidência; não ofereça
orientação jurídica e não amplie o escopo para outros artigos.

Produza um mapa com seções independentes:
A. conceitos, definições e sinônimos perigosos;
B. tipos de fato que relacionam os conceitos;
C. regras estruturais de classificação;
D. regras estruturais de derivação;
E. regras operativas, separadas em obrigação, proibição e permissão;
F. exceções e precedência;
G. conflitos, lacunas e dependências de regulamento;
H. tabela de decisão com política de acerto declarada.

Para cada regra:
- atribua ID estável;
- escreva uma sentença atômica em SBVR/RuleSpeak;
- cite artigo, inciso ou parágrafo como evidência;
- marque confiança alta, média ou baixa;
- escreva uma pergunta de validação quando houver inferência.

Ao tratar lacunas, não invente resposta. Não transforme silêncio da fonte em
regra. Não escolha interpretação jurídica quando duas leituras forem
possíveis. Use o rótulo LACUNA e formule a pergunta necessária.
```

## Passo 3 — revise por camada

| Verificação | Pergunta de controle |
|---|---|
| Conceitos | “Responsável familiar” e “integrante” ficaram distintos? |
| Fatos | A ligação entre documento fiscal, CPF e integrante foi representada? |
| Classificação | Os quatro critérios cumulativos da pessoa destinatária aparecem juntos? |
| Derivação | Percentual do tributo foi separado do valor monetário devolvido? |
| Operação | Momento da devolução foi tratado como obrigação, não como fórmula? |
| Exceção | Itens sujeitos ao Imposto Seletivo ficaram fora do consumo considerado? |
| Lacuna | A expressão “momento definido em regulamento” permaneceu sem data inventada? |

## Passo 4 — confronte a tabela

A tabela precisa distinguir ao menos estas dimensões: pessoa elegível, documento vinculado, consumo domiciliar, incidência de Imposto Seletivo e categoria da aquisição. Se duas linhas puderem combinar, o agente deve explicar a precedência. Para este recorte, uma política `Unique` é defensável somente depois que as categorias forem tornadas mutuamente exclusivas.

## Evidência a entregar

Entregue:

1. sua marcação inicial;
2. o mapa do agente com conceitos, fatos e tipos de regra separados;
3. a tabela de decisão;
4. três correções feitas por você;
5. duas lacunas ou perguntas que precisam de validação jurídica.

**Próxima página:** [Exercício de IA — Especialista](regras-formais-exercicio-especialista.md).
