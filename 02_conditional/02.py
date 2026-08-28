items = {
    "small": 10,
    "medium": 15,
    "Large": 20
}

input_item = input("Please share preference: ").lower()

if input_item in items:
    print(f"Your order is confirmed for {input_item.capitalize()}")
else:
    print(f"Unknown selection {input_item}")