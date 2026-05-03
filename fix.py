path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''  // Previous day
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

new = '''  // Also check if first day is a custom day with a stored date offset
  if (!firstDate && customDays[firstKey] && customDays[firstKey].dateOffset !== undefined) {
    firstDate = new Date(now);
    firstDate.setDate(now.getDate() + customDays[firstKey].dateOffset + (weekOffset * 7));
  }

  const newKey = "custom_" + Date.now();
  let newLabel = "Day";
  let newDateOffset = null;
  if (firstDate) {
    const prevDate = new Date(firstDate);
    prevDate.setDate(firstDate.getDate() - 1);
    const prevDayIdx = prevDate.getDay();
    newLabel = DAY_LABELS[DAY_NAMES[prevDayIdx]];
    // Store offset from today so we can calculate date later
    const todayMidnight = new Date(now); todayMidnight.setHours(0,0,0,0);
    const prevMidnight = new Date(prevDate); prevMidnight.setHours(0,0,0,0);
    newDateOffset = Math.round((prevMidnight - todayMidnight) / (24*60*60*1000)) - (weekOffset * 7);
    customDays[newKey] = {key: newKey, label: newLabel, dateOffset: newDateOffset, isWeekday: false};
  } else {
    customDays[newKey] = {key: newKey, label: newLabel, isWeekday: false};
  }
  activeDays.unshift(newKey);'''

# Fix Bug 1: render custom day label with date on second line
old2 = '''        const dateStr = getDayDate(dayKey);
        const isCustom = dayKey.startsWith("custom_");
        const customLabel = customDays[dayKey]?.label || dayKey;
        const labelText = isCustom ? customLabel : (stdDay?.label || dayKey);
        cell.innerHTML = `<div>${labelText}</div>${dateStr ? `<div style="font-size:9px;color:#a8a29e">${dateStr}</div>` : ""}`;'''

new2 = '''        const dateStr = getDayDate(dayKey);
        const isCustom = dayKey.startsWith("custom_");
        const customLabel = customDays[dayKey]?.label || dayKey;
        const labelText = isCustom ? customLabel : (stdDay?.label || dayKey);
        // For custom days with dateOffset, show date from offset
        let customDateStr = "";
        if (isCustom && customDays[dayKey]?.dateOffset !== undefined) {
          const d = new Date();
          d.setDate(d.getDate() + customDays[dayKey].dateOffset + (getWeekOffset() * 7));
          customDateStr = d.getDate() + "/" + (d.getMonth()+1);
        }
        const displayDate = isCustom ? customDateStr : dateStr;
        cell.innerHTML = `<div>${labelText}</div>${displayDate ? `<div style="font-size:9px;color:#a8a29e">${displayDate}</div>` : ""}`;'''

old_v = 'v3.2.4'
new_v = 'v3.2.5'

hits = [old in content, old2 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old, new)
    content = content.replace(old2, new2)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.4', 'meal-planner-v3.2.5')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
