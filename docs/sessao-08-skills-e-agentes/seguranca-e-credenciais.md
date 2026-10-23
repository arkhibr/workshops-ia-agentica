# Segurança e credenciais

Uma skill ou um agente atua com as permissões e as credenciais que recebe, e uma instrução maliciosa ou um erro do modelo têm o alcance dessas permissões. Esta página trata das permissões mínimas, do cuidado com as credenciais que o agente usa, em especial a regra de não emprestar a identidade pessoal do Windows e de preferir tokens de escopo restrito, e do ciclo de vida do token.

## Onde o risco entra

A [documentação de segurança do Claude Code](../referencia/bibliografia.md#anthropic-claude-code-security-documentacao) descreve uma arquitetura baseada em permissões. No modo manual, o Claude Code começa com permissão de leitura e pergunta antes de editar arquivos ou executar comandos. No modo automático, um modelo classificador separado revisa as ações e bloqueia as que julga inseguras. A ferramenta de shell pode rodar em sandbox, com isolamento de arquivos e de rede.

Os pontos de entrada de instrução maliciosa que importam para esta sessão são quatro. A skill de terceiros pode instruir o agente a chamar ferramentas ou a vazar dados, e a documentação das skills orienta usar apenas as que a própria equipe criou ou obteve da Anthropic. O servidor MCP de terceiros recebe o mesmo alerta, e o Claude Code encoraja escrever os próprios servidores ou usar os de provedores confiáveis. O conteúdo externo buscado pelo agente, como páginas e documentos, pode conter instruções de injeção de prompt. A skill que busca dados em URLs externas herda esse risco, porque o conteúdo buscado muda sem que a skill mude.

A documentação lista boas práticas para conteúdo não confiável: revisar os comandos antes da aprovação, evitar enviar conteúdo não confiável diretamente ao agente, verificar mudanças em arquivos críticos e usar máquinas virtuais para executar scripts e chamadas de ferramenta, em especial com serviços web externos. O mesmo texto reconhece que nenhum sistema é imune a todos os ataques.

## Permissões mínimas por construção

A restrição de permissões é declarada no arquivo do subagente e não depende da boa conduta do modelo.

| Mecanismo | Efeito | Cuidado |
|---|---|---|
| `tools` | Lista as únicas ferramentas permitidas | Se omitido, o subagente herda todas as disponíveis |
| `disallowedTools` | Nega ferramentas, aplicada antes de `tools` | Útil para herdar tudo menos escrita |
| `permissionMode` | Define o modo de permissão do subagente | É ignorado quando a conversa principal está em `bypassPermissions`, `acceptEdits` ou modo automático, porque o subagente herda esse modo |
| `maxTurns` | Limita os turnos do subagente | Limita também o consumo de tokens |
| Hook `PreToolUse` | Aplica regras condicionais, como bloquear comandos de escrita em SQL | Complementa a lista de ferramentas |
| `permissions.deny` | Bloqueia subagentes ou comandos específicos | A regra casa com o comando como escrito |

Um subagente de revisão, que apenas lê e comenta, declara `tools: Read, Grep, Glob`. Um subagente que precisa de rede ou de escrita declara, no arquivo, o motivo, e a equipe revisa essa declaração como revisa uma mudança de código.

Numa skill, o campo `allowed-tools` libera ferramentas sem pedir aprovação e deixa as demais disponíveis, e a restrição vem de `disallowed-tools`, como mostra a página [Front-matter de skills](front-matter-de-skills.md#liberar-nao-e-restringir). A documentação alerta que o Claude Code aplica o `allowed-tools` de uma skill de projeto até numa execução com `-p` em pasta nunca marcada como confiável, de modo que o `allowed-tools` de uma skill versionada no repositório entra na revisão como mudança de permissão.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** o alerta sobre `allowed-tools` consta de [Pre-approve tools for a skill](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill).
    **Codex CLI:** o sandbox e a aprovação são definidos na sessão que inicia o agente e herdados pelos subagentes, conforme [aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security). Na [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference), `shell_environment_policy.ignore_default_excludes` tem padrão `true`, que mantém no ambiente dos subprocessos as variáveis com KEY, SECRET ou TOKEN no nome, e o valor `false` aplica as exclusões automáticas de nomes de segredo, comportamento que consta da documentação e não teve execução observada nesta sessão.

## Credenciais do agente

O agente age em nome de alguma identidade, e a pergunta de projeto é qual. As regras abaixo reúnem a orientação do Microsoft Learn para PATs do Azure DevOps e a do GitHub para tokens de acesso pessoal, e a tabela marca o que é orientação das fontes e o que é conclusão deste material.

| Regra | Origem |
|---|---|
| Não usar a identidade integrada do Windows nem a senha de domínio da pessoa para o agente. O agente receberia tudo o que a pessoa pode fazer, sem limite de escopo | Conclusão deste material, a partir de a documentação afirmar que um PAT é uma senha alternativa que limita o acesso por escopos |
| Preferir identidade de aplicação (token do Microsoft Entra, identidade gerenciada ou service principal) quando a ferramenta aceita | [Microsoft Learn](../referencia/bibliografia.md#microsoft-use-personal-access-tokens-in-azure-devops-documentacao) |
| Quando a ferramenta não aceita identidade de aplicação, usar um PAT de escopo de organização, com os escopos mínimos e a vida mais curta possível | Microsoft Learn |
| No GitHub, preferir tokens de granularidade fina, restritos aos repositórios e às permissões necessárias | [GitHub Docs](../referencia/bibliografia.md#github-managing-your-personal-access-tokens-documentacao) |
| Usar um token diferente para cada ferramenta ou fluxo e não compartilhá-lo | Microsoft Learn |
| Definir sempre a expiração. No GitHub, o padrão do token de granularidade fina é de 30 dias | GitHub Docs |
| Não incluir dado pessoal nem parte do valor do token no nome do token | Microsoft Learn |

Um PAT identifica a pessoa que o criou e não concede mais permissões do que ela possui. A frase delimita o dano máximo e não o elimina: o PAT com escopo de leitura de código só lê código, e o PAT de escopo total faz tudo o que a pessoa faz. A Microsoft informa ainda que os PATs globais do Azure DevOps deixam de funcionar em 1º de dezembro de 2026 e que se deve usar PATs de escopo de organização ou autenticação do Microsoft Entra.

## Onde o token fica

O Microsoft Learn proíbe embutir PATs em URLs de remoto do Git, em `.git/config`, em código-fonte, em YAML de pipeline e em logs, e recomenda um cofre de segredos, como o Azure Key Vault, ou o gerenciador de credenciais da ferramenta, como o Git Credential Manager. O GitHub recomenda, para scripts, guardar o token como segredo do GitHub Actions ou do Codespaces. O Claude Code armazena as próprias chaves e tokens no Keychain do macOS quando disponível, em arquivo com modo `0600` no Linux e em arquivo que herda as permissões do perfil do usuário no Windows.

Por extensão destas regras, conclusão deste material e não afirmação das fontes, o valor do token também não aparece no texto de uma skill, no arquivo de instruções do projeto, no prompt de um subagente nem no artefato gerado, porque esses arquivos são versionados, lidos pelo modelo e compartilhados. O script da skill lê o token de uma variável de ambiente preenchida por um cofre, e o validador do artefato inclui uma verificação de padrões de segredo antes de o arquivo ser salvo.

## Ciclo de vida do token

O Microsoft Learn descreve o rodízio em seis passos, que valem para o token de um agente.

1. Criar o novo token, com escopo de organização, apenas os escopos necessários e vida curta.
2. Guardar o valor no cofre, sem colocá-lo em remoto Git, código, YAML ou logs.
3. Testar o token novo numa operação fora de produção.
4. Atualizar cada serviço e ferramenta que usa o token antigo.
5. Testar cada integração atualizada e verificar falhas de autenticação.
6. Revogar o token antigo.

Convém manter um inventário com o dono, a finalidade, os escopos, a validade e as integrações de cada token. A revogação deve ser imediata quando o token é exposto, e a Microsoft informa que o log de auditoria registra a criação, a expiração, a modificação e a revogação, mas não o uso, de modo que o log não indica se um token foi usado. O Azure DevOps ainda varre repositórios públicos do GitHub e revoga automaticamente os PATs vazados, salvo se a política do tenant desativar o recurso.

## Perguntas de revisão

| Pergunta | Resposta aceitável |
|---|---|
| Que identidade o agente usa? | Uma identidade de aplicação ou um token dedicado ao agente, nunca a conta pessoal integrada |
| Qual é o alcance máximo do token? | Escopos e repositórios listados, com o motivo de cada um |
| Quando o token expira e quem o renova? | Data definida e responsável nomeado |
| Onde o valor está guardado? | Cofre de segredos ou gerenciador de credenciais, nunca no repositório |
| O que o subagente pode fazer? | Lista `tools` explícita, com justificativa para escrita e rede |
| Quem revisou a skill de origem externa? | Pessoa nomeada, com todos os arquivos lidos |
| Como o token é revogado? | Procedimento escrito e testado, com o inventário atualizado |

**Próxima página:** [Exercícios](exercicios.md).
