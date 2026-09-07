# Evidência empírica de produtividade

Dois estudos mediram o efeito da IA sobre a produtividade de quem programa e chegaram a resultados opostos.

Estudo 1 - [Peng et al. (2023)](../referencia/bibliografia.md#peng-et-al-copilot-productivity-2023) conduziram um experimento randomizado com 70 desenvolvedores profissionais implementando um servidor HTTP em JavaScript: o grupo com GitHub Copilot terminou a tarefa em 71 minutos contra 161 minutos do grupo de controle, um ganho de 55,8%. O efeito foi maior justamente para desenvolvedores menos experientes.

Estudo 2 - O [METR, em 2025](../referencia/bibliografia.md#metr-experienced-developer-productivity-2025), testou uma situação diferente: 16 desenvolvedores experientes, cada um com cerca de cinco anos de trajetória nos próprios projetos maduros de código aberto, resolvendo 246 tarefas reais de manutenção. O resultado inverteu a expectativa: usar IA tornou a conclusão das tarefas 19% mais lenta. Mais revelador ainda, os próprios desenvolvedores, depois de terminar, estimaram que a IA os havia deixado 20% mais rápidos — o oposto exato do que os dados mediram.

A contradição entre os dois estudos não invalida nenhum dos dois. Ela aponta a variável que mais importa: tarefa nova e bem delimitada versus manutenção de um sistema grande que o desenvolvedor já conhece de cor. O ganho de piso do Bloco seguinte aparece rápido no primeiro caso; no segundo, sem disciplina, o tempo gasto revisando e corrigindo a proposta do agente supera o tempo que teria sido gasto escrevendo o código direto.

### Os três sintomas do time que ainda não saiu da primeira linha

- **Inconsistente.** Alguns desenvolvedores extraem resultados excelentes do mesmo modelo que outros usam apenas como um completador de código sofisticado. A causa está em como cada um pede ao modelo e ausência de Arnês (Harness).
- **Sem rede de proteção.** Código é aceito sem que quem aceitou entenda de fato o que ele faz. [Pearce et al. (2022)](../referencia/bibliografia.md#pearce-et-al-copilot-security-2022), em um estudo hoje seminal, submeteram o GitHub Copilot a 89 cenários de programação cobrindo as principais categorias de vulnerabilidade (CWE Top 25) e encontraram falha de segurança em cerca de 40% dos programas gerados. Quando esse código quebra ou é explorado em produção, não há protocolo de depuração, só tentativa e erro.
- **Ad hoc (De qualquer jeito).** Não existe fluxo, vocabulário ou critério de aceitação compartilhado entre o time para o que "um bom pedido à IA" significa.

!!! question "Antes de continuar"  
    Qual desses três sintomas apareceu no seu time na última semana? Pense num exemplo concreto, sem apontar culpados: o objetivo é reconhecer o padrão coletivo.

A régua prática: quanto mais o problema depende de conhecimento tácito do sistema, maior a dose de especificação explícita que compensa.

**Próxima página:** [A tese do Software 3.0](software-3-0.md).
