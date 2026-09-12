# Quatro abordagens para o mesmo padrão

O Spec Kit implementa o desenvolvimento guiado por especificação, e é uma implementação entre outras. Quatro abordagens resolvem o mesmo problema, transformar intenção em evidência, com formas bem diferentes de organizar o trabalho. Conhecê-las evita confundir a sintaxe de um comando com o princípio que ele serve.

## SDD não designa uma prática única

A expressão *Spec-Driven Development* reúne fluxos com níveis muito diferentes de compromisso entre especificação e código. A taxonomia proposta por [Birgitta Böckeler](../referencia/bibliografia.md#bockeler-understanding-spec-driven-development-2025) evita que ferramentas distintas pareçam equivalentes só porque todas produzem arquivos Markdown:

1. **Spec-first.** A especificação melhora a primeira geração, mas pode ser arquivada ou abandonada depois. O código volta a ser a fonte operacional de verdade.
2. **Spec-anchored.** Especificação e código evoluem juntos. Cada mudança parte do estado documentado e reconcilia os dois lados antes de terminar.
3. **Spec-as-source.** A especificação é o artefato primário editável, e o código é uma projeção regenerável dela. É a forma mais ambiciosa e a mais difícil, porque a especificação precisaria expressar detalhe suficiente para reproduzir o comportamento sem decisões escondidas no código.

As quatro abordagens desta página se concentram entre *spec-first* e *spec-anchored*. Nenhuma delas alcança *spec-as-source* hoje, e desconfiar de quem promete isso é uma postura razoável.

!!! question "Antes de continuar"
    No seu time, depois que uma funcionalidade entra em produção, alguém volta ao documento que a descreveu? Se a resposta for não, o fluxo é *spec-first*, mesmo que a ferramenta prometa outra coisa.

## OpenSpec: a mudança como unidade

O [OpenSpec](../referencia/bibliografia.md#fission-ai-openspec) organiza o trabalho em torno da mudança, não de um fluxo completo por funcionalidade. O repositório tem dois espaços: um que descreve o comportamento atual do sistema e outro que contém uma pasta por mudança proposta, com proposta, especificação-delta, design e tarefas. Quando o trabalho termina, o delta é incorporado à especificação principal e a pasta da mudança é arquivada.

O ganho central é separar o estado do sistema da história das mudanças. Quem mantém o código lê a especificação consolidada para saber como o comportamento funciona hoje, e consulta a pasta arquivada quando precisa entender por que a regra foi introduzida. O delta também reduz a tentação de reescrever documentos inteiros a cada alteração.

O custo aparece na disciplina: o fluxo só permanece *spec-anchored* se a sincronização e o arquivamento forem hábitos reais, e a ferramenta permite prosseguir mesmo com tarefas incompletas. Sem uma camada de princípios acima das mudanças individuais, requisitos transversais como segurança e compatibilidade precisam de outro mecanismo.

## GitHub Spec Kit: intenção sob uma constitution

O Spec Kit, detalhado na [página anterior](ciclo-e-artefatos.md), adiciona uma camada que o OpenSpec não tem: a constitution do projeto, com princípios versionados que todo plano técnico precisa respeitar, verificados num portão explícito.

A separação rígida entre especificação funcional e plano técnico é o que impede que uma escolha prematura de tecnologia seja confundida com necessidade de negócio. Os portões intermediários também distribuem a carga de revisão: primeiro a ambiguidade, depois a arquitetura, depois a consistência entre artefatos.

O custo é o número de fases. Uma cadeia completa se justifica em funcionalidade crítica e transversal, e vira burocracia quando aplicada a todo ajuste pequeno. O time precisa de critério explícito para abreviar o fluxo, sob pena de cada pessoa improvisar uma versão diferente do método.

## SPDD: o prompt estruturado como contrato

O [Structured Prompt-Driven Development](../referencia/bibliografia.md#zhang-e-xia-structured-prompt-driven-development-2026), publicado por um time de tecnologia interna da Thoughtworks, trata o prompt como artefato de entrega versionado, revisável e mantido junto do código. Seu núcleo é o Painel REASONS, que organiza a especificação em sete dimensões:

| Dimensão | O que registra |
|---|---|
| **R**equirements | problema, escopo e definição de pronto |
| **E**ntities | conceitos do domínio e seus relacionamentos |
| **A**pproach | estratégia escolhida e trade-offs |
| **S**tructure | componentes, dependências e encaixe no sistema |
| **O**perations | passos de implementação concretos e verificáveis |
| **N**orms | convenções transversais de engenharia |
| **S**afeguards | limites e invariantes que não podem ser violados |

O Painel comprime num artefato só o que o Spec Kit distribui entre constitution, especificação e plano. O que distingue o método é o laço fechado: correção de lógica atualiza o prompt antes do código, e refatoração sincroniza do código de volta ao prompt, para que nenhum dos dois lados divirja em silêncio.

Duas ressalvas. A estrutura reduz mas não elimina variação, porque duas pessoas produzem Painéis diferentes a partir do mesmo requisito, e um Painel formalmente completo ainda pode estar semanticamente errado. E a sequência de testes diverge do TDD praticado nas Sessões 6 e 7: o fluxo de referência valida a interface antes da revisão detalhada e gera testes de unidade depois que a implementação estabiliza, o que conflita com política que exige teste guiando o design desde o início.

## Superpowers: disciplina de execução ao redor do agente

O [Superpowers](../referencia/bibliografia.md#vincent-e-prime-radiant-superpowers-2026) muda de categoria. Não é uma ferramenta de especificação, é um conjunto de habilidades combináveis acionadas automaticamente conforme a situação, com uma metodologia de execução em volta: levantamento de ideias e aprovação do design, cópia isolada do repositório, plano de tarefas pequenas, ciclo vermelho-verde-refatorar obrigatório, revisão em duas etapas e verificação antes de qualquer declaração de conclusão.

A disciplina é levada ao extremo: o próprio sistema apaga código escrito antes de o teste correspondente existir. A revisão separada de conformidade com o plano e de qualidade interna é o mesmo princípio dos dois eixos de verificação, chegando por outro caminho.

A diferença estrutural importa para classificá-lo corretamente. O Superpowers registra design e plano, então não se resume a "código e conversa", mas não mantém uma especificação consolidada do comportamento do sistema que receba deltas ao longo de várias mudanças. Ele é melhor entendido como disciplina de execução adjacente ao SDD, que pode consumir uma especificação produzida por outro processo.

Também é enganoso chamá-lo de leve. A governança documental é menor que a do Spec Kit, mas a exigência operacional é alta, e em bases sem testes rápidos a adoção custa investimento de engenharia antes de dar retorno.

## O que muda e o que não muda

As quatro concordam no princípio e divergem no mecanismo. Todas separam intenção de execução. Todas preservam alguma forma de evidência antes de considerar o trabalho concluído. Todas mantêm com a pessoa a autoridade sobre decisões que o agente não deveria tomar sozinho.

O que muda é onde o contrato mora, quantos portões existem e se o comando é digitado ou disparado automaticamente. A [página seguinte](escolher-a-abordagem.md) compara as quatro sob dez critérios e oferece a régua para escolher.

**Próxima página:** [Escolher a abordagem e a profundidade](escolher-a-abordagem.md).
