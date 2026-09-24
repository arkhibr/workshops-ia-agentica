"""Cobertura de conteúdo por sessão.

As asserções são no nível da sessão, não da página: com a teoria organizada por
tema, o que importa é que o assunto exista na sessão, e não em qual arquivo ele
caiu. Por isso usam `teaching_text`.
"""

from pathlib import Path
import re
import unittest

from scripts.validate_content import DOCS, SESSOES, SESSOES_SEM_CONFINAMENTO_DE_CASO, teaching_text

S1 = DOCS / "sessao-01-o-que-mudou"
S2 = DOCS / "sessao-02-ambiente-agentico"
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


class CasoAplicadoTest(unittest.TestCase):
    """A Vetor entra nas páginas aplicadas, nunca na teoria.

    Exceção documentada em 24/09/2026: sessões em SESSOES_SEM_CONFINAMENTO_DE_CASO
    abandonaram o par papel-fixo/página-temática (ver SESSOES_SEM_CONFINAMENTO_DE_CASO
    em scripts/validate_content.py) e organizam o conteúdo por tema, sem uma única
    página de exemplo. Nelas o caso Vetor corre pela sessão inteira, por desenho.
    """

    def test_a_vetor_nao_aparece_nas_paginas_tematicas(self):
        for slug, (_, completa, _) in SESSOES.items():
            if not completa or slug in SESSOES_SEM_CONFINAMENTO_DE_CASO:
                continue
            with self.subTest(slug=slug):
                self.assertNotIn("Vetor", teaching_text(DOCS / slug))

    def test_a_vetor_aparece_no_exemplo_arquitetural_de_cada_sessao_completa(self):
        for slug, (_, completa, _) in SESSOES.items():
            if not completa or slug in SESSOES_SEM_CONFINAMENTO_DE_CASO:
                continue
            with self.subTest(slug=slug):
                exemplo = (DOCS / slug / "exemplo-arquitetural.md").read_text(encoding="utf-8")
                self.assertIn("Vetor", exemplo)

    def test_a_vetor_aparece_em_algum_lugar_das_sessoes_sem_confinamento(self):
        for slug in SESSOES_SEM_CONFINAMENTO_DE_CASO:
            with self.subTest(slug=slug):
                self.assertIn("Vetor", teaching_text(DOCS / slug))


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
