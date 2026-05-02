path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Show offset in date for debugging
old = "  return d.getDate() + '/' + (d.getMonth()+1);"
new = "  return d.getDate() + '/' + (d.getMonth()+1) + '(' + getWeekOffset() + ')';"

old_v = 'v3.1.7'
new_v = 'v3.1.8'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.7', 'meal-planner-v3.1.8')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
