"""Cobertura de conteúdo por sessão.

As asserções são no nível da sessão, não da página: com a teoria organizada por
tema, o que importa é que o assunto exista na sessão, e não em qual arquivo ele
caiu. Por isso usam `teaching_text`.
"""

from pathlib import Path
import re
import unittest

from scripts.validate_content import (
    DOCS,
    SESSOES,
    SESSOES_SEM_CONFINAMENTO_DE_CASO,
    teaching_text,
)

S1 = DOCS / "sessao-01-o-que-mudou"
S2 = DOCS / "sessao-02-ambiente-agentico"
S4 = DOCS / "sessao-04-regras-formais-com-ia"
S5 = DOCS / "sessao-05-decomposicao"
S6 = DOCS / "sessao-06-spec-kit-aprofundado"
S8 = DOCS / "sessao-08-skills-e-agentes"
BIBLIOGRAFIA = DOCS / "referencia" / "bibliografia.md"


class SessaoUmTest(unittest.TestCase):
    def setUp(self):
        self.teoria = teaching_text(S1)

    def test_vocabulario_da_sessao_esta_coberto(self):
        for termo in (
            "vibe coding",
            "assistência de codificação",
            "SDD",
            "Software 3.0",
            "engenharia agêntica",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, self.teoria)

    def test_evidencia_empirica_cita_os_dois_estudos_opostos(self):
        self.assertIn("Peng", self.teoria)
        self.assertIn("METR", self.teoria)

    def test_curva_de_capacidade_usa_o_benchmark_de_tarefa_real(self):
        self.assertIn("SWE-bench", self.teoria)

    def test_placar_de_modelos_declara_fonte_e_data(self):
        placar = (S1 / "avaliacao-de-modelos.md").read_text(encoding="utf-8")
        self.assertIn("DeepSWE", placar)
        self.assertRegex(placar, r"atualizado em \d{1,2}º? de \w+ de \d{4}")

    def test_criterio_de_escolha_do_modo_e_uma_tabela(self):
        modos = (S1 / "modos-de-trabalho.md").read_text(encoding="utf-8")
        self.assertRegex(modos, r"\|\s*Critério\s*\|")


class SessaoDoisTest(unittest.TestCase):
    def setUp(self):
        self.teoria = teaching_text(S2)

    def test_vocabulario_da_sessao_esta_coberto(self):
        for termo in ("context engineering", "AGENTS.md", "worktree", "autonomia"):
            with self.subTest(termo=termo):
                self.assertIn(termo, self.teoria)

    def test_problema_de_integracao_aparece_com_a_notacao_usada_em_aula(self):
        self.assertIn("M×N", self.teoria)
        self.assertIn("Model Context Protocol", self.teoria)

    def test_as_quatro_pecas_do_ambiente_estao_lado_a_lado(self):
        ambiente = (S2 / "ambiente-compartilhado.md").read_text(encoding="utf-8")
        self.assertIn("| Peça |", ambiente)

    def test_oficina_traz_comandos_para_windows_e_para_posix(self):
        oficina = (S2 / "oficina-de-ferramentas.md").read_text(encoding="utf-8")
        self.assertIn('=== "macOS/Linux"', oficina)
        self.assertIn('=== "Windows', oficina)


class SessaoQuatroTest(unittest.TestCase):
    def setUp(self):
        self.teoria = teaching_text(S4)

    def test_vocabulario_da_sessao_esta_coberto(self):
        for termo in (
            "conceitos",
            "fatos",
            "regra estrutural",
            "regra operativa",
            "IRPF",
            "hipotético",
            "TDD",
            "SQL",
            "precedência",
            "evidência",
            "confiança",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, self.teoria)
        self.assertNotIn("TDDD", self.teoria)

    def test_nova_arquitetura_de_paginas_existe(self):
        for nome in (
            "regras-formais-conceitos.md",
            "regras-formais-exemplo-de-aplicacao-de-ia.md",
            "regras-formais-exercicio-geral.md",
            "regras-formais-exercicio-especialista.md",
            "arqueologia-de-regras-conceitos.md",
            "arqueologia-de-regras-exemplo-de-aplicacao-de-ia.md",
            "arqueologia-de-regras-exercicio.md",
        ):
            with self.subTest(pagina=nome):
                self.assertTrue((S4 / nome).is_file())

    def test_paginas_antigas_nao_existem(self):
        for nome in ("regras-formais-exemplo-irpf.md", "arqueologia-de-regras-sql.md"):
            with self.subTest(pagina=nome):
                self.assertFalse((S4 / nome).exists())

    def test_exemplo_irpf_declara_limites_didaticos(self):
        exemplo = (S4 / "regras-formais-exemplo-de-aplicacao-de-ia.md").read_text(encoding="utf-8")
        self.assertIn("valores hipotéticos", exemplo)
        self.assertIn("não é orientação tributária", exemplo)

    def test_exercicios_nao_inventam_resposta_para_lacuna(self):
        for nome in (
            "regras-formais-exercicio-geral.md",
            "regras-formais-exercicio-especialista.md",
        ):
            with self.subTest(pagina=nome):
                texto = (S4 / nome).read_text(encoding="utf-8")
                self.assertIn("não invente", texto)

    def test_arqueologia_exige_teste_de_precedencia(self):
        arqueologia = (S4 / "arqueologia-de-regras-exercicio.md").read_text(encoding="utf-8")
        self.assertIn("teste de precedência", arqueologia)
        self.assertIn("dados ausentes", arqueologia)
        self.assertIn("intervalo exato de linhas", arqueologia)

    def test_arqueologia_separa_evidencia_e_validacao_de_dominio(self):
        arqueologia = (S4 / "arqueologia-de-regras-conceitos.md").read_text(encoding="utf-8")
        self.assertIn("### 2. Captura de evidência", arqueologia)
        self.assertIn("### 4. Validação de domínio", arqueologia)

    def test_exercicios_citam_a_fonte_legal_com_data_de_acesso(self):
        planalto = "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm"
        for nome in (
            "regras-formais-exercicio-geral.md",
            "regras-formais-exercicio-especialista.md",
        ):
            with self.subTest(pagina=nome):
                texto = (S4 / nome).read_text(encoding="utf-8")
                self.assertIn(planalto, texto)
                self.assertIn("29 de setembro de 2026", texto)
                self.assertIn("117", texto)
                self.assertNotIn("reforma-tributaria-do-consumo/marcos", texto)

    def test_exercicios_marcam_lacuna_e_caso_indeterminado(self):
        geral = (S4 / "regras-formais-exercicio-geral.md").read_text(encoding="utf-8")
        especialista = (S4 / "regras-formais-exercicio-especialista.md").read_text(encoding="utf-8")
        self.assertIn("LACUNA", geral)
        self.assertIn("menor fragmento", geral)
        self.assertIn("INDETERMINADO", especialista)
        self.assertIn("| Precedência |", especialista)
        self.assertIn("node --test", especialista)

    def test_devolucao_especifica_mantem_o_sentido_do_art_124(self):
        """Art. 124, II: "específica" é a diferença acima dos percentuais do art. 118."""
        for nome in (
            "regras-formais-conceitos.md",
            "regras-formais-exercicio-especialista.md",
            "assets/calculo-beneficio.sql",
        ):
            with self.subTest(arquivo=nome):
                texto = (S4 / nome).read_text(encoding="utf-8")
                self.assertNotIn("percentual específico", texto)
                self.assertNotIn("percentuais específicos", texto)
                self.assertNotIn("DEVOLUCAO_ESPECIFICA", texto)

    def test_exemplo_irpf_nao_classifica_calculo_como_regra_operativa(self):
        exemplo = (S4 / "regras-formais-exemplo-de-aplicacao-de-ia.md").read_text(encoding="utf-8")
        self.assertNotIn("A apuração deve excluir", exemplo)
        self.assertNotIn("RN-03", exemplo)
        self.assertIn("O contribuinte", exemplo)

    def test_prompt_geral_carrega_as_convencoes_sbvr(self):
        geral = (S4 / "regras-formais-exercicio-geral.md").read_text(encoding="utf-8")
        for termo in (
            "Vocabulário antes das regras",
            "alética",
            "deôntica",
            "EX-nn",
            "REGULAMENTO",
            "INFERÊNCIA",
            "Se não conseguir abri-lo",
            "Unique, First ou Priority",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, geral)

    def test_texto_base_traz_a_frase_do_agente_financeiro(self):
        for nome in ("regras-formais-exercicio-geral.md", "regras-formais-exercicio-especialista.md"):
            with self.subTest(pagina=nome):
                texto = (S4 / nome).read_text(encoding="utf-8")
                self.assertIn("[8]", texto)
                self.assertIn("agente financeiro", texto)
                self.assertIn("art. 116, §§3º e 4º", texto)

    def test_especialista_nao_depende_do_exercicio_geral(self):
        especialista = (S4 / "regras-formais-exercicio-especialista.md").read_text(encoding="utf-8")
        self.assertNotIn("produzido no exercício geral", especialista)
        self.assertNotIn("recebe o mapa revisado no exercício geral", especialista)
        self.assertIn("Vocabulário antes das regras", especialista)

    def test_conceitos_de_arqueologia_ficam_sem_caso_aplicado(self):
        conceitos = (S4 / "arqueologia-de-regras-conceitos.md").read_text(encoding="utf-8")
        for termo in ("calculo-beneficio", "cashback", "759", "biblioteca", "IRPF"):
            with self.subTest(termo=termo):
                self.assertNotIn(termo, conceitos)
        for termo in ("teste de caracterização", "engenharia reversa", "comportamento implementado"):
            with self.subTest(termo=termo):
                self.assertIn(termo, conceitos)

    def test_exemplo_de_arqueologia_usa_artefato_proprio(self):
        exemplo = (S4 / "arqueologia-de-regras-exemplo-de-aplicacao-de-ia.md").read_text(encoding="utf-8")
        self.assertIn("```csharp", exemplo)
        self.assertIn("[Fact]", exemplo)
        self.assertIn("fictíci", exemplo)
        self.assertNotIn("calculo-beneficio", exemplo)


class SessaoCincoTest(unittest.TestCase):
    """Decisões de 06 e 07/10/2026 para a Sessão 5."""

    def setUp(self):
        self.teoria = teaching_text(S5)

    def texto(self, nome):
        return (S5 / nome).read_text(encoding="utf-8")

    def test_vocabulario_da_sessao_esta_coberto(self):
        for termo in (
            "constitution",
            "spec",
            "plan",
            "tasks",
            "implement",
            "tarefa atômica",
            "tarefa composta",
            "controle humano",
            "Constitution Check",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, self.teoria)

    def test_paginas_dos_dois_temas_existem(self):
        for nome in (
            "preparacao.md",
            "especificacao-com-spec-kit-conceitos.md",
            "especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md",
            "especificacao-com-spec-kit-exercicio.md",
            "do-plano-ao-codigo-conceitos.md",
            "do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md",
            "do-plano-ao-codigo-exercicio.md",
        ):
            with self.subTest(pagina=nome):
                self.assertTrue((S5 / nome).is_file())

    def test_trilha_unica_e_trabalho_individual(self):
        self.assertFalse(list(S5.glob("*-geral.md")))
        self.assertFalse(list(S5.glob("*-especialista.md")))
        for caminho in sorted(S5.glob("*.md")):
            with self.subTest(pagina=caminho.name):
                self.assertNotIn("dupla", caminho.read_text(encoding="utf-8").lower())

    def test_sem_rubrica_de_bastidor_para_o_instrutor(self):
        """O texto é do autor da aula, não instrução dirigida a quem conduz."""
        for caminho in sorted(S5.glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            for trecho in ("O instrutor", "à turma", "Mostre ", "Pergunte "):
                with self.subTest(pagina=caminho.name, trecho=trecho):
                    self.assertNotIn(trecho, texto)

    def test_exemplos_e_exercicios_abrem_pelo_primeiro_comando(self):
        """O objetivo de cada roteiro fica em contexto-da-pratica.md, não no topo."""
        self.assertTrue((S5 / "contexto-da-pratica.md").is_file())
        for nome in (
            "especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md",
            "especificacao-com-spec-kit-exercicio.md",
            "do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md",
            "do-plano-ao-codigo-exercicio.md",
        ):
            with self.subTest(pagina=nome):
                linhas = [l for l in self.texto(nome).splitlines() if l.strip()]
                self.assertTrue(linhas[1].startswith("## Passo 1:"))
                self.assertTrue(linhas[2].startswith("Digite "))

    def test_roteiro_abre_com_kahoot_de_quinze_minutos(self):
        self.assertRegex(self.texto("index.md"), r"\| 10:00–10:15 \| 15 \| Kahoot \|")

    def test_versao_do_spec_kit_fixada(self):
        self.assertIn("specify-cli==1.1.1", self.texto("preparacao.md"))
        self.assertIn("1.1.1", self.texto("index.md"))

    def test_pratica_parte_do_pedido_do_po_numa_pasta_vazia(self):
        """Decisão de 07/10/2026: sem código de partida, só a intenção do PO."""
        for nome in (
            "especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md",
            "especificacao-com-spec-kit-exercicio.md",
        ):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertIn("/speckit-specify Sou PO da Vetor", texto)
                self.assertIn("mkdir ", texto)

    def test_projeto_de_exemplo_do_repositorio_nao_e_citado(self):
        for caminho in sorted(S5.glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            for trecho in ("exemplo/vetor", "degit", "calcularDesconto"):
                with self.subTest(pagina=caminho.name, trecho=trecho):
                    self.assertNotIn(trecho, texto)

    def test_demonstracao_usa_caso_diferente_do_exercicio(self):
        for nome in (
            "especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md",
            "do-plano-ao-codigo-exemplo-de-aplicacao-de-ia.md",
        ):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertIn("pedido mínimo", texto)
                self.assertNotIn("RN-12", texto)

    def test_conceitos_ficam_sem_caso_aplicado(self):
        for nome in ("especificacao-com-spec-kit-conceitos.md", "do-plano-ao-codigo-conceitos.md"):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertNotIn("frete", texto)
                self.assertNotIn("pedido mínimo", texto)

    def test_exercicios_limitam_a_leitura_dos_artefatos(self):
        self.assertIn("Não leia o arquivo inteiro", self.texto("especificacao-com-spec-kit-exercicio.md"))
        self.assertIn("Não leia o arquivo", self.texto("do-plano-ao-codigo-exercicio.md"))

    def test_exercicios_cobrem_os_tres_agentes(self):
        for nome in ("especificacao-com-spec-kit-exercicio.md", "do-plano-ao-codigo-exercicio.md"):
            with self.subTest(pagina=nome):
                self.assertIn("$speckit-", self.texto(nome))

    def test_fundamentacao_primaria_do_tamanho_de_tarefa(self):
        for autor in ("Kwa et al.", "Prasad et al.", "Parnas"):
            with self.subTest(autor=autor):
                self.assertIn(autor, self.teoria)


class SessaoSeisTest(unittest.TestCase):
    """Decisões de 13/10/2026 para a Sessão 6."""

    ROTEIROS = (
        "qualidade-da-spec-exemplo-de-aplicacao-de-ia.md",
        "qualidade-da-spec-exercicio.md",
        "teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md",
        "teste-antes-do-codigo-exercicio.md",
    )
    CONCEITOS = ("qualidade-da-spec-conceitos.md", "teste-antes-do-codigo-conceitos.md")
    PEDIDO = "/speckit-specify Sou PO do sistema de pagamentos de projetos de pesquisa da universidade ACME"

    def setUp(self):
        self.teoria = teaching_text(S6)

    def texto(self, nome):
        return (S6 / nome).read_text(encoding="utf-8")

    def test_vocabulario_da_sessao_esta_coberto(self):
        for termo in (
            "clarify",
            "checklist",
            "analyze",
            "## Clarifications",
            "CHK",
            "somente leitura",
            "teste vermelho",
            "constitution",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, self.teoria)

    def test_paginas_existem(self):
        for nome in (
            "contexto-da-pratica.md",
            *self.CONCEITOS,
            *self.ROTEIROS,
            "tarefa-entre-sessoes.md",
            "sintese-e-referencias.md",
        ):
            with self.subTest(pagina=nome):
                self.assertTrue((S6 / nome).is_file())

    def test_pasta_antiga_nao_existe(self):
        self.assertFalse((DOCS / "sessao-06-tdd-assistido").exists())

    def test_roteiros_abrem_pelo_primeiro_comando(self):
        for nome in self.ROTEIROS:
            with self.subTest(pagina=nome):
                linhas = [l for l in self.texto(nome).splitlines() if l.strip()]
                self.assertTrue(linhas[1].startswith("## Passo 1:"))
                self.assertTrue(linhas[2].startswith("Digite "))

    def test_roteiro_abre_com_kahoot_de_quinze_minutos(self):
        self.assertRegex(self.texto("index.md"), r"\| 10:00–10:15 \| 15 \| Kahoot \|")

    def test_versao_do_spec_kit_e_preparacao_da_s5(self):
        self.assertIn("1.1.1", self.texto("index.md"))
        self.assertIn("../sessao-05-decomposicao/preparacao.md", self.texto("contexto-da-pratica.md"))

    def test_pedidos_partem_de_pasta_vazia(self):
        for nome in (
            "qualidade-da-spec-exemplo-de-aplicacao-de-ia.md",
            "qualidade-da-spec-exercicio.md",
            "tarefa-entre-sessoes.md",
        ):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertIn(self.PEDIDO, texto)
                self.assertIn("mkdir ", texto)

    def test_cenario_declarado_como_ficticio_e_anonimizado(self):
        self.assertIn("não reproduzem regra vigente", self.texto("contexto-da-pratica.md"))

    def test_demonstracao_usa_caso_diferente_do_exercicio(self):
        for nome in (
            "qualidade-da-spec-exemplo-de-aplicacao-de-ia.md",
            "teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md",
        ):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertIn("dupla aprovação", texto)
                self.assertNotIn("rubrica", texto)
        for nome in ("qualidade-da-spec-exercicio.md", "teste-antes-do-codigo-exercicio.md"):
            with self.subTest(pagina=nome):
                self.assertIn("rubrica", self.texto(nome))

    def test_conceitos_ficam_sem_caso_aplicado(self):
        for nome in self.CONCEITOS:
            for trecho in ("FUNDEP", "ACME", "rubrica", "dupla aprovação", "ordem de compra"):
                with self.subTest(pagina=nome, trecho=trecho):
                    self.assertNotIn(trecho, self.texto(nome))

    def test_exercicios_limitam_leitura_e_cobrem_o_codex(self):
        for nome in ("qualidade-da-spec-exercicio.md", "teste-antes-do-codigo-exercicio.md"):
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertIn("Não leia o arquivo", texto)
                self.assertIn("$speckit-", texto)

    def test_exercicio_do_tema_2_troca_a_comparacao_de_fronteira(self):
        texto = self.texto("teste-antes-do-codigo-exercicio.md")
        self.assertIn("`<=`", texto)
        self.assertIn("npm test", texto)

    def test_tarefa_para_no_analyze_e_pede_evidencia(self):
        texto = self.texto("tarefa-entre-sessoes.md")
        self.assertIn("/speckit-analyze", texto)
        self.assertNotIn("/speckit-implement", texto)
        self.assertIn("## Evidência a entregar", texto)

    def test_trabalho_individual_e_sem_bastidor(self):
        for caminho in sorted(S6.glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            for trecho in ("em dupla", "em duplas", "O instrutor", "à turma", "Mostre ", "Pergunte ", "exemplo/vetor"):
                with self.subTest(pagina=caminho.name, trecho=trecho):
                    self.assertNotIn(trecho, texto)

    def test_plataforma_de_teste_e_node_test(self):
        # Os roteiros rodam em node:test. A pilha C# aparece só na seção própria
        # de teste-antes-do-codigo-conceitos.md, a pedido do Marco em 13/10/2026,
        # para a sessão não ficar com um único exemplo baseado em npm.
        for caminho in sorted(S6.glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            proibidos = ("Jest",) if caminho.name == "teste-antes-do-codigo-conceitos.md" else ("xUnit", "Jest")
            for trecho in proibidos:
                with self.subTest(pagina=caminho.name, trecho=trecho):
                    self.assertNotIn(trecho, texto)

    def test_fundamentacao_cita_beck(self):
        self.assertIn("Beck", self.teoria)


class RevisaoFinalSessaoSeisTest(unittest.TestCase):
    """Achados da revisão final de 13/10/2026, conferidos contra o ensaio."""

    def texto(self, nome):
        return (S6 / nome).read_text(encoding="utf-8")

    def test_vermelho_por_modulo_ausente_tem_orientacao(self):
        for nome in ("teste-antes-do-codigo-exercicio.md", "teste-antes-do-codigo-conceitos.md"):
            with self.subTest(pagina=nome):
                self.assertIn("ERR_MODULE_NOT_FOUND", self.texto(nome))
        self.assertNotIn("só os testes da primeira história estavam vermelhos", self.texto("teste-antes-do-codigo-exercicio.md"))

    def test_severidade_do_analyze_e_proposta_a_conferir(self):
        self.assertNotIn("como CRITICAL", (S6 / "assets" / "teste-vermelho-conferido.svg").read_text(encoding="utf-8"))
        self.assertIn("classificou como HIGH", self.texto("teste-antes-do-codigo-conceitos.md"))

    def test_limite_do_clarify_nao_e_generalizado(self):
        self.assertIn("pode tratar como resolvida", self.texto("qualidade-da-spec-conceitos.md"))
        self.assertNotIn("ninguém havia apontado", self.texto("qualidade-da-spec-exemplo-de-aplicacao-de-ia.md"))

    def test_pergunta_do_specify_no_exercicio(self):
        texto = self.texto("qualidade-da-spec-exercicio.md")
        self.assertIn("não responda", texto)
        self.assertIn("respondida no specify", texto)

    def test_perguntas_do_checklist_tem_orientacao(self):
        for nome in ("qualidade-da-spec-exercicio.md", "qualidade-da-spec-exemplo-de-aplicacao-de-ia.md"):
            with self.subTest(pagina=nome):
                self.assertIn("perguntas para delimitar", self.texto(nome))

    def test_trava_do_implement_pede_leitura_dos_itens(self):
        self.assertIn("CHK004", self.texto("teste-antes-do-codigo-exemplo-de-aplicacao-de-ia.md"))
        self.assertIn("`yes`", self.texto("teste-antes-do-codigo-exercicio.md"))

    def test_estudo_de_mathews_nao_e_descrito_como_agente(self):
        self.assertNotIn("Com agentes de codificação, a ordem tem efeito medido", self.texto("teste-antes-do-codigo-conceitos.md"))

    def test_retomada_do_tema_1_lista_os_comandos_que_faltam(self):
        texto = self.texto("teste-antes-do-codigo-exercicio.md")
        self.assertIn("reserva de saldo pendente", texto)
        self.assertIn("/speckit-checklist", texto)


class CorrecoesDaSessaoCincoTest(unittest.TestCase):
    """Correções de 13/10/2026 vindas do ensaio da S6 com o Spec Kit 1.1.1."""

    def test_sintese_da_s5_nao_promete_xunit_nem_jest(self):
        texto = (S5 / "sintese-e-referencias.md").read_text(encoding="utf-8")
        self.assertNotIn("xUnit", texto)
        self.assertIn("node:test", texto)

    def test_converge_registrado_como_sexto_comando(self):
        for caminho in (S5 / "index.md", S5 / "especificacao-com-spec-kit-conceitos.md", BIBLIOGRAFIA):
            with self.subTest(arquivo=caminho.name):
                self.assertIn("converge", caminho.read_text(encoding="utf-8"))


class CasoAplicadoTest(unittest.TestCase):
    """Quando a Vetor aparece, ela fica nas páginas aplicadas, nunca na teoria.

    O caso Vetor é opcional desde 29/09/2026: cada sessão o usa quando ele é o
    melhor exemplo disponível, e nenhum teste exige a presença dele.

    Exceção documentada em 24/09/2026: sessões em SESSOES_SEM_CONFINAMENTO_DE_CASO
    abandonaram o par papel-fixo/página-temática (ver SESSOES_SEM_CONFINAMENTO_DE_CASO
    em scripts/validate_content.py) e organizam o conteúdo por tema, sem uma única
    página de exemplo. Nelas o caso aplicado corre pela sessão inteira, por desenho.
    """

    def test_a_vetor_nao_aparece_nas_paginas_tematicas(self):
        for slug, (_, completa, _) in SESSOES.items():
            if not completa or slug in SESSOES_SEM_CONFINAMENTO_DE_CASO:
                continue
            with self.subTest(slug=slug):
                self.assertNotIn("Vetor", teaching_text(DOCS / slug))


class BibliografiaTest(unittest.TestCase):
    def setUp(self):
        self.texto = BIBLIOGRAFIA.read_text(encoding="utf-8")

    def test_toda_entrada_declara_a_que_sessao_serve(self):
        entradas = re.findall(r"(?m)^\*\*\S.+?\*\*", self.texto)
        destinos = re.findall(r"(?m)^→ Sess(?:ão|ões) ", self.texto)
        self.assertTrue(entradas)
        self.assertEqual(len(entradas), len(destinos))

    def test_sessoes_citadas_existem(self):
        for bloco in re.findall(r"(?m)^→ Sess(?:ão|ões) (.+?)\.", self.texto):
            for numero in re.findall(r"\d+", bloco):
                with self.subTest(numero=numero):
                    self.assertIn(int(numero), range(1, len(SESSOES) + 1))


class PortalPublicoSessaoSeisTest(unittest.TestCase):
    """O portal é público: a Sessão 6 usa um caso anonimizado, sem citar o cliente."""

    def test_nenhuma_pagina_nem_ativo_cita_o_cliente(self):
        # docs/superpowers/ guarda specs e planos locais, fora do site.
        arquivos = [c for c in sorted(DOCS.rglob("*")) if c.suffix in (".md", ".svg") and "superpowers" not in c.parts]
        arquivos.append(DOCS.parent / "mkdocs.yml")
        for caminho in arquivos:
            with self.subTest(arquivo=str(caminho.relative_to(DOCS.parent))):
                self.assertNotIn("fundep", caminho.read_text(encoding="utf-8").lower())

    def test_pilha_csharp_do_teste_vermelho(self):
        texto = (S6 / "teste-antes-do-codigo-conceitos.md").read_text(encoding="utf-8")
        for trecho in ("dotnet test", "CS0246", "NotImplementedException", "assets/teste-vermelho-csharp.png"):
            with self.subTest(trecho=trecho):
                self.assertIn(trecho, texto)
        self.assertTrue((S6 / "assets" / "teste-vermelho-csharp.png").exists())
        self.assertNotIn("npm", (S6 / "assets" / "teste-vermelho-csharp.svg").read_text(encoding="utf-8"))


class SessaoOitoReestruturadaTest(unittest.TestCase):
    """Reestruturação de 23/10/2026: onze páginas, ficha de requisitos e figuras por tema."""

    SLUG = "sessao-08-skills-e-agentes"
    PAGINAS = (
        "index.md",
        "skills.md",
        "agentes-e-subagentes.md",
        "geracao-de-artefatos.md",
        "escolha-de-modelos.md",
        "custo-de-tokens.md",
        "performance.md",
        "oficina-de-ferramentas.md",
        "seguranca-e-credenciais.md",
        "exercicios.md",
        "sintese-e-referencias.md",
    )
    TEORIA = (
        "skills.md",
        "agentes-e-subagentes.md",
        "geracao-de-artefatos.md",
        "escolha-de-modelos.md",
        "custo-de-tokens.md",
        "performance.md",
        "seguranca-e-credenciais.md",
    )
    REMOVIDAS = (
        "escolher-o-mecanismo.md",
        "front-matter-de-skills.md",
        "front-matter-de-subagentes.md",
        "depuracao-de-skills-e-agentes.md",
        "claude-code-e-codex.md",
    )
    FIGURAS = (
        "ficha-de-requisitos",
        "mapa-da-sessao",
        "skill-anotada-nucleo-portatil",
        "carga-em-tres-niveis-e-listagem",
        "contexto-skill-subagente-fork",
        "precedencia-de-escopo",
        "arvore-de-decisao-do-mecanismo",
        "laco-de-conferencia-em-duas-camadas",
        "estrategias-de-escolha-de-modelo",
        "de-onde-o-custo-vem",
        "cache-em-unidades-relativas",
        "tres-medidas-de-desempenho",
        "percurso-dos-experimentos",
        "pontos-de-entrada-do-risco",
        "identidade-propria-e-credencial",
        "ciclo-de-vida-do-token",
        "restricao-em-camadas",
        "fluxo-do-exercicio-ancora",
    )
    TEMPOS = {
        "skills.md": 10,
        "agentes-e-subagentes.md": 12,
        "geracao-de-artefatos.md": 5,
        "escolha-de-modelos.md": 4,
        "custo-de-tokens.md": 5,
        "performance.md": 3,
        "oficina-de-ferramentas.md": 17,
        "seguranca-e-credenciais.md": 10,
        "sintese-e-referencias.md": 5,
    }

    def texto(self, nome):
        caminho = S8 / nome
        return caminho.read_text(encoding="utf-8") if caminho.exists() else ""

    def todo_o_texto(self):
        return "\n\n".join(c.read_text(encoding="utf-8") for c in sorted(S8.glob("*.md")))

    def mkdocs(self):
        return (DOCS.parent / "mkdocs.yml").read_text(encoding="utf-8")

    def test_paginas_de_aprofundamento_removidas(self):
        todo = self.todo_o_texto()
        for nome in self.REMOVIDAS:
            with self.subTest(pagina=nome):
                self.assertFalse((S8 / nome).exists())
                self.assertNotIn(nome, self.mkdocs())
                self.assertNotIn(nome, todo)

    def test_onze_paginas_no_nav(self):
        no_nav = re.findall(rf"{self.SLUG}/([a-z0-9.-]+\.md)", self.mkdocs())
        self.assertEqual(list(self.PAGINAS), no_nav)

    def test_paginas_de_teoria_fecham_com_a_linha_da_ficha(self):
        marcador = '!!! abstract "Linha da ficha"'
        for nome in self.TEORIA:
            with self.subTest(pagina=nome):
                texto = self.texto(nome)
                self.assertEqual(1, texto.count(marcador))
                inicio = texto.index(marcador)
                transicao = texto.index("**Próxima página:**")
                self.assertLess(inicio, transicao)
                self.assertIsNone(re.search(r"(?m)^#{1,6} ", texto[inicio:transicao]))

    def test_visao_geral_traz_a_ficha_e_as_duas_figuras(self):
        texto = self.texto("index.md")
        self.assertIn("ficha de requisitos", texto.lower())
        self.assertIn("assets/ficha-de-requisitos.png", texto)
        self.assertIn("assets/mapa-da-sessao.png", texto)

    def test_roteiro_traz_os_tempos_acordados(self):
        texto = self.texto("index.md")
        tabela = texto.split("## Roteiro da sessão", 1)[1].split("\n## ", 1)[0]
        por_pagina = {}
        visao_geral = None
        for linha in re.findall(r"(?m)^\|(?!-)(.+)\|[ \t]*$", tabela):
            minutos = re.search(r"(\d+)\s*min", linha)
            if not minutos:
                continue
            paginas = re.findall(r"\]\(([a-z0-9.-]+\.md)\)", linha)
            if not paginas and "Visão geral" in linha:
                visao_geral = int(minutos.group(1))
            for nome in paginas:
                por_pagina.setdefault(nome, []).append(int(minutos.group(1)))
        self.assertEqual(4, visao_geral)
        for nome, esperado in self.TEMPOS.items():
            with self.subTest(pagina=nome):
                self.assertEqual(esperado, sum(por_pagina.get(nome, [])))
        self.assertEqual(40, sum(por_pagina.get("exercicios.md", [])))

    def test_exercicios_de_1_a_12_com_ancora_e_rubrica(self):
        texto = self.texto("exercicios.md")
        for numero in range(1, 13):
            with self.subTest(exercicio=numero):
                self.assertRegex(texto, rf"(?m)^### {numero}\. ")
        self.assertNotRegex(texto, r"(?m)^### 13\. ")
        self.assertNotIn("Extensão: front-matter na prática", texto)
        ancora = texto.split("### 12. ", 1)[-1]
        self.assertIn("**Critérios de avaliação**", ancora)

    def test_exercicios_nao_citam_numeracao_antiga(self):
        todo = self.todo_o_texto()
        for antiga in ("exercício 13", "exercícios 11 a 14", "exercícios 1 a 9"):
            with self.subTest(trecho=antiga):
                self.assertNotIn(antiga, todo)

    def test_figuras_declaradas_existem_e_sao_referenciadas(self):
        declaradas = set(SESSOES[self.SLUG][2])
        self.assertEqual({f"assets/{nome}.png" for nome in self.FIGURAS}, declaradas)
        todo = self.todo_o_texto()
        for nome in self.FIGURAS:
            with self.subTest(figura=nome):
                self.assertTrue((S8 / "assets" / f"{nome}.png").exists())
                self.assertTrue((S8 / "assets" / f"{nome}.svg").exists())
                self.assertRegex(todo, rf"!\[[^\]]+\]\(assets/{nome}\.png\)")

    def test_fatos_preservados_na_mesclagem(self):
        todo = self.todo_o_texto()
        for termo in (
            "disable-model-invocation",
            "allowed-tools",
            "disallowed-tools",
            "context: fork",
            "does not recognize or apply",
            "claude plugin validate",
            "/context",
            "Git Bash",
            "permissionMode",
            "CLAUDE_CODE_SUBAGENT_MODEL",
            "skillListingBudgetFraction",
            "sandbox_mode",
            "features.*",
            "ignore_default_excludes",
            "developer_instructions",
            ".agents/skills",
            "--debug-file",
            "claude agents",
        ):
            with self.subTest(termo=termo):
                self.assertIn(termo, todo)

    def test_protecoes_da_revisao_final_preservadas(self):
        todo = self.todo_o_texto()
        for proibida in (
            "não traz um campo que limite as ferramentas",
            "acionou com qualquer",
            "O mesmo bloco funciona nas três plataformas",
            "pergunta 1 ou a pergunta 2",
        ):
            with self.subTest(trecho=proibida):
                self.assertNotIn(proibida, todo)
        oficina = self.texto("oficina-de-ferramentas.md")
        d = oficina.split("## Experimento D", 1)[1].split("## Experimento E", 1)[0]
        e = oficina.split("## Experimento E", 1)[1].split("## Experimento F", 1)[0]
        self.assertIn("pasta nova", d)
        self.assertIn("pasta nova", e)


    def test_codex_sem_afirmacao_de_escrita_sem_status(self):
        seg = self.texto("seguranca-e-credenciais.md")
        self.assertNotIn("permite que o agente edite arquivos apesar", seg)
        self.assertIn("não restringe nada sozinho", seg)

    def test_regra_do_front_matter_na_primeira_linha_aparece_uma_vez(self):
        skills = self.texto("skills.md")
        self.assertEqual(
            skills.count("só lê o front-matter quando o primeiro `---`")
            + skills.count("lê o front-matter somente quando o primeiro `---`"),
            1,
        )


if __name__ == "__main__":
    unittest.main()
