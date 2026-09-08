# Oficina de ferramentas — do pedido vago à especificação testada

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o agente de codificação já configurado pelo participante (Claude Code, Codex CLI ou Gemini CLI), o git e o Node.js 20 ou superior. Tempo estimado: 30 minutos.

Todos os experimentos rodam sobre o projeto de exemplo da Vetor, para que cada pessoa parta do mesmo estado. Antes de começar, clone o repositório e confirme que os testes passam:

```bash
git clone https://github.com/arkhibr/workshops-ia-agentica.git
cd workshops-ia-agentica/exemplo/vetor
node --version   # precisa mostrar v20 ou superior
node --test       # deve terminar com 6 testes passando
```

**Decisão em foco:** transformar um pedido vago numa especificação BR/FR/NFR verificável, antes de acionar o agente para implementar.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A (ciclo completo) e Experimento C (entrevista socrática sobre uma especificação ruim).
- **Extensão para quem terminar antes:** Experimento B, sobre cenário de qualidade e função de aptidão.

## Experimento A — feche um pedido vago com especificação

**Objetivo:** conduzir o ciclo explorar → perguntar → propor → especificar sobre um pedido novo da Vetor, e comprovar que a especificação escrita é o que o agente de fato implementa.

**Antes de começar: por que a ordem importa.** O bloco de respostas abaixo simula quem pediu a mudança. Ele só cumpre a função de mostrar o efeito das perguntas se você escrever suas próprias perguntas antes de abri-lo. Abrir antes esvazia o experimento.

**Passo 1 — o pedido.** É este, e nada além disso:

> "Dá pra dar um desconto extra pros clientes que compram muito com a gente?"

Escreva, sem abrir o bloco abaixo, de três a cinco perguntas que você faria antes de especificar qualquer coisa. Use o repertório de [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md) como referência.

**Passo 2 — as respostas.** Abra o bloco e compare com as perguntas que você escreveu.

??? note "Respostas de quem pediu — abra só depois de escrever suas próprias perguntas"
    - O que conta como "compra muito"? Cliente do tipo atacado com mais de 5 pedidos aprovados nos últimos 12 meses.
    - Esse desconto extra é cumulativo com a faixa normal, ou substitui? Cumulativo: soma-se à faixa normal, em pontos percentuais.
    - O desconto extra é de quantos pontos percentuais? 5 pontos percentuais.
    - O teto de R$ 1.000,00 por pedido continua valendo com o desconto extra somado? Sim, sempre — nenhuma regra nova revoga o teto.
    - Esse desconto vale para cliente padrão também? Não, só para atacado.

**Passo 3 — proponha e especifique.** Escreva a proposta em três frases, depois a especificação em BR/FR, seguindo o formato de [Exemplo arquitetural](exemplo-arquitetural.md). `calcularDesconto` vai precisar de um terceiro parâmetro, `pedidosAprovados`, opcional, com valor padrão que preserve o comportamento dos seis testes já existentes.

**Passo 4 — peça a implementação.** Cole sua especificação para o agente e peça a implementação, com testes, dentro de `exemplo/vetor`.

**Passo 5 — rode os casos abaixo contra o resultado.**

| # | Valor do pedido | Tipo de cliente | Pedidos aprovados | Desconto esperado |
|---|---|---|---|---|
| 1 | R$ 3.000,00 | atacado | 2 | R$ 300,00 (10%, não elegível ao adicional) |
| 2 | R$ 3.000,00 | atacado | 6 | R$ 450,00 (10% + 5% = 15%) |
| 3 | R$ 6.000,00 | atacado | 6 | R$ 1.000,00 (15% + 5% = 20% de R$ 6.000,00 seria R$ 1.200,00, mas o teto prevalece) |
| 4 | R$ 3.000,00 | padrão | 6 | R$ 300,00 (o adicional não vale para cliente padrão) |

Rode `node --test` e confira também que os seis testes originais continuam passando.

**Observe:** o caso 3 é o único em que a faixa normal, o adicional de recorrência e o teto se cruzam ao mesmo tempo. Se ele falhar, é sinal de que a especificação não deixou claro que o teto se aplica depois de somar os dois percentuais, não antes.

**Questões exploratórias:**

- Alguma das suas perguntas do passo 1 não apareceu entre as respostas do passo 2? O que você teria feito sem essa resposta?
- Se você tivesse pedido direto ao agente "dá pra dar um desconto extra pros clientes que compram muito", sem o ciclo completo, qual das quatro respostas do passo 2 ele teria decidido sozinho?

## Experimento B — cenário de qualidade e função de aptidão

**Objetivo:** escrever um NFR como cenário de qualidade completo, e transformá-lo numa função de aptidão que continua rodando depois da aula.

**Execute:** a Vetor pede que `calcularDesconto` "continue rápida mesmo com muito tráfego". Escreva o cenário de qualidade completo (fonte, estímulo, ambiente, artefato, resposta, medida), seguindo o template de [Atributos de qualidade e RAS](atributos-de-qualidade-e-ras.md#cenario-de-qualidade-o-template-que-torna-um-nfr-testavel). Depois, peça ao agente uma função de aptidão simples: um teste em Node que chama `calcularDesconto` mil vezes com `console.time`/`console.timeEnd` ao redor, com o limiar da sua medida como condição de falha (`assert` ou `throw` se o tempo médio ultrapassar o limiar).

**Questões exploratórias:**

- O cenário que você escreveu seria o mesmo se a função fosse chamada uma vez por pedido, ou mil vezes por segundo no checkout? O que muda no estímulo e na medida?
- Sua função de aptidão tem responsável e reação declarados, ou só o teste técnico? Quem seria avisado se ela falhasse na esteira, daqui a seis meses?

## Experimento C — entrevista socrática sobre uma especificação ruim

**Objetivo:** usar o próprio agente como entrevistador socrático para expor os defeitos de uma especificação ruim, um de cada vez — sem que o agente corrija por você.

**A especificação ruim**, recebida de um gerente comercial da Vetor:

> "Precisamos de um painel de relatórios de desconto pro time comercial. Ele deve ter um botão de exportar pra Excel, mostrar um gráfico de pizza com os descontos aplicados no mês, e ser bem intuitivo e moderno. Como os gerentes vão usar isso todo dia, o relatório precisa carregar rápido. Todo desconto aplicado aparece lá. Entrega até sexta, com testes completos e cobertura de 100%."

**Passo 1 — instale o entrevistador.** Cole este texto para o seu agente, numa conversa nova:

```text
Você é um entrevistador socrático de requisitos. Vou colar uma especificação
com problemas. Leia a especificação inteira antes de fazer qualquer
pergunta. Depois, procure defeitos nesta ordem de prioridade: solução
apresentada como requisito; requisito sem valor identificável (para quem,
por quê); critério subjetivo ou não testável; requisito não funcional sem
medida numérica; regra sem exceção definida; hipótese tratada como certeza,
sem evidência; contradição entre escopo, prazo e qualidade.

Regra de conduta: cada defeito vira UMA pergunta, nunca uma correção sua.
Uma pergunta por mensagem, nunca duas. Espere minha resposta antes da
próxima pergunta. Não sugira a resposta certa — meu trabalho é responder, o
seu é perguntar. Quando eu disser "fechar entrevista", produza um resumo
com os defeitos encontrados, a resposta que dei para cada um, e a
especificação reescrita incorporando minhas respostas.
```

**Passo 2 — cole a especificação ruim** (acima) e responda as perguntas do agente, uma de cada vez, como se você fosse quem escreveu o pedido original.

**Passo 3 — feche a entrevista.** Depois de pelo menos cinco perguntas respondidas, diga "fechar entrevista" e leia o resumo e a especificação reescrita.

**Passo 4 — confira contra a lista.** Quantas das sete classes de defeito da lista do passo 1 o agente encontrou sozinho? Alguma passou despercebida?

**Questões exploratórias:**

- O agente tentou corrigir a especificação sozinho em algum momento, em vez de só perguntar? Isso violou o contrato que você deu a ele?
- Das perguntas que o agente fez, qual foi a mais desconfortável de responder — e o que esse desconforto revela sobre o que a especificação original escondia?
- Compare a especificação reescrita do passo 3 com o formato BR/FR/NFR do Experimento A. Alguma regra de negócio ficou implícita na versão reescrita, do mesmo jeito que ficava na original?

## Evidência a entregar

Cinco itens, verificáveis contra o mesmo projeto de exemplo:

1. As perguntas do passo 1 do Experimento A, escritas antes de abrir as respostas.
2. A especificação BR/FR escrita no passo 3 do Experimento A, e o resultado de `node --test` no passo 5 — os seis testes originais e os casos novos.
3. O cenário de qualidade do Experimento B (os seis elementos) e a função de aptidão correspondente.
4. O resumo da entrevista socrática do Experimento C e a especificação reescrita.
5. A conferência do passo 4 do Experimento C: quantas classes de defeito o agente encontrou sozinho.

**Próxima página:** [Exercícios](exercicios.md).
