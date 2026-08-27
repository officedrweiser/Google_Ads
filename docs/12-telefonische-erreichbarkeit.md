# 12 – Telefonische Erreichbarkeit

## 12.1 Warum das ein Kampagnenthema ist und keine Bürofrage

Der Anruf ist bei Anwaltssuchen der wertvollste Kontaktweg. Wer in einer Trennungssituation
oder nach einem Todesfall auf die Rufnummer tippt, will jetzt sprechen – nicht ein Formular
ausfüllen. Genau deshalb ist die Erreichbarkeit Teil der Kampagnensteuerung:

**Ein Klick auf „Scheidungsanwalt Wien" kostet 5,00–6,50 €. Aus rund 16 Klicks entsteht
eine Anfrage – also rund 92 € je Anfrage. Wird daraus ein Anruf und niemand hebt ab, sind
diese 92 € verloren.** Und der Anrufer wählt die nächste Nummer in den Suchergebnissen.

Ein verpasster Anruf ist kein entgangener Interessent. Es ist ein **bereits bezahlter
Interessent**, den man ein zweites Mal kaufen müsste.

## 12.2 Der Befund

Für Ihre Kanzlei sind öffentlich **keine Bürozeiten hinterlegt** – weder auf herold.at,
cylex.at, susi.at noch im Branchenbuch. Das hat zwei unmittelbare Folgen:

1. **Das Google-Business-Profil zeigt keine Öffnungszeiten.** Google blendet bei lokalen
   Suchen „Jetzt geöffnet" ein – ohne hinterlegte Zeiten entfällt dieses Signal, und das
   Profil rankt im Kartenbereich schwächer.
2. **Das Anruf-Asset kann nicht sinnvoll geplant werden.** Ohne Zeiten wird die Rufnummer
   entweder rund um die Uhr eingeblendet (dann läuft ein Teil der Anrufe ins Leere) oder
   gar nicht (dann verschenkt man den besten Kontaktweg).

### Rechnung mit den derzeit angenommenen Zeiten

Grundlage: Mo–Do 09:00–17:00 mit Mittagspause 12:00–13:00, Fr 09:00–13:00.
**Das ist eine Annahme, keine erhobene Angabe** – bitte in
`data/erreichbarkeit/buerozeiten.csv` korrigieren.

| | Anteil der Suchnachfrage |
|---|---|
| Stunden mit besetztem Telefon | **35,5 %** |
| Stunden ohne Telefonbesetzung | **64,5 %** |
| davon in Stunden mit **starker** Nachfrage | **21,4 %** |

Rund zwei Drittel der Nachfrage fallen damit in Zeiten, in denen ein Anruf ins Leere geht.
Das ist für eine Einzelkanzlei nicht ungewöhnlich – aber es ist steuerbar.

### Die konkreten Lücken

| Zeitfenster | Nachfrage | Warum es weh tut |
|---|---|---|
| **Mo–Fr 08:00–09:00** | 7/10 | Menschen erledigen Privates vor Arbeitsbeginn |
| **Mo–Do 12:00–13:00** | 7/10 | Die Mittagspause der Kanzlei ist die Mittagspause der Anrufer |
| **Mo–Do 19:00–21:00** | 7/10 | Abendrecherche, oft die erste ernsthafte Beschäftigung mit dem Thema |
| **So 17:00–22:00** | 7–9/10 | Das stärkste Fenster der Woche außerhalb der Bürozeiten |

Die **Mittagspause** ist die ärgerlichste Lücke: Sie liegt mitten in der Kernzeit und
kostet vier Stunden Nachfrage pro Woche, die sonst voll abgedeckt wären.

Der **Sonntagabend** ist der klassische Recherchezeitraum für Scheidungs- und
Erbrechtsthemen. Niemand erwartet dort einen Anwalt am Telefon – wohl aber eine Seite,
die einen Rückruf für Montagfrüh entgegennimmt.

> Die Nachfrageverteilung ist eine Planungsannahme. Nach 60 Tagen Laufzeit liefert
> Google Ads den Bericht „Stunde und Wochentag" mit den echten Zahlen. Diesen Export als
> `data/erreichbarkeit/nachfrage-ist.csv` ablegen – das Werkzeug verwendet dann automatisch
> die realen Daten statt der Annahme.

## 12.3 Die vier Hebel

### Hebel 1 – Das Anruf-Asset zeitlich steuern

Der wichtigste Handgriff und zugleich der einfachste. **Das Anruf-Asset hat in Google Ads
einen eigenen Zeitplan, unabhängig vom Werbezeitplan der Kampagne.**

Das bedeutet: Die Anzeigen laufen weiter, wenn niemand am Telefon ist – aber **ohne
Rufnummer**. Statt eines Anrufs ins Leere entsteht ein Klick auf die Landingpage mit
Rückrufformular. Der Interessent geht nicht verloren, er nimmt nur den anderen Weg.

Erzeugt aus Ihren Bürozeiten:

```bash
python3 tools/baue_werbezeitplan.py
```

Ergebnis: `import/anruf-asset-zeitplan.csv` – die Blöcke, in denen die Rufnummer
eingeblendet wird.

### Hebel 2 – Werbezeitplan mit Gebotsanpassung

`import/werbezeitplan.csv` enthält die Zeitblöcke mit drei Zuständen:

| Zustand | Gebotsanpassung | Was passiert |
|---|---|---|
| **Telefon besetzt**, starke Nachfrage | +15 % | Rufnummer sichtbar, voller Einsatz |
| **Telefon besetzt** | +10 % | Rufnummer sichtbar |
| **Nur Formular** | −25 % | Rufnummer aus, Landingpage mit Rückrufwunsch |
| **Anzeigen aus** | – | Nachts, wenn praktisch niemand sucht |

> **Wichtig:** Diese Gebotsanpassungen wirken nur in **Phase 1** (Klicks maximieren /
> manuelles CPC). Ab „Conversions maximieren" ignoriert Google sie weitgehend. Was in
> allen Phasen wirkt, ist das **Abschalten** von Zeitfenstern und der **Zeitplan des
> Anruf-Assets**. Deshalb ist Hebel 1 der nachhaltigere.

### Hebel 3 – Der Rückrufweg für die unbesetzten Stunden

Kostet nichts und deckt die 64,5 % ab, in denen niemand abnimmt.

Auf jeder Landingpage außerhalb der Telefonzeiten:

```
Statt der Rufnummer prominent:

   "Wir sind derzeit nicht am Telefon erreichbar.
    Hinterlassen Sie Ihre Nummer – wir rufen am nächsten Werktag
    bis 12:00 Uhr zurück."

   [ Name ]  [ Telefonnummer ]  [ Wann erreichbar? ]
   [ Rückruf anfordern ]
```

Zwei Dinge machen den Unterschied:

- **Eine zugesagte Frist**, nicht „wir melden uns". „Bis morgen 12:00 Uhr" ist prüfbar
  und schafft genau die Verbindlichkeit, die ein Anruf sonst liefert.
- **Das Feld „Wann erreichbar?"** – es hebt die Quote erfolgreicher Rückrufe deutlich,
  weil der Rückruf dann nicht seinerseits ins Leere geht.

Die zugesagte Frist muss eingehalten werden. Eine gebrochene Zusage ist schlechter als
gar keine.

### Hebel 4 – Telefonannahmedienst für die Randzeiten

Nur sinnvoll, wenn die Rechnung aufgeht – und die geht anders, als man zunächst denkt.

**Die richtige Frage ist nicht „Was kostet der Dienst?", sondern „Was kostet es, dieselben
Anfragen ein zweites Mal über Anzeigen einzukaufen?"** Eine Anfrage kostet rund 92 €.

| Monatsgebühr | Gerettete Anrufe nötig, um sich zu tragen |
|---|---|
| 150 € | **2 pro Monat** |
| 250 € | **3 pro Monat** |
| 400 € | **5 pro Monat** |

Bei zwei Randzeit-Fenstern (08:00–09:00 und 12:00–13:00, also zehn Stunden pro Woche in
der Kernnachfrage) sind zwei bis fünf zusätzlich angenommene Anrufe im Monat eine
niedrige Hürde. Die Entscheidung sollte trotzdem erst nach 60 Tagen fallen – dann zeigen
die Anrufberichte, wie viele Anrufe tatsächlich verpasst werden.

#### Was ein Annahmedienst für eine Kanzlei erfüllen muss

Das ist kein gewöhnlicher Sekretariatsdienst. Fünf Punkte sind nicht verhandelbar:

1. **Verschwiegenheitsvereinbarung.** Der Dienst erfährt Namen und Anliegen von Menschen,
   die sich an einen Rechtsanwalt wenden. Bereits die Tatsache der Kontaktaufnahme ist von
   der Verschwiegenheitspflicht nach § 9 RAO erfasst.
2. **Auftragsverarbeitervertrag nach Art 28 DSGVO**, mit Serverstandort in der EU.
3. **Keine Sachverhaltsaufnahme.** Der Dienst nimmt auf: Name, Rückrufnummer,
   Rechtsgebiet, Dringlichkeit. **Nicht:** worum es geht. Details gehören ins Gespräch
   mit dem Anwalt, nicht in ein fremdes Ticketsystem.
4. **Keine Rechtsauskunft.** Der Dienst darf keine inhaltlichen Aussagen treffen – auch
   keine zu Fristen, Kosten oder Erfolgsaussichten.
5. **Meldung mit dem Kanzleinamen**, nicht mit dem Namen des Dienstleisters.

## 12.4 Die Werkzeuge

```bash
# 1. Bürozeiten eintragen
nano data/erreichbarkeit/buerozeiten.csv

# 2. Zeitpläne und Abdeckungsrechnung erzeugen
python3 tools/baue_werbezeitplan.py
```

Ausgabe:

| Datei | Inhalt |
|---|---|
| `import/werbezeitplan.csv` | Werbezeitplan mit Gebotsanpassungen je Zeitblock |
| `import/anruf-asset-zeitplan.csv` | Einblendezeiten der Rufnummer |

Dazu ein Bericht auf der Konsole: telefonische Abdeckung in Prozent und eine Liste der
Stunden mit starker Nachfrage und unbesetztem Telefon.

Ändern sich die Bürozeiten – Urlaub, neue Sprechzeiten, ein Annahmedienst –, wird die
Eingabedatei angepasst und das Werkzeug erneut ausgeführt. Die Zeitpläne folgen automatisch.

## 12.5 Messung

### Was Google Ads liefert

| Messgröße | Verfügbarkeit |
|---|---|
| **Klicks auf das Anruf-Asset** | Immer verfügbar – zählt jeden Tipp auf die Rufnummer |
| **Anrufdauer, angenommen/verpasst** | Erfordert eine Google-Anrufweiterleitungsnummer. Die Verfügbarkeit ist länderabhängig – im Konto unter *Anrufberichte* prüfen |
| **Anrufe von der Website** | Über den `tel:`-Link im Google Tag Manager messbar, unabhängig von der Weiterleitungsnummer |

Falls die Weiterleitungsnummer für Österreich nicht verfügbar ist, bleibt die Klickzahl
auf das Anruf-Asset als Näherung – der Abgleich mit den tatsächlich geführten Gesprächen
erfolgt dann manuell.

### Die Kennzahl

```
Anrufannahmequote = angenommene Anrufe ÷ (angenommene + verpasste Anrufe)
Zielwert: über 85 %
```

Diese Zahl gehört in jeden Monatsbericht, direkt neben den CPA. Liegt sie unter 85 %,
ist das Problem nicht die Kampagne, sondern die Erreichbarkeit – und eine Budgeterhöhung
würde das Problem nur vergrößern.

### Ein einfaches Frühwarnsignal

Wenn die Klicks auf das Anruf-Asset steigen, die Zahl der geführten Gespräche aber nicht,
läuft etwas ins Leere. Das ist mit einer Strichliste am Telefon in zwei Wochen geklärt.

## 12.6 Textbausteine

### Ansage außerhalb der Telefonzeiten

> „Sie erreichen die Kanzlei Dr. Martin Weiser. Wir sind derzeit nicht persönlich
> erreichbar. Unsere Telefonzeiten sind Montag bis Donnerstag von 9 bis 17 Uhr und
> Freitag von 9 bis 13 Uhr. Hinterlassen Sie bitte Ihren Namen und Ihre Telefonnummer –
> wir rufen Sie am nächsten Werktag zurück. Sie können uns auch über das Formular auf
> drweiser.at erreichen. Vielen Dank."

Kurz, konkret, mit einer Zusage. Keine Musik, keine Warteschleife.
*(Zeiten anpassen, sobald die tatsächlichen feststehen.)*

### Erfassungsbogen für angenommene Anrufe

Vier Angaben genügen – bewusst ohne Sachverhalt:

```
Datum / Uhrzeit      ______________________
Name                 ______________________
Rückrufnummer        ______________________
Rechtsgebiet         ☐ Scheidung/Familie  ☐ Erbrecht  ☐ Immobilien
                     ☐ Gesellschaft  ☐ Sonstiges: __________
Wie auf uns gestoßen ☐ Google  ☐ Empfehlung  ☐ bekannt  ☐ unklar
Termin vereinbart    ☐ ja, am ________   ☐ nein
```

Die Zeile **„Wie auf uns gestoßen"** ist der einfachste verfügbare Abgleich zwischen
Anzeigen und tatsächlichen Mandaten – und die Vorstufe zum Offline-Conversion-Import
aus Doc 06.

## 12.7 Nächste Schritte

- [ ] Tatsächliche Bürozeiten in `data/erreichbarkeit/buerozeiten.csv` eintragen
- [ ] `python3 tools/baue_werbezeitplan.py` ausführen
- [ ] Bürozeiten im Google-Business-Profil hinterlegen (wirkt sofort auf die lokale Suche)
- [ ] Bürozeiten auf `/kontakt` und auf jede Landingpage übernehmen
- [ ] Ansage für außerhalb der Telefonzeiten aufsprechen
- [ ] Rückrufformular mit Fristzusage auf den Landingpages umsetzen (Doc 05)
- [ ] Erfassungsbogen ans Telefon legen
- [ ] Anrufberichte im Google-Ads-Konto aktivieren, Mindestdauer 60 s
- [ ] Nach 60 Tagen: Bericht „Stunde und Wochentag" exportieren, als
      `data/erreichbarkeit/nachfrage-ist.csv` ablegen, Werkzeug erneut ausführen
- [ ] Nach 60 Tagen: Anrufannahmequote prüfen, dann über den Annahmedienst entscheiden
