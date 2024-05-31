class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"Item: {self.name}, Price:{self.price}"

class Cart:
    def __init__(self, order_number):
        self.order_number = order_number
        self.items = []
bread = Item("Broadways", 100)
smocha = Item("smocha", 60)

new_cart = Cart(1)
new_cart.items.append(bread)
bread.price = 90

print(new_cart.items)
