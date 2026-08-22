# Síntese e referências

## Seis ideias essenciais

1. **Vibe coding, assistência de codificação e SDD são famílias de risco, não degraus de maturidade.** A escolha depende da tarefa, não de uma régua de "quão avançado" o time está.
2. **Um prompt funciona como programa porque o modelo aprende em contexto**, sem ajuste de peso — mecanismo empírico demonstrado por Brown et al. (2020).
3. **A janela de contexto é o programa.** O que não está escrito explicitamente no pedido não existe para o agente, por mais óbvio que pareça para quem escreveu.
4. **Um agente se distingue de um chat pelo ciclo de raciocínio e ação** (Yao et al., ReAct), não pelo tamanho do modelo.
5. **Piso, teto e julgamento humano sobem em ritmos diferentes.** Confundir "o código roda" com "o código está correto" é o erro mais caro e mais comum.
6. **A diferença entre um prompt intuitivo e um estruturado quase nunca está no modelo.** Está em quem já tinha feito, antes de escrever o pedido, o trabalho de reunir a regra de negócio inteira.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue nomear os três modos de trabalho e o artefato que cada um governa.
- [ ] Cada participante rodou os dois prompts do exercício-âncora e testou os cinco casos contra as duas saídas.
- [ ] O grupo discutiu o Estudo de caso e chegou a um critério (não a uma opinião) para quando SDD se justifica.
- [ ] Ninguém saiu achando que "o modelo errou" quando, na verdade, o prompt não continha a regra.

## Autoavaliação

1. Consigo explicar a diferença entre vibe coding e assistência de codificação usando o artefato que cada um governa, não só "um é mais cuidadoso"?
2. Sei dizer por que um prompt funciona como programa, citando o mecanismo técnico, não só repetindo a frase de Karpathy?
3. Consigo apontar, na minha própria saída do exercício-âncora, qual caso de teste revelou a ausência de contexto?
4. Sei distinguir um ganho de piso de um ganho de teto no meu próprio código do dia a dia?

Se duas ou mais respostas forem "ainda não", releia [Conceitos](conceitos.md) antes da Sessão 2.

## Fundamentação

- VASWANI, Ashish et al. *Attention Is All You Need*. NeurIPS, 2017.
- BROWN, Tom B. et al. *Language Models are Few-Shot Learners*. NeurIPS, 2020.
- YAO, Shunyu et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR, 2023.
- KARPATHY, Andrej. *Software Is Changing (Again)*. Palestra, YC AI Startup School, 17 jun. 2025.
- WILLISON, Simon. "What is agentic engineering?" — *Agentic Engineering Patterns*. simonwillison.net, mar. 2026.
- Disciplina de Arquitetura de Soluções com IA Generativa (Arkhi), Módulo 4 — Agentes: distinção vibe coding / assistência de codificação / SDD.

Citações completas, com URL e resumo, em [../referencia/bibliografia.md](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 2 assume que o time já sabe nomear os três modos de trabalho e reconhece onde o contexto explícito muda um resultado. Ela detalha o ambiente agêntico em si: cadeia de ferramentas, fluxos reutilizáveis e isolamento de contexto por ramo — a infraestrutura que torna repetível o que esta sessão praticou uma vez.
