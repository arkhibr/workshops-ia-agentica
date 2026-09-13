# Atributos de qualidade e RAS

"O sistema deve ser rápido" é um adjetivo esperando virar requisito não funcional. Esta página dá o vocabulário para nomear o atributo de qualidade certo, o critério para saber quando ele importa o bastante para virar decisão de arquitetura (o que abrevia como RAS, requisito arquiteturalmente significativo), e a forma de escrever um NFR que continua sendo verificado depois que todo mundo esqueceu de tê-lo escrito.

## Catálogo de atributos de qualidade

Um NFR solto começa quase sempre com um adjetivo: rápido, seguro, escalável, confiável. O primeiro passo é trocar o adjetivo por um atributo de qualidade nomeado, porque cada atributo tem sua própria forma de ser medido:

| Atributo | Pergunta que ele responde | Como se mede |
|---|---|---|
| Desempenho | Quão rápido, sob que carga? | Latência, vazão, tempo de resposta em percentil |
| Segurança | Que acesso é permitido, a quem, sob que condição? | Casos de autorização testados, superfície de ataque |
| Confiabilidade | O que acontece quando algo falha? | Taxa de erro tolerada, tempo de recuperação |
| Modificabilidade | Quão caro é mudar isso depois? | Número de módulos tocados por uma mudança típica |
| Observabilidade | Dá para saber o que o sistema fez, depois do fato? | Cobertura de log e rastro por decisão crítica |
| Usabilidade | Uma pessoa nova consegue operar sem ajuda? | Taxa de erro do usuário, tempo até a primeira tarefa |
| Custo | Quanto custa operar isso, e em que escala? | Custo por transação, por usuário, por mês |

"Rápido" não escolhe uma linha da tabela sozinho. Quem escreve o requisito é que precisa decidir se a preocupação real é desempenho (tempo de resposta), custo (processamento caro) ou os dois ao mesmo tempo, e cada escolha muda a forma da medida.

!!! question "Antes de continuar"
    Pegue um NFR vago que você já recebeu ("o sistema deve ser seguro"). Qual atributo da tabela ele está tentando nomear, e que medida corresponderia a esse atributo?

## Requisito arquiteturalmente significativo (RAS)

Nem todo requisito não funcional exige uma decisão de arquitetura. Um requisito vira **arquiteturalmente significativo** quando atende a pelo menos um destes critérios:

- Atravessa mais de um componente do sistema, em vez de ficar contido numa única função.
- Protege um atributo de qualidade que o negócio já declarou prioritário.
- Cria uma dependência relevante — de outro serviço, de um fornecedor externo, de um formato de dado.
- Torna uma mudança futura mais cara, porque a decisão de hoje molda o que amanhã pode ou não ser trocado sem reescrever tudo.

"O relatório mostra até duas casas decimais" é um NFR real, mas não é arquiteturalmente significativo: fica contido numa função de formatação, não força nenhuma escolha estrutural. "O cálculo de desconto responde em menos de 100ms mesmo com 500 pedidos simultâneos" já é: atravessa a função de cálculo e o que quer que a chame, protege desempenho sob carga, e pode forçar decisões de cache ou de arquitetura de concorrência que uma função isolada não resolveria sozinha.

## Cenário de qualidade

[Bass, Clements e Kazman](../referencia/bibliografia.md#bass-clements-e-kazman-software-architecture-in-practice-2021) formalizam o template que torna um NFR testável, o cenário de qualidade (*quality attribute scenario*). Um NFR verificável descreve seis elementos, em vez de um número solto:

| Elemento | Pergunta | Exemplo genérico |
|---|---|---|
| Fonte | Quem ou o que provoca o estímulo? | Um pico de tráfego no checkout |
| Estímulo | O que acontece? | 500 pedidos chegam no mesmo segundo |
| Ambiente | Sob que condição do sistema? | Em operação normal, sem degradação prévia |
| Artefato | O que é afetado? | A função de cálculo de desconto |
| Resposta | O que o sistema faz? | Calcula o desconto de cada pedido sem enfileirar |
| Medida | Como se mede se a resposta foi aceitável? | 95% das respostas em menos de 100ms |

Escrever os seis elementos, mesmo em uma frase corrida, é o que separa "o sistema deve ser rápido" de um requisito que um agente consegue implementar e alguém consegue testar sem adivinhar o resto.

## Função de aptidão arquitetural (fitness function)

Escrever um NFR verificável não garante que ele continue verdadeiro depois que o sistema muda. [Ford, Parsons, Kua e Sadalage](../referencia/bibliografia.md#ford-parsons-kua-e-sadalage-building-evolutionary-architectures-2023) definem **função de aptidão arquitetural** como "uma avaliação objetiva de integridade de alguma característica arquitetural". Na prática, é um teste automatizado que roda toda vez que o código muda, em vez de uma revisão manual esporádica. Para fins de verificação prática, este workshop declara três elementos em cada função de aptidão:

- **Limiar**: o valor que separa aceitável de inaceitável (o mesmo da medida do cenário de qualidade).
- **Responsável**: quem é avisado quando o limiar é ultrapassado.
- **Reação**: o que acontece quando a função de aptidão falha, seja bloquear a promoção, abrir um alerta ou reduzir a exposição.

Para o cenário de desempenho acima, a função de aptidão poderia ser um teste de carga que roda na esteira de integração contínua, com limiar de 100ms no percentil 95, responsável definido (o time que mantém o cálculo de desconto) e reação declarada (bloquear o deploy se o limiar for ultrapassado).

## O antipadrão do NFR sem função de aptidão

Um NFR escrito e nunca mais verificado é só uma promessa. O sintoma: alguém escreve "o sistema deve responder em menos de 100ms" na especificação, o código passa no teste manual do dia em que foi escrito, e ninguém percebe quando uma mudança seis meses depois faz a resposta subir para 400ms. Não existe verificação automatizada rodando a cada mudança, só a memória de que "isso já foi rápido uma vez". A função de aptidão é o que transforma o NFR de uma frase na especificação em uma condição que continua sendo cobrada do sistema a cada mudança.

!!! tip "Aplique agora"
    Pegue o cenário de qualidade que você escreveu no exercício anterior. Descreva a função de aptidão correspondente: que teste automatizado provaria, hoje e daqui a seis meses, que o cenário continua verdadeiro? Quem seria avisado se ele parasse de ser?

## Isso vira código assim

O cenário de qualidade da tabela acima (500 pedidos, 95% abaixo de 100ms) vira uma função de aptidão executável, em vez de uma frase revisada de vez em quando:

```javascript
// test/desconto.fitness.test.js
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { calcularDesconto } from '../src/desconto.js';

const LIMIAR_MS = 100;
const AMOSTRAS = 500;

test('fitness function: percentil 95 abaixo do limiar', () => {
  const tempos = [];
  for (let i = 0; i < AMOSTRAS; i += 1) {
    const inicio = performance.now();
    calcularDesconto(12000, 'atacado');
    tempos.push(performance.now() - inicio);
  }
  tempos.sort((a, b) => a - b);
  const p95 = tempos[Math.floor(AMOSTRAS * 0.95)];
  assert.ok(p95 < LIMIAR_MS, `p95 foi ${p95}ms, limiar é ${LIMIAR_MS}ms`);
});
```

Os três elementos declarados nesta página aparecem em pontos distintos:

- O **limiar** é a constante `LIMIAR_MS`.
- O **responsável** fica na configuração da esteira de integração contínua, com o `CODEOWNERS` apontando quem revisa falha nesse arquivo.
- A **reação** é o que o `pipeline.yml` faz quando `node --test` retorna falha, normalmente bloquear o merge.

Um NFR escrito só em prosa não tem nenhum dos três. O teste acima tem os três e roda de novo a cada mudança no código.

**Próxima página:** [Perguntas que revelam ambiguidade](elicitacao-e-perguntas.md).
