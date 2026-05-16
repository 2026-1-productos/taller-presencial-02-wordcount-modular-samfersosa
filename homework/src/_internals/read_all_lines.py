from pathlib import Path


def read_all_lines(input_folder):
    """Read all lines from all files in the input folder."""
    lines = []
    for file_path in Path(input_folder).iterdir():
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines
