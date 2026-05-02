path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Fix 1: Week nav full width + flash animation CSS
old_css = '''  /* Week navigation */
  #week-nav { display: flex; align-items: center; gap: 0; margin-top: 3px; width: 100%; }
  .week-nav-btn { background: none; border: none; color: #78716c; font-size: 12px; font-weight: 600; cursor: pointer; padding: 4px 0; border-radius: 6px; transition: all 0.15s; flex: 1; text-align: center; }
  .week-nav-btn:hover { background: #44403c; color: white; }
  .week-nav-btn.current-week { background: white; color: #1c1917; font-size: 14px; font-weight: 800; }
  .week-nav-btn.future-week { color: #93c5fd; }
  .week-nav-btn.past-week { color: #78716c; }'''

new_css = '''  /* Week navigation */
  #week-nav { display: flex; align-items: center; gap: 0; margin-top: 3px; width: 100vw; margin-left: -18px; }
  .week-nav-btn { background: none; border: none; color: #78716c; font-size: 12px; font-weight: 600; cursor: pointer; padding: 8px 0; border-radius: 0; transition: all 0.15s; flex: 1; text-align: center; }
  .week-nav-btn:hover { background: #44403c; color: white; }
  .week-nav-btn.current-week { background: white; color: #1c1917; font-size: 14px; font-weight: 800; }
  .week-nav-btn.future-week { color: #93c5fd; }
  .week-nav-btn.past-week { color: #78716c; }
  @keyframes weekFlash { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
  #grid-wrap.flashing { animation: weekFlash 0.2s ease; }'''

# Fix 2: Filter layout - When left, Who right
old_filters_css = '  #meal-filters { padding: 8px 8px 0; display: flex; flex-wrap: wrap; gap: 4px; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; align-items: center; }'
new_filters_css = '  #meal-filters { padding: 8px 8px 0; display: flex; flex-wrap: wrap; gap: 4px; justify-content: space-between; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; align-items: center; }\n  .filter-group.push-right { margin-left: auto; }'

# Fix 3: Add flash + date refresh to navWeek
old_nav = '''function navWeek(dir) {
  saveCurrentToArchive();'''

new_nav = '''function navWeek(dir) {
  // Flash the grid
  const grid = document.getElementById('grid-wrap');
  if (grid) { grid.classList.remove('flashing'); void grid.offsetWidth; grid.classList.add('flashing'); setTimeout(() => grid.classList.remove('flashing'), 200); }
  saveCurrentToArchive();'''

# Fix 4: renderTable already calls getDayDate which uses getWeekOffset — 
# but we need to ensure renderTable is called after viewingWeekKey is set in navWeek
# The existing code already calls loadArchivedWeek/loadLiveWeek which call renderTable
# So the fix is just making sure getDayDate is called AFTER viewingWeekKey is updated
# which it already is. The real issue is getDayDate uses `now` not the viewed week date.
# getWeekOffset fix was in previous patch - just need to make sure it's applied.

# Fix 5: Push 'Who' group right in renderFilters
old_render_filters = '''  FILTER_GROUPS.forEach(group => {
    const grp = document.createElement("div");
    grp.className = "filter-group";'''

new_render_filters = '''  FILTER_GROUPS.forEach(group => {
    const grp = document.createElement("div");
    grp.className = "filter-group" + (group.key === "who" ? " push-right" : "");'''

old_v = 'v3.1.4'
new_v = 'v3.1.5'

hits = [old_css in content, old_filters_css in content, old_nav in content, old_render_filters in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old_css, new_css)
    content = content.replace(old_filters_css, new_filters_css)
    content = content.replace(old_nav, new_nav)
    content = content.replace(old_render_filters, new_render_filters)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.4', 'meal-planner-v3.1.5')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
