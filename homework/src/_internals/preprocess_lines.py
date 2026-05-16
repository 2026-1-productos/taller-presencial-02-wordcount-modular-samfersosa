def preprocess_lines(lines):
    """Preprocess lines by converting to lowercase and stripping whitespace."""
    preprocessed = []
    for line in lines:
        preprocessed.append(line.lower().strip())
    return preprocessed
