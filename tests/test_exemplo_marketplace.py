"""O marketplace governado de exemplo da Sessão 9 e a regra de não conter dado real."""

import json
import re
import unittest
import zipfile

import termos_privados
from scripts import gerar_zip_marketplace
from scripts.validate_content import ROOT

PASTA = ROOT / "exemplo" / "marketplace-governado"
PLUGINS = ("identificando-tarefas-e-riscos", "revisando-pull-requests")


OFICINA = ROOT / "docs" / "sessao-09-governanca-de-skills-e-agentes" / "oficina-de-ferramentas.md"
ZIP = ROOT / "docs" / "sessao-09-governanca-de-skills-e-agentes" / "assets" / "marketplace-governado.zip"
# Um bloco publicado é precedido pela linha **Arquivo:** `<caminho>`, relativo a PASTA.
# O rótulo fica fora do bloco porque o JSON não aceita comentário.
BLOCO_PUBLICADO_RE = re.compile(r"(?m)^\*\*Arquivo:\*\* `([^`]+)`\n\n```[a-z]*\n(.*?)^```$", re.DOTALL)
# A página publica por inteiro só a ficha que o participante corrige no Experimento B.
PUBLICADOS = ("marketplace-acme/plugins/revisando-pull-requests/governanca.json",)
# O restante chega ao participante pelo zip, que a oficina manda baixar no Experimento A.
# Regenerar com: python scripts/gerar_zip_marketplace.py
NO_ZIP = ("README.md", "package.json", "portao.mjs", "test/portao.test.mjs",
          "marketplace-acme/.claude-plugin/marketplace.json") + tuple(
    f"marketplace-acme/plugins/{plugin}/{arquivo}"
    for plugin in PLUGINS
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

    def test_bloco_publicado_igual_ao_arquivo(self):
        blocos = BLOCO_PUBLICADO_RE.findall(OFICINA.read_text(encoding="utf-8"))
        self.assertEqual(sorted(PUBLICADOS), sorted(caminho for caminho, _ in blocos))
        for caminho, conteudo in blocos:
            with self.subTest(arquivo=caminho):
                self.assertEqual((PASTA / caminho).read_text(encoding="utf-8"), conteudo)

    def test_zip_igual_aos_arquivos_do_exemplo(self):
        self.assertTrue(ZIP.is_file(), "rode python scripts/gerar_zip_marketplace.py")
        with zipfile.ZipFile(ZIP) as arquivo_zip:
            self.assertEqual(sorted(NO_ZIP), sorted(arquivo_zip.namelist()))
            for relativo in NO_ZIP:
                with self.subTest(arquivo=relativo):
                    self.assertEqual((PASTA / relativo).read_bytes(), arquivo_zip.read(relativo),
                                     "zip desatualizado: rode python scripts/gerar_zip_marketplace.py")

    def test_gerador_lista_os_mesmos_arquivos(self):
        self.assertEqual(sorted(NO_ZIP), sorted(gerar_zip_marketplace.ARQUIVOS))

    def test_oficina_aponta_para_o_zip(self):
        experimento_a = OFICINA.read_text(encoding="utf-8").split("## Experimento A", 1)[1].split("\n## ", 1)[0]
        self.assertIn("](assets/marketplace-governado.zip)", experimento_a)
        self.assertIn("unzip marketplace-governado.zip", experimento_a)
        self.assertIn("Expand-Archive marketplace-governado.zip", experimento_a)

if __name__ == "__main__":
    unittest.main()
