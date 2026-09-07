# Estudo de caso: a especificação que estava certa

Discussão em grupo, sem resposta certa preparada. O objetivo é o grupo chegar a um critério, não a uma opinião, sobre de quem é a responsabilidade quando uma especificação tecnicamente completa ainda produz o sistema errado.

## O incidente

A Vetor, a plataforma fictícia de e-commerce B2B usada nesta sessão, precisava de uma regra nova: pedidos de clientes atacado acima de R$ 50.000,00 passam por aprovação manual antes de serem processados. Alguém do time escreveu a especificação:

**BR-01.** Pedidos de clientes atacado com valor acima de R$ 50.000,00 exigem aprovação manual antes do processamento.

**FR-01.** `processarPedido(pedido)` verifica se `pedido.tipoCliente === 'atacado'` e `pedido.valor > 50000`; se sim, marca `pedido.status = 'aguardando_aprovacao'` em vez de prosseguir.

**Caso de teste:** pedido de R$ 60.000,00 de cliente atacado → status `'aguardando_aprovacao'`. Passou.

O agente implementou exatamente isso, o teste passou, o código foi para produção. Duas semanas depois, um cliente atacado fez três pedidos de R$ 20.000,00 no mesmo dia, somando R$ 60.000,00 — nenhum deles individualmente passou de R$ 50.000,00, nenhum foi para aprovação manual, e o time só descobriu quando o financeiro notou o volume acumulado no fechamento do mês.

## Onde a especificação estava, e não estava, errada

A especificação cumpriu exatamente o que dizia: por pedido, não por cliente, não por período. O teste que existia comprovava isso. Nada na revisão de código apontaria erro, porque não havia erro em relação ao que foi escrito — o `FR-01` implementa `BR-01` com fidelidade perfeita.

O problema é anterior à especificação: ninguém perguntou, na etapa de explorar e perguntar, se o limite de R$ 50.000,00 era por pedido isolado ou por cliente acumulado num período. As duas leituras são plausíveis para a frase original "pedidos... acima de R$ 50.000,00 exigem aprovação manual", e a especificação escolheu uma sem que ninguém tivesse decidido conscientemente entre as duas.

## Perguntas para orientar a discussão

- A especificação estava errada, ou a especificação estava certa e a pergunta certa nunca foi feita? Essas são a mesma coisa, ou o grupo consegue separar as duas responsabilidades?
- Quem deveria ter levantado a pergunta sobre acúmulo por período: quem escreveu a especificação, quem revisou, ou quem testou? O critério muda se o time tiver, ou não tiver, uma etapa formal de revisão de especificação antes da implementação?
- O caso de teste que existia (um pedido isolado de R$ 60.000,00) cobria exatamente o que a especificação dizia. Um caso de teste adicional, cobrindo acúmulo por período, teria exigido uma pergunta que ninguém fez, ou teria exigido uma especificação diferente? Em que ordem isso deveria ter acontecido?
- Esse incidente aconteceria do mesmo jeito se o pedido tivesse sido implementado por vibe coding, sem especificação nenhuma? A especificação formal preveniu esse erro, ou só deu a ele uma aparência de rigor que não tinha?

!!! question "Antes de continuar"
    Sem consultar o restante do grupo, escreva sua posição em uma frase: a falha está na especificação, na elicitação que a precedeu, ou em nenhuma das duas — é um risco que nenhum processo elimina de vez?

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
