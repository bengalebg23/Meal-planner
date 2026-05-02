path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '  #unified-bank-pills { padding: 9px; display: flex; flex-wrap: wrap; gap: 6px; }'
new = '  #unified-bank-pills { padding: 9px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; }'

old_v = 'v3.1.1'
new_v = 'v3.1.2'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.1', 'meal-planner-v3.1.2')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
