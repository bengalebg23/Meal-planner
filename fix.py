path = '/data/data/com.termux/files/home/meal-planner/index.html'
with open(path, 'r') as f:
    content = f.read()

# 1. Add filter CSS
old_css = '  #banks { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 10px 8px 0; }'
new_css = '''  #meal-filters { padding: 8px 8px 0; display: flex; flex-wrap: wrap; gap: 5px; }
  .filter-group { display: flex; flex-wrap: wrap; gap: 3px; margin-bottom: 3px; }
  .filter-group-label { font-size: 9px; font-weight: 700; color: #a8a29e; text-transform: uppercase; letter-spacing: 0.5px; width: 100%; margin-bottom: 2px; }
  .filter-btn { border-radius: 20px; padding: 4px 11px; font-size: 11px; cursor: pointer; border: 1px solid #e7e5e4; background: #f5f5f4; color: #78716c; }
  .filter-btn.active { background: #1c1917; color: white; border-color: #1c1917; }
  #unified-bank { background: white; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); overflow: hidden; margin: 8px 8px 0; }
  #unified-bank-header { background: #292524; color: white; padding: 8px 13px; font-size: 12px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; }
  #unified-bank-header span { font-size: 9px; color: #a8a29e; margin-left: 5px; font-weight: 400; }
  #unified-bank-pills { padding: 9px; display: flex; flex-wrap: wrap; gap: 6px; }
  .upill { border-radius: 20px; padding: 4px 11px; font-size: 12px; cursor: default; border: 1px solid #e7e5e4; background: #f5f5f4; color: #1c1917; }
  .upill.active-bank { cursor: pointer; }
  .upill.active-bank:hover { opacity: 0.85; }
  #banks { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 10px 8px 0; }'''

# 2. Add tag data to MEAL_BANK_SECTIONS and unified bank data
old_sections = '''const MEAL_BANK_SECTIONS = [
  {
    key:"all", label:"👨‍👩‍👧‍👦 Everyone", color:"#1c1917", bg:"#f5f5f4",
    items:["Karen's","Nursery","MIRA","Spaghetti Bolognese","Sausage potato bean","Fish pie","Lasagne","Fish cakes + wedges","Stir fry","Tinga + rice","Cottage pie","Chicken & leek bake","Burgers","Sausage orzo","One pot garlic chicken","Teriyaki skewers","Chilli","Pizza","Roast","Fajitas","Tortellini","????","Pulled pork fajitas","Tuna pasta","Mozzarella melts","Sausage and veg and potatoes","Fish fingers and veg and beans"],
  },
  {
    key:"adults", label:"🧑 Adults only", color:"#7c3aed", bg:"#ede9fe",
    items:["Laksa","Thai curry","Indian curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato"],
  },
  {
    key:"kids", label:"🧒 Kids", color:"#0369a1", bg:"#e0f2fe",
    items:["Chicken Alfredo","Pitta pizza","Fish fingers + wedges","Porridge fingers","Mac & cheese","Pasta sauce","Snack Attack","Dairylea Dunker","Tortellini"],
  },
];'''

new_sections = '''const MEAL_BANK_SECTIONS = [
  {
    key:"all", label:"👨‍👩‍👧‍👦 Everyone", color:"#1c1917", bg:"#f5f5f4",
    items:["Karen's","Nursery","MIRA","Spaghetti Bolognese","Sausage potato bean","Fish pie","Lasagne","Fish cakes + wedges","Stir fry","Tinga + rice","Cottage pie","Chicken & leek bake","Burgers","Sausage orzo","One pot garlic chicken","Teriyaki skewers","Chilli","Pizza","Roast","Fajitas","Tortellini","????","Pulled pork fajitas","Tuna pasta","Mozzarella melts","Sausage and veg and potatoes","Fish fingers and veg and beans"],
  },
  {
    key:"adults", label:"🧑 Adults only", color:"#7c3aed", bg:"#ede9fe",
    items:["Laksa","Thai curry","Indian curry","Fajita + nachos","Loaded nachos","Sourdough chicken kievs","Mushroom burgers","Spinach ricotta pasta bake","Greek feta salad","Aioli roast veg + chorizo + potato"],
  },
  {
    key:"kids", label:"🧒 Kids", color:"#0369a1", bg:"#e0f2fe",
    items:["Chicken Alfredo","Pitta pizza","Fish fingers + wedges","Porridge fingers","Mac & cheese","Pasta sauce","Snack Attack","Dairylea Dunker","Tortellini"],
  },
];

// Unified meal bank with tags
const UNIFIED_MEALS = [
  {name:"Spaghetti Bolognese", tags:["tea","beef","everyone","medium","pasta"]},
  {name:"Sausage potato bean", tags:["tea","pork","everyone","medium","one-pot"]},
  {name:"Fish pie", tags:["tea","fish","everyone","slow","bake"]},
  {name:"Lasagne", tags:["tea","beef","everyone","slow","pasta","freezable"]},
  {name:"Fish cakes + wedges", tags:["tea","fish","everyone","medium"]},
  {name:"Stir fry", tags:["tea","chicken","everyone","quick"]},
  {name:"Tinga + rice", tags:["tea","chicken","everyone","medium","rice"]},
  {name:"Cottage pie", tags:["tea","beef","everyone","slow","bake"]},
  {name:"Chicken & leek bake", tags:["tea","chicken","everyone","medium","bake"]},
  {name:"Burgers", tags:["tea","beef","everyone","quick"]},
  {name:"Sausage orzo", tags:["tea","pork","everyone","medium","pasta","one-pot"]},
  {name:"One pot garlic chicken", tags:["tea","chicken","everyone","medium","one-pot"]},
  {name:"Teriyaki skewers", tags:["tea","chicken","everyone","medium","rice"]},
  {name:"Chilli", tags:["tea","beef","everyone","medium","one-pot","freezable"]},
  {name:"Pizza", tags:["tea","everyone","quick"]},
  {name:"Roast", tags:["tea","everyone","slow"]},
  {name:"Fajitas", tags:["tea","chicken","everyone","quick"]},
  {name:"Tortellini", tags:["tea","everyone","quick","pasta"]},
  {name:"Pulled pork fajitas", tags:["tea","pork","everyone","slow","freezable"]},
  {name:"Tuna pasta", tags:["tea","fish","everyone","quick","pasta"]},
  {name:"Mozzarella melts", tags:["tea","everyone","quick"]},
  {name:"Sausage and veg and potatoes", tags:["tea","pork","everyone","medium","one-tray"]},
  {name:"Fish fingers and veg and beans", tags:["tea","fish","everyone","quick"]},
  {name:"Laksa", tags:["tea","chicken","adults","medium"]},
  {name:"Thai curry", tags:["tea","chicken","adults","medium","curry"]},
  {name:"Indian curry", tags:["tea","chicken","adults","medium","curry"]},
  {name:"Fajita + nachos", tags:["tea","chicken","adults","quick"]},
  {name:"Loaded nachos", tags:["tea","beef","adults","quick"]},
  {name:"Sourdough chicken kievs", tags:["tea","chicken","adults","medium"]},
  {name:"Mushroom burgers", tags:["tea","veggie","adults","quick"]},
  {name:"Spinach ricotta pasta bake", tags:["tea","veggie","adults","medium","pasta","bake"]},
  {name:"Greek feta salad", tags:["tea","veggie","adults","quick","salad"]},
  {name:"Aioli roast veg + chorizo + potato", tags:["tea","pork","adults","medium","one-tray"]},
  {name:"Chicken Alfredo", tags:["tea","chicken","kids","quick","pasta"]},
  {name:"Pitta pizza", tags:["tea","kids","quick"]},
  {name:"Fish fingers + wedges", tags:["tea","fish","kids","quick"]},
  {name:"Porridge fingers", tags:["tea","kids","quick"]},
  {name:"Mac & cheese", tags:["tea","veggie","kids","medium","pasta"]},
  {name:"Pasta sauce", tags:["tea","veggie","kids","quick","pasta"]},
  {name:"Snack Attack", tags:["tea","kids","quick"]},
  {name:"Dairylea Dunker", tags:["tea","kids","quick"]},
  {name:"Karen's", tags:["lunch","tea","everyone"]},
  {name:"Nursery", tags:["lunch","tea","everyone"]},
  {name:"MIRA", tags:["lunch","tea","everyone"]},
  {name:"????", tags:["lunch","tea","everyone"]},
  {name:"Sandwich", tags:["lunch","everyone","quick"]},
  {name:"Salad pot", tags:["lunch","adults","quick","salad"]},
  {name:"Pasta and sauce", tags:["lunch","everyone","quick","pasta"]},
  {name:"Pinwheels", tags:["lunch","everyone","quick"]},
  {name:"Quiche", tags:["lunch","everyone","medium"]},
  {name:"Soup", tags:["lunch","everyone","quick"]},
  {name:"Fish finger sandwiches", tags:["lunch","fish","everyone","quick"]},
  {name:"Pâté", tags:["lunch","adults","quick"]},
  {name:"Soup + pâté", tags:["lunch","adults","quick"]},
  {name:"Pizza pockets", tags:["lunch","kids","quick"]},
  {name:"Omelette", tags:["lunch","egg","everyone","quick"]},
  {name:"Scrambled eggs", tags:["lunch","egg","everyone","quick"]},
  {name:"Tortilla", tags:["lunch","kids","quick"]},
  {name:"PB toast", tags:["lunch","kids","quick"]},
  {name:"Avo toast", tags:["lunch","everyone","quick"]},
  {name:"Crumpets", tags:["lunch","kids","quick"]},
  {name:"Pitta pizza", tags:["lunch","kids","quick"]},
];

const FILTER_GROUPS = [
  {key:"when",   label:"When",    filters:["lunch","tea"]},
  {key:"who",    label:"Who",     filters:["everyone","adults","kids"]},
  {key:"protein",label:"Protein", filters:["beef","chicken","pork","fish","veggie","egg"]},
  {key:"effort", label:"Effort",  filters:["quick","medium","slow"]},
  {key:"style",  label:"Style",   filters:["pasta","rice","curry","bake","one-pot","one-tray","salad","freezable"]},
];

let activeFilters = new Set();'''

# 3. Add filter bar HTML before type-in bar
old_html = '  <div id="type-in-bar" style="padding:6px 8px 0;">'
new_html = '''  <div id="meal-filters"></div>
  <div id="unified-bank">
    <div id="unified-bank-header">🍽 Meal Bank <span id="unified-bank-hint"></span></div>
    <div id="unified-bank-pills"></div>
  </div>
  <div id="type-in-bar" style="padding:6px 8px 0;">'''

# 4. Add renderUnifiedBank and renderFilters functions before renderBanks
old_fn = 'function renderBanks() {'
new_fn = '''function renderFilters() {
  const div = document.getElementById("meal-filters");
  div.innerHTML = "";
  FILTER_GROUPS.forEach(group => {
    const grp = document.createElement("div");
    grp.className = "filter-group";
    const lbl = document.createElement("div");
    lbl.className = "filter-group-label";
    lbl.textContent = group.label;
    grp.appendChild(lbl);
    group.filters.forEach(f => {
      const btn = document.createElement("button");
      btn.className = "filter-btn" + (activeFilters.has(f) ? " active" : "");
      btn.textContent = f;
      btn.onclick = () => {
        if (activeFilters.has(f)) activeFilters.delete(f);
        else activeFilters.add(f);
        renderFilters();
        renderUnifiedBank();
      };
      grp.appendChild(btn);
    });
    div.appendChild(grp);
  });
}

function getFilteredMeals() {
  if (activeFilters.size === 0) return UNIFIED_MEALS;
  return UNIFIED_MEALS.filter(m => [...activeFilters].every(f => m.tags.includes(f)));
}

function renderUnifiedBank() {
  const pillsDiv = document.getElementById("unified-bank-pills");
  pillsDiv.innerHTML = "";
  const hint = document.getElementById("unified-bank-hint");
  const isActive = activeBank || multiSelected.size > 0;

  // Update header
  const hdr = document.getElementById("unified-bank-header");
  if (activeBank) {
    const dayLabel = DAYS.find(d => d.key === activeBank.day)?.label || "";
    hdr.innerHTML = `🍽 Meal Bank <span>→ tap to fill ${activeBank.person} ${activeBank.slot === "L" ? "lunch" : "tea"} on ${dayLabel}</span>`;
  } else if (multiSelected.size > 0) {
    hdr.innerHTML = `🍽 Meal Bank <span>→ tap to fill ${multiSelected.size} cells</span>`;
  } else {
    hdr.innerHTML = "🍽 Meal Bank";
  }

  const meals = getFilteredMeals();
  if (meals.length === 0) {
    pillsDiv.innerHTML = '<div style="padding:8px;font-size:11px;color:#a8a29e;">No meals match these filters</div>';
    return;
  }
  meals.forEach(m => {
    const btn = document.createElement("button");
    btn.className = "upill" + (isActive ? " active-bank" : "");
    btn.textContent = m.name;
    if (isActive) btn.onclick = () => injectMeal(m.name);
    pillsDiv.appendChild(btn);
  });
}

function renderBanks() {'''

# 5. Call renderFilters and renderUnifiedBank from renderBanks, and hide old banks
old_banks_end = '''  // Bank header hint
  const hdr = document.getElementById("meal-bank-header");
  if (activeBank) {
    const dayLabel = DAYS.find(d => d.key === activeBank.day)?.label || "";
    hdr.innerHTML = `🍽 Meal Bank <span>→ tap to fill ${activeBank.person} ${activeBank.slot === "L" ? "lunch" : "tea"} on ${dayLabel}</span>`;
  } else {
    hdr.innerHTML = "🍽 Meal Bank";
  }
}'''

new_banks_end = '''  // Bank header hint
  const hdr = document.getElementById("meal-bank-header");
  if (activeBank) {
    const dayLabel = DAYS.find(d => d.key === activeBank.day)?.label || "";
    hdr.innerHTML = `🍽 Meal Bank <span>→ tap to fill ${activeBank.person} ${activeBank.slot === "L" ? "lunch" : "tea"} on ${dayLabel}</span>`;
  } else {
    hdr.innerHTML = "🍽 Meal Bank";
  }
  renderFilters();
  renderUnifiedBank();
}'''

# 6. Hide old banks section (keep notes)
old_banks_html = '''  <div id="banks">
    <div class="bank-card">
      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank</div>
      <div id="meal-bank-pills"></div>
    </div>
    <div id="right-banks">
      <div class="bank-card">
        <div class="bank-header">🥪 Lunch Options</div>
        <div id="lunch-grid">
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#fffbeb;color:#b45309">⚡ Quick</div>
            <div class="lunch-col-items" id="quick-lunches"></div>
          </div>
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#e0f2fe;color:#0369a1">🍳 Cooked</div>
            <div class="lunch-col-items" id="cooked-lunches"></div>
          </div>
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#d1fae5;color:#065f46">🧒 Viv</div>
            <div class="lunch-col-items" id="viv-lunches"></div>
          </div>
        </div>
      </div>
      <div class="bank-card">
        <div class="bank-header">📝 Notes</div>
        <textarea id="notes-ta" oninput="saveToStorage()" placeholder="defrost chicken Tues&#10;need pitta bread&#10;Reuben school trip Fri"></textarea>
      </div>
    </div>
  </div>'''

new_banks_html = '''  <div id="banks" style="display:none">
    <div class="bank-card">
      <div class="bank-header" id="meal-bank-header">🍽 Meal Bank</div>
      <div id="meal-bank-pills"></div>
    </div>
    <div id="right-banks">
      <div class="bank-card">
        <div class="bank-header">🥪 Lunch Options</div>
        <div id="lunch-grid">
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#fffbeb;color:#b45309">⚡ Quick</div>
            <div class="lunch-col-items" id="quick-lunches"></div>
          </div>
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#e0f2fe;color:#0369a1">🍳 Cooked</div>
            <div class="lunch-col-items" id="cooked-lunches"></div>
          </div>
          <div class="lunch-col">
            <div class="lunch-col-header" style="background:#d1fae5;color:#065f46">🧒 Viv</div>
            <div class="lunch-col-items" id="viv-lunches"></div>
          </div>
        </div>
      </div>
      <div class="bank-card">
        <div class="bank-header">📝 Notes</div>
        <textarea id="notes-ta" oninput="saveToStorage()" placeholder="defrost chicken Tues&#10;need pitta bread&#10;Reuben school trip Fri"></textarea>
      </div>
    </div>
  </div>'''

old_v = 'v3.0.3'
new_v = 'v3.1.0'

hits = [old_css in content, old_sections in content, old_html in content, old_fn in content, old_banks_end in content, old_banks_html in content]
print("Hits:", hits)
if all(hits):
    content = content.replace(old_css, new_css)
    content = content.replace(old_sections, new_sections)
    content = content.replace(old_html, new_html)
    content = content.replace(old_fn, new_fn)
    content = content.replace(old_banks_end, new_banks_end)
    content = content.replace(old_banks_html, new_banks_html)
    content = content.replace(old_v, new_v)
    content = content.replace('meal-planner-v3.0.3', 'meal-planner-v3.1.0')
    with open(path, 'w') as f:
        f.write(content)
    print("Done")
else:
    print("MISS")
