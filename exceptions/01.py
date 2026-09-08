menu = { "dosa": 50, "Idli": 30, "Vada": 20, "Pongal": 40 }
isValidMenu = False

try:
    meal = input("Enter our meal preference: ")
    isValidMenu = menu[meal]
except Exception as e:
    error_type = type(e).__name__
    print(f"The error type is: {error_type}")
    print(f"The error message is: {e}")

print("Is Valid Menu: ", isValidMenu)