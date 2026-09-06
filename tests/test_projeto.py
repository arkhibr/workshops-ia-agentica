"""Estrutura do projeto e coerência entre o disco, o nav e a tabela de sessões."""

from pathlib import Path
import re
import unittest

from scripts.validate_content import DOCS, IMAGES, ROOT, SESSOES

ARQUIVOS_OBRIGATORIOS = (
    "mkdocs.yml",
    "requirements.txt",
    "scripts/validate_content.py",
    ".github/workflows/publicar-site.yml",
    "docs/index.md",
    "docs/referencia/bibliografia.md",
)


class EstruturaTest(unittest.TestCase):
    def test_arquivos_obrigatorios_existem(self):
        for relativo in ARQUIVOS_OBRIGATORIOS:
            with self.subTest(arquivo=relativo):
                self.assertTrue((ROOT / relativo).is_file())

    def test_a_tabela_de_sessoes_cobre_as_dez_sessoes_do_disco(self):
        no_disco = sorted(p.name for p in DOCS.iterdir() if p.name.startswith("sessao-"))

        self.assertEqual(sorted(SESSOES), no_disco)
        self.assertEqual(10, len(SESSOES))

    def test_toda_pagina_do_disco_aparece_no_nav(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        declaradas = set(re.findall(r"([\w./-]+\.md)", config))

        for caminho in sorted(DOCS.rglob("*.md")):
            relativo = caminho.relative_to(DOCS).as_posix()
            with self.subTest(pagina=relativo):
                self.assertIn(relativo, declaradas)

    def test_o_nav_nao_aponta_para_pagina_inexistente(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

        for relativo in re.findall(r"(?m):\s+([\w./-]+\.md)\s*$", config):
            with self.subTest(pagina=relativo):
                self.assertTrue((DOCS / relativo).is_file())

    def test_toda_imagem_do_disco_e_usada_por_alguma_pagina(self):
        markdown = "\n".join(p.read_text(encoding="utf-8") for p in DOCS.rglob("*.md"))

        for imagem in sorted(IMAGES.glob("*.png")):
            if imagem.name == "favicon.png":
                continue
            with self.subTest(imagem=imagem.name):
                self.assertIn(imagem.name, markdown)

    def test_sessao_incompleta_tem_apenas_o_indice(self):
        for slug, (_, completa, _) in SESSOES.items():
            if completa:
                continue
            with self.subTest(slug=slug):
                self.assertEqual(["index.md"], [p.name for p in (DOCS / slug).glob("*.md")])

    def test_horario_fixo_declarado_no_material(self):
        """10h–12h com intervalo de 5 min às 11h é decisão fechada."""
        for slug, (_, completa, _) in SESSOES.items():
            if not completa:
                continue
            with self.subTest(slug=slug):
                indice = (DOCS / slug / "index.md").read_text(encoding="utf-8")
                self.assertIn("Roteiro da sessão (2h, das 10h às 12h)", indice)
                self.assertIn("| — | Intervalo | — | 5 min | — |", indice)


if __name__ == "__main__":
    unittest.main()
