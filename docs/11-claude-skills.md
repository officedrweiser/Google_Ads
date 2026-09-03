# 11 – Welche Claude-Skills bei diesem Projekt helfen

## 11.1 Die Ausgangslage

Im offiziellen Skill-Katalog von Anthropic gibt es **keinen Google-Ads-Skill**. Die
dortigen Skills (`xlsx`, `docx`, `pdf`, …) erzeugen Ergebnisse – Tabellen, Berichte,
Präsentationen –, sie leisten aber keine Kampagnenarbeit.

Diese Lücke schließt eine freie Bibliothek: **[marketingskills](https://github.com/coreyhaines31/marketingskills)**
von Corey Haines, 50 Marketing-Skills unter MIT-Lizenz, darunter ein ausgearbeiteter
`ads`-Skill mit eigenem Google-Ads-Audit-Katalog und einer Spezifikation für
RSA-Anzeigentexte. Sie ist in diesem Repository unter `.claude/skills/` installiert und
steht damit in jeder Claude-Sitzung zur Verfügung, die dieses Projekt geöffnet hat
(Abschnitt 11.2).

Der eigentliche Hebel bleibt daneben unverändert: aus diesem Plan **eigene Kanzlei-Skills
zu bauen** (Abschnitt 11.3). Die fremde Bibliothek kennt Ihre Rechtsgebiete, Ihre
CPA-Ziele und das österreichische Standesrecht nicht – ein eigener Skill schon.

## 11.2 Vorhandene Skills und ihr Nutzen hier

### Marketing-Skill-Bibliothek im Repository

50 Skills liegen unter `.claude/skills/`, Herkunft und Aktualisierung sind in
`.claude/skills/HERKUNFT.md` beschrieben. Sie werden automatisch erkannt, sobald das
Thema passt – ein Aufruf per `/name` ist möglich, aber nicht nötig. Diese sind hier
einschlägig:

| Skill | Wofür in diesem Projekt |
|---|---|
| **`product-marketing`** | Das Fundament. Legt eine Kontextdatei mit Kanzleiprofil, Zielgruppe und Positionierung an, die alle übrigen Skills zuerst lesen. **Vor der ersten Nutzung einmal ausführen.** |
| **`ads`** | Kampagnenstruktur, Gebote, Zielgruppen, Ausschlüsse, Performance Max. Enthält eine Google-Ads-Audit-Checkliste und eine Formatvorgabe für RSA-Texte – direkt anwendbar auf Doc 02, 03 und 07 |
| **`ad-creative`** | Neue Anzeigentitel und Beschreibungen in Menge erzeugen und durchtesten – die Arbeit hinter `data/anzeigen/` |
| **`cro`** | Landingpages und Kontaktformulare auf Anfragen optimieren (Doc 05) |
| **`copywriting`** / **`copy-editing`** | Seitentexte schreiben und überarbeiten; bestehende Anzeigentexte nachschärfen |
| **`analytics`** | Ereignis- und Conversion-Messung sauber aufsetzen (Doc 06) |
| **`attribution`** | Beurteilen, welcher Kanal ein Mandat tatsächlich ausgelöst hat – bei langen Entscheidungswegen im Familien- und Erbrecht der Knackpunkt |
| **`ab-testing`** | Anzeigen- und Seitentests planen, ohne sich Ergebnisse einzubilden, die statistisch nicht tragen |
| **`seo-audit`**, **`schema`**, **`site-architecture`** | Website drweiser.at: technische Prüfung, `Attorney`-/`LegalService`-Auszeichnung, Seitenstruktur je Rechtsgebiet |
| **`ai-seo`** | Auffindbarkeit in KI-Antworten – wachsender Anteil der Erstrecherche bei Rechtsfragen |
| **`competitors`**, **`competitor-profiling`** | Mitbewerberkanzleien in 1030/1010 Wien einordnen |
| **`customer-research`** | Mandantengespräche auswerten; liefert die Sprache, die in Anzeigen wirklich funktioniert |
| **`marketing-psychology`** | Vertrauensaufbau bei einer Entscheidung, die Menschen ungern treffen |
| **`marketing-plan`** | Gesamtplan über alle Kanäle, falls die Kanzlei über Google Ads hinausgeht |
| **`public-relations`**, **`events`** | Fachbeiträge, Vorträge, Presseanfragen als Ergänzung zur bezahlten Sichtbarkeit |

**Zwei Einschränkungen, die Sie kennen müssen:**

1. **Die Skills sind für SaaS-Produkte geschrieben, nicht für Kanzleien.** Rund die Hälfte
   (`paywalls`, `onboarding`, `churn-prevention`, `referrals`, `aso`, `free-tools`,
   `programmatic-seo`, `community-marketing`) trifft auf eine Einzelkanzlei nicht zu.
   `referrals` ist darüber hinaus heikel: Provisionen für Mandatsvermittlung sind
   standesrechtlich unzulässig.
2. **Sie kennen das österreichische Standesrecht nicht.** Alles, was aus diesen Skills an
   Anzeigen- oder Seitentexten kommt, geht durch **Doc 08 (RL-BA 2015)** und durch
   `python3 tools/pruefe_anzeigen.py`. Im Zweifel gilt Doc 08, nicht der Skill.

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
| Gibt es einen fertigen Google-Ads-Skill? | Im Anthropic-Katalog nein, in der Bibliothek `marketingskills` ja (`ads`) |
| Was hilft sofort? | `ads`, `ad-creative`, `cro`, `analytics`, `attribution` aus der Bibliothek; `xlsx`, `docx`, `pptx`, `pdf`, `dataviz`, Artifacts für die Ergebnisse |
| Wo liegt der eigentliche Hebel? | `skill-creator` – eigene Kanzlei-Skills aus diesem Plan |
| Was ist die lohnendste erste Automatisierung? | `kanzlei-negativliste` (wöchentlich) und `kanzlei-ads-monatscheck` (monatlich) |
| Wovon ist abzuraten? | KI-generierte Bilder als Anzeigen-Assets; Skill-Ausgaben ohne Prüfung nach Doc 08 übernehmen |
