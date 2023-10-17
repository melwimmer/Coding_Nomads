from pathlib import Path

# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

books = Path("python-301-main/05_exceptions/books")

pride_and_prejudice = "python-301-main/05_exceptions/books/pride_and_prejudice.txt"
war_and_peace = "python-301-main/05_exceptions/books/war_and_peace.txt"
with open(war_and_peace, "r") as wp:
    war_and_peace_content = wp.read()
    
with open(pride_and_prejudice, 'w')as pp:
    pp.write("")


for book in books.iterdir():
    try:
        with open (book, "r") as book_text:
            print(book_text.read()[0])
    except IndexError:
        print(f'{book} has no character with index 0 make sure your file is not empty')

