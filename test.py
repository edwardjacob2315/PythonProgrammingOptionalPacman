import unittest
from script import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction()
        self.transaction.add_item('remote', 2, 7500)
        self.transaction.add_item('kunci', 10, 3500)

    def test_add_item(self):
        # global items
        items = self.transaction.items

        key_list = list(items.keys())
        self.assertEqual(key_list[0], 'remote') #check item name
        self.assertEqual(items['remote'][0], 2) # check item quantitiy
        self.assertEqual(items['remote'][1], 7500) # check item price

        self.assertEqual(key_list[1], 'kunci') #check item name
        self.assertEqual(items['kunci'][0], 10) # check item quantitiy
        self.assertEqual(items['kunci'][1], 3500) # check item price

    def test_change_item_name(self):
        # print(self.transaction.items)
        # print(items)
        self.transaction.update_item_name('remote', 'remote AC')
        self.assertEqual(list(self.transaction.items.keys())[1], 'remote AC')

    def test_change_item_quantity(self):
        # print(self.transaction.items)
        # print(items)
        self.transaction.update_item_qty('remote', 5)
        self.assertEqual(self.transaction.items['remote'][0], 5)

    def test_change_item_price(self):
        # print(self.transaction.items)
        # print(items)
        self.transaction.update_item_price('remote', 7200)
        self.assertEqual(self.transaction.items['remote'][1], 7200)

    def test_delete_item(self):
        self.transaction.delete_item('kunci')
        self.assertNotIn('kunci', self.transaction.items.keys())



if __name__ == '__main__':
    unittest.main()