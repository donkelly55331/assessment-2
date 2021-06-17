import unittest, itertools
from modules.customer import *
from modules.inventory import *

class StoreTestSuite(unittest.TestCase):

    def test_add_store(self, "Blockbuster"): # First customer, ID should be 1
        self.assertEqual(view_customer, 1)


    def test_add_customer(self, "Don", "Kelly"): # First customer, ID should be 1
        self.assertEqual(view_customer, 1)

    def test_view_customer(self, 3):
        a_cust = customer()
        self.assertEqual(view_inventory, 0)


    def test_view_inventory(self):
        my_inv = Inventory()
        self.assertEqual(view_inventory, 0)

if __name__ == '__main__':
    unittest.main()
