path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Fix 1: Remove debug (offset) from getDayDate
old1 = "  return d.getDate() + '/' + (d.getMonth()+1) + '(' + getWeekOffset() + ')';"
new1 = "  return d.getDate() + '/' + (d.getMonth()+1);"

# Fix 2: Restructure custom day cell layout - date left, delete right
old2 = '''      tdDay.appendChild(labelInp);
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

new2 = '''      const topRow = document.createElement("div");
      topRow.style.cssText = "display:flex;align-items:center;justify-content:space-between;";
      topRow.appendChild(labelInp);
      topRow.appendChild(delBtn);
      tdDay.appendChild(topRow);
      // Show date below label if dateOffset is stored
      if (customDays[dayKey] && customDays[dayKey].dateOffset !== undefined) {
        const d = new Date();
        d.setDate(d.getDate() + customDays[dayKey].dateOffset + (getWeekOffset() * 7));
        const dateDiv = document.createElement("div");
        dateDiv.style.cssText = "font-size:8px;color:#a8a29e;";
        dateDiv.textContent = d.getDate() + "/" + (d.getMonth()+1);
        tdDay.appendChild(dateDiv);
      }'''

old_v = 'v3.2.6'
new_v = 'v3.2.7'

hits = [old1 in content, old2 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.6', 'meal-planner-v3.2.7')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
