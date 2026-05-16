from collections import Counter


def count_words(words):
    """Count occurrences of each word using Counter."""
    return dict(Counter(words))
