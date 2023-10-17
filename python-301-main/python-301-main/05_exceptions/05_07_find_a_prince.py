from pathlib import Path
# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

books = Path("python-301-main/05_exceptions/books")

class Prince(Exception):
    def __init__(self, bookpath):
        self.message = f"There is no prince in this {bookpath}."
for book in books.iterdir():
    try:   
        with open (book, "r") as book_text:
            text = book_text.read()[0:100]
            if "Prince" not in text:
                raise Prince(book)
            else:
                print(f'there is a Prince in {book}')
    except Prince as p:
        print(p.message)
    
  
  
