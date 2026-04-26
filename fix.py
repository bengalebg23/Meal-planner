path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function injectMeal(text) {
  if (text === "New - type in") {
    if (multiSelected.size > 0) { multiSelected.clear(); updateFloating(); renderTable(); renderBanks(); }
    else if (activeBank) {
      const inp = document.querySelector(`textarea[data-cellkey="${activeBank.day}|${activeBank.person}|${activeBank.slot}"]`);
      activeBank = null; updateFloating(); renderBanks();
      if (inp) { inp.focus(); inp.select(); }
    }
    return;
  }'''

new = '''function injectMeal(text) {
  if (text === "New - type in") {
    if (multiSelected.size > 0) { multiSelected.clear(); updateFloating(); renderTable(); renderBanks(); }
    else if (activeBank) {
      const key = `${activeBank.day}|${activeBank.person}|${activeBank.slot}`;
      activeBank = null; updateFloating(); renderBanks();
      setTimeout(() => {
        const inp = document.querySelector(`textarea[data-cellkey="${key}"]`);
        if (inp) { inp.focus(); inp.click(); }
      }, 50);
    }
    return;
  }'''

old_v = 'v2.5.11'
new_v = 'v2.5.12'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace("meal-planner-v2.5.11", "meal-planner-v2.5.12")
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
