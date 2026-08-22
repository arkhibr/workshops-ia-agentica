# Síntese e referências

## Onze ideias essenciais

1. **Um ambiente agêntico tem quatro peças: harness, arquivo de configuração, MCP e isolamento por ramo.** Só a primeira depende de qual ferramenta o time escolhe; as outras três são agnósticas.
2. **Context engineering é mais amplo que prompt engineering.** Cuida de tudo que chega à janela de contexto numa execução, não só do texto da instrução.
3. **A janela de contexto degrada de forma gradual, não abrupta, conforme cresce.** A degradação de contexto (*context rot*) é o motivo técnico por trás de recuperação just-in-time, compactação e sub-agentes com contexto isolado.
4. **Ferramentas são o contrato entre o agente e o ambiente.** Uma ferramenta mal desenhada consome espaço de contexto que poderia ir para informação relevante.
5. **O MCP transforma M×N integrações numa soma.** Cada modelo e cada ferramenta implementam o protocolo uma vez, em vez de cada par precisar da própria integração. As três primitivas do protocolo (*tools*, *resources*, *prompts*) ajudam a decidir que tipo de acesso pedir depois de decidir conectar.
6. **O AGENTS.md é um padrão aberto, não de um fornecedor.** Mantido pela Agentic AI Foundation (Linux Foundation), lido por agentes de múltiplos fornecedores concorrentes, com suporte nativo a mais de um arquivo por monorepo.
7. **Uma linha de arquivo de instrução só vale a pena se muda uma decisão real do agente.** "Escreva código limpo" não muda nada; "o comando de teste é X" muda.
8. **Conectar um servidor MCP exige avaliar origem, escopo e auditabilidade antes de autorizar.** Servidor de terceiro não é proibido, mas pede mais cautela do que servidor mantido pelo próprio fornecedor da ferramenta.
9. **Isolamento por ramo resolve conflito de sistema de arquivos, não de comunicação entre pessoas.** As duas coisas são problemas diferentes, mesmo quando aparecem juntas no mesmo incidente.
10. **Arquivo de instrução decai como qualquer documentação.** A correção é revisá-lo no mesmo PR que muda a convenção que ele documenta, e verificar de vez em quando, manualmente ou pela esteira de CI, se os comandos documentados ainda existem.
11. **Isolar por ramo tem custo de ambiente, não só de git.** Cada worktree precisa da própria instalação de dependências; sem automatizar esse passo, a fricção de esperar a instalação desestimula o hábito exatamente nos casos em que ele mais evitaria um conflito.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue nomear as quatro peças de um ambiente agêntico e qual delas é agnóstica de ferramenta.
- [ ] Cada participante saiu com um `AGENTS.md`/`CLAUDE.md` real, escrito para um repositório que usa de verdade.
- [ ] O grupo discutiu o Estudo de caso e chegou a um critério (não a uma opinião) para quando isolamento por ramo é obrigatório.
- [ ] Ninguém saiu achando que MCP é uma ferramenta específica — é um protocolo que qualquer ferramenta pode implementar.
- [ ] O grupo sabe nomear os três critérios (origem, escopo, auditabilidade) para avaliar um servidor MCP antes de conectar.
- [ ] O grupo sabe explicar por que um worktree novo pode exigir instalação de dependências antes de estar pronto para uso.

## Autoavaliação

1. Consigo explicar a diferença entre prompt engineering e context engineering sem dizer que uma é "melhor" que a outra?
2. Sei dizer, para o meu próprio repositório, uma linha de arquivo de instrução que muda comportamento real do agente?
3. Consigo explicar o problema M×N que o MCP resolve, com um exemplo próprio?
4. Sei distinguir um conflito de sistema de arquivos (que isolamento por ramo resolve) de um conflito de comunicação entre pessoas (que não resolve)?
5. Antes de conectar um servidor MCP novo, sei dizer quais das três primitivas (*tool*, *resource*, *prompt*) ele deveria expor para o meu caso, e qual escopo de permissão pedir?

Se duas ou mais respostas forem "ainda não", releia [Conceitos](conceitos.md) antes da Sessão 3.

**Síntese de mercado**

- ANTHROPIC. "Effective context engineering for AI agents". Anthropic Engineering, set. 2025.
- ANTHROPIC. "Introducing the Model Context Protocol". Anthropic News, 25 nov. 2024.
- Agentic AI Foundation (Linux Foundation). "AGENTS.md". Padrão aberto, formalizado em ago. 2025 por OpenAI, Google, Cursor, Factory e Sourcegraph.

Citações completas, com URL e resumo, em [../referencia/bibliografia.md](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 3 assume que o time já tem um ambiente compartilhado configurado e reconhece a diferença entre um arquivo de instrução que muda comportamento e um que só declara boas intenções. Ela avança para a exploração e especificação de requisitos: transformar um pedido vago em um contrato humano-agente no padrão BR/FR/NFR — o mesmo cuidado de "cada linha precisa mudar uma decisão", visto aqui para o arquivo de instrução, reaparece lá para a especificação inteira.
