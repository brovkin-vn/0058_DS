import pandas as pd
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 
# log = log.dropna(axis = 0)
# log.time = log.time.apply(lambda x:str(x)[1:])
# log.time = pd.to_datetime(log.time)
# log['hour'] = log.time.dt.hour
log['bet'] = log['bet'].fillna(0)
log['bet_calc'] = log['bet'].apply(lambda x: 1 if(x == 0.0) else 0)
print(log.sum())


