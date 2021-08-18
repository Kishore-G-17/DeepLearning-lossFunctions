import numpy as np
import math
y_true = np.array([1, 1, 0, 0, 1])
y_pred = np.array([0.3, 0.7, 1, 0, 0.1])

def mean_absolute_error(y_pred, y_true):
    total_error = 0
    for i, j in zip(y_true, y_pred):
        total_error += abs(i - j)
    return total_error / len(y_true)

print(mean_absolute_error(y_pred, y_true))
        
