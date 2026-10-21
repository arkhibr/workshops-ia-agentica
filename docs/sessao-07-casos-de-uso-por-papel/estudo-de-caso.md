# Estudo de caso: a ata que ninguém conferiu

Este estudo de caso apresenta um dilema sobre a conferência de resultados de IA numa tarefa de rotina, o resumo de reunião, e serve para leitura depois da aula, com discussão em grupo se houver tempo. O caso é fictício e se passa na ACME, a universidade fictícia usada nesta sessão. Ele não descreve fato real, e as regras citadas não reproduzem norma de nenhuma instituição.

## O caso

Marina é product owner do time que mantém o portal de prestação de contas de projetos de pesquisa da ACME. Desde o início do semestre, ela transforma a transcrição de cada reunião de refinamento em ata com um agente de IA e envia a ata ao time e à área financeira no mesmo dia. A primeira versão do processo incluía a leitura da ata por ela antes do envio. Em março, com a agenda cheia, Marina passou a enviar a ata sem a leitura, porque as dez atas anteriores não tinham apresentado erro.

Na reunião de 14 de maio, o time discutiu o prazo para o coordenador de projeto enviar o relatório trimestral. A proposta inicial foi de cinco dias úteis, o representante do financeiro objetou que a conciliação bancária só termina por volta do oitavo dia útil, e a decisão final foi de dez dias úteis. A ata gerada registrou cinco dias úteis, sem menção à mudança, e foi enviada sem leitura.

O time de desenvolvimento implementou o prazo de cinco dias úteis na sprint seguinte. O primeiro trimestre depois da entrega fechou com quarenta e um relatórios enviados antes da conciliação, e o financeiro precisou pedir correção em trinta e dois deles. O coordenador de um dos projetos recebeu a cobrança de uma inconsistência que o sistema, funcionando como especificado, havia produzido.

## O dilema

Marina reconhece o erro da ata e defende que a ferramenta deu suporte durante o semestre inteiro: foram doze reuniões, onze atas sem divergência e uma com erro. O representante do financeiro argumenta que a ata é o documento que o time usa para decidir o que implementar, e que uma ata sem conferência é um documento sem autor. O líder do time de desenvolvimento afirma que o time deveria ter percebido a divergência com o que Caio, do financeiro, havia dito em reunião, e que o time implementou o que estava escrito sem consultar ninguém.

A coordenação do projeto propõe duas medidas. A primeira exige que toda ata gerada por IA seja lida e assinada pelo product owner antes do envio. A segunda proíbe o uso de IA para registrar decisões e limita o uso a rascunhos de pauta.

## Perguntas para orientar a discussão

1. A quem cabe a responsabilidade pela decisão errada, e o que muda nessa resposta quando o autor da ata é um agente?
2. O que a conferência da ata exigiria de Marina em minutos por reunião, e o que a [demonstração desta sessão](exemplo-arquitetural.md) indica sobre onde esse tempo é gasto?
3. A primeira medida é suficiente? Descreva um erro que ela não evitaria.
4. A segunda medida elimina o risco ou o transfere? Que outra etapa passaria a registrar as decisões?
5. O time de desenvolvimento tinha meios de perceber a divergência? Que prática do time, e não da ata, a teria revelado?
6. Que critério distingue um caso de uso em que a conferência pode ser por amostra de um caso em que precisa ser integral?

## Material de apoio

A [página sobre como escolher um caso de uso](como-escolher-um-caso-de-uso.md) traz os critérios de risco e de conferência que sustentam a discussão da pergunta 6.

**Próxima página:** [Oficina de ferramentas](oficina-de-ferramentas.md).
