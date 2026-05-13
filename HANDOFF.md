# Family Meal Planner — Handoff Notes

## Current state
- **Version:** v3.3.27
- **Branch:** `dev` (NOT `main`). Production is on `main`; promote via `mplive`.
- **Repo:** bengalebg23/Meal-planner
- **Stack:** Single-file `index.html` (~2500 lines) + `sw.js`. Vanilla JS, Firebase RTDB sync, GitHub Pages.
- **PWA:** Yes. Manifest dynamically injected. Service worker caches per `CACHE = 'meal-planner-vX.X.X'`.
- **Family:** Ben, Emily, Reuben, Vivien — 17 Melody Drive, Sileby.

## Workflow
- Patches are bash scripts using Python heredocs to edit `~/meal-planner/index.html`.
- From v3.3.17 onwards every patch must:
  1. Bump version in `<title>`, `#version-badge`, and `sw.js` CACHE
  2. Auto-dump `cp index.html code_dump_vX.X.X.txt`
  3. Regenerate this HANDOFF.md
  4. Print the dump URL: `https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/code_dump_vX.X.X.txt`
- Push: `cd ~/meal-planner && mp` (dev) or `mplive` (prod).

## Self-review checklist for patches (mandatory before pushing)
Check the JS being added for:
- Duplicate `const`/`let` in same scope (caused v3.3.19/v3.3.20 to break)
- Variable shadowing in forEach loops
- Unclosed template literals
- References to undefined vars/functions
- Existing context in the dump that would collide

## Features
### Plan tab
- 4-person × 2-meal table (Reuben / Vivien / Emily / Ben × Lunch / Tea)
- DAY column sticky-left when horizontally scrolling
- Three-week navigation (W-1, current W, W+1) with read-only past weeks
- Past weeks can be unlocked with confirm prompt → edits save back to archive
- Custom day rows (insert above with auto-calculated previous date)
- Per-day flag dropdown: D&D, Swimming, Nursery, School trip, Karen's, Eating out, Quick, plus ✏ Custom...
- All flags render uniformly as grey text under day label with × delete + tap-to-edit
- Per-day work mode (office / wfh / weekend)
- Cell typing with autocomplete dropdown (top 5: prefix matches first, then substring, alphabetical)
- Top action bar (replaces old legend): 🔔 history / + Add meal / Clear cell
- Multi-cell select via double-tap; floating bar shows current selection

### Meal bank
- Unified pill bank with tag filters: When / Who / Protein / Effort / Style (all exclusive within group)
- Filter group dividers between groups
- Always sorted by popularity descending (archive-only counts), ties alphabetical
- Grey "(N)" count badge next to each pill (only shown when count > 0)
- + Add meal modal: 6 steps (name → who → when → protein → effort → style)
- Custom meals tagged `_custom: true`, synced via Firebase `/customMeals`
- Each custom meal stores `addedBy` + `addedAt`

### Notifications & history
- First-load name prompt, stored in `mealplanner_username`
- Yellow banner above bank when others add meals (dismissable, tap to flash pill)
- 🔔 history modal: all custom meals sorted newest-first with addedBy + relative date
- Tapping a history row scrolls bank into view and flashes the pill

### Cloud sync (Firebase RTDB)
- `/currentWeek`: plan, notes, week label, activedays, customdays, shop
- `/customMeals/{slug}`: custom meal bank
- `/archives/{weekKey}`: all past week snapshots
- `/recipes`: recipe edits
- Last-write-wins. 1.5s debounce on archives and recipes.

### Other tabs
- Shopping tab: Asda baseline order picker, AI-generated shopping list, manual add, category breakdown
- Recipes tab: ingredient editing, notes, #ClaudeRecipe / #GaleRecipe tagging

### Local-only state
- Dark mode preference, locked state, username, selected Asda baseline order

## Open threads
- **W1–W8 historical import:** Ben has photos from earlier weeks but only W9–W15 attempted. v3.3.19 attempt broke the app (duplicate const), reverted. May retry later, more carefully — one week at a time.
- **Cell typing keyboard regression:** Resolved in v3.3.12. `updateTableHighlight()` was re-rendering the entire table mid-focus event, destroying the just-focused textarea. Fix: toggle classes directly instead of re-rendering.

## Key files
- `index.html` — the whole app (~2500 lines)
- `sw.js` — service worker (cache busting per version)
- `code_dump_vX.X.X.txt` — snapshots committed alongside each patch
- `HANDOFF.md` — this file, refreshed each patch

## Lessons learned
- Click handlers that re-render DOM via `innerHTML = ""` destroy the click target mid-bubble. Document-level click handlers then see `e.target.closest(...)` as null. Fix: defer the re-render with `setTimeout(..., 0)`.
- Duplicate `const isCustom` in the same forEach scope is a silent SyntaxError that kills the whole script.
- Browser cache is aggressive on PWAs. Hard reload via long-press → "Reload from origin" or clear site data.
