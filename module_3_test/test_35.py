import pandas as pd
import numpy as np
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 

log['bet'] = log['bet'].fillna(0)
log['win'] = log['win'].fillna(0)

def fill_net(row):
    return row.win - row.bet

log['net'] = log.apply(lambda row: fill_net(row), axis=1) 