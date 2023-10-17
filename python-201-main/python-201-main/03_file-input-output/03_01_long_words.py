# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

data_path = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/words.txt")

words = []
with open(data_path, "r") as f:
    for lines in f.readlines():
        lines = lines.rstrip()
        words.append(lines)

#print(words)

words20 = []

for w in words:
    if len(w) >= 20: 
        words20.append(w)
print(words20)