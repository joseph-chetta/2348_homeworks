# Joseph Chetta 1640405

class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        total = self.total_cost()
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_in_cart = False
        for item in self.cart_items:
            if item.item_name == item_name:
                item_in_cart = True
                self.cart_items.remove(item)
        if not item_in_cart:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item_name, quantity):
        item_in_cart = False
        for item in self.cart_items:
            if item_name == item.item_name:
                item_in_cart = True
                modified_item = ItemToPurchase(item_name, item.item_description, item.item_price, quantity)
                item.item_quantity = modified_item.item_quantity
        if not item_in_cart:
            print('Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.total_cost()
        return total

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        num_items = self.get_num_items_in_cart()
        print('Number of Items: {}\n'.format(num_items))
        if self.cart_items:
            for item in self.cart_items:
                item.print_item_cost()
            print()
            total = self.get_cost_of_cart()
            print('Total: ${}\n'.format(total))
        else:
            print('SHOPPING CART IS EMPTY\n')
            print('Total: $0\n')

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for item in self.cart_items:
            item.print_item_description()
        print()

def print_menu_options():
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print('o - Output shopping cart')
    print('q - Quit\n')

def print_menu(cart):
    print_menu_options()
    option = None
    while option != 'q':
        option = input('Choose an option:')
        print()
        if option == 'q':
            break
        elif option == 'a':
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:\n')
            description = input('Enter the item description:\n')
            price = int(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:'))
            print()
            print()
            item = ItemToPurchase(item_name, description, price, quantity)
            cart.add_item(item)
            print_menu_options()
        elif option == 'r':
            print('\nREMOVE ITEM FROM CART')
            item_name = input("Enter name of item to remove:")
            print()
            cart.remove_item(item_name)
            print()
            print_menu_options()
        elif option == 'c':
            print('CHANGE ITEM QUANTITY')
            item_name = input('Enter the item name:\n')
            quantity = int(input('Enter the new quantity:\n'))
            cart.modify_item(item_name, quantity)
            print_menu_options()
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            print_menu_options()
        elif option == 'o':
            print('OUTPUT SHOPPING CART')
            cart.print_total()
            print_menu_options()


if __name__ == '__main__':
    cust_name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    cart = ShoppingCart(cust_name, date)
    print('Customer name: {}'.format(cust_name))
    print("Today's date: {}\n".format(date))

    print_menu(cart)


