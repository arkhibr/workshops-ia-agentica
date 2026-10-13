# Síntese e referências

A sessão retomou o fluxo do GitHub Spec Kit com os três comandos opcionais, `clarify`, `checklist` e `analyze`, e com um princípio de constitution que exige o teste vermelho antes da implementação de cada história. Os exemplos e exercícios usaram dois pedidos de um sistema de pagamentos de projetos de pesquisa da ACME, uma universidade fictícia, e em cada comando a pergunta foi o que ele examina, o que grava e o que deixa de ver.

## Ideias essenciais

1. **Cada comando opcional examina o que os anteriores gravaram.** O `clarify` lê a spec antes do plano, o `checklist` lê os requisitos depois do plano, e o `analyze` lê spec, plano e tarefas antes da implementação, sem alterar nenhum arquivo.
2. **O `clarify` pergunta o que o agente considera aberto.** Uma decisão que o `specify` registrou em *Assumptions* ou declarou fora do escopo pode ser tratada como resolvida, e só a leitura dessas seções garante que ela seja encontrada.
3. **A recomendação do `clarify` é uma proposta do agente.** Aceitá-la grava na spec, como resposta do PO, uma decisão que pode alterar o pedido original, e a pergunta a fazer antes de cada "yes" é quem tem autoridade sobre aquela regra.
4. **O checklist testa a escrita dos requisitos.** Os itens `CHK` perguntam se o requisito é completo e verificável, a marcação `[x]` é decisão de quem revisa, e o `implement` para quando encontra item desmarcado.
5. **O princípio de teste vermelho muda as tarefas.** Sem ele, o modelo da versão 1.1.1 trata os testes como opcionais, e com ele cada história ganha uma seção de testes antes da implementação.
6. **O `analyze` aponta o teste que nasce verde.** As instruções do comando mandam classificar como CRITICAL toda violação da constitution, e no ensaio o agente classificou como HIGH um dos achados do princípio de teste vermelho, o que faz da severidade uma proposta a conferir.
7. **Conferir o vermelho é ler o motivo da falha.** Asserção sobre o valor esperado e esqueleto ainda não implementado são motivos certos, módulo inexistente (`ERR_MODULE_NOT_FOUND`) é um vermelho fraco que pede os esqueletos e uma nova execução, e erro de digitação e teste que já passava indicam problema no teste.
8. **A troca do operador mostra se a fronteira tem teste.** Trocar `<=` por `<` muda o resultado só no valor exato do limite, e se nenhum teste falha a suíte não cobre esse valor.

## Checklist da sessão

- [ ] O `clarify` rodou antes do `plan`, e cada recomendação aceita foi conferida contra o pedido do PO.
- [ ] As seções *Assumptions* e de escopo foram lidas depois do `clarify`.
- [ ] O checklist foi gerado e os itens desmarcados foram lidos antes de responder à trava do `implement`.
- [ ] A constitution tem o princípio de teste vermelho, e o `tasks.md` tem seção de testes antes da implementação em cada história.
- [ ] O `analyze` rodou, o `git status` confirmou que nada mudou, e cada achado CRITICAL foi corrigido ou registrado.
- [ ] O vermelho foi conferido pelo motivo de cada falha antes de seguir para o verde.
- [ ] A troca do operador da fronteira derrubou ao menos um teste, e o código foi restaurado.

## Autoavaliação

1. Sei dizer em que posição do fluxo roda cada comando opcional e o que cada um grava?
2. Consigo apontar, numa spec, uma decisão do agente que o `clarify` não perguntou?
3. Sei explicar a diferença entre um item de checklist e um teste do código?
4. Consigo ler um relatório do `analyze` e dizer por que um achado é CRITICAL?
5. Sei distinguir uma falha de teste pelo motivo certo de uma falha por problema no teste?

Se duas respostas forem "ainda não", refaça o exercício do saldo da rubrica com a recomendação do `clarify` recusada na pergunta sobre a reserva de saldo, e compare as tarefas e os testes gerados com os da primeira execução.

## Fundamentação

- **[GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit).** Instruções dos comandos `clarify`, `checklist`, `analyze`, `tasks` e `implement` instaladas pelo `specify init` da versão 1.1.1, usadas em todos os trechos desta sessão.
- **[Beck — Test-Driven Development: By Example (2002)](../referencia/bibliografia.md#beck-test-driven-development-by-example-2002).** Ciclo vermelho, verde e refatoração, com o teste escrito antes do código e visto falhando.
- **[Mathews e Nagappan — Test-Driven Development and LLM-based Code Generation (2024)](../referencia/bibliografia.md#mathews-e-nagappan-test-driven-development-and-llm-based-code-generation-2024).** Efeito de fornecer os testes junto com o enunciado na proporção de soluções corretas geradas por modelos de linguagem.
- **[Intervenção socrática, Sessão 3](../sessao-03-exploracao-especificacao/intervencao-socratica-conceitos.md#uma-pergunta-por-mensagem-cinco-fases-seis-categorias).** Contrato de uma pergunta por mensagem, sem sugerir a resposta, usado como comparação com o formato de pergunta do `clarify`.

As referências completas e seus links estão na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A troca manual de um operador, feita no exercício do Tema 2, é um caso único de teste de mutação. A Sessão 7 automatiza essa verificação, junto com testes de propriedade e de contrato, e decide onde cada técnica compensa o custo. Antes dela, a [tarefa entre sessões](tarefa-entre-sessoes.md) repete o fluxo desta sessão, do `init` ao `analyze`, sobre o pedido da ordem de compra.

**Próxima página:** [Tarefa entre sessões](tarefa-entre-sessoes.md).
