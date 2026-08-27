# 08 – Standesrecht-Compliance (RL-BA 2015)

> Dieses Dokument fasst die für Google Ads relevanten Werberegeln zusammen. Es ist eine
> Arbeitsgrundlage für die Kampagnenarbeit, keine Rechtsauskunft – die Beurteilung im
> Einzelfall obliegt selbstverständlich der Kanzlei. Maßgeblich sind der Gesetzestext und
> die jeweils geltende Fassung der Richtlinien.

## 8.1 Die Grundnorm

**§ 10 Abs 5 RAO:** Dem Rechtsanwalt ist Werbung insoweit gestattet, als sie über seine
berufliche Tätigkeit wahr und sachlich informiert und mit den Berufspflichten im Einklang steht.

**RL-BA 2015:** Werbung ist zulässig, wenn sie wahr und sachlich ist und mit Ehre und
Ansehen des Standes, den Berufspflichten und der Funktion des Rechtsanwalts in der
Rechtspflege vereinbar ist.

Für Google Ads bedeutet das: **Fakten dürfen genannt werden, Wertungen nicht.**

| Zulässig (Tatsache) | Unzulässig (Wertung/Anpreisung) |
|---|---|
| „Rechtsanwalt in Wien seit 1990" | „Die erfahrenste Kanzlei Wiens" |
| „Schwerpunkt Erbrecht" | „Der Erbrechts-Experte Wiens" |
| „Kanzlei in 1030 Wien, U3 Rochusgasse" | „Die beste Adresse für Ihre Scheidung" |
| „Wir besprechen das Honorar vorab" | „Günstiger als jede andere Kanzlei" |

## 8.2 Der Katalog unzulässiger Werbung (§ 47 Abs 3 RL-BA 2015)

Ausdrücklich unzulässig sind insbesondere:

| lit | Verbot | Bedeutung für Google Ads |
|---|---|---|
| **a** | Selbstanpreisung durch marktschreierische Werbung | Keine Superlative, keine reißerischen Formulierungen, keine Rabattlogik |
| **b** | Vergleichende Werbung gegen Berufskollegen | Keine Vergleiche im Anzeigentext; auch kein Bieten auf Kanzleinamen von Kollegen |
| **c** | Mandatsakquisition unter Ausnützung einer Zwangslage | Keine Ausrichtung auf akute Notlagen mit Druckformulierungen |
| **d** | Weitergabe von Vollmachtsformularen an Dritte zur Verteilung | Keine Vollmachtsdownloads über Werbekanäle |
| **e** | Nennung von Mandanten ohne deren Zustimmung | Keine Referenzen, keine Fallbeispiele mit erkennbaren Personen |
| **f** | Gewährung von Vorteilen für Mandatsvermittlung | **Keine Lead-Portale mit Provision je vermitteltem Mandat** |
| **g** | Hinweis auf Erfolgs- oder Umsatzzahlen | Keine Erfolgsquoten, keine „500 gewonnene Verfahren", keine Umsatzangaben |

### Die zwei Punkte mit der größten praktischen Sprengkraft

**lit f – Provisionen für Mandatsvermittlung.** Das betrifft nicht Google Ads selbst
(Google wird für Klicks bezahlt, nicht für Mandate), wohl aber viele Anwaltsportale und
Lead-Generatoren, die pro vermitteltem Mandat abrechnen. Vor jeder Zusammenarbeit mit
einem Lead-Anbieter ist das Abrechnungsmodell zu prüfen: **Klickvergütung ja, Erfolgs-
oder Mandatsprovision nein.**

**lit g – Erfolgszahlen.** Genau das, was in der Onlinewerbung üblicherweise als
Vertrauensbeleg eingesetzt wird („98 % Erfolgsquote", „über 2.000 Mandate"), ist hier
untersagt. Der Ersatz sind sachliche Angaben: Bestehen seit 1990, Tätigkeitsschwerpunkte,
Standort, Erreichbarkeit.

## 8.3 Weitere relevante Grenzen

### Quota litis (§ 879 Abs 2 Z 2 ABGB)

Die Vereinbarung eines Anteils am Streitgegenstand als Honorar ist nichtig. Ein
Erfolgshonorar in Form eines pauschalen Zuschlags ist demgegenüber zulässig.

Für die Anzeigentexte heißt das: Formulierungen wie **„Nur zahlen, wenn wir gewinnen"**
oder **„Kein Erfolg, keine Kosten"** dürfen nicht verwendet werden.

### Fachanwaltstitel

In Österreich gibt es **keine** Fachanwaltstitel (anders als in Deutschland). Die Angabe
„Fachanwalt für Familienrecht" wäre irreführend und zugleich ein UWG-Risiko.

Als **Keyword** ist der Begriff dennoch gebucht – Menschen suchen so, weil sie deutsche
Werbung kennen. Im **Anzeigentext** darf er nicht erscheinen. Das Prüfskript
`tools/pruefe_anzeigen.py` blockiert das automatisch.

### UWG

Unabhängig vom Standesrecht gilt das Lauterkeitsrecht: Irreführende Angaben über
Qualifikation, Erfolgsaussichten oder Kosten sind unzulässig. Da Wettbewerber
klagsbefugt sind, ist das praktisch das schärfere Schwert.

## 8.4 Automatische Prüfung

`tools/pruefe_anzeigen.py` prüft jeden Anzeigentext gegen einen Wortfilter:

| Auslöser | Zugeordneter Grund |
|---|---|
| beste/r/n, Nr. 1, führend, Marktführer, Top-Kanzlei | § 47 Abs 3 lit a |
| besser als, günstiger als | § 47 Abs 3 lit b |
| Erfolgsquote, Erfolgsrate, „x % Erfolg", gewonnene Verfahren, „x Mandate" | § 47 Abs 3 lit g |
| garantiert, Garantie, 100 % sicher | Erfolgsversprechen, UWG |
| nur bei Erfolg, kein Erfolg keine Kosten | § 879 Abs 2 Z 2 ABGB |
| Fachanwalt | Titel existiert in Österreich nicht |
| Spezialist, Experte | Suggeriert formale Qualifikation |
| billig, Schnäppchen | § 47 Abs 3 lit a |

```bash
python3 tools/pruefe_anzeigen.py
```

Aktueller Stand: **449 Assets geprüft, 0 Beanstandungen.**

Der Filter ist eine Vorprüfung, kein Freibrief. Neue Formulierungen sollten weiterhin
inhaltlich beurteilt werden – der Filter erkennt nur bekannte Muster.

## 8.5 Prüfliste vor der Freigabe neuer Texte

- [ ] Enthält der Text ausschließlich überprüfbare Tatsachen?
- [ ] Kommt kein Superlativ und keine Bewertung vor?
- [ ] Wird kein Kollege und keine andere Kanzlei erwähnt oder angedeutet?
- [ ] Keine Erfolgs-, Quoten- oder Umsatzangaben?
- [ ] Kein Erfolgshonorar-Versprechen?
- [ ] Kein Mandantenname, kein Fallbeispiel mit erkennbaren Personen?
- [ ] Keine Formulierung, die Druck auf Menschen in einer Notlage ausübt?
- [ ] Stimmt jede Serviceaussage tatsächlich? („Termin nach Vereinbarung" nur, wenn das
      auch eingehalten wird)
- [ ] `python3 tools/pruefe_anzeigen.py` ohne Fehler durchgelaufen?

## 8.6 Zusätzliche Google-Ads-Vorgaben

Neben dem Standesrecht gelten Googles eigene Richtlinien:

| Vorgabe | Status |
|---|---|
| EU-Werbetreibenden-Verifizierung (DSA) | **Muss vor dem Start abgeschlossen sein** – sonst werden Anzeigen ausgesetzt |
| Identitätsprüfung des Werbetreibenden | Erforderlich, Nachweis über Firmenbuch/Kammereintrag |
| Zielseite muss Impressum und Datenschutzerklärung enthalten | Erfüllt, sofern aktuell |
| Keine irreführenden Angaben | deckungsgleich mit UWG |
| Interpunktion: kein Ausrufezeichen im Anzeigentitel, höchstens eines je Anzeige | Vom Prüfskript abgedeckt |
| Keine Großbuchstaben-Blöcke („JETZT ANRUFEN") | Vom Prüfskript abgedeckt |

Die EU-Verifizierung ist der Punkt, an dem Kampagnen am häufigsten scheitern, bevor sie
begonnen haben: Sie dauert einige Werktage und wird oft erst bemerkt, wenn die Anzeigen
bereits pausiert sind. Deshalb steht sie in Doc 10 auf Tag 1.

## 8.7 Quellen

- § 10 Abs 5 RAO (Rechtsanwaltsordnung) – Werbebefugnis
- RL-BA 2015, insbesondere § 47 – Werbung, Abs 3 Katalog unzulässiger Werbung
- § 879 Abs 2 Z 2 ABGB – Quota-litis-Verbot
- § 9 RAO – Verschwiegenheitspflicht (relevant für Formulare und Tracking, siehe Doc 06)
- UWG – irreführende Geschäftspraktiken
- Google-Ads-Richtlinien zu Werbetreibenden-Verifizierung und Anzeigenformat

Die jeweils geltende Fassung der RL-BA 2015 wird vom Österreichischen
Rechtsanwaltskammertag (oerak.at) und von der Rechtsanwaltskammer Wien (rakwien.at)
veröffentlicht.
