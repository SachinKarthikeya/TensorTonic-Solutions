import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)

    vals, counts = np.unique(x, return_counts=True)
    mode = vals[np.argmax(counts)]

    return mean, median, mode
    pass