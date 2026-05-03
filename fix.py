path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '''function getCurrentWeekKey() {
  // ISO week number based key e.g. "2026_W16"
  const now = new Date();
  const jan4 = new Date(now.getFullYear(), 0, 4);
  const weekNum = Math.ceil(((now - jan4) / 86400000 + jan4.getDay() + 1) / 7);
  return `${now.getFullYear()}_W${String(weekNum).padStart(2,'0')}`;
}'''

new = '''function getCurrentWeekKey() {
  // Proper ISO 8601 week number
  const now = new Date();
  const d = new Date(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()));
  const dayNum = d.getUTCDay() || 7; // Mon=1, Sun=7
  d.setUTCDate(d.getUTCDate() + 4 - dayNum); // nearest Thursday
  const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  const weekNum = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
  return `${d.getUTCFullYear()}_W${String(weekNum).padStart(2,'0')}`;
}'''

old2 = '''function getOffsetWeekKey(n) {
  const now = new Date();
  now.setDate(now.getDate() + n * 7);
  const jan4 = new Date(now.getFullYear(), 0, 4);
  const w = Math.ceil(((now - jan4) / 86400000 + jan4.getDay() + 1) / 7);
  return now.getFullYear() + '_W' + String(w).padStart(2, '0');
}'''

new2 = '''function getOffsetWeekKey(n) {
  const now = new Date();
  now.setDate(now.getDate() + n * 7);
  const d = new Date(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()));
  const dayNum = d.getUTCDay() || 7;
  d.setUTCDate(d.getUTCDate() + 4 - dayNum);
  const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  const w = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
  return `${d.getUTCFullYear()}_W${String(w).padStart(2,'0')}`;
}'''

old_v = 'v3.2.7'
new_v = 'v3.2.8'

hits = [old in content, old2 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old, new)
    content = content.replace(old2, new2)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.7', 'meal-planner-v3.2.8')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
