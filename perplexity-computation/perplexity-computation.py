import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    n = len(actual_tokens)
    log_prob_sum = 0
    for i in range(n):
        token_prob = prob_distributions[i][actual_tokens[i]]
        log_prob_sum += math.log(token_prob)
    perplexity = math.exp(-log_prob_sum / n)
    return perplexity