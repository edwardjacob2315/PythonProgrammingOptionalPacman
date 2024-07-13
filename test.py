import unittest
from script import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction()

    def test_add_item(self):
        self.transaction.add_item('remote', 2, 7500)
        items = self.transaction.items
        self.assertEqual(list(items.keys())[0], 'remote') #check item nane
        self.assertEqual(items['remote'][0], 2) # check item quantitiy
        self.assertEqual(items['remote'][1], 7500) # check item price

if __name__ == '__main__':
    unittest.main()