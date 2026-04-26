path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('v2.5.18', 'v3.0.0')
content = content.replace('v2.5.19', 'v3.0.0')

with open(path, 'w') as f:
    f.write(content)
print("Done")
