# 03 – Keywords & Negativlisten

## 3.1 Umfang

| | Anzahl | Datei |
|---|---|---|
| Aktive Keywords | 212 | `data/keywords/*.csv` |
| Ausschluss-Keywords | 192 | `data/negativlisten/*.csv` |
| Anzeigengruppen | 30 | |

Alle Listen sind dublettenfrei geprüft und liegen in einem Format vor, das sich mit dem
Google Ads Editor per Kopieren/Einfügen übernehmen lässt.

## 3.2 Match-Type-Strategie

| Phase | Zulässige Optionen | Begründung |
|---|---|---|
| Phase 1 (Monat 1–3) | **Exact + Phrase** | Kontrolle über die Suchbegriffe; Datenbasis für die Negativliste aufbauen |
| Phase 2 (ab Monat 4) | Exact + Phrase, DSA ergänzend | DSA findet Suchbegriffe, an die niemand denkt |
| Phase 3 (ab Monat 7) | zusätzlich Broad in **separater** Kampagne | Nur mit Ziel-CPA und ausgereifter Negativliste |

**Warum kein Broad Match zum Start:** Google matcht seit den Änderungen der letzten Jahre
auch Phrase und Exact deutlich loser als früher – Broad Match würde bei Anwalts-Keywords
in Themen streuen, die mit dem Mandat nichts zu tun haben, und das gesamte Tagesbudget
in wenigen Stunden verbrauchen. Broad Match ist ein Werkzeug für Konten mit vielen
Conversions pro Woche, nicht für den Start.

**Konsequenz aus dem lockeren Matching:** Der Suchbegriffbericht muss in Phase 1
**wöchentlich** durchgesehen werden. Das ist kein optionaler Feinschliff, sondern die
Hauptarbeit der ersten acht Wochen.

## 3.3 Gebotsstruktur der Keywords

Die `Max CPC`-Werte in den CSV-Dateien gelten für **Phase 1** (Klicks maximieren mit
CPC-Limit). Sie sind nach Mandatswert gestaffelt:

| Keyword-Typ | Max. CPC | Beispiel |
|---|---|---|
| Marke | 1,00–1,50 € | „dr weiser rechtsanwalt" |
| Nische mit wenig Wettbewerb | 2,50–3,00 € | „flexco gründen anwalt", „stiftungszusatzurkunde" |
| Fachbegriff mit klarer Absicht | 3,00–4,50 € | „pflichtteil einklagen", „treuhänder anwalt wien" |
| Hart umkämpft, hoher Mandatswert | 5,00–6,50 € | „scheidungsanwalt wien", „unternehmenskauf anwalt wien" |
| Kostenrecherche | 3,00–3,50 € | „was kostet eine scheidung in wien" |

Ab Phase 2 werden diese Werte durch die automatische Gebotsstrategie ersetzt und dienen
nur noch als Referenz.

## 3.4 Die sieben Negativlisten

Alle sieben werden auf **Kontoebene** als geteilte Listen angelegt und dann den
Kampagnen zugewiesen. Vorteil: Eine Änderung wirkt sofort in allen Kampagnen.

| Liste | Einträge | Zweck |
|---|---|---|
| `L1` Jobs & Ausbildung | 27 | Bewerber, Studierende, Referatssucher |
| `L2` Gratis & DIY | 31 | Wer „gratis" oder „Muster" sucht, beauftragt keine Kanzlei |
| `L3` Information & Recherche | 23 | Wissensfragen ohne Mandatsabsicht |
| `L4` Deutsche Rechtsbegriffe | 21 | Erkennt deutschen Traffic zuverlässiger als Geo-Targeting |
| `L5` Fremde Rechtsgebiete | 35 | Strafrecht, Asyl, Arbeitsrecht, Markenrecht usw. |
| `L6` Portale & Vermittler | 24 | Anwaltsverzeichnisse, Kammern, Rechtsschutzversicherer |
| `L7` Standorte außerhalb | 31 | Graz, Linz, München, Zürich … |

### Zuweisung je Kampagne

| Kampagne | L1 | L2 | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|---|
| BRAND | ✓ | | | | ✓ | | |
| Scheidung + Familie | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Erbrecht | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Immobilien + Treuhand | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gesellschaftsrecht | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Stiftung + Nachfolge | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | |

Bei der Brand-Kampagne bewusst nur L1 und L5: Wer den Kanzleinamen sucht, soll die Anzeige
sehen – auch aus Graz, auch mit dem Wort „kosten".

### Drei Listen, die besondere Aufmerksamkeit verdienen

**L4 – Deutsche Rechtsbegriffe.** Der wirksamste Geo-Filter ist nicht die
Standortausrichtung, sondern die Sprache. Wer „Erbschein" sucht, sitzt in Deutschland –
in Österreich heißt das Dokument Einantwortungsbeschluss. Dasselbe gilt für
„Nachlassgericht", „Amtsgericht", „Handelsregister", „Zugewinnausgleich",
„Trennungsjahr" und „Düsseldorfer Tabelle". Diese Liste fängt Traffic ab, den die
Standorteinstellung durchlässt.

**L5 – Fremde Rechtsgebiete: drei Einträge zum Prüfen.**
- `arbeitsrecht` – auf der Website nicht als Schwerpunkt ausgewiesen. Falls Sie
  Arbeitsrecht doch bearbeiten, muss der Eintrag entfernt und eine eigene
  Anzeigengruppe ergänzt werden.
- `notar` – notarielle Leistungen sind keine Anwaltsleistungen. Bei Immobilien- und
  Gesellschaftsrecht suchen viele Menschen „Notar", meinen aber die Vertragserrichtung,
  die auch ein Rechtsanwalt vornimmt. Hier ist ein Test sinnvoll: einige Wochen ohne
  Ausschluss laufen lassen und die Anfragequalität beobachten.
- `steuerberater` / `buchhaltung` – klare Abgrenzung, kann ausgeschlossen bleiben.

**L6 – `rechtsschutzversicherung`.** Zweischneidig: Ein Teil dieser Suchen sind
Deckungsanfragen von Menschen, die tatsächlich ein Mandat erteilen wollen und wissen,
dass die Versicherung zahlt. Empfehlung: zunächst **nicht** ausschließen, sondern über
den Suchbegriffbericht beobachten und erst bei schlechter Anfragequalität ergänzen.

## 3.5 Die Sonderrolle der „Kosten"-Keywords

Standard-Vorgehen wäre, `kosten`, `preis`, `honorar` und `was kostet` pauschal
auszuschließen. Dieser Plan tut das bewusst **nicht**.

Begründung: Bei einer Scheidung ist die Kostenfrage keine Ausrede, sondern die zentrale
offene Frage vor der Beauftragung. Wer „was kostet eine scheidung in wien" tippt, hat die
Entscheidung meist bereits getroffen und sucht Planungssicherheit. Diese Suchanfragen
abzuschneiden verschenkt Mandate an die Kanzlei, die eine ehrliche Antwort auf der
Website hat.

Umsetzung:
1. Eigene Anzeigengruppe `Kosten Honorar` in der Scheidungskampagne
2. Niedrigeres Gebot (3,00–3,50 € statt 5,50–6,50 €)
3. Eigene Landingpage `/scheidung/kosten` mit tatsächlicher Aufschlüsselung
   (Gerichtsgebühren, Honorar, Kostentragung) – siehe Doc 05
4. Ausgeschlossen wird nur die Kombination mit `gratis`, `kostenlos`, `ohne anwalt`
   (bereits über L2 abgedeckt)

Kontrolle nach 60 Tagen: Liegt der CPA dieser Anzeigengruppe über dem Kampagnendurchschnitt,
wird sie pausiert. Das ist ein messbarer Test, keine Glaubensfrage.

## 3.6 Keywords auf Wettbewerber – Empfehlung: nein

Technisch wäre es möglich, auf die Namen anderer Wiener Kanzleien zu bieten. Davon ist
abzuraten:

- **Standesrechtlich riskant.** § 47 Abs 3 lit b RL-BA 2015 untersagt vergleichende
  Werbung gegen Berufskollegen. Auch wenn die Anzeige selbst keinen Vergleich enthält,
  ist das Gebot auf einen Kollegennamen eine Auseinandersetzung, die man nicht braucht.
- **Wirtschaftlich schwach.** Wer einen bestimmten Anwalt namentlich sucht, ist meist
  bereits empfohlen worden. Die Wechselquote ist niedrig, der Klickpreis hoch.
- **Reziprozitätsrisiko.** Wer damit anfängt, provoziert Gebote auf den eigenen Namen.

Umgekehrt gilt: Die eigene Brand-Kampagne ist genau deshalb sinnvoll – sie ist die
Verteidigung, nicht der Angriff.

## 3.7 Pflege-Routine

| Rhythmus | Aufgabe |
|---|---|
| Wöchentlich (Monat 1–3) | Suchbegriffbericht der letzten 7 Tage; jeden irrelevanten Begriff sofort ausschließen; gute Begriffe mit Volumen als Exact-Keyword aufnehmen |
| Zweiwöchentlich (ab Monat 4) | dasselbe, geringere Frequenz |
| Monatlich | Keywords mit 0 Impressionen über 60 Tage pausieren; Keywords mit hohem Verbrauch und 0 Conversions prüfen |
| Quartalsweise | Negativlisten gegen neue Rechtsgebiete und Standorte durchsehen; auf zu breite Ausschlüsse prüfen (häufigster Fehler nach 12 Monaten) |

> **Achtung bei Broad-Match-Ausschlüssen:** Ein Ausschluss wie `kosten` (Broad) blockiert
> auch „scheidungskosten anwalt wien". Ausschlüsse deshalb so eng wie möglich formulieren –
> im Zweifel als Phrase, nicht als Broad.
