# S7 — Estratégias avançadas de teste

**Bloco:** 3 — Execução

## Problema

Testar tudo com a mesma profundidade desperdiça esforço em partes de baixo risco e deixa partes críticas subtestadas.

## Intenção metodológica

Teste de propriedade (FsCheck em C#, fast-check em JavaScript/TypeScript) para verificar invariantes em vez de exemplos isolados. Teste de mutação (Stryker.NET, StrykerJS) para medir se a suíte realmente detecta defeitos, não só se cobre linhas. Teste de contrato para dependências entre serviços. A decisão central é estratégica: onde investir profundidade de teste, e onde um teste simples já basta.

## Ao final desta sessão, o participante consegue

Definir uma estratégia de teste por risco, combinando propriedade, mutação e contrato conforme a criticidade de cada parte do sistema.

---

> Conteúdo completo (roteiro-ia.md, artefatos-exemplo/, exercicio/) a desenvolver.
