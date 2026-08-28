# Take input from user
avaiable_snacks = ["cookies", "samosa"]
snack_asked = input("Enter your order: ").lower()

if snack_asked in avaiable_snacks:
    print(f"Your Order for {snack_asked} confirmed !!!")
else:
    print(f"{snack_asked} is not currently available !!!")