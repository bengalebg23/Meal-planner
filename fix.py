path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '  #meal-filters { padding: 8px 8px 0; display: flex; flex-wrap: wrap; gap: 5px; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; margin-bottom: 3px; }'
new = '  #meal-filters { padding: 8px 8px 0; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; margin-bottom: 3px; background: white; border-radius: 8px; padding: 7px 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }'

old_v = 'v3.1.0'
new_v = 'v3.1.1'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.0', 'meal-planner-v3.1.1')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
