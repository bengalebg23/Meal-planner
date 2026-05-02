path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old_v = 'v3.1.6'
new_v = 'v3.1.7'

content = content.replace(old_v, new_v)
content = content.replace('meal-planner-v3.1.6', 'meal-planner-v3.1.7')

with open(path, 'w') as f:
    f.write(content)
print("Done")
