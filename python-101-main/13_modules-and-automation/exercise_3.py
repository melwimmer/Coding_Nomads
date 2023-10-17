import pathlib


path = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop")
desktop = pathlib.Path("/mnt/c/Users/meme_/OneDrive/Desktop")

print(desktop / "Fotos")

for filepath in desktop.iterdir():
    print(filepath.name)

print(desktop.name)

