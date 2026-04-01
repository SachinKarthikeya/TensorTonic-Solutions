import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)

    axis = 1 if x.ndim == 2 else 0
    
    x_max = np.max(x, axis=axis, keepdims=True)
    e_x = np.exp(x - x_max)

    e_x_sum = np.sum(e_x, axis=axis, keepdims=True)
    return np.round(e_x / e_x_sum, 4)