#!/bin/bash
cd ~/meal-planner
VERSION=$(grep -o 'v[0-9]*\.[0-9]*\.[0-9]*' index.html | head -1)
cp index.html code_dump_${VERSION}.txt
git add -A
git commit -m "Update HANDOFF.md + code dump ${VERSION}" 2>/dev/null
git push origin dev
git push origin main
TS=$(date +%s)
echo ""
echo "════ NEW CHAT PROMPT — copy this ════"
echo "I'm working on a family meal planner PWA. Please fetch these for context:"
echo "https://cdn.jsdelivr.net/gh/bengalebg23/Meal-planner@main/HANDOFF.md?t=$TS"
echo "https://cdn.jsdelivr.net/gh/bengalebg23/Meal-planner@main/code_dump_${VERSION}.txt?t=$TS"
echo "═════════════════════════════════════"
