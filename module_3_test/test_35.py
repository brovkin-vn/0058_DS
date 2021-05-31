import pandas as pd
import numpy as np
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 

log['bet'] = log['bet'].fillna(0)
log['win'] = log['win'].fillna(0)

def fill_net(row):
    return row.win - row.bet

log['net'] = log.apply(lambda row: fill_net(row), axis=1) 
log['winwin'] = log.net.apply(lambda x: 1 if x > 0 else 0)   
log['is_bet'] = log.bet.apply(lambda x: 1 if x > 0 else 0)   

# print(log.is_bet.count())
# print(log.is_bet.sum())
# print(log.bet)

# print(log.loc[log.bet > 0].bet.mean())
# print(log.loc[log.bet > 0].net.mean())
# print(log.loc[log.net < 0].net.mean())
# print(log.loc[log.net > 0].net.count())
# print(log.loc[log.net < 0].net.count())
print(log.loc[log.bet > 0].bet.min())
print(log.loc[log.bet == log.loc[log.bet > 0].bet.min()].net.count())

min_bet_amount =  log.loc[log.bet == log.loc[log.bet > 0].bet.min()].net.count()