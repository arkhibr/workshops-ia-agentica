# Síntese e referências

A sessão percorreu duas direções: da política escrita para o modelo formal e do código existente para as regras que ele implementa. Nos dois casos, o produto é um mapa rastreável em que cada regra aponta para o artigo ou a linha de código que a sustenta.

## Ideias essenciais

1. **Conceitos vêm antes das regras.** Um termo indefinido transfere a ambiguidade para todas as sentenças que o usam e para todos os testes derivados delas.
2. **Fatos ligam conceitos.** A leitura inversa de cada tipo de fato expõe a cardinalidade, a direção e os pressupostos que a prosa costuma deixar implícitos.
3. **Regra estrutural organiza o domínio.** Classificação e derivação definem o que as coisas são e como os valores se calculam, e nenhum ator as cumpre ou as descumpre.
4. **Regra operativa rege conduta.** Obrigação, proibição e permissão condicionada têm um ator identificável, que pode cumpri-las ou violá-las.
5. **Atomicidade torna a regra verificável.** Uma sentença com vários efeitos normativos precisa ser decomposta até que cada regra tenha um único efeito e um único ID.
6. **Tabela de decisão revela combinação e precedência.** A política de acerto, seja Unique, First ou Priority, faz parte da regra e precisa estar declarada na tabela.
7. **Lacuna é resultado válido.** Um agente disciplinado registra o rótulo LACUNA e formula a pergunta que o especialista do domínio precisa responder.
8. **TDD começa na regra.** Cada caso de teste conserva o ID e a evidência da sentença que lhe deu origem, e os casos indeterminados entram como pendentes.
9. **Código é evidência de comportamento implantado.** A arqueologia registra o que o SQL faz, e a intenção do negócio só entra no catálogo depois da validação de domínio.

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

- **[OMG — SBVR 1.5](../referencia/bibliografia.md#omg-semantics-of-business-vocabulary-and-business-rules).** Vocabulário, tipos de fato, regras estruturais e regras operativas.
- **[OMG — DMN 1.5](../referencia/bibliografia.md#decision-model-and-notation-dmn).** Tabelas de decisão e políticas de acerto Unique, First e Priority.
- **[Ronald G. Ross — RuleSpeak](../referencia/bibliografia.md#ross-rulespeak).** Formas controladas para sentenças de regra.
- **[Lei Complementar nº 214/2025, texto compilado](../referencia/bibliografia.md#lei-complementar-2142025-ibs-cbs-e-imposto-seletivo).** Arts. 112, 113, 116, 117 e 118 sobre destinatário, consumo considerado, momento e percentuais da devolução personalizada de IBS e CBS, e art. 124 sobre devolução geral e devolução específica, com as alterações da Lei Complementar nº 227/2026, acesso em 29 de setembro de 2026.

As referências completas e seus links estão na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 5 recebe o mapa produzido aqui, com regras atômicas identificadas por ID, e decompõe a entrega em tarefas que preservem a rastreabilidade até cada regra de origem.
