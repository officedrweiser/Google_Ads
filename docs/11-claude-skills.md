# 11 – Welche Claude-Skills bei diesem Projekt helfen

## 11.1 Die ehrliche Vorabantwort

**Einen fertigen „Google Ads"-Skill gibt es nicht.** Ich habe die für Ihr Konto
freigeschalteten Skills und den Skill-Katalog nach den Stichwörtern *Google Ads, PPC,
Kampagne, Marketingstrategie, Keyword-Recherche, SEO, Werbetexte, Kanzlei* durchsucht –
ohne Treffer.

Das ist keine schlechte Nachricht. Skills sind kein Katalog fertiger Produkte, sondern
wiederverwendbare Arbeitsanweisungen. Der eigentliche Hebel liegt darin, aus diesem Plan
**eigene Kanzlei-Skills zu bauen** (Abschnitt 11.3). Die vorhandenen Skills sind dabei
das Werkzeug für die Ergebnisse, nicht für die Kampagnenarbeit selbst.

## 11.2 Vorhandene Skills und ihr Nutzen hier

### Bereits für Ihr Konto freigeschaltet

| Skill | Wofür in diesem Projekt |
|---|---|
| **`xlsx`** | Keyword- und Budgetdateien als Excel; Monatsreporting mit Formeln und Diagrammen; CPA-Rechenmodell je Rechtsgebiet; Aufbereitung von Google-Ads-Exporten |
| **`docx`** | Monatsbericht als Word-Dokument mit Kanzleikopf; Strategiepapier für interne Abstimmung; Briefing an eine Agentur |
| **`pptx`** | Präsentation der Strategie – etwa wenn der Plan im Kanzleiteam oder gegenüber einem Dienstleister vorgestellt wird |
| **`pdf`** | Google-Ads-Berichte, die nur als PDF vorliegen, auslesen und auswerten; den fertigen Plan als PDF ausgeben |
| **`skill-creator`** | **Der wichtigste – siehe Abschnitt 11.3** |

### In Claude Code zusätzlich verfügbar

| Skill / Funktion | Wofür in diesem Projekt |
|---|---|
| **`dataviz`** | Diagramme für den Monatsbericht: CPA-Entwicklung je Rechtsgebiet, Budgetverteilung, Anfragen im Zeitverlauf – konsistent gestaltet und in hellem wie dunklem Modus lesbar |
| **Artifacts** | Der Kampagnenplan als teilbare Webseite mit eigener Adresse. Wird das Dokument aktualisiert, bleibt der Link derselbe. Geeignet auch für ein laufendes Kennzahlen-Dashboard. |
| **`/loop`** | Wiederkehrende Aufgaben in festem Intervall, z. B. ein wöchentlicher Erinnerungslauf für den Suchbegriffbericht |
| **`code-review`** | Prüfung der Tracking-Einbindung (GTM-Container, Formularcode, GCLID-Feld) auf Fehler |
| **Web-Suche** | Wettbewerbsrecherche, aktuelle Google-Ads-Änderungen, Prüfung standesrechtlicher Fragen |

### Was hier bewusst nicht empfohlen wird

| Verfügbar, aber ungeeignet | Grund |
|---|---|
| **Higgsfield** (Bild-/Videogenerierung) | Für Anzeigenbilder einer Kanzlei ungeeignet. Ein KI-erzeugtes Bild von „Kanzleiräumen", die es so nicht gibt, wäre irreführend – standesrechtlich wie lauterkeitsrechtlich. Verwenden Sie echte Aufnahmen Ihrer Kanzlei (Doc 04, Abschnitt 4.5). Für rein abstrakte Grafiken auf der Website wäre es denkbar, für Anzeigen-Assets nicht. |
| **`design`** | Für Landingpage-Entwürfe grundsätzlich nutzbar; die Seiten müssen aber ohnehin ins bestehende CMS von drweiser.at, daher ist ein Briefing (Doc 05) der direktere Weg. |

## 11.3 Der eigentliche Hebel: eigene Kanzlei-Skills bauen

Mit **`skill-creator`** lässt sich dieser Plan in wiederverwendbare Arbeitsanweisungen
überführen. Der Unterschied: Statt bei jeder Auswertung neu zu erklären, worauf es
ankommt, ruft man den Skill auf – und er kennt Ihre Rechtsgebiete, Ihre CPA-Ziele und die
Grenzen des Standesrechts bereits.

### Drei Skills, die sich hier lohnen

**1. `kanzlei-ads-monatscheck`**
Führt die Monatsroutine aus Doc 09 aus: Google-Ads-Export einlesen, CPA je Rechtsgebiet
berechnen, mit dem Deckungsbeitrag abgleichen, Budgetumschichtung nach der Regel aus
Doc 07 vorschlagen und den Monatsbericht als Word-Dokument ausgeben.
*Ersparnis: rund 90 Minuten Handarbeit pro Monat.*

**2. `kanzlei-anzeigentext`**
Erzeugt neue Anzeigentitel und Beschreibungen für eine Anzeigengruppe – mit den
Zeichengrenzen, dem Kanzleiprofil und dem Wortfilter aus `tools/pruefe_anzeigen.py`
bereits eingebaut. Damit entstehen keine Texte mehr, die nachträglich am Standesrecht
scheitern.

**3. `kanzlei-negativliste`**
Nimmt einen Suchbegriff-Export entgegen, ordnet jeden Begriff einer der sieben Listen zu
und schlägt die Ausschlüsse in der richtigen Match-Type-Variante vor – inklusive Warnung,
wenn ein Ausschluss zu breit wäre und relevante Suchanfragen mitblockieren würde.
*Das ist die wöchentliche Hauptarbeit der ersten acht Wochen.*

### So gehen Sie vor

```
/skill-creator
```

und beschreiben, welche Routine automatisiert werden soll. Der Skill fragt das Nötige ab
und legt die Anweisung an. Als Grundlage kann er direkt auf die Dokumente in diesem
Repository verweisen – die fachlichen Regeln stehen bereits geschrieben.

## 11.4 Was in diesem Projekt konkret schon eingesetzt wurde

| Mittel | Ergebnis |
|---|---|
| Web-Suche | Kanzleiprofil, Standort und Schwerpunkte recherchiert; CPC-Benchmarks für Rechtsdienstleistungen in Österreich; RL-BA 2015 § 47 Abs 3 im Wortlaut; FlexKapG als Nischenchance identifiziert |
| Eigenes Prüfskript | `tools/pruefe_anzeigen.py` – 449 Anzeigen-Assets auf Zeichengrenzen, Duplikate, Google-Formatregeln und Standesrecht geprüft, 0 Beanstandungen |
| Datenbereinigung | 212 Keywords auf korrekte Umlautschreibweise normalisiert und auf Dubletten geprüft |
| Artifact | Der Gesamtplan als teilbare Webseite |

## 11.5 Ergänzung außerhalb der Skills: Connectors

Skills sind Arbeitsanweisungen. Der Zugriff auf Ihre echten Kampagnendaten läuft über
**Connectors** – das ist die andere Hälfte der Automatisierung.

Ein Connector zu Google Ads oder Google Sheets würde bedeuten, dass die Monatsauswertung
nicht mehr über manuelle Exporte läuft, sondern direkt auf den Kontodaten arbeitet. In der
aktuellen Sitzung ist kein solcher Connector verbunden. Falls Sie das anstreben, ist der
pragmatische Zwischenschritt:

1. Google Ads liefert geplante Berichte automatisch per E-Mail oder in Google Sheets
2. Der Skill `kanzlei-ads-monatscheck` verarbeitet diesen Export
3. Ergebnis ist der fertige Monatsbericht

Das kommt ohne API-Anbindung aus und deckt den praktischen Bedarf einer Einzelkanzlei ab.

## 11.6 Kurzfassung

| Frage | Antwort |
|---|---|
| Gibt es einen fertigen Google-Ads-Skill? | Nein |
| Was hilft trotzdem sofort? | `xlsx`, `docx`, `pptx`, `pdf`, `dataviz`, Artifacts |
| Wo liegt der eigentliche Hebel? | `skill-creator` – eigene Kanzlei-Skills aus diesem Plan |
| Was ist die lohnendste erste Automatisierung? | `kanzlei-negativliste` (wöchentlich) und `kanzlei-ads-monatscheck` (monatlich) |
| Wovon ist abzuraten? | KI-generierte Bilder als Anzeigen-Assets |
