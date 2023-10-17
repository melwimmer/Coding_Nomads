import unittest
import ta06_05_revisit_testing

pride_and_prejudice = "python-301-main/05_exceptions/books/pride_and_prejudice.txt"

class BookReading(unittest.TestCase):
    def test_empty_text(self):
        blankbook = ta06_05_revisit_testing.reading_a_blank_book(pride_and_prejudice)
        self.assertFalse(blankbook)


if __name__ == "__main__":
    unittest.main()
