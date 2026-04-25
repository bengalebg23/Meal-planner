import subprocess

# Update mp alias to include code dump
bashrc = '/data/data/com.termux/files/home/.bashrc'
with open(bashrc, 'r') as f:
    content = f.read()

old = "alias mp='cd ~/meal-planner && git add -A && git commit -m \"update\" && git push origin dev'"
new = "alias mp='cd ~/meal-planner && cp index.html code_dump.txt && git add -A && git commit -m \"update\" && git push origin dev'"

if old in content:
    content = content.replace(old, new)
    with open(bashrc, 'w') as f:
        f.write(content)
    print("mp alias updated")
else:
    print("MISS - mp alias not found")
