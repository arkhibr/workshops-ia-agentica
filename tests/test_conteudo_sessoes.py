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

    def test_roteiro_abre_com_kahoot_de_quinze_minutos(self):
        self.assertRegex(self.texto("index.md"), r"\| 10:00–10:15 \| 15 \| Kahoot \|")

    def test_versao_do_spec_kit_fixada(self):
        self.assertIn("specify-cli==1.1.1", self.texto("preparacao.md"))
        self.assertIn("1.1.1", self.texto("index.md"))

    def test_valor_de_referencia_e_regra_de_derivacao(self):
        """Convenção da S4: RC classifica, RD deriva, RN rege conduta."""
        for nome in ("especificacao-com-spec-kit-exercicio.md", "do-plano-ao-codigo-exercicio.md"):
            with self.subTest(pagina=nome):
                self.assertNotIn("RC-11", self.texto(nome))
        self.assertIn("RD-11", self.texto("especificacao-com-spec-kit-exercicio.md"))
        self.assertIn("RD-01", self.texto("especificacao-com-spec-kit-exemplo-de-aplicacao-de-ia.md"))

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


if __name__ == "__main__":
    unittest.main()
