# Experimentos complementares

Estas três práticas partem do marketplace `marketplace-acme`, que vem no arquivo [marketplace-governado.zip](assets/marketplace-governado.zip) com duas skills da ACME, uma universidade fictícia, empacotadas como plugins. Cada plugin traz o arquivo `governanca.json`, a ficha de governança com quem responde pela skill, que dados ela lê, quanto ela age sozinha, qual é o risco e que controles o reduzem, e o script `portao.mjs` reprova a publicação quando essa ficha está incompleta ou fraca.

Nenhuma das práticas publica dado interno, e o trabalho com o protótipo real da equipe fica num repositório interno dela.

## Empacotar o protótipo real da equipe

Nesta prática, o protótipo em que a equipe trabalha entra como terceiro plugin de uma cópia do marketplace, num repositório interno.

![Seis etapas do protótipo ao marketplace da equipe: terceiro plugin numa cópia do marketplace no repositório interno, ficha em governanca.json, portão e instalação com os comandos da oficina, troca com outra equipe, hospedagem num repositório git da equipe, registrada por owner/repo ou por URL git, e portão na esteira, como proposta a configurar pela equipe.](assets/do-prototipo-ao-marketplace.png)

**Passo 1:** extrair o zip no repositório interno da equipe e criar, dentro de `marketplace-acme/plugins/`, uma pasta com o nome do protótipo, em letras minúsculas e com hífens.

**Passo 2:** copiar para a pasta nova o arquivo `.claude-plugin/plugin.json` do plugin `identificando-tarefas-e-riscos` e trocar nele os valores de `name`, `version` e `description` pelos do protótipo.

**Passo 3:** colocar cada skill do protótipo em `skills/<nome-da-skill>/SKILL.md`, dentro da pasta do plugin.

**Passo 4:** copiar o `governanca.json` do mesmo plugin como modelo e preencher os campos com os dados do protótipo. A ficha descreve cada credencial pelo tipo, pelo dono e pelo escopo, sem conter o valor de nenhuma delas, e uma faixa `alta` exige o nome do aprovador e a data da aprovação em `gate`, regra que o portão confere.

**Passo 5:** acrescentar a entrada do protótipo à lista `plugins` de `marketplace-acme/.claude-plugin/marketplace.json`, com `name`, `description` e `source` no formato `./plugins/<nome-do-prototipo>`.

**Passo 6:** rodar o portão, registrar o marketplace e instalar o protótipo.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace add ./marketplace-acme
claude plugin install <nome-do-prototipo>@marketplace-acme
claude plugin details <nome-do-prototipo>
```

O portão deve responder `<nome-do-prototipo>: aprovado`, e o `details` deve mostrar a versão gravada no `plugin.json`.

**Passo 7:** entregar a cópia do marketplace a outra equipe, que instala o protótipo como colega e revisa a ficha. A revisão confere se a faixa de risco foi decidida pelo fator mais grave, se cada risco está escrito no formato "se este evento acontecer, esta consequência ocorre" e se o controle preventivo roda fora do modelo, como uma permissão ou um hook, e cada achado entra na ficha com o nome de quem vai corrigi-lo, como uma premissa sem responsável ou um controle que ainda depende de pedido ao modelo.

## Hospedar o marketplace num repositório git da equipe

Nesta prática, o marketplace sai da pasta local e passa a ficar num servidor git, para que os colegas o registrem sem depender de um caminho do computador de outra pessoa.

**Passo 1:** criar um repositório git interno, colocar nele o conteúdo da pasta `marketplace-acme` e enviar o commit para o servidor da equipe.

**Passo 2:** registrar o marketplace a partir do servidor. A forma `owner/repo` vale para um repositório no GitHub, e a URL completa vale para outro servidor git.

```text
claude plugin marketplace add <owner>/<repo>
claude plugin marketplace add https://<servidor>/<caminho-do-repositorio>.git
```

**Passo 3:** publicar uma correção com versão nova no `plugin.json` e conferir, na máquina de um colega, se `claude plugin update` entrega a versão nova. Numa fonte git, o colega recebe a cópia nova quando a `version` do plugin muda, e um commit com a mesma `version` não chega até ele.

**Passo 4:** para prender o plugin a uma versão, preencher na fonte do plugin o campo `ref`, com um ramo ou uma etiqueta, ou o campo `sha`, com um commit.

O portão também pode rodar na esteira do repositório antes de cada merge, porque termina com código 1 quando algum plugin reprova e com código 2 quando o catálogo é ilegível.

## Avaliar o plugin antes da publicação

O comando `claude plugin eval` roda casos de avaliação contra um plugin. Cada execução chama o modelo com a credencial de quem a roda e conta no uso do plano ou na fatura de API, e por isso esta seção descreve o comando sem passos para executar.

Segundo a documentação do Claude Code, um caso de avaliação fica numa pasta dentro do plugin, com `prompt.md`, `case.yaml` ou os dois, e precisa de ao menos um avaliador. Os avaliadores do tipo `regex`, `tool_used`, `tool_order` e `file_exists` conferem o resultado sem chamar o modelo, e por padrão cada caso roda três vezes com o plugin e três vezes sem ele, o que soma seis execuções de agente. O relatório em HTML é gravado localmente, e a opção `--no-publish` evita que ele seja publicado como artefato privado no claude.ai.

Um teste que confere se o agente deixou de chamar uma URL externa, por exemplo, corresponde ao que um avaliador do tipo `tool_used` verifica, e a decisão de rodar a avaliação cabe à equipe, numa conta autorizada para esse uso.

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
