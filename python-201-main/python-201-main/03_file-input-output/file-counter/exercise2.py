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

# print(newsuffuxlist)


for i in newsuffuxlist:
    dictionary[i]=newsuffuxlist.count(i)


# print(dictionary)

# # file_out = open("desktopclutter.txt", "w") write mode (always rewrites the file so after the file is created, I wouldn't want to open it like this because it would get overwritten)
# file_out = open("desktopclutter.txt", "a") # 'append' mode
# file_out.write(f'{dictionary}')
# file_out.write('\n')
# file_out.close()
info = []
with open("desktopclutter.txt", "r") as file_in:
    for line in file_in.readlines():
        line = line.rstrip()
        print(line)
        info.append(line)
        # info += file_in.readlines()
print(info)
print('\n'.join(info))


with open ("farlist.txt", "w") as fout:
    fout.write('\n'.join(info))
    
    # print(file_in.read())
    # print(info)
# import csv
# # -- snip --
# count = {'.appref-ms': 1, '': 4, '.ini': 1, '.lnk': 8, '.MX]': 1, '.jpg': 0}

# with open("desktopclutter.csv", "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count['.appref-ms'], count['.ini'], count['.lnk'], count['.jpg']]
#     countwriter.writerow(data)