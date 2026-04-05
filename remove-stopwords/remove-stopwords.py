def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    for word in tokens[:]:
        if word in stopwords:
            tokens.remove(word)
    return tokens
    pass