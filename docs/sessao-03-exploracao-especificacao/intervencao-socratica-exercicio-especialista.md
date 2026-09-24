# Exercício de IA — Especialista: da entrevista ao esqueleto técnico

**Para quem implementa em código.** Este exercício usa o agente de codificação já configurado (Claude Code, Codex CLI ou Gemini CLI) e um projeto vazio, montado nesta oficina. Ele parte do mesmo pedido do [Exercício de IA — Geral](intervencao-socratica-exercicio-geral.md), mas acrescenta uma etapa de exploração de código antes da entrevista, e fecha traduzindo o dossiê em um esqueleto técnico, em vez de parar no texto.

## Preparação

```bash
mkdir oficina-intervencao-socratica && cd oficina-intervencao-socratica
git init
```

## O pedido

A Vetor recebeu este pedido de um gerente de logística:

> "Quero que o sistema avise o time de logística quando um pedido atacado ficar parado demais. A gente perde cliente quando isso acontece e ninguém percebe a tempo."

## Passo 1 — explore antes de perguntar

Peça ao agente para propor, em três linhas, uma estrutura mínima de dados que já registraria o necessário para detectar um "pedido parado": um campo de status, um carimbo de tempo por mudança de status, e nada além disso. Essa exploração não é a especificação. É o levantamento que evita perguntar, na entrevista, algo cuja resposta técnica óbvia já existe.

## Passo 2 — instale o entrevistador e conduza a entrevista

Numa conversa separada da exploração do passo 1, cole o [prompt de intervenção socrática](intervencao-socratica-exemplo-de-aplicacao-de-ia.md#o-prompt-de-intervencao-socratica), entregue o pedido e responda como se você fosse o gerente de logística. Force, em algum momento, um adjetivo vago ("o time precisa ser avisado rápido") e confira se a próxima pergunta foi de quantificação. Feche com "fechar entrevista" depois de pelo menos seis respostas substantivas.

## Passo 3 — traduza o dossiê em esqueleto técnico

Com o dossiê em mãos, peça ao agente um esqueleto de função, sem implementação de lógica de negócio, só a assinatura e os tipos: algo como `verificarPedidosParados(pedidos, limiarHoras)`, com um comentário por parâmetro citando de qual item do dossiê ele vem. Cada parâmetro da assinatura precisa apontar para uma resposta específica do dossiê, e nenhum valor numérico entra na assinatura sem ter aparecido no registro de proveniência como `[FATO]`, `[DECISÃO]` ou, na falta de uma fonte melhor, `[PRESSUPOSTO]` explicitamente marcado como tal em comentário.

## Passo 4 — audite a tradução

Compare o esqueleto do passo 3 com o dossiê do passo 2, linha por linha. Alguma decisão entrou na assinatura sem ter sido perguntada na entrevista? Esse é o sinal de que a tradução reintroduziu, por conta própria, exatamente o tipo de suposição que a entrevista existe para evitar.

**Questões exploratórias:**

- A exploração do passo 1 mudou alguma pergunta que você faria na entrevista do passo 2? Qual pergunta você teria feito sem ter olhado a estrutura de dados primeiro?
- O limiar de tempo que define "parado demais" veio da entrevista como `[FATO]`, `[DECISÃO]` ou `[PRESSUPOSTO]`? O que muda no esqueleto técnico se essa marca estiver errada?
- Se você tivesse pedido direto ao agente "implemente um alerta de pedido parado", sem a entrevista, qual valor de limiar ele teria escolhido sozinho, e com que grau de confiança isso teria sido comunicado a você?

## Evidência a entregar

Quatro itens: a proposta de estrutura de dados do passo 1, o dossiê completo do passo 2, o esqueleto técnico do passo 3 com os comentários de proveniência, e a auditoria do passo 4 apontando qualquer decisão que tenha entrado sem passar pela entrevista.

**Próxima página:** [Conceitos de decomposição de requisitos](decomposicao-de-requisitos-conceitos.md).
