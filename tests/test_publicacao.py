"""O pipeline de publicação também é artefato versionado, e é testado como tal."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

from scripts.validate_content import ROOT

WORKFLOW = ROOT / ".github" / "workflows" / "publicar-site.yml"
MKDOCS = ROOT / "mkdocs.yml"


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.texto = WORKFLOW.read_text(encoding="utf-8")

    def test_publica_no_push_da_main_e_permite_disparo_manual(self):
        self.assertIn("branches:\n      - main", self.texto)
        self.assertIn("workflow_dispatch:", self.texto)

    def test_permissoes_minimas_e_concorrencia_por_grupo(self):
        self.assertIn("contents: read", self.texto)
        self.assertIn("pages: write", self.texto)
        self.assertIn("id-token: write", self.texto)
        self.assertIn("group: pages", self.texto)
        self.assertIn("cancel-in-progress: true", self.texto)

    def test_acoes_de_terceiros_estao_fixadas_por_versao_maior(self):
        usos = re.findall(r"uses: ([^\s]+)", self.texto)
        self.assertTrue(usos)
        for uso in usos:
            with self.subTest(uso=uso):
                self.assertRegex(uso, r"@v\d+$")

    def test_roda_testes_e_validacao_antes_de_construir_o_site(self):
        ordem = [
            self.texto.index("python -m unittest discover -s tests"),
            self.texto.index("python scripts/validate_content.py --all"),
            self.texto.index("mkdocs build --strict"),
        ]
        self.assertEqual(sorted(ordem), ordem)

    def test_constroi_em_modo_estrito(self):
        self.assertIn("mkdocs build --strict", self.texto)

    def test_publica_no_ambiente_do_github_pages(self):
        self.assertIn("environment:\n      name: github-pages", self.texto)
        self.assertIn("actions/deploy-pages@v4", self.texto)

    def test_o_job_de_deploy_depende_do_job_de_build(self):
        self.assertIn("needs: build", self.texto)


class ComandosDocumentadosTest(unittest.TestCase):
    def test_o_validador_expoe_ajuda_e_termina_bem(self):
        resultado = subprocess.run(
            [sys.executable, "scripts/validate_content.py", "--help"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, resultado.returncode, resultado.stderr)
        self.assertIn("--all", resultado.stdout)

    def test_o_validador_exige_escolher_o_escopo(self):
        resultado = subprocess.run(
            [sys.executable, "scripts/validate_content.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(0, resultado.returncode)


class ConfiguracaoDoSiteTest(unittest.TestCase):
    def setUp(self):
        self.texto = MKDOCS.read_text(encoding="utf-8")

    def test_extensoes_usadas_pelo_material_estao_habilitadas(self):
        for extensao in ("attr_list", "md_in_html", "admonition", "pymdownx.tabbed"):
            with self.subTest(extensao=extensao):
                self.assertIn(extensao, self.texto)

    def test_abas_por_plataforma_usam_o_estilo_alternativo(self):
        self.assertIn("alternate_style: true", self.texto)

    def test_o_site_declara_idioma_e_endereco_de_publicacao(self):
        self.assertIn("language: pt-BR", self.texto)
        self.assertIn("site_url:", self.texto)


if __name__ == "__main__":
    unittest.main()
