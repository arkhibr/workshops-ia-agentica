# Quando o SDD falha

Desenvolvimento guiado por especificação não corrige automaticamente entendimento ruim. Ele pode produzir documentação em escala sem produzir conhecimento, e a aparência de rigor torna esse fracasso mais difícil de perceber do que a ausência de método. Esta página cobre os antipadrões, os casos em que o método não compensa e o que observar num piloto de adoção.

## Os antipadrões

Cada um destes tem a mesma assinatura: o artefato existe, a etapa foi cumprida, e nenhuma decisão ficou melhor por causa disso.

- **Especificação teatral.** Documento extenso que não contém decisão nem critério testável. Tem a mesma informação do pedido original, organizada em tópicos com títulos em negrito.
- **Falsa precisão.** Números e regras que o modelo inventou para preencher lacuna. Um limite de "trinta dias" que ninguém decidiu parece tão definitivo quanto um que o jurídico aprovou.
- **Cascata regenerada.** Tentar completar todos os artefatos antes de qualquer experimento, em domínio onde a informação necessária só aparece depois de construir alguma coisa.
- **Artefatos divergentes.** Especificação, plano, tarefas e código evoluem separadamente até ninguém saber qual está certo.
- **Aprovação automática.** O mesmo agente produz e aprova todos os artefatos. O relatório confirma a coerência interna de uma premissa errada.
- **Fatiamento horizontal.** Tarefas organizadas por camada, sem resultado demonstrável antes da última.
- **Testes espelho.** O teste copia a implementação em vez de expressar a intenção, e passa a proteger o defeito.
- **Constitution ornamental.** Princípios que nunca rejeitam nada, porque não têm consequência nomeada.
- **Contexto excessivo.** Despejar o repositório inteiro no agente em vez de oferecer as interfaces e as fontes relevantes.

O mais perigoso é a aprovação automática, porque produz evidência falsa. Um agente que escreve o plano, o código e a revisão aplica a mesma interpretação equivocada nas três etapas, e o relatório final diz que está tudo coerente. Está mesmo, internamente. O problema é que a premissa inicial estava errada, e nada no fluxo tinha a função de contestá-la.

!!! question "Antes de continuar"
    Dos nove antipadrões acima, qual você já viu acontecer, com ou sem IA envolvida? A maior parte deles existia antes dos agentes, e o agente apenas acelerou.

## Quando o custo não compensa

Há tarefas em que o contrato completo tem retorno baixo:

- correção óbvia e localizada, com teste de regressão cobrindo o comportamento.
- atualização mecânica de dependência.
- protótipo descartável, com data de descarte declarada.
- exploração cujo objetivo é descobrir se uma abordagem é viável.
- correção emergencial durante incidente ativo, onde restaurar o serviço vem antes.

Nesses casos, use um contrato menor: problema, limite, teste e evidência. O incidente merece nota à parte: restaurar primeiro é a decisão certa, e a dívida de intenção é fechada depois, com teste de regressão e atualização dos artefatos. Ter passado a crise não cancela essa dívida.

Existe também o caso em que nenhuma quantidade de especificação ajuda. Quando nem a área de negócio consegue definir a regra e as fronteiras, um documento detalhado apenas confere aparência de precisão a premissas frágeis. O trabalho ali é de descoberta.

## Indicadores de adoção

Contar especificações criadas incentiva produção de arquivos. As perguntas úteis observam efeito:

| Pergunta | Indicador possível |
|---|---|
| a intenção ficou clara antes do código? | proporção de implementações iniciadas após aceite versionado |
| os testes nasceram dos critérios? | cobertura de critérios por cenário, não cobertura de linhas |
| a implementação respeitou a especificação? | desvios encontrados na revisão de aderência |
| os artefatos permaneceram vivos? | mudanças de comportamento acompanhadas de atualização |
| o método melhorou o fluxo? | retrabalho, tempo até aceitação e defeitos escapados |
| os portões encontram problema real? | frequência com que um portão barra algo, contra aprovação automática |

Velocidade de geração isolada é a métrica mais perigosa do conjunto. Um time que passou de quatro para onze integrações por semana depois de adotar o agente, e no mesmo trimestre viu o retrabalho por defeito escapado subir de 8% para 21% das horas, tem um número que recomenda ampliar o uso e outro que recomenda investigar onde a intenção está se perdendo. Os dois juntos dizem que o sistema local ficou rápido e o fluxo global piorou.

## O que observar num piloto

Adotar o método na organização inteira antes de aprender com mudanças reais repete o erro que o próprio método tenta evitar, que é comprometer-se cedo demais com uma solução.

Um piloto útil compara classes semelhantes de tarefa e observa a cadeia inteira de entrega, não o tempo até a primeira geração de código. Começa com poucas mudanças representativas, declara quais etapas são obrigatórias e registra as exceções quando alguma é pulada.

Ao final, o time deve conseguir responder a quatro perguntas: qual artefato foi de fato consultado por alguém, qual portão mudou uma decisão, qual etapa não agregou valor, e quem mantém o processo quando a ferramenta mudar de versão. Se nenhum artefato foi consultado e nenhum portão mudou decisão alguma, o piloto produziu documentação e nada além disso.

!!! tip "Aplique agora"
    Escolha um dos seis indicadores da tabela acima e descubra se o seu time conseguiria medi-lo hoje, com os dados que já existem. O que não é mensurável com o instrumental atual não serve como critério de adoção.

## O que permanece humano

O método desloca trabalho sem transferir responsabilidade. Continuam sendo decisões de pessoas escolher quais problemas merecem investimento, ouvir usuários e reconhecer conflito de interesse, aceitar risco e suas consequências, decidir trade-offs arquiteturais, julgar se a evidência apresentada é suficiente e responder pelos efeitos em produção.

Agentes ampliam pesquisa, comparação, consistência, geração e revisão, e sustentam bem as relações entre muitos artefatos. Mas não têm mandato organizacional. A especificação é central porque pessoas autorizadas a adotaram como contrato e mantêm mecanismos para testá-la. Estar escrita em linguagem natural não tem parte nisso.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
