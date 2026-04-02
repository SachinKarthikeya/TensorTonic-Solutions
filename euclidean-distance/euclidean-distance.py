import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x, y = np.array(x), np.array(y)
    square = np.square(x - y)
    sum = np.sum(square)
    result = np.sqrt(sum)
    return result
    pass