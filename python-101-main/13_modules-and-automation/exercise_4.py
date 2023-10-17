# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop")

# List all the files on there
for filepath in desktop.iterdir():
    print(filepath.name)


# Filter for screenshots only
# for filepath in desktop.iterdir():
#     print(filepath.suffix)
# This one names all the suffixes

# for filepath in desktop.iterdir():
#     if filepath.suffix == '.jpg':  # Filter for screenshots only
#         print(filepath.name)
# Create a new folder
new_path = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop/Screenshots")
new_path.mkdir(exist_ok=True)
# new_path.mkdir(exist_ok=True) used if the directory already exists. And you should create the folder before the for loop

# Move the screenshots in there
# 
for filepath in desktop.iterdir():
    # Filter for screenshots only
    if filepath.suffix == '.jpg':
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)