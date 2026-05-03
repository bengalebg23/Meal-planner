path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# Add to adults meal bank
old1 = '    items:["Laksa","Thai curry","Indian curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato"],'
new1 = '    items:["Laksa","Thai curry","Indian curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato","Marry me chicken","Marry me salmon"],'

# Add to UNIFIED_MEALS
old2 = '  {name:"Aioli roast veg + chorizo + potato", tags:["tea","pork","adults","medium","one-tray"]},'
new2 = '  {name:"Aioli roast veg + chorizo + potato", tags:["tea","pork","adults","medium","one-tray"]},\n  {name:"Marry me chicken", tags:["tea","chicken","adults","medium"]},\n  {name:"Marry me salmon", tags:["tea","fish","adults","medium"]},'

# Add recipes
old3 = '  "Aioli roast veg + chorizo + potato": { tag: "ClaudeRecipe"'
new3 = '  "Marry me chicken": { tag: "ClaudeRecipe", ingredients: ["4 chicken breasts","150ml double cream","100ml chicken stock","1 tin chopped tomatoes","frozen garlic","1 tsp dried chilli flakes","1 tsp dried oregano","Handful fresh basil","Parmesan to serve","Salt & pepper"], notes: "Adults only. Sear chicken in olive oil, remove and set aside. Fry garlic, add tomatoes, stock, cream, chilli and oregano. Return chicken and simmer 15-20 mins until cooked through. Finish with fresh basil and parmesan. Serve with pasta or crusty bread." },\n  "Marry me salmon": { tag: "ClaudeRecipe", ingredients: ["4 salmon fillets","150ml double cream","100ml fish or veg stock","1 tin chopped tomatoes","frozen garlic","1 tsp dried chilli flakes","1 tsp dried oregano","Handful fresh basil","Parmesan to serve","Salt & pepper"], notes: "Adults only. Same method as marry me chicken but with salmon fillets. Sear skin-side down first. Simmer in the sauce for 10-12 mins only — don\'t overcook the salmon. Serve with pasta or new potatoes." },\n  "Aioli roast veg + chorizo + potato": { tag: "ClaudeRecipe"'

old_v = 'v3.2.8'
new_v = 'v3.2.9'

hits = [old1 in content, old2 in content, old3 in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old1, new1)
    content = content.replace(old2, new2)
    content = content.replace(old3, new3)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.2.8', 'meal-planner-v3.2.9')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
