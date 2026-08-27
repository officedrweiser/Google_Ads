#!/usr/bin/env python3
"""
Prüft die Anzeigentexte in data/anzeigen/rsa-anzeigentexte.csv auf:

  1. Google-Ads-Zeichengrenzen (Anzeigentitel 30, Beschreibung 90)
  2. Mindest-/Empfehlungsanzahl der Assets je Anzeigengruppe
  3. Duplikate innerhalb einer Anzeigengruppe
  4. Google-Ads-Formatregeln (Ausrufezeichen im Anzeigentitel, Großbuchstaben-Blöcke)
  5. Standesrechtlich heikle Formulierungen nach RL-BA 2015 § 47 Abs 3

Aufruf:  python3 tools/pruefe_anzeigen.py
Exit-Code 1, wenn harte Fehler gefunden wurden.
"""
import csv
import re
import signal
import sys
from collections import defaultdict

# Abbruch ohne Fehlermeldung, wenn die Ausgabe z. B. nach "| head" umgeleitet wird
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

DATEI = "data/anzeigen/rsa-anzeigentexte.csv"

GRENZEN = {"Anzeigentitel": 30, "Beschreibung": 90}
EMPFOHLEN_MIN = {"Anzeigentitel": 8, "Beschreibung": 3}
GOOGLE_MIN = {"Anzeigentitel": 3, "Beschreibung": 2}
GOOGLE_MAX = {"Anzeigentitel": 15, "Beschreibung": 4}

# RL-BA 2015 § 47 Abs 3 – unzulässige Werbung, plus UWG-Irreführungsrisiko
VERBOTEN = [
    (r"\bbeste[rsn]?\b",            "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\bnr\.?\s*1\b",              "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\bnummer\s*eins\b",          "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\bführend",                  "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\btop[- ]?kanzlei\b",        "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\bmarktführer",              "Superlativ – marktschreierisch (§ 47 Abs 3 lit a)"),
    (r"\bbesser als\b",             "Vergleichende Werbung (§ 47 Abs 3 lit b)"),
    (r"\bgünstiger als\b",          "Vergleichende Werbung (§ 47 Abs 3 lit b)"),
    (r"\berfolgsquote\b",           "Erfolgsangabe (§ 47 Abs 3 lit g)"),
    (r"\berfolgsrate\b",            "Erfolgsangabe (§ 47 Abs 3 lit g)"),
    (r"\d+\s*%\s*erfolg",           "Erfolgsangabe (§ 47 Abs 3 lit g)"),
    (r"\bgewonnene?n?\s+(verfahren|prozesse|fälle)", "Erfolgsangabe (§ 47 Abs 3 lit g)"),
    (r"\b\d+\+?\s*(mandate|mandanten|fälle)\b", "Erfolgs-/Umsatzzahl (§ 47 Abs 3 lit g)"),
    (r"\bgarantiert",               "Erfolgsversprechen – irreführend (UWG)"),
    (r"\bgarantie\b",               "Erfolgsversprechen – irreführend (UWG)"),
    (r"\b100\s*%\s*sicher",         "Erfolgsversprechen – irreführend (UWG)"),
    (r"\bnur bei erfolg\b",         "Quota-litis-Verbot (§ 879 Abs 2 Z 2 ABGB)"),
    (r"\bkein erfolg,? keine kosten", "Quota-litis-Verbot (§ 879 Abs 2 Z 2 ABGB)"),
    (r"\bfachanwalt\b",             "Fachanwaltstitel existiert in Österreich nicht – irreführend"),
    (r"\bspezialist\b",             "Suggeriert formale Qualifikation – besser 'Schwerpunkt'"),
    (r"\bexperte\b",                "Suggeriert formale Qualifikation – besser 'Schwerpunkt'"),
    (r"\bbillig",                   "Preisanpreisung – Ansehen des Standes (§ 47 Abs 3 lit a)"),
    (r"\bschnäppchen\b",            "Preisanpreisung – Ansehen des Standes (§ 47 Abs 3 lit a)"),
]

def main() -> int:
    zeilen = list(csv.DictReader(open(DATEI, encoding="utf-8")))
    gruppen = defaultdict(lambda: defaultdict(list))
    fehler, warnungen = [], []

    for i, r in enumerate(zeilen, start=2):
        ag = (r["Campaign"].strip(), r["Ad Group"].strip())
        typ = r["Typ"].strip()
        txt = r["Text"].strip()
        gruppen[ag][typ].append(txt)

        # 1) Zeichengrenzen
        grenze = GRENZEN.get(typ)
        if grenze and len(txt) > grenze:
            fehler.append(f"Z{i:>3} [{ag[1]}] {typ} {len(txt)}/{grenze} Zeichen: {txt!r}")

        # 4) Google-Formatregeln
        if typ == "Anzeigentitel" and "!" in txt:
            fehler.append(f"Z{i:>3} [{ag[1]}] Ausrufezeichen im Anzeigentitel nicht erlaubt: {txt!r}")
        if txt.count("!") > 1:
            fehler.append(f"Z{i:>3} [{ag[1]}] Mehr als ein Ausrufezeichen: {txt!r}")
        for wort in re.findall(r"\b[A-ZÄÖÜ]{4,}\b", txt):
            if wort not in {"BTVG", "GMBH", "FLEXCO"}:
                warnungen.append(f"Z{i:>3} [{ag[1]}] Großbuchstaben-Block {wort!r} in: {txt!r}")

        # 5) Standesrecht
        low = txt.lower()
        for muster, grund in VERBOTEN:
            if re.search(muster, low):
                fehler.append(f"Z{i:>3} [{ag[1]}] STANDESRECHT – {grund}: {txt!r}")

    # 2) + 3) je Anzeigengruppe
    for ag, assets in sorted(gruppen.items()):
        for typ in ("Anzeigentitel", "Beschreibung"):
            texte = assets.get(typ, [])
            n = len(texte)
            if n < GOOGLE_MIN[typ]:
                fehler.append(f"[{ag[1]}] nur {n} {typ} – Google verlangt mindestens {GOOGLE_MIN[typ]}")
            if n > GOOGLE_MAX[typ]:
                fehler.append(f"[{ag[1]}] {n} {typ} – Google erlaubt höchstens {GOOGLE_MAX[typ]}")
            if GOOGLE_MIN[typ] <= n < EMPFOHLEN_MIN[typ]:
                warnungen.append(f"[{ag[1]}] nur {n} {typ} – empfohlen sind {EMPFOHLEN_MIN[typ]}+")
            doppelt = {t for t in texte if texte.count(t) > 1}
            for t in sorted(doppelt):
                fehler.append(f"[{ag[1]}] {typ} doppelt vorhanden: {t!r}")

    # Ausgabe
    print(f"Geprüft: {len(zeilen)} Assets in {len(gruppen)} Anzeigengruppen\n")
    if fehler:
        print(f"FEHLER ({len(fehler)}):")
        for f in fehler:
            print("  ✗", f)
        print()
    if warnungen:
        print(f"HINWEISE ({len(warnungen)}):")
        for w in warnungen:
            print("  !", w)
        print()
    if not fehler and not warnungen:
        print("Alles in Ordnung – keine Fehler, keine Hinweise.")
    elif not fehler:
        print("Keine Fehler. Nur Hinweise (siehe oben).")

    # Statistik
    print("\nAssets je Anzeigengruppe:")
    for ag, assets in sorted(gruppen.items()):
        h = len(assets.get("Anzeigentitel", []))
        b = len(assets.get("Beschreibung", []))
        print(f"  {ag[1]:<32} {h:>2} Anzeigentitel, {b} Beschreibungen")

    return 1 if fehler else 0

if __name__ == "__main__":
    sys.exit(main())
