# Manter os artefatos vivos

Um conjunto de artefatos de especificação produz valor enquanto descreve o sistema que existe. No dia em que a especificação diz uma coisa e o código faz outra, ela deixa de ser contrato e vira ruído: quem lê passa a conferir tudo no código de qualquer forma, e o tempo gasto em mantê-la foi perdido duas vezes. Esta página trata da disciplina que impede isso.

## Que descoberta atualiza qual artefato

Durante a implementação aparecem informações que não existiam no início. Isso é esperado. O que importa é direcionar cada descoberta ao artefato certo:

| Mudança descoberta | Atualizar |
|---|---|
| necessidade ou regra de negócio | especificação e critérios de aceitação |
| restrição organizacional | constitution ou especificação, conforme o alcance |
| escolha técnica relevante | plano e registro de decisão |
| nova dependência entre trabalhos | tarefas |
| defeito de comportamento | critério e teste de regressão |
| incidente ou métrica de produção | requisito de qualidade, risco e experimento |

O erro comum é registrar tudo no lugar mais fácil, que costuma ser um comentário no código ou uma mensagem de commit. Uma restrição regulatória anotada como comentário numa função não governa a próxima mudança, porque o agente que receber a próxima tarefa não vai lê-la.

!!! question "Antes de continuar"
    Na última vez que a implementação revelou algo que a especificação não previa, onde essa informação ficou registrada? Se foi na conversa com o agente ou na mensagem do commit, ela já se perdeu.

## Rastreabilidade em duas direções

Antes de integrar, vale conferir se a cadeia fecha:

```text
requisito → cenário → decisão de plano → tarefa → teste → evidência
```

Isso não exige ferramenta sofisticada. Identificadores estáveis e links bastam para começar. O que importa é conseguir navegar nos dois sentidos, respondendo tanto "que código implementa o requisito FR-07?" quanto "por que esta validação existe?".

A segunda pergunta é a que costuma ficar sem resposta, e é a mais cara. Quando ninguém consegue distinguir uma regra de negócio deliberada de um acidente de implementação, o time perde a capacidade de mexer no código com segurança: mudar pode quebrar uma regra que ninguém sabia que existia, e não mudar preserva um defeito que todos acham que é regra.

## Regeneração destrutiva

Existe uma tentação específica em fluxos agênticos: pedir ao agente que regenere a especificação inteira a partir do código atual, ou a partir de um modelo novo. O resultado tem aparência de atualização e é, na prática, uma perda.

Texto aprovado por uma pessoa não pode ser sobrescrito porque um modelo produziu formulação diferente. A frase que um especialista de domínio revisou e aceitou carrega uma decisão. A reformulação automática que "diz a mesma coisa com outras palavras" frequentemente não diz, e a diferença só aparece meses depois, quando alguém implementa o caso de fronteira segundo a redação nova.

A regra prática é que toda alteração em artefato aprovado apareça como diferença revisável, do mesmo jeito que uma alteração em código. Se o agente propõe reescrever a especificação, a saída dele é uma proposta de mudança, não um novo estado do arquivo.

## Onde a correção precisa ficar gravada

Um mal-entendido comum atribui ao modelo uma capacidade que ele não tem. Quando o time corrige uma decisão durante a revisão, o modelo não "absorve" aquela correção para as próximas sessões. Ele não aprende com o seu projeto entre uma conversa e outra.

Isso tem consequência direta no fluxo de trabalho: a correção precisa entrar no artefato versionado, senão ela vale só para a sessão em que foi feita. Um time que corrige o agente por conversa, repetidamente, está pagando o mesmo custo de explicação toda semana, e culpando o modelo por "não aprender" quando o problema é que ninguém escreveu a decisão em lugar nenhum.

O [SPDD](abordagens-sdd.md#spdd) torna isso explícito ao exigir que a correção altere o prompt estruturado antes do código. Mesmo sem adotar aquele método, o princípio vale: uma decisão corrigida pertence ao artefato versionado.

!!! tip "Aplique agora"
    Procure no seu projeto uma regra de negócio que só existe no código. Escreva, em duas linhas, o requisito e o caso de fronteira dela. Esse é o menor artefato vivo possível, e já resolve a pergunta "por que isto existe?".

## Depois da entrega

Um artefato vivo continua recebendo informação depois da entrega. Métrica de uso, incidente e reclamação de usuário são evidências de que uma premissa da especificação pode estar errada.

Quando produção contradiz uma premissa, a correção não termina no ajuste que restaura o serviço. Ela volta para a especificação, para que a próxima mudança parta do entendimento corrigido. Um incidente que gera apenas um remendo, sem atualizar requisito nem teste de regressão, garante que o mesmo erro conceitual continue disponível para ser cometido de novo.

**Próxima página:** [Quando o SDD falha](quando-sdd-falha.md).
