import pathlib
print(pathlib.Path().cwd())
print(pathlib.Path.home())
path = pathlib.Path().cwd()

for filepath in path.iterdir():
    print(filepath)

for filepath in path.iterdir():
    print(filepath.name)