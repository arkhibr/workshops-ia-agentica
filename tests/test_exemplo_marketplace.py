"""O marketplace governado de exemplo da Sessão 9 e a regra de não conter dado real."""

import json
import re
import unittest

import termos_privados
from scripts.validate_content import ROOT

PASTA = ROOT / "exemplo" / "marketplace-governado"
PLUGINS = ("identificando-tarefas-e-riscos", "revisando-pull-requests")


OFICINA = ROOT / "docs" / "sessao-09-governanca-de-skills-e-agentes" / "oficina-de-ferramentas.md"
# Um bloco publicado é precedido pela linha **Arquivo:** `<caminho>`, relativo a PASTA.
# O rótulo fica fora do bloco porque o JSON não aceita comentário e o front-matter
# do SKILL.md precisa começar na primeira linha do arquivo.
BLOCO_PUBLICADO_RE = re.compile(r"(?m)^\*\*Arquivo:\*\* `([^`]+)`\n\n```[a-z]*\n(.*?)^```$", re.DOTALL)
PUBLICADOS = ("portao.mjs", "marketplace-acme/.claude-plugin/marketplace.json") + tuple(
    f"marketplace-acme/plugins/{plugin}/{arquivo}"
    for plugin in ("identificando-tarefas-e-riscos", "revisando-pull-requests")
    for arquivo in (".claude-plugin/plugin.json", "governanca.json", f"skills/{plugin}/SKILL.md")
)


class MarketplaceGovernadoTest(unittest.TestCase):
    def test_arquivos_do_exemplo_existem(self):
        relativos = ["README.md", "package.json", "portao.mjs", "test/portao.test.mjs",
                     "marketplace-acme/.claude-plugin/marketplace.json"]
        for plugin in PLUGINS:
            base = f"marketplace-acme/plugins/{plugin}"
            relativos += [f"{base}/.claude-plugin/plugin.json", f"{base}/governanca.json",
                          f"{base}/skills/{plugin}/SKILL.md"]
        for relativo in relativos:
            with self.subTest(arquivo=relativo):
                self.assertTrue((PASTA / relativo).is_file())

    def test_exemplo_nao_tem_dependencias(self):
        manifesto = json.loads((PASTA / "package.json").read_text(encoding="utf-8"))

        self.assertNotIn("dependencies", manifesto)
        self.assertNotIn("devDependencies", manifesto)
        self.assertEqual("node --test", manifesto["scripts"]["test"])

    def test_nenhum_termo_proibido_na_pasta(self):
        # A lista de termos é local e fica fora do Git: o repositório é público.
        padroes = termos_privados.padroes()
        if padroes is None:
            self.skipTest(termos_privados.AVISO_SEM_LISTA)
        for arquivo in PASTA.rglob("*"):
            if not arquivo.is_file() or "node_modules" in arquivo.parts:
                continue
            texto = arquivo.read_text(encoding="utf-8")
            for termo, regex in padroes:
                with self.subTest(arquivo=arquivo.name, termo=termo):
                    self.assertIsNone(regex.search(texto))
                    self.assertIsNone(regex.search(arquivo.name))

    def test_blocos_publicados_iguais_aos_arquivos(self):
        blocos = BLOCO_PUBLICADO_RE.findall(OFICINA.read_text(encoding="utf-8"))
        self.assertEqual(sorted(PUBLICADOS), sorted(caminho for caminho, _ in blocos))
        for caminho, conteudo in blocos:
            with self.subTest(arquivo=caminho):
                self.assertEqual((PASTA / caminho).read_text(encoding="utf-8"), conteudo)


if __name__ == "__main__":
    unittest.main()
