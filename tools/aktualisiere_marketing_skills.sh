#!/usr/bin/env bash
# Holt die Marketing-Skills von Corey Haines nach .claude/skills/.
#
# Quelle: https://github.com/coreyhaines31/marketingskills (MIT)
# Aufruf:  bash tools/aktualisiere_marketing_skills.sh
#
# Die Skills sind eine 1:1-Kopie des Ordners skills/ aus dem Original-Repository,
# ohne die evals/-Ordner (Testdaten der Skill-Entwickler, im Betrieb ohne Funktion).
# Nicht von Hand bearbeiten - Aenderungen gehen beim naechsten Lauf verloren.
# Eigene Kanzlei-Skills gehoeren nach .claude/skills/kanzlei-*/ und werden
# von diesem Skript nicht angetastet.

set -euo pipefail

QUELLE="https://github.com/coreyhaines31/marketingskills.git"
WURZEL="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ZIEL="$WURZEL/.claude/skills"
TEMP="$(mktemp -d)"
trap 'rm -rf "$TEMP"' EXIT

echo "Hole $QUELLE ..."
git clone --depth 1 --quiet "$QUELLE" "$TEMP/ms"

VERSION="$(sed -n 's/.*"version": "\([^"]*\)".*/\1/p' "$TEMP/ms/.claude-plugin/plugin.json" | head -1)"
echo "Version $VERSION"

mkdir -p "$ZIEL"

# Nur die Fremd-Skills ersetzen. Alles unter kanzlei-* bleibt unberuehrt.
while IFS= read -r -d '' vorhanden; do
  name="$(basename "$vorhanden")"
  case "$name" in
    kanzlei-*) continue ;;
  esac
  rm -rf "$vorhanden"
done < <(find "$ZIEL" -mindepth 1 -maxdepth 1 -type d -print0)

anzahl=0
for skill in "$TEMP/ms/skills"/*/; do
  name="$(basename "$skill")"
  cp -r "$skill" "$ZIEL/$name"
  rm -rf "$ZIEL/$name/evals"
  anzahl=$((anzahl + 1))
done

cp "$TEMP/ms/LICENSE" "$ZIEL/LICENSE-marketingskills"

cat > "$ZIEL/HERKUNFT.md" <<HINWEIS
# Herkunft der Skills in diesem Ordner

| | |
|---|---|
| Quelle | https://github.com/coreyhaines31/marketingskills |
| Autor | Corey Haines |
| Lizenz | MIT (siehe \`LICENSE-marketingskills\`) |
| Version | $VERSION |
| Stand | $(date +%Y-%m-%d) |
| Anzahl | $anzahl Skills |

Kopiert wird der Ordner \`skills/\` des Original-Repositories, ohne die
\`evals/\`-Unterordner. Diese Dateien werden **nicht von Hand gepflegt** –
zum Aktualisieren:

\`\`\`bash
bash tools/aktualisiere_marketing_skills.sh
\`\`\`

Eigene Kanzlei-Skills gehoeren in Ordner mit dem Praefix \`kanzlei-\`.
Das Aktualisierungsskript laesst sie stehen.
HINWEIS

echo "$anzahl Skills nach $ZIEL geschrieben."
