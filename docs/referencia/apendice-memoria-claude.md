# Apêndice — Ativar e conferir a memória do Claude

Este roteiro cobre os recursos de memória do Claude nas aplicações de conversa e no Claude Code, com seus controles, escopos e locais de armazenamento. Comece pela seção correspondente à aplicação que você usa.

!!! info "Registro de versão e ambiente"
    **Fontes conferidas em 30/09/2026:** páginas oficiais da Anthropic vinculadas ao fim deste apêndice. **Teste local realizado:** `claude --version` retornou `2.1.285 (Claude Code)` em macOS. Os caminhos de interface do Claude web, Desktop, Mobile e os comandos interativos `/memory` e `/context` foram conferidos na documentação oficial, mas não executados numa conta de participante. Ao repetir o roteiro, anote **aplicação, versão, plataforma, plano, data e resultado** no [registro de verificação](#registro-de-verificacao).

## Escolha o mecanismo

| Necessidade | Recurso | Onde fica |
|---|---|---|
| Claude lembrar preferências e contexto entre conversas | Memória das conversas | Claude web, Desktop e Mobile: **Configurações → Memória** |
| Encontrar o que foi dito em um chat anterior | Busca e referência a chats | Alternância em **Configurações → Memória** e consulta no chat |
| Manter contexto de um assunto separado dos demais | Memória de projeto | Conversas dentro de um **Projeto** do Claude |
| Fixar convenções de um repositório para sessões de programação | `CLAUDE.md` | Arquivo no repositório ou na pasta pessoal do Claude Code |
| Permitir que Claude Code anote aprendizados por repositório | Memória automática | Comando `/memory` no Claude Code |

Memória de conversas e busca de chats têm controles próprios. O arquivo `CLAUDE.md` fornece instruções persistentes ao Claude Code. Consulte [Memória e busca de chats](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) e [Memória do Claude Code](https://code.claude.com/docs/en/memory).

## 1. Ativar memória das conversas no Claude

**Onde este roteiro foi verificado:** documentação oficial do Claude web, Desktop e Mobile consultada em **30/09/2026**. A interface de uma conta específica não foi testada. A Anthropic informa que a memória vem ligada por padrão nos planos Free, Pro e Max. Nos planos Team e Enterprise, um proprietário precisa habilitá-la para a organização antes de o membro ativá-la. [Fonte oficial](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

1. Abra o Claude e entre em **Configurações → Memória**.
2. Ative **Gerar memória a partir dos chats** (*Generate memory from chats*). Se a alternância já estiver ligada, registre esse estado no campo “resultado” do [registro de verificação](#registro-de-verificacao).
3. Em uma conversa comum, peça: “Lembre que, neste workshop, prefiro exemplos de C# e TypeScript.”
4. Abra **Configurações → Memória → Tópicos** e confira a entrada. Também é possível pedir ao Claude para alterar ou esquecer uma informação.
5. Inicie uma nova conversa comum e pergunte qual preferência foi guardada. Confira a resposta contra a entrada exibida em Tópicos.

!!! warning "Se a opção não aparecer"
    Registre o plano e a plataforma. Em Team ou Enterprise, peça ao proprietário que confira **Configurações da organização → Capacidades**. Algumas organizações têm restrições de disponibilidade. Se a conta ainda mostrar **Memória** dentro de **Configurações → Capacidades**, siga a seção de experiência legada da [documentação oficial](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#information-for-legacy-memory-users) e anote esse caminho no registro. Não procure um botão de ativação em outra aplicação do Claude.

### Busca de chats anteriores

Nos planos pagos Pro, Max, Team e Enterprise, confira a alternância **Buscar e referenciar chats** em **Configurações → Memória**. Em um novo chat, pergunte “O que discutimos sobre [assunto]?” e observe se a busca aparece como chamada de ferramenta, com referência ao chat de origem. Dentro de um projeto, a busca fica limitada às conversas daquele projeto. Nos chats comuns, ela cobre os chats fora de projetos. A disponibilidade pode depender da implantação gradual na conta. [Fonte oficial](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

**Lembrete de versão:** registre o plano, a aplicação e a data em que testou a alternância. Confirme a chamada de ferramenta e a referência ao chat de origem para verificar o uso da busca.

### Memória de projeto

Crie um projeto em **Projetos → Novo projeto** e abra uma conversa dentro dele. Cada projeto tem seu próprio espaço de memória, separado dos chats comuns e dos demais projetos. Use **Definir instruções do projeto** para orientações que devem valer em todas as conversas do projeto. Coloque documentos de referência na base de conhecimento do projeto. [Projetos no Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), [memória de projetos](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

**Lembrete de versão:** anote em qual projeto, aplicação, plano e data você conferiu a memória. Teste com duas conversas do mesmo projeto e uma conversa fora dele para observar o escopo.

## 2. Dar memória de projeto ao Claude Code

**Onde este roteiro foi verificado:** [documentação oficial do Claude Code](https://code.claude.com/docs/en/memory) consultada em **30/09/2026**. A instalação local respondeu **Claude Code 2.1.285 no macOS** ao comando `claude --version`. A criação ou edição de arquivos pessoais de memória não foi executada neste repositório.

### Instruções persistentes com `CLAUDE.md`

1. No terminal, entre na raiz do repositório e execute `claude`.
2. Dentro da sessão, execute `/init` para gerar uma proposta inicial de `CLAUDE.md`. Se o arquivo já existir, o comando sugere melhorias em vez de substituí-lo automaticamente.
3. Revise o arquivo. Registre comandos de build e teste, estrutura do projeto e convenções que devem valer em todas as sessões. Um exemplo curto:

   ```markdown
   # Convenções do projeto

   - Execute `npm test` antes de propor um commit.
   - Código de interface fica em `src/ui/`.
   - Exemplos de API usam TypeScript.
   ```

4. Inicie uma nova sessão no mesmo repositório e execute `/context`. Confirme que o arquivo aparece em **Memory files**. Use `/memory` para localizar e editar os arquivos carregados.

O arquivo `./CLAUDE.md` ou `./.claude/CLAUDE.md` serve ao projeto e pode ser versionado com a equipe. O arquivo `~/.claude/CLAUDE.md` serve às preferências pessoais em todos os projetos daquela máquina. Essas instruções orientam o agente, mas não são uma trava técnica para ações. [Locais e escopos oficiais](https://code.claude.com/docs/en/memory#choose-where-to-put-claudemd-files).

**Lembrete de versão:** registre a saída de `claude --version`, o sistema operacional, o caminho do arquivo e a data da checagem com `/context`. Nesta edição, a verificação local cobriu apenas a versão instalada.

### Memória automática do Claude Code

1. Na sessão do Claude Code, execute `/memory`.
2. Confira a alternância de **auto memory**. A documentação a descreve como ligada por padrão. Se estiver desligada, ative-a no menu. O controle grava `autoMemoryEnabled` nas configurações do usuário.
3. Peça uma lembrança útil para sessões futuras, como “Lembre que os testes de integração deste projeto exigem Redis local”.
4. Volte a `/memory` e abra a pasta de memória automática. Confira o índice `MEMORY.md` e, se houver, o arquivo do tópico criado.
5. Abra uma nova sessão no mesmo repositório e verifique se a informação é recuperada. A gravação não ocorre necessariamente em toda sessão. Confira o arquivo para saber se o pedido foi salvo.

A memória automática fica em `~/.claude/projects/<project>/memory/`, é local à máquina e é compartilhada entre worktrees do mesmo repositório. O índice `MEMORY.md` é carregado no início da conversa. Arquivos de tópicos são lidos quando necessários. Para desativar apenas em um projeto, a [documentação](https://code.claude.com/docs/en/memory#enable-or-disable-auto-memory) descreve `"autoMemoryEnabled": false` em `.claude/settings.json`. [Armazenamento e auditoria](https://code.claude.com/docs/en/memory#storage-location).

**Lembrete de versão:** registre a versão do Claude Code, o repositório, a máquina e a data em que executou `/memory`. A documentação consultada em 30/09/2026 descreve esse comportamento. A verificação local deste apêndice confirmou apenas que a instalação é 2.1.285.

## Trazer memória de outro assistente

No Claude web ou Desktop, abra **Configurações → Memória → Iniciar importação**, cole o texto exportado do serviço anterior e selecione **Adicionar à memória**. Revise os tópicos criados antes de usá-los. A Anthropic classifica a importação como experimental e informa que nem toda entrada será incorporada. O recurso está documentado para Free, Pro, Max e Team. [Instruções oficiais de importação](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude).

**Lembrete de versão:** registre a aplicação, o plano, a data, o caminho exibido e quais tópicos apareceram após a importação. Esta edição verificou o fluxo apenas na documentação oficial em 30/09/2026.

## Revisar, pausar e apagar

Na memória de conversas, **Configurações → Memória → Tópicos** permite ler, editar e excluir entradas. **Pausar memória** preserva as entradas sem usá-las ou criar outras. **Redefinir memória** apaga as entradas, inclusive as dos projetos, de forma irreversível. Chats anônimos não entram na memória. [Controles oficiais](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

No Claude Code, `/memory` abre os arquivos de instrução e a pasta de memória automática para inspeção. Antes de excluir um arquivo, confirme seu escopo: pessoal, projeto ou organização. [Controles oficiais](https://code.claude.com/docs/en/memory#view-and-edit-with-memory).

## Registro de verificação

Preencha este quadro sempre que o tutorial for repetido ou atualizado. Ele identifica **onde a versão foi testada** e evita que um caminho visto em uma conta seja apresentado como universal.

| Campo | Registro desta edição | Sua verificação |
|---|---|---|
| Data | 30/09/2026 | ____ |
| Aplicação e plataforma | Claude Code no macOS. Web, Desktop e Mobile conferidos em documentação | ____ |
| Versão observada | Claude Code 2.1.285 (`claude --version`) | ____ |
| Plano e tipo de conta | Não verificados nesta edição | ____ |
| Conta ou organização de teste | Não houve teste autenticado | ____ |
| Caminho de interface ou comando | Fontes oficiais abaixo. Execução local apenas de `claude --version` | ____ |
| Resultado e evidência | Versão local confirmada. Demais passos documentados | ____ |

Se uma tela divergir, anote a versão e a plataforma, consulte a fonte oficial correspondente e corrija o roteiro com a data do novo teste.

## Fontes oficiais

- [Anthropic — Usar busca de chats e memória no Claude](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context), consultado em 30/09/2026.
- [Anthropic — Criar e gerenciar projetos](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), consultado em 30/09/2026.
- [Anthropic — Como Claude Code lembra seu projeto](https://code.claude.com/docs/en/memory), consultado em 30/09/2026.
- [Anthropic — Importar e exportar memória](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude), consultado em 30/09/2026.
