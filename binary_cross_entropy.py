import numpy as np
import math
y_pred = np.array([0.30, 0.70, 1, 0, 0.1])
y_true = np.array([1, 1, 0, 0, 1])

def binary_cross_entropy(y_pred, y_true):
    epsilon = 1e-15 #0.0000000000000001
    y_pred_new = [max(i, epsilon) for i in y_pred]#To replace 0 with epsilon coz log(0) and log(1) becomes infinity
    y_pred_new = [min(i, 1-epsilon) for i in y_pred_new]#To replace 1 with (1-epsilon)
    y_predicted = np.array(y_pred_new)
    return -(np.mean(y_true* np.log(y_predicted) + (1 - y_true) * np.log(1 - y_predicted)))

print(binary_cross_entropy(y_pred, y_true))
