from copy import copy

# def remove_dups(values):
#     val = copy(values)
#     for i in range(1, len(values)+1):
#         if values[-i] in values[:-i]:
#             val.remove(values[-i])
#     return val

# 
import pandas as pd
def remove_dups(values):
    return pd.Series(values).unique().tolist()

    
print(remove_dups([1, 12, 4, 1, 4, 8]))


