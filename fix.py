path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old1 = '      headers: {"Content-Type": "application/json"},'
new1 = '      headers: {"Content-Type": "application/json", "x-api-key": getApiKey(), "anthropic-version": "2023-06-01", "anthropic-dangerous-direct-browser-access": "true"},'

old2 = 'async function generateShoppingList() {'
new2 = '''function getApiKey() {
  let key = localStorage.getItem('mealplanner_apikey');
  if (!key) {
    key = prompt('Enter your Anthropic API key (stored locally on this device only):');
    if (key) localStorage.setItem('mealplanner_apikey', key.trim());
  }
  return key;
}

async function generateShoppingList() {'''

old_v = 'v3.0.0'
new_v = 'v3.0.1'

hits = [old1 in content, old2 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.0.0', 'meal-planner-v3.0.1')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
