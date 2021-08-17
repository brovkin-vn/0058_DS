import pandas as pd
import numpy as np

def removeOutliers(data, col):
    Q3 = np.quantile(data[col], 0.75)
    Q1 = np.quantile(data[col], 0.25)
    IQR = Q3 - Q1
     
    print("IQR value for column %s is: %s" % (col, IQR))
    global outlier_free_list 
    global filtered_data
     
    lower_range = Q1 - 1.5 * IQR
    upper_range = Q3 + 1.5 * IQR
    outlier_free_list = [x for x in data[col] if (
        (x >= lower_range) & (x <= upper_range))]
    filtered_data = data.loc[data[col].isin(outlier_free_list)]
    print(col)
    print(filtered_data.info())
    print("\n")
 
  
df = pd.read_csv('./module_5_test/heart_fin1.csv',sep=';')


for col in df.columns[:-1]:
    print('asd')
    removeOutliers(df, col)
    df = filtered_data



