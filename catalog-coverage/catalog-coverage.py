def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    unique_recomms = set()
    for sublist in recommendations:
        for item in sublist:
            unique_recomms.add(item)

    coverage = len(unique_recomms) / n_items
    return coverage