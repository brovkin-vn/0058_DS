import pandas as pd
import os

files = os.listdir('module_3/data')
# print(files)

# files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
# # print(files) 
# data = []
# for f in files:
#     if '.txt' in f:
#         data.append(f)

# print(data)

for root, dirs, files in os.walk('module_3/data'):
    print(root, dirs, files)

# print(files)
data = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])


for filename in files:
    temp = pd.read_csv( os.path.join('module_3/data', filename), names = ['userId', 'movieId', 'rating', 'timestamp'] )
    data = pd.concat([data, temp])

print(data.count())