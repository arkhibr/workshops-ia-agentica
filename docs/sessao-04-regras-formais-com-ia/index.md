# S4 — Regras formais com IA

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** como transformar uma regra espalhada entre prosa e código em um modelo que pessoas, agentes e testes consigam verificar?

## Problema

Uma política pode estar correta em cada frase e falhar no conjunto. Condições se sobrepõem, exceções aparecem longe da regra geral, o mesmo conceito recebe nomes diferentes e a ordem de um `CASE` decide o que nenhum documento declarou. Nesta sessão, a IA ajuda a separar conceitos, fatos, regras e exceções sem receber autoridade para preencher lacunas da fonte.

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

| Horário | Min | Bloco | Página | Produto do bloco |
|---|---:|---|---|---|
| 10:00–10:20 | 20 | Tema 1: modelo conceitual | [Conceitos, fatos e regras](regras-formais-conceitos.md) | Esquema de mapa com as cinco camadas e a convenção de IDs RC, RD e RN |
| 10:20–10:45 | 25 | Tema 1: demonstração do ninho de IRPF | [Exemplo: decomposição do IRPF](regras-formais-exemplo-irpf.md) | Ninho decomposto em glossário, regras, tabela de faixas e casos de fronteira |
| 10:45–11:00 | 15 | Tema 1: início do mapa tributário | [Exercício de IA — Geral](regras-formais-exercicio-geral.md) | Marcação inicial do texto-base e primeira saída do agente |
| 11:00–11:05 | 5 | Intervalo | Nenhuma | Nenhum |
| 11:05–11:10 | 5 | Tema 1: conclusão do mapa tributário | [Exercício de IA — Geral](regras-formais-exercicio-geral.md) | Mapa revisado, tabela de decisão e perguntas para validação jurídica |
| 11:10–11:30 | 20 | Tema 1: casos de teste em TDD | [Exercício de IA — Especialista](regras-formais-exercicio-especialista.md) | Matriz de testes rastreada e três casos verdes em `node --test` |
| 11:30–11:55 | 25 | Tema 2: arqueologia em SQL | [Arqueologia de regras em SQL](arqueologia-de-regras-sql.md) | Catálogo SBVR com linhas do SQL, tabela de decisão e matriz de testes |
| 11:55–12:00 | 5 | Síntese e autoavaliação | [Síntese e referências](sintese-e-referencias.md) | Autoavaliação e lista de lacunas levadas à Sessão 5 |

O conteúdo soma 115 minutos, e o intervalo das 11:00 às 11:05 completa os 120 minutos de relógio.

## Como conduzir

No Tema 1, esconda a decomposição do exemplo até o grupo marcar conceitos, fatos e possíveis regras. No Tema 2, peça uma primeira leitura do SQL sem IA, porque essa linha de base torna visível o que a ferramenta encontrou e o que ela apenas formulou melhor.

!!! warning "Limite da IA nesta sessão"
    O agente pode classificar, comparar e encontrar combinações, e quando a fonte não determina uma resposta a saída correta é o rótulo LACUNA acompanhado da pergunta que o especialista precisa responder.

**Próxima página:** [Conceitos, fatos e regras](regras-formais-conceitos.md).
