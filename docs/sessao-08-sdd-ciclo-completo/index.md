# S8 — SDD: ciclo completo

**Bloco:** 3 — Execução

> **Pergunta-guia:** o que precisa sobreviver à conversa com o agente para que outra pessoa consiga manter o código depois?

## Problema

Especificação, plano e testes que não se conectam num ciclo executável viram documentação que ninguém segue. Cada artefato precisa alimentar o próximo, e a mudança precisa deixar rastro: quando alguém perguntar, seis meses depois, por que aquela regra existe, a resposta não pode estar só no histórico de um chat que ninguém guardou.

## Como usar este material

Estas páginas não são leitura prévia. O instrutor conduz a exploração dos conceitos ao vivo, intercalada com a prática. Chegar sem ter lido nada é a expectativa normal.

## Objetivos de aprendizagem

Ao final desta sessão, o participante deve ser capaz de:

1. **Executar** um ciclo SDD completo, da constitution ao código verificado, com os quatro artefatos canônicos.
2. **Distinguir** as quatro abordagens de SDD pelo artefato que cada uma preserva e pelo tipo de rigor que cada uma cobra.
3. **Classificar** uma prática como *spec-first*, *spec-anchored* ou *spec-as-source*.
4. **Escolher** a profundidade de processo proporcional ao risco da mudança, em vez de aplicar o pacote completo a tudo.
5. **Reconhecer** os antipadrões que transformam SDD em documentação cara que ninguém consulta.
6. **Propor** o que medir num piloto de adoção, sem confundir volume gerado com fluxo de entrega.

## O caso que nos acompanha: Vetor

A Vetor, plataforma fictícia de e-commerce B2B que atravessa o workshop, tem uma lacuna conhecida na função `calcularDesconto`: a faixa de 20% para clientes de atacado acima de R$ 10.000,00 nunca foi implementada. As Sessões 3 e 4 especificaram e formalizaram essa regra. Esta sessão fecha o ciclo até o código, com os artefatos conectados e a evidência que autoriza a integração.

## Roteiro da sessão (2h, das 10h às 12h)

| # | Página | Bloco | Tempo | Resultado esperado |
|---|---|---|---|---|
| 1 | [O ciclo e os quatro artefatos](ciclo-e-artefatos.md) | Teoria | 8 min | O que cada artefato decide e por que a ordem entre eles não é burocracia |
| 2 | [Quatro abordagens para o mesmo padrão](abordagens-sdd.md) | Teoria | 9 min | Spec Kit, OpenSpec, SPDD e Superpowers, e o que cada um preserva |
| 3 | [Escolher a abordagem e a profundidade](escolher-a-abordagem.md) | Teoria | 7 min | Dez critérios de comparação e a régua de profundidade proporcional ao risco |
| 4 | [Manter os artefatos vivos](artefatos-vivos.md) | Teoria | 7 min | Que mudança atualiza qual artefato, e por que regenerar às cegas destrói decisão |
| 5 | [Quando o SDD falha](quando-sdd-falha.md) | Teoria | 7 min | Os antipadrões, os casos em que o método não compensa e o que medir num piloto |
| 6 | [Exemplo arquitetural](exemplo-arquitetural.md) | Demonstração | 12 min | Ver o ciclo inteiro na Vetor, da constitution ao teste verde |
| 7 | [Estudo de caso](estudo-de-caso.md) | Discussão em grupo | 12 min | Julgar um ciclo que produziu todos os artefatos e ainda assim entregou errado |
| — | Intervalo | — | 5 min | — |
| 8 | [Oficina de ferramentas](oficina-de-ferramentas.md) | Prática guiada | 30 min | Rodar o ciclo Spec Kit de verdade sobre a Vetor, com os quatro artefatos versionados |
| 9 | [Exercícios](exercicios.md) | Prática avaliada | 18 min | Exercício-âncora: a faixa de atacado especificada, planejada, implementada e verificada |
| — | [Síntese e referências](sintese-e-referencias.md) | Fechamento | 5 min | Checklist, autoavaliação e fontes completas |
| | | | **120 min** | |

## Como conduzir

As cinco páginas de teoria somam 38 minutos. É o bloco mais conceitual do Bloco 3, e o risco de condução é transformá-lo em apresentação de ferramenta. A página das quatro abordagens existe justamente para impedir isso: o participante precisa sair sabendo que o Spec Kit é uma implementação de um padrão, não o padrão.

Na oficina, todos partem de `exemplo/vetor`, o mesmo projeto das sessões anteriores. O Spec Kit é instalado no clone local, não no repositório de trabalho de cada um. A transposição para o repositório real do participante entra como extensão no fim da oficina, nunca como caminho principal.

**Próxima página:** [O ciclo e os quatro artefatos](ciclo-e-artefatos.md).
