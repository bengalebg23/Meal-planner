path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '      <button onclick="typeInConfirm()" style="background:#1c1917;color:white;border:none;border-radius:8px;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;">Fill</button>'
new = '      <button onclick="typeInConfirm()" style="background:#1c1917;color:white;border:none;border-radius:8px;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;">Fill</button>\n      <button onclick="injectMeal(\'\')" style="background:#e7e5e4;color:#1c1917;border:none;border-radius:8px;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;">Clear</button>'

old_v = 'v2.5.17'
new_v = 'v2.5.18'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v2.5.17', 'meal-planner-v2.5.18')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
