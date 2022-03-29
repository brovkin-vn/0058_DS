import pandas as pd
import numpy as np
log = pd.read_csv("./module_3_test/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win'] 
#log.time = log.time.apply(lambda x:str(x)[1:])
log.time = log.time.apply(lambda s:str(s).replace('[',''))     
log.time = pd.to_datetime(log.time)

# print(log)
print(1, log['time'].apply(lambda x: x.month()))
#print(2, log.time.dt.month(inplace=True))
#print(3, log['time'].apply(lambda pandas_dataframe: pandas_dataframe.month))
#print(4, log.time.dt.month)