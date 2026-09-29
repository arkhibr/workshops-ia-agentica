# S4 — Regras formais com IA

**Bloco:** 2 — Especificação e Planejamento

> **Pergunta-guia:** como transformar uma regra espalhada entre prosa e código em um modelo que pessoas, agentes e testes consigam verificar?

## Problema

Uma política pode estar correta em cada frase e falhar no conjunto. Condições se sobrepõem, exceções aparecem longe da regra geral, o mesmo conceito recebe nomes diferentes e a ordem de um `CASE` decide o que nenhum documento declarou. Nesta sessão, a IA ajuda a desmontar esse emaranhado sem receber autoridade para preencher lacunas.

## Como usar este material

Estas páginas apoiam uma sessão conduzida ao vivo. O instrutor alterna explicação, demonstração e prática; não há leitura prévia obrigatória. Cada exercício termina com um artefato revisável.

## Dois temas, um contrato de saída

**Tema 1 — Regras formais com IA.** O grupo parte de prosa, separa conceitos e fatos, classifica regras estruturais e operativas, atomiza sentenças e organiza combinações em tabelas de decisão. A demonstração usa um exemplo fictício de IRPF. Os exercícios usam o cashback da nova tributação do consumo.

**Tema 2 — Arqueologia de regras.** O grupo parte de SQL, trata cada condição como evidência de comportamento implementado e recupera um catálogo SBVR com casos de teste. Não há trilhas Geral e Especialista neste tema: todos examinam o mesmo artefato.

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
4. **Gerar** casos de teste antes da implementação, seguindo TDD e mantendo vínculo com a regra de origem.
5. **Recuperar** regras de SQL legado, registrando evidência, confiança e perguntas para o domínio.

## Roteiro da sessão (2h, das 10h às 12h)

| Horário | Min | Bloco | Página |
|---|---:|---|---|
| 10:00–10:20 | 20 | Tema 1 — Modelo conceitual | [Conceitos, fatos e regras](regras-formais-conceitos.md) |
| 10:20–10:45 | 25 | Tema 1 — Demonstração do ninho de IRPF | [Exemplo: decomposição do IRPF](regras-formais-exemplo-irpf.md) |
| 10:45–11:00 | 15 | Tema 1 — Início do mapa tributário | [Exercício de IA — Geral](regras-formais-exercicio-geral.md) |
| 11:00–11:05 | 5 | Intervalo | Nenhuma |
| 11:05–11:10 | 5 | Tema 1 — Conclusão do mapa tributário | [Exercício de IA — Geral](regras-formais-exercicio-geral.md) |
| 11:10–11:30 | 20 | Tema 1 — Casos de teste em TDD | [Exercício de IA — Especialista](regras-formais-exercicio-especialista.md) |
| 11:30–11:55 | 25 | Tema 2 — Arqueologia em SQL | [Arqueologia de regras em SQL](arqueologia-de-regras-sql.md) |
| 11:55–12:00 | 5 | Síntese e autoavaliação | [Síntese e referências](sintese-e-referencias.md) |

O conteúdo soma 115 minutos. O intervalo completa os 120 minutos de relógio.

## Como conduzir

No Tema 1, esconda a decomposição do exemplo até o grupo marcar conceitos, fatos e possíveis regras. No Tema 2, peça uma primeira leitura do SQL sem IA; essa linha de base torna visível o que a ferramenta encontrou e o que ela apenas formulou melhor.

!!! warning "Limite da IA nesta sessão"
    O agente pode classificar, comparar e encontrar combinações. Quando a fonte não determina uma resposta, a saída correta é uma lacuna acompanhada de pergunta, não uma regra plausível inventada.

**Próxima página:** [Conceitos, fatos e regras](regras-formais-conceitos.md).
