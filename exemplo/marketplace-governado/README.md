# Marketplace governado da ACME

Este diretório reúne o material de partida da oficina da Sessão 9: um marketplace local de plugins do Claude Code, com dois plugins fictícios da ACME e um portão de governança que lê a ficha `governanca.json` de cada plugin antes de aprovar a publicação.

## Pré-requisitos

Node.js 20 ou superior e, para a validação final, o Claude Code instalado. O projeto não tem dependências, e o executor de testes é o que já vem embutido no Node.

```bash
node --version   # precisa mostrar v20 ou superior
npm test         # deve terminar com 26 testes passando
```

## O que tem aqui

| Arquivo | Conteúdo |
|---|---|
| `portao.mjs` | O portão, que exporta `verificarFicha` e `verificarMarketplace` e também roda pela linha de comando |
| `test/portao.test.mjs` | Vinte e seis testes das regras do portão, da leitura do catálogo e da chamada ao `claude` |
| `marketplace-acme/` | O marketplace local, com o catálogo em `.claude-plugin/marketplace.json` e dois plugins em `plugins/` |

Cada plugin traz o `plugin.json`, uma skill em `skills/<nome>/SKILL.md` e a ficha `governanca.json` com dono, finalidade, dados tratados, autonomia, faixa de risco, controles e critérios de revisão.

## Como rodar o portão

```bash
node portao.mjs marketplace-acme --sem-claude
```

A saída traz um bloco por plugin, com "aprovado" ou a lista de erros. Sem a opção `--sem-claude`, o portão executa também `claude plugin validate` quando nenhum plugin tem erro, e no Windows passa o caminho entre aspas para aceitar pasta com espaço no nome.

| Código de saída | Situação |
|---|---|
| 0 | Todos os plugins aprovados e, sem `--sem-claude`, `claude plugin validate` aprovado |
| 1 | Algum plugin reprovado, ou o código devolvido por `claude plugin validate` quando ele reprova |
| 2 | Uso incorreto, `marketplace.json` ausente ou ilegível, `plugins` fora de uma lista, ou comando `claude` não encontrado |

Uma entrada nula ou sem `name` em `plugins` reprova só aquela entrada, identificada pela posição, como `plugins[0]`, e os demais plugins continuam a ser verificados. A mensagem de `claude` ausente informa a versão 2.1.317, única em que os comandos da oficina foram executados, como versão mínima verificada.

## Um plugin reprova de propósito

O plugin `revisando-pull-requests` usa uma credencial pessoal ampla por conveniência, e o único controle preventivo do risco é uma instrução ao modelo. O portão reprova esse caso, e a oficina pede a correção da ficha para que ele passe.

## O zip publicado na oficina

A oficina da Sessão 9 distribui este diretório como `docs/sessao-09-governanca-de-skills-e-agentes/assets/marketplace-governado.zip`, com os arquivos acima e sem `node_modules`. Depois de alterar qualquer arquivo daqui, o zip é regenerado na raiz do repositório do workshop com o comando abaixo, igual no Windows, no macOS e no Linux, que usa só a biblioteca padrão do Python.

```text
python scripts/gerar_zip_marketplace.py
```

A suíte `python -m unittest discover -s tests` reprova o commit quando o conteúdo do zip difere destes arquivos.
