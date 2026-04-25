#!/bin/bash
cd ~/meal-planner
git add HANDOFF.md
git commit -m "Update HANDOFF.md" 2>/dev/null
git push origin dev
git push origin main
TS=$(date +%s)
echo ""
echo "════ NEW CHAT PROMPT — copy this ════"
echo "I'm working on a family meal planner PWA. Please fetch this for context: https://cdn.jsdelivr.net/gh/bengalebg23/Meal-planner@main/HANDOFF.md?t=$TS"
echo "═════════════════════════════════════"
