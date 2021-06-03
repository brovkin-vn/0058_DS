import json  
import pandas as pd

def find_item(cell):
    if item in cell:
        return 1
    return 0

with open('./module_3_test/recipes.json') as f:
   recipes = json.load(f)

ingredients = set()
for recipe in recipes: 
    for ingredient in recipe['ingredients']:
        ingredients.add(ingredient) 

df = pd.DataFrame(recipes)

for item in ingredients:
    df[item] = df['ingredients'].apply(find_item)    

df['ingredients'] = df['ingredients'].apply(len)    

# df.info()
print(df.head())

df.to_csv('./module_3_test/recipes.csv', index = False)


