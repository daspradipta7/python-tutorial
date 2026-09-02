class ChaiOrder:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def order_summary(self):
        print(f"Order summary: {self.item}: {self.quantity}")


first_order = ChaiOrder("Masala Chai", 2)
first_order.order_summary()

second_order = ChaiOrder("Masala Chai", 2)
first_order.order_summary()