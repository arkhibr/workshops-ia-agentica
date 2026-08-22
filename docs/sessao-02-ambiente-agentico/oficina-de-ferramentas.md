# Oficina de ferramentas — montando o ambiente compartilhado

**Objetivo Bloom:** Compreender e Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Copilot ou Cursor) e o próprio git, já instalado em qualquer máquina de desenvolvimento. Tempo estimado: 30 minutos.

**Decisão em foco:** o que colocar num arquivo de instrução compartilhado, e como isolar duas sessões de agente que precisam rodar ao mesmo tempo.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A e Experimento C, para sair da sessão com um arquivo de instrução real e um worktree testado.
- **Exploração em dupla:** Experimento B, para quem já tem acesso a um MCP server configurado.

## Experimento A — escreva o AGENTS.md do seu próprio repositório

**Classificação:** Essencial em aula.

**Objetivo:** produzir um arquivo de instrução que muda comportamento real do agente, não uma lista de boas intenções.

**Execute:**

1. Escolha um repositório real que você usa no dia a dia (não um exemplo genérico).
2. Escreva um `AGENTS.md` (ou `CLAUDE.md`) com no máximo quatro seções: comandos de build/teste, convenções específicas do domínio, o que nunca deve ser feito, e uma seção de segurança se aplicável.
3. Para cada linha escrita, pergunte: "o agente tomaria uma decisão diferente sem essa linha?" Se a resposta for não, apague a linha.

**Observe:** peça ao agente para executar uma tarefa pequena e real do repositório (corrigir um nome de variável, adicionar um teste) antes e depois de o arquivo existir. O comportamento mudou de forma perceptível?

**Questões exploratórias:**

- Alguma linha do seu arquivo é genérica o suficiente para valer para qualquer repositório? Isso é sinal de que ela não diz nada específico.
- O que você escreveria de novo se seu time inteiro fosse ler esse arquivo amanhã?

## Experimento B — conecte uma ferramenta via MCP

**Classificação:** Exploração em dupla.

**Objetivo:** observar, na prática, a diferença entre um agente que só lê arquivos e um agente com acesso a uma ferramenta externa.

**Execute:** usando um servidor MCP já disponível no seu ambiente (um servidor de arquivos, de busca, ou específico do seu stack), peça ao agente uma tarefa que exigiria a ferramenta — por exemplo, consultar o estado de algo fora do repositório.

**Compare:** peça a mesma tarefa sem a ferramenta conectada. O que o agente faz na ausência dela — recusa, inventa uma resposta plausível, ou pede a informação de volta a você?

**Questões exploratórias:**

- A ferramenta conectada mudou o comportamento do agente, ou só acrescentou uma etapa que você faria manualmente de qualquer forma?
- Que outra ferramenta do seu dia a dia faria sentido conectar da mesma forma?

## Experimento C — isole duas sessões por worktree

**Classificação:** Essencial em aula.

**Objetivo:** sentir na prática por que isolamento por ramo evita o incidente do [Estudo de caso](estudo-de-caso.md).

**Execute:**

```bash
git worktree add ../teste-worktree-a -b experimento/a
git worktree add ../teste-worktree-b -b experimento/b
```

Abra um agente em cada diretório e peça, em paralelo, para cada um alterar o mesmo arquivo de formas diferentes (por exemplo, um adicionando um comentário no topo, outro no final).

**Observe:** as duas edições coexistem sem conflito, porque cada worktree tem sua própria cópia de trabalho. Depois, tente mesclar as duas branches — é aqui, no merge, e não durante a edição, que uma eventual sobreposição real precisa ser resolvida.

**Limpeza:**

```bash
git worktree remove ../teste-worktree-a
git worktree remove ../teste-worktree-b
```

**Questões exploratórias:**

- Em que situação do seu time de verdade esse isolamento evitaria um problema como o do Estudo de caso?
- Isolar por worktree substitui a necessidade de comunicação entre quem está mexendo em partes relacionadas do sistema, ou só reduz um tipo específico de risco?

## Evidência a entregar

O `AGENTS.md` ou `CLAUDE.md` escrito no Experimento A, e uma frase sobre o que mudou (ou não) no comportamento do agente depois dele existir.

**Próxima página:** [Exercícios](exercicios.md).
