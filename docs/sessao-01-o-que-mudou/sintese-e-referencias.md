# Síntese e referências

## Onze ideias essenciais

1. **Vibe coding, assistência de codificação e SDD são famílias de risco, não degraus de maturidade.** A escolha depende da tarefa, não de uma régua de "quão avançado" o time está.
2. **Um prompt funciona como programa porque o modelo aprende em contexto**, sem ajuste de peso — mecanismo empírico demonstrado por [Brown et al. (2020)](../referencia/bibliografia.md#brown-et-al-language-models-are-few-shot-learners-2020).
3. **A janela de contexto é o programa.** O que não está escrito explicitamente no pedido não existe para o agente, por mais óbvio que pareça para quem escreveu.
4. **Um agente se distingue de um chat pelo ciclo de raciocínio e ação** ([Yao et al., ReAct](../referencia/bibliografia.md#yao-et-al-react-2023)), não pelo tamanho do modelo.
5. **Piso, teto e julgamento humano sobem em ritmos diferentes.** Confundir "o código roda" com "o código está correto" é o erro mais caro e mais comum.
6. **A diferença entre um prompt intuitivo e um estruturado quase nunca está no modelo.** Está em quem já tinha feito, antes de escrever o pedido, o trabalho de reunir a regra de negócio inteira.
7. **O ganho de produtividade depende do tipo de tarefa, com números reais para provar.** [Peng et al.](../referencia/bibliografia.md#peng-et-al-copilot-productivity-2023) mediram 55,8% de ganho numa tarefa nova e delimitada; o [METR](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025) mediu 19% de perda numa tarefa de manutenção em sistema maduro — e os próprios desenvolvedores não perceberam a perda.
8. **A régua de decisão é a simplicidade, não a ferramenta mais avançada.** A recomendação da [Anthropic em "Building Effective Agents"](../referencia/bibliografia.md#anthropic-building-effective-agents-2024) vale para os três modos desta sessão: comece pelo mais simples que a tarefa permitir.
9. **A capacidade de resolver problemas reais deu um salto medido, não só sentido.** O [SWE-bench](../referencia/bibliografia.md#jimenez-et-al-swe-bench-2024) foi de 1,96% de resolução em 2024 para cerca de 97% em 2026 — o mesmo "works.any() vira works.all()" de [Karpathy](../referencia/bibliografia.md#karpathy-software-is-changing-again-2025), numa escala de dois anos.
10. **Reversibilidade e tempo de vida importam porque corrigir cedo é mais barato.** [Boehm](../referencia/bibliografia.md#boehm-software-engineering-economics-1981) documentou isso em 1981, décadas antes de qualquer LLM: quanto mais tarde uma ambiguidade aparece, mais caro fica resolvê-la.
11. **Escolher modelo pelo nome mais falado é o mesmo erro do vibe coding: aceitar sem verificar.** Use benchmark de engenharia real e independente (como o [DeepSWE](../referencia/bibliografia.md#datacurve-deepswe-leaderboard)), desconfie de número autorreportado pelo fabricante, e lembre que o placar muda a cada poucas semanas.

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

Se duas ou mais respostas forem "ainda não", releia [Modos de trabalho com IA](modos-de-trabalho.md) e [A tese do Software 3.0](software-3-0.md) antes da Sessão 2.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 2 assume que o time já sabe nomear os três modos de trabalho e reconhece onde o contexto explícito muda um resultado. Ela detalha o ambiente agêntico em si: cadeia de ferramentas, fluxos reutilizáveis e isolamento de contexto por ramo — a infraestrutura que torna repetível o que esta sessão praticou uma vez.
