# Síntese e referências

## Nove ideias essenciais

1. **SBVR separa vocabulário de regra.** Só depois de os termos estarem definidos, com sinônimos a evitar registrados, uma regra pode ser escrita sem ambiguidade.
2. **Regra estrutural não se viola; regra operativa, sim.** Classificação e derivação usam operador alético e definem o que algo é. Regra operativa usa operador deôntico e rege conduta.
3. **RuleSpeak tem só três formas que contam como regra:** "deve", "não deve" e "pode ... somente se". "Deveria" não é regra, é preferência sem compromisso.
4. **Toda regra formalizada carrega numeração, evidência e confiança.** Sem isso, ela se perde entre a especificação e o código, e ninguém aponta, meses depois, se ainda está implementada.
5. **Um artefato sem especificação escrita ainda tem regras — só que escondidas.** Código legado e planilha com fórmula escondem regra de negócio do mesmo jeito que prosa ambígua, e a engenharia reversa extrai a mesma disciplina de qualquer um dos três.
6. **Tabela de decisão torna combinação ausente visível.** Três ou mais condições combinando é o limiar em que prosa deixa de escalar.
7. **Política de acerto não declarada é a falha mais cara, não a linha errada.** O incidente da linha que ninguém viu sobrepor mostrou isso: cada linha estava certa, e a ausência de uma decisão sobre sobreposição produziu um resultado que ninguém escolheu.
8. **O agente formaliza, não decide.** Ele erra sozinho de três formas típicas: generaliza o escopo, inventa a política de acerto, confunde estrutural com operativa.
9. **Retrotradução é a verificação que expõe os três erros acima.** Uma formalização que "parece certa" não é o mesmo que uma formalização que preservou a intenção, e só a retrotradução, numa conversa separada, distingue as duas.

## Checklist antes de encerrar a sessão

- [ ] O grupo consegue distinguir regra estrutural de operativa pelo teste de violação, sem hesitar.
- [ ] Cada participante formalizou pelo menos uma regra a partir de um artefato sem especificação escrita (código ou planilha), com vocabulário, numeração, evidência e confiança.
- [ ] Cada participante rodou uma retrotradução numa conversa separada, e comparou o resultado com a intenção original.
- [ ] O grupo discutiu o incidente da sobreposição e chegou a um critério, não a uma opinião, sobre quando a política de acerto exige revisão obrigatória.
- [ ] Ninguém saiu achando que uma formalização "que parece profissional" dispensa a checagem por retrotradução.

## Autoavaliação

1. Consigo distinguir, numa regra que recebi, se ela é estrutural (classificação ou derivação) ou operativa, pelo teste de violação?
2. Sei escolher, entre "deve", "não deve" e "pode ... somente se", a forma certa para uma regra do meu domínio?
3. Consigo extrair regras de negócio de um código legado ou de uma planilha sem especificação, sem parafrasear a estrutura do artefato?
4. Diante de uma tabela de decisão com mais de uma dimensão, sei declarar a política de acerto antes de alguém implementar?

Se duas ou mais respostas forem "ainda não", releia [Vocabulário e sentenças de regra](vocabulario-e-sentencas-conceitos.md) e [Tabelas de decisão e IA como formalizadora](tabelas-de-decisao-conceitos.md) antes da Sessão 5.

Todas as fontes citadas nesta sessão, com URL e resumo, estão reunidas na [bibliografia do curso](../referencia/bibliografia.md).

## Conexão com a próxima sessão

A Sessão 5 assume que o time já sabe formalizar uma regra de negócio em vocabulário controlado, com evidência e confiança declaradas. Ela aprofunda a decomposição: como fatiar uma regra ou uma funcionalidade formalizada em tarefas executáveis por um agente, uma de cada vez, sem perder a rastreabilidade até a regra que a originou.
