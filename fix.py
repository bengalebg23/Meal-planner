path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = "    hdr.innerHTML = \"🍽 Meal Bank <button onclick='injectMeal(\"????\")' style='margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;'>????</button>\";"
new = '    hdr.innerHTML = `🍽 Meal Bank <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button>`;'

if old in content:
    content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
