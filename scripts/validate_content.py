#!/usr/bin/env python3
"""Valida a estrutura e os portões editoriais do material do workshop.

Adaptado do validador da disciplina `arquitetura-solucoes-ia-generativa`, com as
convenções próprias deste repositório: sessões em vez de módulos, rubrica apenas
no nível Aplicar, e teoria organizada por tema em vez do par conceitos/padrões.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMAGES = DOCS / "assets" / "images"

# `completa` distingue a sessão já desenvolvida da que ainda é esqueleto.
# Ao construir uma sessão nova, vire a chave e declare as imagens esperadas.
SESSOES: dict[str, tuple[str, bool, tuple[str, ...]]] = {
    "sessao-01-o-que-mudou": (
        "O que mudou",
        True,
        (
            "s1-tres-modos-trabalho.png",
            "s1-software-1-2-3.png",
            "s1-ciclo-engenharia-agentica.png",
            "s1-regua-escolha.png",
            "s1-simplicidade-risco.png",
        ),
    ),
    "sessao-02-ambiente-agentico": (
        "O ambiente agêntico",
        True,
        (
            "s2-anatomia-ambiente-agentico.png",
            "s2-context-engineering.png",
            "s2-mcp-mxn-mmaisn.png",
            "s2-ambiente-compartilhado.png",
            "s2-regua-investimento.png",
            "s2-decisoes-instrucao-mcp.png",
            "s2-commit-que-sumiu.png",
            "s2-vetor-ambiente-tres-passos.png",
        ),
    ),
    "sessao-03-exploracao-especificacao": ("Exploração e especificação", False, ()),
    "sessao-04-regras-formais-com-ia": ("Regras formais com IA", False, ()),
    "sessao-05-decomposicao": ("Decomposição", False, ()),
    "sessao-06-tdd-assistido": ("TDD assistido por IA", False, ()),
    "sessao-07-estrategias-avancadas-teste": ("Estratégias avançadas de teste", False, ()),
    "sessao-08-sdd-ciclo-completo": ("SDD ciclo completo", False, ()),
    "sessao-09-depuracao-sistematica": ("Depuração sistemática", False, ()),
    "sessao-10-esteira-completa": ("Esteira completa", False, ()),
}

# As seis páginas de papel fixo. Tudo o mais numa sessão é página temática de teoria.
PAGINAS_FIXAS = (
    "index.md",
    "exemplo-arquitetural.md",
    "estudo-de-caso.md",
    "oficina-de-ferramentas.md",
    "exercicios.md",
    "sintese-e-referencias.md",
)
NAO_TEMATICA = frozenset(PAGINAS_FIXAS)

# Páginas que encerram a sessão e por isso não carregam transição de saída.
SEM_TRANSICAO = frozenset({"exercicios.md", "sintese-e-referencias.md"})

BLOOM = ("Recordar", "Compreender", "Aplicar", "Analisar", "Avaliar", "Criar")
BLOOM_COM_GABARITO = ("Recordar", "Compreender")
BLOOM_COM_RUBRICA = ("Aplicar",)

TEMAS_MIN, TEMAS_MAX = 3, 8
PALAVRAS_MIN, PALAVRAS_MAX = 300, 2100

MARCADORES_PROIBIDOS = ("TODO", "TBD", "PLACEHOLDER", "PREENCHER")

IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
REFERENCE_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\[([^\]]+)\]")
REFERENCE_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\[([^\]]+)\]")
REFERENCE_DEFINITION_RE = re.compile(r"(?m)^[ \t]{0,3}\[([^\]]+)\]:[ \t]*(.+?)[ \t]*$")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HTML_ATTRIBUTE_RE = re.compile(r"([:\w-]+)\s*=\s*(?:\"([^\"]*)\"|'([^']*)')", re.IGNORECASE)
HEADING_RE = re.compile(r"(?m)^(#{1,6})[ \t]+(.*?)[ \t]*$")
EXPLICIT_ANCHOR_RE = re.compile(r"<a\s+id=\"([^\"]+)\"", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
TAB_RE = re.compile(r"(?m)^=== \"([^\"]+)\"")
TRANSICAO_RE = re.compile(r"(?m)^\*\*Próxima página:\*\*")
WORD_RE = re.compile(r"\b[^\W\d_]+(?:[-’'][^\W\d_]+)*\b", re.UNICODE)


@dataclass
class Counts:
    pages: int = 0
    words: int = 0
    images: int = 0
    exercises: int = 0


def thematic_pages(session_dir: Path) -> tuple[str, ...]:
    """Nomes das páginas temáticas de uma sessão, em ordem de arquivo."""
    return tuple(
        path.name
        for path in sorted(session_dir.glob("*.md"))
        if path.name not in NAO_TEMATICA
    )


def teaching_text(session_dir: Path) -> str:
    """Concatena as páginas temáticas de uma sessão.

    A organização por tema substituiu o par conceitos/padrões: a asserção
    editorial passa a ser "este conteúdo existe nesta sessão", não "está nesta
    página". Testes de conteúdo devem usar este auxiliar em vez de abrir um
    arquivo específico.
    """
    return "\n\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(session_dir.glob("*.md"))
        if path.name not in NAO_TEMATICA
    )


def strip_fences(text: str) -> str:
    """Remove blocos de código cercados, para checagens que só valem em prosa."""
    out, fenced = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            out.append(line)
    return "\n".join(out)


def markdown_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split()[0] if target.split() else target


def local_path(source: Path, raw_target: str) -> Path | None:
    target = markdown_target(raw_target)
    if not target or target.startswith("#"):
        return None
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    return (source.parent / unquote(parts.path)).resolve()


def document_anchors(text: str) -> set[str]:
    anchors = {anchor.casefold() for anchor in EXPLICIT_ANCHOR_RE.findall(text)}
    for _, title in HEADING_RE.findall(strip_fences(text)):
        anchors.add(slugify(title))
    return anchors


def slugify(title: str) -> str:
    """Reproduz o slug de âncora do Python-Markdown (extensão toc)."""
    import unicodedata

    text = unicodedata.normalize("NFKD", title.strip().lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", text.strip())


def validate_anchor(source: Path, resolved: Path, raw_target: str, errors: list[str]) -> None:
    fragment = unquote(urlsplit(markdown_target(raw_target)).fragment)
    if not fragment or resolved.suffix.casefold() != ".md":
        return
    if fragment.casefold() not in document_anchors(resolved.read_text(encoding="utf-8")):
        errors.append(
            f"{source.relative_to(ROOT)}: âncora inexistente no destino: "
            f"{markdown_target(raw_target)}"
        )


def validate_references(
    path: Path,
    text: str,
    errors: list[str],
    counts: Counts,
    image_references: Counter[Path] | None = None,
) -> None:
    definitions = {
        reference_id.strip().casefold(): target
        for reference_id, target in REFERENCE_DEFINITION_RE.findall(text)
    }

    for alt, target in IMAGE_RE.findall(text):
        counts.images += 1
        if not alt.strip():
            errors.append(f"{path.relative_to(ROOT)}: imagem com texto alternativo vazio")
        destination = local_path(path, target)
        if destination is None:
            continue
        if image_references is not None:
            image_references[destination] += 1
        if not destination.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: imagem local inexistente: {markdown_target(target)}"
            )

    for tag in HTML_IMAGE_RE.findall(text):
        attributes = {
            name.casefold(): double or single
            for name, double, single in HTML_ATTRIBUTE_RE.findall(tag)
        }
        counts.images += 1
        if not attributes.get("alt", "").strip():
            errors.append(f"{path.relative_to(ROOT)}: imagem com texto alternativo vazio")
        target = attributes.get("src", "").strip()
        if not target:
            errors.append(f"{path.relative_to(ROOT)}: imagem HTML sem origem: src ausente ou vazio")
            continue
        destination = local_path(path, target)
        if destination is None:
            continue
        if image_references is not None:
            image_references[destination] += 1
        if not destination.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: imagem local inexistente: {markdown_target(target)}"
            )

    for target in LINK_RE.findall(text):
        destination = local_path(path, target)
        if destination is None:
            continue
        if destination.is_dir():
            destination = destination / "index.md"
        if not destination.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: link relativo inexistente: {markdown_target(target)}"
            )
        else:
            validate_anchor(path, destination, target, errors)

    for alt, reference_id in REFERENCE_IMAGE_RE.findall(text):
        counts.images += 1
        if not alt.strip():
            errors.append(f"{path.relative_to(ROOT)}: imagem com texto alternativo vazio")
        target = definitions.get(reference_id.strip().casefold())
        if target is None:
            errors.append(
                f"{path.relative_to(ROOT)}: referência de imagem sem definição: {reference_id}"
            )
            continue
        destination = local_path(path, target)
        if destination is None:
            continue
        if image_references is not None:
            image_references[destination] += 1
        if not destination.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: imagem local inexistente: {markdown_target(target)}"
            )

    for reference_id in REFERENCE_LINK_RE.findall(text):
        target = definitions.get(reference_id.strip().casefold())
        if target is None:
            errors.append(
                f"{path.relative_to(ROOT)}: referência de link sem definição: {reference_id}"
            )
            continue
        destination = local_path(path, target)
        if destination is None:
            continue
        if destination.is_dir():
            destination = destination / "index.md"
        if not destination.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: link relativo inexistente: {markdown_target(target)}"
            )
        else:
            validate_anchor(path, destination, target, errors)


def bloom_sections(text: str) -> dict[str, str]:
    """Mapeia cada nível de Bloom para o corpo da sua seção."""
    prose = strip_fences(text)
    headings = list(HEADING_RE.finditer(prose))
    sections: dict[str, str] = {}
    for index, match in enumerate(headings):
        level, title = len(match.group(1)), match.group(2).strip()
        if title not in BLOOM:
            continue
        end = len(prose)
        for later in headings[index + 1 :]:
            if len(later.group(1)) <= level:
                end = later.start()
                break
        sections[title] = prose[match.end() : end]
    return sections


def validate_exercises(path: Path, text: str, errors: list[str], counts: Counts) -> None:
    sections = bloom_sections(text)
    counts.exercises += len(sections)
    for level in BLOOM:
        if level not in sections:
            errors.append(f"{path.relative_to(ROOT)}: seção de Bloom ausente: {level}")

    for level in BLOOM_COM_GABARITO:
        section = sections.get(level, "")
        if not re.search(r"<details(?:\s|>)", section, re.IGNORECASE) or not re.search(
            r"</details\s*>", section, re.IGNORECASE
        ):
            errors.append(f"{path.relative_to(ROOT)}: {level} requer bloco <details> com gabarito")

    for level in BLOOM_COM_RUBRICA:
        if not re.search(r"\*\*Critérios de avaliação\*\*", sections.get(level, "")):
            errors.append(f"{path.relative_to(ROOT)}: {level} requer critérios de avaliação")


def validate_multiplatform(path: Path, text: str, errors: list[str]) -> None:
    """Todo grupo de abas que abre com macOS/Linux precisa da aba de Windows."""
    labels = TAB_RE.findall(text)
    for index, label in enumerate(labels):
        if "macOS" not in label and "Linux" not in label:
            continue
        seguinte = labels[index + 1] if index + 1 < len(labels) else ""
        if not seguinte.startswith("Windows"):
            errors.append(
                f"{path.relative_to(ROOT)}: bloco de abas '{label}' sem a aba Windows correspondente"
            )


def validate_session(
    slug: str, errors: list[str], counts: Counts, image_references: Counter[Path]
) -> None:
    session_dir = DOCS / slug
    _, completa, imagens = SESSOES[slug]

    if not session_dir.is_dir():
        errors.append(f"sessão ausente: docs/{slug}")
        return

    if completa:
        for page_name in PAGINAS_FIXAS:
            if not (session_dir / page_name).is_file():
                errors.append(f"página ausente: docs/{slug}/{page_name}")

        temas = thematic_pages(session_dir)
        if not TEMAS_MIN <= len(temas) <= TEMAS_MAX:
            errors.append(
                f"docs/{slug}: {len(temas)} páginas temáticas, "
                f"fora da faixa de {TEMAS_MIN} a {TEMAS_MAX}"
            )
        for name in ("conceitos.md", "padroes-e-decisoes.md"):
            if (session_dir / name).is_file():
                errors.append(
                    f"docs/{slug}/{name}: a teoria é organizada por tema; "
                    "página por tipo de conteúdo não é permitida"
                )
        for name in temas:
            palavras = len(WORD_RE.findall((session_dir / name).read_text(encoding="utf-8")))
            if not PALAVRAS_MIN <= palavras <= PALAVRAS_MAX:
                errors.append(
                    f"docs/{slug}/{name}: {palavras} palavras, "
                    f"fora da faixa de {PALAVRAS_MIN} a {PALAVRAS_MAX}"
                )

        for esperada in imagens:
            if not (IMAGES / esperada).is_file():
                errors.append(f"imagem declarada e ausente: docs/assets/images/{esperada}")

    for path in sorted(session_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        counts.pages += 1
        counts.words += len(WORD_RE.findall(text))

        for marcador in MARCADORES_PROIBIDOS:
            if re.search(rf"\b{marcador}\b", text):
                errors.append(f"{path.relative_to(ROOT)}: marcador editorial proibido: {marcador}")

        validate_references(path, text, errors, counts, image_references)
        validate_multiplatform(path, text, errors)

        if completa and path.name not in SEM_TRANSICAO and not TRANSICAO_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: página sem a transição '**Próxima página:**'")

        if path.name == "exercicios.md" and completa:
            validate_exercises(path, text, errors, counts)


def validate_shared_pages(
    errors: list[str], counts: Counts, image_references: Counter[Path]
) -> None:
    """Valida o Markdown fora das sessões sem somá-lo ao orçamento delas."""
    session_dirs = {DOCS / slug for slug in SESSOES}
    for path in sorted(DOCS.rglob("*.md")):
        if any(session_dir in path.parents for session_dir in session_dirs):
            continue
        text = path.read_text(encoding="utf-8")
        for marcador in MARCADORES_PROIBIDOS:
            if re.search(rf"\b{marcador}\b", text):
                errors.append(f"{path.relative_to(ROOT)}: marcador editorial proibido: {marcador}")
        validate_references(path, text, errors, counts, image_references)


def validate_nav(errors: list[str]) -> None:
    """Toda página de docs/ precisa aparecer no nav do mkdocs."""
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    declaradas = set(re.findall(r"([\w./-]+\.md)", config))
    for path in sorted(DOCS.rglob("*.md")):
        relativa = path.relative_to(DOCS).as_posix()
        if relativa not in declaradas:
            errors.append(f"docs/{relativa}: página fora do nav do mkdocs.yml")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Valida páginas, exercícios, links, âncoras e imagens do workshop."
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--sessao", choices=tuple(SESSOES), metavar="SLUG")
    selection.add_argument("--all", action="store_true", help="valida todas as sessões")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slugs = tuple(SESSOES) if args.all else (args.sessao,)
    errors: list[str] = []
    counts = Counts()
    image_references: Counter[Path] = Counter()

    for slug in slugs:
        validate_session(slug, errors, counts, image_references)
    if args.all:
        validate_shared_pages(errors, counts, image_references)
        validate_nav(errors)

    print(
        f"Páginas: {counts.pages} | Palavras: {counts.words} | "
        f"Imagens: {counts.images} | Níveis de exercício: {counts.exercises}"
    )
    if errors:
        print(f"Validação falhou com {len(errors)} erro(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Validação concluída sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
