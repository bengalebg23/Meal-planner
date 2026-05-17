# Meal Planner PWA — Handoff Document

## New Chat Prompt (copy this)
```
I'm working on a family meal planner PWA. Please fetch these for context:
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/HANDOFF.md
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/code_dump_v3.3.32.txt
```

## Current Version
- **Dev branch**: v3.3.32

## v3.3.32 Changes
- Shifted historical archives W09-W15 → W13-W19. (Versions 29-31 failed due to self-review bugs; this one finally lands the shift.)
- Safe-by-default: only writes to a target week if no real data exists. Skipped weeks surfaced in alert.

## v3.3.28 Changes (last working baseline before this shift)
- Past + future weeks editable with confirm-on-first-edit.
- saveToStorage routes non-live edits to their correct archive key.

## Termux Workflow
```
mv /sdcard/Download/patch_v3.3.xx.sh ~/
bash ~/patch_v3.3.xx.sh
cd ~/meal-planner && mp
```
