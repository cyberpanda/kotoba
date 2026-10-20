#!/usr/bin/env bash
set -eu
rm -rf "${XDG_DATA_HOME:-$HOME/.local/share}/kotoba" "$HOME/.local/bin/kotoba" "${XDG_DATA_HOME:-$HOME/.local/share}/applications/kotoba.desktop"
echo "Kotoba removed."
