menu = [
    "Cutting Chai",
    "Lemon Chai",
    "Special Chai",
    "Black Coffee",
    "Coffe",
    "Chocolate Coffee"
]

list_tea = [tea for tea in menu if "Chai" in tea]

list_coffee = [coffee for coffee in menu if "Coffee" in coffee]

print(f"Chai: {list_tea}")
print(f"list_coffee: {list_coffee}")


