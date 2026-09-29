"""Testa o próprio validador: cada checagem precisa ser capaz de reprovar."""

from collections import Counter
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import scripts.validate_content as validador

from scripts.validate_content import (
    Counts,
    ROOT,
    bloom_sections,
    document_anchors,
    slugify,
    validate_exercises,
    validate_multiplatform,
    validate_references,
    validate_session,
)


class ReferenciasTest(unittest.TestCase):
    def setUp(self):
        self.temporario = tempfile.TemporaryDirectory(dir=ROOT)
        self.diretorio = Path(self.temporario.name)
        self.pagina = self.diretorio / "pagina.md"

    def tearDown(self):
        self.temporario.cleanup()

    def validar(self, texto):
        errors, counts = [], Counts()
        validate_references(self.pagina, texto, errors, counts)
        return errors, counts

    def test_link_e_imagem_validos_nao_geram_erro(self):
        (self.diretorio / "destino.md").write_text("# Destino\n", encoding="utf-8")
        (self.diretorio / "figura.png").write_bytes(b"png")

        errors, counts = self.validar("[texto](destino.md)\n![Legenda](figura.png)\n")

        self.assertEqual([], errors)
        self.assertEqual(1, counts.images)

    def test_link_relativo_inexistente_e_reprovado(self):
        errors, _ = self.validar("[texto](sumiu.md)\n")

        self.assertTrue(any("sumiu.md" in erro for erro in errors), errors)

    def test_imagem_inexistente_e_reprovada(self):
        errors, _ = self.validar("![Legenda](sumiu.png)\n")

        self.assertTrue(any("sumiu.png" in erro for erro in errors), errors)

    def test_texto_alternativo_vazio_e_reprovado(self):
        (self.diretorio / "figura.png").write_bytes(b"png")

        errors, _ = self.validar("![](figura.png)\n")

        self.assertTrue(any("alternativo vazio" in erro for erro in errors), errors)

    def test_imagem_html_sem_src_e_reprovada_sem_quebrar(self):
        errors, counts = self.validar('<img alt="Diagrama">')

        self.assertTrue(any("sem origem" in erro for erro in errors), errors)
        self.assertEqual(1, counts.images)

    def test_ancora_inexistente_no_destino_e_reprovada(self):
        (self.diretorio / "destino.md").write_text("# Destino\n\n## Uma seção\n", encoding="utf-8")

        errors, _ = self.validar("[texto](destino.md#outra-secao)\n")

        self.assertTrue(any("âncora inexistente" in erro for erro in errors), errors)

    def test_ancora_de_cabecalho_existente_e_aceita(self):
        (self.diretorio / "destino.md").write_text("# Destino\n\n## Uma seção\n", encoding="utf-8")

        errors, _ = self.validar("[texto](destino.md#uma-secao)\n")

        self.assertEqual([], errors)

    def test_ancora_html_explicita_e_aceita(self):
        (self.diretorio / "destino.md").write_text(
            '# Destino\n\n<a id="ancora-preservada"></a>\n', encoding="utf-8"
        )

        errors, _ = self.validar("[texto](destino.md#ancora-preservada)\n")

        self.assertEqual([], errors)

    def test_cabecalho_dentro_de_bloco_cercado_nao_vira_ancora(self):
        (self.diretorio / "destino.md").write_text(
            "# Destino\n\n```bash\n## Não é cabeçalho\n```\n", encoding="utf-8"
        )

        errors, _ = self.validar("[texto](destino.md#nao-e-cabecalho)\n")

        self.assertTrue(any("âncora inexistente" in erro for erro in errors), errors)

    def test_referencia_sem_definicao_e_reprovada(self):
        errors, _ = self.validar("[texto][doc]\n![Legenda][img]\n")

        self.assertTrue(any("link sem definição" in erro for erro in errors), errors)
        self.assertTrue(any("imagem sem definição" in erro for erro in errors), errors)

    def test_referencia_com_definicao_quebrada_e_reprovada(self):
        errors, _ = self.validar("[texto][doc]\n\n[doc]: sumiu.md\n")

        self.assertTrue(any("sumiu.md" in erro for erro in errors), errors)

    def test_url_externa_nao_e_checada_no_disco(self):
        errors, _ = self.validar("[texto](https://example.org/pagina.md)\n")

        self.assertEqual([], errors)


class BloomTest(unittest.TestCase):
    def setUp(self):
        self.pagina = ROOT / "docs" / "exercicios-ficticios.md"

    def validar(self, texto):
        errors, counts = [], Counts()
        validate_exercises(self.pagina, texto, errors, counts)
        return errors, counts

    def test_secao_termina_no_cabecalho_de_mesmo_nivel(self):
        secoes = bloom_sections("## Recordar\n\ncorpo A\n\n## Compreender\n\ncorpo B\n")

        self.assertIn("corpo A", secoes["Recordar"])
        self.assertNotIn("corpo B", secoes["Recordar"])

    def test_subsecao_continua_dentro_do_nivel(self):
        secoes = bloom_sections("## Recordar\n\n### 1. Item\n\ncorpo\n\n## Compreender\n")

        self.assertIn("corpo", secoes["Recordar"])

    def test_nivel_ausente_e_reprovado(self):
        errors, _ = self.validar("## Recordar\n\n<details><summary>x</summary>y</details>\n")

        self.assertTrue(any("Bloom ausente: Criar" in erro for erro in errors), errors)

    def test_recordar_sem_gabarito_e_reprovado(self):
        errors, _ = self.validar("## Recordar\n\nenunciado sem gabarito\n")

        self.assertTrue(any("Recordar requer bloco <details>" in erro for erro in errors), errors)

    def test_aplicar_sem_rubrica_e_reprovado(self):
        errors, _ = self.validar("## Aplicar\n\nenunciado sem rubrica\n")

        self.assertTrue(
            any("Aplicar requer critérios de avaliação" in erro for erro in errors), errors
        )

    def test_niveis_superiores_a_aplicar_nao_exigem_rubrica(self):
        """Convenção deste repositório: rubrica só no nível Aplicar."""
        errors, _ = self.validar("## Analisar\n\nenunciado curto\n")

        self.assertFalse(any("Analisar requer" in erro for erro in errors), errors)


class MultiplataformaTest(unittest.TestCase):
    def setUp(self):
        self.pagina = ROOT / "docs" / "oficina-ficticia.md"

    def validar(self, texto):
        errors = []
        validate_multiplatform(self.pagina, texto, errors)
        return errors

    def test_aba_posix_sem_par_windows_e_reprovada(self):
        errors = self.validar('=== "macOS/Linux"\n\n    ls -la\n')

        self.assertTrue(any("sem a aba Windows" in erro for erro in errors), errors)

    def test_par_completo_e_aceito(self):
        errors = self.validar(
            '=== "macOS/Linux"\n\n    ls -la\n\n=== "Windows (PowerShell)"\n\n    dir\n'
        )

        self.assertEqual([], errors)

    def test_marcador_de_aba_dentro_de_prosa_nao_conta(self):
        errors = self.validar('O agente escreve `tipo === "Atacado"` sem saber a convenção.\n')

        self.assertEqual([], errors)


class ImagemDeclaradaTest(unittest.TestCase):
    """Imagem declarada com barra resolve na pasta da sessão, sem barra em docs/assets/images/."""

    SLUG = "sessao-99-teste"

    def setUp(self):
        self.temporario = tempfile.TemporaryDirectory(dir=ROOT)
        self.raiz = Path(self.temporario.name)
        self.docs = self.raiz / "docs"
        (self.docs / self.SLUG / "assets").mkdir(parents=True)
        (self.docs / "assets" / "images").mkdir(parents=True)

    def tearDown(self):
        self.temporario.cleanup()

    def validar(self, imagens):
        errors = []
        sessoes = {self.SLUG: ("Teste", True, imagens)}
        with mock.patch.multiple(
            validador,
            ROOT=self.raiz,
            DOCS=self.docs,
            IMAGES=self.docs / "assets" / "images",
            SESSOES=sessoes,
        ):
            validate_session(self.SLUG, errors, Counts(), Counter())
        return [erro for erro in errors if "imagem declarada" in erro]

    def test_caminho_com_barra_presente_na_pasta_da_sessao_e_aceito(self):
        (self.docs / self.SLUG / "assets" / "figura.png").write_bytes(b"png")

        self.assertEqual([], self.validar(("assets/figura.png",)))

    def test_caminho_com_barra_resolve_na_sessao_e_nao_em_assets_images(self):
        (self.docs / "assets" / "images" / "figura.png").write_bytes(b"png")

        erros = self.validar(("assets/figura.png",))

        self.assertEqual(1, len(erros), erros)
        self.assertIn(f"docs/{self.SLUG}/assets/figura.png", erros[0])


class SlugTest(unittest.TestCase):
    def test_slug_reproduz_a_ancora_do_python_markdown(self):
        self.assertEqual("de-prompt-engineering-para-context", slugify("De prompt engineering para context"))
        self.assertEqual("evidencia-empirica", slugify("Evidência empírica"))
        self.assertEqual("mcp-quando-conectar", slugify("MCP: quando conectar"))

    def test_ancoras_do_documento_reunem_cabecalhos_e_ancoras_html(self):
        anchors = document_anchors('# Título\n\n<a id="preservada"></a>\n\n## Outra seção\n')

        self.assertIn("titulo", anchors)
        self.assertIn("preservada", anchors)
        self.assertIn("outra-secao", anchors)


if __name__ == "__main__":
    unittest.main()
