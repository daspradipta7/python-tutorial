menu = ["Green Tea", "Lemon Tea", "Milk Tea"]

for item in enumerate(menu, 1):
    print(f"{item[0]}: {item[1]}")

# use ZIP
price = [10, 20, 30]

for item, price in zip(menu, price):
    print(f"{item}: {price}")