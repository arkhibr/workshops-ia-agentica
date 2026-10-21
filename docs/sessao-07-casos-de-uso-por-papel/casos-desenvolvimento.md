# Casos de uso de IA para Desenvolvimento

Esta página reúne quinze casos de uso de IA generativa para quem desenvolve software em C#, JavaScript ou TypeScript. Dez casos compõem o catálogo do mural da sessão, e cinco são complementares. Quatro dos dez casos do mural reaproveitam técnicas das Sessões 4, 5 e 6, e a página indica a sessão de origem em cada um.

## Onde a IA entra no trabalho do desenvolvedor

O desenvolvimento é a área com mais evidência publicada sobre IA generativa, e o resultado varia de forma marcante entre estudos. A conferência de cada caso desta página usa o que o desenvolvedor já tem à mão: o código, os testes, o compilador e o histórico do repositório.

Em revisão de código, três estudos de campo de 2024 a 2026 mostram resultados diferentes. [Cihan et al. (2025)](../referencia/bibliografia.md#cihan-et-al-automated-code-review-in-practice-2025) acompanharam uma ferramenta de revisão automatizada em três projetos industriais e relataram que 73,8% dos comentários automatizados foram resolvidos e que o tempo médio de fechamento de pull request subiu de 5 horas e 52 minutos para 8 horas e 20 minutos. [Olewicki et al. (2024)](../referencia/bibliografia.md#olewicki-et-al-impact-of-llm-based-review-comment-generation-2024) mediram, em duas organizações, aceitação de 8,1% e 7,2% dos comentários gerados, com mediana de 43 segundos adicionais por patch. [Tantithamthavorn et al. (2026)](../referencia/bibliografia.md#tantithamthavorn-et-al-rovodev-code-reviewer-2026), da própria empresa que opera a ferramenta, relataram que 38,70% dos comentários levaram a alteração de código e que o tempo de ciclo de pull request caiu 30,8%. Os três estudos medem ferramentas, projetos e métricas diferentes, e o contraste é o motivo de a página recomendar que cada equipe meça o próprio resultado.

Em documentação de código legado, [Diggs et al. (2024)](../referencia/bibliografia.md#diggs-et-al-llms-for-legacy-code-documentation-2024) avaliaram comentários gerados para código em MUMPS e em assembly de mainframe e concluíram que foram em geral sem alucinação, completos, legíveis e úteis, com o assembly mais difícil, e que nenhuma métrica automática correlacionou fortemente com a qualidade. Em mensagens de commit, [Zhang et al. (2024)](../referencia/bibliografia.md#zhang-et-al-llms-para-mensagens-de-commit-2024) relataram que, na avaliação humana, as mensagens geradas por modelos foram consideradas as melhores em 78% de 366 amostras. Em migração de código, [Ziftci et al. (2025)](../referencia/bibliografia.md#ziftci-et-al-migrating-code-at-scale-with-llms-at-google-2025) descreveram 39 migrações no Google em que 74,45% das alterações foram geradas pelo modelo, e a redução de 50% no tempo foi estimada pelos próprios desenvolvedores, sem medição controlada. Em resolução de problemas reais de repositórios, o [SWE-bench](../referencia/bibliografia.md#jimenez-et-al-swe-bench-2024) é a referência de medição já apresentada na Sessão 1.

## Catálogo do mural

| Caso | Entrada e saída | Pedido-base | Conferência |
|---|---|---|---|
| Entender código legado | Módulo desconhecido vira mapa de responsabilidades e explicação do comportamento | "Descreva o que o módulo faz citando a linha de cada afirmação" | Executar o módulo com um caso conhecido e comparar com a explicação |
| Extrair regras do código | Condicionais viram regras em RuleSpeak com evidência (Sessão 4) | "Reescreva cada condição como regra de negócio e cite arquivo, função e linha" | Retrotradução da regra em conversa limpa e conferência da linha citada |
| Implementar da especificação | Especificação vira código com teste (Sessões 5 e 6) | "Implemente apenas o que a especificação declara e escreva o teste antes do código" | Teste vermelho antes da implementação e verde depois |
| Gerar testes de unidade | Função vira casos de teste com valores de borda (Sessão 6) | "Inclua casos de fronteira e de erro e não altere o código de produção" | Alterar a comparação de fronteira e confirmar que um teste falha |
| Depurar com hipóteses | Erro e log viram hipóteses ordenadas por probabilidade | "Liste hipóteses e o dado que confirmaria ou descartaria cada uma" | Verificar a primeira hipótese com um experimento antes de alterar o código |
| Revisar código antes do pull request | Alteração vira lista de achados por severidade | "Classifique cada achado como bloqueio, sugestão ou dúvida e cite a linha" | O autor confere cada achado e descarta o que não se aplica |
| Escrever commit e descrição de PR | Alteração vira mensagem de commit e descrição de pull request | "Descreva o que mudou e por quê, sem listar arquivos" | O autor confirma que a mensagem não promete o que o diff não faz |
| Refatorar com rede de testes | Código e testes viram alteração que preserva o comportamento | "Refatore sem alterar o comportamento e rode a suíte a cada passo" | A suíte passa antes e depois, sem teste alterado |
| Documentar API e código | Código vira documentação de uso | "Documente parâmetros, retorno e erros observáveis no código" | Executar o exemplo da documentação |
| Planejar migração de versão | Projeto e versão alvo viram plano por etapas | "Liste as mudanças incompatíveis da versão e o impacto em cada módulo" | Conferir cada mudança incompatível na documentação oficial da versão |

## Casos complementares

| Caso | Entrada e saída | Conferência |
|---|---|---|
| Explicar mensagem de erro ou log | Erro e contexto viram explicação e passos de verificação | Reproduzir o erro e aplicar um passo de cada vez |
| Converter código entre linguagens ou frameworks | Trecho vira equivalente na outra linguagem | Rodar os testes do original contra o convertido |
| Escrever consultas SQL e explicar o plano | Descrição da necessidade vira consulta e leitura do plano | Executar a consulta em base de teste e comparar o resultado esperado |
| Escrever script de automação | Tarefa repetitiva vira script | Rodar em ambiente descartável antes de usar em produção |
| Preparar exemplos de uso de uma biblioteca | Documentação vira exemplos executáveis | Executar cada exemplo |

## Onde os casos falham

Os casos de geração de código e de teste dependem de verificação executável, e o risco aumenta quando o agente escreve código e teste juntos, porque o teste pode confirmar o que o código já faz. A prática da Sessão 6, de conferir que o teste falha antes da implementação e pelo motivo certo, é a defesa para os casos que envolvem implementação. Nos casos de revisão e de documentação, a defesa é a decisão final do autor, que descarta o achado ou a frase que não se aplica. O código usado como entrada não deve conter segredo, credencial nem dado pessoal, e o uso em repositório com restrição segue a política da organização.

**Próxima página:** [Casos de uso para Testes](casos-testes.md).
