#!/bin/bash

echo -e "\n[1] Usuwam poufne dane z historii..."
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch WARSTWY/skrypt.sh" \
  --prune-empty --tag-name-filter cat -- --all

echo -e "\n[2] Dodaję zmiany..."
git add .
git commit -m "Czysty commit bez tokenów"

echo -e "\n[3] Wypycham z nadpisaniem..."
git push --force --set-upstream origin main
