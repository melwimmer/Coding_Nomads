# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.



# # import pathlib
import pathlib

#find the files directory 
print(pathlib.Path.cwd())
codingnomads = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-101-main")
for filepath in codingnomads.iterdir():
    print(filepath.name)
    if filepath.is_dir():
        for filepath2 in filepath.iterdir():
            if filepath2.suffix == ".py":
                print(filepath2.name)

# import pathlib

# labsfolder = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Documents/codingnomads/python-101-main")

# for f in labsfolder.iterdir():
#     if f.is_dir():
#         print(f)
#         for f2 in f.iterdir():
#             if f2.is_dir():
#                 print("There are more directories!")
#             else:
#                 print(f"{f2.name:>50}")
#     else:
#         print(labsfolder)
#         print(f"{f.name:>30}")
