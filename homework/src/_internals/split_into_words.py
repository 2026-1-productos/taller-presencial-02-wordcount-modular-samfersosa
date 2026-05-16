def split_into_words(lines):
    """Split preprocessed lines into individual words, removing punctuation."""
    words = []
    for line in lines:
        for word in line.split():
            cleaned = word.strip(",.!?;:")
            if cleaned:
                words.append(cleaned)
    return words
