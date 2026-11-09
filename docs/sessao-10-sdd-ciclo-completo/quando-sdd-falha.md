# Quando o SDD falha

Desenvolvimento guiado por especificação não corrige automaticamente entendimento ruim. Ele pode produzir documentação em escala sem produzir conhecimento, e a aparência de rigor torna esse fracasso mais difícil de perceber do que a ausência de método. Esta página cobre os antipadrões, os casos em que o método não compensa e o que observar num piloto de adoção.

## Os antipadrões

Os antipadrões abaixo têm o mesmo padrão: o artefato existe e a etapa foi cumprida, mas nenhuma decisão melhorou por causa deles.

- **Especificação teatral.** Documento extenso que não contém decisão nem critério testável. Tem a mesma informação do pedido original, organizada em tópicos com títulos em negrito.
- **Falsa precisão.** Números e regras que o modelo inventou para preencher lacuna. Um limite de "trinta dias" que ninguém decidiu parece tão definitivo quanto um que o jurídico aprovou.
- **Cascata regenerada.** Tentar completar todos os artefatos antes de qualquer experimento, em domínio onde a informação necessária só aparece depois de construir alguma coisa.
- **Artefatos divergentes.** Especificação, plano, tarefas e código evoluem separadamente até ninguém saber qual está certo.
- **Aprovação automática.** O mesmo agente produz e aprova todos os artefatos. O relatório confirma a coerência interna de uma premissa errada.
- **Fatiamento horizontal.** Tarefas organizadas por camada, sem resultado demonstrável antes da última.
- **Testes espelho.** O teste copia a implementação em vez de expressar a intenção, e passa a proteger o defeito.
- **Constitution ornamental.** Princípios que nunca rejeitam nada, porque não têm consequência nomeada.
- **Contexto excessivo.** Despejar o repositório inteiro no agente em vez de oferecer as interfaces e as fontes relevantes.

O mais perigoso é a aprovação automática, porque produz evidência falsa. Um agente que escreve o plano, o código e a revisão aplica a mesma interpretação equivocada nas três etapas, e o relatório final declara coerência entre os artefatos. A coerência interna é real, mas a premissa inicial estava errada, e nenhuma etapa do fluxo tinha a função de contestá-la.

!!! question "Antes de continuar"
    Dos nove antipadrões acima, qual você já viu acontecer, com ou sem IA envolvida? A maior parte deles existia antes dos agentes, que aumentaram a velocidade com que aparecem.

## Quando o custo não compensa

Há tarefas em que o contrato completo tem retorno baixo:

- correção óbvia e localizada, com teste de regressão cobrindo o comportamento.
- atualização mecânica de dependência.
- protótipo descartável, com data de descarte declarada.
- exploração cujo objetivo é descobrir se uma abordagem é viável.
- correção emergencial durante incidente ativo, onde restaurar o serviço vem antes.

Nesses casos, use um contrato menor: problema, limite, teste e evidência. O incidente merece nota à parte: restaurar primeiro é a decisão certa, e a dívida de intenção é fechada depois, com teste de regressão e atualização dos artefatos.

Existe também o caso em que nenhuma quantidade de especificação ajuda. Quando nem a área de negócio consegue definir a regra e as fronteiras, um documento detalhado apenas confere aparência de precisão a premissas frágeis. Nesse caso, o trabalho necessário é descobrir a regra com a área de negócio antes de especificar.

## Indicadores de adoção

Contar especificações criadas incentiva a produção de arquivos, e por isso as perguntas úteis observam o efeito do método:

| Pergunta | Indicador possível |
|---|---|
| a intenção ficou clara antes do código? | proporção de implementações iniciadas após aceite versionado |
| os testes nasceram dos critérios? | cobertura de critérios por cenário |
| a implementação respeitou a especificação? | desvios encontrados na revisão de aderência |
| os artefatos permaneceram vivos? | mudanças de comportamento acompanhadas de atualização |
| o método melhorou o fluxo? | retrabalho, tempo até aceitação e defeitos escapados |
| os portões encontram problema real? | frequência com que um portão barra algo, contra aprovação automática |

Velocidade de geração isolada é a métrica mais perigosa do conjunto. Um time que passou de quatro para onze integrações por semana depois de adotar o agente, e no mesmo trimestre viu o retrabalho por defeito escapado subir de 8% para 21% das horas, tem um número que recomenda ampliar o uso e outro que recomenda investigar onde a intenção está se perdendo. Os dois juntos dizem que o sistema local ficou rápido e o fluxo global piorou.

## O que observar num piloto

Adotar o método na organização inteira antes de aprender com mudanças reais repete o erro que o próprio método tenta evitar, que é comprometer-se cedo demais com uma solução.

Um piloto útil compara classes semelhantes de tarefa e mede a cadeia inteira de entrega, do pedido à aceitação, porque o tempo até a primeira geração de código, medido sozinho, não informa o efeito do método. Começa com poucas mudanças representativas, declara quais etapas são obrigatórias e registra as exceções quando alguma é pulada.

Ao final, o time deve conseguir responder a quatro perguntas: qual artefato foi de fato consultado por alguém, qual portão mudou uma decisão, qual etapa não agregou valor, e quem mantém o processo quando a ferramenta mudar de versão. Se nenhum artefato foi consultado e nenhum portão mudou decisão alguma, o piloto não demonstrou benefício do método, e a adoção ampla fica sem base.

!!! tip "Aplique agora"
    Escolha um dos seis indicadores da tabela acima e descubra se o seu time conseguiria medi-lo hoje, com os dados que já existem. Indicador que o time não consegue medir hoje não deve entrar como critério de adoção do piloto.

## O que permanece humano

O método redistribui trabalho entre pessoas e agentes, e a responsabilidade pelas decisões continua com as pessoas. Continuam sendo decisões de pessoas escolher quais problemas merecem investimento, ouvir usuários e reconhecer conflito de interesse, aceitar risco e suas consequências, decidir trade-offs arquiteturais, julgar se a evidência apresentada é suficiente e responder pelos efeitos em produção.

Agentes ampliam pesquisa, comparação, consistência, geração e revisão, e sustentam bem as relações entre muitos artefatos, mas não têm mandato organizacional. A especificação ocupa posição central porque pessoas autorizadas a adotaram como contrato e mantêm mecanismos para testá-la.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
