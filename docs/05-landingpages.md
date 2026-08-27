# 05 – Landingpages

## 5.1 Der teuerste Fehler: alles auf die Startseite

Wenn alle Anzeigen auf `drweiser.at` verweisen, passiert dreierlei:

1. **Der Qualitätsfaktor sinkt.** Google bewertet die Übereinstimmung zwischen Suchanfrage,
   Anzeige und Zielseite. Eine Startseite, die acht Rechtsgebiete gleichzeitig nennt, ist
   für „Pflichtteil einklagen" wenig relevant. Ein niedriger Qualitätsfaktor bedeutet einen
   höheren Klickpreis für dieselbe Position – bei sonst identischer Kampagne.
2. **Die Conversion-Rate sinkt.** Wer nach „Treuhänder Anwalt Wien" sucht und auf einer
   allgemeinen Kanzleiseite landet, muss selbst suchen. Ein erheblicher Teil tut das nicht.
3. **Die Messung wird unbrauchbar.** Ohne getrennte Seiten lässt sich nicht sagen, welches
   Rechtsgebiet die Anfragen liefert.

Faustregel: Jede Anzeigengruppe braucht eine Zielseite, die den gesuchten Begriff in der
Überschrift trägt.

## 5.2 Seitenstruktur

### Stufe 1 – zwingend vor dem Kampagnenstart (5 Seiten)

| Seite | URL | Für Kampagne |
|---|---|---|
| Scheidung & Familienrecht | `/scheidung` | 2 (alle AG außer Kosten) |
| Kosten einer Scheidung | `/scheidung/kosten` | 2 (AG Kosten Honorar) |
| Erbrecht | `/erbrecht` | 3 (alle AG) |
| Immobilien- & Liegenschaftsrecht | `/immobilienrecht` | 4 (alle AG) |
| Kontakt & Termin | `/kontakt` | Sitelink, alle Kampagnen |

Mit diesen fünf Seiten kann die Kampagne starten. Nicht optimal, aber tragfähig.

### Stufe 2 – bis Ende Monat 2 (7 weitere Seiten)

| Seite | URL |
|---|---|
| Einvernehmliche Scheidung | `/scheidung/einvernehmlich` |
| Unterhalt | `/familienrecht/unterhalt` |
| Obsorge & Kontaktrecht | `/familienrecht/obsorge` |
| Pflichtteil | `/erbrecht/pflichtteil` |
| Testament | `/erbrecht/testament` |
| Kaufvertrag Immobilie | `/immobilienrecht/kaufvertrag` |
| Treuhandabwicklung | `/immobilienrecht/treuhand` |

### Stufe 3 – ab Monat 4, nach Datenlage

Die übrigen Anzeigengruppen erhalten eigene Seiten, sobald sie messbar Anfragen liefern.
Kein Vorratsbau.

## 5.3 Aufbau einer Rechtsgebiets-Landingpage

Die Reihenfolge ist bewusst gewählt: Sie folgt der Frage, die der Suchende gerade hat.

```
1  Überschrift  = der gesuchte Begriff, wörtlich
   Beispiel: "Pflichtteil in Wien durchsetzen – Anwaltliche Vertretung"

2  Ein Absatz Einordnung (max. 3 Sätze)
   Worum es geht, was die Kanzlei dabei tut. Kein Kanzlei-Lebenslauf.

3  Kontaktbereich, direkt sichtbar ohne Scrollen
   - Telefonnummer als klickbarer Link (auf Mobilgeräten entscheidend)
   - Formular mit 4 Feldern: Name, Telefon oder E-Mail, Rechtsgebiet, Rückrufzeit
   - Bürozeiten und Hinweis, wann eine Rückmeldung erfolgt

4  "Womit wir Sie unterstützen" – 4 bis 6 konkrete Punkte
   Beispiel Pflichtteil: Anspruch berechnen, Schenkungen anrechnen,
   Auskunftsanspruch durchsetzen, außergerichtliche Einigung, Klage

5  Ablauf in 3 bis 4 Schritten
   Erstgespräch → Prüfung der Unterlagen → Vorgehensvorschlag mit Kostenrahmen → Umsetzung

6  Kosten – ehrlich und ohne Zahlenversprechen
   Wonach sich das Honorar richtet, wann eine Pauschale möglich ist,
   wie die Kostenvereinbarung zustande kommt.

7  Häufige Fragen – 4 bis 6, mit FAQ-Schema ausgezeichnet
   Fristen, Unterlagen, Dauer, Ablauf

8  Kanzlei-Kurzprofil
   Dr. Martin Weiser, Rechtsanwalt in Wien Landstraße seit 1990.
   Bild der Kanzleiräume, Anfahrt, U3 Rochusgasse.

9  Kontaktbereich wiederholt
```

## 5.4 Anforderungen an das Kontaktformular

**Vier Felder, nicht mehr.** Jedes zusätzliche Pflichtfeld kostet Anfragen.

| Feld | Pflicht | Hinweis |
|---|---|---|
| Name | ja | |
| Telefon **oder** E-Mail | ja | Nicht beides erzwingen |
| Rechtsgebiet | ja | Auswahlliste – dient zugleich der Zuordnung im Reporting |
| Wann erreichbar? | nein | Erhöht die Quote erfolgreicher Rückrufe deutlich |
| Verstecktes Feld: `gclid` | – | Technisch nötig für den Offline-Conversion-Import, siehe Doc 06 |

> **Wichtig – anwaltliche Verschwiegenheit:** Das Formular darf **keinen** großen Freitext
> für die Sachverhaltsschilderung enthalten. Wer dort seine Scheidungsgründe oder den
> Erbstreit schildert, erzeugt Daten, die durch Formular-Software, Mailserver, Analytics
> und CRM laufen. Bei anwaltlichen Anfragen ist das ein unnötiges Risiko – für die Kanzlei
> wie für die anfragende Person. Das Formular dient der **Kontaktaufnahme**, der Sachverhalt
> gehört ins Gespräch. Falls doch ein Freitextfeld gewünscht ist: als optionales Feld mit
> dem ausdrücklichen Hinweis „Bitte hier keine vertraulichen Details – wir rufen Sie zurück."

## 5.5 Technische Anforderungen

| Anforderung | Zielwert | Warum |
|---|---|---|
| Ladezeit (LCP) mobil | < 2,5 s | Google gewichtet die Nutzererfahrung im Qualitätsfaktor |
| Mobile Darstellung | vollständig responsiv | Der überwiegende Teil der Anwaltssuchen erfolgt mobil |
| Telefonnummer | `<a href="tel:+43120510 03">` | Ein Tippen statt Abtippen |
| Formular | ohne Neuladen bestätigen | Klare Dankeseite oder Inline-Bestätigung für das Tracking |
| SSL | durchgehend HTTPS | Voraussetzung für Google Ads |
| Impressum & Datenschutz | von jeder Seite verlinkt | Rechtlich zwingend, wird von Google geprüft |
| Dankeseite | `/danke` mit eigener URL | Ermöglicht sauberes Conversion-Tracking |

## 5.6 Besonderheit: die Seite `/scheidung/kosten`

Diese Seite ist der Grund, warum die Kosten-Keywords überhaupt gebucht werden. Sie muss
tatsächlich beantworten, wonach gesucht wird – sonst ist der Klick verschwendet.

Inhaltliche Gliederung:

1. **Woraus sich die Gesamtkosten zusammensetzen**
   Gerichtsgebühren (Pauschalgebühr für den Scheidungsantrag), Anwaltshonorar,
   allfällige Sachverständigenkosten.
2. **Unterschied einvernehmlich / strittig**
   Warum die einvernehmliche Scheidung planbar ist und die strittige nicht.
3. **Wie das Honorar zustande kommt**
   Nach Aufwand, nach Rechtsanwaltstarifgesetz oder als Pauschale – und dass die
   Grundlage vorab schriftlich vereinbart wird.
4. **Wer die Kosten trägt**
   Aufteilung bei der einvernehmlichen Scheidung, Kostenersatz im streitigen Verfahren.
5. **Verfahrenshilfe**
   Kurzer, sachlicher Hinweis, unter welchen Voraussetzungen sie in Betracht kommt.
   Das wirkt vertrauensbildend und filtert zugleich Anfragen, die ohnehin nicht passen.
6. **Kontaktbereich**

> **Nicht auf diese Seite gehören:** konkrete Eurobeträge als Werbeversprechen
> („Scheidung ab 990 €"). Das ist standesrechtlich heikel und fachlich nicht haltbar, weil
> der Aufwand vom Einzelfall abhängt. Erklären, wonach sich die Kosten richten – nicht,
> was sie kosten.

## 5.7 Zuordnung Anzeigengruppe → Zielseite

Die vollständige Zuordnung steht in Doc 02, Abschnitt 2.3. Bis die jeweilige Seite existiert,
verweist die Anzeigengruppe auf die nächsthöhere vorhandene Seite (z. B. `Pflichtteil` →
`/erbrecht`). Niemals auf die Startseite.

## 5.8 Prüfliste vor dem Kampagnenstart

- [ ] Die fünf Seiten der Stufe 1 sind online und erreichbar
- [ ] Jede Seite trägt den gesuchten Begriff in der H1-Überschrift
- [ ] Telefonnummer auf jeder Seite ohne Scrollen sichtbar und klickbar
- [ ] Formular funktioniert und leitet auf `/danke` weiter
- [ ] Ladezeit mobil unter 2,5 Sekunden geprüft (PageSpeed Insights)
- [ ] Impressum und Datenschutzerklärung vollständig und aktuell
- [ ] Datenschutzerklärung nennt Google Ads, Google Analytics und die eingesetzte
      Consent-Lösung ausdrücklich
- [ ] Consent-Banner erscheint und blockiert Tracking vor der Einwilligung
