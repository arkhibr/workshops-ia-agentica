# S2 — O ambiente agêntico: ferramentas e fluxo

**Bloco:** 1 — Fundamentos

> **Pergunta-guia:** o que muda quando o time para de usar IA cada um do seu próprio jeito e passa a compartilhar um ambiente?

## Problema

Cada desenvolvedor configura o próprio agente à própria maneira: arquivo de instrução diferente (quando existe um), ferramentas conectadas diferentes, nenhum isolamento entre o trabalho de um agente e o resto do repositório. O que funciona na máquina de um raramente se repete na do colega ao lado.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Distinguir** prompt engineering de context engineering, e explicar por que ferramentas são o contrato entre o agente e o ambiente.
2. **Explicar** o problema que o Model Context Protocol (MCP) resolve.
3. **Configurar**, para o próprio repositório, um arquivo de instrução compartilhado pelo time.
4. **Isolar** o trabalho de um agente por ramo, evitando que duas sessões pisem no mesmo contexto.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B introduzida na Sessão 1, tem hoje quatro desenvolvedores usando quatro agentes configurados de quatro jeitos diferentes — nenhum arquivo de instrução compartilhado, nenhuma ferramenta conectada em comum, nenhum isolamento quando duas pessoas usam o agente ao mesmo tempo. Esta sessão organiza isso.

## Roteiro da sessão (2h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ambiente compartilhado](ambiente-compartilhado.md) | Teoria | 7 min | As quatro peças do ambiente e quando vale configurá-las em conjunto |
| 2 | [Context engineering](context-engineering.md) | Teoria | 6 min | A diferença entre cuidar da instrução e cuidar da janela de contexto |
| 3 | [MCP e ferramentas externas](mcp.md) | Teoria | 10 min | O problema M×N, as três primitivas e o critério para conectar um servidor |
| 4 | [O arquivo de instrução](arquivo-de-instrucao.md) | Teoria | 11 min | O que colocar no AGENTS.md, como estruturá-lo e como verificá-lo |
| 5 | [Isolamento por ramo](isolamento-por-ramo.md) | Teoria | 5 min | O que o `git worktree` isola e o cuidado que ele exige |
| 6 | [Autonomia e supervisão](autonomia-e-supervisao.md) | Teoria | 6 min | Níveis de autonomia e o critério de reversibilidade para liberar cada um |
| 7 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 10 min | Ver, com a Vetor, o ambiente compartilhado montado do zero |
| 8 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 15 min | Julgar se um incidente de contexto cruzado justifica isolamento formal |
| 9 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 30 min | Três experimentos práticos com o próprio agente do participante |
| 10 | [Exercícios](exercicios.md) | Prática avaliada | 15 min | Exercício-âncora: configurar e rodar um ciclo entrada → resposta → verificação |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As seis páginas de teoria têm caixas de destaque embutidas no texto. Pare de verdade nesses pontos, em vez de ler a pergunta e seguir em frente.

Ao chegar na oficina, cada participante deve usar o próprio repositório real (ou um repositório de teste), não um exemplo genérico — o objetivo é que o arquivo de instrução configurado hoje continue existindo depois da sessão.

**Próxima página:** [O ambiente compartilhado](ambiente-compartilhado.md).
