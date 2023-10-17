# Write the file counts to a `.csv` file.

from pathlib import Path

filepath = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/file-counter/filecounts.csv")


import csv
# -- snip -- count I got from what was printed from the previous document. 
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open(filepath, "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)