import pandas as pd

# pd.set_option('display.max_columns', None) # вывод всех стобцов
data = pd.read_excel("./module_3_test/questions.xlsx", header=None, skiprows=0, na_values=['NA'])
# # Чтобы убирать только те строки, в которых все значения являются пропусками, нужно использовать параметр how и передавать в него значение all.
# data = data.dropna(axis=0, how='all')
# data = data.dropna(axis=1, how='all')
# print(data)