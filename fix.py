path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Fix 1: getDayDate to accept an offset (weeks from current)
old1 = '''function getDayDate(dayKey) {
  // Returns e.g. "21/4" for the day in the current week
  const now = new Date();
  const dayOfWeek = now.getDay(); // 0=Sun
  const days = {mon:1,tue:2,wed:3,thu:4,fri:5,sat:6,sun:0};
  if (!(dayKey in days)) return '';
  const target = days[dayKey];
  const diff = target - dayOfWeek;
  const d = new Date(now);
  d.setDate(now.getDate() + diff);
  return d.getDate() + '/' + (d.getMonth()+1);
}'''

new1 = '''function getWeekOffset() {
  // Returns how many weeks we are from current week based on viewingWeekKey
  if (!viewingWeekKey) return 0;
  const cur = getCurrentWeekKey();
  if (!cur) return 0;
  const [cy, cw] = cur.split('_W').map(Number);
  const [vy, vw] = viewingWeekKey.split('_W').map(Number);
  return (vy - cy) * 52 + (vw - cw);
}

function getDayDate(dayKey) {
  const now = new Date();
  const dayOfWeek = now.getDay(); // 0=Sun
  const days = {mon:1,tue:2,wed:3,thu:4,fri:5,sat:6,sun:0};
  if (!(dayKey in days)) return '';
  const target = days[dayKey];
  const diff = target - dayOfWeek;
  const d = new Date(now);
  d.setDate(now.getDate() + diff + (getWeekOffset() * 7));
  return d.getDate() + '/' + (d.getMonth()+1);
}'''

# Fix 2: addCustomDay - intelligently add previous day
old2 = '''function addCustomDay() {
  const id = "custom_" + Date.now();
  customDays[id] = {key: id, label: "New day", isWeekday: false};
  activeDays.unshift(id);
  ensureDayInPlan(id);
  saveToStorage();
  renderTable();
}'''

new2 = '''function addCustomDay() {
  // Find the day before the first active day
  const STD_DAYS = ["sun","mon","tue","wed","thu","fri","sat"];
  const firstKey = activeDays[0];
  const firstStd = STD_DAYS.indexOf(firstKey);
  let newLabel = "Day";
  let newKey = "custom_" + Date.now();
  
  if (firstStd > 0) {
    // Previous standard day exists
    const prevDay = STD_DAYS[firstStd - 1];
    const stdDay = DAYS.find(d => d.key === prevDay);
    if (stdDay && !activeDays.includes(prevDay)) {
      // Use the standard day key directly
      newKey = prevDay;
      newLabel = stdDay.label;
      activeDays.unshift(newKey);
      ensureDayInPlan(newKey);
      saveToStorage();
      renderTable();
      return;
    }
  }
  // Fall back to custom day
  customDays[newKey] = {key: newKey, label: newLabel, isWeekday: false};
  activeDays.unshift(newKey);
  ensureDayInPlan(newKey);
  saveToStorage();
  renderTable();
}'''

old_v = 'v3.1.3'
new_v = 'v3.1.4'

hits = [old1 in content, old2 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.3', 'meal-planner-v3.1.4')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
