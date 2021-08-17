import pandas as pd
import numpy as np
data = pd.read_csv('./module_5_test/glass.csv')
print(len(data['Type'].unique()))
