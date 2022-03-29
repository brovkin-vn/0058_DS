import numpy as np
import math
import sys

def logloss(y_pred, y_true):
    # обрезаем нули
    if y_pred == 0: y_pred = sys.float_info.min
    # и единицы
    if y_pred == 1: y_pred = 0.9999999999
    loss = -y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred)
    return loss

loss = np.round(np.nansum([logloss(0.2,0), logloss(0.8,0), logloss(1,1), logloss(0.6,1)]), 2)

print(loss)