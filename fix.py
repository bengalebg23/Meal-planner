path = '/data/data/com.termux/files/home/.bashrc'
with open(path, 'r') as f:
    content = f.read()

old = 'alias mp="cd ~/meal-planner && cp index.html code_dump.txt && git add -A && git commit -m \\"update\\" && git push origin dev"'
new = 'alias mp="cd ~/meal-planner && VERSION=\\$(grep -o \'v[0-9]*\\.[0-9]*\\.[0-9]*\' index.html | head -1) && cp index.html code_dump_\\${VERSION}.txt && cp index.html code_dump.txt && git add -A && git commit -m \\"update \\${VERSION}\\" && git push origin dev"'

if old in content:
    content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
    print("Current mp line:")
    for line in content.split('\n'):
        if 'alias mp=' in line:
            print(repr(line))
