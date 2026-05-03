path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function addCustomDay() {
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

new = '''function addCustomDay() {
  // Work out the date of the first day currently showing
  const DAY_NAMES = ["sun","mon","tue","wed","thu","fri","sat"];
  const DAY_LABELS = {sun:"Sun",mon:"Mon",tue:"Tue",wed:"Wed",thu:"Thu",fri:"Fri",sat:"Sat"};
  const firstKey = activeDays[0];
  const firstStdIdx = DAY_NAMES.indexOf(firstKey);
  
  // Get the actual date of the first row
  const weekOffset = getWeekOffset();
  const now = new Date();
  let firstDate = null;
  if (firstStdIdx !== -1) {
    const todayIdx = now.getDay(); // 0=Sun
    const diff = firstStdIdx - todayIdx;
    firstDate = new Date(now);
    firstDate.setDate(now.getDate() + diff + (weekOffset * 7));
  }
  
  // Previous day
  const newKey = "custom_" + Date.now();
  let newLabel = "Day";
  if (firstDate) {
    const prevDate = new Date(firstDate);
    prevDate.setDate(firstDate.getDate() - 1);
    const prevDayIdx = prevDate.getDay();
    newLabel = DAY_LABELS[DAY_NAMES[prevDayIdx]] + " " + prevDate.getDate() + "/" + (prevDate.getMonth()+1);
  }
  customDays[newKey] = {key: newKey, label: newLabel, isWeekday: false};
  activeDays.unshift(newKey);'''

old_v = 'v3.2.3'
new_v = 'v3.2.4'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.3', 'meal-planner-v3.2.4')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
