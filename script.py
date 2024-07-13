from tabulate import tabulate


class Transaction:

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        self.items[name] = [quantity, price]

    def update_item_name(self, name, new_name):
        self.items[new_name] = self.items.pop(name)

    def update_item_qty(self, name, new_quantity):
        self.items[name][0] = new_quantity

    def update_item_price(self, name, new_price):
        self.items[name][1] = new_price

    def delete_item(self, name):
        if name in self.items.keys():
            del self.items[name]

    def reset_transaction(self):
        self.items = {}

    def check_order(self):
        if not self.items:
            return 'Pesanan Salah'

        for key, value in self.items.items():
            if not key or not isinstance(value[0], int) or not isinstance(value[1], int):
                return 'Pesanan Salah'

        headers = ['name', 'quantity', 'price']
        data = self.items

        values = [[name, value[0], value[1]] for name, value in data.items()]
        data = tabulate(values, headers=headers, tablefmt='grid')
        print(data)

        return 'Pesanan Benar'

    def total_price(self):

        total_list = []

        for value in self.items.values():

            total = value[0] * value[1]
            total_list.append(total)

        total_belanja = sum(total_list)

        print('Total belanja sebelum diskon', total_belanja)

        if total_belanja > 500000:
            total_belanja = (total_belanja * 90) / 100

        elif total_belanja > 300000:
            total_belanja = total_belanja * 92 / 100

        elif total_belanja > 200000:
            total_belanja = total_belanja * 95 / 100

        return total_belanja
