path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function addCustomDay() {
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

new = '''function addCustomDay() {
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

old_v = 'v3.2.0'
new_v = 'v3.2.1'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.0', 'meal-planner-v3.2.1')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
