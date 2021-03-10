import pandas as pd
from IPython.display import display



log = pd.read_csv('module_4/log.csv', header=None)
log.columns = ['user_id','time','bet','win']
log = log[~log.user_id.str.contains("error", na=False)]

def extr(s):
    v = s.split('-')
    if(len(v) > 1):
        return f"{v[1].replace(' ' , '')}"
    else:
        return ''

log.user_id = log.user_id.apply(extr)            
log.time = log.time.apply(lambda s:str(s).replace('[',''))     


display(log)
display(log.info())
