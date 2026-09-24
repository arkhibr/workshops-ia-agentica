# Decomposição de requisitos: BR, FR e NFR

Uma especificação mal escrita esconde três perguntas diferentes: qual é a regra que o negócio impõe, o que o sistema precisa fazer, e sob que critério de qualidade ele precisa fazer isso. Confundir as três produz uma especificação de aparência completa, com decisões de negócio ausentes do texto escrito, e esta página trata do vocabulário que separa as três perguntas e do critério que torna cada resposta verificável.

## As três categorias

**Regra de negócio (BR, *business rule*)** é uma declaração sobre como o negócio funciona, independente de haver software ou não. [Ross](../referencia/bibliografia.md#ross-ed-business-rules-manifesto-2003), no *Business Rules Manifesto*, é categórico: "regras não são processo nem procedimento" e devem ser expressas de forma declarativa, sem sequenciamento implícito. "O desconto de um pedido nunca ultrapassa um teto fixo em reais" é uma regra de negócio: valeria mesmo que o cálculo fosse feito numa planilha, sem nenhum sistema.

**Requisito funcional (FR, *functional requirement*)** é o que o software precisa fazer para que a regra de negócio se cumpra. "O sistema calcula o desconto de um pedido a partir do valor total e do tipo de cliente" descreve comportamento observável do sistema, e não existe fora dele.

**Requisito não funcional (NFR, *non-functional requirement*)**, no vocabulário da norma [ISO/IEC/IEEE 29148](../referencia/bibliografia.md#isoiecieee-291482018), não descreve uma ação específica, mas um critério para julgar como o sistema executa a ação: desempenho, usabilidade, segurança. "O cálculo de desconto responde em menos de 100ms" acrescenta o limite de tempo sob o qual o cálculo, que já é o requisito funcional, precisa acontecer.

| Categoria | Pergunta que responde | Existiria sem o sistema? |
|---|---|---|
| BR | O que o negócio permite, exige ou proíbe? | Sim |
| FR | O que o sistema precisa fazer? | Não |
| NFR | Sob que critério de qualidade? | Não |

[Wiegers e Beatty](../referencia/bibliografia.md#wiegers-e-beatty-software-requirements-2013) tratam regra de negócio como categoria anterior aos requisitos de software: ela também vale para operação manual, fora de qualquer sistema, e é dela que os requisitos funcionais derivam como tradução em comportamento observável. O requisito não funcional entra depois dos dois, como restrição de qualidade sobre esse comportamento.

## O antipadrão da regra embutida

O sintoma mais comum é uma frase única, funcional na forma, que carrega várias regras de negócio dentro dela:

> "O sistema deve aplicar desconto de 20% para pedidos de atacado acima de R$ 10.000,00, respeitando o teto de R$ 1.000,00."

Três regras estão embutidas aí: a existência de uma faixa própria para o cliente de atacado, o valor de corte a partir do qual ela vale, e a prevalência do teto sobre qualquer faixa. Nenhuma tem linha própria, e por isso nenhuma tem identificador — quando a gerência comercial decidir baixar o corte para R$ 8.000,00, alguém precisa reabrir a especificação funcional inteira para localizar o número. A versão decomposta separa cada regra numa linha, com prefixo (`BR` para regra de negócio, `FR` para requisito funcional) e número:

```text
BR-03: Cliente do tipo atacado tem faixa de desconto própria,
       distinta da faixa por volume.
BR-04: A faixa de atacado é de 20% e se aplica a pedido com valor
       total acima de R$ 10.000,00.
BR-05: O desconto de um pedido nunca ultrapassa R$ 1.000,00,
       qualquer que seja a faixa aplicada.

FR-03: calcularDesconto aplica a faixa definida em BR-04 quando o
       cliente é do tipo atacado e o valor total supera o corte
       dessa faixa, e limita o retorno ao teto de BR-05.
       Para valorTotal = 12000 e tipoCliente = 'atacado', o retorno
       é 1000, porque 20% de R$ 12.000,00 excede o teto.
```

Baixar o corte para R$ 8.000,00 agora altera só BR-04, e criar uma faixa nova para outro tipo de cliente acrescenta uma BR sem reescrever BR-05, porque o teto foi declarado como restrição geral, e não como detalhe da faixa de atacado. Um agente que recebe a especificação decomposta trata BR-05 como restrição aplicável a qualquer faixa nova; diante da frase única do início desta seção, o mesmo agente pode ler o teto como parte só da regra de atacado, e deixar uma faixa nova sem limite.

!!! question "Antes de continuar"
    Releia a última especificação que você escreveu ou recebeu. Alguma frase que parecia requisito funcional era, na verdade, regra de negócio disfarçada — algo que valeria mesmo sem o sistema existir?

## Atributos de qualidade e requisito arquiteturalmente significativo

Um NFR solto começa quase sempre com um adjetivo: rápido, seguro, escalável, confiável. O primeiro passo é trocar o adjetivo por um atributo de qualidade nomeado, porque cada um tem sua própria forma de ser medido:

| Atributo | Pergunta que ele responde | Como se mede |
|---|---|---|
| Desempenho | Quão rápido, sob que carga? | Latência, vazão, tempo de resposta em percentil |
| Segurança | Que acesso é permitido, a quem, sob que condição? | Casos de autorização testados |
| Confiabilidade | O que acontece quando algo falha? | Taxa de erro tolerada, tempo de recuperação |
| Modificabilidade | Quão caro é mudar isso depois? | Número de módulos tocados por uma mudança típica |
| Observabilidade | Dá para saber o que o sistema fez, depois do fato? | Cobertura de log e rastro por decisão crítica |
| Usabilidade | Uma pessoa nova consegue operar sem ajuda? | Taxa de erro do usuário, tempo até a primeira tarefa |

Nem todo requisito não funcional exige uma decisão de arquitetura. Um requisito é **arquiteturalmente significativo (RAS)** quando atravessa mais de um componente, protege um atributo que o negócio já declarou prioritário, cria uma dependência relevante, ou torna uma mudança futura mais cara. "O relatório mostra até duas casas decimais" é um NFR real, mas fica contido numa função de formatação. "O cálculo de desconto responde em menos de 100ms mesmo com 500 pedidos simultâneos" já é significativo: atravessa a função de cálculo e quem a chama sob carga, e pode forçar decisão de cache ou de concorrência.

## Cenário de qualidade e função de aptidão

[Bass, Clements e Kazman](../referencia/bibliografia.md#bass-clements-e-kazman-software-architecture-in-practice-2021) formalizam o template que torna um NFR testável, o **cenário de qualidade**, em seis elementos: fonte (quem provoca o estímulo), estímulo (o que acontece), ambiente (sob que condição do sistema), artefato (o que é afetado), resposta (o que o sistema faz) e medida (como se mede se a resposta foi aceitável). Escrever os seis elementos, mesmo em uma frase corrida, é o que separa "o sistema deve ser rápido" de um requisito que um agente consegue implementar e alguém consegue testar sem adivinhar o resto.

Escrever um NFR verificável não garante que ele continue verdadeiro depois que o sistema muda. [Ford, Parsons, Kua e Sadalage](../referencia/bibliografia.md#ford-parsons-kua-e-sadalage-building-evolutionary-architectures-2023) definem **função de aptidão arquitetural** como uma avaliação objetiva de integridade de uma característica arquitetural: um teste automatizado que roda a cada mudança de código, em vez de uma revisão manual esporádica. Toda função de aptidão declara três elementos: o **limiar** (o valor que separa aceitável de inaceitável, o mesmo da medida do cenário), o **responsável** (quem é avisado quando o limiar é ultrapassado) e a **reação** (o que acontece quando ela falha — bloquear a promoção, abrir um alerta, reduzir a exposição). Um NFR escrito e nunca mais verificado é só uma promessa: alguém escreve "responde em menos de 100ms", o teste manual do dia passa, e ninguém percebe quando uma mudança seis meses depois faz a resposta subir para 400ms.

!!! tip "Aplique agora"
    Pegue um NFR vago que você já recebeu ("o sistema deve ser seguro"). Qual atributo da tabela acima ele está tentando nomear, que medida corresponderia a esse atributo, e quem seria avisado se essa medida deixasse de ser cumprida?

## O critério de verificabilidade

Uma especificação pode estar tecnicamente completa e ainda assim não permitir nenhuma conferência, porque não há como determinar, examinando o resultado, se ele a cumpriu. Uma especificação executável responde, para cada requisito, a mesma pergunta: existe um caso concreto que prova se este requisito foi atendido ou não? "O sistema deve calcular o desconto corretamente" não passa nesse critério, porque "correto" não tem caso de teste. "Para um pedido de R$ 12.000,00 de um cliente atacado, o desconto é R$ 1.000,00" passa: existe um valor de entrada e um valor de saída esperado, verificável por qualquer pessoa, inclusive por um agente que nunca viu a regra antes.

O [GitHub Spec Kit](../referencia/bibliografia.md#github-spec-kit) formaliza esse critério na prática: cada requisito funcional recebe um identificador e uma frase verificável, e a especificação só é aceita como pronta quando todo requisito tem essa forma. [Delimarsky](../referencia/bibliografia.md#delimarsky-spec-driven-development-with-ai-2025) chama a especificação de "contrato para como seu código deve se comportar" — o termo contrato indica que o cumprimento pode ser verificado por qualquer das partes, com base no texto, sem consulta a quem o escreveu. Uma especificação executável tem, para cada requisito, três elementos: a regra ou o requisito na forma declarativa (BR) ou funcional (FR), pelo menos um caso concreto (valor de entrada e resultado esperado), e o caso de fronteira, sempre que a regra tiver faixa, teto ou condição — o ponto em que duas leituras plausíveis divergem.

## Uma especificação pode estar certa e ainda produzir o sistema errado

A regra decomposta e o caso de fronteira protegem contra ambiguidade dentro do texto escrito, mas não protegem contra a pergunta que nunca foi feita. A Vetor precisava de uma regra nova: pedidos de clientes atacado acima de R$ 50.000,00 exigem aprovação manual antes do processamento. A especificação saiu assim:

```text
BR-01: Pedidos de clientes atacado com valor acima de R$ 50.000,00
       exigem aprovação manual antes do processamento.
FR-01: processarPedido verifica tipoCliente e valor. Se atacado e
       valor > 50000, marca status = 'aguardando_aprovacao'.
Caso de teste: pedido de R$ 60.000,00 de cliente atacado →
       status 'aguardando_aprovacao'. Passou.
```

O agente implementou exatamente isso, o teste passou, o código foi para produção. Duas semanas depois, um cliente atacado fez três pedidos de R$ 20.000,00 no mesmo dia, somando R$ 60.000,00. Nenhum, isoladamente, passou de R$ 50.000,00, nenhum foi para aprovação manual, e o time só descobriu quando o financeiro notou o volume acumulado no fechamento do mês. FR-01 implementa BR-01 com fidelidade perfeita, e o `BR` decomposto, com identificador próprio e caso de teste, não preveniu o incidente, porque a pergunta "por pedido isolado ou por cliente acumulado num período?" nunca foi feita na etapa de explorar e perguntar. As duas leituras eram plausíveis para a frase original, e a especificação escolheu uma sem que ninguém tivesse decidido conscientemente entre as duas.

!!! question "Antes de continuar"
    A falha do incidente acima está na especificação, na elicitação que a precedeu, ou em nenhuma das duas, por ser um risco que nenhum processo elimina de vez? Escreva sua posição em uma frase, antes de comparar com a de outra pessoa.

**Próxima página:** [Exemplo de aplicação de IA](decomposicao-de-requisitos-exemplo-de-aplicacao-de-ia.md).
