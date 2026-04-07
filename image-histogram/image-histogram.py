def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    histogram = {}
    for row in image:
        for pixel in row:
            if pixel in histogram:
                histogram[pixel] += 1
            else:
                histogram[pixel] = 1
    histogram_list = [histogram.get(pixel, 0) for pixel in range(256)] # To retrieve the count of the specific pixel value from the histogram dictionary.
    return histogram_list