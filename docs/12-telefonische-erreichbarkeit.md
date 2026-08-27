# 12 – Telefonische Erreichbarkeit

## 12.1 Warum das ein Kampagnenthema ist und keine Bürofrage

Der Anruf ist bei Anwaltssuchen der wertvollste Kontaktweg. Wer in einer Trennungssituation
oder nach einem Todesfall auf die Rufnummer tippt, will jetzt sprechen – nicht ein Formular
ausfüllen. Genau deshalb ist die Erreichbarkeit Teil der Kampagnensteuerung:

**Ein Klick auf „Scheidungsanwalt Wien" kostet 5,00–6,50 €. Aus rund 16 Klicks entsteht
eine Anfrage – also rund 92 € je Anfrage. Wird daraus ein Anruf und niemand hebt ab, sind
diese 92 € verloren.** Und der Anrufer wählt die nächste Nummer in den Suchergebnissen.

Ein verpasster Anruf ist kein entgangener Interessent. Es ist ein **bereits bezahlter**
Interessent, den man ein zweites Mal kaufen müsste.

## 12.2 Die Ausgangslage der Kanzlei

| | |
|---|---|
| **Telefonzeiten** | Mo–Do 09:00–17:00, Fr 09:00–13:00 |
| **Durchgehend besetzt** | ja, keine Mittagspause |
| **Anrufbeantworter** | vorhanden |
| **Wochenstunden mit besetztem Telefon** | 36 |

*Angabe der Kanzlei vom 27. 08. 2026, hinterlegt in `data/erreichbarkeit/buerozeiten.csv`.*

> **Die durchgehende Besetzung ist ein echter Vorteil.** Bei vielen Kanzleien fällt die
> Mittagszeit als Telefonlücke aus – und zwar ausgerechnet in einer Stunde, in der viele
> Menschen Privates erledigen. Dass bei Ihnen zwischen 12 und 13 Uhr jemand abhebt, deckt
> vier zusätzliche Stunden Kernnachfrage pro Woche ab.

### Abdeckungsrechnung

| | Anteil der Suchnachfrage |
|---|---|
| Stunden mit besetztem Telefon | **39,3 %** |
| Stunden ohne Telefonbesetzung | **60,7 %** |
| davon in Stunden mit **starker** Nachfrage | **17,7 %** |

Rund 60 % der Nachfrage fallen außerhalb der Telefonzeiten an. Das ist für eine
Einzelkanzlei normal und kein Mangel – entscheidend ist, dass diese Stunden einen
funktionierenden zweiten Weg haben.

### Die verbleibenden Lücken

| Zeitfenster | Nachfrage | Charakter |
|---|---|---|
| **Mo–Fr 08:00–09:00** | 7/10 | Menschen erledigen Privates vor Arbeitsbeginn |
| **Mo–Do 19:00–21:00** | 7/10 | Abendrecherche, oft die erste ernsthafte Beschäftigung mit dem Thema |
| **So 17:00–22:00** | 7–9/10 | Das stärkste Fenster der Woche außerhalb der Bürozeiten |

Der **Sonntagabend** ist der klassische Recherchezeitraum für Scheidungs- und
Erbrechtsthemen. Niemand erwartet dort einen Anwalt am Telefon – wohl aber eine Seite,
die einen Rückruf für Montagfrüh entgegennimmt.

Die Stunde **08:00–09:00** ist die einzige Lücke, die durch eine Anpassung der Bürozeiten
schließbar wäre. Ob sich das lohnt, zeigen die Anrufberichte nach 60 Tagen – vorher wäre
das eine Entscheidung ohne Datengrundlage.

> Die Nachfrageverteilung ist eine Planungsannahme. Nach 60 Tagen Laufzeit liefert
> Google Ads den Bericht „Stunde und Wochentag" mit den echten Zahlen. Diesen Export als
> `data/erreichbarkeit/nachfrage-ist.csv` ablegen – das Werkzeug verwendet dann automatisch
> die realen Daten statt der Annahme.

## 12.3 Die drei Hebel

### Hebel 1 – Das Anruf-Asset zeitlich steuern

Der wichtigste Handgriff und zugleich der einfachste. **Das Anruf-Asset hat in Google Ads
einen eigenen Zeitplan, unabhängig vom Werbezeitplan der Kampagne.**

Die Anzeigen laufen also weiter, wenn niemand am Telefon ist – aber **ohne Rufnummer**.
Statt eines Anrufs auf den Anrufbeantworter entsteht ein Klick auf die Landingpage mit
Rückrufformular.

> **Warum die Rufnummer trotz Anrufbeantworter ausgeblendet wird:** Ein Anrufbeantworter
> ist kein Ersatz für ein Gespräch. Ein erheblicher Teil der Anrufer legt auf, statt eine
> Nachricht zu hinterlassen – gerade bei einem heiklen persönlichen Anliegen. Der Klick auf
> die Rufnummer ist dann bezahlt, aber es bleibt kein Kontakt zurück. Ein Formular mit
> Namen und Rückrufnummer ist der verlässlichere Weg. Der Anrufbeantworter bleibt
> selbstverständlich aktiv – er fängt weiterhin die Anrufe auf, die über die Website, das
> Google-Business-Profil oder Empfehlungen kommen.

Erzeugt aus den Bürozeiten:

```bash
python3 tools/baue_werbezeitplan.py
```

Ergebnis: `import/anruf-asset-zeitplan.csv` – 18 Blöcke, in denen die Rufnummer
eingeblendet wird (Mo–Do 09:00–17:00, Fr 09:00–13:00).

### Hebel 2 – Werbezeitplan mit Gebotsanpassung

`import/werbezeitplan.csv` enthält 30 Zeitblöcke mit drei Zuständen:

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

Kostet nichts und deckt die 60,7 % ab, in denen niemand abnimmt.

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

## 12.4 Telefonannahmedienst – vorerst nicht nötig

Ein Telefonannahmedienst für die Randzeiten war als Option vorgesehen. Da die Kanzlei
durchgehend besetzt ist und ein Anrufbeantworter besteht, ist er **derzeit nicht
empfohlen**. Die Entscheidung sollte erst nach 60 Tagen auf Basis echter Zahlen fallen –
und dann anhand einer konkreten Frage:

> **Wie viele der außerhalb der Bürozeiten eingegangenen Anrufe hinterlassen tatsächlich
> eine Nachricht auf dem Anrufbeantworter?**

Das lässt sich in zwei Wochen mit einer Strichliste klären. Bleiben viele Anrufe ohne
Nachricht, ist das die Lücke, die ein Annahmedienst schließen würde.

Erst dann greift die Wirtschaftlichkeitsrechnung. Die richtige Frage ist nicht, was der
Dienst kostet, sondern was es kostet, dieselben Anfragen ein zweites Mal über Anzeigen
einzukaufen – rund 92 € je Anfrage:

| Monatsgebühr | Gerettete Anrufe nötig, um sich zu tragen |
|---|---|
| 150 € | **2 pro Monat** |
| 250 € | **3 pro Monat** |
| 400 € | **5 pro Monat** |

Falls es später doch dazu kommt: Für eine Kanzlei gelten fünf nicht verhandelbare
Anforderungen.

1. **Verschwiegenheitsvereinbarung.** Der Dienst erfährt Namen und Anliegen von Menschen,
   die sich an einen Rechtsanwalt wenden. Bereits die Tatsache der Kontaktaufnahme ist von
   der Verschwiegenheitspflicht nach § 9 RAO erfasst.
2. **Auftragsverarbeitervertrag nach Art 28 DSGVO**, mit Serverstandort in der EU.
3. **Keine Sachverhaltsaufnahme.** Nur Name, Rückrufnummer, Rechtsgebiet, Dringlichkeit.
   **Nicht:** worum es geht.
4. **Keine Rechtsauskunft** – auch keine zu Fristen, Kosten oder Erfolgsaussichten.
5. **Meldung mit dem Kanzleinamen**, nicht mit dem Namen des Dienstleisters.

## 12.5 Die Werkzeuge

```bash
# Bürozeiten (bereits eingetragen) ändern
nano data/erreichbarkeit/buerozeiten.csv

# Zeitpläne und Abdeckungsrechnung neu erzeugen
python3 tools/baue_werbezeitplan.py
```

| Datei | Inhalt |
|---|---|
| `import/werbezeitplan.csv` | 30 Zeitblöcke mit Gebotsanpassung je Erreichbarkeitszustand |
| `import/anruf-asset-zeitplan.csv` | 18 Blöcke mit eingeblendeter Rufnummer |

Dazu ein Bericht auf der Konsole: telefonische Abdeckung in Prozent und eine Liste der
Stunden mit starker Nachfrage und unbesetztem Telefon.

Ändern sich die Zeiten – Urlaub, geänderte Sprechzeiten, eine frühere Öffnung ab 8 Uhr –,
wird die Eingabedatei angepasst und das Werkzeug erneut ausgeführt. Die Zeitpläne folgen
automatisch.

## 12.6 Messung

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

Da die Rufnummer künftig nur zu besetzten Zeiten eingeblendet wird, sollte dieser Wert
von Beginn an hoch sein. Fällt er darunter, geht während der Bürozeiten etwas verloren –
etwa weil parallel telefoniert wird oder ein Termin läuft. Das ist dann ein anderes
Problem als eine Randzeitlücke und braucht eine andere Antwort (zweite Leitung,
Rufumleitung, Terminfenster ohne Telefondienst).

### Ein einfaches Frühwarnsignal

Wenn die Klicks auf das Anruf-Asset steigen, die Zahl der geführten Gespräche aber nicht,
läuft etwas ins Leere. Das ist mit einer Strichliste am Telefon in zwei Wochen geklärt.

## 12.7 Textbausteine

### Ansage des Anrufbeantworters

Die bestehende Ansage sollte drei Dinge enthalten, die häufig fehlen: die konkreten
Zeiten, eine Rückrufzusage mit Frist und den Verweis auf das Formular.

> „Sie erreichen die Kanzlei Dr. Martin Weiser. Wir sind derzeit nicht persönlich
> erreichbar. Unsere Telefonzeiten sind Montag bis Donnerstag von 9 bis 17 Uhr und
> Freitag von 9 bis 13 Uhr. Hinterlassen Sie bitte Ihren Namen und Ihre Telefonnummer –
> wir rufen Sie am nächsten Werktag zurück. Sie können uns auch jederzeit über das
> Formular auf drweiser.at erreichen. Vielen Dank."

Kurz, konkret, mit einer Zusage. Keine Musik, keine Warteschleife.

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

## 12.8 Nächste Schritte

- [x] Bürozeiten eingetragen (Mo–Do 09:00–17:00, Fr 09:00–13:00, durchgehend besetzt)
- [x] Werbezeitplan und Anruf-Asset-Zeitplan erzeugt
- [ ] **Bürozeiten im Google-Business-Profil hinterlegen** – wirkt sofort auf die lokale
      Suche und blendet „Jetzt geöffnet" ein
- [ ] Bürozeiten auf `/kontakt` und auf jede Landingpage übernehmen
- [ ] Ansage des Anrufbeantworters um Zeiten, Rückrufzusage und Formularhinweis ergänzen
- [ ] Rückrufformular mit Fristzusage auf den Landingpages umsetzen (Doc 05)
- [ ] Erfassungsbogen ans Telefon legen
- [ ] Anrufberichte im Google-Ads-Konto aktivieren, Mindestdauer 60 s
- [ ] Nach 60 Tagen: Bericht „Stunde und Wochentag" exportieren, als
      `data/erreichbarkeit/nachfrage-ist.csv` ablegen, Werkzeug erneut ausführen
- [ ] Nach 60 Tagen: Strichliste auswerten – wie viele Anrufer hinterlassen keine Nachricht?
