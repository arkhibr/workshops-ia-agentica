# Compartilhamento governado

Esta página apresenta os quatro níveis em que uma skill ou um agente pode ser compartilhado no Claude Code, o que cada nível exige e quem o configura, e o ciclo de vida de um plugin publicado num marketplace, da publicação à retirada. A página preenche, na [ficha de governança](index.md#a-ficha-de-governanca), as linhas "Canal e versão" e "Revisão e retirada". A ficha de governança é a tabela de oito linhas que esta sessão usa para registrar o que precisa estar decidido antes de outra pessoa da equipe instalar uma skill ou um agente.

As afirmações sobre o Claude Code levam uma de três marcas. **Observado** indica comportamento executado em 03/11/2026 com o Claude Code 2.1.317 no macOS, **documentado** indica texto da documentação oficial lido sem execução e **não confirmado** indica item que a documentação lida não cobre ou que não foi executado.

## Quatro níveis de compartilhamento

A [documentação de skills do Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao) lista quatro locais de skill: pessoal, de projeto, de plugin e corporativo. Cada local corresponde a um nível de compartilhamento, com alcance, requisito e responsável diferentes, e o nível escolhido define a linha "Canal e versão" da ficha.

| Nível | Onde fica | Alcance | Quem configura | Como a versão chega ao colega |
|---|---|---|---|---|
| Pessoal | `~/.claude/skills/` na máquina da pessoa | Só a pessoa | O próprio usuário | Não chega, a cópia para outra máquina é manual |
| Repositório | `.claude/skills/` versionado no repositório, ou registro de marketplace em `.claude/settings.json` | Quem clona o repositório e confia na pasta | Quem tem permissão de commit no repositório | Pelo commit, a cada `git pull` |
| Marketplace | Pasta ou repositório com `.claude-plugin/marketplace.json` | Quem registra o marketplace e instala o plugin | Mantenedor do marketplace publica, cada usuário instala | Em fonte git ou remota, pela `version` do plugin (documentado). Em marketplace de pasta local, a `version` governa o aviso, o número exibido e o cache, e o conteúdo é lido da pasta (observado) |
| Organização | Configurações gerenciadas, e página Organization settings > Plugins & skills do claude.ai | Todas as máquinas e contas que recebem a política | **Administrador** da organização | Pela política, aplicada no início da sessão sem ação do usuário |

![Quatro colunas lado a lado, do menor para o maior alcance: pessoal, repositório, marketplace e organização. Cada coluna mostra onde a skill fica, quem configura e como a atualização chega ao colega. As três primeiras colunas são configuradas sem privilégio de administrador, e a quarta, com as configurações gerenciadas e a página Organization settings, é marcada como responsabilidade do administrador.](assets/niveis-de-compartilhamento.png)

Os três primeiros níveis ficam ao alcance de qualquer pessoa da equipe, e os exercícios desta sessão usam apenas eles. A documentação informa uma ordem de precedência quando a mesma skill existe em mais de um local: o escopo corporativo prevalece sobre o pessoal, e o pessoal prevalece sobre o de projeto, e as skills de plugin são invocadas com o prefixo `/plugin:skill`, que identifica o plugin de origem (documentado).

### Nível de repositório

A forma mais simples de compartilhar uma skill com a equipe é versioná-la em `.claude/skills/` no repositório, recomendação da própria documentação de skills. O repositório também pode registrar um marketplace e habilitar plugins para quem trabalha nele, com as chaves `extraKnownMarketplaces` e `enabledPlugins` no `.claude/settings.json`. A [página de gestão de plugins na organização](../referencia/bibliografia.md#anthropic-gerenciar-plugins-na-organizacao-documentacao-do-claude-code) informa que as entradas de `extraKnownMarketplaces` do repositório só se aplicam numa pasta em que a pessoa aceitou o diálogo de confiança, e que numa pasta não confiável o Claude Code as ignora sem mensagem (documentado).

O comando `claude plugin marketplace add <pasta> --scope project` grava esse registro no `.claude/settings.json` da pasta atual, e foi executado nesta sessão com resultado `declared in project settings` (observado). O caminho gravado em `extraKnownMarketplaces` é absoluto, com a forma `{"source": "directory", "path": "<caminho absoluto>"}`, e por isso o arquivo versionado carrega um caminho que existe apenas no computador de quem executou o comando (observado). Para um repositório compartilhado, a documentação de marketplaces descreve as fontes `github` e `git`, cuja configuração dispensa caminho local, e essas duas fontes ficaram sem teste nesta sessão (documentado e não confirmado em campo).

### Nível de organização

As configurações gerenciadas são aplicadas pelo administrador e o usuário não as pode sobrescrever. A documentação descreve três formas de entrega: as configurações gerenciadas pelo servidor, definidas no console de administração do claude.ai e que exigem papel Owner na organização, a política de MDM e o arquivo `managed-settings.json` no caminho de sistema de cada plataforma (documentado).

| Chave gerenciada | Efeito documentado |
|---|---|
| `strictKnownMarketplaces` | Lista de permissão das origens de marketplace, em que `[]` bloqueia todas as origens, inclusive o marketplace oficial |
| `blockedMarketplaces` | Lista de bloqueio das origens, conferida antes da lista de permissão |
| `disableSideloadFlags` | Rejeita `--plugin-dir` e opções semelhantes que carregam plugin de pasta local ou URL |
| `strictPluginOnlyCustomization` | Bloqueia skills, agentes, hooks e servidores MCP que não venham de plugin, de configuração gerenciada ou do próprio Claude Code |
| `extraKnownMarketplaces` e `enabledPlugins` | Registram o marketplace e instalam e habilitam os plugins em todas as máquinas, com precedência sobre os demais escopos |

A página Organization settings > Plugins & skills do console de administração do claude.ai liga plugins para as contas dos membros, e esses plugins chegam ao Claude Code como plugins sincronizados. A documentação registra que essa página não define nenhuma das chaves da tabela acima, de modo que o controle das origens de marketplace no Claude Code depende das configurações gerenciadas (documentado). As duas vias exigem papel de administrador, e nenhum exercício desta sessão depende delas.

## Plugin e marketplace

Um plugin é a unidade de distribuição do Claude Code, uma pasta com o manifesto `.claude-plugin/plugin.json` que agrupa skills, agentes, hooks e servidores MCP. Um marketplace é uma pasta ou um repositório com o arquivo `.claude-plugin/marketplace.json`, que a [documentação de marketplaces](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao) define com três campos obrigatórios: `name`, `owner` e a lista `plugins`. Cada entrada da lista exige `name` e `source`, e a fonte pode ser um caminho relativo dentro do marketplace, um repositório `github`, uma subpasta de repositório git, uma URL, um arquivo compactado, um pacote npm ou um comando (documentado).

O marketplace pode ficar no GitHub, em outro servidor git, numa URL que serve o `marketplace.json` ou numa pasta de sistema de arquivos compartilhado. O usuário o registra com `claude plugin marketplace add <origem>` e instala cada plugin com `claude plugin install <plugin>@<marketplace>`, e o comando `claude plugin validate <pasta>` confere a sintaxe e os campos obrigatórios antes da publicação (documentado e observado, v2.1.317).

O nome do marketplace é a chave do registro na máquina do usuário. Ao registrar de novo o mesmo nome com outra origem, a CLI substituiu a origem sem pedir confirmação e exibiu o aviso `Plugins already installed from it now update from the new source` (observado). A consequência para a governança é que o nome do marketplace da equipe precisa ser único e conhecido, porque um segundo registro com o mesmo nome redireciona as atualizações de todos os plugins já instalados a partir dele.

## Ciclo de vida do plugin

O ciclo de vida de um plugin compartilhado tem cinco operações: publicar, versionar, fixar, renomear e retirar. A linha "Canal e versão" da ficha registra as três primeiras, e a linha "Revisão e retirada" registra as duas últimas.

| Operação | Mecanismo | Marca |
|---|---|---|
| Publicar | Entrada nova em `plugins` no `marketplace.json`, conferida por `claude plugin validate` | Observado |
| Versionar | Campo `version` no `plugin.json`, com precedência sobre a `version` da entrada do marketplace, e acompanhamento dos commits quando o campo é omitido | Documentado |
| Fixar | Campos `ref` e `sha` na fonte git, que prendem o plugin a um ramo, etiqueta ou commit | Documentado |
| Renomear | Mapa `renames` no `marketplace.json`, do nome antigo para o novo | Documentado |
| Retirar | Mapa `renames` com o valor `null` para o nome retirado, e a opção `forceRemoveDeletedPlugins` para desinstalar | Documentado, parcialmente observado |

A documentação de hospedagem informa que uma versão nova só chega ao usuário quando a versão calculada do plugin muda, e que commits novos com a mesma `version` não chegam (documentado). Num marketplace registrado a partir de pasta local, o comportamento observado foi diferente em um ponto. A `version` governou o aviso de atualização, com a mensagem `updated from 1.0.0 to 1.0.1`, o número exibido por `claude plugin list` e `claude plugin details` e a cópia gravada no cache, enquanto o conteúdo carregado continuou a ser lido da própria pasta do marketplace, e a CLI informou que uma edição sem aumento de versão passa a valer no início da sessão seguinte ou depois de `/reload-plugins` (observado). A carga da edição numa sessão nova não foi executada (não confirmado). A documentação descreve esse caso como o de plugin carregado no lugar, que não é controlado pela `version`, e a entrega condicionada à versão numa fonte git remota não foi testada nesta sessão (não confirmado).

A documentação não prevê um estado de plugin obsoleto. A retirada é feita removendo a entrada de `plugins` e acrescentando `"renames": {"<nome>": null}`, e segundo a documentação o usuário passa a ver a mensagem `Removed from the "<marketplace>" marketplace` em `claude plugin list` e no comando `/plugin` de uma sessão interativa (documentado). Na execução feita pela linha de comando, sem abrir sessão interativa, a mensagem não apareceu (observado). Logo depois de `claude plugin marketplace update`, a primeira listagem ainda mostrou o plugin retirado como `enabled`, a segunda listagem já o mostrou como `disabled`, e só depois dela o comando `claude plugin update` do plugin retirado terminou com `Plugin "<plugin>" not found` (observado). A opção `forceRemoveDeletedPlugins` não produziu diferença visível pela linha de comando, e a desinstalação que a documentação descreve ocorre no início de cada sessão (não confirmado).

Duas observações completam o ciclo. O comando `claude plugin marketplace remove <nome>` desinstalou todos os plugins daquele marketplace, inclusive o que estava desabilitado, e a pasta do cache permaneceu no disco (observado). Um comando `claude plugin uninstall` executado depois da remoção do marketplace terminou com erro, porque os plugins já tinham sido desinstalados (observado).

## Avaliação antes da publicação

O Claude Code tem um comando de avaliação de plugins, `claude plugin eval`, descrito na [documentação de avaliação de plugins](../referencia/bibliografia.md#anthropic-avaliacao-de-plugins-no-claude-code-documentacao). Um caso de avaliação é uma pasta com `prompt.md`, `case.yaml` ou os dois, com ao menos um avaliador, e os avaliadores do tipo `regex`, `tool_used`, `tool_order` e `file_exists` conferem o resultado sem chamar o modelo (documentado). Por padrão, cada caso roda três vezes com o plugin e três vezes sem ele, o que soma seis execuções de agente, e cada execução consome o plano ou a fatura de API da conta autenticada (documentado).

O comando existe na versão 2.1.317 e nenhuma avaliação foi executada nesta sessão (não executado). Por inferência deste material, sem execução, os testes T01 a T03 da página [Controles e evidências](controles-e-evidencias.md) podem ser escritos como casos de avaliação, e a parte do T01 que exige a ausência de chamada a URL externa corresponde ao que um avaliador do tipo `tool_used` confere segundo a documentação.

## Revisão e retirada

A linha "Revisão e retirada" da ficha registra quando a ficha é revista e como a skill sai de circulação. O guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026) indica cinco gatilhos de revalidação dos controles: a troca do modelo, a troca da base de documentos usada na recuperação, a mudança de permissões, a mudança da skill e a mudança de finalidade. Cada revisão fica registrada na ficha com a data, o gatilho que a motivou e a versão do plugin vigente no momento da revisão.

A retirada precisa de um procedimento escrito antes de ser necessária. O procedimento registra quem decide a retirada, a entrada `renames` com `null` que a executa no marketplace, a revogação dos tokens usados pela skill, conforme a página [Segurança e credenciais](../sessao-08-skills-e-agentes/seguranca-e-credenciais.md#ciclo-de-vida-do-token) da Sessão 8, e a forma de avisar quem tinha a skill instalada, já que a mensagem de retirada só aparece para o usuário numa sessão interativa (documentado).

!!! note "Claude Code e Codex CLI"
    **Claude Code:** marketplace em `.claude-plugin/marketplace.json`, registrado com `claude plugin marketplace add` e controlado na organização pelas configurações gerenciadas, conforme a [documentação de marketplaces](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao).
    **Codex CLI:** a [documentação de plugins do Codex](../referencia/bibliografia.md#openai-codex-build-plugins-documentacao) descreve um marketplace de repositório em `$REPO_ROOT/.agents/plugins/marketplace.json` e um pessoal em `~/.agents/plugins/marketplace.json`, registrados com `codex plugin marketplace add`, que aceita GitHub, URL git ou pasta local. Cada entrada declara `policy.installation` com `AVAILABLE`, `INSTALLED_BY_DEFAULT` ou `NOT_AVAILABLE`, e a publicação de um plugin no workspace exige administrador. A página de skills do Codex cita a pasta `/etc/codex/skills` para skills administrativas da máquina. Esses itens constam da documentação consultada em 03/11/2026, sem execução nesta sessão.

!!! abstract "Linha da ficha"
    Canal e versão, e revisão e retirada:

    - Em que nível a skill é compartilhada (pessoal, repositório, marketplace ou organização), e quem configura esse nível?
    - Qual é a versão publicada, e como o colega recebe a atualização?
    - Que gatilho exige revisão da ficha, e qual é o procedimento escrito de retirada?

**Próxima página:** [Oficina — marketplace local governado](oficina-de-ferramentas.md).
