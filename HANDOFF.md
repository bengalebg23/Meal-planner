# Meal Planner PWA — Handoff Document

## Live URLs
- **Production**: https://bengalebg23.github.io/Meal-planner/
- **Dev preview**: https://bengalebg23.github.io/Meal-planner/dev/
- **GitHub repo**: https://github.com/bengalebg23/Meal-planner.git

## Current Version
- **Production (main)**: v2.3.6
- **Dev branch**: v2.3.26 (in progress — stacked INFO column)

## Tech Stack
- Single HTML file `index.html` + `sw.js` service worker
- Firebase Realtime Database for real-time cross-device sync
  - Project: `meal-planner-f5ba2`
  - DB URL: `https://meal-planner-f5ba2-default-rtdb.europe-west1.firebasedatabase.app`
  - Rules: public read/write (private family use)
- GitHub Pages hosting
- Network-first service worker (auto-updates without cache clearing)
- localStorage for offline persistence

## Family Config
- **People**: Reuben, Vivien, Emily, Ben
- **Address**: 17 Melody Drive, Sileby, Loughborough LE127UU
- D&D nights → 🍕 Pizza hint
- Swimming days → ⚡ Quick tea hint

## App Features
- Meal plan grid: 4 people × Lunch/Tea × 7 days
- Meal bank (Everyone/Adults/Kids sections)
- Lunch options sidebar
- Lock button 🔓/🔒 to freeze meal plan
- Three-week navigation (W15 · W16 · W17)
- Week archive (auto-saves by ISO week key e.g. 2026_W16)
- Forward navigation into future weeks for planning ahead
- Share modal — exports `MEALPLAN:base64` string for import
- Shopping tab with Asda order picker
- Recipes tab with #ClaudeRecipe / #GaleRecipe tagging
- Dark mode toggle
- Firebase ⟳ sync indicator
- Version badge (white, large) in header

## Termux Workflow (Android/Pixel)
```bash
# Aliases in ~/.bashrc
mp      # git add -A, commit, push to dev branch
mplive  # merge dev -> main, push to production
mpu     # copy latest versioned file from Downloads + mp
```

## Branch Strategy
- `dev` branch → deploys to `/Meal-planner/dev/` via GitHub Actions
- `main` branch → deploys to `/Meal-planner/` via GitHub Actions
- Always work on dev, test, then mplive to go live
- GitHub Actions workflow at `.github/workflows/deploy.yml`

## Deployment Method
**Never use downloaded files from Claude chat** — they are often cached old versions.
**Always patch directly in Termux using Python scripts**, then `mp` to push.

Standard Python patch template:
```bash
python3 << 'PYEOF'
import os
path = os.path.expanduser('~') + '/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Make changes here
content = content.replace('old', 'new')

with open(path, 'w') as f:
    f.write(content)
print("Done")
PYEOF
```

## RULES — Always Follow These

1. **Always uprevision** — every change must bump the version number (e.g. v2.3.26 → v2.3.27)
2. **Always bump sw.js cache** — `sed -i "s/const CACHE = .*/const CACHE = 'meal-planner-vX.X.X';/" sw.js`
3. **Name output files with full version** — `meal-planner-v2.3.26.html` not `meal-planner-v2.html`
4. **Never patch outputs file and expect phone to get it** — always patch phone file directly via Python
5. **One change = one version bump** — don't batch multiple fixes under the same version
6. **Test on dev first** — push to dev branch, check `/dev/` URL, then `mplive` when happy
7. **If white screen** — check for duplicate `const` declarations in JS (especially `const currentKey` in `navWeek`)
8. **If table not rendering** — check `isPlanLocked` is defined before `saveToStorage` calls it
9. **sw.js uses network-first** — no manual cache clears needed after each push

## Current In-Progress Work (v2.3.26 on dev)
- Stacking FLAG and WHERE into single INFO column (saves a whole column width)
- `wsel2` is the work select inside the flag cell
- Header should show `<th class="flag-th">INFO</th>` (single column)
- Flag-th width: 44px
- Day column: 50px, day-label-input: 30px
- Slot columns: Lunch=30px, Tea=45px
- Dates shown next to day labels (e.g. Mon 21/4)
- Short day names: Mon/Tue/Wed etc

## Known Issues
- Shopping list generator (✨ Generate) requires Anthropic API key — currently broken on GitHub Pages
  - Was working via Claude artifact proxy, doesn't work without `x-api-key` header
  - Decision deferred — will add key later if needed
- Firebase sync only syncs current live week (not future planned weeks)

## File Locations
- Phone repo: `~/meal-planner/index.html` and `~/meal-planner/sw.js`
- Claude outputs: `/mnt/user-data/outputs/meal-planner-vX.X.X.html`
- GitHub Actions: `~/meal-planner/.github/workflows/deploy.yml`

## Version History Summary
- v2.1.x — wider columns, version badge, textarea meal cells
- v2.2.0 — Firebase real-time sync
- v2.2.1 — lock button, forward week navigation
- v2.2.2 — three-week nav (W15·W16·W17)
- v2.3.0 — clean rebuild, isPlanLocked at top of script
- v2.3.5 — fixed duplicate const in navWeek
- v2.3.6 — fixed false import error message (PRODUCTION)
- v2.3.7-v2.3.26 — column sizing, day labels, stacked INFO column (dev)
