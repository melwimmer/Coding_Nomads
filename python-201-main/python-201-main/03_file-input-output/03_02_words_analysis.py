# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from pathlib import Path

data_path = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/words.txt")

words = []
with open(data_path, "r") as f:
    for lines in f.readlines():
        lines = lines.rstrip()
        words.append(lines[0::-1])
        print(words)

# print(words)

minlen = (len(min(words, key=len))) 
maxlen = (len(max(words, key=len))) 

print(min(words))
print(len(min(words, key=len)))
print(max(words))
print(len(max(words, key=len)))
wordsmin = []
wordsmax = []

for w in words:
    if len(w) == minlen: 
        wordsmin.append(w)
print(wordsmin)

for w in words:
    if len(w) == maxlen: 
        wordsmax.append(w)
print(wordsmax)

print(len(words))

