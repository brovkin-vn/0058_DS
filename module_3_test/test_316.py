import pandas as pd
import numpy as np

# vis_data = pd.read_csv('./module_3_test/train.csv', encoding='ISO-8859-1', low_memory=False)
# mode_state = vis_data.state.value_counts().index[0]
# result = vis_data.state.fillna(mode_state)
# print(mode_state)

data = pd.read_csv('./module_3_test/data_flats.csv',sep=";")
# data.info()
# data=data.dropna(axis=0)

# ecology_dict = data.ecology.value_counts().to_dict()
# print(ecology_dict)
# data.ecology = data.ecology.replace(to_replace=ecology_dict)
# print(data.ecology)
# print(data.ecology.mean())


data = pd.get_dummies(data.sub_area, drop_first=True)
data.info()
