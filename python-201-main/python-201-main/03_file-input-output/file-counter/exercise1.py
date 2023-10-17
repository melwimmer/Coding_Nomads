file_in = open("desktopclutter.txt", "r")
contents = file_in.read()
print(contents)
print(type(contents))
file_in.close()

with open("desktopclutter.txt", "r") as file_in:
    print(file_in.read())  #Using the above construct with the with keyword, which is called a context manager, you'll automatically close the file object after the indented part of your code is done running