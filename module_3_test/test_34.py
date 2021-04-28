import pandas as pd
import numpy as np
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 

def fillna_win(row):
    if not pd.isna(row.win):
        return row.win
    elif pd.isna(row.win) and pd.isna(row.bet):
        return 0
    elif not pd.isna(row.bet) and pd.isna(row.win):
        return -1
    else:
        return row.win


log.win = log.apply(lambda row: fillna_win(row), axis=1)
log['loss'] = log.win.apply(lambda x: 1 if x == -1 else 0)

def fill_net(row):
    if row.win < 0:
        return row.win
    else:
        return row.win - row.bet

log['net'] = log.apply(lambda row: fill_net(row), axis=1) 
log['winwin'] = log.net.apply(lambda x: 1 if x > 0 else 0)   


# print(log.winwin.sum())

# print(log.loc[log.net > 0].net.mean())
# print(log.loc[log.net > 0].net.median())


print(1,log.bet.mean())
print(2,log.bet.mean(skipna=False))
# print(pd.mean(log['bet']))
print(3, log.bet.sum() / log.bet.dropna().shape[0])
print(4, np.mean(log.bet))
print(5, log['bet'].dropna().mean())
