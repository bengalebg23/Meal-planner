# Meal Planner PWA - Handoff Document
Last updated: 2026-04-24

## Live URLs
Production: https://bengalebg23.github.io/Meal-planner/
Dev preview: https://bengalebg23.github.io/Meal-planner/dev/
GitHub repo: https://github.com/bengalebg23/Meal-planner.git

## Current Version
Production (main): v2.5.0
Dev branch: v2.5.0 (in sync with main)

## Tech Stack
- Single HTML file index.html + sw.js service worker
- Firebase Realtime Database for sync
  Project: meal-planner-f5ba2
  DB URL: https://meal-planner-f5ba2-default-rtdb.europe-west1.firebasedatabase.app
  Rules: public read/write (private family use)
- GitHub Pages via gh-pages branch
- GitHub Actions at .github/workflows/deploy.yml
  Push to dev deploys to /Meal-planner/dev/
  Push to main deploys to /Meal-planner/
- Network-first service worker
- localStorage for offline persistence

## Family Config
People: Reuben, Vivien, Emily, Ben
Address: 17 Melody Drive, Sileby, Loughborough LE127UU
DnD nights: pizza hint on tea cell
Swimming days: quick tea hint on tea cell

## Column Layout (v2.5.0)
Day: 60px
INFO (Flag + Work stacked vertically): 40px
Lunch slots: 62px
Tea slots: 112px
Table total width: 796px, table-layout: fixed
day-label-input: 30px, font 10px
Flag/work selects: -webkit-appearance none, font 8px
Del day button: font 9px, display block

## App Features
- Meal plan grid: 4 people x Lunch/Tea x 7 days
- Meal bank (Everyone/Adults/Kids sections)
- Lunch options sidebar
- Lock button to freeze meal plan
- Three-week navigation (W15 W16 W17)
- Week archive by ISO week key e.g. 2026_W16
- Share modal exports MEALPLAN:base64 for import
- Shopping tab with Asda order picker
- Recipes tab with ClaudeRecipe / GaleRecipe tagging
- Dark mode toggle
- Firebase sync indicator
- Version badge white large top right
- Date shown next to day label e.g. Mon 20/4
- Short day names Mon/Tue/Wed/Thu/Fri/Sat/Sun
- INFO column: Flag + Work select stacked vertically

## Termux Aliases
mp: git add -A, commit, push to dev
mplive: merge dev to main, push to production
mpu: copy latest versioned file from Downloads + mp
mphandoff: push HANDOFF.md to both dev and main

## Branch Strategy
dev: test at bengalebg23.github.io/Meal-planner/dev/
main: live at bengalebg23.github.io/Meal-planner/
Always work on dev, test, then mplive when happy
mplive prints reminder to update HANDOFF.md

## Deployment Method
NEVER use downloaded files from Claude - always patch phone directly via Python.

Standard patch template:
python3 << PYEOF
import os
path = os.path.expanduser('~') + '/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()
content = content.replace('old', 'new')
content = content.replace('v2.5.X', 'v2.5.Y')
with open(path, 'w') as f:
    f.write(content)
print("Done:", 'new' in content)
PYEOF

Then always run:
sed -i "s/const CACHE = .*/const CACHE = 'meal-planner-vX.X.X';/" sw.js
mp

## Rules
1. Always uprevision on every change
2. Always bump sw.js cache to match
3. Name output files with full version e.g. meal-planner-v2.5.0.html
4. Never patch outputs file - always patch phone directly
5. One change = one version bump
6. Test on dev first, mplive when happy
7. White screen = check for duplicate const declarations in JS
8. Table not rendering = check isPlanLocked defined before saveToStorage
9. Network-first SW, no manual cache clears needed
10. Update HANDOFF.md at end of every session, run mphandoff
11. Always verify patches with print statements
12. Always grep exact strings before replacing
13. Use meaningful commit messages describing what changed

## Known Issues
- Shopping list generator needs Anthropic API key, broken on GitHub Pages
- Firebase only syncs current week, not future planned weeks

## Version History
v2.3.6: Last stable before major column work
v2.4.0-v2.4.14: INFO column merge, column sizing iterations
v2.5.0: CURRENT - Final column sizing (Day 60, Info 40, Lunch 62, Tea 112), table-layout fixed, INFO column (Flag+Work stacked)

## New Chat Prompt
I'm working on a family meal planner PWA. Full context is at https://raw.githubusercontent.com/bengalebg23/Meal-planner/main/HANDOFF.md?v=2.5.0 - please read that first, then I'll tell you what I need next.
