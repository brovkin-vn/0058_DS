import pandas as pd
import numpy as np
log = pd.read_csv("./module_3_test/log.csv", header=None)
us = pd.read_csv("./module_3_test/users0.csv", encoding="koi8-r", sep='\t')
us.columns = ['user_id', 'emale', 'geo'] 
# print(us)
log.columns = ['user_id', 'time', 'bet', 'win'] 


log['bet'] = log['bet'].fillna(0)
log['win'] = log['win'].fillna(0)
def fill_net(row):
    return row.win - row.bet

log['net'] = log.apply(lambda row: fill_net(row), axis=1) 
log['winwin'] = log.net.apply(lambda x: 1 if x > 0 else 0)   
log['is_bet'] = log.net.apply(lambda x: 1 if x > 0 else 0)   
log['is_no_bet'] = log.net.apply(lambda x: 0 if x == 0 else 1)   

us.user_id = us.user_id.apply(lambda x: x.lower())  
log = log[log.user_id != '#error']  
log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])  
df = pd.merge(us, log, on='user_id')  

sample2 = df.groupby('user_id').user_id.count()
print(sample2)