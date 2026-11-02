# Kotoba – QA-Plan

## Ziel
Kotoba soll sich wie eine hochwertige Web-App anfühlen: fehlerfrei, schnell, auf jedem Gerät bedienbar, barrierearm und offline nutzbar.

## Testumgebungen
| Gerät | Viewport | Eingabe |
|---|---|---|
| Phone | 390×844, DPR 3 | Touch |
| Tablet | 820×1180 | Touch |
| Desktop | 1440×900 | Maus/Tastatur |

Je Gerät: Dunkel- und Hellmodus, Sprache DE/EN.

## Testbereiche und Erwartungen
1. **Erststart**: Logo-Animation läuft von selbst, wartet auf „Los geht's“, Hell→Dunkel-Vorführung, Willkommensdialog, Menü-Einführung (alle Schritte), keine Fehler.
2. **Wiederkehrender Start**: kurzer Splash (< 2,5 s), dann App; gespeichertes Design bleibt.
3. **Navigation**: alle 7 Bereiche + Lernpfad öffnen ohne Fehler, kein horizontales Scrollen, Inhalte nicht von der Leiste verdeckt.
4. **Lernsession**: Karten, Antworten, Weiter/Zurück, Fortschritt gespeichert.
5. **Spiele**: Bilderweg, Challenge, Maneki Run, Bonsai, Atmen, RPG (2D/2.5D/3D, Arcade) starten ohne Fehler; Ton aus funktioniert.
6. **Einstellungen**: Musik, Lautstärke, Stimme, Toggles, Daten löschen (setzt auf Erststart zurück).
7. **Barrierefreiheit**: Kontrast WCAG AA (4,5:1 / 3:1 groß), Touch-Ziele ≥ 44 px (mind. 28 px sichtbar mit erweitertem Trefferbereich), Buttons mit Namen, `prefers-reduced-motion`.
8. **Audio**: kein Autoplay-Fehler, Ton erst nach Interaktion, Stummschalten global/Spiel.
9. **Offline/PWA**: Manifest, Icons, Service Worker, Vorladen der Ressourcen, Fortschritt bleibt bei Update.
10. **Performance**: Start < 3,5 s bis bedienbar, keine Ruckler beim Seitenwechsel.

## Automatisierung
`tools/qa.py` (Playwright) prüft je Gerät × Design × Bereich: JS-/Konsolenfehler, horizontales Scrollen, unbeschriftete/zu kleine Bedienelemente, Kontrast, Bilder ohne `alt`, Erststart-Ablauf, Screenshots zur Sichtprüfung.

## Ergebnis Lauf 1 (v273) und Behebung (v274)
| Befund | Schwere | Behebung |
|---|---|---|
| Atmen-Spiel zeigte Rohtext `{呼吸|こきゅう}` statt Furigana | hoch | Furigana-Renderer angewendet |
| Aktive Buttons im Dunkelmodus: Kontrast 3,1:1 (weiß auf Zinnober) | mittel | dunkle Schrift auf Akzent (> 6:1) |
| 🔊-Vorlesebuttons 35×26 px, zu kleines Touch-Ziel | mittel | min. 38×30 px + erweiterter Trefferbereich |
| Kana-Tabs brachen mitten im Wort um („ひらが/な“) | mittel | kein Umbruch, skalierende Schrift |
| Musik-Button als Emoji, uneinheitlich zu SVG-Icons | niedrig | SVG-Lautsprecher-Icon (an/aus) |
| Keine JS-Fehler, kein horizontales Scrollen, Erststart inkl. 14 Tour-Schritte OK | – | – |
