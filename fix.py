path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function addCustomDay() {
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
  activeDays.unshift(newKey);'''

new = '''function addCustomDay() {
  // Full week in calendar order, wrapping Sun before Mon
  const WEEK_ORDER = ["sun","mon","tue","wed","thu","fri","sat"];
  // Find the first standard day in activeDays
  let firstStdKey = null;
  for (const key of activeDays) {
    if (WEEK_ORDER.includes(key)) { firstStdKey = key; break; }
  }
  if (firstStdKey) {
    const idx = WEEK_ORDER.indexOf(firstStdKey);
    // Walk backwards to find a day not already in activeDays
    for (let i = idx - 1; i >= 0; i--) {
      const prevDay = WEEK_ORDER[i];
      if (!activeDays.includes(prevDay)) {
        const stdDay = DAYS.find(d => d.key === prevDay);
        if (stdDay) {
          activeDays.unshift(prevDay);
          ensureDayInPlan(prevDay);
          saveToStorage();
          renderTable();
          return;
        }
      }
    }
  }
  // Fall back to custom day
  const newKey = "custom_" + Date.now();
  customDays[newKey] = {key: newKey, label: "New day", isWeekday: false};
  activeDays.unshift(newKey);'''

old_v = 'v3.2.2'
new_v = 'v3.2.3'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.2', 'meal-planner-v3.2.3')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
