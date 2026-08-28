order_amount = int(input("Provide order amount: "))

isDelivery = True if order_amount > 350 else False

if isDelivery:
    print("Delivery is free")
else:
    print("Please pay 10Rs")