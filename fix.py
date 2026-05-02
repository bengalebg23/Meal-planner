path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old_filters = '  #meal-filters { padding: 8px 8px 0; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; margin-bottom: 3px; background: white; border-radius: 8px; padding: 7px 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }'
new_filters = '  #meal-filters { padding: 8px 8px 0; display: flex; flex-wrap: wrap; gap: 4px; }\n  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; align-items: center; }'

old_pill = '  .filter-btn { border-radius: 20px; padding: 4px 11px; font-size: 11px; cursor: pointer; border: 1px solid #e7e5e4; background: #f5f5f4; color: #78716c; }'
new_pill = '  .filter-btn { border-radius: 20px; padding: 0 10px; font-size: 11px; cursor: pointer; border: 1px solid #e7e5e4; background: #f5f5f4; color: #78716c; height: 26px; line-height: 26px; white-space: nowrap; }'

old_flabel = '  .filter-group-label { font-size: 9px; font-weight: 700; color: #a8a29e; text-transform: uppercase; letter-spacing: 0.5px; width: 100%; margin-bottom: 2px; }'
new_flabel = '  .filter-group-label { font-size: 9px; font-weight: 700; color: #a8a29e; text-transform: uppercase; letter-spacing: 0.5px; margin-right: 2px; white-space: nowrap; }'

old_upill = '  .upill { border-radius: 20px; padding: 4px 11px; font-size: 12px; cursor: default; border: 1px solid #e7e5e4; background: #f5f5f4; color: #1c1917; }'
new_upill = '  .upill { border-radius: 20px; padding: 0 11px; font-size: 12px; cursor: default; border: 1px solid #e7e5e4; background: #f5f5f4; color: #1c1917; height: 30px; line-height: 30px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-align: center; }'

old_v = 'v3.1.2'
new_v = 'v3.1.3'

hits = [old_filters in content, old_pill in content, old_flabel in content, old_upill in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old_filters, new_filters)
    content = content.replace(old_pill, new_pill)
    content = content.replace(old_flabel, new_flabel)
    content = content.replace(old_upill, new_upill)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.1.2', 'meal-planner-v3.1.3')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
