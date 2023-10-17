# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.


pride_and_prejudice = "python-301-main/05_exceptions/books/pride_and_prejudice.txt"

def making_a_blank_book (path):
    with open(path, 'w')as pp:
        pp.write("")

def reading_a_blank_book(path):
    with open(path, 'r')as pp:
        return bool(pp.read())

making_a_blank_book(pride_and_prejudice)
reading_a_blank_book(pride_and_prejudice)