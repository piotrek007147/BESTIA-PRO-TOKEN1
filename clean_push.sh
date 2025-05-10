#!/bin/bash
echo "[1] Usuwam dane z historii..."
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch WARSTWY/skrypt.sh" \
  --prune-empty --tag-name-filter cat -- --all

echo "[2] Dodaję zmiany..."
git add .
git commit -m "Czysty commit bez tokenów"

echo "[3] Wypycham z nadpisaniem..."
git push --force --set-upstream origin main
