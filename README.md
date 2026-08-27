# Google Ads – Kampagnenstrategie Kanzlei Dr. Martin Weiser

Vollständiger Kampagnen- und Strategieplan für die Mandantengewinnung über Google Ads.

**Zusammenfassung als Webseite:** https://claude.ai/code/artifact/cd600dc4-8620-4630-94dc-a24bd5488aea

**Kanzlei:** Dr. Martin Weiser, Rechtsanwalt
**Standort:** Landstraßer Hauptstraße 60, Eingang Rochusgasse 2, 1030 Wien (U3 Rochusgasse)
**Bestehend seit:** 1990
**Schwerpunkte:** Scheidungs- & Familienrecht · Erbrecht · Liegenschafts- & Immobilienrecht ·
Vertragsrecht · Gesellschafts- & Unternehmensrecht · Stiftungsrecht · Treuhandschaft · Mediation

---

## Leseanleitung – in dieser Reihenfolge

| # | Dokument | Wofür |
|---|---|---|
| 01 | [Strategie & Wirtschaftlichkeit](docs/01-strategie.md) | Warum welches Rechtsgebiet, welches Budget, welche Ziele |
| 02 | [Kontostruktur](docs/02-kontostruktur.md) | Kampagnen, Anzeigengruppen, Ausrichtung, Namenskonvention |
| 03 | [Keywords & Negativlisten](docs/03-keywords-und-negativlisten.md) | Was gebucht wird – und was Geld verbrennt |
| 04 | [Anzeigentexte & Assets](docs/04-anzeigentexte-und-assets.md) | Fertige RSA-Texte, Sitelinks, Snippets |
| 05 | [Landingpages](docs/05-landingpages.md) | Was auf der Website passieren muss |
| 06 | [Conversion-Tracking & DSGVO](docs/06-conversion-tracking-und-dsgvo.md) | Messung, Consent Mode v2, Verschwiegenheit |
| 07 | [Gebote, Budget & Steuerung](docs/07-gebote-budget-steuerung.md) | Gebotsstrategie-Fahrplan, Budgetsplit |
| 08 | [Standesrecht-Compliance](docs/08-compliance-rl-ba.md) | RL-BA 2015 – was in Anzeigen erlaubt ist und was nicht |
| 09 | [Betrieb, KPI & Reporting](docs/09-betrieb-kpi-reporting.md) | Wochen-/Monatsroutine, Kennzahlen |
| 10 | [90-Tage-Fahrplan](docs/10-90-tage-fahrplan.md) | Konkrete Umsetzungsschritte mit Terminen |
| 11 | [Claude-Skills für dieses Projekt](docs/11-claude-skills.md) | Antwort auf: „Welche Skills helfen uns dabei?" |
| 12 | [Telefonische Erreichbarkeit](docs/12-telefonische-erreichbarkeit.md) | Werbezeitplan, Anruf-Asset, Rückrufweg, Annahmedienst |

## Daten und Werkzeuge

### Quelldateien (gepflegt wird hier)

```
data/keywords/          206 Keywords in 6 Dateien, nach Kampagne getrennt
data/negativlisten/     217 Ausschluss-Keywords in 7 wiederverwendbaren Listen
data/anzeigen/          449 Anzeigen-Assets + Anzeigenerweiterungen
data/erreichbarkeit/    Bürozeiten und Nachfrageverteilung (Eingabedateien)
```

### Werkzeuge

```bash
python3 tools/pruefe_anzeigen.py       # Zeichengrenzen, Duplikate, Standesrecht-Wortfilter
python3 tools/pruefe_negativlisten.py  # blockiert ein Ausschluss eigene Keywords?
python3 tools/baue_editor_import.py    # Keywords, Ausschlüsse und Anzeigen
python3 tools/baue_werbezeitplan.py    # Werbezeitplan aus den Bürozeiten
```

`pruefe_anzeigen.py` liefert Exit-Code 1 bei Fehlern und sollte nach jeder Textänderung laufen.
Aktueller Stand: **449 Assets, 30 Anzeigengruppen, 0 Beanstandungen.**

### Importdateien für den Google Ads Editor

```
import/keywords.csv           206 Keywords mit Zielseite und Gebot
import/negative-keywords.csv  217 Ausschlüsse, den 7 Listen zugeordnet
import/anzeigen-rsa.csv       30 Responsive Suchanzeigen im Breitformat
import/werbezeitplan.csv      Zeitblöcke mit Gebotsanpassung nach Erreichbarkeit
import/anruf-asset-zeitplan.csv  Einblendezeiten der Rufnummer
```

Diese drei Dateien werden erzeugt, nicht von Hand bearbeitet. Änderungen gehören in
`data/`, danach `tools/baue_editor_import.py` erneut ausführen.

## Vor dem Start prüfen

- [ ] Google-Ads-Konto: EU-Werbetreibenden-Verifizierung abgeschlossen (sonst pausieren die Anzeigen)
- [ ] Google Business Profile für 1030 Wien angelegt und verifiziert
- [ ] Consent-Management-Plattform mit Consent Mode v2 auf drweiser.at aktiv
- [x] Rechtsgebiete-Freigabe erteilt (27. 08. 2026): kein Mietrecht, kein Arbeitsrecht
- [x] Bürozeiten eingetragen: Mo–Do 09:00–17:00, Fr 09:00–13:00, durchgehend besetzt (Doc 12)

## Wichtiger Hinweis zu den Zahlen

Alle CPC-, Conversion-Rate- und CPA-Werte in diesen Dokumenten sind **Planungsannahmen**,
abgeleitet aus Branchen-Benchmarks für Rechtsdienstleistungen im DACH-Raum. Sie dienen der
Budgetplanung und der Priorisierung. Nach 60–90 Tagen Laufzeit werden sie durch die echten
Kontodaten ersetzt – erst dann sind belastbare Aussagen zur Wirtschaftlichkeit je Rechtsgebiet
möglich.
