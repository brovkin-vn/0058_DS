import numpy as np

def mult_logloss(y_true, y_pred):
    n, m = y_true.shape[0], y_true.shape[1]
    sum_ = []
    for i in range(n):
        for j in range(m):
            if y_true[i][j] != 0 and y_pred[i][j] != 0:
                sum_.append(y_true[i][j] * np.log(y_pred[i][j]))
    sum_ = np.nansum(sum_)
    loss = -(sum_ / n)
    return loss

y_pred = np.array([[0.2, 0.3, 0.5], [0, 0, 1], [0.1, 0, 0.9]])
y_true = np.array([[0, 0, 1], [0, 0, 1], [1, 0, 0]])

loss_mult = np.round(mult_logloss(y_true, y_pred),2)
print(loss_mult)