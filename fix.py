path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# 1. Add the type-in bar HTML after the grid-wrap div
old1 = '  <div id="banks">'
new1 = '''  <div id="type-in-bar" style="padding:6px 8px 0;">
    <div style="display:flex;gap:6px;align-items:center;">
      <input id="type-in-input" type="text" placeholder="Type a meal name then tap a cell..." style="flex:1;border:1px solid #e7e5e4;border-radius:8px;padding:8px 11px;font-size:12px;outline:none;font-family:inherit;" />
      <button onclick="typeInConfirm()" style="background:#1c1917;color:white;border:none;border-radius:8px;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;">Fill</button>
    </div>
  </div>
  <div id="banks">'''

# 2. Remove "New - type in" from meal bank
old2 = '"Roast","Fajitas","Tortellini","????","New - type in"]'
new2 = '"Roast","Fajitas","Tortellini","????"]'

# 3. Remove the "New - type in" handler from injectMeal
old3 = '''function injectMeal(text) {
  if (text === "New - type in") {
    if (multiSelected.size > 0) { multiSelected.clear(); updateFloating(); renderTable(); renderBanks(); }
    else if (activeBank) {
      const key = `${activeBank.day}|${activeBank.person}|${activeBank.slot}`;
      const inp = document.querySelector(`textarea[data-cellkey="${key}"]`);
      activeBank = null;
      document.getElementById("floating-bar").classList.remove("visible");
      if (inp) { inp.focus(); inp.setSelectionRange(0, inp.value.length); }
    }
    return;
  }'''
new3 = 'function injectMeal(text) {'

# 4. Add typeInConfirm function before injectMeal
old4 = 'function injectMeal(text) {'
new4 = '''function typeInConfirm() {
  const val = document.getElementById("type-in-input").value.trim();
  if (!val) return;
  if (multiSelected.size > 0 || activeBank) {
    injectMeal(val);
    document.getElementById("type-in-input").value = "";
  }
}

function injectMeal(text) {'''

old_v = 'v2.5.16'
new_v = 'v2.5.17'

hits = [old1 in content, old2 in content, old3 in content, old4 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old3, new3)
    content = content.replace(old4, new4)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v2.5.16', 'meal-planner-v2.5.17')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
