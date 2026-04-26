path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# 1. Wire fbSubscribeWeek into loadLiveWeek
old1 = '''function loadLiveWeek() {
  plan = emptyPlan();
  loadFromStorage();
  if (selectedOrderIndex === null) loadBaselineIntoShop();
  else loadSelectedOrderIntoShop();
  renderTable();
  renderBanks();
  renderShop();
  updateMealsDetected();
}'''

new1 = '''function loadLiveWeek() {
  plan = emptyPlan();
  loadFromStorage();
  if (selectedOrderIndex === null) loadBaselineIntoShop();
  else loadSelectedOrderIntoShop();
  renderTable();
  renderBanks();
  renderShop();
  updateMealsDetected();
  const weekKey = localStorage.getItem('mealplanner_week');
  if (weekKey && window.fbSubscribeWeek) window.fbSubscribeWeek(weekKey);
}'''

# 2. Wire fbSubscribeWeek into navWeek when loading archived week
old2 = '''    if (dir === 1 && newKey === currentKey) { viewingWeekKey = null; loadLiveWeek(); }
    else { viewingWeekKey = newKey; loadArchivedWeek(viewingWeekKey); }'''

new2 = '''    if (dir === 1 && newKey === currentKey) { viewingWeekKey = null; loadLiveWeek(); }
    else { viewingWeekKey = newKey; loadArchivedWeek(viewingWeekKey); if (window.fbSubscribeWeek) window.fbSubscribeWeek(newKey); }'''

# 3. Wire fbSubscribeWeek for the back-nav case too
old3 = '''      viewingWeekKey = archiveKeys[archiveKeys.length - 1];
      loadArchivedWeek(viewingWeekKey);'''

new3 = '''      viewingWeekKey = archiveKeys[archiveKeys.length - 1];
      loadArchivedWeek(viewingWeekKey);
      if (window.fbSubscribeWeek) window.fbSubscribeWeek(viewingWeekKey);'''

# 4. Wire fbSubscribeWeek for forward-nav into future week
old4 = '''      viewingWeekKey = getOffsetWeekKey(1);
      loadArchivedWeek(viewingWeekKey);'''

new4 = '''      viewingWeekKey = getOffsetWeekKey(1);
      loadArchivedWeek(viewingWeekKey);
      if (window.fbSubscribeWeek) window.fbSubscribeWeek(viewingWeekKey);'''

# 5. Version bump to v3.0.0
old_v = 'v2.5.19'
new_v = 'v3.0.0'

hits = [old1 in content, old2 in content, old3 in content, old4 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old3, new3)
    content = content.replace(old4, new4)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v2.5.19', 'meal-planner-v3.0.0')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
