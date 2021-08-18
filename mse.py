import numpy as np
y_predicted = np.array([1,1,0,0,1])
y_true = np.array([0.30, 0.70, 1, 0, 0.5])
import math
def mean_squared_error(y_pred, y_true):
    total_error = 0
    for i, j in zip(y_true, y_pred):
        diff = abs(i -j)
        total_error += (diff)**2
    mean = total_error / len(y_true)
    print(mean)
mean_squared_error(y_predicted, y_true)
