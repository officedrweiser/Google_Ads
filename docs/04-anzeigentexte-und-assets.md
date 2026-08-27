# 04 – Anzeigentexte & Assets

## 4.1 Umfang und Prüfstatus

449 fertige Anzeigen-Assets für 30 Anzeigengruppen in `data/anzeigen/rsa-anzeigentexte.csv`.

Alle Texte sind mit `tools/pruefe_anzeigen.py` automatisiert geprüft auf:

- Google-Zeichengrenzen (Anzeigentitel ≤ 30, Beschreibung ≤ 90)
- Anzahl der Assets je Anzeigengruppe (Google-Minimum und Empfehlung)
- Duplikate innerhalb einer Anzeigengruppe
- Formatregeln (kein Ausrufezeichen im Anzeigentitel, keine Großbuchstaben-Blöcke)
- **Standesrechtliche Wortfilter nach RL-BA 2015 § 47 Abs 3**

Ergebnis des letzten Laufs: **449 Assets, 30 Anzeigengruppen, 0 Fehler, 0 Hinweise.**

```bash
python3 tools/pruefe_anzeigen.py
```

Das Skript sollte vor jeder Textänderung erneut laufen. Es liefert Exit-Code 1 bei Fehlern
und eignet sich damit auch für eine automatische Prüfung.

## 4.2 Aufbau einer Responsive Suchanzeige

Google mischt aus den bereitgestellten Bausteinen automatisch Anzeigen zusammen.
Pro Anzeigengruppe:

| Element | Google-Limit | Dieser Plan | Zeichen |
|---|---|---|---|
| Anzeigentitel | 3–15 | 8–15 | max. 30 |
| Beschreibung | 2–4 | 4 | max. 90 |
| Anzeigenpfad 1 & 2 | optional | 1–2 gesetzt | max. 15 je |

### Pinning-Strategie

In der Spalte `Pin` der CSV ist `1` eingetragen, wo ein Anzeigentitel an **Position 1**
fixiert werden soll. Fixiert werden ausschließlich die Assets, die das Keyword-Thema
wörtlich aufnehmen – zum Beispiel „Scheidungsanwalt Wien" in der gleichnamigen
Anzeigengruppe.

**Warum überhaupt fixieren:** Ohne Pinning kann Google einen beliebigen Anzeigentitel an
Position 1 setzen. Bei einer Kanzlei mit acht Rechtsgebieten führt das dazu, dass jemand
nach „Pflichtteil" sucht und „Immobilien & Treuhand" als Überschrift sieht. Das kostet
Klickrate und Anzeigenrelevanz.

**Warum nur zwei Assets fixieren:** Jedes zusätzliche Pinning schränkt Googles
Kombinationsmöglichkeiten ein und senkt die Anzeigeneffektivität. Zwei fixierte Titel auf
Position 1 (Google rotiert zwischen ihnen) sind der Kompromiss aus Relevanz und
Testspielraum.

### Anzeigenpfade (Display-URL)

| Kampagne | Pfad 1 | Pfad 2 |
|---|---|---|
| Scheidung + Familie | `Scheidung` | `Wien` |
| Erbrecht | `Erbrecht` | `Wien` |
| Immobilien + Treuhand | `Immobilien` | `Wien` |
| Gesellschaftsrecht | `Gesellschaft` | `Wien` |
| Stiftung + Nachfolge | `Stiftungsrecht` | – |
| Brand | `Kanzlei` | – |

## 4.3 Textbausteine – Systematik

Jede Anzeigengruppe folgt demselben Aufbau, damit die Texte konsistent bleiben:

| Rolle | Anzahl | Beispiel |
|---|---|---|
| **Thema wörtlich** (gepinnt) | 2 | „Pflichtteil Anwalt Wien" |
| **Leistungsdetails** | 3–5 | „Pflichtteil berechnen", „Schenkungsanrechnung" |
| **Kanzlei-Identität** | 2 | „Kanzlei Dr. Weiser, Wien 3", „Rechtsanwalt seit 1990" |
| **Standortnutzen** | 1 | „U3 Rochusgasse, Wien 3" |
| **Vertrauen/Service** | 1–2 | „Klare Kostenauskunft", „Diskret und persönlich" |
| **Handlungsaufforderung** | 1–2 | „Erstgespräch vereinbaren", „Jetzt Termin anfragen" |

Diese Mischung sorgt dafür, dass jede von Google gebaute Kombination aus Thema, Beleg
und Handlungsaufforderung besteht.

## 4.4 Was in den Texten bewusst NICHT vorkommt

| Nicht verwendet | Grund |
|---|---|
| „beste Kanzlei", „Nr. 1", „führend" | Marktschreierische Anpreisung – § 47 Abs 3 lit a RL-BA |
| „98 % Erfolgsquote", „500 gewonnene Verfahren" | Hinweis auf Erfolgszahlen – § 47 Abs 3 lit g RL-BA |
| „besser als …", „günstiger als …" | Vergleichende Werbung gegen Berufskollegen – § 47 Abs 3 lit b RL-BA |
| „nur zahlen bei Erfolg" | Quota-litis-Verbot – § 879 Abs 2 Z 2 ABGB |
| „Fachanwalt für Familienrecht" | Der Fachanwaltstitel existiert in Österreich nicht – irreführend |
| „Spezialist", „Experte" | Suggeriert eine formale Qualifikation; korrekt ist „Schwerpunkt" |
| Mandantennamen oder -logos | Nennung nur mit Zustimmung – § 47 Abs 3 lit e RL-BA |
| „Kostenlose Erstberatung" | siehe unten |

### Zur „kostenlosen Erstberatung"

Werbung mit einer kostenlosen Erstberatung ist in Österreich grundsätzlich zulässig,
solange die Angabe wahr und sachlich ist. Sie ist in diesem Plan trotzdem **nicht**
enthalten, aus zwei praktischen Gründen:

1. **Anfragequalität.** Ein Gratis-Angebot zieht Menschen an, die Auskunft suchen, kein
   Mandat. Bei einem Klickpreis von 5–6 € ist das der teuerste Weg zu unbezahlter Arbeit.
2. **Verbindlichkeit.** Wer die Kostenfrage transparent beantwortet („Wir besprechen das
   Honorar vorab"), gewinnt dieselbe Sicherheit, ohne Gratisleistung zu versprechen.

Falls Sie es dennoch anbieten wollen: unbedingt eingegrenzt formulieren, etwa
„Kostenloses Erstgespräch, 15 Minuten telefonisch" – und es muss tatsächlich so gehandhabt
werden.

## 4.5 Anzeigenerweiterungen (Assets)

Vollständig in `data/anzeigen/assets-erweiterungen.csv`. Übersicht:

| Asset-Typ | Anzahl | Ebene | Status |
|---|---|---|---|
| Sitelinks | 8 | Konto | Anlegen |
| Callouts (Snippets) | 8 | Konto | Anlegen |
| Strukturierte Snippets „Dienstleistungen" | 3 | Konto | Anlegen |
| Anruf-Asset | 1 | Konto | Anlegen – nur zu Bürozeiten einblenden |
| Standort-Asset | 1 | Konto | Setzt verifiziertes Google Business Profile voraus |
| Bild-Assets | 3–5 | Konto | Anlegen |
| Preis-Asset | – | – | **Nicht verwenden** |
| Promotion-Asset | – | – | **Nicht verwenden** |
| Lead-Formular-Asset | – | – | **Nicht empfohlen** |

### Begründung der drei Ausschlüsse

- **Preis-Asset:** Honorarangaben in der Anzeige sind standesrechtlich heikel und
  fachlich kaum seriös darstellbar, weil das Honorar vom Streitwert abhängt.
- **Promotion-Asset:** Rabattwerbung („20 % im September") ist mit dem Ansehen des
  Standes nicht vereinbar.
- **Lead-Formular-Asset:** Das Formular wird direkt in der Google-Oberfläche ausgefüllt.
  Die Anfragequalität ist erfahrungsgemäß deutlich schlechter als bei einem Formular auf
  der eigenen Seite – und bei anwaltlichen Anfragen ist es datenschutzrechtlich
  ungünstig, wenn potenziell sensible Angaben über die Anzeigenplattform laufen.

### Hinweis zu den Bild-Assets

Verwenden Sie Aufnahmen der eigenen Kanzleiräume und ein Portrait. **Keine Stockfotos mit
Richterhammer** – der Gavel ist ein Symbol aus dem angloamerikanischen Rechtsraum und
kommt an österreichischen Gerichten nicht vor. Ebenso wenig Justitia-Statuen und
Paragrafenzeichen; das wirkt austauschbar und senkt die Wiedererkennung.

## 4.6 Anzeigentest-Verfahren

| Zeitraum | Vorgehen |
|---|---|
| Monat 1–2 | Nichts ändern. Daten sammeln. Änderungen setzen die Lernphase zurück. |
| Ab Monat 3 | Assets mit Bewertung „Niedrig" in der Asset-Detailansicht durch neue Varianten ersetzen – **einzeln**, nicht alle gleichzeitig |
| Ab Monat 4 | Zweite RSA je Anzeigengruppe für die stärksten drei Anzeigengruppen |
| Laufend | Anzeigeneffektivität mindestens „Gut" anstreben; „Ausgezeichnet" ist kein Selbstzweck, wenn es nur durch generische Zusatztexte erreicht wird |

**Wichtig:** Die Kennzahl „Anzeigeneffektivität" ist eine Empfehlung von Google, kein
Qualitätsurteil. Eine Anzeige mit Bewertung „Gut" und niedrigem CPA ist besser als eine
mit „Ausgezeichnet" und hohem CPA. Im Zweifel entscheidet der CPA.
