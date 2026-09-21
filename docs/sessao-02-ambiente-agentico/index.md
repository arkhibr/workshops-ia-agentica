# S2 — O ambiente agêntico

**Bloco:** 1 — Fundamentos

> **Pergunta-guia:** o que muda quando o time para de usar IA cada um do seu próprio jeito e passa a compartilhar um ambiente?

## Problema

Cada desenvolvedor configura o próprio agente do próprio jeito: arquivo de instrução diferente, quando existe um, ferramentas conectadas diferentes, e nenhum isolamento entre o trabalho de um agente e o resto do repositório. O que funciona na máquina de um raramente se repete na do colega ao lado.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** engenharia de prompt de engenharia de contexto, e explicar por que ferramentas são o contrato entre o agente e o ambiente.
2. **Explicar** o problema que o Model Context Protocol (MCP) resolve.
3. **Configurar**, para o próprio repositório, um arquivo de instrução compartilhado pelo time.
4. **Isolar** o trabalho de um agente por ramo, evitando que duas sessões pisem no mesmo contexto.
5. **Diagnosticar** uma falha do agente pela peça do arnês que provavelmente a causou, antes de considerar a troca de modelo.

## A Vetor

A Vetor é uma empresa fictícia de e-commerce B2B, usada nos exemplos deste workshop e apresentada na Sessão 1. Hoje ela tem quatro desenvolvedores usando quatro agentes configurados de quatro jeitos. Nenhum arquivo de instrução em comum, nenhuma ferramenta conectada em comum, e nenhum isolamento quando duas pessoas usam o agente ao mesmo tempo. Esta sessão organiza isso.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ambiente compartilhado](ambiente-compartilhado.md) | Teoria | 4 min | As quatro peças do ambiente e quando vale configurá-las em conjunto |
| 2 | [O arnês do agente](arnes.md) | Teoria | 11 min | A equação agente = modelo + arnês, o erro composto, os componentes e o diagnóstico por tipo de falha |
| 3 | [Engenharia de contexto](engenharia-de-contexto.md) | Teoria | 4 min | A diferença entre cuidar da instrução e cuidar da janela de contexto |
| 4 | [MCP e ferramentas externas](mcp.md) | Teoria | 7 min | O problema M×N, as três primitivas, o critério para conectar e o catálogo mínimo |
| 5 | [O arquivo de instrução](arquivo-de-instrucao.md) | Teoria | 8 min | O que colocar no AGENTS.md, como estruturá-lo e como verificá-lo |
| 6 | [Isolamento por ramo](isolamento-por-ramo.md) | Teoria | 2 min | O que o `git worktree` isola e o cuidado que ele exige |
| 7 | [Autonomia e supervisão](autonomia-e-supervisao.md) | Teoria | 3 min | Erro composto, níveis de autonomia e o critério de reversibilidade |
| 8 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 8 min | Ver, com a Vetor, o ambiente compartilhado montado do zero |
| 9 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 8 min | Julgar se um incidente de contexto cruzado justifica isolamento formal |
| — | Intervalo | — | 5 min | — |
| 10 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 45 min | O mesmo fechamento em planilha rodado cinco vezes, com uma peça de arnês a mais por vez |
| 11 | [Exercícios](exercicios.md) | Prática avaliada | 10 min | Exercício-âncora: rodar um ciclo entrada → resposta → verificação sobre o fechamento |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As sete páginas de teoria têm caixas de destaque embutidas no texto. Pare nesses pontos e espere a turma responder, em vez de ler a pergunta e seguir em frente.

Na oficina, todos criam a mesma pasta vazia, `oficina-arnes`, com dois comandos (`mkdir` e `git init`), e salvam nela o mesmo arquivo de 22 pedidos. Daí em diante cada participante faz o mesmo pedido de fechamento cinco vezes, acrescentando uma peça de arnês por rodada e conferindo contra um gabarito publicado na página. A transposição para um repositório real fica na extensão ao fim da página, e é o que mantém o arquivo de instrução em uso depois da aula.

**Próxima página:** [O ambiente compartilhado](ambiente-compartilhado.md).
