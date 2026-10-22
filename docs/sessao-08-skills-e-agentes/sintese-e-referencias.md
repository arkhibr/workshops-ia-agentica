# Síntese e referências

## Oito ideias essenciais

1. **Uma skill carrega em três níveis.** Os metadados custam cerca de 100 tokens por skill e ficam sempre no contexto, o corpo do `SKILL.md` carrega quando a skill é acionada e fica abaixo de 5 mil tokens, e os recursos e scripts carregam sob demanda, conforme a [documentação das skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao).
2. **Um subagente tem contexto, ferramentas e modelo próprios.** O isolamento mantém a saída volumosa fora da conversa principal, e o campo `tools` omitido faz o subagente herdar todas as ferramentas, de acordo com a [documentação dos subagentes](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao).
3. **Vários agentes só compensam em tarefas amplas e paralelizáveis.** O [relato da Anthropic](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) cita cerca de 4 vezes os tokens de um chat para um agente e cerca de 15 vezes para vários agentes, e aponta a maioria das tarefas de programação como mau encaixe.
4. **O artefato tem duas camadas de conferência.** O script verifica a estrutura, e a pessoa nomeada verifica o conteúdo que o script não decide, com o plano, a validação e a execução como padrão para operações em lote, segundo as [boas práticas de skills](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao).
5. **O modelo certo é o menor que passa nas avaliações da própria equipe.** O [guia de escolha](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) oferece duas estratégias de partida, com Haiku 5.5 ou Opus 5.5, e aponta o esforço como alavanca dentro de um mesmo modelo.
6. **O custo se declara antes e se mede depois.** A leitura do cache custa 0,1 do preço-base na maioria dos modelos, conforme a [documentação do cache](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao), e o [guia de custo](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) mostra o consumo com `/usage`.
7. **Desempenho tem três medidas que se compensam.** Tempo, tokens e taxa de acerto precisam ser registrados juntos, e o relato multiagente recomenda começar com cerca de 20 consultas reais.
8. **O agente usa identidade própria e credencial mínima.** O token tem escopo mínimo, validade curta e local de guarda fora do repositório, e o rodízio segue seis passos, conforme o [Microsoft Learn](../referencia/bibliografia.md#microsoft-use-personal-access-tokens-in-azure-devops-documentacao) e o [GitHub](../referencia/bibliografia.md#github-managing-your-personal-access-tokens-documentacao).

## Checklist antes de encerrar a sessão

- [ ] Cada pessoa criou uma skill, executou e conferiu o artefato nas duas camadas.
- [ ] A tabela de medição da oficina tem os dois modelos preenchidos.
- [ ] Cada equipe declarou os requisitos funcionais e não funcionais antes de construir.
- [ ] O subagente da equipe tem `tools` explícito e justificativa para escrita ou rede.
- [ ] Nenhuma credencial real foi usada, e o plano de cada equipe indica identidade, escopo, validade e cofre.
- [ ] A conferência cruzada produziu ao menos um achado por equipe.

## Autoavaliação

1. Consigo dizer quando uma tarefa deve ser uma skill, quando deve ser um subagente e quando deve permanecer no agente principal?
2. Sei estimar, em unidades relativas, o efeito do cache sobre uma tarefa repetida?
3. Sei explicar por que um campo de restrição com erro de grafia pode deixar um subagente com acesso total?
4. Consigo dizer qual identidade o meu agente usa e o que acontece se o token vazar hoje?

Se duas ou mais respostas forem "ainda não", releia [Segurança e credenciais](seguranca-e-credenciais.md) e [Custo de tokens](custo-de-tokens.md) antes da Sessão 9.

## Fundamentação

Todas as fontes citadas nesta sessão estão na [bibliografia do curso](../referencia/bibliografia.md), com URL. As fontes são documentação oficial acessada em 22/10/2026 e um relato de engenharia da própria Anthropic, e nenhuma delas mede as tarefas da equipe. Os números de custo e de desempenho valem para as versões e as configurações descritas em cada fonte.

| Página | Fontes citadas |
|---|---|
| Skills | [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao), [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) e [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) |
| Agentes e subagentes | [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao) e [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) |
| Geração de artefatos | [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) e [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) |
| Escolha de modelos | [Choosing the Right Model](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) e [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) |
| Custo de tokens | [Manage costs](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code), [Prompt Caching](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao) e [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system) |
| Performance | [How We Built Our Multi-Agent Research System](../referencia/bibliografia.md#anthropic-how-we-built-our-multi-agent-research-system), [Prompt Caching](../referencia/bibliografia.md#anthropic-prompt-caching-documentacao), [Choosing the Right Model](../referencia/bibliografia.md#anthropic-choosing-the-right-model-documentacao) e [Skill authoring best practices](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) |
| Segurança e credenciais | [Claude Code Security](../referencia/bibliografia.md#anthropic-claude-code-security-documentacao), [Agent Skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao), [Subagents](../referencia/bibliografia.md#anthropic-subagents-no-claude-code-documentacao), [Azure DevOps PATs](../referencia/bibliografia.md#microsoft-use-personal-access-tokens-in-azure-devops-documentacao) e [GitHub PATs](../referencia/bibliografia.md#github-managing-your-personal-access-tokens-documentacao) |

## Conexão com a próxima sessão

A Sessão 9 trata de depuração sistemática e de revisão de código gerado por IA. Ela parte de skills e agentes que a equipe já escreveu nesta sessão, porque um agente que gera código ou artefatos produz defeitos que precisam de hipótese, investigação e verificação, e o registro de modelo, tokens, tempo e resultado da conferência, definido aqui, é o primeiro dado que a depuração consulta.
