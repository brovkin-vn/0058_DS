import pandas as pd
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
print(log.loss.sum())


