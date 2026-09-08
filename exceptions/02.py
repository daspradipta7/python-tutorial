menu = { "dosa": 50, "Idli": 30, "Vada": 20, "Pongal": 40 }

try:
    meal = input("Enter our meal preference: ")
    if meal not in menu:
        raise KeyError(f"{meal} is not available in the menu.")

except Exception as e:
    error_type = type(e).__name__
    print(f"The error type is: {error_type}")
    print(f"The error message is: {e}")

else:
    isValidMenu = menu[meal]
    print("Is Valid Menu: ", isValidMenu)
finally:
    print("Execution completed.")