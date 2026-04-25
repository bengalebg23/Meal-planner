path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('v2.5.4', 'v2.5.6')

with open(path, 'w') as f:
    f.write(content)
print("Done")
