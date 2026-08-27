#!/usr/bin/env python3
"""
Prüft, ob ein Ausschluss-Keyword eigene aktive Keywords blockiert.

Das ist der häufigste Fehler in gewachsenen Google-Ads-Konten: Eine über die Jahre
gewachsene Negativliste blockiert Suchanfragen, die man eigentlich haben will. Bei
jeder Erweiterung der Ausschlusslisten sollte dieses Skript laufen.

Zugrunde gelegte Google-Logik für Ausschlüsse:
  Broad  - blockiert, wenn ALLE Wörter des Ausschlusses im Keyword vorkommen
           (Reihenfolge egal, keine Wortvarianten)
  Phrase - blockiert, wenn die Wortfolge zusammenhängend im Keyword vorkommt
  Exact  - blockiert nur bei exakter Übereinstimmung

Aufruf:  python3 tools/pruefe_negativlisten.py
Exit-Code 1, wenn ein aktives Keyword blockiert würde.
"""
import csv
import glob
import re
import signal
import sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass


def worte(text):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def blockiert(negativ, art, keyword):
    nw, kw = worte(negativ), worte(keyword)
    if not nw:
        return False
    if art == "Exact":
        return nw == kw
    if art == "Phrase":
        return any(kw[i:i + len(nw)] == nw for i in range(len(kw) - len(nw) + 1))
    return all(w in kw for w in nw)   # Broad


def main() -> int:
    aktive = []
    for pfad in sorted(glob.glob("data/keywords/*.csv")):
        for r in csv.DictReader(open(pfad, encoding="utf-8")):
            aktive.append((r["Campaign"].strip(), r["Ad Group"].strip(),
                           r["Keyword"].strip(), r["Criterion Type"].strip()))

    negative = []
    for pfad in sorted(glob.glob("data/negativlisten/*.csv")):
        for r in csv.DictReader(open(pfad, encoding="utf-8")):
            negative.append((r["Liste"].strip(), r["Keyword"].strip(),
                             r["Criterion Type"].strip()))

    treffer = []
    for liste, neg, art in negative:
        for kampagne, ag, kw, _ in aktive:
            if blockiert(neg, art, kw):
                treffer.append((liste, neg, art, ag, kw))

    print(f"Geprüft: {len(aktive)} aktive Keywords gegen {len(negative)} Ausschlüsse")
    print(f"= {len(aktive) * len(negative):,} Kombinationen\n".replace(",", "."))

    if treffer:
        print(f"KONFLIKTE ({len(treffer)}) — diese Ausschlüsse blockieren eigene Keywords:\n")
        for liste, neg, art, ag, kw in treffer:
            print(f"  ✗ [{liste}] {neg!r} ({art})")
            print(f"      blockiert  [{ag}]  {kw!r}")
        print("\n  Lösung: den Ausschluss enger fassen (Phrase statt Broad) oder entfernen.")
        return 1

    print("Keine Konflikte. Kein Ausschluss blockiert ein aktives Keyword.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
