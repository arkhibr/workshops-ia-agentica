# Oficina de ferramentas — o ciclo SDD ponta a ponta na Vetor

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit) instalado no clone local de `exemplo/vetor`, a versão executável da Vetor, plataforma fictícia de e-commerce B2B do workshop. O agente é o já configurado pelo participante (Claude Code, Codex CLI ou Copilot). Tempo estimado: 30 minutos.

**Decisão em foco:** conduzir o ciclo com os quatro artefatos versionados e observar, na etapa de clarificação, uma ambiguidade que o pedido original escondia, antes que o agente a resolva sozinho.

O Spec Kit é instalado no clone do projeto de exemplo, nunca no repositório de trabalho do participante. A transposição para o repositório real entra na extensão, ao final.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, do pedido vago aos quatro artefatos.
- **Exploração em dupla:** Experimento B, a ambiguidade que o agente resolveria sozinho.
- **Extensão opcional:** Experimento C, transpor para o repositório do participante.

## Preparação

Todos partem do mesmo estado. Clone o projeto de exemplo e confirme que a suíte passa:

```bash
git clone https://github.com/arkhibr/workshops-ia-agentica
cd workshops-ia-agentica/exemplo/vetor
npm test
```

A saída deve mostrar os seis testes passando. A função `calcularDesconto` recebe `tipoCliente` e não usa esse parâmetro: a faixa de atacado nunca foi implementada, e é a lacuna que esta oficina fecha.

Instale o Spec Kit no diretório do projeto:

=== "macOS/Linux"

    ```bash
    uvx --from git+https://github.com/github/spec-kit.git specify init --here
    ```

=== "Windows (PowerShell)"

    ```powershell
    uvx --from git+https://github.com/github/spec-kit.git specify init --here
    ```

O comando é o mesmo nos três sistemas, desde que `uv` esteja instalado. Se a instalação falhar por ausência de `uv`, o experimento A pode ser conduzido sem a ferramenta: os quatro artefatos são arquivos Markdown, e o agente consegue produzi-los a partir da descrição de cada etapa.

## Experimento A — do pedido vago aos quatro artefatos

**Objetivo:** produzir constitution, especificação, plano e tarefas para a faixa de atacado, e observar o que cada artefato decide.

**Passo 1 — a constitution.** Peça ao agente para criar a constitution do projeto com três princípios, cada um com a consequência nomeada, sobre: regra de precificação nunca implícita no código, comportamento novo começando por teste que falha, e assinatura pública de função de cálculo mantida compatível. Confira se cada princípio é capaz de rejeitar alguma mudança plausível. Um princípio que não rejeita nada é decoração, e a hora de descobrir isso é agora.

**Passo 2 — a especificação.** Dê ao agente o pedido exatamente como ele chegaria na vida real: "ativa o desconto de atacado, 20% acima de dez mil". Peça a especificação com requisitos numerados, cada um com caso concreto e caso de fronteira. Não ofereça mais informação do que essa frase.

**Passo 3 — leia antes de seguir.** Antes de pedir o plano, leia a especificação gerada e procure a resposta para esta pergunta: o que acontece com o teto de desconto de R$ 1.000,00 que já existe no código, quando o pedido de atacado dá 20% sobre R$ 12.000,00?

**Passo 4 — o plano e as tarefas.** Depois de decidir a questão do passo 3 e registrá-la na especificação, peça o plano técnico e a decomposição em tarefas. Verifique se as tarefas são fatias verticais, cada uma com teste e definição de pronto, e não uma lista de camadas.

**Evidência a entregar:** os quatro arquivos gerados, e a linha da especificação onde a decisão sobre o teto ficou registrada.

**Questões exploratórias:**

- A especificação do passo 2 mencionou o teto por conta própria, ou ficou silenciosa sobre ele?
- O plano propôs alterar a assinatura de `calcularDesconto`? Se sim, ele registrou a exceção ao princípio 3 da constitution, ou seguiu em silêncio?

## Experimento B — a ambiguidade que o agente resolveria sozinho

**Objetivo:** medir o que teria acontecido sem a etapa de clarificação.

**Antes de começar: por que a ordem importa.** Este experimento só mede alguma coisa se rodar numa conversa nova, que não viu a decisão sobre o teto tomada no experimento A. Um agente que já leu aquela decisão vai reproduzi-la, e o experimento perde o sentido.

**Passo 1 — peça o código direto.** Abra uma conversa nova. Dê o arquivo `src/desconto.js` e o mesmo pedido original, sem especificação nenhuma: "ativa o desconto de atacado, 20% acima de dez mil". Peça a implementação e os testes.

**Passo 2 — inspecione a escolha.** Rode `npm test` e depois leia o código gerado. Para um pedido de R$ 12.000,00 de cliente atacado, qual valor a função devolve: R$ 2.400,00, ou R$ 1.000,00 por causa do teto?

**Passo 3 — confronte.** Qualquer que tenha sido a escolha, ela foi registrada em algum lugar? O teste que o agente escreveu documenta a decisão como deliberada, ou apenas congela o comportamento que saiu?

**Questões exploratórias:**

- A escolha do agente coincidiu com a decisão que a sua dupla tomou no experimento A? Se coincidiu, isso valida a decisão, ou é coincidência?
- Um revisor que recebesse apenas esse código e esses testes teria como perceber que uma decisão financeira foi tomada ali?

## Experimento C — transpor para o seu repositório

**Objetivo:** avaliar o custo real de adoção fora do exemplo controlado.

Escolha uma mudança pequena e real do seu backlog, de classe S ou M pela régua de profundidade. Escreva apenas a especificação, com dois requisitos numerados e seus casos de fronteira. Não implemente nada.

Meça duas coisas: quanto tempo levou, e quantas perguntas você precisou fazer a outra pessoa para conseguir escrever os casos de fronteira. A segunda medida é a mais informativa: ela estima quanto conhecimento do seu domínio hoje não está escrito em lugar nenhum.

**Questões exploratórias:**

- Das perguntas que você precisou fazer, quantas teriam sido respondidas por suposição se um agente estivesse implementando direto?
- Para essa mudança específica, o contrato completo compensa, ou bastaria problema, limite, teste e evidência?

## Evidência a entregar

Ao final da oficina, cada dupla entrega os quatro artefatos do experimento A e uma frase respondendo: qual decisão o ciclo tornou explícita que o caminho direto do experimento B teria deixado implícita?

**Próxima página:** [Exercícios](exercicios.md).
