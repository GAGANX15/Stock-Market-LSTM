import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def evaluate(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(actual, predicted)

    return mse, rmse, mae