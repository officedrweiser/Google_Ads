# 14 – Was ich vom laufenden Konto brauche

Seit einigen Monaten laufen bereits Anzeigen. Damit gibt es echte Zahlen – und die sind
jeder Planungsannahme überlegen. Dieses Dokument sagt, welche Exporte am meisten bewirken
und wie sie erzeugt werden.

## Warum das so viel ändert

Der Plan rechnet an mehreren Stellen mit **Branchen-Benchmarks**, weil nichts Besseres
vorlag. Jeder dieser Werte lässt sich durch Ihre echten Zahlen ersetzen:

| Bisher im Plan | Wird ersetzt durch |
|---|---|
| Geschätzte Klickpreise je Rechtsgebiet (Doc 01) | Ihre tatsächlichen CPCs |
| Angenommene Conversion-Rate von 5–8 % | Ihre gemessene Rate |
| Geschätzter CPA je Rechtsgebiet | Ihr realer CPA – und damit die ganze Priorisierung |
| Vermutete Ausschluss-Keywords (Doc 03) | Suchbegriffe, die tatsächlich Geld gekostet haben |
| Angenommene Nachfrageverteilung nach Stunden (Doc 12) | Ihr Bericht „Stunde und Wochentag" |
| Startstufe der Gebotsstrategie (Doc 07) | Ihre Conversion-Zahl der letzten 30 Tage |

**Die wichtigste Folge:** Die Wirtschaftlichkeitstabelle in Doc 01 entscheidet über die
gesamte Budgetverteilung. Sie beruht derzeit auf Annahmen. Mit Ihren Zahlen wird daraus
eine belastbare Entscheidung.

## So exportieren Sie

Der Weg ist bei allen Berichten gleich:

```
1  Google Ads öffnen
2  Zeitraum oben rechts  →  "Letzte 90 Tage"
3  Spalten-Symbol (Säulen)  →  "Spalten anpassen"  →  benötigte Spalten anhaken
4  Download-Symbol (Pfeil nach unten, rechts oben über der Tabelle)  →  ".csv"
```

Die CSV-Dateien dann **hier im Chat anhängen**. Screenshots gehen auch, sind aber weniger
auswertbar – aus einer CSV kann ich rechnen, aus einem Bild nur ablesen.

> **Vor dem Teilen kurz durchsehen:** Suchbegriffberichte enthalten, was Menschen bei
> Google getippt haben. Sehr selten steht dort ein Name oder etwas Persönliches. Solche
> Zeilen bitte vorher löschen. Für die Auswertung geht dadurch nichts Wesentliches verloren.

## Priorität 1 – die drei wichtigsten Exporte

### 1. Kampagnen-Übersicht, letzte 90 Tage

**Kampagnen → Kampagnen**

Spalten: Kampagne · Status · Kampagnentyp · Gebotsstrategie · Tagesbudget · Kosten ·
Klicks · Impressionen · CTR · Durchschn. CPC · Conversions · Kosten/Conv. ·
Conversion-Rate

*Ändert:* die gesamte Wirtschaftlichkeitsrechnung und den Budgetsplit.

### 2. Suchbegriffbericht, letzte 90 Tage

**Kampagnen → Keywords → Suchbegriffe**, nach **Kosten absteigend** sortieren

Spalten: Suchbegriff · Übereinstimmungstyp · Kosten · Klicks · Impressionen ·
Conversions · Kosten/Conv.

Die Top 200 nach Kosten genügen.

*Ändert:* die Ausschlusslisten – und zeigt Keywords, an die niemand gedacht hat.
**Das ist erfahrungsgemäß der Export mit dem schnellsten Ergebnis.**

### 3. Conversion-Aktionen

**Zielvorhaben → Conversions → Zusammenfassung**

Hier genügt ein **Screenshot**. Wichtig ist die Spalte *Conversion-Aktion für Gebote
verwenden* (Primär / Sekundär) und die Zahl der Conversions.

*Ändert:* mit welcher Gebotsstrategie die neuen Kampagnen starten dürfen – und deckt
den häufigsten Konfigurationsfehler auf (ein Seitenaufruf oder E-Mail-Klick als primäre
Conversion).

## Priorität 2 – wertvoll, aber nicht blockierend

### 4. Stunde und Wochentag

**Berichte → Berichtseditor → Neuer Bericht → Tabelle**
Zeilen: *Wochentag* und *Stunde* · Werte: Klicks, Kosten, Conversions

Falls der Berichtseditor zu umständlich ist, geht auch der einfachere Weg:
**Kampagnen-Tabelle → Segment-Symbol → Zeit → Stunde**, exportieren; danach dasselbe
mit *Wochentag*.

*Ändert:* Doc 12 unmittelbar. Diese Datei als
`data/erreichbarkeit/nachfrage-ist.csv` ablegen – dann rechnet
`tools/baue_werbezeitplan.py` automatisch mit Ihren echten Zahlen statt mit meiner
Annahme. Egal in welchem Format der Export kommt, ich passe das Werkzeug an.

### 5. Keywords mit Qualitätsfaktor

**Kampagnen → Keywords → Suchkeywords**

Spalten zusätzlich: Qualitätsfaktor · Erwartete CTR · Anzeigenrelevanz ·
Nutzererfahrung mit der Zielseite

*Ändert:* zeigt, welche der 206 geplanten Keywords sich bereits bewährt haben – und wo
der Klickpreis wegen eines schwachen Qualitätsfaktors unnötig hoch ist.

### 6. Geografischer Bericht

**Kampagnen → Einstellungen → Standorte** oder
**Berichte → Vordefinierte Berichte → Standorte → Nutzerstandorte**

*Ändert:* bestätigt oder widerlegt den Zuschnitt Wien + 25 km. Wenn ein nennenswerter
Teil der Kosten aus Deutschland stammt, ist die Standortoption falsch gesetzt – ein
Fehler, der sich sofort auszahlt, wenn man ihn behebt.

### 7. Anzeigengruppen

**Kampagnen → Anzeigengruppen**, Spalten wie bei der Kampagnenübersicht

*Ändert:* verfeinert die Priorisierung innerhalb eines Rechtsgebiets.

## Priorität 3 – wenn ohnehin schon Exporte laufen

| Export | Wo | Nutzen |
|---|---|---|
| Bestehende Ausschlusslisten | Tools → Gemeinsam genutzte Bibliothek → Ausschlusslisten | Abgleich mit `data/negativlisten/` – Vorhandenes ist aus echten Daten gewachsen |
| Anzeigen mit Anzeigeneffektivität | Kampagnen → Anzeigen | Zeigt, welche Textbausteine bereits funktionieren |
| Assets nach Bewertung | Kampagnen → Assets | Welche Sitelinks und Snippets ziehen |
| Abrechnungsübersicht | Abrechnung → Zusammenfassung | Tatsächlicher Monatsverbrauch gegenüber Plan |

## Was ich damit mache

1. **Doc 01 neu rechnen** – echte CPC, Conversion-Rate und CPA je Rechtsgebiet
2. **Budgetsplit neu bestimmen** – nach realem CPA statt nach Annahme
3. **Ausschlusslisten erweitern** – aus dem Suchbegriffbericht, geprüft mit
   `tools/pruefe_negativlisten.py`
4. **Keywordliste abgleichen** – bewährte Begriffe ergänzen, aussichtslose streichen
5. **Startstufe der Gebotsstrategie festlegen** – statt pauschal mit Stufe 1 zu beginnen
6. **Doc 12 neu rechnen** – echte Nachfrageverteilung nach Stunden
7. **Umstellungsplan schärfen** – welche bestehende Kampagne wann pausiert wird (Doc 13, Teil A)

## Wenn nur eine einzige Datei möglich ist

Dann der **Suchbegriffbericht der letzten 90 Tage** (Priorität 1, Nr. 2). Er zeigt in
einer Datei, wofür tatsächlich Geld ausgegeben wurde – und das ist der schnellste Weg zu
einer messbaren Verbesserung.
