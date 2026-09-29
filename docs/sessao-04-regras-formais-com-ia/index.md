# S4 — Regras formais com IA

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** como transformar uma regra espalhada entre prosa e código em um modelo que pessoas, agentes e testes consigam verificar?

## Problema

Uma política com todas as frases corretas pode produzir resultados incompatíveis quando as frases são combinadas, porque condições se sobrepõem, exceções aparecem longe da regra geral, o mesmo conceito recebe nomes diferentes e a ordem de um `CASE` decide o que nenhum documento declarou. Nesta sessão, a IA ajuda a separar conceitos, fatos, regras e exceções sem receber autoridade para preencher lacunas da fonte.

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo, sem leitura prévia obrigatória, em que o instrutor alterna explicação, demonstração e prática, e cada exercício termina com um artefato revisável.

## Os dois temas e o contrato de saída

**Tema 1 — Regras formais com IA.** O grupo usa o SBVR (*Semantics of Business Vocabulary and Business Rules*, padrão da OMG para vocabulário e regras de negócio), parte de prosa, separa conceitos e fatos, classifica regras estruturais e operativas, atomiza sentenças e organiza combinações em tabelas de decisão, que dispõem em linhas as condições e o resultado de cada combinação. A demonstração usa um exemplo fictício de IRPF. Os exercícios usam o cashback do IBS e da CBS, previsto nos arts. 112, 113, 116, 117, 118 e 124 da Lei Complementar nº 214/2025.

**Tema 2 — Arqueologia de regras.** A arqueologia de regras recupera decisões de negócio já incorporadas a um sistema. O grupo parte de SQL, trata cada condição como evidência de comportamento implementado e recupera um catálogo SBVR com casos de teste. Neste tema todos os participantes examinam o mesmo artefato, sem divisão entre trilhas Geral e Especialista.

| Camada | Pergunta |
|---|---|
| Conceitos | Quais substantivos do domínio precisam de definição? |
| Fatos | Como esses conceitos se relacionam? |
| Regras estruturais | O que é classificado ou derivado? |
| Regras operativas | O que é obrigatório, proibido ou permitido sob condição? |
| Controle | Quais exceções, conflitos, lacunas, evidências e níveis de confiança existem? |

## Objetivos de aprendizagem

Ao final da sessão, o participante será capaz de:

1. **Distinguir** conceitos, fatos, regras estruturais e regras operativas no vocabulário do SBVR.
2. **Decompor** um ninho de regras em sentenças atômicas e rastreáveis.
3. **Organizar** combinações em uma tabela de decisão com política de acerto explícita.
4. **Gerar** casos de teste antes da implementação, seguindo TDD (*Test-Driven Development*, em que o teste é escrito antes do código) e mantendo vínculo com a regra de origem.
5. **Recuperar** regras de SQL legado, registrando evidência, confiança e perguntas para o domínio.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Trilha | Página | Produto do bloco |
|---|---:|---|---|---|---|
| 10:00–10:16 | 16 | Tema 1 — Conceitos | Comum | [Conceitos, fatos e regras](regras-formais-conceitos.md) | Esquema de mapa com as cinco camadas e a convenção de IDs RC, RD e RN |
| 10:16–10:28 | 12 | Tema 1 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](regras-formais-exemplo-de-aplicacao-de-ia.md) | Ninho decomposto em glossário, regras, tabela de faixas e casos de fronteira |
| 10:28–11:00 | 32 | Tema 1 — Exercício | Geral | [Exercício de IA — Geral](regras-formais-exercicio-geral.md) | Mapa revisado, tabela de decisão e perguntas para validação jurídica |
| 10:28–11:00 | 32 | Tema 1 — Exercício | Especialista | [Exercício de IA — Especialista](regras-formais-exercicio-especialista.md) | Matriz de testes rastreada e três casos verdes em `node --test` |
| 11:00–11:05 | 5 | Intervalo | Todos | Nenhuma | Nenhum |
| 11:05–11:20 | 15 | Tema 2 — Conceitos | Comum | [Conceitos: arqueologia de regras](arqueologia-de-regras-conceitos.md) | Método de seis movimentos e taxonomia de tipos de evidência para arqueologia de regras |
| 11:20–11:33 | 13 | Tema 2 — Exemplo de aplicação de IA | Comum | [Exemplo de aplicação de IA](arqueologia-de-regras-exemplo-de-aplicacao-de-ia.md) | Catálogo SBVR do método C# com evidência por linha e correções do instrutor |
| 11:33–11:55 | 22 | Tema 2 — Exercício | Comum | [Exercício de IA: arqueologia de regras em SQL](arqueologia-de-regras-exercicio.md) | Catálogo SBVR com linhas do SQL, tabela de decisão e matriz de testes |
| 11:55–12:00 | 5 | Síntese e autoavaliação | Comum | [Síntese e referências](sintese-e-referencias.md) | Autoavaliação e lista de lacunas levadas à Sessão 5 |

O conteúdo soma 115 minutos, e o intervalo das 11:00 às 11:05 completa os 120 minutos de relógio.

## Como conduzir

No Tema 1, esconda a decomposição do exemplo até o grupo marcar conceitos, fatos e possíveis regras, e explique as duas trilhas paralelas do exercício antes de liberar o grupo. A trilha geral verifica o mapa por revisão por camada e conferência manual, sem terminal, e a trilha especialista monta o projeto a partir dos blocos de código da própria página e conclui com os casos de teste em TDD. No Tema 2, siga a sequência de conceitos, exemplo e exercício: apresente o método de seis movimentos, conduza a demonstração sobre o método C# legado e só então peça ao grupo uma primeira leitura do SQL sem IA, porque essa linha de base torna visível o que a ferramenta encontrou e o que ela apenas formulou melhor.

!!! warning "Limite da IA nesta sessão"
    O agente pode classificar, comparar e encontrar combinações, e quando a fonte não determina uma resposta a saída correta é o rótulo LACUNA acompanhado da pergunta que o especialista precisa responder.

**Próxima página:** [Conceitos, fatos e regras](regras-formais-conceitos.md).
