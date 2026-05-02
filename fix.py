path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Add dark mode for new elements
old = '''  body.dark .recipe-toggle { color: #78716c; }

  @media print {'''

new = '''  body.dark .recipe-toggle { color: #78716c; }
  body.dark #meal-filters { background: transparent; }
  body.dark .filter-group-label { color: #78716c; }
  body.dark .filter-btn { background: #292524; border-color: #44403c; color: #a8a29e; }
  body.dark .filter-btn.active { background: #e2e0dd; color: #1c1917; border-color: #e2e0dd; }
  body.dark #unified-bank { background: #1c1917; }
  body.dark #unified-bank-header { background: #0f0e0d; }
  body.dark .upill { background: #292524; border-color: #44403c; color: #e2e0dd; }
  body.dark #type-in-bar input { background: #292524; border-color: #44403c; color: #e2e0dd; }
  body.dark #type-in-bar button:first-of-type { background: #e2e0dd; color: #1c1917; }
  body.dark #type-in-bar button:last-of-type { background: #44403c; color: #a8a29e; }

  @media print {'''

old_v = 'v3.1.9'
new_v = 'v3.2.0'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.9', 'meal-planner-v3.2.0')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
