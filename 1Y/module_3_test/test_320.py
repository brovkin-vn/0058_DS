import json  
from pprint import pprint  

with open('./module_3_test/recipes.json') as f:
   recipes = json.load(f)


# pprint(recipes)
print(len(recipes))
print(recipes[499]['cuisine'])
print(len(recipes[499]['ingredients']))


for recipe in recipes:  # начинаем перебор всех рецептов
   if recipe['id'] == 23629:  # если id текущего рецепта равен искомому
        print(recipe['ingredients'])  # выводим на экран кухню, к которой относится блюдо
        break   # и прерываем цикл, т.к. нужное блюдо уже найденоfor recipe in recipes:  # начинаем перебор всех рецептов

for recipe in recipes:  # начинаем перебор всех рецептов
   if recipe['id'] == 42013:  # если id текущего рецепта равен искомому
        print(len(recipe['ingredients']))  # выводим на экран кухню, к которой относится блюдо
        break   # и прерываем цикл, т.к. нужное блюдо уже найденоfor recipe in recipes:  # начинаем перебор всех рецептов


cuisines = []  # создаём пустой список для хранения уникальных значений кухонь
for recipe in recipes:  # начинаем перебор всех рецептов
   if not(recipe['cuisine'] in cuisines):  # если тип кухни текущего блюда ещё не встречался
        cuisines.append(recipe['cuisine']) # добавляем его к списку cuisines
print(len(cuisines))

cuisines = set()  # создаём пустое множество для хранения уникальных значений кухонь
for recipe in recipes:  # начинаем перебор всех рецептов
   cuisines.add(recipe['cuisine']) # добавляем название типа кухни к множеству
print(len(cuisines))

ingredients = set()  # создаём пустое множество для хранения уникальных значений кухонь
for recipe in recipes:  # начинаем перебор всех рецептов0
    if recipe['cuisine'] == 'russian':
        for ingredient in recipe['ingredients']:
            ingredients.add(ingredient) # добавляем название типа кухни к множеству

print(sorted(ingredients))

