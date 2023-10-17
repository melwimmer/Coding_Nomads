import unittest
import a06_03_unittest_function

class AnimalImages(unittest.TestCase):
    def test_animal_files_are_jpg(self):
        farm_animals = ["alpaca.jpg", "dog.py", "cat.xls", "anaconda.jpg"]
        jpg_farm_animals = []
        animals = a06_03_unittest_function.animals_start_with_a(farm_animals, jpg_farm_animals)
        print(jpg_farm_animals)
        self.assertTrue(bool(animals), True)


if __name__ == "__main__":
    unittest.main()
    