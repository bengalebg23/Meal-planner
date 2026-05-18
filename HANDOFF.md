# Meal Planner PWA — Handoff Document

## New Chat Prompt (copy this)
```
I'm working on a family meal planner PWA. Please fetch these for context:
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/HANDOFF.md
https://raw.githubusercontent.com/bengalebg23/Meal-planner/dev/code_dump_v3.3.35.txt
```

## Current Version
- **Dev branch**: v3.3.35

## v3.3.35 Changes
- Force-overwrite W13/W14/W15 with photo data (Tennis Sun / odd socks / K@Melody plans).
- Gated on mealplanner_force_w13_w15_v3.

## v3.3.33 Changes
- Nav buttons always enabled.

## Termux Workflow
```
mv /sdcard/Download/patch_v3.3.xx.sh ~/
bash ~/patch_v3.3.xx.sh
cd ~/meal-planner && mp
```
