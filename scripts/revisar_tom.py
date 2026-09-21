#!/usr/bin/env python3
"""Relatório de licenças poéticas e cacoetes de IA no material publicado.

Não bloqueia o portão de qualidade. Serve para localizar, em texto corrido, os
padrões que a revisão manual não encontra de forma confiável: remate sem
informação, staccato, metáfora, personificação de artefato, contraste artificial,
clivagem enfática e título em forma de oração.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

METAFORA = [
    "puxar o fio", "passar batido", "bater cabeça", "derrapar", "rede de segurança",
    "elefante na sala", "morno-quente", "dar de cara", "no fim das contas", "em voz alta",
    "mastigado", "pra valer", "de graça", "cardápio", "roupa nova", "mora a ambiguidade",
    "mora no", "moram", "cai por terra", "à toa", "de bandeja", "pano de fundo",
    "ponta do iceberg", "saltar aos olhos", "vale destacar", "em suma", "mergulhar",
    "dito isso", "por sua vez", "abrir caminho", "dar o tom", "ganhar corpo", "pôr de pé",
    "colocar de pé", "na veia", "de cara", "do zero ao", "a régua", "régua",
    "calcanhar de aquiles", "pedra no sapato", "tiro no pé", "bala de prata",
    "caixa-preta", "caixa preta", "terreno", "armadilha", "esqueleto", "espinha dorsal",
    "coração do", "alma do", "no papel", "no mundo real", "na vida real", "sangue",
    "cicatriz", "ferida", "veneno", "remédio", "vacina", "anticorpo",
]
COLOQUIAL = [
    "do seu lado", "do nosso lado", "do lado de", "em lugar nenhum", "lugar nenhum",
    "qualquer coisa", "a gente", "da gente", "pra ", "pro ", "tá ", "né", "acaba sendo",
    "acaba virando", "de uma vez", "por aí", "e por aí vai", "coisa que", "um monte de",
    "na hora de", "na hora em que", "de cara", "sem mais", "todo mundo", "ninguém mais",
    "o tempo todo", "de vez em quando", "aos poucos", "mais ou menos", "meio que",
    "na melhor das hipóteses", "no mínimo", "pelo menos por enquanto", "de verdade",
]
PERSONIFICACAO = re.compile(
    r"\b(o|a)\s+(código|especificação|requisito|regra|teste|documento|arquivo|agente|modelo|sistema|página|tabela)\s+"
    r"(esconde|escolhe|decide|acredita|sabe|quer|prefere|entende|percebe|finge|mente|promete|jura|confessa)\b",
    re.I,
)
CLIVAGEM = re.compile(r"\b(é isso que|é ela que|é ele que|é aí que|foi isso que|é o que faz)\b", re.I)
CONTRASTE = [
    r"\bnão é [^.,]{2,45}, é \b", r"\bnão está em [^.,]{2,40} e sim\b", r"\bmenos [^.,]{2,30} e mais \b",
    r"\bnão apenas[^.]{2,60}mas também\b", r"\bnão só[^.]{2,60}mas\b", r"\bmais do que [^.,]{2,40}, \b",
]
AFORISMO = re.compile(r"^[A-ZÀ-Ú][^.!?]{10,70}\.$")
TEM_DADO = re.compile(r"\d|R\$|`|\b[A-Z]{2,}\b|\[[^\]]+\]\(")
TITULO_ORACAO = re.compile(
    r"^#{2,3}\s+(O que |Por que |Como |Quando |Onde |Quem |Se )|"
    r"^#{2,3}\s+.*\b(que|porque|quando)\b.*\b(é|são|foi|muda|vale|importa|funciona|acontece|esconde|sustenta|cobria|acompanha)\b",
    re.I,
)

def prosa(texto: str) -> str:
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    texto = re.sub(r"(?m)^\|.*$", "", texto)
    texto = re.sub(r"(?m)^\s{4,}.*$", "", texto)
    return texto

def paragrafos(texto: str) -> list[str]:
    for bruto in prosa(texto).split("\n\n"):
        p = bruto.strip().replace("\n", " ")
        if not p or p.startswith(("#", "|", ">", "!!!", "???", "<")):
            continue
        if re.match(r"^\s*(\d+\.|[-*])\s", p):
            continue
        if p.startswith("**") and p.count("**") <= 2 and len(p.split()) < 25:
            continue
        yield p

def frases(par: str) -> list[str]:
    return [f.strip() for f in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ú\"“])", par) if f.strip()]

def analisar(caminho: Path) -> list[tuple[str, str, str]]:
    texto = caminho.read_text(encoding="utf-8")
    achados = []
    for linha in texto.splitlines():
        if TITULO_ORACAO.match(linha):
            achados.append(("TITULO-ORACAO", linha.strip(), ""))
    corpo = prosa(texto)
    baixo = corpo.lower()
    for termo in METAFORA:
        for m in re.finditer(rf"\b{re.escape(termo)}\b", baixo):
            achados.append(("METAFORA", termo, corpo[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")))
    for termo in COLOQUIAL:
        for m in re.finditer(rf"\b{re.escape(termo.strip())}\b", baixo):
            achados.append(("COLOQUIAL", termo.strip(), corpo[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")))
    for m in PERSONIFICACAO.finditer(corpo):
        achados.append(("PERSONIFICACAO", m.group(0), ""))
    for m in CLIVAGEM.finditer(corpo):
        achados.append(("CLIVAGEM", m.group(0), corpo[max(0, m.start() - 50):m.end() + 60].replace("\n", " ")))
    for padrao in CONTRASTE:
        for m in re.finditer(padrao, baixo):
            achados.append(("CONTRASTE", m.group(0), ""))
    for par in paragrafos(texto):
        fs = frases(par)
        if len(fs) < 2:
            continue
        ultima = fs[-1]
        if len(ultima.split()) < 14 and not TEM_DADO.search(ultima):
            achados.append(("REMATE-SEM-DADO", ultima, ""))
        tam = [len(f.split()) for f in fs]
        if sum(tam) / len(tam) < 14:
            achados.append(("STACCATO-MEDIA", f"média {sum(tam)/len(tam):.1f}", par[:90]))
        else:
            for i in range(len(tam) - 2):
                if all(t < 12 for t in tam[i:i + 3]):
                    achados.append(("STACCATO-SEQ", " / ".join(fs[i:i + 3])[:120], ""))
                    break
        primeira = fs[0]
        if len(primeira.split()) < 8 and AFORISMO.match(primeira) and not TEM_DADO.search(primeira):
            achados.append(("ABERTURA-ANUNCIADORA", primeira, ""))
    return achados

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--caminho", default="docs")
    ap.add_argument("--resumo", action="store_true")
    args = ap.parse_args()
    alvo = ROOT / args.caminho
    arquivos = sorted(alvo.rglob("*.md")) if alvo.is_dir() else [alvo]
    total = 0
    por_tipo: dict[str, int] = {}
    por_arquivo: dict[str, int] = {}
    for caminho in arquivos:
        achados = analisar(caminho)
        if not achados:
            continue
        rel = str(caminho.relative_to(ROOT))
        por_arquivo[rel] = len(achados)
        if not args.resumo:
            print(f"\n=== {rel}")
        for tipo, trecho, contexto in achados:
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
            total += 1
            if not args.resumo:
                print(f"  [{tipo}] {trecho}")
                if contexto:
                    print(f"        …{contexto}")
    print("\n--- RESUMO ---")
    for tipo, n in sorted(por_tipo.items(), key=lambda x: -x[1]):
        print(f"{n:5d}  {tipo}")
    print(f"{total:5d}  TOTAL em {len(por_arquivo)} arquivos")
    if args.resumo:
        for rel, n in sorted(por_arquivo.items(), key=lambda x: -x[1])[:20]:
            print(f"  {n:4d}  {rel}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
