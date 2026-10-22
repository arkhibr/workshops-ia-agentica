# Skills

Uma skill é uma pasta com um arquivo `SKILL.md` que ensina o agente a executar um tipo de tarefa da equipe sempre do mesmo modo, sem que a pessoa repita as instruções a cada conversa. Esta página descreve a anatomia da skill, o custo de carga em três níveis e as regras de escrita que a documentação da Anthropic recomenda.

## Anatomia de uma skill

A [documentação das skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) define como obrigatório um arquivo `SKILL.md` com frontmatter YAML que contém dois campos. O campo `name` aceita até 64 caracteres, apenas letras minúsculas, números e hífens, e não pode conter as palavras reservadas "anthropic" e "claude". O campo `description` não pode ficar vazio, aceita até 1.024 caracteres e precisa dizer o que a skill faz e quando usá-la.

No Claude Code, as skills ficam em `~/.claude/skills/` quando são pessoais e em `.claude/skills/` quando pertencem ao projeto, e cada skill ocupa uma pasta com o nome dela. As skills do Claude Code são baseadas em arquivos e não são sincronizadas com as do claude.ai nem com as da API, de modo que cada superfície recebe a própria cópia. No Claude Code, a skill também pode ser distribuída por meio de plugins.

```text
.claude/skills/registrando-decisao-arquitetural/
├── SKILL.md            instruções principais, carregadas quando a skill é acionada
├── modelo-adr.md       modelo do artefato, lido só quando o agente precisa dele
└── scripts/
    └── validar_adr.py  script de conferência, executado sem entrar no contexto
```

## Três níveis de carga

A skill usa divulgação progressiva: o agente carrega a informação em etapas, conforme a tarefa exige. A tabela reproduz os valores da documentação.

| Nível | Quando carrega | Custo em tokens | Conteúdo |
|---|---|---|---|
| 1. Metadados | Sempre, na inicialização | Cerca de 100 tokens por skill | `name` e `description` do frontmatter |
| 2. Instruções | Quando a skill é acionada | Abaixo de 5 mil tokens | Corpo do `SKILL.md` |
| 3. Recursos e código | Sob demanda | Nenhum até o acesso | Arquivos de referência, modelos e scripts |

Enquanto uma skill não é acionada, somente o nome e a descrição ocupam o contexto, e por isso uma equipe pode instalar muitas skills sem penalidade relevante. Os scripts têm uma vantagem adicional: o código nunca entra no contexto, e apenas a saída do script consome tokens. A documentação recomenda escrever scripts para as operações determinísticas, porque são mais confiáveis que o código gerado a cada uso, economizam tokens e garantem consistência entre execuções.

## Escrever a descrição

A descrição é o texto contra o qual o agente compara o pedido da pessoa para decidir se aciona a skill, e a documentação indica que essa escolha ocorre entre possivelmente mais de 100 skills disponíveis. As regras de escrita são três: a descrição vem em terceira pessoa, porque é injetada no prompt de sistema e a mudança de ponto de vista prejudica a descoberta, informa o que a skill faz e em que situações deve ser usada, e contém os termos que a pessoa costuma empregar no pedido.

| Descrição | Avaliação |
|---|---|
| `Processa arquivos Excel e gera relatórios. Use ao analisar planilhas, dados tabulares ou arquivos .xlsx.` | Terceira pessoa, diz o que faz e quando usar |
| `Posso ajudar você a processar arquivos Excel.` | Primeira pessoa, sem gatilho de uso |
| `Ajuda com documentos.` | Vaga, o agente não distingue de outras skills |

## Escrever o corpo

O corpo deve conter apenas o que o agente ainda não sabe. A documentação trata a janela de contexto como um recurso compartilhado entre o prompt de sistema, o histórico da conversa, os metadados das outras skills e o pedido, e pede que cada parágrafo justifique o custo em tokens. O corpo do `SKILL.md` fica abaixo de 500 linhas, e o conteúdo excedente vai para arquivos separados, referenciados diretamente a partir do `SKILL.md`, a um nível de profundidade, porque o agente pode ler apenas o início de arquivos referenciados por outros arquivos.

O grau de liberdade da instrução acompanha a fragilidade da tarefa.

| Grau de liberdade | Quando usar | Forma da instrução |
|---|---|---|
| Alto | Vários caminhos válidos, decisão depende do contexto | Passos em texto e heurísticas |
| Médio | Existe um padrão preferido, com alguma variação aceitável | Modelo ou pseudocódigo com parâmetros |
| Baixo | Operação frágil, em que a ordem importa | Script exato, sem alteração dos parâmetros |

A documentação ainda recomenda usar uma única palavra para cada conceito ao longo da skill, evitar informação que perde a validade com a data e oferecer um caminho padrão com uma exceção explícita para o caso especial, sem listar alternativas equivalentes.

## Skill, instrução de projeto e pedido avulso

Uma instrução pode ficar em três lugares, e cada um tem um custo de carga diferente. O guia de [custo do Claude Code](../referencia/bibliografia.md#anthropic-manage-costs-effectively-documentacao-do-claude-code) informa que o `CLAUDE.md` é carregado no início de toda sessão, que as skills carregam apenas sob demanda e que o `CLAUDE.md` deve ter menos de 200 linhas, com instruções de fluxos específicos, como revisão de pull request, movidas para skills.

| Lugar | Carga | Indicado para |
|---|---|---|
| `CLAUDE.md` | Toda sessão | Regras que valem para qualquer tarefa do projeto |
| Skill | Quando acionada | Procedimento recorrente de um tipo de tarefa |
| Pedido avulso | Uma conversa | Tarefa que não se repete |

## Avaliar antes de escrever

A documentação recomenda criar as avaliações antes do texto extenso. O procedimento tem cinco passos: executar o agente em tarefas representativas sem a skill e registrar as falhas, criar três cenários que testem essas falhas, medir o desempenho sem a skill, escrever o mínimo de instruções que resolva as falhas e iterar contra a medição inicial. A lista de verificação da própria documentação pede pelo menos três avaliações e testes com Haiku, Sonnet e Opus, porque o que basta para o Opus pode exigir mais detalhe para o Haiku.

!!! warning "Skill de terceiros"
    A documentação orienta usar apenas skills criadas pela própria equipe ou obtidas da Anthropic, porque uma skill maliciosa pode instruir o agente a chamar ferramentas ou executar código de modo diferente do objetivo declarado. No Claude Code, a skill tem o mesmo acesso de rede que qualquer programa do computador da pessoa. Antes de instalar uma skill externa, revise todos os arquivos dela, incluindo scripts, e procure chamadas de rede e acessos a arquivos que não combinem com a finalidade descrita.

**Próxima página:** [Agentes e subagentes](agentes-e-subagentes.md).
