# Síntese e referências

A sessão percorreu duas direções: da política escrita para o modelo formal e do código existente para as regras que ele implementa. Nos dois casos, o produto é um mapa rastreável, não uma resposta elegante sem evidência.

## Ideias essenciais

1. **Conceitos vêm antes das regras.** Um termo indefinido transfere a ambiguidade para todas as sentenças que o usam.
2. **Fatos ligam conceitos.** Eles expõem cardinalidade, direção e pressupostos que a prosa costuma esconder.
3. **Regra estrutural organiza o domínio.** Classificação e derivação não são obrigações.
4. **Regra operativa rege conduta.** Obrigação, proibição e permissão condicionada podem ser cumpridas ou violadas.
5. **Atomicidade torna a regra verificável.** Uma sentença com vários efeitos precisa ser decomposta.
6. **Tabela de decisão revela combinação e precedência.** A política de acerto faz parte da regra.
7. **Lacuna é resultado válido.** Um agente disciplinado formula a pergunta em vez de completar o silêncio.
8. **TDD começa na regra.** O caso de teste conserva o ID e a evidência da sentença que lhe deu origem.
9. **Código prova comportamento, não intenção.** Arqueologia separa o que está implementado do que o domínio confirma.

## Checklist do mapa de regras

- [ ] Conceitos têm definições e sinônimos arriscados.
- [ ] Fatos relacionam os conceitos sem misturar consequência normativa.
- [ ] Classificações e derivações estão separadas.
- [ ] Obrigações, proibições e permissões usam sentenças atômicas.
- [ ] Exceções e precedência aparecem explicitamente.
- [ ] Cada regra possui ID, evidência, confiança e questão em aberto.
- [ ] A tabela declara política de acerto.
- [ ] Casos de teste apontam para a regra de origem.
- [ ] Lacunas permanecem sem resposta inventada.

## Autoavaliação

1. Consigo distinguir conceito, fato e regra numa frase densa?
2. Sei explicar por que uma derivação não é regra operativa?
3. Consigo transformar uma exceção distante em precedência explícita?
4. Sei recusar um resultado esperado quando a fonte não o determina?
5. Consigo citar as linhas de SQL que sustentam uma regra recuperada?

Se duas respostas forem “ainda não”, refaça o ninho de IRPF usando o prompt-base e compare sua decomposição com as seis etapas do exemplo.

## Fundamentação

- **OMG — SBVR 1.5.** Vocabulário, tipos de fato, regras estruturais e regras operativas.
- **OMG — DMN 1.5.** Tabelas de decisão e políticas de acerto.
- **Ronald G. Ross — RuleSpeak.** Formas controladas para sentenças de regra.
- **Lei Complementar nº 214/2025, texto compilado.** Arts. 112 a 124 sobre devolução personalizada de IBS e CBS, com alterações posteriores.
- **Receita Federal — Principais marcos regulatórios.** Contexto oficial da implantação da reforma da tributação do consumo.

As referências completas e seus links estão na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 5 recebe regras menores, identificadas e testáveis. O próximo passo é decompor a entrega em tarefas que preservem a rastreabilidade até o mapa produzido aqui.
