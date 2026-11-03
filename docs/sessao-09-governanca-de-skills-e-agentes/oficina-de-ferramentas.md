# Oficina — marketplace local governado

Esta oficina instala duas skills da ACME, a universidade fictícia usada na Sessão 8 e nesta sessão, como plugins de um marketplace local do Claude Code e percorre o ciclo de vida de um plugin compartilhado, da aprovação no portão até a limpeza. Conforme a página [Compartilhamento governado](compartilhamento-governado.md), um plugin é uma pasta com o manifesto `.claude-plugin/plugin.json`, e um marketplace é uma pasta com o catálogo `.claude-plugin/marketplace.json`.

Cada plugin traz a ficha de governança no arquivo `governanca.json`, e o script de portão `portao.mjs` reprova a publicação quando a ficha está incompleta ou declara um controle que depende só de instrução ao modelo.

![Ciclo de vida do plugin em seis etapas: baixar e validar no Experimento A, aprovar no portão no B, instalar e publicar a versão 1.0.1 no C, retirar pelo mapa renames no D e limpar no F, com o Experimento E derivado da instalação para registrar o marketplace num repositório com --scope project.](assets/ciclo-de-vida-do-plugin.png)

## Preparação

A oficina exige o Claude Code, o Node.js 20 ou superior e o git, e os comandos abaixo, iguais nos três sistemas, conferem as versões e criam a pasta de trabalho.

```text
claude --version
claude update
node --version
git --version
mkdir oficina-governanca
cd oficina-governanca
```

Os experimentos registram o marketplace na configuração do usuário do Claude Code, o Experimento F desfaz o registro, e a lista de `claude plugin list` pode trazer outros plugins já instalados na máquina.

## Experimento A: baixar e validar o marketplace

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

A listagem mostra as pastas `identificando-tarefas-e-riscos` e `revisando-pull-requests`, e a pasta de trabalho fica com a estrutura abaixo.

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

O primeiro plugin é a skill `identificando-tarefas-e-riscos` da Sessão 8, na versão 1.0.0 e com ficha completa, e o segundo é uma skill fictícia de revisão que carrega o incidente B de [Riscos de agentes](riscos-de-agentes.md#tres-incidentes), permissão maior que a finalidade.

**Passo 3:** validar o catálogo com a CLI do Claude Code.

```text
claude plugin validate ./marketplace-acme
```

A saída traz `Validating marketplace manifest:` com o caminho absoluto do catálogo e termina com `✔ Validation passed` e código 0. O comando ignora `governanca.json`, e por isso a ficha precisa de um portão próprio.

## Experimento B: aprovar no portão

A ficha do segundo plugin declara como controle preventivo um pedido ao modelo, do tipo `instrucao`.

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

O portão reprova a ficha com campo obrigatório vazio, a faixa abaixo da alta com dado sensível ou autonomia `executa`, a faixa alta sem aprovador e o controle preventivo do tipo `instrucao`. Quando nenhum plugin reprova, ele executa `claude plugin validate`, e o código de saída é 0 na aprovação, 1 na reprovação e 2 quando o catálogo é ilegível ou o `claude` está ausente.

![Caminho da ficha à instalação: o arquivo governanca.json entra no script portao.mjs, que reprova com código 1 diante de campo vazio, faixa incompatível com dado sensível ou autonomia executa, faixa alta sem aprovador ou controle preventivo do tipo instrucao, e sai com código 2 quando o catálogo é ilegível. Com código 0, o portão chama claude plugin validate e o colega registra o marketplace e instala o plugin.](assets/caminho-do-portao.png)

**Passo 1:** rodar o portão.

```text
node portao.mjs ./marketplace-acme
```

A saída mostra a reprovação do segundo plugin, e o código de saída é 1.

```text
identificando-tarefas-e-riscos: aprovado
revisando-pull-requests: reprovado
  - riscos[0]: controle preventivo depende só de instrução ao modelo
```

A reprovação aplica o critério do [exercício 5](exercicios.md#5-controle-preventivo-e-evidencia). A faixa `moderada` dessa ficha também é questionável, porque a resposta esperada do [exercício 3](exercicios.md#3-faixa-e-fator-decisivo) é a faixa alta enquanto a credencial pessoal ampla for usada, e o portão deixa passar a divergência porque `governanca.json` não tem campo para a permissão da credencial.

**Passo 2:** corrigir a ficha. No arquivo acima, substitua o objeto `preventivo` pelo trecho abaixo e troque a premissa `"A revisão usa a credencial pessoal de quem a executa"` por `"O token do agente tem só permissão de leitura no repositório revisado"`.

```json
      "preventivo": {
        "tipo": "permissao",
        "descricao": "Token próprio do agente, somente de leitura e restrito ao repositório do pull request revisado"
      },
```

**Passo 3:** rodar o portão de novo com `node portao.mjs ./marketplace-acme`. Os dois plugins passam e o código de saída é 0.

```text
identificando-tarefas-e-riscos: aprovado
revisando-pull-requests: aprovado
Validating marketplace manifest: <caminho absoluto>/marketplace-acme/.claude-plugin/marketplace.json

✔ Validation passed
```

O portão confere só o que a ficha declara, e a prova de que o token é somente de leitura é um teste em que a API rejeita uma escrita, como o [T03](controles-e-evidencias.md#testes-de-aceite-t01-a-t07), guardado na linha "Evidência e gate" da ficha.

## Experimento C: instalar como colega e publicar a versão 1.0.1

**Passo 1:** registrar o marketplace e instalar os dois plugins.

```text
claude plugin marketplace add ./marketplace-acme
claude plugin install identificando-tarefas-e-riscos@marketplace-acme
claude plugin install revisando-pull-requests@marketplace-acme
claude plugin list
```

O registro responde `✔ Successfully added marketplace: marketplace-acme (declared in user settings)`, cada instalação termina com `(scope: user)`, e a lista mostra `Version: 1.0.0`, `Read from:` com a pasta do plugin e `Status: ✔ enabled`.

**Passo 2:** publicar uma correção. Acrescente ao fim do `SKILL.md` de `identificando-tarefas-e-riscos` a linha `Ordene as tarefas pelo prazo, com as tarefas sem prazo no fim da lista.` e troque `"version": "1.0.0"` por `"version": "1.0.1"` no `plugin.json` do mesmo plugin.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace update marketplace-acme
claude plugin update identificando-tarefas-e-riscos@marketplace-acme
claude plugin details identificando-tarefas-e-riscos
```

O `update` responde `✔ Plugin "identificando-tarefas-e-riscos" updated from 1.0.0 to 1.0.1 for scope user. Restart to apply changes.`, e `details` passa a mostrar a versão 1.0.1.

Num marketplace de pasta local, a versão controla o aviso de atualização e o número exibido, além da cópia gravada no cache, e o conteúdo carregado pela skill vem da própria pasta do marketplace, indicada na linha `Read from:` de `claude plugin list`. Uma edição sem aumento de versão produz `nothing to update`. Numa fonte git remota, a documentação indica que a versão decide o que o colega recebe.

## Experimento D: retirar o plugin de revisão

**Passo 1:** no `marketplace-acme/.claude-plugin/marketplace.json`, remova a entrada de `revisando-pull-requests` da lista `plugins` e acrescente o mapa abaixo depois do fechamento da lista, separado dela por vírgula.

```json
  "renames": {
    "revisando-pull-requests": null
  }
```

**Passo 2:** passar a retirada pelo portão, atualizar o catálogo e tentar atualizar o plugin retirado.

```text
node portao.mjs ./marketplace-acme
claude plugin marketplace update marketplace-acme
claude plugin list
claude plugin list
claude plugin update revisando-pull-requests@marketplace-acme
```

O portão aprova o plugin restante. A primeira lista ainda mostra `revisando-pull-requests` com `Status: ✔ enabled`, já sem `Read from:`, a segunda mostra `Status: ✘ disabled`, e o `update` termina com código 1 e a mensagem `Plugin "revisando-pull-requests" not found`. A mensagem `Removed from the "marketplace-acme" marketplace`, que a documentação descreve, não aparece na linha de comando. Como o colega fica sem aviso explícito, o campo `revisao.retirada` da ficha inclui a revogação da credencial e o aviso direto a quem tinha o plugin instalado.

## Experimento E: registrar o marketplace num repositório

Os comandos criam um repositório vazio dentro de `oficina-governanca` e registram o marketplace no escopo do projeto.

```text
mkdir repositorio-acme
cd repositorio-acme
git init
claude plugin marketplace add ../marketplace-acme --scope project
claude plugin install identificando-tarefas-e-riscos@marketplace-acme --scope project
git status
```

Com o marketplace já registrado no escopo do usuário, o registro responde `✔ Marketplace 'marketplace-acme' already on disk — declared in project settings`, e a instalação responde com `(scope: project)`. O `git status` mostra `.claude/` como pasta nova, com `.claude/settings.json` contendo `extraKnownMarketplaces` e `enabledPlugins`.

O valor gravado em `extraKnownMarketplaces` é o caminho absoluto da pasta no computador de quem executou o comando, e esse caminho entra no arquivo versionado do repositório. Para repositório compartilhado, a documentação descreve as fontes `github` e `git`, e a página [Experimentos complementares](experimentos-complementares.md) trata dessa hospedagem.

## Experimento F: limpar

**Passo 1:** remover o marketplace, dentro de `repositorio-acme` para quem fez o Experimento E, ou em `oficina-governanca` para quem não fez.

```text
claude plugin marketplace remove marketplace-acme
claude plugin list
```

A remoção responde `✔ Successfully removed marketplace: marketplace-acme` e `Also uninstalled` com os plugins instalados a partir dele, inclusive o desabilitado, e por isso um `claude plugin uninstall` depois dela termina com erro.

**Passo 2:** sair da pasta de trabalho e apagá-la. Quem está em `repositorio-acme` executa `cd ..` uma vez antes dos comandos abaixo.

=== "macOS/Linux"
    ```bash
    cd ..
    rm -rf ./oficina-governanca
    ```

=== "Windows (PowerShell)"
    ```powershell
    cd ..
    Remove-Item -Recurse -Force ./oficina-governanca
    ```

A pasta do cache do marketplace, dentro da configuração do Claude Code do usuário, permaneceu no disco depois da remoção, sem registrar o marketplace nem habilitar plugin.

**Próxima página:** [Experimentos complementares](experimentos-complementares.md).
