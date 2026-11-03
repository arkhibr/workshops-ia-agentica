"""Lista local de termos privativos usada pelas checagens de privacidade.

A lista fica fora do Git, em docs/superpowers/notes/termos-privados.txt. Sem o
arquivo, os testes que dependem dela são pulados.
"""

import re
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent / "docs" / "superpowers" / "notes" / "termos-privados.txt"
AVISO_SEM_LISTA = (
    "lista local de termos privativos ausente: a checagem de privacidade só roda na máquina do autor"
)


def padroes():
    """Devolve [(termo, regex compilada)] ou None quando o arquivo local não existe."""
    if not ARQUIVO.is_file():
        return None
    resultado = []
    for linha in ARQUIVO.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        regra, termo = linha.split(" ", 1)
        if regra == "sem-caixa":
            regex = re.compile(re.escape(termo), re.IGNORECASE)
        elif regra == "limite":
            regex = re.compile(rf"\b{re.escape(termo)}\b")
        elif regra == "exato":
            regex = re.compile(re.escape(termo))
        else:
            raise ValueError(f"regra desconhecida na lista local de termos: {regra}")
        resultado.append((termo, regex))
    if not resultado:
        raise ValueError("lista local de termos privativos vazia")
    return resultado
