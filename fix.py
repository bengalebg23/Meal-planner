path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''    if (isCustom) {
      const labelInp = document.createElement("input");
      labelInp.className = "day-label-input";
      labelInp.value = day.label;
      labelInp.oninput = () => { customDays[dayKey].label = labelInp.value; saveToStorage(); };
      const delBtn = document.createElement("button");
      delBtn.className = "del-day-btn";
      delBtn.title = "Remove this row";
      delBtn.textContent = "✕";
      delBtn.onclick = () => removeDay(dayKey);
      tdDay.appendChild(labelInp);
      tdDay.appendChild(delBtn);'''

new = '''    if (isCustom) {
      const labelInp = document.createElement("input");
      labelInp.className = "day-label-input";
      labelInp.value = day.label;
      labelInp.oninput = () => { customDays[dayKey].label = labelInp.value; saveToStorage(); };
      const delBtn = document.createElement("button");
      delBtn.className = "del-day-btn";
      delBtn.title = "Remove this row";
      delBtn.textContent = "✕";
      delBtn.onclick = () => removeDay(dayKey);
      tdDay.appendChild(labelInp);
      // Show date below label if dateOffset is stored
      if (customDays[dayKey]?.dateOffset !== undefined) {
        const d = new Date();
        d.setDate(d.getDate() + customDays[dayKey].dateOffset + (getWeekOffset() * 7));
        const dateDiv = document.createElement("div");
        dateDiv.style.cssText = "font-size:8px;color:#a8a29e;text-align:center;";
        dateDiv.textContent = d.getDate() + "/" + (d.getMonth()+1);
        tdDay.appendChild(dateDiv);
      }
      tdDay.appendChild(delBtn);'''

old_v = 'v3.2.4'
new_v = 'v3.2.5'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.4', 'meal-planner-v3.2.5')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
