# Exemplo arquitetural: o ambiente da Vetor

Este exemplo é uma demonstração conduzida pelo instrutor, não um exercício. O objetivo é ver, do zero, as três peças compartilhadas de um ambiente agêntico sendo montadas para um repositório real.

**A Vetor**, usada como caso em toda esta sessão, é uma plataforma fictícia de e-commerce B2B que atende clientes padrão e atacado. Hoje, os quatro desenvolvedores do time usam agentes configurados de formas diferentes: dois têm um `CLAUDE.md` pessoal e desatualizado, um não tem arquivo nenhum, e nenhum deles conecta o agente ao rastreador de tarefas da empresa. Há três semanas, esse ambiente ad hoc já custou um bug em produção: um agente comparou o tipo de cliente com `"Atacado"` (maiúsculo, o jeito como aparece na tela) em vez de `"atacado"` (o valor real gravado no banco), e a faixa de desconto de 20% nunca disparou para um lote inteiro de pedidos.

## Passo 1 — Um arquivo de instrução compartilhado

O time da Vetor escreve, em conjunto, um único `AGENTS.md` na raiz do repositório:

```markdown
# AGENTS.md — Vetor

## Build e testes
- Build: `npm run build`
- Testes: `npm test` (Jest)
- Nunca commitar sem rodar `npm run lint` antes

## Convenções
- Nomes de variáveis e funções em português, alinhado ao domínio do negócio
- Tipos de cliente: sempre "padrao" ou "atacado" (sem acento, minúsculo) — é o valor usado no banco

## Segurança
- Nunca imprimir a chave de API do gateway de pagamento em log
```

Repare no que ficou de fora: nenhuma explicação de arquitetura histórica, nenhuma boa intenção genérica como "escreva código limpo". Cada linha muda um comportamento concreto que o agente tomaria de forma diferente sem essa informação.

O teste está em repetir a tarefa que causou o bug. **Antes** do arquivo existir, um desenvolvedor pede: "escreva a validação que decide se um pedido é elegível para a faixa de desconto de atacado." Uma saída típica escreve `if (cliente.tipo === "Atacado")`, porque nada no prompt disse qual é o valor exato gravado no banco. **Depois** do arquivo existir, o mesmo pedido produz `if (cliente.tipo === "atacado")` — o agente leu a convenção antes de escrever a primeira linha, sem que o desenvolvedor precisasse repeti-la a cada prompt.

## Passo 2 — Uma ferramenta conectada via MCP

A Vetor conecta o agente ao rastreador de tarefas da empresa por um servidor MCP:

```json
{
  "mcpServers": {
    "rastreador-vetor": {
      "command": "npx",
      "args": ["-y", "@vetor-interno/mcp-server-tarefas"],
      "env": {
        "API_TOKEN": "${VETOR_TRACKER_TOKEN}"
      }
    }
  }
}
```

**Antes** de conectar, pegar uma tarefa em aberto exigia abrir o rastreador no navegador, copiar o texto da tarefa e colar no prompt — um passo manual a cada tarefa nova, e uma fonte comum de descrição incompleta quando alguém colava só o título.

**Depois** de conectado, perguntar "quais tarefas estão atribuídas a mim agora" faz o agente chamar a ferramenta `listar_minhas_tarefas` do servidor e devolver algo como:

```json
[
  { "id": "VET-482", "titulo": "Corrigir cálculo de frete para CEP de zona rural", "status": "em andamento", "prioridade": "alta" },
  { "id": "VET-490", "titulo": "Adicionar filtro de status no relatório de vendas", "status": "aberta", "prioridade": "média" }
]
```

Pedir "comece a trabalhar na VET-482" a partir daqui já entrega ao agente o título e a prioridade sem que o desenvolvedor precise copiar mais nada — e, se a descrição completa da tarefa também estiver no rastreador, uma segunda chamada de ferramenta (`obter_detalhes_tarefa`) traz o resto antes de qualquer código ser escrito.

## Passo 3 — Isolamento por ramo

Dois desenvolvedores da Vetor, na mesma tarde, pegam tarefas diferentes do rastreador: Ana assume a VET-482 (frete), Bruno assume a VET-490 (relatório). Em vez de os dois trabalharem no mesmo diretório, cada um cria um worktree:

```bash
git worktree add ../vetor-fix-frete -b fix/VET-482-frete-zona-rural
git worktree add ../vetor-relatorio -b feature/VET-490-filtro-status
```

A VET-482 é uma correção pequena, num cálculo isolado, fácil de reverter: Ana deixa o agente rodar no modo de maior autonomia dentro do próprio worktree, sem confirmar cada edição. A VET-490 mexe no relatório de vendas usado pela diretoria toda semana; Bruno mantém o modo de confirmar antes de cada edição, mesmo isolado no próprio worktree — o critério de [Padrões e decisões](padroes-e-decisoes.md#quanto-de-autonomia-liberar) (reversibilidade da tarefa) decide o nível de autonomia, não o fato de estar isolado ou não.

Cada agente roda no próprio diretório, na própria branch, sem risco de um sobrescrever a edição do outro enquanto os dois trabalham ao mesmo tempo.

![A plataforma Vetor sai de quatro configurações diferentes para um ambiente construído em três passos: AGENTS.md compartilhado, rastreador conectado via MCP e worktrees isolados para a correção de frete e o relatório de vendas.](../assets/images/s2-vetor-ambiente-tres-passos.png)

## Passo 4 — as três peças juntas, numa tarefa só

Isoladas, as três peças parecem três ferramentas separadas. Juntas, mudam o formato inteiro de uma tarefa. Veja a VET-482 do início ao fim:

1. Ana pergunta "quais tarefas estão atribuídas a mim agora" — o agente chama o MCP e devolve a VET-482, com título e prioridade, sem Ana abrir o navegador.
2. Ana pede "cria um worktree e começa a VET-482" — o agente sugere o comando de worktree do Passo 3, numa branch nomeada a partir do próprio ID da tarefa.
3. Dentro do worktree, Ana pede a correção do cálculo de frete. O agente já sabe, pelo `AGENTS.md`, que tipo de cliente é `"padrao"` ou `"atacado"` em minúsculo, e que todo commit passa por `npm run lint` antes — duas regras que ninguém precisou repetir no prompt.
4. Como a tarefa é pequena e está isolada no próprio worktree, Ana aprovou autonomia ampla para essa sessão: o agente edita, roda os testes e só avisa Ana quando termina, em vez de confirmar edição por edição.

Nenhum desses quatro passos exigiu uma ferramenta de IA específica: o rastreador poderia ser outro, o worktree é git puro, o `AGENTS.md` é lido por qualquer agente compatível com o padrão. O que mudou foi o ambiente ao redor do agente, não o agente em si.

## Leitura do exemplo

O `AGENTS.md` evitou uma repetição do bug de comparação de string. O MCP tirou um passo manual (copiar e colar) do meio do fluxo. O worktree isolou o raio de impacto de dois trabalhos paralelos, e essa mesma isolação foi o que permitiu a Ana usar mais autonomia sem aumentar o risco real. Nenhuma das quatro peças resolve sozinha o problema descrito no início da página: juntas, formam o ambiente que faz isso.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
