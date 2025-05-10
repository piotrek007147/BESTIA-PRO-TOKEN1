#!/bin/bash
echo "[1] Dodaję zmiany..."
git add .
git commit -m "Czysty commit bez tokenów"

echo "[2] Czyszczę historię..."
git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch WARSTWY/skrypt.sh" \
--prune-empty --tag-name-filter cat -- --all

echo "[3] Wypycham z nadpisaniem..."
git push --force --set-upstream origin main
