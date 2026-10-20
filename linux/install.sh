#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../site"
DEST="${XDG_DATA_HOME:-$HOME/.local/share}/kotoba"
BIN="$HOME/.local/bin"
APPS="${XDG_DATA_HOME:-$HOME/.local/share}/applications"
mkdir -p "$DEST" "$BIN" "$APPS"
cp "$SRC/kotoba.html" "$DEST/kotoba.html"
cp "$SRC/kotoba-icon-512.png" "$DEST/kotoba.png"
cat > "$BIN/kotoba" <<EOF
#!/usr/bin/env bash
URL="file://$DEST/kotoba.html"
for b in chromium chromium-browser google-chrome google-chrome-stable microsoft-edge microsoft-edge-stable brave-browser vivaldi; do
  if command -v "\$b" >/dev/null 2>&1; then exec "\$b" --app="\$URL" --class=Kotoba --user-data-dir="$DEST/profile"; fi
done
if command -v firefox >/dev/null 2>&1; then exec firefox --new-window "\$URL"; fi
exec xdg-open "\$URL"
EOF
chmod +x "$BIN/kotoba"
cat > "$APPS/kotoba.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Kotoba
GenericName=Learn Japanese
Comment=Learn Japanese – lessons, games, RPG, chill modes (offline)
Exec=$BIN/kotoba
Icon=$DEST/kotoba.png
Terminal=false
Categories=Education;Languages;
StartupWMClass=Kotoba
EOF
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$APPS" >/dev/null 2>&1 || true
echo "Kotoba installed. Start it from your app menu or run: $BIN/kotoba"
