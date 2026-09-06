"""Invariantes da organização por tema, adotada em 06/09/2026.

A teoria de cada sessão vive em páginas temáticas, uma por assunto. Estes testes
protegem as regras que a reorganização estabeleceu, para que uma sessão nova não
volte ao par conceitos/padrões por inércia.
"""

from pathlib import Path
import re
import unittest

from scripts.validate_content import (
    DOCS,
    PAGINAS_FIXAS,
    SEM_TRANSICAO,
    SESSOES,
    TEMAS_MAX,
    TEMAS_MIN,
    strip_fences,
    thematic_pages,
)

COMPLETAS = tuple(slug for slug, (_, completa, _) in SESSOES.items() if completa)
LINHA_ROTEIRO_RE = re.compile(r"^\|[^|]*\|\s*\[[^\]]+\]\(([a-z0-9.-]+\.md)\)\s*\|(.*)$", re.M)
MINUTOS_RE = re.compile(r"(\d+)\s*min")


def linhas_do_roteiro(slug: str) -> list[tuple[str, str]]:
    texto = (DOCS / slug / "index.md").read_text(encoding="utf-8")
    return LINHA_ROTEIRO_RE.findall(texto)


class OrganizacaoTematicaTest(unittest.TestCase):
    def test_ha_pelo_menos_uma_sessao_completa(self):
        self.assertTrue(COMPLETAS, "nenhuma sessão marcada como completa em SESSOES")

    def test_nenhuma_sessao_tem_pagina_por_tipo_de_conteudo(self):
        for slug in SESSOES:
            for proibida in ("conceitos.md", "padroes-e-decisoes.md"):
                with self.subTest(slug=slug, pagina=proibida):
                    self.assertFalse((DOCS / slug / proibida).exists())

    def test_sessao_completa_tem_de_tres_a_oito_paginas_tematicas(self):
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                temas = thematic_pages(DOCS / slug)
                self.assertGreaterEqual(len(temas), TEMAS_MIN)
                self.assertLessEqual(len(temas), TEMAS_MAX)

    def test_pagina_tematica_tem_um_unico_titulo_de_nivel_um(self):
        for slug in COMPLETAS:
            for nome in thematic_pages(DOCS / slug):
                with self.subTest(slug=slug, pagina=nome):
                    prosa = strip_fences((DOCS / slug / nome).read_text(encoding="utf-8"))
                    self.assertEqual(1, len(re.findall(r"(?m)^# ", prosa)))

    def test_pagina_tematica_abre_com_contexto_antes_da_primeira_secao(self):
        """Toda página é autocontida: o leitor pode chegar direto nela."""
        for slug in COMPLETAS:
            for nome in thematic_pages(DOCS / slug):
                with self.subTest(slug=slug, pagina=nome):
                    prosa = strip_fences((DOCS / slug / nome).read_text(encoding="utf-8"))
                    corpo = prosa.split("\n", 1)[1]
                    abertura = corpo.split("\n## ", 1)[0].strip()
                    abertura = re.sub(r"<a\s+id=\"[^\"]+\"></a>", "", abertura).strip()
                    self.assertGreaterEqual(len(abertura.split()), 20)

    def test_paginas_encadeiam_ate_a_ultima_da_sessao(self):
        for slug in COMPLETAS:
            for caminho in sorted((DOCS / slug).glob("*.md")):
                if caminho.name in SEM_TRANSICAO:
                    continue
                with self.subTest(slug=slug, pagina=caminho.name):
                    self.assertIn("**Próxima página:**", caminho.read_text(encoding="utf-8"))

    def test_roteiro_lista_todas_as_paginas_da_sessao_menos_o_indice(self):
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                no_roteiro = [nome for nome, _ in linhas_do_roteiro(slug)]
                no_disco = {p.name for p in (DOCS / slug).glob("*.md")} - {"index.md"}
                self.assertEqual(sorted(no_disco), sorted(no_roteiro))

    def test_roteiro_soma_cento_e_vinte_minutos(self):
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                texto = (DOCS / slug / "index.md").read_text(encoding="utf-8")
                tabela = texto.split("## Roteiro da sessão", 1)[1].split("\n## ", 1)[0]
                minutos = [int(m) for m in MINUTOS_RE.findall(tabela)]
                declarado = [m for m in minutos if m == 120]
                self.assertTrue(declarado, "a tabela não declara o total de 120 min")
                self.assertEqual(120, sum(m for m in minutos if m != 120))

    def test_ordem_do_nav_segue_a_ordem_do_roteiro(self):
        config = (DOCS.parent / "mkdocs.yml").read_text(encoding="utf-8")
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                no_nav = re.findall(rf"{slug}/([a-z0-9.-]+\.md)", config)
                self.assertEqual("index.md", no_nav[0])
                self.assertEqual([nome for nome, _ in linhas_do_roteiro(slug)], no_nav[1:])

    def test_paginas_de_papel_fixo_existem_em_sessao_completa(self):
        for slug in COMPLETAS:
            for nome in PAGINAS_FIXAS:
                with self.subTest(slug=slug, pagina=nome):
                    self.assertTrue((DOCS / slug / nome).is_file())


if __name__ == "__main__":
    unittest.main()
