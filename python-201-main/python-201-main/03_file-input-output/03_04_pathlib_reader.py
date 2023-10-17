# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import pathlib

dictionary = {}
suffixlist= []
newsuffuxlist = []
set1 = set()

desktop = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop")

print(type(desktop))

for filepath in desktop.iterdir():
    # Filter for screenshots only
    suffixlist.append(filepath.suffix)

for i in suffixlist:
    if i in suffixlist is list:
        for x in i:
            newsuffuxlist.append(x)
    else:
        newsuffuxlist.append(i)

print(newsuffuxlist)


for i in newsuffuxlist:
    dictionary[i]=newsuffuxlist.count(i)


print(dictionary)

from pathlib import Path
data_path = Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-201-main/python-201-main/03_file-input-output/desktopclutter.txt")


# file_out = open("desktopclutter.txt", "w") write mode (always rewrites the file so after the file is created, I wouldn't want to open it like this because it would get overwritten)
# with open(data_path, "w") as f:
#     f.write(f'{dictionary}\n')

file_out = open(data_path, "a") # 'append' mode
file_out.write(f'{dictionary}\n')
