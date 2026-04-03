import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred, y_true = np.array(y_pred), np.array(y_true)

    n = np.size(y_true)

    sum = np.sum(np.square(y_true - y_pred))
    mse = 1 / n * sum

    return mse.tolist()
    pass
