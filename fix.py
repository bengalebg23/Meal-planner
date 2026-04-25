path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = """function renderTableHighlights() {
  document.querySelectorAll(".meal-cell").forEach(td => {
    const inp = td.querySelector("input");
    if (!inp) return;
    const key = inp.dataset.cellkey;"""

new = """function renderTableHighlights() {
  document.querySelectorAll(".meal-cell").forEach(td => {
    const inp = td.querySelector("textarea");
    if (!inp) return;
    const key = inp.dataset.cellkey;"""

old_v = 'v2.5.2'
new_v = 'v2.5.3'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
