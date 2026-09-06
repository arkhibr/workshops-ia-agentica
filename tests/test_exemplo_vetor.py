"""O projeto de exemplo e a regra de que nenhum enunciado depende do repo do aluno.

Oficina e exercícios partem de `exemplo/vetor`, clonável por qualquer pessoa. A
transposição para o repositório real do participante existe como extensão no fim
da página, nunca como o caminho principal.
"""

import json
from pathlib import Path
import re
import unittest

from scripts.validate_content import DOCS, ROOT

VETOR = ROOT / "exemplo" / "vetor"
S2 = DOCS / "sessao-02-ambiente-agentico"
OFICINA = S2 / "oficina-de-ferramentas.md"
EXERCICIOS = S2 / "exercicios.md"


class ProjetoDeExemploTest(unittest.TestCase):
    def test_arquivos_do_exemplo_existem(self):
        for relativo in ("README.md", "package.json", "src/desconto.js", "test/desconto.test.js"):
            with self.subTest(arquivo=relativo):
                self.assertTrue((VETOR / relativo).is_file())

    def test_exemplo_nao_tem_dependencias(self):
        """Sem `npm install` no meio da aula."""
        manifesto = json.loads((VETOR / "package.json").read_text(encoding="utf-8"))

        self.assertNotIn("dependencies", manifesto)
        self.assertNotIn("devDependencies", manifesto)
        self.assertEqual("node --test", manifesto["scripts"]["test"])

    def test_a_lacuna_de_atacado_continua_aberta(self):
        """A faixa de atacado é o que os experimentos pedem ao agente."""
        codigo = (VETOR / "src" / "desconto.js").read_text(encoding="utf-8")

        self.assertIn("tipoCliente", codigo)
        self.assertNotIn("0.2", codigo)
        self.assertNotIn("10000", codigo)

    def test_o_teto_de_desconto_esta_coberto_por_teste(self):
        testes = (VETOR / "test" / "desconto.test.js").read_text(encoding="utf-8")

        self.assertIn("TETO_DESCONTO", testes)


class EnunciadoReprodutivelTest(unittest.TestCase):
    def test_a_oficina_comeca_pelo_clone_do_exemplo(self):
        texto = OFICINA.read_text(encoding="utf-8")

        self.assertIn("git clone https://github.com/arkhibr/workshops-ia-agentica.git", texto)
        self.assertIn("exemplo/vetor", texto)

    def test_a_oficina_nao_manda_escolher_um_repositorio_qualquer(self):
        texto = OFICINA.read_text(encoding="utf-8")

        for proibido in (
            "Escolha um repositório real que você usa",
            "não um exemplo genérico",
        ):
            with self.subTest(trecho=proibido):
                self.assertNotIn(proibido, texto)

    def test_nenhum_passo_de_execucao_depende_do_repositorio_do_participante(self):
        """Pergunta reflexiva pode citar o repositório do aluno; passo de execução, não."""
        texto = OFICINA.read_text(encoding="utf-8")
        extensao = texto.index("## Extensão")

        for ocorrencia in re.finditer(r"seu (próprio )?(projeto|repositório)", texto):
            inicio = ocorrencia.start()
            if inicio > extensao:
                continue
            anterior = texto[:inicio]
            ultima_questao = anterior.rfind("**Questões exploratórias:**")
            ultimo_passo = max(anterior.rfind("**Passo"), anterior.rfind("**Execute:**"))
            with self.subTest(posicao=inicio):
                self.assertGreater(
                    ultima_questao,
                    ultimo_passo,
                    f"passo de execução dependente do repo do aluno: {texto[inicio:inicio + 80]}",
                )

    def test_os_exercicios_declaram_a_situacao_compartilhada(self):
        texto = EXERCICIOS.read_text(encoding="utf-8")
        situacao = texto.split("## Recordar", 1)[0]

        self.assertIn("## Situação compartilhada", texto)
        self.assertIn("exemplo/vetor", situacao)
        self.assertIn("npm test", situacao)

    def test_a_situacao_vem_antes_do_primeiro_nivel_de_bloom(self):
        texto = EXERCICIOS.read_text(encoding="utf-8")

        self.assertLess(texto.index("## Situação compartilhada"), texto.index("## Recordar"))


if __name__ == "__main__":
    unittest.main()
