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
    SEM_TRANSICAO,
    SESSOES,
    paginas_fixas,
    strip_fences,
    thematic_pages,
)

COMPLETAS = tuple(slug for slug, (_, completa, _) in SESSOES.items() if completa)
LINHA_TABELA_RE = re.compile(r"(?m)^\|(?!-)(.+)\|[ \t]*$")
LINK_PAGINA_RE = re.compile(r"\[[^\]]+\]\(([a-z0-9.-]+\.md)\)")
HORARIO_RE = re.compile(r"^\d{2}:\d{2}[–-]\d{2}:\d{2}$")
MINUTOS_RE = re.compile(r"(\d+)\s*min")
TOTAL_DECLARADO = 120


def tabela_do_roteiro(slug: str) -> str:
    texto = (DOCS / slug / "index.md").read_text(encoding="utf-8")
    return texto.split("## Roteiro da sessão", 1)[1].split("\n## ", 1)[0]


def linhas_do_roteiro(slug: str) -> list[tuple[str, int, list[str]]]:
    """Cada linha da tabela vira (chave de bloco, minutos, páginas citadas).

    Dois formatos convivem. No formato com trilhas, a primeira célula é a faixa de
    horário e a chave é ela, porque linhas que repetem o mesmo horário são trilhas
    paralelas e valem uma vez só no relógio. No formato sem trilhas, a chave é a
    posição da linha e os minutos vêm da célula com "N min".
    """
    linhas = []
    for posicao, bruta in enumerate(LINHA_TABELA_RE.findall(tabela_do_roteiro(slug))):
        celulas = [c.strip() for c in bruta.split("|")]
        paginas = LINK_PAGINA_RE.findall(bruta)
        if celulas and HORARIO_RE.match(celulas[0]):
            minutos = int(celulas[1]) if len(celulas) > 1 and celulas[1].isdigit() else 0
            linhas.append((celulas[0], minutos, paginas))
            continue
        encontrados = [int(m) for m in MINUTOS_RE.findall(bruta)]
        minutos = encontrados[0] if encontrados else 0
        if minutos == TOTAL_DECLARADO:
            continue
        linhas.append((f"linha-{posicao}", minutos, paginas))
    return linhas


def paginas_do_roteiro(slug: str) -> list[str]:
    """Páginas na ordem da primeira aparição no roteiro, sem repetição."""
    ordem = []
    for _, _, paginas in linhas_do_roteiro(slug):
        for nome in paginas:
            if nome not in ordem:
                ordem.append(nome)
    return ordem


class OrganizacaoTematicaTest(unittest.TestCase):
    def test_ha_pelo_menos_uma_sessao_completa(self):
        self.assertTrue(COMPLETAS, "nenhuma sessão marcada como completa em SESSOES")

    def test_nenhuma_sessao_tem_pagina_por_tipo_de_conteudo(self):
        for slug in SESSOES:
            for proibida in ("conceitos.md", "padroes-e-decisoes.md"):
                with self.subTest(slug=slug, pagina=proibida):
                    self.assertFalse((DOCS / slug / proibida).exists())

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
                no_disco = {p.name for p in (DOCS / slug).glob("*.md")} - {"index.md"}
                self.assertEqual(sorted(no_disco), sorted(paginas_do_roteiro(slug)))

    def test_roteiro_soma_cento_e_vinte_minutos(self):
        """Linhas que repetem o mesmo horário são trilhas paralelas, contam uma vez."""
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                por_horario = {}
                for horario, minutos, _ in linhas_do_roteiro(slug):
                    por_horario[horario] = minutos
                self.assertTrue(por_horario, "a tabela do roteiro não tem linhas com horário")
                self.assertEqual(120, sum(por_horario.values()))

    def test_ordem_do_nav_segue_a_ordem_do_roteiro(self):
        config = (DOCS.parent / "mkdocs.yml").read_text(encoding="utf-8")
        for slug in COMPLETAS:
            with self.subTest(slug=slug):
                no_nav = re.findall(rf"{slug}/([a-z0-9.-]+\.md)", config)
                self.assertEqual("index.md", no_nav[0])
                self.assertEqual(paginas_do_roteiro(slug), no_nav[1:])

    def test_paginas_de_papel_fixo_existem_em_sessao_completa(self):
        for slug in COMPLETAS:
            for nome in paginas_fixas(slug):
                with self.subTest(slug=slug, pagina=nome):
                    self.assertTrue((DOCS / slug / nome).is_file())


if __name__ == "__main__":
    unittest.main()
