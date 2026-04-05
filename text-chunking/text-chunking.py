def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size] #Slices list to take the "chunk_size" tokens
        if i == 0 or len(chunk) == chunk_size:
            chunks.append(chunk)
    return chunks