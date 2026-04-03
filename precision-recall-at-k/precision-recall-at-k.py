def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    intersection = set(top_k) & set(relevant)

    precision = len(intersection) / k
    recall = len(intersection) / len(relevant)

    return [precision, recall]