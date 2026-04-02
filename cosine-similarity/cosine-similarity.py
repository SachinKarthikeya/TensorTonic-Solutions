import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a, b = np.array(a), np.array(b)

    num = np.dot(a, b)
    denom = np.linalg.norm(a) * np.linalg.norm(b)

    if denom == 0:
        return 0
        
    return num / denom
    pass