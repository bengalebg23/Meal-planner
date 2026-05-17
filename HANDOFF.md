# Meal Planner PWA — Handoff Document

## New Chat Prompt (copy this)
```
I'm working on a family meal planner PWA. Please fetch these for context:
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/HANDOFF.md
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/code_dump_v3.3.33.txt
```

## Current Version
- **Dev branch**: v3.3.33

## v3.3.33 Changes
- Back/forward nav buttons always enabled. Users can step into empty weeks and edit them.
- navWeek from live with dir=-1 now always steps back by one ISO week (used to bail if no archives).

## v3.3.32 (previous)
- Shifted historical archives W09-W15 → W13-W19. W13-W15 skipped (real data present).
- Old W09-W15 placeholders deleted.

## v3.3.28 baseline
- Past + future weeks editable with confirm-on-first-edit.
- saveToStorage routes non-live edits to their correct archive key.

## Termux Workflow
```
mv /sdcard/Download/patch_v3.3.xx.sh ~/
bash ~/patch_v3.3.xx.sh
cd ~/meal-planner && mp
```
