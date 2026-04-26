path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''const manifest = {
  name: "Family Meal Planner",
  short_name: "Meal Planner",'''

new = '''const isDev = window.location.hostname.includes('github.io') && window.location.pathname.includes('dev') || window.location.port !== '';
const manifest = {
  name: isDev ? "Meal Planner DEV" : "Family Meal Planner",
  short_name: isDev ? "Meals DEV" : "Meal Planner",'''

old_v = 'v2.5.13'
new_v = 'v2.5.14'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v2.5.13', 'meal-planner-v2.5.14')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
