# S2 — O ambiente agêntico: ferramentas e fluxo

**Bloco:** 1 — Fundamentos

> **Pergunta-guia:** o que muda quando o time para de usar IA cada um do seu próprio jeito e passa a compartilhar um ambiente?

## Problema

Cada desenvolvedor configura o próprio agente à própria maneira: arquivo de instrução diferente (quando existe um), ferramentas conectadas diferentes, nenhum isolamento entre o trabalho de um agente e o resto do repositório. O que funciona na máquina de um raramente se repete na do colega ao lado.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** engenharia de prompt de engenharia de contexto, e explicar por que ferramentas são o contrato entre o agente e o ambiente.
2. **Explicar** o problema que o Model Context Protocol (MCP) resolve.
3. **Configurar**, para o próprio repositório, um arquivo de instrução compartilhado pelo time.
4. **Isolar** o trabalho de um agente por ramo, evitando que duas sessões pisem no mesmo contexto.
5. **Diagnosticar** uma falha do agente pela peça do arnês que provavelmente a causou, antes de considerar a troca de modelo.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem hoje quatro desenvolvedores usando quatro agentes configurados de quatro jeitos diferentes — nenhum arquivo de instrução compartilhado, nenhuma ferramenta conectada em comum, nenhum isolamento quando duas pessoas usam o agente ao mesmo tempo. Esta sessão organiza isso.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ambiente compartilhado](ambiente-compartilhado.md) | Teoria | 4 min | As quatro peças do ambiente e quando vale configurá-las em conjunto |
| 2 | [O arnês do agente](arnes.md) | Teoria | 11 min | A equação agente = modelo + arnês, o erro composto, os componentes e o diagnóstico por tipo de falha |
| 3 | [Engenharia de contexto](engenharia-de-contexto.md) | Teoria | 4 min | A diferença entre cuidar da instrução e cuidar da janela de contexto |
| 4 | [MCP e ferramentas externas](mcp.md) | Teoria | 8 min | O problema M×N, as três primitivas, o critério para conectar e o catálogo mínimo |
| 5 | [O arquivo de instrução](arquivo-de-instrucao.md) | Teoria | 8 min | O que colocar no AGENTS.md, como estruturá-lo e como verificá-lo |
| 6 | [Isolamento por ramo](isolamento-por-ramo.md) | Teoria | 3 min | O que o `git worktree` isola e o cuidado que ele exige |
| 7 | [Autonomia e supervisão](autonomia-e-supervisao.md) | Teoria | 4 min | Erro composto, níveis de autonomia e o critério de reversibilidade |
| 8 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 10 min | Ver, com a Vetor, o ambiente compartilhado montado do zero |
| 9 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 13 min | Julgar se um incidente de contexto cruzado justifica isolamento formal |
| — | Intervalo | — | 5 min | — |
| 10 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 30 min | Três experimentos práticos com o próprio agente do participante |
| 11 | [Exercícios](exercicios.md) | Prática avaliada | 15 min | Exercício-âncora: configurar e rodar um ciclo entrada → resposta → verificação |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As sete páginas de teoria têm caixas de destaque embutidas no texto. Pare de verdade nesses pontos, em vez de ler a pergunta e seguir em frente.

Ao chegar na oficina, todos criam o mesmo projeto vazio, `oficina-arnes`, com dois comandos (`mkdir` e `git init`), para que as saídas sejam comparáveis entre as duplas sem ninguém precisar clonar nada pronto. A transposição para o repositório real de cada um está na extensão ao fim da oficina, e é a tarefa que faz o arquivo de instrução sobreviver à aula.

**Próxima página:** [O ambiente compartilhado](ambiente-compartilhado.md).
