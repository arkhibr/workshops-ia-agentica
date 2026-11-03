# Oficina — marketplace local governado

Nesta oficina, duas skills da ACME, uma universidade fictícia, são publicadas como plugins num marketplace local do Claude Code e passam por todo o ciclo de um plugin compartilhado com colegas. Um plugin é uma pasta que empacota uma ou mais skills para instalação, e um marketplace é uma pasta com o catálogo dos plugins que os colegas podem instalar.

Cada plugin traz o arquivo `governanca.json`, a ficha de governança, que registra quem responde pela skill, que dados ela lê, quanto ela age sozinha, qual é o risco e que controles o reduzem. O portão é o script `portao.mjs`, que lê essa ficha e bloqueia a publicação quando ela está incompleta ou quando um controle depende só de um pedido escrito ao modelo.

![Ciclo de vida do plugin em seis etapas: baixar e validar no Experimento A, aprovar no portão no B, instalar e publicar a versão 1.0.1 no C, retirar pelo mapa renames no D e limpar no F, com o Experimento E derivado da instalação para registrar o marketplace num repositório com --scope project.](assets/ciclo-de-vida-do-plugin.png)

## Preparação

**Passo 1:** conferir as ferramentas e criar a pasta de trabalho, com os comandos abaixo, que são iguais nos três sistemas.

```text
claude --version
claude update
node --version
git --version
mkdir oficina-governanca
cd oficina-governanca
```

O comando `node --version` deve mostrar a versão 20 ou superior do Node, e os demais devem responder com um número de versão.

## Experimento A: baixar e validar o marketplace

Neste experimento, o marketplace é colocado na pasta de trabalho e o Claude Code confere se o catálogo está bem formado.

**Passo 1:** baixar o arquivo [marketplace-governado.zip](assets/marketplace-governado.zip) para a pasta `oficina-governanca`.

**Passo 2:** extrair o arquivo e listar os plugins.

=== "macOS/Linux"
    ```bash
    unzip marketplace-governado.zip
    ls ./marketplace-acme/plugins
    ```

=== "Windows (PowerShell)"
    ```powershell
    Expand-Archive marketplace-governado.zip -DestinationPath .
    Get-ChildItem ./marketplace-acme/plugins
    ```

A listagem deve mostrar duas pastas, `identificando-tarefas-e-riscos`, com uma skill que extrai tarefas e riscos de transcrições de reuniões, e `revisando-pull-requests`, com uma skill que revisa pull requests contra os padrões de arquitetura da ACME. A pasta de trabalho fica com a estrutura abaixo.

```text
oficina-governanca/
├── portao.mjs, package.json, README.md, test/portao.test.mjs
└── marketplace-acme/
    ├── .claude-plugin/marketplace.json
    └── plugins/
        ├── identificando-tarefas-e-riscos/
        │   ├── .claude-plugin/plugin.json
        │   ├── governanca.json
        │   └── skills/identificando-tarefas-e-riscos/SKILL.md
        └── revisando-pull-requests/
            ├── .claude-plugin/plugin.json
            ├── governanca.json
            └── skills/revisando-pull-requests/SKILL.md
```

**Passo 3:** validar o catálogo com a linha de comando do Claude Code.

```text
claude plugin validate ./marketplace-acme
```

A saída deve começar com `Validating marketplace manifest:` e terminar com `✔ Validation passed`. Esse comando confere a estrutura do catálogo e dos plugins e ignora o arquivo `governanca.json`, e por isso a ficha passa pelo portão no Experimento B.

## Experimento B: aprovar no portão

Neste experimento, o portão reprova a ficha do plugin de revisão e aprova a mesma ficha depois de uma correção.

**Passo 1:** abrir a ficha do plugin de revisão num editor de texto e localizar o objeto `preventivo`, dentro da lista `riscos`.

**Arquivo:** `marketplace-acme/plugins/revisando-pull-requests/governanca.json`

```json
{
  "dono": "Arquitetura de Software da ACME",
  "finalidade": "Revisar pull requests contra os padrões de arquitetura da ACME",
  "alternativaSemIA": "Revisão manual feita pela pessoa responsável pela arquitetura",
  "dados": ["interno"],
  "ferramentas": ["Read", "Bash"],
  "autonomia": "sugere",
  "faixa": "moderada",
  "fatorDecisivo": "O código revisado é interno e o parecer é apenas uma sugestão",
  "premissas": [
    "Os critérios de aprovação ainda não foram definidos",
    "A revisão usa a credencial pessoal de quem a executa"
  ],
  "riscos": [
    {
      "evento": "A credencial pessoal ampla, usada por conveniência, permite ao agente alterar repositórios além do pull request revisado",
      "consequencia": "Uma alteração indevida chega a um repositório sem que ninguém a tenha solicitado",
      "preventivo": {
        "tipo": "instrucao",
        "descricao": "Pedir ao modelo que use a credencial somente para ler o pull request"
      },
      "detectivo": "Auditoria mensal dos acessos feitos com a credencial",
      "evidencia": "Relatório de auditoria dos acessos"
    }
  ],
  "gate": { "aprovador": "", "aprovadoEm": "" },
  "revisao": {
    "gatilhos": ["Definição dos critérios de aprovação", "Troca de credencial"],
    "retirada": "Revogar a credencial e remover o plugin do marketplace"
  }
}
```

A skill de revisão usa a credencial pessoal de quem a executa, que pode alterar qualquer repositório da pessoa, mais do que a revisão precisa. O controle preventivo é a medida que deveria impedir esse problema antes que ele ocorra, e nesta ficha ele é do tipo `instrucao`, um pedido escrito ao modelo que o próprio modelo pode deixar de cumprir.

**Passo 2:** rodar o portão.

```text
node portao.mjs ./marketplace-acme
```

A saída deve aprovar o primeiro plugin e reprovar o de revisão, com o motivo na linha de baixo.

```text
identificando-tarefas-e-riscos: aprovado
revisando-pull-requests: reprovado
  - riscos[0]: controle preventivo depende só de instrução ao modelo
```

![Caminho da ficha à instalação: o arquivo governanca.json entra no script portao.mjs, que reprova com código 1 diante de campo vazio, faixa incompatível com dado sensível ou autonomia executa, faixa alta sem aprovador ou controle preventivo do tipo instrucao, e sai com código 2 quando o catálogo é ilegível. Com código 0, o portão chama claude plugin validate e o colega registra o marketplace e instala o plugin.](assets/caminho-do-portao.png)

**Passo 3:** no mesmo arquivo, substituir o objeto `preventivo` pelo trecho abaixo, que troca o pedido ao modelo por um token próprio do agente com permissão só de leitura, uma restrição que o modelo não consegue alterar.

```json
      "preventivo": {
        "tipo": "permissao",
        "descricao": "Token próprio do agente, somente de leitura e restrito ao repositório do pull request revisado"
      },
```

**Passo 4:** na lista `premissas` do mesmo arquivo, trocar `"A revisão usa a credencial pessoal de quem a executa"` por `"O token do agente tem só permissão de leitura no repositório revisado"` e salvar o arquivo.

**Passo 5:** rodar o portão de novo com `node portao.mjs ./marketplace-acme`. Os dois plugins devem passar, e o portão chama em seguida a validação do Claude Code.

```text
identificando-tarefas-e-riscos: aprovado
revisando-pull-requests: aprovado
Validating marketplace manifest: <caminho absoluto>/marketplace-acme/.claude-plugin/marketplace.json

✔ Validation passed
```

## Experimento C: instalar como colega e publicar a versão 1.0.1

Neste experimento, os dois plugins são instalados como um colega os instalaria, e uma correção é publicada com um número de versão novo.

**Passo 1:** registrar o marketplace, instalar os dois plugins e listar o que ficou instalado.

```text
claude plugin marketplace add ./marketplace-acme
claude plugin install identificando-tarefas-e-riscos@marketplace-acme
claude plugin install revisando-pull-requests@marketplace-acme
claude plugin list
```

O registro deve responder `✔ Successfully added marketplace: marketplace-acme (declared in user settings)`, cada instalação deve terminar com `(scope: user)`, e a lista deve mostrar os dois plugins com `Version: 1.0.0` e `Status: ✔ enabled`. A lista pode trazer também outros plugins que já estavam instalados na máquina.

**Passo 2:** abrir o arquivo `marketplace-acme/plugins/identificando-tarefas-e-riscos/skills/identificando-tarefas-e-riscos/SKILL.md`, acrescentar ao fim dele a linha abaixo e salvar.

```text
Ordene as tarefas pelo prazo, com as tarefas sem prazo no fim da lista.
```

**Passo 3:** abrir o arquivo `marketplace-acme/plugins/identificando-tarefas-e-riscos/.claude-plugin/plugin.json`, trocar `"version": "1.0.0"` por `"version": "1.0.1"` e salvar.

**Passo 4:** passar a correção pelo portão, atualizar o catálogo e atualizar o plugin.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace update marketplace-acme
claude plugin update identificando-tarefas-e-riscos@marketplace-acme
claude plugin details identificando-tarefas-e-riscos
```

O `update` deve responder `✔ Plugin "identificando-tarefas-e-riscos" updated from 1.0.0 to 1.0.1 for scope user. Restart to apply changes.`, e o `details` deve mostrar a versão 1.0.1. Sem a troca de versão do Passo 3, o `update` responde `nothing to update`, e por isso cada correção publicada recebe um número de versão novo.

## Experimento D: retirar o plugin de revisão

Neste experimento, o plugin de revisão sai do catálogo, e a máquina de quem já o tinha instalado mostra o efeito da retirada.

**Passo 1:** abrir o arquivo `marketplace-acme/.claude-plugin/marketplace.json`, apagar da lista `plugins` a entrada de `revisando-pull-requests` e acrescentar o trecho abaixo depois do colchete que fecha a lista, separado dele por vírgula. O valor `null` indica que o plugin saiu do catálogo sem um substituto.

```json
  "renames": {
    "revisando-pull-requests": null
  }
```

**Passo 2:** passar a retirada pelo portão e atualizar o catálogo.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace update marketplace-acme
```

O portão deve aprovar o único plugin que restou no catálogo, `identificando-tarefas-e-riscos`.

**Passo 3:** listar os plugins duas vezes seguidas e tentar atualizar o plugin retirado.

```text
claude plugin list
claude plugin list
claude plugin update revisando-pull-requests@marketplace-acme
```

A primeira lista ainda mostra `revisando-pull-requests` com `Status: ✔ enabled`, a segunda mostra `Status: ✘ disabled`, e o `update` termina com a mensagem `Plugin "revisando-pull-requests" not found`. Nenhuma das saídas avisa que o plugin foi retirado, e por isso o procedimento de retirada da ficha inclui revogar a credencial da skill e avisar diretamente cada pessoa que tinha o plugin instalado.

## Experimento E: registrar o marketplace num repositório

Neste experimento, o marketplace é registrado nas configurações de um repositório git, e o arquivo versionado mostra o que o registro grava.

**Passo 1:** criar um repositório vazio dentro de `oficina-governanca`, registrar o marketplace no escopo do projeto e instalar um plugin nesse escopo.

```text
mkdir repositorio-acme
cd repositorio-acme
git init
claude plugin marketplace add ../marketplace-acme --scope project
claude plugin install identificando-tarefas-e-riscos@marketplace-acme --scope project
git status
```

O registro deve responder `✔ Marketplace 'marketplace-acme' already on disk — declared in project settings`, a instalação deve terminar com `(scope: project)`, e o `git status` deve mostrar a pasta nova `.claude/`.

**Passo 2:** abrir o arquivo `.claude/settings.json` num editor de texto. O arquivo traz as chaves `extraKnownMarketplaces` e `enabledPlugins`, e o valor gravado em `extraKnownMarketplaces` é o caminho absoluto da pasta do marketplace no computador de quem executou o comando. Esse caminho não existe na máquina de um colega, e por isso um repositório compartilhado precisa apontar para um marketplace hospedado num servidor git.

## Experimento F: limpar

Neste experimento, o marketplace e os plugins são removidos da configuração do Claude Code, e a pasta de trabalho é apagada.

**Passo 1:** ainda dentro de `repositorio-acme`, remover o marketplace e conferir a lista de plugins.

```text
claude plugin marketplace remove marketplace-acme
claude plugin list
```

A remoção deve responder `✔ Successfully removed marketplace: marketplace-acme` e `Also uninstalled` com os plugins instalados a partir dele, inclusive o desabilitado, e a lista deixa de mostrá-los. Um `claude plugin uninstall` depois disso termina com erro, porque os plugins já foram desinstalados.

**Passo 2:** sair das duas pastas e apagar a pasta de trabalho.

=== "macOS/Linux"
    ```bash
    cd ../..
    rm -rf ./oficina-governanca
    ```

=== "Windows (PowerShell)"
    ```powershell
    cd ../..
    Remove-Item -Recurse -Force ./oficina-governanca
    ```

**Próxima página:** [Experimentos complementares](experimentos-complementares.md).
