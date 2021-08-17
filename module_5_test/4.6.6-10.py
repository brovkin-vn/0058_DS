import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, f1_score, accuracy_score, roc_curve, roc_auc_score, precision_score, recall_score


precision = 0.75
recall = 0.6
f1 = (2*precision*recall) / (precision + recall)
print(round(f1, 2))

y_true= np.array([0,0,1,1,1,1,0,1])
y_pred= np.array([0,1,0,0,1,1,0,1])
f1 = f1_score(y_true, y_pred)
print(round(f1, 2))

y_true= np.array([0,0,1,0,0,1,0])
y_pred= np.array([1,1,1,0,1,1,0])
precision = precision_score(y_true, y_pred)
print(round(precision, 2))


y_true= np.array([0,0,1,0,0,1,0])
y_pred= np.array([1,1,1,0,1,1,0])
recall = recall_score(y_true, y_pred)
print(round(recall , 2))