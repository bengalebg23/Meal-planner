# Meal Planner PWA — Handoff Document

## New Chat Prompt (copy this)
```
I'm working on a family meal planner PWA. Please fetch these for context:
https://cdn.jsdelivr.net/gh/bengalebg23/Meal-planner@main/HANDOFF.md?t=TIMESTAMP
https://cdn.jsdelivr.net/gh/bengalebg23/Meal-planner@main/code_dump_v3.3.28.txt?t=TIMESTAMP
```
Replace `TIMESTAMP` with `$(date +%s)` (or use the `mphandoff` alias which prints a fresh one).

## Live URLs
- **Production**: https://bengalebg23.github.io/Meal-planner/
- **Dev preview**: https://bengalebg23.github.io/Meal-planner/dev/
- **GitHub repo**: https://github.com/bengalebg23/Meal-planner.git

## Current Version
- **Dev branch**: v3.3.28
- **Production (main)**: previous (push with `mplive` when verified)

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
- D&D nights -> 🍕 Pizza hint
- Swimming days -> ⚡ Quick tea hint

## v3.3.28 Changes (this version)
- **Editable past and future weeks.** Read-only gate dropped. Inputs always enabled across all weeks.
- **Confirm-on-first-edit per non-live week.** First keystroke / dropdown change on a past or future week pops a confirm dialog with the week label. Approve once and that week stays unlocked for the rest of the session (resets on reload).
- **Saves routed to correct archive.** Previously, edits on a future week silently clobbered the live week. Now any non-live edit writes to `mealplanner_archive_{weekKey}` and Firebase `/archives/{weekKey}`.
- **Read-only badge replaced** with `past` (purple) / `future` (blue) / `editing` (orange).
- **Restore-to-current button** hidden when viewing future weeks (only past makes sense to restore).
- **Bootstrap injection** of historical archives W9–W15 of 2026 from photos. One-shot, flagged with `mealplanner_w9_w15_bootstrap` in localStorage. Won't overwrite existing keys. Pushed to Firebase on inject.

## App Features
- Meal plan grid: 4 people × Lunch/Tea × 7-8 days
- Unified meal bank with tag filters (When/Who/Protein/Effort/Style/Sort)
- Lunch options sidebar (Quick/Cooked/Viv)
- Lock button 🔓/🔒 to freeze meal plan
- Three-week navigation (W-1 · W · W+1)
- Week archive (auto-saves by ISO week key e.g. 2026_W16)
- Past and future weeks now editable with confirmation
- Share modal — exports `MEALPLAN:base64` string for import
- Shopping tab with Asda order picker (auto-suggests best-matching past order)
- Recipes tab with #ClaudeRecipe / #GaleRecipe tagging
- Dark mode toggle
- Firebase ⟳ sync indicator
- Custom meals with addedBy + addedAt, new-meals banner, 🔔 history modal
- Version badge (white, large) in header

## Termux Workflow (Android/Pixel)
```bash
# Aliases in ~/.bashrc
mp        # git add -A, commit, push to dev branch
mplive    # merge dev -> main, push to production
mphandoff # commit + push HANDOFF.md, print new-chat prompt
```

## Branch Strategy
- `dev` -> deploys to `/Meal-planner/dev/`
- `main` -> deploys to `/Meal-planner/`
- Always work on dev, test, then `mplive` to go live

## Patch Conventions (from v3.3.17 onwards)
Every patch script must:
1. **Always uprevision** — bump in `<title>`, `#version-badge`, and `sw.js` CACHE
2. **Self-review JS** for scope collisions, syntax errors, duplicate `const`/`let`
3. **Auto-dump** `index.html` -> `code_dump_vX.X.X.txt`
4. **Output the jsDelivr dump URL** for session handoff
5. **Regenerate HANDOFF.md** with current state
6. Work on `dev` branch, not `main`

Standard Python patch template lives in `~/meal-planner/patches/`.

## Known Issues
- Shopping list generator (✨ Generate) requires Anthropic API key — currently asks via prompt and stores in `mealplanner_apikey` localStorage. Calls Anthropic API directly with `anthropic-dangerous-direct-browser-access` header.

## File Locations
- Phone repo: `~/meal-planner/index.html` and `~/meal-planner/sw.js`
- Patch scripts: `~/meal-planner/patches/`
- Claude outputs: `/mnt/user-data/outputs/`

## Key Debugging Lessons
- **White screen** -> check for duplicate `const` declarations in JS (especially `const currentKey` in `navWeek`)
- **Table not rendering** -> check `isPlanLocked` is defined before `saveToStorage` calls it
- **Click handlers that re-render the DOM via `innerHTML=""`** cause detached-node issues with document-level bubbling listeners — fix with `setTimeout(..., 0)` to defer re-render
- **Stale fetches from raw.githubusercontent.com** — use jsDelivr instead with `?t=TIMESTAMP` cache buster
