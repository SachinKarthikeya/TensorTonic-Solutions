def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    union = list(set(set_a) | set(set_b))
    intersection = list(set(set_a) & set(set_b))

    if len(union) == 0 or len(intersection) == 0:
        return 0.0

    jcc_sim = len(intersection) / len(union)
    return jcc_sim