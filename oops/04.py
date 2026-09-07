class BaseChai:
    def __init__(self, flavour, base):
        self.chaiFlavor = flavour
        self.chaiBase = base

class MaslaChai(BaseChai):
    def __init__(self, flavour, base="Milk"):
        super().__init__(flavour, base)

class GingerChai(BaseChai):
    def __init__(self, flavour, base="Milk"):
        super().__init__(flavour, base)

class ChaiOrder:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def order_summary(self):
        print(f"Order summary: {self.item.chaiFlavor}: {self.quantity} with base {self.item.chaiBase}")


first_order = ChaiOrder(MaslaChai("Masala Chai"), 2)
first_order.order_summary()
second_order = ChaiOrder(GingerChai("Ginger Chai", "Water"), 3)
second_order.order_summary()