path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '  .meal-input.school { color: #92400e; font-style: italic; opacity: 0.4; }\n  .meal-input.karen { color: #9d174d; font-style: italic; opacity: 0.4; }\n  .meal-input.nursery { color: #065f46; font-style: italic; opacity: 0.4; }\n  .meal-input.mira { color: #0369a1; font-style: italic; opacity: 0.4; }'

new = '  .meal-input.school { color: #92400e; font-style: italic; opacity: 0.4; }\n  .meal-input.karen { color: #9d174d; font-style: italic; opacity: 0.4; }\n  .meal-input.nursery { color: #065f46; font-style: italic; opacity: 0.4; }\n  .meal-input.mira { color: #0369a1; font-style: italic; opacity: 0.4; }\n  .meal-input.school, .meal-input.karen, .meal-input.nursery, .meal-input.mira { background: #e5e5e5 !important; border-radius: 4px; }'

old_v = 'v2.5.9'
new_v = 'v2.5.10'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
