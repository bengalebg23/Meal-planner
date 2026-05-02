path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function addCustomDay() {
  const STD_DAYS = ["sun","mon","tue","wed","thu","fri","sat"];
  // Find the earliest standard day in activeDays
  let earliestStdIdx = -1;
  for (const key of activeDays) {
    const idx = STD_DAYS.indexOf(key);
    if (idx !== -1) { earliestStdIdx = idx; break; }
  }
  if (earliestStdIdx > 0) {
    // Try to add the previous standard day
    const prevDay = STD_DAYS[earliestStdIdx - 1];
    const stdDay = DAYS.find(d => d.key === prevDay);
    if (stdDay && !activeDays.includes(prevDay)) {
      activeDays.unshift(prevDay);
      ensureDayInPlan(prevDay);
      saveToStorage();
      renderTable();
      return;
    }
  }
  // Fall back to custom day
  const newKey = "custom_" + Date.now();
  customDays[newKey] = {key: newKey, label: "New day", isWeekday: false};
  activeDays.unshift(newKey);
  ensureDayInPlan(newKey);
  saveToStorage();
  renderTable();
}'''

new = '''function addCustomDay() {
  // Week order for prepending: going back from Mon means Sun, Sat, Fri...
  const WEEK_ORDER = ["mon","tue","wed","thu","fri","sat","sun"];
  // Find the earliest day in activeDays that is a standard weekday
  let earliestIdx = -1;
  for (const key of activeDays) {
    const idx = WEEK_ORDER.indexOf(key);
    if (idx !== -1) { earliestIdx = idx; break; }
  }
  if (earliestIdx > 0) {
    // Previous day in week order
    const prevDay = WEEK_ORDER[earliestIdx - 1];
    const stdDay = DAYS.find(d => d.key === prevDay);
    if (stdDay && !activeDays.includes(prevDay)) {
      activeDays.unshift(prevDay);
      ensureDayInPlan(prevDay);
      saveToStorage();
      renderTable();
      return;
    }
  }
  // Fall back to custom day
  const newKey = "custom_" + Date.now();
  customDays[newKey] = {key: newKey, label: "New day", isWeekday: false};
  activeDays.unshift(newKey);
  ensureDayInPlan(newKey);
  saveToStorage();
  renderTable();
}'''

old_v = 'v3.2.1'
new_v = 'v3.2.2'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.1', 'meal-planner-v3.2.2')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
