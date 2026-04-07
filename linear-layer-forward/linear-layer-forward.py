import numpy as np

def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    lin_layer = np.dot(X, W) + b
    return lin_layer.tolist()