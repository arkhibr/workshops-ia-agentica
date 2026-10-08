# Síntese e referências

A sessão percorreu o caminho básico do GitHub Spec Kit, da constitution ao código com testes passando, sobre duas features da Vetor, a plataforma fictícia de e-commerce B2B do workshop. Em cada artefato, a pergunta foi a mesma: o que o agente decidiu que o pedido do PO não decidiu, e onde essa decisão vai aparecer depois.

## Ideias essenciais

1. **O Spec Kit impõe ordem e lugar.** Quem escreve cada artefato é o agente. A ferramenta garante que a spec exista antes do plano, que o plano exista antes das tarefas e que tudo fique gravado em arquivo versionado.
2. **Princípio útil muda a saída.** Um princípio da constitution vale quando removê-lo faria desaparecer alguma coisa da spec, do plano ou das tarefas. Sem o princípio de teste antes do código, o template trata as tarefas de teste como opcionais.
3. **A spec decide onde o pedido foi omisso.** Suposições, casos de borda e critérios de sucesso são os lugares onde o agente registra decisões próprias no mesmo tom das regras. Uma decisão que muda um resultado calculado volta para o dono da regra.
4. **Erro na spec chega ao código pelo caminho mais curto.** Cada comando lê os anteriores como premissa. Um critério de sucesso sem origem vira campo de contrato no plano, tarefa no `tasks.md` e código no `implement`.
5. **A rastreabilidade depende da constitution.** O Spec Kit numera requisitos e histórias e desconhece os IDs de regra. Com um princípio de rastreabilidade, localizar uma regra no código vira uma busca textual.
6. **Tarefa atômica tem um comando que prova a conclusão.** O tamanho certo depende de quem executa: grande demais falha mais, pequena demais consome atenção sem decidir nada.
7. **Critério que não falha não verifica.** Ver o teste falhar antes da implementação prova que ele distingue o código pronto do ausente.
8. **O ponto de controle humano é escolhido.** O `implement` valida as fases sozinho e só para quando algo falha. A parada humana existe quando alguém roda o comando por etapa.

## Checklist do caminho básico

- [ ] A constitution tem poucos princípios, e cada um muda alguma saída.
- [ ] Todo requisito funcional cita a regra de origem, ou tem justificativa para não citar.
- [ ] Nenhuma suposição, caso de borda ou critério de sucesso decide regra de negócio sem dono.
- [ ] O *Constitution Check* do plano traz evidência em cada linha.
- [ ] A lista de arquivos do plano não toca código existente sem motivo.
- [ ] As tarefas que tocam código existente estão marcadas para parada humana.
- [ ] Cada tarefa tem um comando que prova que terminou, e os testes foram vistos falhando.
- [ ] A busca pelo ID de cada regra devolve requisito, teste e código.

## Autoavaliação

1. Sei dizer o que cada um dos cinco comandos decide e onde grava?
2. Consigo escrever um princípio de constitution e apontar o que ele muda nas tarefas?
3. Encontro numa spec uma decisão que o agente tomou sozinho, mesmo quando ela está fora de *Assumptions*?
4. Consigo dizer se uma tarefa é atômica e qual comando prova que ela terminou?
5. Sei rodar o `implement` por etapa e explicar por que parei onde parei?

Se duas respostas forem "ainda não", refaça o exercício do frete com uma regra alterada, por exemplo baixando o limite do atacado para R$ 2.000,00, e use a busca pelo ID para ver o que precisa mudar.

## Fundamentação

- **[GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit).** Templates, scripts e comandos do caminho básico; versão 1.1.1, de 06/10/2026, usada em todos os trechos desta sessão.
- **[Delimarsky — Spec-Driven Development with AI (2025)](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025).** Lançamento do Spec Kit e a especificação como contrato do comportamento do código.
- **[Kwa et al. — Measuring AI Ability to Complete Long Software Tasks (2025)](../referencia/bibliografia.md#kwa-et-al-measuring-ai-ability-to-complete-long-software-tasks-2025).** Horizonte de tarefa de 50% como medida da capacidade de um agente, com duplicação a cada sete meses desde 2019.
- **[Prasad et al. — ADaPT: As-Needed Decomposition and Planning (2024)](../referencia/bibliografia.md#prasad-et-al-adapt-as-needed-decomposition-and-planning-2024).** Decomposição sob demanda, ajustada à capacidade do executor e à complexidade da tarefa.
- **[Parnas — On the Criteria to Be Used in Decomposing Systems into Modules (1972)](../referencia/bibliografia.md#parnas-on-the-criteria-to-be-used-in-decomposing-systems-into-modules-1972).** Decomposição pelas decisões que provavelmente vão mudar.

As referências completas e seus links estão na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 6 retoma o caminho completo com as variações que esta sessão deixou de lado: os comandos opcionais `clarify`, `analyze` e `checklist`, e o teste antes do código tratado como prática de engenharia, com xUnit e Jest.
