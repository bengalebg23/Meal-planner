path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''    else if (activeBank) {
      const key = `${activeBank.day}|${activeBank.person}|${activeBank.slot}`;
      const inp = document.querySelector(`textarea[data-cellkey="${key}"]`);
      activeBank = null; updateFloating(); renderBanks();
      if (inp) { inp.focus(); }
    }'''

new = '''    else if (activeBank) {
      const key = `${activeBank.day}|${activeBank.person}|${activeBank.slot}`;
      const inp = document.querySelector(`textarea[data-cellkey="${key}"]`);
      if (inp) { inp.focus(); }
      activeBank = null; updateFloating(); renderBanks();
    }'''

old_v = 'v2.5.14'
new_v = 'v2.5.15'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v2.5.14', 'meal-planner-v2.5.15')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
