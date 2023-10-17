import pathlib

dictionary = {}
suffixlist= []
newsuffuxlist = []
set1 = set()

desktop = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop")

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

# file_out = open("desktopclutter.txt", "w") write mode (always rewrites the file so after the file is created, I wouldn't want to open it like this because it would get overwritten)
file_out = open("desktopclutter.txt", "a") # 'append' mode
file_out.write(f'{dictionary}')
file_out.write('\n')
file_out.close()


