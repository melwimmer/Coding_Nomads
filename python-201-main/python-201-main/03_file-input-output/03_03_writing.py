# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path
data_path = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/words.txt")

words = []
with open(data_path, "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        newline = line[::-1]
     
        words.append(newline)

data_path2 = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/words_reverse.txt")

with open (data_path2, "w") as fout:
    fout.write(str(words))
    

