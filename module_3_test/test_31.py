import pandas as pd
df_log = pd.read_csv("./module_3_test/log.csv", header=None)
df_log.columns = ['user_id', 'time', 'bet', 'win'] 
# print(df_log.head())
# Подсчет количества пустых строк
# print(df_log.isna().sum())
# print(df_log.time.isna().sum())
# Удаление пропусков
log = df_log
# print(log.count())
# log = log.dropna(subset=['time'])
# print(log.count())

# Удалите все столбцы, где есть пропуски. 
# print(log.dropna(axis = 1).count())
# Удалите все строки, где есть пропуски.
# print(log.dropna(axis = 0).count())

# если есть пропуски в столбце time далите столбец time.
log = log.dropna(axis = 1, subset=['user_id', 'time'])
print(log.count())