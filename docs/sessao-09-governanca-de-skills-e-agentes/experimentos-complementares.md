# Experimentos complementares

Estas três práticas são opcionais e ficam para depois da sessão. Elas partem do marketplace local da [oficina](oficina-de-ferramentas.md), que empacota duas skills da ACME, a universidade fictícia usada na Sessão 8 e nesta sessão, com a ficha de governança gravada em `governanca.json` dentro de cada plugin e conferida pelo script de portão `portao.mjs`.

As afirmações sobre o Claude Code seguem as marcas da sessão: **observado** indica comportamento executado em 03/11/2026 com o Claude Code 2.1.317 no macOS, **documentado** indica texto da documentação oficial lido sem execução e **não confirmado** indica item que a documentação lida não cobre ou que não foi executado. Nenhuma das práticas publica dado interno, e o trabalho com o protótipo real do grupo fica no ambiente interno da equipe.

## Empacotar o protótipo real do grupo

O grupo acrescenta o protótipo em que trabalha como terceiro plugin de uma cópia do marketplace da oficina. A cópia fica num repositório interno da equipe, e nem a ficha nem os arquivos do protótipo entram no repositório público do workshop ou neste site.

**Passo 1:** copiar a pasta `marketplace-acme` da oficina para o repositório interno e criar dentro de `plugins/` uma pasta com o nome do protótipo, em letras minúsculas e com hífens. A pasta recebe o manifesto `.claude-plugin/plugin.json`, com `name`, `version` e `description`, e cada skill do protótipo em `skills/<nome-da-skill>/SKILL.md`, a mesma estrutura dos dois plugins da oficina.

**Passo 2:** gravar em `governanca.json` a ficha preenchida nos exercícios 1 a 5, com os mesmos campos dos plugins da oficina. A ficha descreve a credencial pelo tipo, pelo dono e pelo escopo, sem conter o valor de nenhuma credencial, e uma faixa alta exige o nome do aprovador e a data da aprovação em `gate`, regra que o portão confere.

**Passo 3:** acrescentar a entrada do protótipo à lista `plugins` do `marketplace.json`, com `name`, `source` relativo em barras normais e `description`, e rodar o portão e a instalação da oficina. Os comandos são os mesmos dos Experimentos B e C, observados na versão 2.1.317, com o nome do protótipo no lugar de `identificando-tarefas-e-riscos`.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace add ./marketplace-acme
claude plugin install <nome-do-prototipo>@marketplace-acme
claude plugin details <nome-do-prototipo>
```

**Passo 4:** trocar o marketplace com outro grupo, que instala o protótipo como colega e revisa a ficha com os critérios dos exercícios 3 a 5. O resultado esperado é ao menos um achado registrado na ficha, como uma premissa sem responsável pela verificação ou um controle preventivo que ainda depende de instrução ao modelo.

A página [Compartilhamento governado](compartilhamento-governado.md) informa que um plugin também pode agrupar agentes, hooks e servidores MCP, e a disposição desses componentes dentro do plugin consta da [documentação de marketplaces](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao) sem execução nesta sessão (documentado).

## Hospedar o marketplace num repositório git da equipe

Esta prática descreve a forma que a documentação indica para um marketplace compartilhado entre máquinas, e nenhum dos seus passos foi executado nesta sessão. O Experimento E da oficina mostrou que o registro de uma pasta local grava um caminho absoluto em `.claude/settings.json`, que só funciona no computador de quem executou o comando (observado).

A documentação de marketplaces descreve quatro formas de hospedagem: um repositório no GitHub, outro servidor git identificado pela URL completa, uma URL que serve o `marketplace.json` e uma pasta de sistema de arquivos compartilhado (documentado). Na versão 2.1.317, a mensagem de erro de `claude plugin marketplace add` para uma origem recusada lista os formatos aceitos como `owner/repo`, `https://...` e `./path` (observado).

| Decisão | Comportamento descrito | Marca |
|---|---|---|
| Entrega da correção | Numa fonte git, o colega recebe a cópia nova quando a versão calculada do plugin muda, e commits novos com a mesma `version` não chegam | Documentado |
| Fixação da versão | Os campos `ref` e `sha` da fonte prendem o plugin a um ramo, a uma etiqueta ou a um commit | Documentado |
| Registro no repositório | `extraKnownMarketplaces` em `.claude/settings.json` com fonte `github` ou `git` dispensa caminho local e vale para quem confia na pasta | Documentado, sem execução nesta sessão |
| Acesso a servidor privado | A autenticação num servidor git privado da equipe, como GitHub ou Azure DevOps, ficou sem verificação nesta sessão | Não confirmado |

Por inferência deste material, sem execução, o portão da oficina pode rodar na esteira do repositório do marketplace antes de cada merge, porque ele termina com código 1 quando algum plugin reprova e com código 2 quando o catálogo é ilegível. Com essa esteira, a linha "Evidência e gate" da ficha passa a apontar para o registro da execução do portão e para o nome de quem aprovou o pull request.

!!! note "Claude Code e Codex CLI"
    **Claude Code:** hospedagem em GitHub, servidor git, URL ou pasta compartilhada, conforme a [documentação de marketplaces](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao).
    **Codex CLI:** a [documentação de plugins do Codex](../referencia/bibliografia.md#openai-codex-build-plugins-documentacao) informa que `codex plugin marketplace add` aceita GitHub, URL git ou pasta local, e que a publicação de um plugin no workspace exige administrador. Esses itens constam da documentação consultada em 03/11/2026, sem execução nesta sessão.

## Avaliar o plugin antes da publicação

O Claude Code 2.1.317 tem o comando `claude plugin eval`, que aparece na ajuda de `claude plugin` (observado) e roda casos de avaliação contra um plugin, segundo a [documentação de avaliação de plugins](../referencia/bibliografia.md#anthropic-avaliacao-de-plugins-no-claude-code-documentacao). Nenhuma avaliação foi executada nesta sessão, porque cada execução chama o modelo com a credencial de quem a roda e conta no uso do plano ou na fatura de API, e por isso esta seção descreve o comando sem passos para executar.

Segundo a documentação, um caso de avaliação fica numa pasta dentro do plugin, com `prompt.md`, `case.yaml` ou os dois, e precisa de ao menos um avaliador. Os avaliadores do tipo `regex`, `tool_used`, `tool_order` e `file_exists` conferem o resultado sem chamar o modelo, e por padrão cada caso roda três vezes com o plugin e três vezes sem ele, o que soma seis execuções de agente (documentado). O relatório em HTML é gravado localmente e, quando a conta permite, também é publicado como artefato privado no claude.ai, com a opção `--no-publish` para evitar a publicação (documentado).

Por inferência deste material, sem execução, os testes T01 a T03 da página [Controles e evidências](controles-e-evidencias.md) podem ser escritos como casos de avaliação do plugin. A parte do T01 que exige a ausência de chamada a URL externa corresponde ao que um avaliador do tipo `tool_used` confere segundo a documentação, e a decisão de rodar a avaliação cabe à equipe, numa conta autorizada para esse uso.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
