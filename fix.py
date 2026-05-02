path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

old = '  "Tortellini": { tag: "ClaudeRecipe", ingredients: ["300g fresh tortellini (cheese or ham & cheese)","Butter","Parmesan to serve","Handful frozen peas (optional)"], notes: "Quick kids\' tea. Cook tortellini per packet, toss in butter and parmesan. Peas add colour and veg without fuss. Can serve with a simple tomato sauce on the side if needed." },'

new = '''  "Tortellini": { tag: "ClaudeRecipe", ingredients: ["300g fresh tortellini (cheese or ham & cheese)","Butter","Parmesan to serve","Handful frozen peas (optional)"], notes: "Quick kids\' tea. Cook tortellini per packet, toss in butter and parmesan. Peas add colour and veg without fuss. Can serve with a simple tomato sauce on the side if needed." },
  "Pulled pork fajitas": { tag: "ClaudeRecipe", ingredients: ["1kg pork shoulder","2 tbsp fajita seasoning","1 tbsp smoked paprika","1 tbsp brown sugar","200ml chicken stock","Flour tortillas","Sour cream","Grated cheddar","Slaw (cabbage, carrot, mayo)","Salsa"], notes: "Slow cooker: rub pork with seasoning, cook on low 8hrs or high 4hrs. Shred with forks. Serve in tortillas with slaw. Great for batch cooking — freezes well." },
  "Tuna pasta": { tag: "ClaudeRecipe", ingredients: ["400g pasta (penne or fusilli)","2 tins tuna chunks, drained","200g crème fraîche","100g frozen sweetcorn","100g frozen peas","frozen garlic","1 tsp mixed herbs","Parmesan to serve","Salt & pepper"], notes: "Cook pasta, drain reserving a cup of water. Fry garlic, add crème fraîche, tuna, sweetcorn and peas. Toss with pasta, loosen with pasta water if needed. Kids love this." },
  "Mozzarella melts": { tag: "ClaudeRecipe", ingredients: ["4 thick slices sourdough or ciabatta","2 balls mozzarella, sliced","4 tomatoes, sliced","Fresh basil","Olive oil","Salt & pepper","Optional: ham or pesto"], notes: "Top bread with tomato, mozzarella and basil. Drizzle with olive oil. Grill for 5-7 mins until bubbling. Quick and popular with kids." },
  "Indian curry": { tag: "ClaudeRecipe", ingredients: ["600g chicken thighs, diced","1 jar tikka masala sauce or homemade","400ml coconut milk","frozen diced onion","frozen garlic","1 inch fresh ginger","1 tsp garam masala","1 tsp turmeric","Basmati rice","Naans to serve","Fresh coriander"], notes: "Adults only. Fry onion, garlic and ginger. Add spices, then chicken and brown. Add sauce and coconut milk, simmer 25 mins. Serve with rice and naans." },
  "Sausage and veg and potatoes": { tag: "ClaudeRecipe", ingredients: ["8 sausages","4 large potatoes, cut into chunks","2 carrots, chopped","1 parsnip, chopped","1 red onion, quartered","Olive oil","Mixed herbs","Salt & pepper","Gravy to serve"], notes: "Roast potatoes and veg at 200°C for 25 mins. Add sausages and roast for a further 25 mins until everything is golden. Simple one-tray tea." },
  "Fish fingers and veg and beans": { tag: "ClaudeRecipe", ingredients: ["12 fish fingers","400g tin baked beans","200g frozen mixed veg (peas, carrots, sweetcorn)","Ketchup to serve"], notes: "Oven cook fish fingers per packet. Heat beans and veg separately. Kids\' classic — no faff required." },'''

old_v = 'v3.0.2'
new_v = 'v3.0.3'

if old in content:
    content = content.replace(old, new)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.0.2', 'meal-planner-v3.0.3')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
