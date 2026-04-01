import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    alpha = 1 / (1 + np.exp(-x))
    sw = x * alpha
    return sw