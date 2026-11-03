"""Gera o zip do marketplace governado que a oficina da Sessão 9 publica para download.

Uso, igual nos três sistemas, a partir da raiz do repositório:

    python scripts/gerar_zip_marketplace.py

O zip reúne os arquivos de exemplo/marketplace-governado/ listados em ARQUIVOS, sem
node_modules, na raiz do arquivo compactado. A data fixa, a ordem fixa e as permissões
fixas tornam a saída reprodutível: o mesmo conteúdo gera o mesmo zip.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGEM = ROOT / "exemplo" / "marketplace-governado"
DESTINO = ROOT / "docs" / "sessao-09-governanca-de-skills-e-agentes" / "assets" / "marketplace-governado.zip"

PLUGINS = ("identificando-tarefas-e-riscos", "revisando-pull-requests")
ARQUIVOS: tuple[str, ...] = (
    "README.md",
    "package.json",
    "portao.mjs",
    "test/portao.test.mjs",
    "marketplace-acme/.claude-plugin/marketplace.json",
) + tuple(
    f"marketplace-acme/plugins/{plugin}/{arquivo}"
    for plugin in PLUGINS
    for arquivo in (".claude-plugin/plugin.json", "governanca.json", f"skills/{plugin}/SKILL.md")
)

DATA_FIXA = (1980, 1, 1, 0, 0, 0)


def gerar(destino: Path = DESTINO) -> Path:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w") as arquivo_zip:
        for relativo in sorted(ARQUIVOS):
            info = zipfile.ZipInfo(relativo, date_time=DATA_FIXA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            info.create_system = 3
            arquivo_zip.writestr(info, (ORIGEM / relativo).read_bytes(), compresslevel=9)
    return destino


if __name__ == "__main__":
    caminho = gerar(Path(sys.argv[1]) if len(sys.argv) > 1 else DESTINO)
    print(f"zip gerado: {caminho.relative_to(ROOT) if caminho.is_relative_to(ROOT) else caminho}")
