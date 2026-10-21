# Exercícios

Tente responder antes de abrir os blocos de feedback nos dois primeiros níveis. A progressão segue a Taxonomia de Bloom, do nível mais simples (recordar) ao mais exigente (criar). Os exercícios de Aplicar e de Criar usam material da ACME, a universidade fictícia desta sessão, e o exercício-âncora do nível Criar é a atividade de 43 minutos do segundo bloco da sessão.

## Recordar

### 1. Os cinco elementos de um caso

Nomeie os cinco elementos que um caso de uso de IA precisa declarar e indique qual deles corresponde à coluna "Conferência" das páginas por papel.

<details>
<summary>Ver resposta</summary>

Os cinco elementos são entrada, saída, pedido, conferência e decisão humana, e a coluna "Conferência" das páginas por papel corresponde ao quarto, que é a fonte contra a qual o resultado é comparado antes de circular.

</details>

### 2. As três colunas do mural

Escreva o critério para um cartão entrar na coluna "Já é rotina" do mural das equipes.

<details>
<summary>Ver resposta</summary>

O cartão entra em "Já é rotina" quando a equipe usa o caso de forma recorrente, em tarefa real, e alguém confere o resultado antes de usá-lo, e um caso usado com frequência sem conferência fica em "Já experimentamos".

</details>

## Compreender

### 3. A fronteira irregular

Um colega afirma que a IA sempre acelera o trabalho de quem a usa, e cita um estudo em que o ganho foi de 25,1% em velocidade. Explique, com base na página sobre como escolher um caso de uso, o que essa afirmação deixa de fora.

<details>
<summary>Ver resposta</summary>

O mesmo estudo, de Dell'Acqua et al., mediu 19% menos probabilidade de solução correta numa tarefa fora da capacidade do modelo. O efeito muda de sinal conforme a tarefa, e o limite entre tarefas favorecidas e prejudicadas não segue a dificuldade aparente. A afirmação do colega vale para o conjunto de tarefas dentro da fronteira e precisa ser medida para as tarefas da equipe.

</details>

### 4. Conferência integral e por amostra

Explique em que situação a conferência por amostra é suficiente e em que situação a conferência integral é necessária.

<details>
<summary>Ver resposta</summary>

A amostra basta quando o erro é barato de desfazer e a amostra representa o conjunto, como na contagem de temas de uma pesquisa de clima. A conferência integral é necessária para decisões, números e prazos que outras pessoas vão implementar, porque uma divergência isolada produz trabalho errado que ninguém questiona depois.

</details>

## Aplicar

### 5. Conferir uma ata gerada sem restrições

**Situação**

Esta situação usa o caso "Processar reuniões", do catálogo de Product Owner. A ata abaixo foi gerada a partir de uma reunião da ACME, a universidade fictícia usada nesta sessão, com um pedido sem restrições, que dizia apenas para transformar a transcrição em ata com decisões, ações e pendências, e a reunião, os nomes e as regras citadas são inventados e não reproduzem norma de nenhuma instituição.

**Transcrição**

```text
Priscila (PO): Hoje decidimos como o coordenador é avisado quando um relatório é rejeitado. Eu pensei em e-mail e aviso no portal.
Davi (desenvolvimento): O e-mail eu faço na sprint. O aviso no portal depende da nova tela, que ainda não existe.
Helena (financeiro): Só e-mail então, por enquanto. O coordenador tem que receber o aviso no mesmo dia da rejeição.
Priscila: Combinado, só e-mail, no mesmo dia.
Lucas (testes): Qual é o texto do e-mail?
Helena: O financeiro escreve o texto até a semana que vem.
Davi: Preciso saber se o e-mail leva o motivo da rejeição.
Priscila: Se o jurídico aprovar a inclusão do motivo, entra o motivo. Se não aprovar, vai só o aviso.
Lucas: Quantas tentativas de reenvio o coordenador tem?
Priscila: Três, mas isso ainda precisa de confirmação do financeiro.
Helena: Eu confirmo com a diretoria.
Davi: Alguém vai atualizar o manual do coordenador?
Priscila: Boa pergunta, a gente vê depois.
```

**Ata gerada, sem edição**

```markdown
# Ata de reunião: notificação de relatório rejeitado

**Participantes:** Priscila (PO), Davi (desenvolvimento), Helena (financeiro), Lucas (testes)

**Pauta:** definir como o coordenador é avisado quando um relatório é rejeitado.

## Decisões

1. O coordenador será avisado somente por e-mail nesta etapa. O aviso no portal fica fora do escopo, porque depende da nova tela, que ainda não existe.
2. O e-mail deverá ser enviado no mesmo dia da rejeição do relatório.

## Ações

| Responsável | Ação | Prazo |
| --- | --- | --- |
| Davi | Implementar o envio do e-mail | Sprint em andamento |
| Financeiro (Helena) | Redigir o texto do e-mail | Semana que vem |
| Helena | Confirmar com a diretoria o número de tentativas de reenvio | Não definido |

## Pendências

- **Motivo da rejeição no e-mail:** depende da aprovação do jurídico. Se aprovado, o e-mail inclui o motivo; se não, leva apenas o aviso. O responsável por consultar o jurídico não foi definido.
- **Número de tentativas de reenvio:** a proposta é de três tentativas, sujeita à confirmação do financeiro com a diretoria.
- **Manual do coordenador:** Davi perguntou quem o atualizará e a questão ficou sem responsável e sem prazo, com a indicação de que será tratada depois.
- **Aviso no portal:** deverá ser reavaliado após a entrega da nova tela, sem data prevista.
```

**Passos**

1. Leia a transcrição e liste, antes de ler a ata, as decisões, as ações com responsável e os pontos sem decisão que ela contém.
2. Leia a ata e compare cada linha com a sua lista.
3. Marque cada divergência como decisão alterada, responsável inventado, prazo convertido ou ampliado, ponto sem decisão registrado como decisão, ou texto que não consta da reunião.
4. Escreva uma restrição de uma linha que o pedido deveria conter para evitar a divergência que você considera mais grave.

<details>
<summary>Conferir depois de responder</summary>

A ata contém três divergências. A primeira é o prazo "Sprint em andamento", porque Davi disse apenas "na sprint" e a reunião não indica qual. A segunda é o responsável "Financeiro (Helena)", porque Helena atribuiu o texto à área e não a si mesma. A terceira é o item de pendência "Aviso no portal", porque a reunião não disse que o aviso seria reavaliado depois da nova tela, e a ata acrescentou essa decisão. As demais linhas correspondem à transcrição, inclusive os dois itens que a ata deixou sem responsável, a consulta ao jurídico e a atualização do manual.

</details>

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Lista feita antes da leitura da ata | 40% | A lista do passo 1 existe e foi escrita sem consultar a ata |
| Divergências localizadas e classificadas | 40% | Cada divergência aponta a linha da ata e a fala da transcrição |
| Restrição proposta | 20% | A restrição é uma instrução verificável e corresponde a uma divergência encontrada |

### 6. Classificar cinco cartões do catálogo

Escolha cinco cartões do catálogo do seu papel e classifique cada um segundo a tabela de critérios da [oficina](oficina-de-ferramentas.md). Para cada cartão em "Já é rotina", escreva a fonte de comparação que a equipe usa na conferência.

## Analisar

### 7. O que a conferência não encontraria

A conferência do exercício 5 compara cada linha da ata com a transcrição, e toda linha aprovada nessa comparação corresponde a uma fala. Descreva uma falha que essa conferência não encontraria mesmo assim, e indique o que mudaria na conferência para encontrá-la.

## Avaliar

### 8. Duas medidas para a ata sem conferência

Na ACME, a universidade fictícia usada nesta sessão, uma ata gerada por IA foi enviada ao time sem leitura e registrou o prazo de cinco dias úteis, quando a reunião havia decidido dez. A coordenação propõe duas medidas: a leitura obrigatória da ata pelo product owner antes do envio, ou a proibição do uso de IA para registrar decisões. Escolha uma, defenda a escolha em cinco linhas e indique o custo que ela impõe ao time.

## Criar

### 9. Exercício-âncora: um caso real e o pitch

**O que é:** a equipe aplica um caso de uso a uma tarefa real, confere o resultado e apresenta o pitch de oitenta segundos descrito na página [Pitch de um caso de uso](pitch-de-caso-de-uso.md). A atividade ocupa 23 minutos de preparação e 20 minutos de apresentações.

**Situação**

Cada equipe escolhe uma tarefa que realizaria na semana seguinte, com material sem dado pessoal nem sigiloso, e um caso do catálogo, ou do Experimento C da oficina, que se aplique a ela.

**Passos**

1. Em cinco minutos, a equipe escolhe a tarefa e o caso e declara a fonte de comparação para a conferência.
2. Em dez minutos, uma pessoa da equipe escreve o pedido com papel, tarefa, formato e restrições, e executa o caso no agente.
3. Em cinco minutos, a equipe confere o resultado contra a fonte declarada e registra cada divergência.
4. Em três minutos, a equipe prepara as cinco partes do pitch e decide se adota, ajusta ou descarta o caso.

**Critérios de avaliação**

| Critério | Peso | O que se espera |
|---|---:|---|
| Conferência executada e registrada | 40% | O pitch diz contra que fonte o resultado foi comparado e o que a comparação encontrou |
| Pedido com restrições | 25% | O pedido declara pelo menos uma restrição que impede o agente de preencher lacunas |
| Decisão com próximo passo | 20% | A equipe diz se adota, ajusta ou descarta o caso e declara um prazo |
| Respeito ao tempo | 15% | O pitch cabe nos oitenta segundos |

**Próxima página:** [Síntese e referências](sintese-e-referencias.md).
