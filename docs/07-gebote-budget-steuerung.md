# 07 – Gebote, Budget & Steuerung

## 7.1 Der Gebotsstrategie-Fahrplan

Der häufigste Fehler bei Kanzlei-Konten: sofort mit „Ziel-CPA" starten. Ohne Conversion-Daten
hat die Automatik keine Grundlage – sie rät, und zwar teuer. Die Umstellung erfolgt in
Stufen, jeweils an eine Datenmenge gekoppelt:

| Stufe | Strategie | Voraussetzung | Einstellung |
|---|---|---|---|
| **1** | Klicks maximieren **mit CPC-Limit** | Kampagnenstart | Limit = `Max CPC` aus den Keyword-CSV |
| **2** | Conversions maximieren | ≥ 15 Conversions in 30 Tagen je Kampagne | ohne Ziel-CPA |
| **3** | Ziel-CPA | ≥ 30 Conversions in 30 Tagen je Kampagne | Ziel = realer CPA minus 10 % |
| **4** | Ziel-ROAS | Offline-Import läuft, echte Mandatswerte fließen zurück | Ziel nach Deckungsbeitrag |

**Warum das CPC-Limit in Stufe 1 wichtig ist:** „Klicks maximieren" ohne Limit gibt das
Tagesbudget für die teuersten verfügbaren Klicks aus. Mit Limit sammeln Sie mehr Klicks
für dasselbe Geld – und damit schneller die Datenbasis für Stufe 2.

### Regeln für den Wechsel zwischen den Stufen

- Nach jeder Umstellung **7 bis 14 Tage Lernphase** – in dieser Zeit keine weiteren
  Änderungen an Geboten, Budget oder Keywords.
- Der Ziel-CPA wird **nie um mehr als 20 % auf einmal** verändert. Größere Sprünge lösen
  eine neue Lernphase aus.
- Fällt eine Kampagne dauerhaft unter 15 Conversions/Monat, geht sie zurück auf Stufe 2.
  Ein Ziel-CPA auf dünner Datenbasis ist schlechter als keiner.

## 7.2 Budgetsteuerung

### Tagesbudget richtig setzen

```
Tagesbudget = Monatsbudget ÷ 30,4
```

Google darf an einzelnen Tagen bis zum Doppelten des Tagesbudgets ausgeben, gleicht das
aber über den Monat aus. Das Monatslimit ist Tagesbudget × 30,4 – nicht × 31.

### Budgetsplit Phase 1 (Monat 1–3)

| Kampagne | Anteil | Monat | Tag |
|---|---|---|---|
| BRAND | 3 % | 55 € | 1,80 € |
| Scheidung + Familie | 34 % | 610 € | 20,00 € |
| Erbrecht | 30 % | 540 € | 17,80 € |
| Immobilien + Treuhand | 28 % | 505 € | 16,60 € |
| Gesellschaftsrecht (Test) | 5 % | 90 € | 3,00 € |
| **Summe** | **100 %** | **1.800 €** | **59,20 €** |

### Umschichtungsregel ab Monat 4

Monatlich, immer nach demselben Verfahren:

1. CPA je Kampagne berechnen (Kosten ÷ Mandate, nicht ÷ Anfragen)
2. CPA ins Verhältnis zum Deckungsbeitrag des Rechtsgebiets setzen
3. Kampagne mit dem schlechtesten Verhältnis verliert 25 % Budget
4. Kampagne mit dem besten Verhältnis erhält diese 25 %
5. Keine Kampagne fällt unter 3 €/Tag – darunter ist sie nicht mehr lernfähig
6. Änderungen nur **einmal im Monat**, nicht laufend

> **Warum in Schritten von 25 % und nicht mehr:** Jede Budgetänderung über etwa 30 % löst
> bei Smart Bidding eine neue Lernphase aus. Wer zweimal im Monat kräftig umschichtet, hält
> das Konto dauerhaft in der Lernphase und wundert sich über instabile Ergebnisse.

### Wann das Budget erhöht wird

Ein klares Signal, keine Bauchentscheidung:

| Kennzahl | Schwelle | Bedeutung |
|---|---|---|
| Anteil an möglichen Impressionen (Suchnetzwerk) | < 60 % | Nachfrage ist da, Budget bremst |
| Verlorener Anteil durch Budget | > 15 % | Direkt messbarer entgangener Verkehr |
| CPA | unter Zielwert | Jeder zusätzliche Euro rechnet sich |

Sind alle drei erfüllt, Budget der betreffenden Kampagne um 20–25 % erhöhen und
14 Tage beobachten.

## 7.3 Gebotsanpassungen

### Phase 1 (manuelle Steuerung – Anpassungen wirken)

| Dimension | Anpassung | Begründung |
|---|---|---|
| Mobil | +10 % | Anwaltssuchen erfolgen überwiegend mobil, Anrufe kommen fast nur von dort |
| Computer | 0 % | Referenz |
| Tablet | −20 % | Schwache Anfragequalität, kaum Anrufe |
| Wien | 0 % | Referenz |
| Radius 25 km | −10 % | |
| Niederösterreich/Burgenland | −20 % | Nur Erbrecht und Immobilien |
| Mo–Do 08:00–18:00 | +15 % | Anrufe werden entgegengenommen |
| Fr 08:00–15:00 | +10 % | |
| Sa/So und abends | −20 % | Formularanfragen laufen weiter, Anrufe nicht |

### Ab Phase 2 (Smart Bidding)

**Alle diese Anpassungen werden von Google weitgehend ignoriert**, sobald „Conversions
maximieren" oder „Ziel-CPA" aktiv ist. Das ist kein Fehler, sondern Absicht: Die Automatik
bewertet Gerät, Standort und Uhrzeit selbst, und zwar auf Basis jedes einzelnen Auktionssignals.

Was ab Phase 2 stattdessen gesteuert wird:
- **Werbezeitplan als Ein/Aus**, nicht als Gebotsanpassung – und auch das nur, wenn ein
  Zeitfenster nachweislich keine verwertbaren Anfragen liefert
- **Standortausschlüsse** statt negativer Gebotsanpassungen
- **Zielgruppensegmente** in „Beobachtung", um zu sehen, wer konvertiert

## 7.4 Saisonale Anpassung

Google bietet dafür „Saisonale Anpassungen" (Tools → Budgets und Gebote). Sinnvoll bei
kurzfristig erwarteten Ausschlägen von mehr als 30 %.

| Zeitraum | Maßnahme |
|---|---|
| 2.–31. Jänner | Scheidungs-/Familienbudget +25 %; erfahrungsgemäß stärkste Nachfrage des Jahres |
| Mitte August – Ende September | Scheidungs-/Familienbudget +20 % |
| März–Juni, September–November | Immobilienbudget +15 % |
| Juli–August | Scheidungsbudget −20 % zugunsten Erbrecht |
| 20. Dezember – 1. Jänner | Gesamtbudget −40 %; Kanzlei geschlossen, Anrufe laufen ins Leere |

Der letzte Punkt ist wichtiger, als er klingt: Anzeigen, die schalten, während niemand
erreichbar ist, kosten Geld und erzeugen einen schlechten ersten Eindruck.

## 7.5 Steuerung über den Anteil an möglichen Impressionen

Diese Kennzahl zeigt, wie viel der verfügbaren Nachfrage Sie erreichen.

| Kennzahl | Auslegung | Maßnahme |
|---|---|---|
| Anteil gesamt < 40 % | Viel Nachfrage bleibt liegen | Ursache klären (Budget oder Rang?) |
| Verlust durch Budget > 15 % | Budget bremst | Budget erhöhen |
| Verlust durch Rang > 30 % | Gebot oder Qualitätsfaktor zu niedrig | Landingpage und Anzeigenrelevanz verbessern, dann Gebot |
| Anteil > 80 % bei gutem CPA | Nahe an der Marktobergrenze | Neue Rechtsgebiete erschließen statt Gebote erhöhen |

**Bei der Brand-Kampagne** sollte der Anteil bei über 90 % liegen. Wenn nicht, ist das
Gebot zu niedrig – Markenklicks kosten wenig und sind nahezu immer rentabel.

## 7.6 Qualitätsfaktor

Der Qualitätsfaktor (1–10) beeinflusst direkt, was ein Klick kostet. Er setzt sich aus drei
Teilen zusammen:

| Bestandteil | Beeinflussbar über |
|---|---|
| Erwartete Klickrate | Anzeigentexte, Relevanz der Anzeigengruppe |
| Anzeigenrelevanz | Enge Anzeigengruppen – der Grund für 30 statt 8 Anzeigengruppen |
| Nutzererfahrung mit der Landingpage | Eigene Zielseite je Thema, Ladezeit, mobile Darstellung |

Praktische Auswirkung: Der Sprung von Qualitätsfaktor 5 auf 8 senkt den effektiven Klickpreis
spürbar – bei unverändertem Gebot und unveränderter Position. Deshalb ist die Landingpage-Arbeit
aus Doc 05 keine Kür, sondern der günstigste Hebel im gesamten Konto.

Prüfung: Spalten „Qualitätsfaktor", „Erwartete CTR", „Anzeigenrelevanz" und
„Nutzererfahrung mit der Zielseite" in der Keyword-Ansicht einblenden. Alles unter 5 ist
ein Arbeitsauftrag.

## 7.7 Was nicht getan wird

| Nicht tun | Grund |
|---|---|
| Gebote täglich anpassen | Erzeugt Dauer-Lernphase, verschlechtert die Ergebnisse |
| Automatische Regeln zur Gebotssteuerung | Konflikt mit Smart Bidding |
| Alle Kampagnen in eine zusammenlegen | Kein getrenntes Budget je Rechtsgebiet, keine getrennte Steuerung |
| Empfehlungen im Konto blind übernehmen | Googles „Optimierungsfaktor" empfiehlt bevorzugt mehr Ausgaben – jede Empfehlung einzeln prüfen |
| Automatische Anwendung von Empfehlungen aktivieren | Fügt ungeprüft Broad-Match-Keywords und Kampagnentypen hinzu |
| Performance Max in Phase 1 | Kannibalisiert die Suchkampagnen bei diesem Budget |

> Der Punkt „Optimierungsfaktor" verdient Nachdruck: In der Kontooberfläche erscheint eine
> Prozentzahl, die suggeriert, das Konto sei „nur zu 68 % optimiert". Diese Zahl steigt,
> wenn man Googles Vorschläge annimmt – unabhängig davon, ob sie wirtschaftlich sinnvoll
> sind. Ein Konto mit 60 % Optimierungsfaktor und gutem CPA ist besser als eines mit 100 %
> und schlechtem. Die Zahl ist kein Ziel.
