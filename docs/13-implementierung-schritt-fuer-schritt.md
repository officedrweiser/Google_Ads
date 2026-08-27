# 13 – Implementierung Schritt für Schritt

> **Hinweis zu den Klickpfaden:** Die Pfade beziehen sich auf die Google-Ads-Oberfläche im
> August 2026. Google benennt Menüpunkte gelegentlich um. Wenn ein Pfad nicht stimmt, hilft
> die Suchleiste oben im Konto – dort den fettgedruckten Begriff eingeben.

**Zeitbedarf gesamt: 6–9 Stunden**, sinnvoll auf drei bis vier Sitzungen verteilt.
Die Reihenfolge ist nicht beliebig – Teil A und H müssen vor dem Start abgeschlossen sein.

| Teil | Inhalt | Dauer |
|---|---|---|
| [A](#teil-a) | Bestandsaufnahme des laufenden Kontos | 45 Min |
| [B](#teil-b) | Google Ads Editor einrichten | 20 Min |
| [C](#teil-c) | Ausschlusslisten anlegen | 40 Min |
| [D](#teil-d) | Kampagnen anlegen | 60 Min |
| [E](#teil-e) | Keywords und Anzeigen importieren | 45 Min |
| [F](#teil-f) | Assets und Erweiterungen | 40 Min |
| [G](#teil-g) | Werbezeitplan und Anruf-Asset | 30 Min |
| [H](#teil-h) | Conversion-Tracking prüfen | 60 Min |
| [I](#teil-i) | Testlauf und Start | 45 Min |
| [J](#teil-j) | Die erste Woche | laufend |

---

## Teil A – Bestandsaufnahme des laufenden Kontos {#teil-a}

Da bereits Anzeigen laufen, ist dies **kein Neuaufbau, sondern eine Umstellung**. Der
wichtigste Grundsatz dabei:

> **Niemals zwei Kampagnen desselben Kontos auf dieselben Keywords bieten.**
> Google liefert pro Suchanfrage nur eine Anzeige je Werbetreibendem aus – die mit dem
> höheren Anzeigenrang. Die zweite Kampagne bekommt dann keinen Traffic, aber die
> Auswertung wird unbrauchbar, weil sich die Daten auf zwei Kampagnen verteilen.

### A1 – Was im Konto vorhanden ist, festhalten

**Kampagnen → Kampagnen**, Zeitraum oben rechts auf **Letzte 90 Tage**.

Notieren Sie je bestehender Kampagne:

| Was | Warum |
|---|---|
| Name und Typ (Suche / Display / Performance Max) | PMax und Suche konkurrieren um dieselben Anfragen |
| Status (aktiv / pausiert) | |
| Tagesbudget | Summe muss zum Gesamtbudget passen |
| Gebotsstrategie | Bestimmt die Startstufe der neuen Kampagnen (Doc 07) |
| Kosten, Klicks, Conversions, Kosten/Conv. | Die Vergleichsgrundlage |
| Welche Rechtsgebiete abgedeckt sind | Überschneidung mit dem neuen Aufbau |

### A2 – Conversion-Aktionen prüfen

**Zielvorhaben → Conversions → Zusammenfassung**

Drei Fragen entscheiden über alles Weitere:

1. **Gibt es überhaupt Conversion-Aktionen?**
   Wenn nein: Die bisherigen Daten sagen nichts über Anfragen aus, nur über Klicks. Dann
   ist der neue Aufbau eine echte Neuaufsetzung, und die alten Kampagnen können ohne
   Verlust pausiert werden.
2. **Welche sind als „Primär" markiert?**
   Nur primäre Conversions fließen in die Gebotsoptimierung. Steht dort ein Seitenaufruf
   oder ein E-Mail-Klick, optimiert Google seit Monaten auf das Falsche.
3. **Wie viele Conversions in den letzten 30 Tagen?**
   Das entscheidet, mit welcher Gebotsstrategie die neuen Kampagnen starten dürfen:

   | Conversions / 30 Tage | Startstufe |
   |---|---|
   | 0–14 | Klicks maximieren mit CPC-Limit |
   | 15–29 | Conversions maximieren |
   | ab 30 | Ziel-CPA möglich |

   **Das ist der größte Vorteil eines laufenden Kontos:** Bei ausreichender
   Conversion-Historie überspringen die neuen Kampagnen die Lernphase teilweise, weil
   Google auf Kontoebene bereits gelernt hat.

### A3 – Bestehende Ausschlusslisten sichern

**Tools → Gemeinsam genutzte Bibliothek → Ausschlusslisten**

Vorhandene Listen exportieren und mit `data/negativlisten/` abgleichen. Alles, was dort
schon steht und in unseren Listen fehlt, ist wertvoll – es stammt aus echten
Suchbegriffdaten.

### A4 – Umstellungsentscheidung je bestehender Kampagne

| Befund | Vorgehen |
|---|---|
| Kein Conversion-Tracking vorhanden | Alte Kampagne **pausieren**, neue Struktur startet sauber |
| Tracking vorhanden, CPA gut | Alte Kampagne **vorerst weiterlaufen lassen**; neue Kampagne nur für Rechtsgebiete, die noch nicht abgedeckt sind |
| Tracking vorhanden, CPA schlecht | Alte Kampagne **pausieren**, neue Struktur übernimmt |
| Performance-Max-Kampagne aktiv | **Pausieren** – PMax nimmt den Suchkampagnen bei diesem Budget die Anfragen weg (Doc 01) |

> **Pausieren, nicht löschen.** Eine gelöschte Kampagne nimmt ihre Historie mit. Eine
> pausierte bleibt auswertbar und lässt sich reaktivieren.

### A5 – Umstellung gestaffelt, nicht auf einen Schlag

Empfohlene Reihenfolge über drei Wochen:

```
Woche 1   Neue Kampagne "Erbrecht" aktivieren, entsprechende alte Kampagne pausieren
          → eine Woche beobachten: Kosten, Anfragen, Suchbegriffe
Woche 2   Neue Kampagne "Immobilien + Treuhand" aktivieren, alte pausieren
Woche 3   Neue Kampagne "Scheidung + Familie" aktivieren, alte pausieren
          Brand und Gesellschaftsrecht zuletzt
```

So bleibt bei einem Fehler immer nur ein Rechtsgebiet betroffen.

---

## Teil B – Google Ads Editor einrichten {#teil-b}

Die 206 Keywords und 30 Anzeigen von Hand in die Weboberfläche einzugeben, dauert Tage.
Mit dem Editor sind es Minuten.

### B1 – Installieren

Google Ads Editor ist kostenlos und läuft lokal:
`ads.google.com/intl/de/home/tools/ads-editor/`

### B2 – Konto laden

1. Editor öffnen → **Konto → Konten öffnen**
2. **Anmelden** mit dem Google-Konto der Kanzlei
3. Konto auswählen → **Neueste Änderungen abrufen** (lädt den aktuellen Kontostand)
4. Beim ersten Mal: **Alle Kampagnen** auswählen

### B3 – Sicherungskopie anlegen

**Konto → Konto exportieren → Ganzes Konto exportieren (CSV)**

Das ist Ihr Rückfallpunkt. Vor jedem größeren Import wiederholen.

---

## Teil C – Ausschlusslisten anlegen {#teil-c}

Diese werden in der **Weboberfläche** angelegt, nicht im Editor – geteilte Listen sind
eine Kontofunktion.

### C1 – Sieben Listen erstellen

**Tools → Gemeinsam genutzte Bibliothek → Ausschlusslisten → ➕**

Für jede der sieben Listen:

1. Name eintragen, exakt wie in der Datei:
   `L1 Jobs und Ausbildung`, `L2 Gratis und DIY`, `L3 Information`,
   `L4 DE-Rechtsbegriffe`, `L5 Fremde Rechtsgebiete`, `L6 Portale`, `L7 Standorte`
2. Die passende CSV aus `data/negativlisten/` öffnen
3. Nur die **Keyword-Spalte** kopieren, in das Eingabefeld einfügen
4. **Übereinstimmungstyp beachten:** Google erwartet in diesem Feld
   - Broad → Wort ohne Zeichen: `job`
   - Phrase → in Anführungszeichen: `"kündigung arbeitsvertrag"`
   - Exact → in eckigen Klammern: `[erbschein]`

   In den CSV-Dateien steht der Typ in einer eigenen Spalte. Am schnellsten geht es,
   die Phrase-Einträge in einem zweiten Durchgang mit Anführungszeichen nachzutragen.
5. **Speichern**

### C2 – Listen den Kampagnen zuweisen

Erst nach Teil D möglich. Die Zuordnung steht in **Doc 03, Abschnitt 3.4**:

| Kampagne | L1 | L2 | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|---|
| BRAND | ✓ | | | | ✓ | | |
| alle anderen | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Stiftung + Nachfolge | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | – |

Zuweisen unter **Kampagnen → [Kampagne] → Keywords → Ausgeschlossene Keywords →
Listen → Ausschlusslisten anwenden**.

### C3 – Konfliktprüfung

Vor dem Anlegen einmal lokal prüfen:

```bash
python3 tools/pruefe_negativlisten.py
```

Meldet jeden Ausschluss, der ein eigenes aktives Keyword blockieren würde.

---

## Teil D – Kampagnen anlegen {#teil-d}

Kampagnen mit ihren Einstellungen werden in der **Weboberfläche** angelegt – dort sind
alle Optionen zugänglich. Keywords und Anzeigen kommen danach über den Editor.

### D1 – Neue Kampagne

**Kampagnen → ➕ → Neue Kampagne**

1. **Zielvorhaben:** *Ohne Zielvorhaben fortfahren* auswählen
   → verhindert, dass Google Einstellungen vorwegnimmt
2. **Kampagnentyp:** **Suchnetzwerk**
3. **Ergebnisse:** Websitebesuche **und** Anrufe ankreuzen, Rufnummer +43 1 205 1003
4. **Name** exakt nach Doc 02, Abschnitt 2.2, z. B.
   `SUCHE | Erbrecht | Wien+NÖ | P1`

### D2 – Gebote

- **Worauf möchten Sie sich konzentrieren?** → siehe Startstufe aus Schritt A2
- Bei *Klicks maximieren*: **Höchstgebot für Cost-per-Click festlegen** aktivieren,
  Wert aus der Spalte `Max CPC` der Keyword-CSV (höchster Wert der Kampagne)

### D3 – Kampagneneinstellungen (der wichtigste Bildschirm)

| Einstellung | Wert |
|---|---|
| **Netzwerke** | Suchnetzwerk ✓ · **Suchnetzwerk-Partner ✗** · **Displaynetzwerk ✗** |
| **Standorte** | Wien; zusätzlich Radius 25 km um 1030 Wien; bei Erbrecht/Immobilien auch Niederösterreich und Burgenland |
| **Standortoptionen** | ⚠️ **Aufklappen!** → *Anwesenheit: Personen an oder regelmäßig an Ihren Zielstandorten* |
| **Ausgeschlossene Standorte** | Deutschland, Schweiz |
| **Sprachen** | Deutsch, Englisch |
| **Tagesbudget** | nach Doc 07, Abschnitt 7.2 |

> **Die Standortoption ist der teuerste Standardfehler.** Google steht ab Werk auf
> *Anwesenheit oder Interesse* – damit klicken Menschen aus Hamburg, die sich für Wien
> *interessieren*. Diese Einstellung liegt aufgeklappt hinter „Standortoptionen" und wird
> fast immer übersehen.

### D4 – Weitere Einstellungen aufklappen

- **Anzeigenrotation:** Optimieren
- **Werbezeitplan:** vorerst leer lassen – kommt in Teil G
- **Kampagnen-URL-Optionen:** Tracking-Vorlage nur, wenn ein Tracking-Tool im Einsatz ist

### D5 – Vorläufige Anzeigengruppe

Google verlangt beim Anlegen mindestens eine Anzeigengruppe mit einer Anzeige. Legen Sie
eine Platzhalter-Gruppe an – sie wird in Teil E gelöscht. **Kampagne pausiert speichern.**

### D6 – Für alle fünf Kampagnen wiederholen

`BRAND`, `Scheidung+Familie`, `Erbrecht`, `Immobilien+Treuhand`, `Gesellschaftsrecht`.
Alle zunächst **pausiert**.

---

## Teil E – Keywords und Anzeigen importieren {#teil-e}

### E1 – Importdateien erzeugen

```bash
python3 tools/baue_editor_import.py
```

Erzeugt drei Dateien in `import/`. Das Skript meldet auch, ob jede Anzeigengruppe
Keywords, Anzeigentexte und eine Zielseite hat.

### E2 – Keywords importieren

1. Editor → **Konto → Importieren → Aus Datei importieren**
2. `import/keywords.csv` auswählen
3. Im Vorschaufenster **Spaltenzuordnung prüfen** – der Editor erkennt
   `Campaign`, `Ad Group`, `Keyword`, `Criterion Type`, `Max CPC`, `Final URL` automatisch
4. **Vorgeschlagene Änderungen prüfen** → es müssen 206 Keywords und 30 neue
   Anzeigengruppen erscheinen
5. **Änderungen übernehmen**

> Die Kampagnennamen in der CSV müssen **exakt** mit den in Teil D angelegten
> übereinstimmen, sonst legt der Editor neue Kampagnen an. Bei einer Abweichung: Import
> rückgängig machen (Strg+Z), Namen in der CSV korrigieren, erneut importieren.

### E3 – Anzeigen importieren

Gleicher Weg mit `import/anzeigen-rsa.csv`. Ergebnis: 30 Responsive Suchanzeigen mit
gesetztem Pinning auf Position 1.

### E4 – Platzhalter entfernen

Die in Teil D angelegten Platzhalter-Anzeigengruppen jetzt löschen.

### E5 – Prüfen und posten

1. **Prüfen → Änderungen prüfen** – der Editor meldet Fehler und Warnungen
2. Typische Meldungen:
   - *Zielseite nicht erreichbar* → die Landingpage existiert noch nicht (siehe Doc 05).
     Vorerst auf die nächsthöhere vorhandene Seite umhängen.
   - *Keyword doppelt* → sollte nicht auftreten, die Dateien sind geprüft
3. **Posten** – erst danach ist alles im Konto

---

## Teil F – Assets und Erweiterungen {#teil-f}

**Kampagnen → Assets → ➕**, jeweils auf **Kontoebene** anlegen, damit sie für alle
Kampagnen gelten. Vorlagen: `data/anzeigen/assets-erweiterungen.csv`

| Asset | Anzahl | Hinweis |
|---|---|---|
| **Sitelinks** | 8 | Je zwei Beschreibungszeilen ausfüllen – ohne sie werden sie kleiner ausgeliefert |
| **Snippets (Callouts)** | 8 | |
| **Strukturierte Snippets** | 3 | Kopfzeile: *Dienstleistungen* |
| **Anruf** | 1 | Zeitplan folgt in Teil G |
| **Standort** | 1 | Setzt ein verifiziertes Google-Business-Profil voraus |
| **Bild** | 3–5 | Echte Kanzleiaufnahmen. Keine Stockfotos mit Richterhammer – der Gavel kommt an österreichischen Gerichten nicht vor |

**Nicht anlegen:** Preis-Assets, Promotion-Assets, Lead-Formular-Assets. Begründung in
Doc 04, Abschnitt 4.5.

### Anzeigenpfade nachtragen

Die Pfade stehen in Doc 04, Abschnitt 4.2 und werden beim Import bereits gesetzt.
Stichprobe: eine Anzeige öffnen und prüfen, dass unter der URL z. B.
`drweiser.at/Erbrecht/Wien` steht.

---

## Teil G – Werbezeitplan und Anruf-Asset {#teil-g}

### G1 – Zeitpläne erzeugen

```bash
python3 tools/baue_werbezeitplan.py
```

Grundlage sind die Bürozeiten in `data/erreichbarkeit/buerozeiten.csv`
(Mo–Do 09:00–17:00, Fr 09:00–13:00, durchgehend besetzt).

### G2 – Werbezeitplan eintragen

**Kampagnen → [Kampagne] → Einstellungen → Werbezeitplan**

Die 30 Zeitblöcke aus `import/werbezeitplan.csv` eintragen. Spalte `Bid adjustment`
ist die Gebotsanpassung.

> Das ist der mühsamste Handgriff der ganzen Einrichtung. Er lohnt sich nur in Phase 1 –
> ab „Conversions maximieren" ignoriert Google die Gebotsanpassungen weitgehend. Wenn Sie
> nach Schritt A2 direkt auf *Conversions maximieren* starten, **überspringen Sie die
> Gebotsanpassungen** und tragen nur die Zeiten ein, in denen gar nicht geschaltet werden
> soll (nachts).

### G3 – Anruf-Asset zeitlich begrenzen

**Kampagnen → Assets → Anruf-Asset → Bearbeiten → Erweiterte Optionen → Zeitplan**

Die 18 Blöcke aus `import/anruf-asset-zeitplan.csv` eintragen:
Mo–Do 09:00–17:00, Fr 09:00–13:00.

**Außerhalb dieser Zeiten wird die Rufnummer nicht eingeblendet.** Begründung in Doc 12:
Ein bezahlter Klick, der auf dem Anrufbeantworter landet, hinterlässt keinen Kontakt.

### G4 – Anrufberichte aktivieren

**Verwaltung → Kontoeinstellungen → Anrufberichte → aktivieren**
Mindestdauer für eine Conversion: **60 Sekunden**.

Falls die Google-Anrufweiterleitungsnummer für Österreich nicht verfügbar ist, bleibt die
Klickzahl auf das Anruf-Asset als Näherung (Doc 12, Abschnitt 12.6).

---

## Teil H – Conversion-Tracking prüfen {#teil-h}

Laut Ihrer Angabe ist Woche 2 des Fahrplans erledigt – Consent Mode v2, Google Tag
Manager und Analytics 4 stehen also. Dieser Teil ist daher **Prüfung, keine Einrichtung**.

### H1 – Die vier Kontrollen

| # | Prüfung | Wo | Sollzustand |
|---|---|---|---|
| 1 | Conversion-Aktionen vorhanden | Zielvorhaben → Conversions | Anruf, Formular, Termin als **Primär** |
| 2 | E-Mail-Klick, WhatsApp, Seitenaufruf | ebenda | als **Sekundär** markiert |
| 3 | Consent Mode v2 aktiv | Zielvorhaben → Conversions → Einwilligungseinstellungen | Status *aktiv* |
| 4 | Enhanced Conversions für Leads | Conversion-Aktion → Einstellungen | aktiviert |

Punkt 2 ist der häufigste Fehler: Ein E-Mail-Klick als primäre Conversion trainiert Google
darauf, Menschen zu liefern, die auf E-Mail-Adressen klicken – nicht solche, die anrufen.

### H2 – GCLID-Feld im Formular

Für den späteren Offline-Conversion-Import (Doc 06, Abschnitt 6.6) muss das
Kontaktformular ein verstecktes Feld enthalten, das die GCLID aus der URL mitspeichert.

**Das muss ab dem ersten Tag laufen**, auch wenn der Import erst ab Monat 4 genutzt wird –
ohne die gespeicherten GCLIDs fehlt später die Historie.

Prüfung: Eine Landingpage mit `?gclid=TEST123` aufrufen, Formular abschicken, in der
Formularverwaltung nachsehen, ob `TEST123` mitgespeichert wurde.

### H3 – Die Testanfrage

**Der wichtigste Schritt der ganzen Einrichtung, und der am häufigsten übersprungene.**

1. Eine Kampagne kurz aktivieren, Tagesbudget vorübergehend auf 5 €
2. Selbst googeln, was ein Mandant googeln würde (z. B. „scheidungsanwalt wien")
3. Auf die eigene Anzeige klicken
4. Auf der Landingpage das Formular ausfüllen und absenden
5. **In Google Ads prüfen:** Zielvorhaben → Conversions → die Conversion muss innerhalb
   von 3–24 Stunden erscheinen
6. Denselben Test mit einem Anruf über die Anzeige wiederholen
7. Kampagne wieder pausieren, Budget zurücksetzen

Erscheint die Test-Conversion nicht, ist die Messkette unterbrochen. **Dann nicht starten** –
sonst laufen Wochen Budget ohne verwertbare Daten.

---

## Teil I – Testlauf und Start {#teil-i}

### I1 – Abschlussprüfung

- [ ] Alle Werkzeuge laufen fehlerfrei:
      `pruefe_anzeigen.py`, `pruefe_negativlisten.py`, `baue_editor_import.py`
- [ ] Standortoption steht auf *Anwesenheit*, nicht *Anwesenheit oder Interesse*
- [ ] Suchnetzwerk-Partner und Displaynetzwerk sind **aus**
- [ ] Deutschland und Schweiz sind ausgeschlossen
- [ ] Alle sieben Ausschlusslisten sind zugewiesen
- [ ] Jede Anzeigengruppe hat mindestens 8 Anzeigentitel und 4 Beschreibungen
- [ ] Anruf-Asset hat einen Zeitplan
- [ ] Testanfrage ist als Conversion sichtbar
- [ ] Alte konkurrierende Kampagnen sind pausiert (Teil A4)
- [ ] Summe aller Tagesbudgets entspricht dem geplanten Monatsbudget ÷ 30,4

### I2 – Gestaffelt starten

Nach dem Plan aus Schritt A5: eine Kampagne pro Woche aktivieren, beginnend mit Erbrecht.

### I3 – Die ersten 72 Stunden

Täglich prüfen:

| Was | Wo | Warnsignal |
|---|---|---|
| Abgelehnte Anzeigen | Kampagnen → Anzeigen | rotes Symbol bei einer Anzeige |
| Budgetverbrauch | Kampagnen-Übersicht | Budget vor Mittag aufgebraucht |
| Suchbegriffe | Keywords → Suchbegriffe | offensichtlich unpassende Anfragen |
| Erste Conversions | Zielvorhaben → Conversions | nach 72 h keine einzige |

---

## Teil J – Die erste Woche {#teil-j}

### Täglich, 10 Minuten

**Kampagnen → Keywords → Suchbegriffe**, Zeitraum *Gestern*, nach Kosten sortiert.

Jeden unpassenden Begriff ausschließen. Auf der richtigen Ebene:

| Der Begriff ist unpassend für … | Ausschluss auf Ebene |
|---|---|
| nur diese eine Anzeigengruppe | Anzeigengruppe |
| die ganze Kampagne | Kampagne |
| das gesamte Konto | passende Ausschlussliste (L1–L7) |

Neue Ausschlüsse zusätzlich in `data/negativlisten/` nachtragen, damit die Dateien den
Kontostand abbilden. Danach `python3 tools/pruefe_negativlisten.py` laufen lassen.

### Was in der ersten Woche NICHT getan wird

| Nicht tun | Grund |
|---|---|
| Gebotsstrategie wechseln | Lernphase beginnt von vorn |
| Anzeigentexte ändern | Zu wenig Daten für eine Bewertung |
| Budget erhöhen | Erst den Verlust durch Budget messen |
| Keywords pausieren | Sieben Tage sind keine Datenbasis |
| Googles Empfehlungen übernehmen | Jede einzeln prüfen – der „Optimierungsfaktor" ist kein Ziel |

---

## Die häufigsten Fehler bei der Einrichtung

| Fehler | Folge | Verhindern durch |
|---|---|---|
| Standortoption auf *Interesse* belassen | Klicks aus ganz Deutschland | Teil D3 |
| Suchnetzwerk-Partner aktiviert gelassen | Streuverlust ohne Auswertbarkeit | Teil D3 |
| Ohne Test-Conversion gestartet | Wochen ohne verwertbare Daten | Teil H3 |
| Alte Kampagne auf dieselben Keywords weiterlaufen lassen | Daten verteilen sich, Auswertung unbrauchbar | Teil A4 |
| E-Mail-Klick als primäre Conversion | Google optimiert auf das Falsche | Teil H1 |
| Alle Kampagnen gleichzeitig gestartet | Bei einem Fehler ist alles betroffen | Teil A5 |
| Anruf-Asset ohne Zeitplan | Bezahlte Klicks landen auf dem Anrufbeantworter | Teil G3 |
| Landingpages fehlen, alles zeigt auf die Startseite | Niedriger Qualitätsfaktor, höherer Klickpreis | Doc 05 |
