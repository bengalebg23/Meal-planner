path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function getWeekOffset() {
  // Returns how many weeks we are from current week based on viewingWeekKey
  if (!viewingWeekKey) return 0;
  const cur = getCurrentWeekKey();
  if (!cur) return 0;
  const [cy, cw] = cur.split('_W').map(Number);
  const [vy, vw] = viewingWeekKey.split('_W').map(Number);
  return (vy - cy) * 52 + (vw - cw);
}'''

new = '''function getWeekOffset() {
  if (!viewingWeekKey) return 0;
  const cur = getCurrentWeekKey();
  if (!cur) return 0;
  // Parse week keys to actual Monday dates and diff in weeks
  function weekKeyToMonday(key) {
    const [y, w] = key.split('_W').map(Number);
    // ISO week 1 is the week containing the first Thursday of the year
    const jan4 = new Date(y, 0, 4);
    const startOfWeek1 = new Date(jan4);
    startOfWeek1.setDate(jan4.getDate() - ((jan4.getDay() + 6) % 7));
    const d = new Date(startOfWeek1);
    d.setDate(d.getDate() + (w - 1) * 7);
    return d;
  }
  const curDate = weekKeyToMonday(cur);
  const viewDate = weekKeyToMonday(viewingWeekKey);
  return Math.round((viewDate - curDate) / (7 * 24 * 60 * 60 * 1000));
}'''

old_v = 'v3.1.5'
new_v = 'v3.1.6'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.5', 'meal-planner-v3.1.6')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
