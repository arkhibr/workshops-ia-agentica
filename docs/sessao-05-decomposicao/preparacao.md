# Preparação do ambiente

Na Sessão 5 cada participante roda, na própria máquina, o GitHub Spec Kit, ferramenta de linha de comando que conduz o agente pela especificação, pelo plano e pelas tarefas de uma mudança. A instalação leva de 20 a 30 minutos e precisa estar pronta **antes da aula**, porque não há tempo para ela dentro das duas horas.

O roteiro abaixo é para Windows. Quem usa macOS ou Linux encontra as diferenças na [última seção](#macos-e-linux).

## O que precisa funcionar no fim

| Verificação | Comando | Resultado esperado |
|---|---|---|
| Git | `git --version` | `git version 2.x` |
| Node.js | `node --version` | `v20` ou superior |
| uv | `uv --version` | `uv 0.x.y` |
| Spec Kit | `specify version` | `CLI Version 1.1.1` |
| Agente | teste do Passo 6 | o agente lista os comandos `speckit-` |

Se as cinco linhas passarem, o ambiente está pronto. Se alguma falhar e a tabela de [problemas comuns](#problemas-comuns) não resolver, envie ao instrutor a saída do comando antes do dia da aula.

## Passo 1: abra o PowerShell

Abra o **PowerShell** pelo menu Iniciar, sem executar como administrador. Todos os comandos desta página rodam nele, e a instalação fica no seu perfil de usuário.

## Passo 2: Git e Node.js

Confira o que já está instalado:

```powershell
git --version
node --version
```

Instale só o que faltar ou estiver abaixo da versão 20 do Node:

```powershell
winget install --id Git.Git -e --source winget
winget install --id OpenJS.NodeJS.LTS -e --source winget
```

Feche o PowerShell, abra outro e repita as duas verificações. O terminal só enxerga um programa recém-instalado depois de reaberto.

## Passo 3: uv

O uv é o gerenciador de pacotes Python que instala o Spec Kit. Não é preciso instalar o Python antes: o uv baixa a versão necessária sozinho.

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Feche o PowerShell, abra outro e confira com `uv --version`.

## Passo 4: Spec Kit

Instale a versão 1.1.1. A turma inteira usa a mesma versão porque os nomes dos comandos mudam entre versões, e o material da sessão foi testado nesta.

```powershell
uv tool install specify-cli==1.1.1
```

Se a saída avisar que a pasta de ferramentas não está no `PATH`, rode `uv tool update-shell` e reabra o PowerShell. Depois confira:

```powershell
specify version
specify check
```

O `specify version` deve mostrar `CLI Version 1.1.1`. O `specify check` lista dezenas de agentes, quase todos como `not found`, e isso é normal: só importa a linha do agente que você vai usar.

## Passo 5: o agente

Use o agente que você já configurou para o workshop. Confira se ele responde no terminal:

| Agente | Verificação |
|---|---|
| Claude Code | `claude --version` |
| Codex CLI | `codex --version` |
| GitHub Copilot | abra o VS Code e confirme que o chat do Copilot está ativo e com login feito |

Se o agente ainda não estiver instalado:

```powershell
# Claude Code
irm https://claude.ai/install.ps1 | iex

# Codex CLI
npm install -g @openai/codex
```

O GitHub Copilot é a extensão GitHub Copilot, instalada pelo painel de extensões do VS Code.

Antes da aula, abra o agente uma vez e faça o login. Um login pendente costuma travar o primeiro comando da oficina.

## Passo 6: teste completo

Este teste cria um projeto descartável, confirma que o agente enxerga os comandos do Spec Kit e apaga tudo no fim. Troque `claude` por `codex` ou `copilot`, conforme o seu agente.

```powershell
cd $HOME
specify init teste-speckit --integration claude --script ps
cd teste-speckit
```

A saída termina com um painel *Next Steps* listando os comandos instalados. Abra o agente dentro da pasta `teste-speckit` e digite o início do comando, sem apertar Enter:

| Agente | Como abrir | O que digitar |
|---|---|---|
| Claude Code | `claude` | `/speckit-` |
| Codex CLI | `codex` | `$speckit-` |
| GitHub Copilot | `code .` e abra o chat | `/speckit-` |

O agente deve sugerir `speckit-constitution`, `speckit-specify`, `speckit-plan` e `speckit-tasks`, entre outros. Feche o agente sem rodar nenhum deles e apague o projeto de teste:

```powershell
cd $HOME
Remove-Item -Recurse -Force teste-speckit
```

Com Codex, se o `specify init` responder `codex not found`, o Codex CLI não está no `PATH`: volte ao Passo 5.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| `specify` ou `uv` não é reconhecido como comando | o terminal foi aberto antes da instalação | reabra o PowerShell; se persistir, rode `uv tool update-shell` e reabra |
| `a execução de scripts foi desabilitada neste sistema` ao rodar `claude` ou `codex` | política de execução do PowerShell bloqueia os scripts instalados pelo npm | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e reabra o PowerShell |
| erro de certificado ou SSL durante `uv tool install` | a rede da instituição inspeciona o tráfego HTTPS | rode `$env:UV_SYSTEM_CERTS = "true"` e repita a instalação no mesmo terminal |
| `winget` não é reconhecido | Windows sem o Instalador de Aplicativo | instale o Git por [git-scm.com](https://git-scm.com/download/win) e o Node.js por [nodejs.org](https://nodejs.org/) |
| `specify version` mostra outra versão | havia uma instalação anterior | `uv tool install specify-cli==1.1.1 --force` |

Se a política de execução for definida pela TI e o comando `Set-ExecutionPolicy` for recusado, avise o instrutor antes da aula.

## macOS e Linux

A sequência é a mesma, e muda só a forma de instalar. Git e Node.js vêm pelo gerenciador de pacotes do sistema (Homebrew no macOS). O uv é instalado com:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

O Claude Code usa `curl -fsSL https://claude.ai/install.sh | bash`. No teste do Passo 6, troque `--script ps` por `--script sh` e apague a pasta com `rm -rf teste-speckit`. Os demais comandos são idênticos.

**Próxima página:** [Contexto da prática: exemplos e exercícios](contexto-da-pratica.md).
