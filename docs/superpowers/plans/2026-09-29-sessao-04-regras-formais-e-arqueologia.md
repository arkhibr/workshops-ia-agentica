# Session 04 Formal Rules and Rule Archaeology Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild Session 04 around formal rule modeling with SBVR and decision tables, followed by rule archaeology from SQL, with exercises, public sources, TDD cases, and instructional infographics.

**Architecture:** Replace the current eight thematic pages with five focused teaching pages plus the session index and synthesis. Keep authoritative legal material distinct from didactic adaptations, make every exercise produce a typed rule inventory, and use project-local visual assets with verified alt text and captions.

**Tech Stack:** Material for MkDocs, Markdown, Python `unittest` content checks, project content validator, MkDocs strict build, built-in image generation.

**Spec:** `docs/superpowers/specs/2026-09-29-sessao-04-regras-formais-e-arqueologia-design.md`

## Global Constraints

- Preserve the fixed 10:00–12:00 schedule with 115 teaching minutes and a five-minute break at 11:00.
- Use SBVR as the normative acronym and TDD as the testing method.
- Every exercise explicitly separates concepts, facts, structural rules, operative rules, exceptions, conflicts, gaps, evidence, and confidence.
- Use only public primary sources for current Brazilian tax legislation; identify quotation, paraphrase, didactic adaptation, and hypothetical values.
- Do not present the IRPF example as tax advice or as a current production calculator.
- Keep the rule-archaeology workflow vendor-neutral and cite SQL evidence by line.
- Every image must be stored under the session `assets/` directory and have meaningful alt text and a caption.
- Run the repository anti-cliché review and all three quality-gate commands before completion.

## Review Focus

- A reader must not mistake hypothetical IRPF values for current law; test for the didactic disclaimer and hypothetical-value label.
- A legal source may change after publication; verify the official URL, access date, and the boundary between source text and synthesis.
- SQL condition order can change semantics; ensure the exercise asks for precedence evidence and a test for overlapping conditions.
- Missing or ambiguous legal facts must become gaps, not invented expected results; assert this instruction in both tax exercises.
- Navigation and next-page links must contain no references to deleted pages; run the link validator and strict build.

---

### Task 1: Lock the New Content Contract in Tests

**Files:**
- Modify: `tests/test_conteudo_sessoes.py`
- Test: `tests/test_conteudo_sessoes.py`

**Interfaces:**
- Consumes: `teaching_text("sessao-04-regras-formais-com-ia")` and the repository's existing Markdown helpers.
- Produces: regression assertions for the required vocabulary, page structure, legal disclaimer, SQL precedence, and removal of `TDDD`.

- [ ] **Step 1: Add focused Session 04 assertions**

Add tests that assert the combined Session 04 teaching text contains `conceitos`, `fatos`, `regra estrutural`, `regra operativa`, `IRPF`, `hipotético`, `TDD`, `SQL`, `precedência`, `evidência`, and `confiança`; assert it does not contain `TDDD`. Add exact page-existence assertions for the five new thematic filenames.

- [ ] **Step 2: Run the focused tests and verify the contract initially fails**

Run: `python -m unittest tests.test_conteudo_sessoes -v`

Expected: FAIL because the new filenames and complete content do not exist.

- [ ] **Step 3: Commit the failing contract**

```bash
git add tests/test_conteudo_sessoes.py
git commit -m "test: define contrato editorial da sessao 04"
```

### Task 2: Build the Formal-Rules Theory and IRPF Demonstration

**Files:**
- Create: `docs/sessao-04-regras-formais-com-ia/regras-formais-conceitos.md`
- Create: `docs/sessao-04-regras-formais-com-ia/regras-formais-exemplo-irpf.md`
- Modify: `docs/sessao-04-regras-formais-com-ia/index.md`

**Interfaces:**
- Consumes: definitions and page architecture from the approved spec.
- Produces: the typed rule model and identifiers referenced by both tax exercises.

- [ ] **Step 1: Write the unified theory page**

Define concepts, fact types, fact instances, structural classification and derivation rules, operative obligation/prohibition/permission rules, atomicity, evidence, confidence, and decision tables. Include a reusable output schema with columns `ID`, `Tipo`, `Sentença`, `Evidência`, `Confiança`, and `Questão em aberto`.

- [ ] **Step 2: Write the IRPF rule nest**

Create a clearly labeled fictional policy paragraph with intertwined taxable income, deductions, brackets, withholding, and a cap. Label all monetary values hypothetical and add a statement that the example is neither current legislation nor tax advice.

- [ ] **Step 3: Decompose the nest end to end**

Show the concept glossary, fact types, structural rules, operative rules, exceptions, precedence, decision table, and boundary examples. Ensure each stage preserves identifiers and points back to a precise phrase in the nest.

- [ ] **Step 4: Rewrite the session index**

State the two themes, learning objectives, output of each block, and the exact schedule: 20 + 25 + 20 minutes before the break; 20 + 25 + 5 minutes after it.

- [ ] **Step 5: Run focused tests**

Run: `python -m unittest tests.test_conteudo_sessoes -v`

Expected: page-existence tests progress; content assertions for unfinished exercises may still fail.

- [ ] **Step 6: Commit the theory and example**

```bash
git add docs/sessao-04-regras-formais-com-ia/index.md docs/sessao-04-regras-formais-com-ia/regras-formais-conceitos.md docs/sessao-04-regras-formais-com-ia/regras-formais-exemplo-irpf.md
git commit -m "docs: ensina regras formais com exemplo de irpf"
```

### Task 3: Create the Tax-Legislation Exercises from Official Sources

**Files:**
- Create: `docs/sessao-04-regras-formais-com-ia/regras-formais-exercicio-geral.md`
- Create: `docs/sessao-04-regras-formais-com-ia/regras-formais-exercicio-especialista.md`
- Modify: `docs/sessao-04-regras-formais-com-ia/sintese-e-referencias.md`
- Modify: `docs/referencia/bibliografia.md`

**Interfaces:**
- Consumes: the typed rule schema from Task 2 and verified official legislation.
- Produces: a general rule-mapping exercise and a specialist TDD test-design exercise sharing stable rule IDs.

- [ ] **Step 1: Verify a current primary source**

Use official government pages to select a bounded rule from Brazil's consumption-tax reform. Record the instrument, article numbers, publication status, canonical URL, and access date. Cross-check claims against at least one second official explanatory source when available.

- [ ] **Step 2: Write the general exercise source packet**

Provide a complex but bounded teaching text and mark every passage as quotation, paraphrase, or didactic synthesis. Include a direct source link and access date.

- [ ] **Step 3: Write the rule-map prompt**

Require separate outputs for concepts, facts, structural rules, operative rules, exceptions, conflicts, gaps, evidence, and confidence. Instruct the agent to quote no more than the minimum source fragment, never fill a gap, and return questions for legal review.

- [ ] **Step 4: Write the specialist TDD exercise**

Make participants derive tests before implementation. Require rule ID, scenario, input, expected result, partition or boundary, evidence, and justification; include nominal, boundary, exception, overlap, precedence, null/missing-data, and indeterminate cases.

- [ ] **Step 5: Add sources and synthesis**

Update the session synthesis and global bibliography with complete official and methodological references. Include the access date and distinguish legislation from explanatory material.

- [ ] **Step 6: Run focused tests**

Run: `python -m unittest tests.test_conteudo_sessoes -v`

Expected: all content-contract assertions pass except any dependency on the archaeology page.

- [ ] **Step 7: Commit the exercises**

```bash
git add docs/sessao-04-regras-formais-com-ia/regras-formais-exercicio-geral.md docs/sessao-04-regras-formais-com-ia/regras-formais-exercicio-especialista.md docs/sessao-04-regras-formais-com-ia/sintese-e-referencias.md docs/referencia/bibliografia.md
git commit -m "docs: cria exercicios tributarios com tdd"
```

### Task 4: Build the SQL Rule-Archaeology Module

**Files:**
- Create: `docs/sessao-04-regras-formais-com-ia/assets/calculo-beneficio.sql`
- Create: `docs/sessao-04-regras-formais-com-ia/arqueologia-de-regras-sql.md`

**Interfaces:**
- Consumes: the rule schema from Task 2.
- Produces: a line-addressable SQL artifact, a vendor-neutral archaeology prompt, an SBVR catalog format, and a traceable test-case format.

- [ ] **Step 1: Create the SQL artifact**

Write a realistic query containing nested `CASE`, repeated conditions, magic values, a `JOIN` that changes eligibility, `NULL` handling, order-dependent overlap, and an excluding `WHERE` clause. Keep the query self-contained and annotate only database mechanics, not hidden business intent.

- [ ] **Step 2: Write the archaeology workflow**

Teach inventory, evidence capture, hypothesis formation, domain validation, formalization, and test derivation. Explain why executable behavior is evidence of an implemented rule but not proof of intended policy.

- [ ] **Step 3: Write the single shared exercise**

Ask all participants to inspect the SQL through an agent that can cite line numbers. Require concepts, facts, both structural-rule types, all operative-rule types found, exceptions, conflicts, gaps, confidence, decision table, and tests. Include an explicit precedence-overlap test and a missing-data test.

- [ ] **Step 4: Run focused tests**

Run: `python -m unittest tests.test_conteudo_sessoes -v`

Expected: PASS.

- [ ] **Step 5: Commit the archaeology module**

```bash
git add docs/sessao-04-regras-formais-com-ia/assets/calculo-beneficio.sql docs/sessao-04-regras-formais-com-ia/arqueologia-de-regras-sql.md
git commit -m "docs: adiciona arqueologia de regras em sql"
```

### Task 5: Generate and Integrate the Instructional Visuals

**Files:**
- Create: `docs/sessao-04-regras-formais-com-ia/assets/mapa-de-regras.png`
- Create: `docs/sessao-04-regras-formais-com-ia/assets/ninho-irpf.png`
- Create: `docs/sessao-04-regras-formais-com-ia/assets/fluxo-regra-tributaria.png`
- Create: `docs/sessao-04-regras-formais-com-ia/assets/arqueologia-sql.png`
- Modify: all five thematic Session 04 Markdown pages
- Modify: `scripts/validate_content.py`

**Interfaces:**
- Consumes: final page terminology and workflow order from Tasks 2–4.
- Produces: four project-local visuals referenced by Markdown and declared to the validator.

- [ ] **Step 1: Generate one visual per learning relationship**

Use the built-in image generator with the shared direction: clean educational infographic, horizontal layout, green/teal palette, high contrast, minimal Portuguese labels, no logos, no watermark. Generate separate assets for the rule map, IRPF decomposition, tax-exercise workflow, and SQL archaeology workflow.

- [ ] **Step 2: Inspect every generated image**

Check label spelling, direction of arrows, legibility, unwanted extra text, and consistency with the corresponding page. Regenerate any asset that misstates a concept.

- [ ] **Step 3: Copy selected outputs into the session assets directory**

Preserve the four exact filenames listed above and do not leave any published reference pointing to the generator's private output directory.

- [ ] **Step 4: Integrate figures with alt text and captions**

Place each figure beside the explanation it supports. Use descriptive alt text that states the relationship and a caption that tells the reader how to scan the diagram.

- [ ] **Step 5: Declare expected assets**

Change the Session 04 image tuple in `scripts/validate_content.py` from empty to the four relative asset paths.

- [ ] **Step 6: Validate assets and links**

Run: `python scripts/validate_content.py --all`

Expected: PASS with no missing image, empty alt text, or broken link.

- [ ] **Step 7: Commit the visuals**

```bash
git add docs/sessao-04-regras-formais-com-ia scripts/validate_content.py
git commit -m "docs: ilustra fluxos da sessao 04"
```

### Task 6: Switch Navigation and Remove Superseded Material

**Files:**
- Modify: `mkdocs.yml`
- Delete: `docs/sessao-04-regras-formais-com-ia/vocabulario-e-sentencas-conceitos.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/vocabulario-e-sentencas-exemplo-de-aplicacao-de-ia.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/vocabulario-e-sentencas-exercicio-geral.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/vocabulario-e-sentencas-exercicio-especialista.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/tabelas-de-decisao-conceitos.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/tabelas-de-decisao-exemplo-de-aplicacao-de-ia.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/tabelas-de-decisao-exercicio-geral.md`
- Delete: `docs/sessao-04-regras-formais-com-ia/tabelas-de-decisao-exercicio-especialista.md`
- Delete after reference check: `docs/sessao-04-regras-formais-com-ia/assets/planilha-comissoes-vetor.xlsx`

**Interfaces:**
- Consumes: all new pages and cross-page transitions.
- Produces: the final public navigation with no orphaned or superseded pages.

- [ ] **Step 1: Update the MkDocs navigation**

List the pages in instructional order: overview, formal-rules concepts, IRPF example, general exercise, specialist exercise, SQL archaeology, synthesis.

- [ ] **Step 2: Verify old references are gone**

Run: `rg -n "vocabulario-e-sentencas|tabelas-de-decisao-(conceitos|exemplo|exercicio)|planilha-comissoes-vetor" docs mkdocs.yml tests scripts`

Expected: no output outside historical design/plan documents.

- [ ] **Step 3: Remove superseded pages and the unreferenced spreadsheet**

Delete only the nine files listed in this task after Step 2 proves the spreadsheet has no remaining consumer.

- [ ] **Step 4: Run link and navigation checks**

Run: `python scripts/validate_content.py --all`

Expected: PASS.

Run: `mkdocs build --strict`

Expected: exit 0 with no orphaned-page warning.

- [ ] **Step 5: Commit the navigation cutover**

```bash
git add mkdocs.yml docs/sessao-04-regras-formais-com-ia
git commit -m "refactor: reorganiza navegacao da sessao 04"
```

### Task 7: Editorial, Visual, and Full Quality Verification

**Files:**
- Modify as findings require: `docs/sessao-04-regras-formais-com-ia/*.md`
- Modify as findings require: `tests/test_conteudo_sessoes.py`

**Interfaces:**
- Consumes: the complete rebuilt session.
- Produces: reviewed and render-verified workshop material.

- [ ] **Step 1: Run the mechanical editorial scan**

Scan for forbidden markers, `TDDD`, multiple em dashes per paragraph, and occurrences of `não` near a colon or em dash. Rewrite any artificial contrast, generic transition, or unsupported certainty found.

- [ ] **Step 2: Run the complete test suite**

Run: `python -m unittest discover -s tests -v`

Expected: PASS.

- [ ] **Step 3: Run the complete content validator**

Run: `python scripts/validate_content.py --all`

Expected: PASS.

- [ ] **Step 4: Build the site strictly**

Run: `mkdocs build --strict`

Expected: exit 0.

- [ ] **Step 5: Inspect rendered pages**

Serve the site locally and inspect every Session 04 page at desktop and mobile widths. Confirm headings, tables, admonitions, prompt blocks, images, captions, and next-page links remain legible and correctly ordered.

- [ ] **Step 6: Commit review fixes**

```bash
git add docs/sessao-04-regras-formais-com-ia docs/referencia/bibliografia.md tests/test_conteudo_sessoes.py scripts/validate_content.py mkdocs.yml
git commit -m "fix: conclui revisao editorial da sessao 04"
```
