path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function addCustomDay() {
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
  activeDays.unshift(newKey);
  ensureDayInPlan(newKey);
  saveToStorage();
  renderTable();
}'''

new = '''function addCustomDay() {
  const DAY_NAMES = ["sun","mon","tue","wed","thu","fri","sat"];
  const DAY_LABELS = {sun:"Sun",mon:"Mon",tue:"Tue",wed:"Wed",thu:"Thu",fri:"Fri",sat:"Sat"};
  const weekOffset = getWeekOffset();
  const now = new Date();
  const todayIdx = now.getDay();

  // Get date of first row - handles standard days and previous custom days
  let firstDate = null;
  const firstKey = activeDays[0];
  const firstStdIdx = DAY_NAMES.indexOf(firstKey);
  if (firstStdIdx !== -1) {
    const diff = firstStdIdx - todayIdx;
    firstDate = new Date(now);
    firstDate.setDate(now.getDate() + diff + (weekOffset * 7));
  } else if (customDays[firstKey] && customDays[firstKey].dateOffset !== undefined) {
    firstDate = new Date(now);
    firstDate.setDate(now.getDate() + customDays[firstKey].dateOffset + (weekOffset * 7));
  }

  const newKey = "custom_" + Date.now();
  let newLabel = "Day";
  let dateOffset = null;
  if (firstDate) {
    const prevDate = new Date(firstDate);
    prevDate.setDate(firstDate.getDate() - 1);
    const prevDayIdx = prevDate.getDay();
    newLabel = DAY_LABELS[DAY_NAMES[prevDayIdx]];
    const todayMidnight = new Date(now); todayMidnight.setHours(0,0,0,0);
    const prevMidnight = new Date(prevDate); prevMidnight.setHours(0,0,0,0);
    dateOffset = Math.round((prevMidnight - todayMidnight) / (24*60*60*1000)) - (weekOffset * 7);
  }
  customDays[newKey] = {key: newKey, label: newLabel, dateOffset: dateOffset, isWeekday: false};
  activeDays.unshift(newKey);
  ensureDayInPlan(newKey);
  saveToStorage();
  renderTable();
}'''

old_v = 'v3.2.5'
new_v = 'v3.2.6'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.5', 'meal-planner-v3.2.6')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
