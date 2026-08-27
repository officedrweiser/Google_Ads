# 06 – Conversion-Tracking & DSGVO

## 6.1 Warum das der wichtigste technische Schritt ist

Ohne Conversion-Tracking optimiert Google auf Klicks. Mit Conversion-Tracking optimiert
Google auf Anfragen. Der Unterschied im Ergebnis ist größer als jede Keyword- oder
Textoptimierung.

**Reihenfolge ist zwingend:** Tracking zuerst, Kampagne danach. Eine Kampagne, die vier
Wochen ohne Messung läuft, hat vier Wochen Budget verbraucht, ohne etwas zu lernen.

## 6.2 Technischer Aufbau

```
Google Tag Manager (GTM)
   ├─ Consent-Management-Plattform (CMP), lädt zuerst
   ├─ Google-Tag (gtag) → Google Ads + Google Analytics 4
   ├─ Consent Mode v2 (advanced)
   └─ Ereignis-Trigger für alle Conversion-Aktionen
```

Einzelne Bausteine:

| Baustein | Empfehlung | Kosten |
|---|---|---|
| Tag-Verwaltung | Google Tag Manager | kostenlos |
| Analyse | Google Analytics 4, verknüpft mit Google Ads | kostenlos |
| Einwilligung | Cookiebot, Usercentrics oder CCM19 | 15–50 €/Monat |
| Anrufmessung | Google-Anrufweiterleitungsnummer | kostenlos |

## 6.3 Die Conversion-Aktionen

| # | Aktion | Kategorie | Wertung | Primär? | Zählung |
|---|---|---|---|---|---|
| 1 | Anruf über die Anzeige (≥ 60 s) | Anruf über Anzeigen | 100 | **ja** | Jede |
| 2 | Anruf von der Website (≥ 60 s) | Anruf von Website | 100 | **ja** | Jede |
| 3 | Formular abgeschickt | Kontaktdaten übermittelt | 80 | **ja** | Eine |
| 4 | Online-Termin gebucht | Termin | 120 | **ja** | Jede |
| 5 | Klick auf E-Mail-Adresse | Kontaktdaten übermittelt | 20 | nein | Eine |
| 6 | Klick auf WhatsApp/Chat | Interaktion | 20 | nein | Eine |
| 7 | Verweildauer > 90 s auf Rechtsgebietsseite | Seitenaufruf | 5 | nein | Eine |
| 8 | **Mandat erteilt** (Offline-Import) | Qualifizierter Lead | echter Wert | **ja**, ab Phase 3 | Eine |

**Nur die als „primär" markierten Aktionen dürfen in die Gebotsoptimierung einfließen.**
Wer E-Mail-Klicks als primäre Conversion mitzählt, trainiert Google darauf, Menschen zu
liefern, die auf eine E-Mail-Adresse klicken – nicht solche, die anrufen.

### Zur Mindestdauer bei Anrufen

Die 60-Sekunden-Schwelle filtert Fehlanrufe und Werbeanrufe heraus. Bei einer Kanzlei ist
90 Sekunden oft die bessere Schwelle, weil ein echtes Erstgespräch nie kürzer ist. Beginnen
Sie mit 60 s und erhöhen Sie, wenn die Anrufberichte zu viele Kurzanrufe zeigen.

## 6.4 Conversion-Werte – warum sie gesetzt werden

Auch ohne echten Umsatz je Anfrage sollten Sie die Conversions gewichten (Spalte
„Wertung" oben). Damit lernt Google, dass eine Terminbuchung mehr wert ist als ein
Formularabsenden.

Der eigentliche Zweck: Ab Phase 3 lässt sich damit auf **Ziel-ROAS** umstellen, sobald über
den Offline-Import echte Mandatswerte zurückfließen. Wer die Werte erst dann einführt,
verliert die gesamte Historie.

## 6.5 Enhanced Conversions für Leads

**Dringend empfohlen.** Dabei werden die vom Nutzer eingegebenen Kontaktdaten (E-Mail,
Telefonnummer) im Browser mit SHA-256 gehasht und in gehashter Form an Google übermittelt.
Der Klartext verlässt die Seite nicht.

Nutzen: deutlich vollständigere Zuordnung von Anfragen zu Klicks – gerade in Browsern, die
Cookies einschränken. Ohne Enhanced Conversions gehen erfahrungsgemäß spürbar viele
Conversions in der Messung verloren, was die Gebotsautomatik systematisch fehlleitet.

Voraussetzung: Hinweis in der Datenschutzerklärung und Einwilligung über die CMP.

## 6.6 Offline-Conversion-Import – der eigentliche Hebel

Das ist der Unterschied zwischen einer durchschnittlichen und einer wirklich
wirtschaftlichen Kanzlei-Kampagne.

**Das Problem:** Google weiß, welcher Klick zu einer Anfrage geführt hat. Google weiß
nicht, welche Anfrage zu einem **Mandat** geführt hat. Also optimiert Google auf Anfragen –
auch auf solche, aus denen nie ein Mandat wird.

**Die Lösung:**

```
1  Beim Klick auf die Anzeige hängt Google die GCLID an die URL
2  Ein verstecktes Formularfeld speichert die GCLID mit ab
3  Die GCLID wandert in Ihre Mandantenverwaltung / eine Tabelle
4  Wird ein Mandat erteilt, wird die GCLID mit dem Wert des Mandats
   nach Google Ads zurückgespielt (Datei-Upload oder automatisiert)
5  Google lernt: Diese Art von Klick führt zu Mandaten – und bietet dort mehr
```

Aufwand: ein zusätzliches Formularfeld, eine Spalte in der Mandantenerfassung und ein
monatlicher CSV-Upload. Wirkung: Google optimiert auf Mandate statt auf Anfragen.

Realistischer Startzeitpunkt: **ab Monat 4**, wenn genug Mandate zugeordnet werden können.
Vorbereitet werden muss es aber **ab Tag 1** – die GCLID muss von Anfang an mitgespeichert
werden, sonst fehlt später die Historie.

> **Datenschutz-Hinweis:** Die GCLID ist eine Klick-Kennung, kein Klarname. Der Upload
> enthält nur GCLID, Conversion-Name, Zeitstempel und Wert – keine Mandantendaten,
> keine Sachverhaltsangaben. Damit ist die anwaltliche Verschwiegenheit gewahrt. Der
> Vorgang ist in der Datenschutzerklärung und im Verarbeitungsverzeichnis zu erfassen.

## 6.7 Consent Mode v2 – seit März 2024 verpflichtend

Ohne korrekt eingerichteten Consent Mode v2 stellt Google für Nutzer im EWR keine
personalisierten Funktionen und keine Remarketing-Zielgruppen mehr bereit – und die
Conversion-Modellierung greift nicht.

Vier Signale müssen gesetzt werden:

| Signal | Bedeutung |
|---|---|
| `ad_storage` | Speicherung für Werbezwecke |
| `analytics_storage` | Speicherung für Analysezwecke |
| `ad_user_data` | Übermittlung von Nutzerdaten an Google für Werbezwecke |
| `ad_personalization` | Personalisierte Werbung |

**Advanced-Modus verwenden, nicht Basic.** Im Advanced-Modus werden ohne Einwilligung
anonyme, cookielose Signale gesendet, aus denen Google die fehlenden Conversions
modelliert. Im Basic-Modus wird gar nichts gesendet – die Datenlücke bleibt offen und
die Gebotsautomatik arbeitet auf unvollständiger Grundlage.

Prüfung nach der Einrichtung:
- Google Tag Assistant: Werden vor der Einwilligung `denied`-Signale gesendet?
- Google Ads → Einstellungen → Einwilligungseinstellungen: Wird der Status „aktiv" angezeigt?

## 6.8 DSGVO-Pflichten der Kanzlei

| Pflicht | Umsetzung |
|---|---|
| Rechtsgrundlage | Einwilligung nach Art 6 Abs 1 lit a DSGVO über die CMP |
| Auftragsverarbeitung | Google-Datenverarbeitungsbedingungen im Ads-Konto akzeptieren |
| Datenschutzerklärung | Google Ads, GA4, Consent-Tool, Enhanced Conversions und Offline-Import ausdrücklich benennen |
| Verarbeitungsverzeichnis | Verarbeitungstätigkeit „Websiteanalyse und Onlinewerbung" ergänzen |
| Drittlandtransfer | Hinweis auf EU-US Data Privacy Framework; Google LLC ist zertifiziert |
| Speicherdauer | In GA4 auf 14 Monate begrenzen |
| Betroffenenrechte | Widerruf der Einwilligung jederzeit möglich – Link im Footer |
| Verschwiegenheit (§ 9 RAO) | Keine Sachverhaltsdaten in Formularen, Analytics oder Uploads |

### Der Punkt, der bei Kanzleien besonders zählt

Die anwaltliche Verschwiegenheit geht über die DSGVO hinaus. Bereits die Tatsache, **dass**
eine bestimmte Person Kontakt aufgenommen hat, ist schutzwürdig. Deshalb:

- Keine Sachverhaltsschilderung im Formular (siehe Doc 05)
- Keine Übermittlung von Namen an Google – Enhanced Conversions übermitteln nur Hashwerte
- Keine Bildschirmaufzeichnungs-Tools (Hotjar, Clarity o. Ä.) auf Formularseiten
- Im Offline-Import ausschließlich GCLID und Wert, niemals Mandantendaten

## 6.9 Einrichtungsreihenfolge

```
1   Google-Ads-Konto: EU-Werbetreibenden-Verifizierung abschließen
2   Google Tag Manager auf drweiser.at einbinden
3   Consent-Management-Plattform installieren, Consent Mode v2 (advanced) konfigurieren
4   Google Analytics 4 einrichten, mit Google Ads verknüpfen
5   Conversion-Aktionen 1–7 in Google Ads anlegen
6   Trigger im GTM einrichten und im Vorschaumodus testen
7   Enhanced Conversions für Leads aktivieren
8   Anrufweiterleitungsnummer aktivieren, Mindestdauer 60 s
9   Verstecktes GCLID-Feld ins Formular einbauen
10  Testanfrage absenden und in Google Ads verifizieren
11  ERST DANN: Kampagnen aktivieren
```

Schritt 10 wird oft übersprungen. Er ist der wichtigste: Eine Testanfrage über eine echte
Anzeige (Kampagne kurz aktivieren, selbst suchen, klicken, Formular absenden) beweist die
gesamte Kette. Alles andere ist Vermutung.
