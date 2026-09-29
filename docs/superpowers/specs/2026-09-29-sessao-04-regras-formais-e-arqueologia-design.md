# Redesenho da Sessão 04: regras formais e arqueologia de regras

**Data:** 29 de setembro de 2026  
**Escopo:** conteúdo, navegação e recursos visuais da Sessão 04  
**Público:** participantes do workshop de engenharia agêntica da FUNDEP

## Resultado esperado

A Sessão 04 passa a ensinar dois percursos complementares. O primeiro transforma uma política escrita em prosa em um modelo verificável de regras. O segundo recupera regras já cristalizadas em código SQL. Ao final, o participante consegue separar conceitos, fatos e tipos de regra; registrar evidências e incertezas; produzir sentenças SBVR, tabelas de decisão e casos de teste; e distinguir formalização de descoberta.

A sessão continua com duas horas de relógio, das 10h às 12h, sendo 115 minutos de conteúdo e cinco minutos de intervalo.

## Decisões editoriais

### Tema 1 — Regras formais com IA

O tema reúne SBVR, sentenças controladas e tabelas de decisão em um único processo. A teoria introduz, nesta ordem:

1. conceitos, termos e definições;
2. tipos de fato e instâncias de fato;
3. regras estruturais de classificação e derivação;
4. regras operativas de obrigação, proibição e permissão condicionada;
5. exceções, conflitos, lacunas, evidência e confiança;
6. normalização em regras atômicas;
7. organização das combinações em tabela de decisão;
8. derivação de exemplos e testes.

O texto usa **SBVR** como sigla normativa. Quando uma ocorrência de “SVBR” for relevante para busca ou orientação do participante, ela será identificada como grafia trocada, sem ser adotada como nome do padrão.

### Exemplo conduzido — IRPF

O exemplo abandona o desconto da Vetor e usa um cenário didático de cálculo de Imposto de Renda da Pessoa Física. Ele começa por um “ninho de regras”: um texto fictício, denso e deliberadamente mal estruturado, mas sem se apresentar como transcrição literal da legislação.

O instrutor conduz a decomposição do texto em:

- glossário de conceitos;
- fatos que relacionam os conceitos;
- regras estruturais;
- regras operativas;
- exceções e precedência;
- parâmetros temporais e monetários;
- tabela de decisão;
- exemplos de fronteira e casos de teste.

Valores usados apenas para ensinar serão rotulados como hipotéticos. O exemplo não deve ser confundido com orientação tributária nem com calculadora fiscal válida.

### Exercício de IA Geral — nova legislação tributária

O exercício usa um trecho complexo de uma regra da reforma da tributação do consumo no Brasil, selecionado de fonte pública primária e estável, preferencialmente legislação publicada no Planalto, atos oficiais ou material normativo da Receita Federal. A versão final deve registrar a data de acesso e ligar diretamente para a fonte.

O material inclui:

- um texto-base complexo, com indicação clara do que é transcrição, adaptação ou síntese;
- a referência pública;
- um prompt pronto para produzir um mapa de regras;
- uma folha de trabalho para separar conceitos, fatos, regras estruturais, regras operativas, exceções, conflitos, lacunas, evidências e confiança;
- critérios de revisão humana do mapa produzido pela IA.

O agente organiza e aponta perguntas. Ele não decide a interpretação jurídica quando a fonte admite mais de uma leitura.

### Exercício de IA Especialista — testes em TDD

O exercício especialista reutiliza o mapa de regras do exercício geral. O participante primeiro confirma a separação entre conceitos, fatos e tipos de regra. Depois pede à IA que proponha casos de teste antes da implementação, seguindo TDD.

Cada caso deve conter:

- identificador da regra de origem;
- cenário e dados de entrada;
- resultado esperado;
- fronteira ou partição coberta;
- justificativa;
- indicação de lacuna quando o resultado não puder ser deduzido da fonte.

O exercício cobre caminho nominal, limites, exceções, sobreposições e ausência de informação. Não exige implementar um motor tributário.

### Tema 2 — Arqueologia de regras em código-fonte

O segundo tema não terá trilhas Geral e Especialista. Todos trabalham com SQL realista e autocontido, longo o bastante para conter regras implícitas, mas pequeno o bastante para ser examinado durante a aula.

O artefato deve conter elementos típicos de arqueologia:

- `CASE` aninhado;
- condições repetidas;
- valores mágicos;
- `JOIN` que altera elegibilidade;
- tratamento de `NULL`;
- precedência implícita pela ordem das condições;
- filtro que elimina casos sem explicar a regra de negócio.

O leitor usa uma ferramenta de arqueologia de regras assistida por IA para produzir:

1. inventário de conceitos e fatos;
2. catálogo de regras em SBVR;
3. evidência precisa por arquivo e intervalo de linhas;
4. nível de confiança e questões para o especialista do domínio;
5. tabela de decisão quando houver combinações;
6. casos de teste rastreáveis às regras recuperadas.

A página será agnóstica de fornecedor. O prompt e o contrato de saída devem funcionar com um agente capaz de ler arquivos e citar linhas.

## Arquitetura de páginas

A navegação nova substitui as oito páginas temáticas atuais por seis páginas:

1. `index.md` — visão geral, objetivos, agenda e orientação de condução;
2. `regras-formais-conceitos.md` — SBVR, fatos, tipos de regra e tabelas de decisão;
3. `regras-formais-exemplo-irpf.md` — ninho de regras e decomposição conduzida;
4. `regras-formais-exercicio-geral.md` — regra da nova tributação e mapa de regras;
5. `regras-formais-exercicio-especialista.md` — casos de teste em TDD;
6. `arqueologia-de-regras-sql.md` — conceitos, artefato SQL e exercício único;
7. `sintese-e-referencias.md` — síntese, autoavaliação e fontes.

As páginas antigas serão removidas depois que todos os links internos, a navegação e os testes apontarem para a nova estrutura. O arquivo de planilha de comissões deixa de integrar a sessão; sua exclusão só ocorrerá após a verificação de que nenhuma outra página o referencia.

## Sistema visual

Os recursos visuais devem ensinar relações, não apenas decorar a página. Serão produzidos como imagens no diretório `docs/sessao-04-regras-formais-com-ia/assets/`, com texto alternativo específico e legenda que explique como ler cada figura.

Conjunto previsto:

1. **Anatomia do mapa de regras:** conceitos → fatos → regras estruturais e operativas → tabela → testes.
2. **Desmonte do ninho do IRPF:** texto entrelaçado sendo separado em cartões de tipos diferentes.
3. **Fluxo do exercício tributário:** fonte pública → extração → classificação → mapa → revisão humana → testes.
4. **Arqueologia de SQL:** código → evidências por linha → catálogo SBVR → tabela de decisão → casos de teste.

A direção visual usa diagramas educacionais limpos, orientação horizontal, alto contraste, poucos rótulos e paleta compatível com o verde do Material for MkDocs. Textos longos permanecem no HTML/Markdown, fora das imagens. Se a geração raster não reproduzir rótulos com precisão suficiente, o infográfico correspondente será implementado como diagrama nativo ou composição HTML/CSS; a imagem gerada não será publicada com texto incorreto.

## Formatação das páginas

Cada página terá:

- abertura com objetivo e produto esperado;
- navegação interna curta para páginas extensas;
- blocos de destaque para risco, decisão humana e evidência;
- tabelas com colunas consistentes;
- prompts em blocos copiáveis;
- exemplos antes/depois apresentados por estágio, não como julgamento de texto “ruim” e “bom”;
- seção “Evidência a entregar” nos exercícios;
- transição explícita para a página seguinte.

O conteúdo deve ser autocontido. A primeira ocorrência de SBVR, TDD, tabela de decisão e arqueologia de regras em cada página recebe uma definição curta.

## Distribuição de tempo

O roteiro preservará 115 minutos de conteúdo:

- abertura e modelo conceitual: 20 minutos;
- exemplo conduzido de IRPF: 25 minutos;
- exercício geral: 20 minutos;
- intervalo: 5 minutos;
- exercício especialista em TDD: 20 minutos;
- arqueologia de regras em SQL: 25 minutos;
- síntese: 5 minutos.

O total de conteúdo é 115 minutos; o intervalo completa as duas horas.

## Fontes e precisão

Antes da redação final, serão verificadas fontes públicas atuais para a legislação tributária escolhida. A página distinguirá:

- texto legal citado, limitado ao trecho necessário;
- paráfrase didática;
- cenário ou valor hipotético;
- interpretação que precisa de validação jurídica.

As referências normativas e metodológicas entram em `sintese-e-referencias.md` e, quando ainda ausentes, em `docs/referencia/bibliografia.md`.

## Verificação e critérios de aceite

A implementação estará completa quando:

1. a navegação refletir exatamente os dois temas;
2. nenhuma página descrever as trilhas antigas ou usar “TDDD”;
3. todos os exercícios pedirem separação explícita de conceitos, fatos e tipos de regra;
4. o exemplo de IRPF contiver o ninho e todas as etapas de decomposição;
5. o exercício geral trouxer fonte pública primária, texto complexo, prompt e critérios de revisão;
6. o exercício especialista gerar casos de teste antes da implementação, com rastreabilidade;
7. o tema de arqueologia usar SQL e gerar SBVR mais casos de teste, sem divisão Geral/Especialista;
8. as ilustrações tiverem texto alternativo, legenda e referências válidas;
9. horários totalizarem 115 minutos de conteúdo;
10. a revisão anti-cacoetes e os três comandos do portão de qualidade terminarem sem erro;
11. a renderização local for inspecionada nas larguras desktop e móvel.

## Fora de escopo

- construir ou recomendar uma calculadora fiscal para uso real;
- oferecer interpretação jurídica definitiva;
- implementar um motor completo de regras tributárias;
- vincular a aula a uma ferramenta comercial específica;
- manter a planilha de comissão ou o desconto da Vetor como caso central desta sessão.
