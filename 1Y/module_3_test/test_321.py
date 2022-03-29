import json  

with open('./module_3_test/recipes.json') as f:
   recipes = json.load(f)


ingredients = set()  # создаём пустое множество для хранения уникальных значений кухонь
for recipe in recipes:  # начинаем перебор всех рецептов0
    for ingredient in recipe['ingredients']:
        ingredients.add(ingredient) # добавляем название типа кухни к множеству

food = {}  # создаём пустой словарь для хранения информации об ингредиентах
for item in ingredients:  # перебираем список ингредиентов
   food[item] = 0 # добавляем в словарь ключ, соответствующий очередному ингредиенту
for recipe in recipes:   # перебираем список рецептов
    for item in recipe['ingredients']:   # и список ингредиентов в каждом рецепте
        food[item] += 1   # увеличиваем значение нужного ключа в словаре на 1
# Теперь мы можем обращаться к словарю food по ключам и получать информацию о количестве рецептов, включающих тот или иной ингредиент:

print(food['sugar'])
print(food['eggs'])

abc = set()  # создаём пустое множество для хранения уникальных значений кухонь

for f in food:  # начинаем перебор всех рецептов0
    if (food[f] > 100):
        abc.add(f) # добавляем название типа кухни к множеству
print('abc:\n', sorted(abc))            

aa = {'water','olive oil','salt','garlic','pepper'}
print('abc:\n',sorted( abc & aa))   
print(max(food))        
# Какой ингредиент чаще всего встречается в составе блюд?
inverse = [(value, key) for key, value in food.items()]
print(max(inverse)[1])

# Сколько ингредиентов входит в состав только одного блюда?
n = 0
for f in food:  
    if (food[f] == 1):
        n = n + 1
print('asd:\n', n)            
