# Formas de delegar trabalho à IA

Um agente de IA é um sistema que recebe um objetivo, escolhe os passos para atingi-lo, usa ferramentas como busca, leitura de arquivos e chamadas a outros sistemas, observa o resultado de cada passo e decide o passo seguinte. O modelo de IA, como Claude ou GPT, é a parte do agente que interpreta texto e propõe a próxima ação, e o restante do agente, chamado no curso de arnês, reúne as instruções, as ferramentas disponíveis, a memória e as regras de execução, como explicado na [Sessão 2](../sessao-02-ambiente-agentico/arnes.md).

## Diferença entre fluxo de trabalho e agente

O texto [Building Effective Agents](../referencia/bibliografia.md#anthropic-building-effective-agents-2024), publicado pela Anthropic em dezembro de 2024, separa dois tipos de sistema com IA. Num fluxo de trabalho, um programa define a sequência de etapas antes da execução, e o modelo executa cada etapa prevista, por exemplo extrair campos de um documento e depois classificá-lo. Num agente, o modelo escolhe a próxima etapa a cada iteração, dentro de um conjunto de ferramentas autorizadas, por exemplo decidindo se precisa ler outro documento antes de responder.

## Quem escolhe o próximo passo

As formas de delegar trabalho da tabela diferem pelo responsável pela escolha do próximo passo, que pode ser a pessoa, um programa ou o próprio agente.

| Forma | Quem escolhe o próximo passo | Exemplo |
|---|---|---|
| Resposta assistida | A pessoa, depois de ler a resposta da IA | O sistema explica uma cláusula de contrato, e a pessoa decide o que fazer com a explicação |
| Fluxo de trabalho com IA | Um programa, que segue uma sequência definida antes da execução | O sistema extrai os campos de uma nota fiscal e a encaminha para a fila de pagamento |
| Agente com autonomia delimitada | O agente, dentro dos limites que a equipe autorizou | O agente investiga por que uma fatura diverge do pedido de compra e prepara a correção para uma pessoa aprovar |
| Vários agentes coordenados | Vários agentes, cada um com ferramentas ou informações próprias, sob a coordenação de um programa ou de outro agente | Um agente pesquisa fornecedores, outro compara preços e um terceiro consolida a recomendação |

Um mesmo processo pode usar formas diferentes em etapas diferentes. A [Sessão 1](../sessao-01-o-que-mudou/sistemas-agenticos.md) recomenda usar em cada etapa a forma mais simples que resolve a tarefa e só dar mais autonomia ao sistema quando a forma mais simples não for suficiente.

## Quando o trabalho delegado termina

O trabalho delegado termina quando o processo aceita o resultado, o que acontece depois de uma verificação e, nos casos que exigem, da aprovação de uma pessoa. O infográfico mostra as etapas com o exemplo de uma divergência de faturamento, em que o valor cobrado na fatura difere do valor do pedido.

![Ciclo de seis etapas do objetivo ao resultado aceito, ilustrado pela investigação de uma divergência de faturamento. A etapa 1, objetivo, recebe a fatura e a divergência, com escopo e critério de aceite. A etapa 2, contexto, reúne contrato e pedido com origem e acesso verificados. A etapa 3, ação, faz consulta e cálculo com ferramentas delimitadas. A etapa 4, verificação, produz proposta e evidências para validar antes de executar. A etapa 5, aprovação, registra a decisão quando exigida, vinculada à proposta. A etapa 6, resultado, entrega correção e comprovante aceitos pelo processo. Uma faixa inferior indica registrar estado, observar o resultado e retomar dentro dos limites.](assets/formas-de-delegacao.png)

| Etapa | O que acontece | Onde o curso tratou do assunto |
|---|---|---|
| 1. Objetivo | O agente recebe a tarefa com o escopo e o critério de aceite, que é a condição que o resultado precisa cumprir para ser aceito | A [Sessão 3](../sessao-03-exploracao-especificacao/index.md) exige o critério de aceite escrito antes de acionar o agente |
| 2. Contexto | O agente reúne os documentos necessários, como contrato e pedido, conferindo de onde vêm e se pode acessá-los | A [Sessão 2](../sessao-02-ambiente-agentico/engenharia-de-contexto.md) trata da escolha do que o agente recebe para ler |
| 3. Ação | O agente consulta e calcula usando apenas as ferramentas liberadas para a tarefa | A [Sessão 8](../sessao-08-skills-e-agentes/seguranca-e-credenciais.md) trata da permissão mínima, que libera apenas o acesso necessário |
| 4. Verificação | O agente prepara a proposta de correção com as evidências que a justificam | A [Sessão 6](../sessao-06-spec-kit-aprofundado/index.md) trata do teste que confere o resultado |
| 5. Aprovação | Uma pessoa aprova a proposta, quando a tarefa exige | A [Sessão 9](../sessao-09-governanca-de-skills-e-agentes/governanca-de-ia.md) define o nível de autonomia em que o agente prepara e uma pessoa aprova |
| 6. Resultado | A correção é registrada no sistema, com comprovante | Nas páginas seguintes desta sessão, o resultado aceito é a unidade de medida |

## Momento da intervenção humana

O ponto em que uma pessoa intervém é definido no desenho do processo, antes da execução, e corresponde ao momento em que a tarefa sai dos limites autorizados para o agente. Num estudo de 2026 com sistemas de agentes em uso real, [Measuring Agents in Production](../referencia/bibliografia.md#pan-et-al-measuring-agents-in-production-2026), 68% dos sistemas executavam no máximo dez passos antes de uma pessoa intervir, o que indica que as empresas usam agentes hoje em tarefas curtas e fáceis de conferir.

**Próxima página:** [Avaliação de números e promessas sobre agentes](avaliacao-de-numeros-e-promessas.md).
