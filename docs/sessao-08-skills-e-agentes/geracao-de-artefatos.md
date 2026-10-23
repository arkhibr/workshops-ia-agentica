# Geração de artefatos

Um artefato é o arquivo que uma skill ou um agente entrega ao final da tarefa, como um registro de decisão, uma planilha, um relatório, um documento ou um trecho de código. Esta página trata de como declarar o modelo do artefato, de como conferi-lo por script e de como organizar o laço de correção, porque a qualidade de uma skill é verificável no artefato que ela produz. A página preenche, na [ficha de requisitos](index.md#a-ficha-de-requisitos), a linha "Artefato e conferência".

## O artefato como saída conferível

A Sessão 7 apresentou os cinco elementos de um caso de uso: entrada, saída, pedido, conferência e decisão humana. Numa skill, o artefato é a saída, e o quarto elemento, a conferência, é a fonte contra a qual o artefato é comparado antes de circular. Um artefato sem conferência declarada herda o problema descrito na [Sessão 7](../sessao-07-casos-de-uso-por-papel/como-escolher-um-caso-de-uso.md): circula na confiança de quem o gerou.

A conferência de um artefato tem duas camadas que dependem de quem as executa. A camada estrutural verifica o que um script consegue decidir sem interpretar o texto, como seções obrigatórias, campos preenchidos, formato de data e referências existentes. A camada de conteúdo verifica o que só uma pessoa decide, como a correção de uma consequência atribuída a uma opção, e permanece como decisão humana nomeada.

## Declarar o modelo do artefato

A [documentação de boas práticas](../referencia/bibliografia.md#anthropic-skill-authoring-best-practices-documentacao) descreve dois padrões para o formato da saída, e a escolha segue a mesma regra do grau de liberdade das instruções.

| Padrão | Quando usar | Exemplo de instrução |
|---|---|---|
| Modelo estrito | Formato de API, de integração ou de documento com campos fixos | "Use sempre exatamente esta estrutura de seções" |
| Modelo flexível | A adaptação ao conteúdo é útil | "Este é um formato padrão razoável, ajuste as seções conforme a análise" |

Quando a qualidade da saída depende de o agente ver o estilo esperado, a documentação recomenda o padrão de exemplos: pares de entrada e saída, como num pedido comum. Exemplos transmitem o estilo e o nível de detalhe com mais clareza que uma descrição escrita.

## Conferir por script

A documentação recomenda o padrão plano, validação e execução para operações em lote, mudanças destrutivas e regras de validação complexas. O agente cria primeiro um plano em formato estruturado, um script valida esse plano, e só então a execução ocorre. O ciclo completo fica: analisar, criar o plano, validar o plano, executar e verificar o resultado.

Os benefícios listados são a detecção antecipada de erros, a verificação objetiva por máquina, o planejamento reversível, porque o agente itera sobre o plano sem tocar nos originais, e a depuração clara, porque a mensagem de erro aponta o problema específico. A mesma documentação orienta escrever o validador com mensagens detalhadas, como "campo 'data_decisao' ausente, campos disponíveis: titulo, status, data_da_decisao", porque a mensagem é o que o agente lê para corrigir o artefato.

Na instrução da skill, vale indicar de forma explícita se o agente deve executar o script ou ler o código dele como referência. A execução é o caso comum, e o código do script não entra no contexto.

## Laço de correção

O laço consiste em gerar o artefato, executar o validador, corrigir os erros apontados e executar o validador de novo até a aprovação. A documentação afirma que esse padrão melhora muito a qualidade da saída e o aplica também sem código, usando um guia de estilo como validador: o agente redige, compara com a lista de verificação, corrige e repete. A skill deve declarar o critério de parada, como "somente prosseguir quando todos os requisitos forem atendidos". Este material acrescenta a recomendação de declarar também um limite de iterações, por exemplo três, para que o laço não consuma tokens sem convergir.

![Cinco etapas em sequência: o modelo do artefato, o agente que gera o artefato, o script que confere a estrutura na camada estrutural, a pessoa que confere o conteúdo na camada de conteúdo e o artefato que circula. Uma seta tracejada leva do script de volta ao agente quando há erros apontados, com limite de iterações, por exemplo três, e um critério de parada declarado no rodapé.](assets/laco-de-conferencia-em-duas-camadas.png)

## Que forma de conferência cada artefato pede

A tabela abaixo é uma síntese deste material e não uma classificação da documentação.

| Artefato | Conferência por script | Conferência por pessoa |
|---|---|---|
| Registro de decisão em Markdown | Seções obrigatórias, status válido, data no formato esperado | Se as consequências decorrem da decisão |
| Planilha | Recalcular totais com script e comparar com a planilha | Se os critérios de agregação servem ao uso |
| Código | Compilar e executar os testes | Se os testes cobrem o comportamento que importa |
| Relatório de texto | Citações e números presentes na fonte | Se a conclusão se sustenta nos dados |
| Apresentação ou documento formatado | Abrir o arquivo e verificar estrutura | Se a mensagem atende ao público |

## Documentos prontos

A Anthropic publica skills prontas para gerar apresentações (`pptx`), planilhas (`xlsx`), documentos de texto (`docx`) e arquivos PDF, disponíveis no claude.ai e na API. A [documentação das skills](../referencia/bibliografia.md#anthropic-agent-skills-documentacao) informa que essas skills de documento não estão disponíveis no Claude Code, que oferece skills personalizadas baseadas em arquivos. Quem precisa dessas saídas no Claude Code cria a própria skill ou usa as skills de documento no claude.ai, e em ambos os casos a conferência do artefato continua sendo declarada.

Artefatos de que outras pessoas dependem, como registros de decisão e especificações, devem ficar no repositório e ser atualizados junto com o código. A [Sessão 10](../sessao-10-sdd-ciclo-completo/artefatos-vivos.md) trata de quais mudanças atualizam qual artefato.

!!! abstract "Linha da ficha"
    Artefato e conferência:

    - Que artefato é gerado, em que formato e com que modelo, estrito ou flexível?
    - O que o script confere por conta própria, e com que limite de iterações?
    - O que só uma pessoa decide, e quem é essa pessoa?

**Próxima página:** [Escolha de modelos](escolha-de-modelos.md).
