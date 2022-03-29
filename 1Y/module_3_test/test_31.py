import pandas as pd
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 
# print(df_log.head())
# Подсчет количества пустых строк
print(log.isna().sum())
print(log.time.isna().sum())
# Удаление пропусков
# print(log.count())
# log = log.dropna(subset=['time'])
# print(log.count())

# Удалите все столбцы, где есть пропуски. 
# print(log.dropna(axis = 1).count())
# Удалите все строки, где есть пропуски.
# print(log.dropna(axis = 0).count())
# log = log.dropna(subset=['time'], axis = 0)

# если есть пропуски в столбце time далите столбец time.
# log = log.dropna(axis = 1, subset=['user_id', 'time'])
# print(log.count())

# Удаление дублей
# log = log.drop_duplicates(subset=['user_id', 'time'])
# print(log.count())

# Преобразовнаие даты
# log.time = log.time.apply(lambda x:str(x)[1:])
# log.time = log.time.apply(lambda s:str(s).replace('[',''))     
# log.time = pd.to_datetime(log.time)
# print(f'time_max: {log.time.max()}')
# print(f'time_min: {log.time.min()}')
# log['time'] = log['time'].apply(lambda x: x.second)
# print(log['time'].head)
# log['time'] = log['time'].apply(lambda x: x.minutes)
# print(log['time'].head)
# log.time = log.time.apply(lambda x: x.minute)
# print(log['time'].head)
# log.time = log.time.apply(lambda x: x.hour)
# print(log['time'].head)
# log['time'] = log.time.apply(lambda x: x.minute)
# print(log['time'].head)

# Найдите минуту, которая встречалась в данных чаще всего.
# minute = log.time.apply(lambda x: x.minute)
# print(minute.value_counts())
# Найдите месяц, который встречался в данных реже всего.
# log['month'] = log['time'].apply(lambda x: x.month)
# print(log.month.value_counts())
# Подсчет выходных
# log['dayofweek'] = log.time.dt.dayofweek
# print(dayofweek.value_counts())
# log.dayofweek = log.dayofweek.apply(lambda x: 1 if(x == 5 or x == 6) else 0)
# print(log.dayofweek.sum())

# Посчитайте, какое время дня встречается в данных реже всего.
# log['hour'] = log.time.dt.hour
# log['time_of_day'] = log.hour.apply(lambda x: 0 if(x < 6) else 1 if(x < 12) else 2 if(x < 18) else 3)
# print(log.time_of_day.value_counts())



