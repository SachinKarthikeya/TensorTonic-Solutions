import numpy as np

def elu(x, alpha=1):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    x = np.array(x, dtype=float)
    elu = np.where(x > 0, x, alpha * (np.exp(x) - 1))
    return elu.tolist()