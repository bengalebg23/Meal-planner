path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Add new quick lunches
old1 = 'const QUICK_LUNCHES = ["Karen\'s","Nursery","School","MIRA","Salad pot","Chicken","Peppers","Skewers","Garlic bites","Ravioli","Pâté","Soup + pâté","Sandwiches","PB toast","Avo toast"];'
new1 = 'const QUICK_LUNCHES = ["Karen\'s","Nursery","School","MIRA","Salad pot","Chicken","Peppers","Skewers","Garlic bites","Ravioli","Pâté","Soup + pâté","Sandwiches","PB toast","Avo toast","Pasta and sauce","Pinwheels","Quiche","Soup","Fish finger sandwiches"];'

# Add new everyone teas
old2 = '"Roast","Fajitas","Tortellini","????"]'
new2 = '"Roast","Fajitas","Tortellini","????","Pulled pork fajitas","Tuna pasta","Mozzarella melts","Sausage and veg and potatoes","Fish fingers and veg and beans"]'

# Add Indian curry to adults
old3 = 'items:["Laksa","Thai curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato"],'
new3 = 'items:["Laksa","Thai curry","Indian curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato"],'

old_v = 'v3.0.1'
new_v = 'v3.0.2'

hits = [old1 in content, old2 in content, old3 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old3, new3)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.0.1', 'meal-planner-v3.0.2')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
