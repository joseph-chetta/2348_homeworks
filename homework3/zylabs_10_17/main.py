# Joseph Chetta 1640405

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        total = self.total_cost()
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total))

if __name__ == '__main__':
    print('Item 1')
    item_name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    print()
    item1 = ItemToPurchase(item_name, price, quantity)

    print('Item 2')
    item_name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    print()
    item2 = ItemToPurchase(item_name, price, quantity)

    total_cost = item1.total_cost() + item2.total_cost()
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print('Total: ${}'.format(total_cost))

