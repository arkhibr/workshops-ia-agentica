# Evidência empírica de produtividade

Dois estudos mediram o efeito da IA sobre a produtividade de quem programa e chegaram a resultados opostos.

**Estudo 1.** [Peng et al. (2023)](../referencia/bibliografia.md#peng-et-al-copilot-productivity-2023) conduziram um experimento randomizado com 70 desenvolvedores profissionais implementando um servidor HTTP em JavaScript: o grupo com GitHub Copilot terminou a tarefa em 71 minutos contra 161 minutos do grupo de controle, um ganho de 55,8%. O efeito foi maior justamente para desenvolvedores menos experientes.

**Estudo 2.** O [METR, em 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025), testou uma situação diferente: 16 desenvolvedores experientes, cada um com cerca de cinco anos de trajetória nos próprios projetos maduros de código aberto, resolvendo 246 tarefas reais de manutenção. O resultado inverteu a expectativa: usar IA tornou a conclusão das tarefas 19% mais lenta. Os próprios desenvolvedores, depois de terminar, estimaram que a IA os havia deixado 20% mais rápidos, uma estimativa de sinal oposto ao da medição.

Os dois resultados são compatíveis, porque os estudos diferem na variável de maior peso, que é o tipo de tarefa: Peng et al. mediram a escrita de código novo e bem delimitado, e o METR mediu a manutenção de sistemas grandes que os participantes já conheciam a fundo. No primeiro tipo de tarefa o ganho aparece rápido. No segundo, sem disciplina, o desenvolvedor gasta mais tempo revisando e corrigindo a proposta do agente do que gastaria escrevendo o código diretamente.

### Três sintomas de uso indisciplinado

- **Inconsistente.** Duas pessoas usam o mesmo modelo e chegam a resultados muito diferentes. Uma resolve a tarefa inteira, a outra usa a ferramenta como um completador de código sofisticado. A diferença está em como cada uma pede ao modelo e no que cada uma configurou em volta dele, assunto da Sessão 2.
- **Aceite sem compreensão.** Código é aceito sem que quem aceitou entenda de fato o que ele faz. [Pearce et al. (2022)](../referencia/bibliografia.md#pearce-et-al-copilot-security-2022), em um estudo hoje seminal, submeteram o GitHub Copilot a 89 cenários de programação cobrindo as principais categorias de vulnerabilidade (CWE Top 25) e encontraram falha de segurança em cerca de 40% dos programas gerados. Quando esse código falha ou é explorado em produção, a equipe não tem protocolo de depuração e recorre a tentativa e erro.
- **Ad hoc.** O time não tem fluxo, vocabulário nem critério de aceitação em comum para o que significa um bom pedido à IA, e cada pessoa faz do próprio jeito.

!!! question "Antes de continuar"  
    Qual desses três sintomas apareceu no seu time na última semana? Pense num exemplo concreto, sem apontar culpados: o objetivo é reconhecer o padrão coletivo.

Na prática, use este critério: quanto mais o problema depende de conhecimento tácito do sistema, mais especificação explícita compensa escrever antes de pedir.

**Próxima página:** [A tese do Software 3.0](software-3-0.md).
