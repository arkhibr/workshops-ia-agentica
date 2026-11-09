# Síntese e referências

## Ideias essenciais

1. **A ficha de governança registra o que precisa estar decidido antes do compartilhamento.** As oito linhas vão do dono e da finalidade até a revisão e a retirada, cada uma preenchida por uma página da sessão, e o segundo bloco de exercícios grava a ficha no arquivo `governanca.json` do plugin, como descreve a [visão geral](index.md#a-ficha-de-governanca).
2. **Governança, gestão de riscos, segurança, qualidade e operação deixam evidências diferentes.** Cada atividade responde a uma pergunta própria, e a evidência que mais costuma faltar é o nome de quem aceitou o risco residual, segundo o guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026).
3. **Quatro decisões de autorização antecedem o uso de um caso.** O caso de uso, os dados e as ferramentas, a autonomia e a produção com continuidade têm pergunta e dono próprios, e a decisão sobre a autonomia escolhe entre sugerir, preparar para aprovação e executar, conforme a página [Governança de IA](governanca-de-ia.md#quatro-decisoes).
4. **A revisão humana só conta como controle quando o revisor tem informação, tempo, autoridade e possibilidade real de rejeitar.** A revisão de [Parasuraman e Manzey](../referencia/bibliografia.md#parasuraman-e-manzey-complacency-and-bias-in-human-use-of-automation-2010) conclui que a complacência e o viés de automação ocorrem em novatos e em especialistas e que treinamento e instruções não os evitam.
5. **A faixa de risco é decidida pelo fator mais grave, sem soma de pontos.** Na forma estrita adotada nesta sessão, um único fator crítico, como a permissão de escrita em sistema financeiro, leva o caso direto à faixa alta, e a ficha registra a faixa como preliminar até a avaliação jurídica e de privacidade quando há dado pessoal, conforme a página [Triagem por criticidade](triagem-por-criticidade.md#a-regra-do-fator-critico).
6. **A autorização fica num componente que o modelo não altera.** Esse componente aplica a mediação completa e o menor privilégio formulados por [Saltzer e Schroeder](../referencia/bibliografia.md#saltzer-e-schroeder-the-protection-of-information-in-computer-systems-1975), e as três [fronteiras de confiança](riscos-de-agentes.md#etapas-e-fronteiras-de-confianca) ficam na entrada do conteúdo recuperado, na chamada de ferramenta e no efeito externo.
7. **Três incidentes concentram a discussão de riscos de agentes.** A instrução escondida no documento, a permissão maior que a finalidade e a resposta plausível e incorreta correspondem a LLM01 (2026), LLM03 (2026) e LLM07 (2026) do [OWASP Top 10 para aplicações de LLM](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026), e a avaliação de [Magesh et al.](../referencia/bibliografia.md#magesh-et-al-hallucination-free-2025) mediu alucinação entre 17% e 33% em ferramentas jurídicas com recuperação de documentos.
8. **Um controle que depende apenas de instrução ao modelo é reprovado como controle.** Permissão de ferramenta, hook, validação de esquema e política na API rodam fora do modelo, e o critério de aceite com a expressão "independentemente da resposta do modelo" é o teste prático que separa os dois casos, conforme a página [Controles e evidências](controles-e-evidencias.md#controle-fora-do-modelo-e-instrucao-textual).
9. **Framework adotado, controle implementado e evidência guardada são três estados com registros próprios.** Os [testes T01 a T07](controles-e-evidencias.md#testes-de-aceite-t01-a-t07) transformam os controles em prova verificável, e o guia recomenda automatizar primeiro o T01, o T02 e o T03, que cobrem a injeção de prompt e a agência excessiva.
10. **Três dos quatro níveis de compartilhamento ficam ao alcance da equipe.** Os níveis pessoal, de repositório e de marketplace dispensam privilégio especial, e o nível de organização, com as configurações gerenciadas, exige papel de administrador, segundo a [página de gestão de plugins na organização](../referencia/bibliografia.md#anthropic-gerenciar-plugins-na-organizacao-documentacao-do-claude-code).
11. **A versão do plugin controla o aviso de atualização, e a retirada exige procedimento escrito.** Num marketplace de pasta local, a `version` governou o aviso `updated from 1.0.0 to 1.0.1`, o número exibido e o cache, com o conteúdo lido da própria pasta, e a retirada pelo mapa `renames` com `null` desabilitou o plugin sem aviso explícito na linha de comando, conforme o [ciclo de vida do plugin](compartilhamento-governado.md#ciclo-de-vida-do-plugin).

## Checklist antes de encerrar a sessão

- [ ] A skill de revisão de pull requests da ACME, a universidade fictícia da sessão, foi classificada numa faixa de risco com o fator que decidiu a faixa.
- [ ] Ao menos um risco foi registrado como evento e consequência, com controle preventivo fora do modelo, controle detectivo e evidência.
- [ ] Cada premissa não verificada da ficha tem o nome de quem vai verificá-la.
- [ ] O portão da oficina reprovou o plugin com controle feito só de instrução e aprovou o plugin que tinha a ficha completa.
- [ ] O plugin foi instalado como colega e atualizado para a versão 1.0.1, com o número conferido em `claude plugin details`.
- [ ] A retirada do plugin de revisão foi feita pelo mapa `renames`, e a ficha registra a revogação da credencial e o aviso direto a quem tinha o plugin instalado.
- [ ] O marketplace da oficina foi removido com `claude plugin marketplace remove`, e a pasta de trabalho foi apagada.
- [ ] Nenhum exercício usou dado real, credencial real ou papel de administrador da organização do Claude.

## Autoavaliação

As seis primeiras perguntas são as discussões orientadas do guia do facilitador, e as perguntas 1, 3 e 5 são as do exercício 6. A resposta de cada pessoa a essas três pode ser comparada depois com a resposta esperada da página de [exercícios](exercicios.md#6-discussao-com-a-turma).

1. Se o PO aprovou o caso, o time pode usar qualquer dado?
2. Se o prompt pede para não vazar dados, já existe controle?
3. Um agente que apenas lê tem risco baixo?
4. Qual é o perigo de dar ao agente permissão ampla por conveniência?
5. E se a avaliação atingir 95% de acerto?
6. O que a equipe deve fazer quando trocar o modelo?
7. Consigo dizer qual fator decidiu a faixa de risco de um protótipo da minha equipe e que premissa dele ainda falta verificar?
8. Sei apontar, para um controle que propus, a evidência que fica guardada, o local de guarda e quem aprova a publicação?
9. Sei dizer qual dos quatro níveis de compartilhamento exige papel de administrador e qual comando registra um marketplace no escopo do projeto?

Se três ou mais respostas forem "ainda não", a releitura de [Riscos de agentes](riscos-de-agentes.md) e de [Controles e evidências](controles-e-evidencias.md) antes da Sessão 10 cobre a maior parte das lacunas.

## Kit para os primeiros 30 dias

O guia do facilitador propõe um kit para os primeiros 30 dias de um programa de governança de IA. A tabela abaixo adapta o kit a uma equipe de desenvolvimento e mantém apenas passos que a própria equipe executa, sem papel de administrador na organização do Claude.

| Semana | Atividade | Resultado registrado |
|---|---|---|
| Semana 1 | Inventariar pilotos, agentes, skills, servidores MCP, tokens e provedores de modelo em uso pela equipe | Lista de casos com dono, finalidade e classes de dado |
| Semana 2 | Adotar a ficha de triagem nas demandas novas e registrar a faixa com o fator que a decidiu | Registro de classificação, de premissas e de decisões pendentes |
| Semana 3 | Escolher os controles críticos e automatizar os testes T01 a T03 no pipeline do repositório da equipe | Pull requests com as verificações e com o escopo dos tokens revisto |
| Semana 4 | Revisar um piloto, simular um incidente e ajustar o portão de publicação do marketplace da equipe | Decisão de continuidade, riscos residuais e plano do mês seguinte |

Os passos que dependem das configurações gerenciadas ou do console de administração do claude.ai ficam fora do kit. Quando a equipe concluir que as origens de marketplace precisam ser restritas em todas as máquinas, a decisão passa a ser um pedido ao administrador, acompanhado da ficha de governança e da evidência da semana 4, e o mecanismo correspondente está descrito na seção [Nível de organização](compartilhamento-governado.md#nivel-de-organizacao).

## Indicadores de partida

O guia propõe quatro indicadores para o primeiro mês, apresentados na página [Controles e evidências](controles-e-evidencias.md#indicadores-de-partida). A terceira coluna indica a fonte de cada indicador dentro do kit acima.

| Indicador | O que mede | Fonte no kit |
|---|---|---|
| Cobertura | Percentual dos casos conhecidos com dono, finalidade e faixa de risco registrados | Lista da semana 1 e registro da semana 2 |
| Prevenção | Percentual dos agentes com permissões verificadas e testes adversariais mínimos | Testes T01 a T03 da semana 3 |
| Entrega | Percentual das mudanças de modelo ou de skill submetidas a reavaliação documentada | Versões publicadas no marketplace com revisão registrada na ficha |
| Operação | Incidentes e quase incidentes observados, tempo até a suspensão e consumo por execução | Incidente simulado da semana 4 |

A figura abaixo liga as duas tabelas pela ficha de governança: cada semana do kit preenche linhas da ficha, e três dos quatro indicadores são calculados a partir dessas linhas.

![Kit de 30 dias ligado às oito linhas da ficha e aos indicadores. A semana 1, de inventário, preenche dono e finalidade e dados e ferramentas. A semana 2, da ficha de triagem, preenche autonomia e faixa de risco. A semana 3, dos controles críticos e dos testes T01 a T03, preenche riscos e controles e evidência e gate. A semana 4, de revisão de piloto, incidente simulado e ajuste do portão, preenche evidência e gate e revisão e retirada. O indicador de cobertura sai das linhas dono e finalidade e faixa de risco, o de prevenção sai de dados e ferramentas e de evidência e gate, e o de entrega sai de canal e versão e de revisão e retirada. O indicador de operação é medido no incidente simulado da semana 4, e a linha canal e versão não aparece em nenhuma atividade do kit.](assets/kit-de-30-dias-e-a-ficha.png)

O guia recomenda evitar metas artificiais de perfeição no primeiro mês e usar os indicadores para descobrir a exposição real e melhorar os controles, sem premiar a subnotificação de incidentes e de quase incidentes.

## Fundamentação

Todas as fontes citadas nesta sessão estão na [bibliografia do curso](../referencia/bibliografia.md), com URL e data de consulta. A teoria se apoia no guia do facilitador, em normas e frameworks usados como quadro de referência, em pesquisa primária sobre segurança de agentes, alucinação e fatores humanos e na documentação oficial do Claude Code e do Codex CLI.

| Página | Fontes citadas |
|---|---|
| Visão geral | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023), [NIST AI 600-1](../referencia/bibliografia.md#nist-ai-600-1-generative-artificial-intelligence-profile-2024), [ISO/IEC 42001:2023](../referencia/bibliografia.md#isoiec-420012023), [OWASP Top 10 para aplicações de LLM, edição 2026](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026), [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) e [PL 2338/2023](../referencia/bibliografia.md#camara-dos-deputados-pl-23382023-ficha-de-tramitacao) |
| Governança de IA | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [Controle e Autonomia](../referencia/bibliografia.md#mendes-controle-e-autonomia-modulo-4-agentes), [Parasuraman e Manzey (2010)](../referencia/bibliografia.md#parasuraman-e-manzey-complacency-and-bias-in-human-use-of-automation-2010), [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018), [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023), [NIST AI 600-1](../referencia/bibliografia.md#nist-ai-600-1-generative-artificial-intelligence-profile-2024), [ISO/IEC 42001:2023](../referencia/bibliografia.md#isoiec-420012023), [OWASP Top 10 para aplicações de LLM, edição 2026](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026) e [PL 2338/2023](../referencia/bibliografia.md#camara-dos-deputados-pl-23382023-ficha-de-tramitacao) |
| Triagem por criticidade | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023), [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) e [ISO/IEC 42001:2023](../referencia/bibliografia.md#isoiec-420012023) |
| Riscos de agentes | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [Saltzer e Schroeder (1975)](../referencia/bibliografia.md#saltzer-e-schroeder-the-protection-of-information-in-computer-systems-1975), [Greshake et al. (2023)](../referencia/bibliografia.md#greshake-et-al-indirect-prompt-injection-2023), [OWASP Top 10 para aplicações de LLM, edição 2026](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026), [Beurer-Kellner et al. (2025)](../referencia/bibliografia.md#beurer-kellner-et-al-design-patterns-for-securing-llm-agents-2025) e [Magesh et al. (2025)](../referencia/bibliografia.md#magesh-et-al-hallucination-free-2025) |
| Exercícios — triagem e riscos de uma skill | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [OWASP Top 10 para aplicações de LLM, edição 2026](../referencia/bibliografia.md#owasp-top-10-for-llm-applications-2026) e [LGPD](../referencia/bibliografia.md#brasil-lei-geral-de-protecao-de-dados-pessoais-2018) |
| Controles e evidências | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), [NIST AI RMF 1.0](../referencia/bibliografia.md#nist-ai-risk-management-framework-10-core-2023) e [Gherkin](../referencia/bibliografia.md#cucumber-gherkin-reference) |
| Compartilhamento governado | [Skills no Claude Code](../referencia/bibliografia.md#anthropic-skills-no-claude-code-documentacao), [Gerenciar plugins na organização](../referencia/bibliografia.md#anthropic-gerenciar-plugins-na-organizacao-documentacao-do-claude-code), [Marketplaces de plugins](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao), [Avaliação de plugins](../referencia/bibliografia.md#anthropic-avaliacao-de-plugins-no-claude-code-documentacao), [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026) e [Codex: Build plugins](../referencia/bibliografia.md#openai-codex-build-plugins-documentacao) |
| Oficina — marketplace local governado | [Marketplaces de plugins](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao) e [Instalação e requisitos do Claude Code](../referencia/bibliografia.md#anthropic-instalacao-e-requisitos-do-claude-code-documentacao) |
| Experimentos complementares | [Marketplaces de plugins](../referencia/bibliografia.md#anthropic-marketplaces-de-plugins-no-claude-code-documentacao), [Avaliação de plugins](../referencia/bibliografia.md#anthropic-avaliacao-de-plugins-no-claude-code-documentacao) e [Codex: Build plugins](../referencia/bibliografia.md#openai-codex-build-plugins-documentacao) |
| Síntese e referências | [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026), para o kit de 30 dias, os indicadores de partida e as discussões orientadas |

O guia do facilitador é material próprio adaptado, sem URL pública, e as afirmações reaproveitadas dele foram conferidas contra as fontes primárias da tabela. O texto da norma ISO/IEC 42001 não foi consultado, e a LGPD e a ficha de tramitação do PL 2338/2023 tiveram leitura parcial, com a situação do projeto registrada na consulta de 03/11/2026.

## Conexão com a próxima sessão

A [Sessão 10](../sessao-10-sdd-ciclo-completo/index.md) executa um ciclo completo de desenvolvimento orientado por especificação com o GitHub Spec Kit, da constitution ao código verificado, com os quatro artefatos canônicos versionados. A faixa de risco desta sessão tem correspondência na régua de profundidade da Sessão 10, que escolhe o processo proporcional ao risco da mudança, e as skills e os agentes que executarem etapas desse ciclo chegam a ele com dono, controles e evidência registrados na ficha de governança.
