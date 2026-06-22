import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffeemenu = CoffeeMenu()
    
    def tearDown(self):
        self.coffeemenu = None

    def test_get_price_existing_item(self):
        self.assertEqual(self.coffeemenu.menu['espresso'], 2.50)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.coffeemenu.menu["long black"]

    def test_add_item(self):
        self.coffeemenu.menu.update({"mocha" : 2.00})
        self.assertIn("mocha", self.coffeemenu.menu)

if __name__ == "__main__":
    unittest.main()