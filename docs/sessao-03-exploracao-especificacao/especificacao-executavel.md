# Especificação executável

Uma especificação pode estar tecnicamente completa e ainda assim não servir para nada, porque não dá para saber, olhando o código gerado, se ele a cumpriu. O critério desta página separa especificação que um agente consegue seguir sem interpretar de resumo do pedido reescrito com letras maiúsculas.

## O critério: verificável, não só descritivo

Uma especificação executável responde, para cada requisito, a mesma pergunta: existe um teste, um caso concreto, que prova se este requisito foi atendido ou não? "O sistema deve calcular o desconto corretamente" não passa nesse critério — "correto" não tem caso de teste, é uma opinião disfarçada de requisito. "Para um pedido de R$ 12.000,00 de um cliente atacado, o desconto é R$ 1.000,00" passa: existe um valor de entrada e um valor de saída esperado, verificável por qualquer pessoa, inclusive por um agente que nunca viu a regra antes.

O [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit) formaliza esse critério na prática: cada requisito funcional do `spec.md` recebe um identificador (`FR-001`, `FR-002`) e uma frase no padrão "o sistema deve...", e a especificação só é aceita como pronta quando todo requisito tem essa forma verificável. [Delimarsky](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025), no post de lançamento do Spec Kit, chama a especificação de "contrato para como seu código deve se comportar" — um contrato, diferente de uma sugestão, permite dizer objetivamente se foi cumprido.

## Estrutura mínima de uma especificação executável

Três elementos, para cada requisito:

- **A regra ou o requisito em si**, na forma declarativa (BR) ou funcional (FR) da página anterior.
- **Pelo menos um caso concreto** que ilustra a regra em ação: um valor de entrada e o resultado esperado, não uma descrição do comportamento em abstrato.
- **O caso de fronteira**, sempre que a regra tiver faixa, teto ou condição — é aí que a ambiguidade de verdade mora, como um teto de desconto ou uma faixa de valor por volume costumam revelar.

Uma especificação sem exemplo concreto deixa a interpretação do valor de fronteira para quem lê depois — e "quem lê depois", quando o pedido vai para um agente, é o próprio agente, decidindo sozinho.

Para um requisito não funcional, o "caso concreto" não é um par entrada/saída simples — é o [cenário de qualidade completo](atributos-de-qualidade-e-ras.md#cenario-de-qualidade-o-template-que-torna-um-nfr-testavel): fonte, estímulo, ambiente, artefato, resposta e medida. Um NFR sem esses seis elementos tem o mesmo problema de um FR sem caso concreto: parece uma especificação, mas não dá para saber se foi cumprido.

!!! question "Antes de continuar"
    Pegue a última especificação que você escreveu. Para o requisito mais importante dela, existe um valor de entrada e um valor de saída esperado escritos, ou só uma descrição do comportamento?

## O antipadrão da especificação que é só o pedido reescrito

O sintoma é fácil de reconhecer: a especificação tem a mesma quantidade de informação que o pedido original, só que organizada em tópicos e com títulos em negrito. "Ative o desconto de atacado" vira "**Requisito:** ativar o desconto de atacado", sem nenhum valor concreto, sem faixa, sem teto, sem caso de fronteira — o trabalho de explorar e perguntar da primeira página desta sessão nunca aconteceu, só ganhou formatação de especificação.

O teste rápido para detectar esse antipadrão: dê a especificação para alguém que nunca ouviu falar do domínio e pergunte se essa pessoa consegue escrever os casos de teste sem fazer nenhuma pergunta adicional. Se a resposta for não, a especificação ainda não é executável — é o pedido original com roupa nova.

!!! tip "Aplique agora"
    Escreva, em três linhas, a especificação executável para um pedido vago do seu próprio backlog (ou, na falta de um, "adicione um limite de tentativas de login"): a regra, um caso concreto e o caso de fronteira. Compare com o que a [Oficina de ferramentas](oficina-de-ferramentas.md) desta sessão vai pedir.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
