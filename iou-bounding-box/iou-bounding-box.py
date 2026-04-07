def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    def area(box):
        return (box[2] - box[0]) * (box[3] - box[1])

    def intersection(box_a, box_b):
        x_overlap = max(0, min(box_a[2], box_b[2]) - max(box_a[0], box_b[0]))
        y_overlap = max(0, min(box_a[3], box_b[3]) - max(box_a[1], box_b[1]))
        return x_overlap * y_overlap

    area_a = area(box_a)
    area_b = area(box_b)
    intersection_area = intersection(box_a, box_b)
    union_area = area_a + area_b - intersection_area
    iou = intersection_area / union_area
    return iou
    pass