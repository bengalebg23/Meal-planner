path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('Clear all', 'Clear week')
content = content.replace('Clear the whole plan and shopping list?', 'Clear this week\'s plan and shopping list?')
content = content.replace('v2.5.7', 'v2.5.8')

with open(path, 'w') as f:
    f.write(content)
print("Done")
