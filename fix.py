path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# 1. Remove ???? button from meal bank header (static HTML)
old1 = '      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button></div>'
new1 = '      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank</div>'

# 2. Remove ???? button from lunch options header
old2 = '        <div class="bank-header">🥪 Lunch Options <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button></div>'
new2 = '        <div class="bank-header">🥪 Lunch Options</div>'

# 3. Remove ???? button from dynamic header
old3 = '    hdr.innerHTML = `🍽 Meal Bank <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button>`;'
new3 = '    hdr.innerHTML = "🍽 Meal Bank";'

# 4. Add ???? and New - type in to Everyone meal bank
old4 = '"Roast","Fajitas","Tortellini"]'
new4 = '"Roast","Fajitas","Tortellini","????","New - type in"]'

# 5. Add unsure CSS fresh after sandwich style
old5 = '  .meal-input.sandwich { color: #374151; font-style: italic; }'
new5 = '  .meal-input.sandwich { color: #374151; font-style: italic; }\n  .meal-input.unsure { color: #dc2626; font-weight: 700; }\n  td.meal-cell.unsure { background: #fee2e2 !important; }'

# 6. Add unsure class to td when value is ????
old6 = '        td.className = "meal-cell " + slot + (isAB ? " active" : "") + (isPizzaHint ? " pizza-hint" : "") + (isQuickHint ? " quick-hint" : "");'
new6 = '        td.className = "meal-cell " + slot + (isAB ? " active" : "") + (isPizzaHint ? " pizza-hint" : "") + (isQuickHint ? " quick-hint" : "") + (val==="????" ? " unsure" : "");'

# 7. Add "New - type in" handler
old7 = 'function injectMeal(text) {'
new7 = '''function injectMeal(text) {
  if (text === "New - type in") {
    if (multiSelected.size > 0) { multiSelected.clear(); updateFloating(); renderTable(); renderBanks(); }
    else if (activeBank) {
      const inp = document.querySelector(`textarea[data-cellkey="${activeBank.day}|${activeBank.person}|${activeBank.slot}"]`);
      activeBank = null; updateFloating(); renderBanks();
      if (inp) { inp.focus(); inp.select(); }
    }
    return;
  }'''

old_v = 'v2.5.10'
new_v = 'v2.5.11'

hits = [old1 in content, old2 in content, old3 in content, old4 in content, old5 in content, old6 in content, old7 in content]
print("Hits:", hits)
if all(hits):
    for old, new in [(old1,new1),(old2,new2),(old3,new3),(old4,new4),(old5,new5),(old6,new6),(old7,new7)]:
        content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
