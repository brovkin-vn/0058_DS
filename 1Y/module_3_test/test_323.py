import pandas as pd
import numpy as np
import json

df = pd.read_csv('./module_3_test/recipes.csv')

new_recipes = []
ids = df.id.to_list()
ingredients = list(df.columns[3:])

# def make_list(row):
#     r = list()
#     for i in ingredients:
#         if row[i].loc[row.index[0]] > 0:
#             r.append(i)
    
#     return r

def make_list(row):
    lst = [item for item in ingredients if row[item].iloc[0] > 0]    

    return lst

for current_id in ids:
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0]
    current_ingredients = make_list(df[df['id'] == current_id])
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients}
    new_recipes.append(current_recipe)

with open("./module_3_test/new_recipes.json", "w") as write_file:
    json.dump(new_recipes, write_file)    