import os


def write_word_counts(output_folder, word_counts):
    """Write word counts sorted alphabetically to a TSV file."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file = os.path.join(output_folder, "wordcount.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in sorted(word_counts.items()):
            f.write(f"{word}\t{count}\n")
