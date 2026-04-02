import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    image = np.array(image, dtype=float)

    if image.max() <= 1.0:
        image *= 255
        
    weights = np.array([0.299, 0.587, 0.114]) # BT .601 Luminance weights
    grayscaled = np.dot(image, weights)
    return grayscaled.tolist()