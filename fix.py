path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function loadArchivedWeek(weekKey) {
  try {
    const raw = localStorage.getItem('mealplanner_archive_' + weekKey);
    if (!raw) return;'''

new = '''function loadArchivedWeek(weekKey) {
  try {
    const raw = localStorage.getItem('mealplanner_archive_' + weekKey);
    if (!raw) {
      plan = emptyPlan();
      renderTable();
      renderBanks();
      renderShop();
      updateMealsDetected();
      return;
    }'''

old_v = 'v3.1.8'
new_v = 'v3.1.9'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.8', 'meal-planner-v3.1.9')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
