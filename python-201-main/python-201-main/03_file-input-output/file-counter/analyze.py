# Use the `csv` module to read in and count the different file types.
from pathlib import Path

filepath = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/file-counter/filecounts.txt")

with filepath.open() as f:
    print(f.read())

# or I can open it like:
# with open(filepath, "r") as file_in:
#     print(file_in.read())