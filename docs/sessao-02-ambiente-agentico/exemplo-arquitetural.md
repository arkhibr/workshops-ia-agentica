# Exemplo arquitetural

O instrutor conduz esta demonstração, montando do zero o ambiente agêntico da Vetor. Você vai ver as três peças compartilhadas sendo instaladas num repositório real, uma de cada vez.

A **Vetor** é uma empresa fictícia de e-commerce B2B, usada nos exemplos deste workshop. Ela atende clientes padrão e atacado. Hoje os quatro desenvolvedores do time usam agentes configurados de formas diferentes. Dois têm um `CLAUDE.md` pessoal e desatualizado, um não tem arquivo nenhum, e nenhum deles conecta o agente ao rastreador de tarefas da empresa. Há três semanas esse arranjo já custou um bug em produção: um agente comparou o tipo de cliente com `"Atacado"`, maiúsculo, do jeito que aparece na tela, em vez de `"atacado"`, que é o valor gravado no banco. A faixa de desconto de 20% nunca disparou para um lote inteiro de pedidos.

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

O arquivo não traz arquitetura histórica nem instrução genérica como "escreva código limpo". Cada linha muda um comportamento que o agente teria de outro jeito sem ela.

Para testar, repita a tarefa que causou o bug. **Antes** de o arquivo existir, um desenvolvedor pede: "escreva a validação que decide se um pedido é elegível para a faixa de desconto de atacado." Uma saída típica escreve `if (cliente.tipo === "Atacado")`, porque nada no prompt disse qual valor está gravado no banco. **Depois** de o arquivo existir, o mesmo pedido produz `if (cliente.tipo === "atacado")`. O agente leu a convenção antes de escrever a primeira linha, e ninguém precisou repeti-la no prompt.

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

**Antes** de conectar, pegar uma tarefa em aberto exigia abrir o rastreador no navegador, copiar o texto e colar no prompt. Era um passo manual a cada tarefa nova, e a descrição chegava incompleta toda vez que alguém colava só o título.

**Depois** de conectado, perguntar "quais tarefas estão atribuídas a mim agora" faz o agente chamar a ferramenta `listar_minhas_tarefas` do servidor e devolver algo como:

```json
[
  { "id": "VET-482", "titulo": "Corrigir cálculo de frete para CEP de zona rural", "status": "em andamento", "prioridade": "alta" },
  { "id": "VET-490", "titulo": "Adicionar filtro de status no relatório de vendas", "status": "aberta", "prioridade": "média" }
]
```

Pedir "comece a trabalhar na VET-482" a partir daqui já entrega ao agente o título e a prioridade, sem ninguém copiar nada. Se a descrição completa também estiver no rastreador, uma segunda chamada de ferramenta (`obter_detalhes_tarefa`) traz o resto antes de qualquer código ser escrito.

## Passo 3 — Isolamento por ramo

Dois desenvolvedores da Vetor, na mesma tarde, pegam tarefas diferentes do rastreador: Ana assume a VET-482 (frete), Bruno assume a VET-490 (relatório). Em vez de os dois trabalharem no mesmo diretório, cada um cria um worktree:

```bash
git worktree add ../vetor-fix-frete -b fix/VET-482-frete-zona-rural
git worktree add ../vetor-relatorio -b feature/VET-490-filtro-status
```

A VET-482 é uma correção pequena, num cálculo isolado e fácil de reverter, então Ana deixa o agente rodar no modo de maior autonomia dentro do próprio worktree, sem confirmar cada edição. A VET-490 mexe no relatório de vendas que a diretoria usa toda semana, então Bruno mantém a confirmação antes de cada edição, mesmo isolado no próprio worktree. Os dois decidiram pelo critério de reversibilidade de [Quanto de autonomia liberar](autonomia-e-supervisao.md#quanto-de-autonomia-liberar), e o isolamento entrou para reduzir o raio de impacto.

Cada agente roda no próprio diretório, na própria branch, sem risco de um sobrescrever a edição do outro enquanto os dois trabalham ao mesmo tempo.

![A plataforma Vetor sai de quatro configurações diferentes para um ambiente construído em três passos: AGENTS.md compartilhado, rastreador conectado via MCP e worktrees isolados para a correção de frete e o relatório de vendas.](../assets/images/s2-vetor-ambiente-tres-passos.png)

## Passo 4 — as três peças juntas, numa tarefa só

Cada peça sozinha parece só mais uma ferramenta. Juntas, elas mudam o formato de uma tarefa inteira. Acompanhe a VET-482 do início ao fim:

1. Ana pergunta "quais tarefas estão atribuídas a mim agora". O agente chama o MCP e devolve a VET-482, com título e prioridade, sem Ana abrir o navegador.
2. Ana pede "cria um worktree e começa a VET-482". O agente sugere o comando de worktree do Passo 3, numa branch nomeada a partir do próprio ID da tarefa.
3. Dentro do worktree, Ana pede a correção do cálculo de frete. O agente já sabe, pelo `AGENTS.md`, que tipo de cliente é `"padrao"` ou `"atacado"` em minúsculo, e que todo commit passa por `npm run lint` antes. São duas regras que ninguém precisou repetir no prompt.
4. Como a tarefa é pequena e está isolada no próprio worktree, Ana aprovou autonomia ampla para essa sessão: o agente edita, roda os testes e só avisa Ana quando termina, em vez de confirmar edição por edição.

Nenhum desses quatro passos dependeu de uma ferramenta de IA específica. O rastreador poderia ser outro, o worktree é git puro, e qualquer agente compatível com o padrão lê o `AGENTS.md`. O que mudou foi o ambiente em volta do agente.

## Leitura do exemplo

O `AGENTS.md` evitou que o bug de comparação de string se repetisse. O MCP tirou o copiar e colar do meio do fluxo. O worktree isolou o raio de impacto de dois trabalhos paralelos, e foi esse isolamento que permitiu a Ana usar mais autonomia sem aumentar o risco. Nenhuma das quatro peças resolve sozinha o problema do início da página. O ambiente nasce da combinação delas.

**Próxima página:** [Estudo de caso](estudo-de-caso.md).
