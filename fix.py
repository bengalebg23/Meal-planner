path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old_bank = '      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank</div>'
new_bank = '      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button></div>'

old_lunch = '        <div class="bank-header">🥪 Lunch Options</div>'
new_lunch = '        <div class="bank-header">🥪 Lunch Options <button onclick="injectMeal(\'????\')" style="margin-left:8px;background:#dc2626;border:none;color:white;border-radius:12px;padding:1px 8px;font-size:10px;font-weight:700;cursor:pointer;">????</button></div>'

old_v = 'v2.5.5'
new_v = 'v2.5.6'

hits = [old_bank in content, old_lunch in content]
if all(hits):
    content = content.replace(old_bank, new_bank)
    content = content.replace(old_lunch, new_lunch)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS - bank header:", hits[0], "lunch header:", hits[1])
