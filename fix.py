path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = """        inp.onfocus = () => {
          if (multiSelected.size > 0) {
            if (multiSelected.has(cellKey)) {
              multiSelected.delete(cellKey);
            } else {
              multiSelected.add(cellKey);
            }
            inp.blur();
            updateFloating();
            updateBankHighlight();
            renderTableHighlights();
          } else {
            activeBank = {day: dayKey, person, slot};
            updateFloating();
            updateBankHighlight();
            updateTableHighlight();
          }
        };
        // Double-tap to toggle multi-select
        const cellKey = dayKey + "|" + person + "|" + slot;"""

new = """        // cellKey must be declared before onfocus closure
        const cellKey = dayKey + "|" + person + "|" + slot;
        inp.onfocus = () => {
          if (multiSelected.size > 0) {
            if (multiSelected.has(cellKey)) {
              multiSelected.delete(cellKey);
            } else {
              multiSelected.add(cellKey);
            }
            inp.blur();
            updateFloating();
            updateBankHighlight();
            renderTableHighlights();
          } else {
            activeBank = {day: dayKey, person, slot};
            updateFloating();
            updateBankHighlight();
            updateTableHighlight();
          }
        };
        // Double-tap to toggle multi-select"""

# Version bump
old_v = 'v2.5.1'
new_v = 'v2.5.2'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS - old not found")
