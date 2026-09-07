class BaseChai:
    def __init__(self):
        self.chaiFlavor = "Normal Chai"
        self.chaiBase = "Milk"

class MaslaChai(BaseChai):
    def __init__(self, flavour):
        self.chaiFlavor = flavour
        self.chaiBase = "Milk"

class GingerChai(BaseChai):
    def __init__(self, flavour):
        self.chaiFlavor = flavour
        self.chaiBase = "Milk"

class ChaiOrder:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def order_summary(self):
        print(f"Order summary: {self.item.chaiFlavor}: {self.quantity} with base {self.item.chaiBase}")


first_order = ChaiOrder(MaslaChai("Masala Chai"), 2)
first_order.order_summary()
second_order = ChaiOrder(GingerChai("Ginger Chai"), 3)
second_order.order_summary()