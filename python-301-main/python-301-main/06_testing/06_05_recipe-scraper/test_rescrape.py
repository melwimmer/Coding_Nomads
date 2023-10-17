# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        index_page = rescrape.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code, 200)
    
    def test_get_html_content(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        # response = rescrape.get_page_content(BASE_URL)
        page = rescrape.get_html_content(BASE_URL)
        self.assertIn("<!DOCTYPE html>", page)

    def test_make_soup_makes_soup(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    def test_get_recipe_links_gets_recipe_links(self):
        index_html = rescrape.get_html_content(self.BASE_URL)
        index_soup = rescrape.make_soup(index_html)
        self.assertGreater(len(rescrape.get_recipe_links(index_soup)), 0)

    def test_get_author_finds_author(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        author = rescrape.get_author(soup)
        self.assertNotEqual(len(author), 0)
        self.assertEqual("Jadafaa", author)

    def test_get_recipe_gets_recipe_text(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        recipe = rescrape.get_recipe(soup)
        self.assertIsInstance(recipe, str)
        self.assertGreater(len(recipe), 0)


if __name__ == "__main__":
    unittest.main()




if __name__ == "__main__":
    unittest.main()


#Note 1: I can use .setUp() method will run before every test, 
# which means that these two variables will be available for each test to use.
#It would work like so:

# class TestRescrape(unittest.TestCase):

#     def setUp(self):
#         self.BASE_URL = "https://codingnomads.github.io/recipes/"
#         self.url = f"{self.BASE_URL}recipes/11-making-my-own-baguet.html"

#Note 2: There is also a python module to test stuff that might be easier to use: pytest
#Explore in the future
