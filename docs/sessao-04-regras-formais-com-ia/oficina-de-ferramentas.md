# Oficina de ferramentas — formalizando com IA e verificando por retrotradução

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Codex CLI ou Gemini CLI). Não exige código nem instalação — o trabalho é inteiramente sobre formalização de regra. Tempo estimado: 30 minutos.

**Decisão em foco:** usar o agente para formalizar uma regra de negócio em SBVR/RuleSpeak/DMN, e verificar se a formalização preservou a intenção original, sem confiar apenas na leitura de quem já sabia o que a regra deveria dizer.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, formalização e verificação por retrotradução.
- **Extensão para quem terminar antes:** Experimento B, sobreposição de tabela.

## Experimento A — formalize e verifique por retrotradução

**Objetivo:** pedir ao agente para formalizar uma regra ainda em prosa, e depois checar, numa conversa separada, se a formalização preservou o escopo original.

**Antes de começar: por que a ordem importa.** O passo 3 só mede alguma coisa se o passo 2 acontecer numa conversa que não viu o passo 1. Se o mesmo chat que formalizou também retrotraduzir, ele tende a repetir a própria formalização em vez de reconstruir a partir dela — a verificação perde o sentido.

**Passo 1 — formalize.** A regra de lançamento da Sessão 3, em prosa: "primeiro pedido de qualquer cliente (padrão ou atacado), se o valor for menor que R$ 1.000,00, recebe 3 pontos percentuais adicionais de desconto, somados à faixa normal." Peça ao agente para formalizar essa regra em três partes: vocabulário SBVR mínimo (os termos que a regra usa), uma sentença RuleSpeak ("must", "must not" ou "may ... only"), e uma linha de tabela de decisão. Guarde a resposta completa.

**Passo 2 — retrotraduza, numa conversa nova.** Abra uma conversa nova com o agente, sem colar o resultado do passo 1, e cole só a sentença RuleSpeak e a linha de tabela que ele gerou. Peça: "reescreva esta regra formal em prosa comum, como se explicasse para alguém que nunca viu a versão técnica."

**Passo 3 — compare.** A retrotradução do passo 2 preservou os três elementos da regra original: que vale para os dois tipos de cliente, que é condicionada ao valor menor que R$ 1.000,00, e que é aditiva (soma-se à faixa normal, não substitui)? Marque qual dos três, se algum, se perdeu ou mudou de escopo na formalização.

**Questões exploratórias:**

- Se algum elemento se perdeu, ele desapareceu na formalização (passo 1) ou na retrotradução (passo 2)? Como você distingue as duas possibilidades?
- O que teria acontecido se você tivesse pulado direto para implementar a partir da formalização do passo 1, sem o passo 2? O erro apareceria num teste, ou só em produção?

## Experimento B — monte a tabela combinada e declare a política

**Objetivo:** combinar a regra de lançamento com a tabela de faixa e tipo de cliente do [Exemplo arquitetural](exemplo-arquitetural.md), e decidir a política de acerto antes que o agente decida por conta própria.

**Execute:** peça ao agente para listar todas as combinações de Valor do Pedido, Tipo de Cliente e "é o primeiro pedido" que poderiam se aplicar ao mesmo tempo a um único pedido real — sem pedir que ele resolva a sobreposição, só que a identifique. Depois, decida você mesmo: essa sobreposição pede Unique (redesenhando as faixas para não se cruzarem), Priority (uma regra explicitamente vence) ou Collect (os dois descontos se somam)? Escreva a política escolhida e o motivo.

**Questões exploratórias:**

- O agente encontrou sozinho a mesma sobreposição que o [Estudo de caso](estudo-de-caso.md) desta sessão descreveu, ou precisou ser guiado a procurá-la?
- Sua política escolhida no Experimento B é a mesma que o incidente do Estudo de caso deveria ter tido desde o início?

## Evidência a entregar

Três itens:

1. A formalização do passo 1 (vocabulário, sentença RuleSpeak, linha de tabela) e a retrotradução do passo 2, lado a lado.
2. A comparação do passo 3: qual elemento, se algum, mudou de escopo.
3. A lista de combinações sobrepostas do Experimento B e a política de acerto escolhida, com o motivo.

**Próxima página:** [Exercícios](exercicios.md).
