# Meal Planner PWA - Handoff Document

## Current Version
- Dev: v3.3.39

## v3.3.39 Notes
- Added Mediterranean lamb flatbread to meal bank + recipes via direct Firebase write.
- Flag: mealplanner_add_lamb_flatbread.

## Firebase Database Rules (CRITICAL)
If these get lost/expired, every write silently fails (.catch swallows the error). Paste this into the Firebase console Realtime DB Rules tab:
```json
{
  "rules": {
    "currentWeek": { ".read": true, ".write": true },
    "archives":    { ".read": true, ".write": true },
    "customMeals": { ".read": true, ".write": true },
    "recipes":     { ".read": true, ".write": true },
    "history": {
      ".read": true, ".write": true,
      "$taskId": { ".validate": "newData.hasChildren() || newData.val() === null" }
    }
  }
}
```
(The /history rule is for another app and must be preserved.)

## Cross-device Sync Diagnosis Playbook
When a new device shows no data:
1. Check Firebase console > Rules tab. Confirm read+write are open for currentWeek, archives, customMeals, recipes. If rules are missing/wrong, fix them first — nothing else matters.
2. Check Firebase console > Data tab. Confirm /archives has the expected week keys. If empty, the writes never landed — Firebase was rejecting them.
3. Custom meals are a good canary: they go through a different code path than archives. If custom meals sync but archives do not, it is the debounce bug.
4. Hard-refresh the device. Service worker can cache old code.
5. Confirm both devices are on the same URL (dev vs production!). `mp` only pushes to dev. `mplive` is required to update production.

## Firebase Debounce Pitfall (class of bug)
These helpers all share a single setTimeout per function:
- fbSave (currentWeek)
- fbSaveArchive (archives)
- fbSaveRecipes (recipes)
- fbSaveCustomMeal (customMeals — actually safe, uses unique key per call)
Calling fbSave/fbSaveArchive/fbSaveRecipes in a tight loop clobbers the timer — only the LAST call writes. For bulk operations, import set() + ref() directly from the firebase-database SDK and use await.

## Verification Checklist for Patches Touching Sync
1. After running the patch, confirm the on-screen alert or console message says what you expect.
2. Open Firebase console > Data tab. Verify the writes actually landed.
3. Load the app on a SECOND device (or in an incognito window). Verify reads work.
Step 2 would have caught the v3.3.36 debounce bug in 30 seconds.

## Termux Patch Flow
```
mv /sdcard/Download/patch_v3.3.xx.sh ~/
bash ~/patch_v3.3.xx.sh
cd ~/meal-planner && mp
```

## Aliases
- `mp` — commit + push to dev
- `mplive` — merge dev to main, push to production
- `mphandoff` — commit + push HANDOFF.md
Production runs whatever was last `mplive`-ed. Family devices opening the production URL get THAT code, not dev. Fresh devices need a working production build.

## Patch Conventions
1. Detect prior version by looping through recent versions in the file.
2. Bump version in title, version-badge, sw.js CACHE.
3. Self-review with debug prints showing actual counts/values, not just boolean asserts.
4. Auto-dump to code_dump_vX.X.X.txt.
5. Output the raw GitHub dev URL.
6. HANDOFF.md generation: use plain string concatenation only. No f-strings (literal braces in JS/JSON crash). No %-format (literal % crashes). Just `+`.
7. Work on dev branch.

## Patch-Writing Gotchas
1. **No f-strings or %-format for blocks with literal braces or %**. v3.3.36 crashed on f-string {}, v3.3.37 crashed on %s. Use plain `+` concatenation.
2. **Do not count substrings that appear in your own new code**. SHIFT_MAP literal contained "2026_W09":" which falsely matched the old archive blob signature. Use longer, more specific signatures.
3. **Do not count flag-name occurrences naively**. Comments mentioning the flag inflate the count. Use >= N not == N.
4. **Do not use find(end_marker) for IIFE ends**. Multiple })(); patterns confuse it. Anchor on a unique surrounding comment.
5. **set -e + assertion-first writes mean failures are safe**. Do all read/replace/check in memory; write to disk only after all asserts pass.

## CDN Caching
- raw.githubusercontent.com lags ~1 min after `mp` push.
- Use `git show HEAD --stat` to confirm a commit pushed.
- The live bengalebg23.github.io/Meal-planner/dev/ URL shows the deployed file (DOM only — localStorage is per-device).

## Bootstrap Flags in localStorage
One-shot migration gates. Clear the flag to re-trigger.
- mealplanner_w9_w15_bootstrap (cleared by v3.3.32)
- mealplanner_shift_w13_w19 (v3.3.32)
- mealplanner_force_w13_w15_v3 (v3.3.35)
- mealplanner_push_archives_v1 (v3.3.36 broken — debounce)
- mealplanner_push_archives_v2 (v3.3.38 fixed Firebase backfill)
- mealplanner_add_lamb_flatbread (v3.3.39 recipe inject)

## Version History
- v3.3.39 - inject Mediterranean lamb flatbread recipe (direct Firebase write)
- v3.3.38 - Firebase archive backfill with direct set+await (the one that finally worked)
- v3.3.36 - first Firebase backfill attempt, broken by shared debounce timer
- v3.3.35 - force-overwrite W13/14/15 with photo data
- v3.3.33 - nav buttons always enabled
- v3.3.32 - shifted W09-W15 to W13-W19 archives
- v3.3.28 - past+future weeks editable with confirm-on-first-edit

## Other Lessons Learnt Tonight
- Service worker can serve stale code. Hard-refresh new devices.
- "Real data" heuristic detection (counting non-default cells with threshold) gives false positives. When force-overwriting, hardcode the data into the bootstrap rather than reading from possibly-corrupt source slots.
- Errors in async Firebase code are easy to swallow. The whole "no sync" issue was masked by `.catch(e => console.warn(...))` on every set() call. When debugging, briefly add `console.error` or `alert` to those catches.
