from numpy.core.numeric import _outer_dispatcher
import pandas as pd
import numpy as np

df = pd.read_csv('./module_5/min_train.csv')


def outliers_iqr(df, col):
    perc25, perc75 = np.percentile(df[col], [25, 75])
    iqr = perc75 - perc25
    low = perc25 - (iqr * 1.5)
    high = perc75 + (iqr * 1.5)
    out_cnt = len(df[df[col] > high]) +  len(df[df[col] < low])
    if out_cnt:
        print(f"{col}:  [{perc25}, {perc75}], [{low}, {high}]")
        print(f"out_cnt:  {out_cnt}, {out_cnt/len(df)*100}%")

outliers_iqr(df, 'score_bki')


#  perc25 = np.percentile(df[column], 25, axis=0)
# perc75 = np.percentile(df[column], 75, axis=0)
# IQR = perc75 - perc25
# low = perc25 - 1.5*IQR
# high = perc75 + 1.5*IQR
# anomaly = len(df[df[column] > high]) + \
#     len(df[df[column] < low])
# if verbose:
#     if mode == 'analysis':
#         print('Наименование признака: {}'.format(column))
#         print('25-й перцентиль: {},'.format(perc25)[:-1], '75-й перцентиль: {},'.format(perc75),
#             'IQR: {}, '.format(IQR), 'Границы выбросов: [{f}, {l}].'.format(f=low, l=high))
#         print('Выбросов, согласно IQR: {} | {:2.2%}'.format(
#             anomaly, anomaly/len(df)))
#     elif mode == 'correction':
#         return low, high