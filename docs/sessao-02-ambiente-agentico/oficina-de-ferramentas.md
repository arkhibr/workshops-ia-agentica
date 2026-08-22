# Oficina de ferramentas — montando o ambiente compartilhado

**Objetivo Bloom:** Compreender e Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Copilot ou Cursor), o próprio git, já instalado em qualquer máquina de desenvolvimento, e Node.js com `npx` disponível no terminal para o Experimento B (participantes de C# sem Node instalado devem instalar antes da aula, ou parear com um colega que tenha). Tempo estimado: 30 minutos.

**Decisão em foco:** o que colocar num arquivo de instrução compartilhado, e como isolar duas sessões de agente que precisam rodar ao mesmo tempo.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimentos A, B e C, para sair da sessão com um arquivo de instrução real, um servidor MCP conectado e testado, e um worktree testado.
- **Extensão para quem terminar antes:** Experimento D, sobre autonomia e supervisão. Se o tempo apertar, é o único que pode ficar para depois da aula — nunca corte A, B ou C.

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

## Experimento B — conecte e examine um servidor MCP real

**Classificação:** Essencial em aula.

**Objetivo:** conectar um servidor MCP real, sem precisar de conta nem de credencial, e examinar exatamente qual ferramenta o agente chamou e o que voltou dessa chamada — não só o resumo final que o modelo escreve para você.

**Ferramenta usada:** o servidor de referência `@modelcontextprotocol/server-filesystem`, mantido pelo próprio projeto do MCP. Ele expõe operações de leitura e escrita de arquivo (`read_text_file`, `list_directory`, `search_files`, `write_file`, entre outras) restritas a uma ou mais pastas que você escolhe — o mesmo princípio de escopo mínimo visto em [Padrões e decisões](padroes-e-decisoes.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp).

**Execute:**

1. Crie uma pasta de teste fora do repositório atual, com dois arquivos dentro:

   ```bash
   mkdir -p ~/mcp-teste
   echo "Senha do cofre de testes: abacate-37." > ~/mcp-teste/anotacoes.txt
   printf "produto,preco\nteclado,150\nmonitor,900\n" > ~/mcp-teste/precos.csv
   ```

2. **Antes de conectar nada**, pergunte ao seu agente: "Liste os arquivos em `~/mcp-teste` e me diga qual é a senha do cofre de testes mencionada em anotacoes.txt." Guarde a resposta. Ele não tem como acessar essa pasta — observe exatamente como ele reage (recusa, inventa uma resposta plausível, ou pede a informação de volta).

3. Adicione o servidor à configuração de MCP da sua aplicação agêntica, apontando só para a pasta de teste:

   ```json
   {
     "mcpServers": {
       "arquivos-teste": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/caminho/completo/para/mcp-teste"]
       }
     }
   }
   ```

4. Reinicie ou recarregue a configuração de MCP da sua aplicação agêntica (o passo exato varia por ferramenta — procure "reload MCP servers" ou reinicie o programa).

5. Repita exatamente a mesma pergunta do passo 2. Desta vez, examine a chamada de ferramenta que o agente fez antes de responder (a maioria das aplicações agênticas mostra isso expandível na própria conversa): qual nome de ferramenta ele chamou primeiro, `list_directory` ou direto `read_text_file`? O conteúdo bruto que voltou da chamada bate com o arquivo que você criou?

6. Teste o limite do escopo: peça ao agente para listar um diretório fora de `~/mcp-teste`, por exemplo sua pasta de Documentos inteira. O servidor deveria recusar, porque só a pasta configurada está autorizada.

**Questões exploratórias:**

- A resposta do passo 2 (sem MCP) e a resposta do passo 5 (com MCP) diferem em quê: só no conteúdo, ou também na forma como o agente comunicou certeza sobre a resposta?
- O que aconteceu no passo 6 confirma ou contradiz o critério de escopo mínimo de [Padrões e decisões](padroes-e-decisoes.md#antes-de-conectar-avaliar-a-origem-do-servidor-mcp)?
- Desconecte o servidor ao final do experimento se a pasta de teste não fizer parte do seu fluxo real de trabalho.

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

## Experimento D — compare dois níveis de autonomia

**Classificação:** Extensão para quem terminar antes.

**Objetivo:** sentir a diferença de risco e de velocidade entre dois modos de permissão da mesma aplicação agêntica, aplicando o critério de [Padrões e decisões](padroes-e-decisoes.md#quanto-de-autonomia-liberar).

**Execute:**

1. Escolha uma tarefa pequena e fácil de reverter (por exemplo, adicionar uma função utilitária num arquivo de teste, sem tocar código de produção).
2. Rode essa tarefa no modo de menor autonomia da sua aplicação agêntica, o que pede confirmação antes de cada edição ou comando. Cronometre o tempo total e conte quantas vezes você precisou confirmar algo.
3. Escolha uma segunda tarefa da mesma classe de risco, mas não idêntica (para não haver cache de resposta). Rode-a dentro de um dos worktrees do Experimento C, no modo de maior autonomia disponível, com edições automáticas.
4. Compare: tempo total, quantas vezes você olhou antes de o agente agir, e se alguma edição saiu diferente do que você esperava.

**Questões exploratórias:**

- A tarefa que você escolheu era mesmo fácil de reverter? Se não fosse, você confiaria no modo de autonomia ampla do passo 3?
- Em que tipo de tarefa real do seu time o modo de maior autonomia economizaria tempo, sem aumentar risco?

## Evidência a entregar

O `AGENTS.md` ou `CLAUDE.md` escrito no Experimento A com uma frase sobre o que mudou (ou não) no comportamento do agente depois dele existir, e do Experimento B, o nome da ferramenta que o agente chamou no passo 5 e se a resposta do passo 6 confirmou o escopo configurado.

**Próxima página:** [Exercícios](exercicios.md).
