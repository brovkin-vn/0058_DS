import pandas as pd

# vis_data = pd.read_csv('./module_3_test/train.csv', encoding='ISO-8859-1', low_memory=False)
# mode_state = vis_data.state.value_counts().index[0]
# result = vis_data.state.fillna(mode_state)
# print(mode_state)

data = pd.read_csv('./module_3_test/data_flats.csv',sep=";")
# data.info()
data=data.dropna(axis=0)

print(data)