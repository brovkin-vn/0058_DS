from collections import defaultdict
import pdb  

user_db = [
    {"name": "Elena", "age": 19, "salary": 80_000},
    {"name": "Sergey", "age": 31, "salary": 160_000},
    {"name": "Olga", "age": 33, "salary": 170_000},
    {"name": "Vadim", "age": 17, "salary": 45_000}
]

def group_values(db, value_key, group_key, step):
    grouped = defaultdict(list) 
    for item in db:
        grouped[item[group_key] // step*step].append(item[value_key])
    return dict(grouped)

print(group_values(user_db, "salary", "age", 10))
