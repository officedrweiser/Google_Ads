#!/usr/bin/env python3
"""
Erzeugt aus den Quelldateien die Importdateien für den Google Ads Editor.

Eingaben:
  data/keywords/*.csv              Keywords je Kampagne
  data/negativlisten/*.csv         Ausschluss-Keywords
  data/anzeigen/rsa-anzeigentexte.csv   Anzeigentexte (Langformat)

Ausgaben (Verzeichnis import/):
  import/keywords.csv              Alle Keywords in einer Datei
  import/negative-keywords.csv     Alle Ausschluesse in einer Datei
  import/anzeigen-rsa.csv          RSA im Breitformat (Anzeigentitel 1-15, Beschreibung 1-4)

Aufruf:  python3 tools/baue_editor_import.py
"""
import csv
import glob
import os
import signal
import sys
from collections import defaultdict

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

AUSGABE = "import"
BASIS_URL = "https://drweiser.at"

# Anzeigengruppe -> (Zielseite, Pfad 1, Pfad 2). Siehe docs/02-kontostruktur.md
ZIELSEITEN = {
    "Kanzleiname":                  ("/",                                     "Kanzlei",      ""),
    "Personenname":                 ("/kanzlei",                              "Kanzlei",      ""),
    "Scheidungsanwalt":             ("/scheidung",                            "Scheidung",    "Wien"),
    "Einvernehmliche Scheidung":    ("/scheidung/einvernehmlich",             "Scheidung",    "Wien"),
    "Strittige Scheidung":          ("/scheidung/strittig",                   "Scheidung",    "Wien"),
    "Unterhalt":                    ("/familienrecht/unterhalt",              "Familienrecht","Wien"),
    "Obsorge Kontaktrecht":         ("/familienrecht/obsorge",                "Familienrecht","Wien"),
    "Vermögensaufteilung":          ("/scheidung/vermoegensaufteilung",       "Scheidung",    "Wien"),
    "Ehevertrag":                   ("/familienrecht/ehevertrag",             "Familienrecht","Wien"),
    "Kosten Honorar":               ("/scheidung/kosten",                     "Scheidung",    "Kosten"),
    "Erbrecht Allgemein":           ("/erbrecht",                             "Erbrecht",     "Wien"),
    "Pflichtteil":                  ("/erbrecht/pflichtteil",                 "Erbrecht",     "Wien"),
    "Testament":                    ("/erbrecht/testament",                   "Erbrecht",     "Wien"),
    "Verlassenschaft":              ("/erbrecht/verlassenschaft",             "Erbrecht",     "Wien"),
    "Erbstreit":                    ("/erbrecht/erbstreit",                   "Erbrecht",     "Wien"),
    "Schenkung Übergabe":           ("/erbrecht/schenkung",                   "Erbrecht",     "Wien"),
    "Immobilienrecht":              ("/immobilienrecht",                      "Immobilien",   "Wien"),
    "Kaufvertrag":                  ("/immobilienrecht/kaufvertrag",          "Immobilien",   "Wien"),
    "Treuhand":                     ("/immobilienrecht/treuhand",             "Immobilien",   "Wien"),
    "Wohnungseigentum":             ("/immobilienrecht/wohnungseigentum",     "Immobilien",   "Wien"),
    "Bauträger Bauvertrag":         ("/immobilienrecht/bautraegervertrag",    "Immobilien",   "Wien"),
    "Grundbuch Dienstbarkeit":      ("/immobilienrecht/grundbuch",            "Immobilien",   "Wien"),
    "Gesellschaftsrecht Allgemein": ("/gesellschaftsrecht",                   "Gesellschaft", "Wien"),
    "GmbH FlexCo Gründung":         ("/gesellschaftsrecht/gruendung",         "Gesellschaft", "Wien"),
    "Gesellschafterverträge":       ("/gesellschaftsrecht/vertraege",         "Gesellschaft", "Wien"),
    "Anteilsabtretung M&A":         ("/gesellschaftsrecht/unternehmenskauf",  "Gesellschaft", "Wien"),
    "Gesellschafterstreit":         ("/gesellschaftsrecht/streit",            "Gesellschaft", "Wien"),
    "Privatstiftung":               ("/stiftungsrecht",                       "Stiftungsrecht", ""),
    "Stiftungsurkunden":            ("/stiftungsrecht/urkunden",              "Stiftungsrecht", ""),
    "Vermögensnachfolge":           ("/nachfolge",                            "Nachfolge",    ""),
}


def keywords_zusammenfuehren() -> int:
    zeilen = []
    for pfad in sorted(glob.glob("data/keywords/*.csv")):
        for r in csv.DictReader(open(pfad, encoding="utf-8")):
            ag = r["Ad Group"].strip()
            seite = ZIELSEITEN.get(ag, ("/", "", ""))[0]
            zeilen.append({
                "Campaign": r["Campaign"].strip(),
                "Ad Group": ag,
                "Keyword": r["Keyword"].strip(),
                "Criterion Type": r["Criterion Type"].strip(),
                "Max CPC": r["Max CPC"].strip(),
                "Final URL": BASIS_URL + seite,
                "Status": "Enabled",
            })
    ziel = os.path.join(AUSGABE, "keywords.csv")
    with open(ziel, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(zeilen[0].keys()))
        w.writeheader()
        w.writerows(zeilen)
    return len(zeilen)


def negative_zusammenfuehren() -> int:
    zeilen = []
    for pfad in sorted(glob.glob("data/negativlisten/*.csv")):
        for r in csv.DictReader(open(pfad, encoding="utf-8")):
            zeilen.append({
                "Campaign": "",  # leer = geteilte Liste auf Kontoebene
                "Negative Keyword List": r["Liste"].strip(),
                "Keyword": r["Keyword"].strip(),
                "Criterion Type": "Campaign Negative " + r["Criterion Type"].strip(),
            })
    ziel = os.path.join(AUSGABE, "negative-keywords.csv")
    with open(ziel, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(zeilen[0].keys()))
        w.writeheader()
        w.writerows(zeilen)
    return len(zeilen)


def anzeigen_breitformat() -> int:
    gruppen = defaultdict(lambda: {"Anzeigentitel": [], "Beschreibung": []})
    for r in csv.DictReader(open("data/anzeigen/rsa-anzeigentexte.csv", encoding="utf-8")):
        schluessel = (r["Campaign"].strip(), r["Ad Group"].strip())
        gruppen[schluessel][r["Typ"].strip()].append((r["Text"].strip(), r["Pin"].strip()))

    spalten = ["Campaign", "Ad Group", "Ad type", "Final URL", "Path 1", "Path 2"]
    spalten += [f"Headline {i}" for i in range(1, 16)]
    spalten += [f"Headline {i} position" for i in range(1, 16)]
    spalten += [f"Description {i}" for i in range(1, 5)]
    spalten += [f"Description {i} position" for i in range(1, 5)]
    spalten += ["Status"]

    zeilen = []
    for (kampagne, ag), assets in sorted(gruppen.items()):
        seite, p1, p2 = ZIELSEITEN.get(ag, ("/", "", ""))
        zeile = {s: "" for s in spalten}
        zeile.update({
            "Campaign": kampagne, "Ad Group": ag,
            "Ad type": "Responsive search ad",
            "Final URL": BASIS_URL + seite, "Path 1": p1, "Path 2": p2,
            "Status": "Enabled",
        })
        for i, (text, pin) in enumerate(assets["Anzeigentitel"][:15], start=1):
            zeile[f"Headline {i}"] = text
            if pin == "1":
                zeile[f"Headline {i} position"] = "1"
        for i, (text, pin) in enumerate(assets["Beschreibung"][:4], start=1):
            zeile[f"Description {i}"] = text
            if pin == "1":
                zeile[f"Description {i} position"] = "1"
        zeilen.append(zeile)

    ziel = os.path.join(AUSGABE, "anzeigen-rsa.csv")
    with open(ziel, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=spalten)
        w.writeheader()
        w.writerows(zeilen)
    return len(zeilen)


def main() -> int:
    os.makedirs(AUSGABE, exist_ok=True)
    n_kw = keywords_zusammenfuehren()
    n_neg = negative_zusammenfuehren()
    n_ads = anzeigen_breitformat()

    kw_gruppen = {r["Ad Group"].strip() for p in glob.glob("data/keywords/*.csv")
                  for r in csv.DictReader(open(p, encoding="utf-8"))}
    ad_gruppen = {r["Ad Group"].strip()
                  for r in csv.DictReader(open("data/anzeigen/rsa-anzeigentexte.csv",
                                               encoding="utf-8"))}
    fehlend = sorted(kw_gruppen - set(ZIELSEITEN))
    ohne_anzeige = sorted(kw_gruppen - ad_gruppen)
    ohne_keyword = sorted(ad_gruppen - kw_gruppen)

    print(f"import/keywords.csv           {n_kw:>3} Keywords")
    print(f"import/negative-keywords.csv  {n_neg:>3} Ausschlüsse")
    print(f"import/anzeigen-rsa.csv       {n_ads:>3} Anzeigen (je eine RSA pro Anzeigengruppe)")
    probleme = False
    if fehlend:
        print("\nWARNUNG – Anzeigengruppen ohne hinterlegte Zielseite:")
        for ag in fehlend:
            print("  !", ag)
        probleme = True
    if ohne_anzeige:
        print("\nWARNUNG – Anzeigengruppen mit Keywords, aber ohne Anzeigentexte:")
        for ag in ohne_anzeige:
            print("  !", ag, "– würde live gehen, ohne dass eine Anzeige ausgeliefert wird")
        probleme = True
    if ohne_keyword:
        print("\nWARNUNG – Anzeigentexte ohne zugehörige Keywords:")
        for ag in ohne_keyword:
            print("  !", ag, "– die Anzeige würde nie ausgeliefert")
        probleme = True
    if probleme:
        return 1
    print(f"\nAlle {len(kw_gruppen)} Anzeigengruppen haben Keywords, Anzeigentexte "
          f"und eine Zielseite. Dateien liegen in import/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
