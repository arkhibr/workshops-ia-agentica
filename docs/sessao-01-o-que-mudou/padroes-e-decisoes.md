# Padrões e decisões

## Quando cada modo se justifica

Os três modos de [Conceitos](conceitos.md) não são degraus de maturidade que todo código precisa subir. São famílias de risco: a pergunta não é "qual modo é melhor", é "qual risco esta tarefa específica carrega".

| Critério | Favorece vibe coding | Favorece assistência de codificação | Favorece SDD |
|---|---|---|---|
| Reversibilidade | fácil de descartar | custo médio de retrabalho | difícil ou caro de desfazer |
| Tempo de vida esperado | horas, um experimento | semanas, uma feature | meses ou anos, parte do produto |
| Quantas pessoas vão mexer depois | só quem escreveu | o time atual | times futuros, sem contexto da decisão original |
| Regra de negócio envolvida | nenhuma, ou trivial | alguma, conhecida pelo time | crítica, com exceções que um prompt vago esquece |

A pergunta que resume a tabela: se esse código quebrar em produção, alguém vai conseguir reconstruir por que ele foi escrito daquele jeito? Vibe coding não deixa rastro para responder. Assistência de codificação deixa o código e o ticket. SDD deixa a especificação inteira.

## Anti-padrão: vibe coding tratado como produto

O anti-padrão não é usar vibe coding. É usar vibe coding e depois esquecer que foi usado. Os sintomas aparecem sempre na mesma ordem: o protótipo funciona na demonstração, alguém decide "já está pronto, só falta subir", ninguém escreve a especificação que existia apenas na cabeça de quem conversou com o agente, e o próximo bug custa uma investigação inteira porque não há teste, não há decisão registrada e não há ninguém que lembre por que aquele caso de borda foi ignorado.

A correção não é proibir vibe coding. É decidir o modo antes de começar, não depois que o protótipo já virou dependência de outras equipes.

## O caso Vetor sob este critério

A Vetor precisa de uma função de desconto por volume de pedido, usada no checkout de produção, com uma regra de teto e uma variação por tipo de cliente. Aplicando a tabela: baixa reversibilidade (afeta faturamento), tempo de vida longo (parte do checkout), várias pessoas vão mexer depois (time de pagamentos, time de relatórios financeiros), regra de negócio real com exceções. Essa combinação aponta para assistência de codificação disciplinada como piso mínimo aceitável — o que o Bloco 4 desta sessão pratica diretamente.

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
