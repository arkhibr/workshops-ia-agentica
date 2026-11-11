# S9 — Governança de skills e agentes

**Bloco:** 4 — Skills, agentes e computação agêntica

> **Pergunta-guia:** o que precisa estar decidido e registrado antes que outra pessoa da equipe instale uma skill ou um agente construído por um colega?

## Problema

Na Sessão 8, a equipe construiu skills e agentes com uma ficha de requisitos que registra artefato, modelo, custo, tempo, permissões e credenciais antes da construção. Quando a skill passa a ser instalada por outras pessoas, aparecem decisões que essa ficha não cobre: quem responde pelo uso, que dados o agente pode ler, quanto ele pode agir sem aprovação, que risco foi aceito, que prova mostra que o controle funciona e como o colega recebe uma correção ou o aviso de retirada. Sem essas decisões escritas, a skill circula por cópia de pasta, a versão instalada em cada máquina fica desconhecida e o primeiro incidente mostra que ninguém havia sido designado para responder por ele.

## A ficha de governança

A resposta à pergunta-guia é a ficha de governança, uma tabela de oito linhas que estende a [ficha de requisitos da Sessão 8](../sessao-08-skills-e-agentes/index.md#a-ficha-de-requisitos). A ficha da Sessão 8 reúne as decisões anteriores à construção da skill, e a ficha desta sessão reúne as decisões anteriores ao compartilhamento com a equipe. Cada página de teoria abre dizendo que linha preenche e termina com o bloco "Linha da ficha", e o segundo bloco de exercícios grava a ficha dentro do próprio plugin, no arquivo `governanca.json`, que um script de portão lê antes da publicação.

| Linha da ficha | Pergunta que a linha responde | Página que preenche |
|---|---|---|
| Dono e finalidade | Quem responde pelo caso, que problema ele resolve e que alternativa sem IA foi considerada | [Governança de IA](governanca-de-ia.md) |
| Dados e ferramentas | Que classes de dado o agente lê e que modelo, skills e APIs ele usa | [Triagem por criticidade](triagem-por-criticidade.md) |
| Autonomia | Se o agente sugere, prepara para aprovação ou executa, e quem o interrompe | [Governança de IA](governanca-de-ia.md) |
| Faixa de risco | Baixa, moderada ou alta, com o fator que decidiu a faixa e as premissas não verificadas | [Triagem por criticidade](triagem-por-criticidade.md) |
| Riscos e controles | Evento e consequência, controle preventivo e controle detectivo | [Riscos de agentes](riscos-de-agentes.md) |
| Evidência e gate | Teste ou registro que prova o controle, onde ele fica guardado e quem aprova a publicação | [Controles e evidências](controles-e-evidencias.md) |
| Canal e versão | Onde a skill é publicada, em que versão e como o colega recebe a atualização | [Compartilhamento governado](compartilhamento-governado.md) |
| Revisão e retirada | Quando a ficha é revista (troca de modelo, de base, de permissão ou de finalidade) e como a skill é retirada | [Compartilhamento governado](compartilhamento-governado.md) |

As linhas não são preenchidas de forma independente, porque a faixa de risco depende dos dados, das ferramentas e da autonomia, e o gate depende da faixa e da evidência de cada controle.

![Dependências entre as linhas da ficha. As linhas dono e finalidade, dados e ferramentas, autonomia e faixa de risco formam a Definition of Ready, e as linhas riscos e controles, evidência e gate e revisão e retirada formam a Definition of Done. Dados e ferramentas e autonomia alimentam a faixa de risco, a faixa alta exige aprovação formal no gate e a premissa que mudaria a faixa passa a ser condição do gate, a evidência prova cada controle, o gate libera a publicação registrada em canal e versão, a revisão registra a versão vigente, e a troca de modelo, de base, de permissão, de skill ou de finalidade reabre a faixa antes da mudança.](assets/dependencias-da-ficha.png)

A ficha existe para que a decisão de compartilhar fique escrita antes da primeira instalação feita por um colega. Uma skill compartilhada sem ela costuma esconder escolhas que só aparecem no primeiro incidente, como a credencial pessoal ampla usada por conveniência, a faixa de risco que ninguém declarou ou a cópia antiga que continua instalada na máquina de outra pessoa.

## Mapa da sessão

A sessão alterna teoria e dois blocos de exercícios. O primeiro bloco aplica a triagem por criticidade e a análise de riscos a uma skill de uma organização fictícia, e o segundo empacota uma skill como plugin num marketplace local, com a ficha de governança dentro do plugin, e percorre a publicação, a instalação, a correção e a retirada.

## Pré-requisitos

A sessão pressupõe o ambiente configurado nas Sessões 1 e 2, o uso do Claude Code e a página de [segurança e credenciais da Sessão 8](../sessao-08-skills-e-agentes/seguranca-e-credenciais.md), que trata de permissões mínimas, identidade própria do agente e ciclo de vida do token e que esta sessão não repete.

As referências normativas entram como quadro de referência, sem estudo aprofundado: o NIST AI RMF 1.0, o perfil NIST AI 600-1, a ISO/IEC 42001:2023, o OWASP Top 10 para aplicações de LLM na edição 2026, a LGPD e o PL 2338/2023, projeto de lei em tramitação na Câmara dos Deputados na consulta de 03/11/2026. As fontes estão listadas na [bibliografia do curso](../referencia/bibliografia.md), com a data de consulta de cada uma.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Classificar** uma skill ou um agente numa faixa de criticidade e justificar a classificação pelo fator mais grave, sem soma de pontos.
2. **Formular** um risco como evento e consequência e associar a ele um controle preventivo, um controle detectivo e a evidência que fica guardada.
3. **Distinguir** um controle aplicado fora do modelo, como permissão, hook, validação de esquema ou política de API, de uma instrução textual dirigida ao modelo.
4. **Empacotar** uma skill como plugin num marketplace local, com a ficha de governança dentro do plugin, e percorrer o ciclo de vida: publicar, instalar como colega, publicar correção com nova versão e retirar.
5. **Selecionar** o mecanismo de compartilhamento adequado a cada situação (pessoal, repositório, marketplace ou organização) e identificar qual deles exige papel de administrador.
6. **Elaborar** material para a política de uso de IA da organização, com a ficha de triagem preenchida para um protótipo da equipe e uma proposta de três controles mínimos.

## Roteiro da sessão

| Página ou atividade | Foco |
|---|---|
| Visão geral | Pergunta disparadora, pergunta-guia e ficha |
| [Governança de IA](governanca-de-ia.md) | Cinco distinções, quatro decisões e papéis |
| [Triagem por criticidade](triagem-por-criticidade.md) | Inventário, três faixas e fator decisivo |
| [Riscos de agentes](riscos-de-agentes.md) | Fronteiras de confiança e três incidentes |
| [Exercícios — triagem e riscos de uma skill](exercicios.md) | Exercícios 1 a 6 |
| Intervalo | Às 11h00 |
| [Controles e evidências](controles-e-evidencias.md) | Controles fora do modelo, testes, DoR e DoD |
| [Compartilhamento governado](compartilhamento-governado.md) | Quatro níveis, plugin, marketplace e ciclo de vida |
| [Oficina — marketplace local governado](oficina-de-ferramentas.md) | Publicar, instalar, corrigir e retirar |
| [Experimentos complementares](experimentos-complementares.md) | Protótipo da equipe, hospedagem em git e avaliação de plugin |
| [Síntese e referências](sintese-e-referencias.md) | Checklist, autoavaliação e kit de 30 dias |

## Como conduzir

A sessão abre com a pergunta disparadora do guia do facilitador [Governança de IA na prática](../referencia/bibliografia.md#arkhi-governanca-de-ia-na-pratica-2026): "Se um agente produzir uma resposta incorreta com aparência de certeza, quem será responsável e como perceberemos o problema?". A pergunta tem uma parte de responsabilidade, registrada nas linhas de dono e de gate da ficha, e uma parte de detecção, registrada nas linhas de riscos e controles e de evidência.

O primeiro bloco de exercícios usa uma skill da ACME, a universidade fictícia da Sessão 8, que revisa pull requests com uma credencial pessoal ampla usada por conveniência, padrão de risco comum em protótipos de equipes de desenvolvimento. O segundo bloco usa o marketplace de exemplo da pasta `exemplo/marketplace-governado/` do repositório do workshop, com os plugins `identificando-tarefas-e-riscos` e `revisando-pull-requests` e um script de portão escrito para Node 20 ou superior, sem dependências.

A regra de dados fictícios vale para toda a sessão. Nenhum exercício usa dado real, credencial real, prompt interno ou documento confidencial, e nenhum depende de papel de administrador na organização do Claude ou do repositório privado do participante. A aplicação ao protótipo real da equipe é feita no ambiente interno dela, sem publicação.

!!! warning "Limite desta sessão"
    As três faixas de criticidade da triagem são uma ferramenta pedagógica adaptada do guia do facilitador, sem valor de classificação normativa oficial. A faixa de um caso real depende do contexto, do apetite a risco aprovado pela organização e da avaliação jurídica e de privacidade quando há dado pessoal envolvido. Na forma estrita da regra adotada nesta sessão, um único fator crítico leva o caso direto à faixa alta, independentemente dos demais fatores.

**Próxima página:** [Governança de IA](governanca-de-ia.md).
