def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    cos = sum(a*b for a, b in zip(x1, x2)) / (sum(a*a for a in x1)**0.5 * sum(b*b for b in x2)**0.5)

    if label == 1:
        loss = 1 - cos
    else:
        loss = max(0, cos - margin)

    return loss