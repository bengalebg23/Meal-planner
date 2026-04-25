import os
path = os.path.expanduser('~') + '/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Check exact whitespace
idx = content.find('inp.onfocus')
print(repr(content[idx-20:idx+200]))
