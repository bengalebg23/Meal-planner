# Meal Planner PWA - Handoff Document

## Current Version
- Dev: v3.3.38

## v3.3.38 Notes
- Proper Firebase backfill using direct SDK set() + await, bypassing the fbSaveArchive debounce that broke v3.3.36/v3.3.37.
- Flag: mealplanner_push_archives_v2.

## Firebase Debounce Pitfall (key lesson)
fbSaveArchive uses a single shared 1500ms setTimeout — calling it in a tight loop clobbers the timer; only the LAST call writes. v3.3.36 reported "pushed 11 archives" but only the final one actually reached Firebase. For bulk operations use the SDK directly with await.

## Firebase DB Rules
Required paths: currentWeek, archives, customMeals, recipes (all .read+.write true).
Plus history rule preserved for the other app.

## Termux Patch Flow
mv /sdcard/Download/patch_v3.3.xx.sh ~/
bash ~/patch_v3.3.xx.sh
cd ~/meal-planner && mp

## Bootstrap Flags
- mealplanner_w9_w15_bootstrap (cleared)
- mealplanner_shift_w13_w19 (v3.3.32)
- mealplanner_force_w13_w15_v3 (v3.3.35)
- mealplanner_push_archives_v1 (v3.3.36 broken)
- mealplanner_push_archives_v2 (v3.3.37+v3.3.38 fixed)

## Version History
- v3.3.38 - Firebase backfill with direct set+await (v3.3.37 patch failed to apply correctly)
- v3.3.37 - intended Firebase backfill fix but patch crashed on HANDOFF write
- v3.3.36 - Firebase backfill via fbSaveArchive (broken by debounce)
- v3.3.35 - force-overwrite W13/14/15 with photo data
- v3.3.33 - nav buttons always enabled
- v3.3.32 - shifted W09-W15 to W13-W19
- v3.3.28 - past+future weeks editable
