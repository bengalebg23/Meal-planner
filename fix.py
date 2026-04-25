path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '"Roast","Fajitas"]'
new = '"Roast","Fajitas","Tortellini"]'

old_r = '"Fajita + nachos": { tag: "ClaudeRecipe", ingredients: ["600g chicken breast, sliced","2 peppers, sliced","frozen sliced onion","2 tbsp fajita seasoning","Flour tortillas","Sour cream","Guacamole","Grated cheddar","Nachos","Salsa"], notes: "Adults only. Let everyone build their own." },'
new_r = '"Fajita + nachos": { tag: "ClaudeRecipe", ingredients: ["600g chicken breast, sliced","2 peppers, sliced","frozen sliced onion","2 tbsp fajita seasoning","Flour tortillas","Sour cream","Guacamole","Grated cheddar","Nachos","Salsa"], notes: "Adults only. Let everyone build their own." },\n  "Tortellini": { tag: "ClaudeRecipe", ingredients: ["500g fresh tortellini (cheese or meat filled)","1 tin chopped tomatoes","150ml double cream","2 cloves garlic, crushed","1 tsp mixed herbs","Salt and pepper","Parmesan to serve"], notes: "Fry garlic in olive oil for 1 min. Add chopped tomatoes, herbs, salt and pepper and simmer for 10 mins. Stir in cream and simmer for 2 more mins. Cook tortellini per packet (usually 3–4 mins), drain and toss in the sauce. Serve with parmesan." },'

old_v = 'v2.5.3'
new_v = 'v2.5.4'

if old in content and old_r in content:
    content = content.replace(old, new)
    content = content.replace(old_r, new_r)
    content = content.replace(old_v, new_v)
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS - meal list:", old in content)
    print("MISS - recipe anchor:", old_r in content)
