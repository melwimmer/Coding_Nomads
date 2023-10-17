from pathlib import Path

data_path = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/file-counter")

with open(data_path.joinpath("input.txt"), "w") as file_in:
    file_in.write('apple')
with open(data_path.joinpath("input.txt"), "r") as file_in:
    print(file_in.read())

#or I can open it like:
from pathlib import Path

filepath = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/file-counter/input.txt")

with filepath.open() as f:
    print(f.read())