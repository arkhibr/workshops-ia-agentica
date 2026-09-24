# Exemplo de aplicação de IA: intervenção socrática

Esta é uma demonstração conduzida pelo instrutor. O objetivo é ver o agente atuando como entrevistador socrático sobre uma especificação ruim, expondo decisões de negócio que a primeira leitura não capturou, antes de qualquer linha de código ser escrita a partir dela.

## O prompt de intervenção socrática

Toda a demonstração parte deste prompt, colado numa conversa nova com o agente:

```text
Você é um entrevistador socrático de requisitos. Seu trabalho é PERGUNTAR,
nunca responder, sugerir solução ou corrigir o que eu escrevi.

CONTRATO DE MENSAGEM, obrigatório em toda mensagem sua:
- no máximo 1 frase espelhando o que acabei de dizer
- UMA única pergunta, uma única interrogação na mensagem inteira
- opcionalmente 2 a 4 opções de múltipla escolha, que não contam como
  perguntas adicionais
Duas interrogações na mesma mensagem violam o contrato, mesmo que as
perguntas sejam curtas ou relacionadas.

FASES, nesta ordem: enquadramento, exploração, aprofundamento (pressupostos
e evidências), ampliação (perspectivas alternativas e cenários de falha),
síntese. Só avance de fase quando o critério da fase estiver satisfeito.

CATEGORIAS que você deve percorrer, não só a primeira: esclarecimento,
pressupostos, evidências, implicações, perspectivas alternativas,
meta-pensamento.

REGRA DO ADJETIVO VAGO: se eu usar rápido, flexível, robusto, escalável,
intuitivo, seguro, simples ou moderno, sua próxima pergunta é de
quantificação — número, comportamento observável ou exemplo concreto.

A cada 4 respostas minhas, substitua o espelhamento por uma síntese curta
separando confirmado, suposto e conflitos, e termine com a única pergunta.

CRITÉRIO DE ENCERRAMENTO: as três canônicas respondidas com precisão —
o que estamos construindo, para quem, e qual o critério de sucesso testável.

Quando eu disser "fechar entrevista", produza o dossiê com cinco seções.
As três canônicas. O registro de proveniência classificando cada afirmação relevante como
[FATO], [EVIDÊNCIA], [PRESSUPOSTO], [DECISÃO], [RESTRIÇÃO], [RISCO],
[ABERTA] ou [CONFLITO]. Os termos quantificados, com antes e depois. Os
riscos examinados. E as perguntas que ficaram abertas, com o dono de cada
uma. Opinião sem fonte identificável é [PRESSUPOSTO], nunca [FATO].

Comece pela fase de enquadramento.
```

## A especificação ruim

A Vetor, plataforma fictícia de e-commerce B2B usada em toda esta sessão, recebeu este pedido de um gerente comercial:

> "Precisamos de um painel de relatórios de desconto pro time comercial. Ele deve ter um botão de exportar pra Excel, mostrar um gráfico de pizza com os descontos aplicados no mês, e ser bem intuitivo e moderno. Como os gerentes vão usar isso todo dia, o relatório precisa carregar rápido. Todo desconto aplicado aparece lá. Entrega até sexta, com testes completos e cobertura de 100%."

Antes de colar essa especificação no agente, o instrutor registra por escrito quantos defeitos enxerga numa leitura só: quatro adjetivos vagos (intuitivo, moderno, rápido, "todo desconto"), um prazo sem escopo fechado, e uma meta de cobertura de teste sem relação declarada com o que precisa ser coberto. Esse número é a linha de base contra a qual o dossiê final será comparado.

## A entrevista, em recorte

**Fase de enquadramento.** O agente pergunta quem vai responder pela especificação e qual o critério de encerramento. O instrutor responde como se fosse o próprio gerente comercial que escreveu o pedido.

**Fase de exploração, categoria de esclarecimento.** Diante de "bem intuitivo e moderno", a regra do adjetivo vago dispara: a próxima pergunta exige um comportamento observável. "Qual tarefa um gerente precisa completar sem ajuda, na primeira vez que abre o painel?" A resposta ("encontrar o desconto total do mês em menos de 10 segundos") é o que "intuitivo" queria dizer, sem o adjetivo.

**Fase de aprofundamento, categoria de evidências.** Diante de "os gerentes vão usar isso todo dia", o agente pergunta que evidência sustenta essa frequência: chamado de suporte, planilha paralela, pedido explícito de alguém. A resposta ("ninguém mediu, mas todo mundo comenta") faz essa afirmação virar `[PRESSUPOSTO]` no registro de proveniência, nunca `[FATO]`.

**Fase de ampliação, categoria de perspectivas alternativas.** O agente pergunta como o time de dados, que hoje já extrai o mesmo número por planilha manual, descreveria o mesmo problema. A resposta revela que a extração manual leva 40 minutos por mês, não por dia, e que a urgência de "carregar rápido" era sobre a extração manual, não sobre um painel que ainda não existe.

**Fase de síntese.** O agente resume em três colunas o que ficou confirmado (o número que precisa aparecer, a tarefa que precisa ser completável sem ajuda), o que ficou suposto (frequência de uso diária) e onde há conflito (export para Excel declarado como obrigatório, mas nenhuma resposta anterior explica quem consome esse arquivo depois de exportado).

## O dossiê

Ao final, o comando "fechar entrevista" produz um dossiê com as três canônicas respondidas ("um painel que mostra o desconto total do mês em até 10 segundos, para gerentes comerciais, com sucesso testável por cronômetro contra um usuário que nunca viu o painel"), o registro de proveniência completo, os termos quantificados (intuitivo → 10 segundos; rápido → sem medida encontrada, marcado `[ABERTA]`), o risco examinado (a meta de cobertura de 100% sem escopo fechado pode gerar testes que travam a esteira sem proteger nada relevante) e as perguntas abertas com dono (quem consome o arquivo exportado, com o próprio gerente comercial como responsável por essa resposta).

## Leitura do exemplo

O dossiê final contém mais decisões de negócio do que a leitura inicial do instrutor havia registrado como linha de base, e ao menos uma delas — a distinção entre a urgência da extração manual e a urgência do painel futuro — não estava em nenhuma frase da especificação original, nem podia ser deduzida dela por releitura, por mais atenta que fosse. Ela só apareceu porque uma pergunta específica, da categoria de perspectivas alternativas, forçou o entrevistado a considerar um ângulo que não tinha ocorrido a ele sozinho. Uma análise direta da mesma especificação, pedindo ao agente "aponte os problemas desta especificação" sem o contrato de entrevista, aponta os adjetivos vagos, mas não produz essa distinção, porque ninguém foi obrigado a respondê-la.

**Próxima página:** [Exercício de IA — Geral](intervencao-socratica-exercicio-geral.md).
