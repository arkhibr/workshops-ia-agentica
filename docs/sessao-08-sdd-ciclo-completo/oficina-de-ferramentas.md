# Oficina de ferramentas

Três experimentos levam o participante pelo ciclo SDD ponta a ponta, da instalação do Spec Kit num projeto vazio até o código verificado com os quatro artefatos versionados.

**Objetivo Bloom:** Aplicar.

## Ferramenta

Esta oficina usa o [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit), o agente de codificação já configurado pelo participante (**Claude Code, Codex CLI ou Copilot**), o git e o Node.js 20 ou superior. Tempo estimado: 30 minutos.

Todos os experimentos partem de um **projeto vazio**, criado durante a própria oficina. Ninguém clona nada pronto: cada pessoa monta o mesmo estado inicial com os comandos abaixo.

**Decisão em foco:** rodar o ciclo completo e observar, na etapa de clarificação, uma ambiguidade que o pedido original escondia, antes que o agente a resolva sozinho.

## Roteiro sugerido para a sessão

- **Essencial em aula:** Experimento A, o ciclo completo comando a comando.
- **Exploração em dupla:** Experimento B, o que o agente decide quando ninguém pergunta.
- **Extensão opcional:** Experimento C, transpor para o repositório do participante.

## Preparação

**Passo 1. Crie o projeto vazio.**

```bash
mkdir oficina-sdd && cd oficina-sdd
git init
node --version   # precisa mostrar v20 ou superior
```

**Passo 2. Crie o código inicial.** Salve como `src/desconto.js`, usando o seu editor:

```javascript
export const TETO_DESCONTO = 1000;

export function calcularDesconto(valorTotal, tipoCliente) {
  let percentual = 0;
  if (valorTotal > 5000) percentual = 0.15;
  else if (valorTotal > 2000) percentual = 0.1;
  else if (valorTotal > 500) percentual = 0.05;

  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
```

Repare em duas coisas antes de seguir. O parâmetro `tipoCliente` é recebido e nunca usado: a faixa de atacado nunca foi implementada, e é a lacuna que esta oficina fecha. E o `Math.min` aplica um teto de R$ 1.000,00 a todas as faixas.

**Passo 3. Crie o teste e confirme o estado inicial.** Salve como `test/desconto.test.js`:

```javascript
import { test } from 'node:test';
import assert from 'node:assert';
import { calcularDesconto } from '../src/desconto.js';

test('nao da desconto ate 500', () => {
  assert.equal(calcularDesconto(500, 'padrao'), 0);
});

test('da 10% na faixa de 2.000,01 a 5.000,00', () => {
  assert.equal(calcularDesconto(3000, 'padrao'), 300);
});

test('respeita o teto de 1.000', () => {
  assert.equal(calcularDesconto(50000, 'padrao'), 1000);
});
```

Declare o projeto como módulo e rode:

```bash
npm init -y
npm pkg set type=module
npm pkg set scripts.test="node --test"
npm test
```

Os três testes precisam passar antes de você continuar. Faça o primeiro commit, porque o ciclo vai comparar estados:

```bash
git add -A && git commit -m "estado inicial da Vetor"
```

## Experimento A

**Objetivo:** produzir os quatro artefatos e o código, observando a saída de cada comando.

A Vetor é a plataforma fictícia de e-commerce B2B do workshop. O pedido que chega é o de sempre: "ativa o desconto de atacado, 20% acima de dez mil".

### A.1 Instalar o Spec Kit no projeto

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --integration claude
```

Troque `claude` pela sua ferramenta (`copilot`, `codex`, `cursor`). Se o diretório não estiver vazio, acrescente `--force`.

**Saída esperada.** Um painel "Next Steps" listando os comandos instalados, seguido de um painel "Enhancement Skills" com os opcionais. Leia essa lista com atenção: **é ela que diz o nome exato dos comandos na sua versão**.

**Consideração.** O nome dos comandos varia por versão e por integração. A versão 1.0.1 com integração `claude` instala habilidades com hífen (`/speckit-constitution`), enquanto a documentação no GitHub usa ponto (`/speckit.constitution`). Use o que o painel imprimiu, não o que está escrito aqui ou no README. Se digitar o separador errado, o agente responde como se fosse texto comum e o ciclo não começa.

**O que foi criado.** Confira com `find .specify .claude -type d`:

```text
.specify/memory/          constitution.md, ainda com marcadores de template
.specify/templates/       spec-template.md, plan-template.md, tasks-template.md
.specify/scripts/bash/    create-new-feature.sh, setup-plan.sh, setup-tasks.sh
.claude/skills/           uma pasta por comando, cada uma com SKILL.md
```

Os scripts em `.specify/scripts/` são o que os comandos chamam por baixo. Vale abrir um deles depois da oficina: o ciclo se resume a um script que cria pastas mais um prompt estruturado.

### A.2 `/speckit-constitution`

No agente, com o projeto aberto:

```text
/speckit-constitution Escreva três princípios. Primeiro, regra de precificação
nunca fica implícita no código. Segundo, comportamento novo começa por um teste
que falha pelo motivo esperado. Terceiro, função pública de cálculo mantém
assinatura compatível. Cada princípio precisa declarar a consequência de violá-lo.
```

**Saída esperada.** O arquivo `.specify/memory/constitution.md` deixa de ter marcadores como `[PRINCIPLE_1_NAME]` e passa a conter os princípios redigidos, com versão e data.

**Consideração.** Leia o que saiu antes de seguir. O teste é se cada princípio consegue rejeitar uma mudança plausível. "Mantém assinatura compatível" rejeita a proposta de trocar os parâmetros por um objeto de configuração, que é justamente o que o agente costuma sugerir mais adiante. Um princípio que não rejeita nada é decoração, e a hora de descobrir isso é agora, antes do portão de arquitetura.

### A.3 `/speckit-specify`

```text
/speckit-specify Clientes do tipo atacado recebem 20% de desconto em pedidos
acima de R$ 10.000,00. As faixas atuais continuam valendo para clientes padrão.
```

**Saída esperada.** O comando chama `create-new-feature.sh`, que responde em JSON e cria a pasta da funcionalidade:

```json
{"BRANCH_NAME":"001-faixa-desconto-atacado",
 "SPEC_FILE":".../specs/001-faixa-desconto-atacado/spec.md",
 "FEATURE_NUM":"001"}
```

O arquivo `specs/001-faixa-desconto-atacado/spec.md` nasce do template e é preenchido pelo agente com as seções obrigatórias: *User Scenarios & Testing*, *Requirements* (com requisitos numerados `FR-001`, `FR-002`), *Success Criteria* e *Assumptions*.

**Consideração.** O número `001` vem da contagem de pastas em `specs/`, não do git. O script também sugere `export SPECIFY_FEATURE=001-faixa-desconto-atacado`, que fixa em qual funcionalidade os próximos comandos vão operar. Em repositório sem ramo por funcionalidade, definir essa variável evita que o comando seguinte trabalhe na funcionalidade errada.

Abra o `spec.md` e procure a seção *Assumptions*. É lá que o agente registra o que ele assumiu por conta própria, e é a seção mais informativa do arquivo inteiro nesta etapa.

### A.4 `/speckit-clarify`

```text
/speckit-clarify
```

**Saída esperada.** O agente faz até cinco perguntas dirigidas, uma por vez, e grava as respostas de volta no `spec.md`, numa seção de esclarecimentos.

**Consideração, e é o ponto central da oficina.** Uma das perguntas deve tocar no teto de R$ 1.000,00. Vinte por cento de um pedido de R$ 12.000,00 são R$ 2.400,00, e o código existente limita qualquer desconto a R$ 1.000,00. O pedido original não disse nada sobre isso, e há três saídas defensáveis:

1. O teto continua valendo, e o desconto de atacado fica limitado a R$ 1.000,00. Nesse caso a faixa de 20% quase nunca difere da de 15%, e o pedido perde o sentido prático.
2. O teto não se aplica ao atacado. Precisa ser dito, porque muda o risco financeiro por pedido.
3. O teto sobe para o atacado, com um valor novo que alguém precisa decidir.

Escolha uma e registre o motivo. Se o agente **não** perguntar sobre o teto, pergunte você: "o teto de R$ 1.000,00 se aplica à nova faixa de atacado?". Anote se ele perguntou sozinho ou se foi preciso provocar, porque essa diferença é o resultado do experimento B.

### A.5 `/speckit-plan`

```text
/speckit-plan O projeto é JavaScript com Node 20, testes com node:test,
sem dependências externas.
```

**Saída esperada.** `specs/001-faixa-desconto-atacado/plan.md`, criado a partir do template, com as seções *Technical Context*, *Constitution Check* e *Project Structure*. Conforme o caso, o agente também gera documentos auxiliares de design na mesma pasta.

**Consideração.** A seção *Constitution Check* é o portão. Confira se ela cita os princípios que você escreveu em A.2 e se declara conformidade item a item. Se o plano propõe alterar a assinatura de `calcularDesconto` e o *Constitution Check* passa mesmo assim, o portão não está funcionando: o agente aprovou a si mesmo. Esse é o antipadrão da aprovação automática acontecendo na sua frente.

### A.6 `/speckit-tasks`

```text
/speckit-tasks
```

**Saída esperada.** `specs/001-faixa-desconto-atacado/tasks.md`, organizado em fases (*Setup*, *Foundational*, uma fase por história de usuário, e *Polish*), com identificadores, marcação de paralelismo e ordem de dependência.

**Consideração.** Verifique se as tarefas são fatias verticais. "Criar a tabela de faixas" é horizontal, porque ninguém consegue demonstrar comportamento novo ao final dela. "Atacado acima de R$ 10.000,00 recebe 20%, com teste de fronteira em R$ 10.000,00 exato" é vertical. O template do Spec Kit marca os blocos de teste como opcionais, com o rótulo *only if tests requested*: se a sua constitution exige teste primeiro, confira se as tarefas de teste estão lá mesmo assim.

### A.7 `/speckit-analyze` (opcional, mas rode)

```text
/speckit-analyze
```

**Saída esperada.** Um relatório de consistência entre `spec.md`, `plan.md` e `tasks.md`, apontando requisito sem tarefa, tarefa sem requisito e divergência entre artefatos. O comando não altera arquivos.

**Consideração.** Um relatório limpo prova coerência interna e nada mais. Se a decisão do teto ficou errada em A.4, os três artefatos vão concordar entre si e o relatório vai passar. Coerência entre artefatos e correspondência com a necessidade real são verificações diferentes, e só a segunda depende de alguém que conheça o negócio.

### A.8 `/speckit-implement`

```text
/speckit-implement
```

**Saída esperada.** O agente percorre `tasks.md`, escreve código e testes e marca as tarefas concluídas.

**Consideração.** Rode `git diff` e `npm test` antes de aceitar. Duas conferências valem mais que as outras: os três testes originais continuam passando, e o teste novo da faixa de atacado reflete a decisão que **você** registrou em A.4, não outra. Se o seu registro disse que o teto não se aplica ao atacado, o teste precisa esperar `2400` para um pedido de R$ 12.000,00.

**Evidência a entregar:** o `constitution.md`, os três arquivos em `specs/001-.../`, a saída de `npm test` e o `git diff` final.

## Experimento B

**Objetivo:** medir o que teria acontecido sem a etapa de clarificação.

**Antes de começar: a ordem importa.** Este experimento só mede alguma coisa numa conversa nova, que não viu a decisão sobre o teto tomada no experimento A. Um agente que já leu aquela decisão vai reproduzi-la.

**Passo 1. Peça o código direto.** Abra uma conversa nova. Cole o conteúdo original de `src/desconto.js` e o mesmo pedido, sem especificação nenhuma: "ativa o desconto de atacado, 20% acima de dez mil". Peça a implementação e os testes.

**Passo 2. Inspecione a escolha.** Para um pedido de R$ 12.000,00 de cliente atacado, qual valor a função devolve: R$ 2.400,00, ou R$ 1.000,00 por causa do teto?

**Passo 3. Confronte.** A escolha foi registrada em algum lugar? O teste que o agente escreveu documenta a decisão como deliberada, ou apenas congela o comportamento que saiu?

**Questões exploratórias:**

- A escolha do agente coincidiu com a decisão da sua dupla no experimento A? Se coincidiu, isso valida a decisão, ou é coincidência?
- Um revisor que recebesse só esse código e esses testes teria como perceber que uma decisão financeira foi tomada ali?

## Experimento C

**Objetivo:** avaliar o custo real de adoção fora do exemplo controlado.

Escolha uma mudança pequena e real do seu backlog, de classe S ou M pela régua de profundidade. Escreva apenas a especificação, com dois requisitos numerados e seus casos de fronteira. Não implemente nada.

Meça duas coisas: quanto tempo levou, e quantas perguntas você precisou fazer a outra pessoa para conseguir escrever os casos de fronteira. A segunda medida estima quanto conhecimento do seu domínio hoje não está escrito em lugar nenhum.

**Questões exploratórias:**

- Das perguntas que você precisou fazer, quantas teriam sido respondidas por suposição se um agente estivesse implementando direto?
- Para essa mudança, o contrato completo compensa, ou bastaria problema, limite, teste e evidência?

## Evidência a entregar

Ao final, cada dupla entrega os artefatos do experimento A e uma frase respondendo: qual decisão o ciclo tornou explícita que o caminho direto do experimento B teria deixado implícita?

**Próxima página:** [Exercícios](exercicios.md).
