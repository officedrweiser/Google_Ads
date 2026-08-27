#!/usr/bin/env python3
"""
Erzeugt aus den Kanzlei-Bürozeiten den Google-Ads-Werbezeitplan und den Zeitplan
für das Anruf-Asset - und rechnet aus, wie viel Suchnachfrage in Stunden fällt,
in denen niemand ans Telefon geht.

Eingaben:
  data/erreichbarkeit/buerozeiten.csv        Bürozeiten (bitte anpassen)
  data/erreichbarkeit/nachfrage-annahme.csv  Nachfrageverteilung nach Stunde
  data/erreichbarkeit/nachfrage-ist.csv      OPTIONAL - echter Google-Ads-Export,
                                             hat Vorrang vor der Annahme

Ausgaben:
  import/werbezeitplan.csv        Werbezeitplan mit Gebotsanpassungen (Phase 1)
  import/anruf-asset-zeitplan.csv Einblendezeiten für das Anruf-Asset

Aufruf:  python3 tools/baue_werbezeitplan.py
"""
import csv
import os
import signal
import sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

TAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
EN = {"Montag": "Monday", "Dienstag": "Tuesday", "Mittwoch": "Wednesday",
      "Donnerstag": "Thursday", "Freitag": "Friday", "Samstag": "Saturday",
      "Sonntag": "Sunday"}

# Gebotsanpassung nach Erreichbarkeit und Nachfrage. Wirkt nur in Phase 1
# (Klicks maximieren / manuelles CPC); ab Smart Bidding ignoriert Google sie.
AUF_TELEFON_HOCH = 15      # Telefon besetzt, starke Nachfrage
AUF_TELEFON = 10           # Telefon besetzt
AB_NUR_FORMULAR = -25      # niemand am Telefon, Formular läuft weiter
AUS_SCHWELLE = 2           # Nachfrage <= diesem Wert und kein Telefon -> Anzeigen aus


def lies_buerozeiten(pfad):
    zeiten = {}
    with open(pfad, encoding="utf-8") as f:
        zeilen = [z for z in f if not z.lstrip().startswith("#")]
    for r in csv.DictReader(zeilen):
        tag = r["Wochentag"].strip()
        if tag not in TAGE:
            continue
        def hh(v):
            v = (v or "").strip()
            return int(v.split(":")[0]) if v else None
        zeiten[tag] = {
            "von": hh(r["Von"]), "bis": hh(r["Bis"]),
            "pause_von": hh(r["Pause von"]), "pause_bis": hh(r["Pause bis"]),
            "telefon": (r["Telefon besetzt"] or "").strip().lower() == "ja",
            "status": (r.get("Status") or "").strip(),
        }
    return zeiten


def lies_nachfrage():
    pfad_ist = "data/erreichbarkeit/nachfrage-ist.csv"
    pfad = pfad_ist if os.path.exists(pfad_ist) else "data/erreichbarkeit/nachfrage-annahme.csv"
    with open(pfad, encoding="utf-8") as f:
        zeilen = [z for z in f if not z.lstrip().startswith("#")]
    daten = {}
    for r in csv.DictReader(zeilen):
        tag = r["Wochentag"].strip()
        if tag in TAGE:
            daten[tag] = [float(r[str(h)]) for h in range(24)]
    return daten, pfad


def telefon_besetzt(cfg, stunde):
    """Ist in dieser Stunde jemand am Telefon?"""
    if not cfg["telefon"] or cfg["von"] is None or cfg["bis"] is None:
        return False
    if not (cfg["von"] <= stunde < cfg["bis"]):
        return False
    pv, pb = cfg["pause_von"], cfg["pause_bis"]
    if pv is not None and pb is not None and pv <= stunde < pb:
        return False
    return True


def main() -> int:
    zeiten = lies_buerozeiten("data/erreichbarkeit/buerozeiten.csv")
    nachfrage, quelle = lies_nachfrage()
    os.makedirs("import", exist_ok=True)

    fehlend = [t for t in TAGE if t not in zeiten]
    if fehlend:
        print("FEHLER - Wochentage fehlen in buerozeiten.csv:", ", ".join(fehlend))
        return 1

    plan, anruf = [], []
    summe = erreicht = verloren_hoch = 0.0
    luecken = []

    for tag in TAGE:
        cfg = zeiten[tag]
        blockstart = None
        blockart = None

        def block_schliessen(ende):
            nonlocal blockstart, blockart
            if blockstart is None:
                return
            art, auf = blockart
            plan.append({
                "Campaign": "ALLE",
                "Day of week": EN[tag],
                "Start time": f"{blockstart:02d}:00",
                "End time": f"{ende:02d}:00" if ende < 24 else "24:00",
                "Bid adjustment": f"{auf:+d}%" if auf else "0%",
                "Erreichbarkeit": art,
            })
            if art == "Telefon besetzt":
                anruf.append({
                    "Asset": "Anruf-Asset +43 1 205 1003",
                    "Day of week": EN[tag],
                    "Start time": f"{blockstart:02d}:00",
                    "End time": f"{ende:02d}:00" if ende < 24 else "24:00",
                })
            blockstart, blockart = None, None

        for h in range(24):
            n = nachfrage[tag][h]
            summe += n
            tel = telefon_besetzt(cfg, h)
            if tel:
                erreicht += n
                art = "Telefon besetzt"
                auf = AUF_TELEFON_HOCH if n >= 8 else AUF_TELEFON
            elif n <= AUS_SCHWELLE:
                art = "Anzeigen aus"
                auf = None
            else:
                art = "Nur Formular"
                auf = AB_NUR_FORMULAR
                if n >= 7:
                    verloren_hoch += n
                    luecken.append((tag, h, n))

            if art == "Anzeigen aus":
                block_schliessen(h)
                continue
            if blockart != (art, auf):
                block_schliessen(h)
                blockstart, blockart = h, (art, auf)
        block_schliessen(24)

    with open("import/werbezeitplan.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(plan[0].keys()))
        w.writeheader(); w.writerows(plan)
    with open("import/anruf-asset-zeitplan.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(anruf[0].keys()))
        w.writeheader(); w.writerows(anruf)

    # --- Bericht ---
    annahme = any(z["status"].upper() == "ANNAHME" for z in zeiten.values())
    print("Grundlage Bürozeiten :", "ANNAHME - bitte in buerozeiten.csv anpassen" if annahme else "Kanzleiangabe")
    print("Grundlage Nachfrage  :", quelle)
    print()
    print(f"Telefonische Abdeckung der Suchnachfrage : {erreicht/summe*100:4.1f} %")
    print(f"Nachfrage ohne Telefonbesetzung          : {(summe-erreicht)/summe*100:4.1f} %")
    print(f"davon in Stunden mit starker Nachfrage   : {verloren_hoch/summe*100:4.1f} %")
    print()
    print(f"import/werbezeitplan.csv        {len(plan):>3} Zeitblöcke")
    print(f"import/anruf-asset-zeitplan.csv {len(anruf):>3} Blöcke mit eingeblendeter Rufnummer")

    if luecken:
        print("\nStunden mit starker Nachfrage, in denen niemand ans Telefon geht:")
        for tag, h, n in luecken:
            print(f"  {tag:<11} {h:02d}:00-{h+1:02d}:00   Nachfrage {n:.0f}/10")
        print("\n  -> Diese Stunden sind die Kandidaten für einen Telefonannahmedienst")
        print("     oder für einen prominenten Rückrufwunsch auf der Landingpage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
