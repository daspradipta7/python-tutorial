class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    pass

menu = { "dosa": 50, "Idli": 30, "Vada": 20, "Pongal": 40 }

meal = input("Enter our meal preference: ")
try:
    if meal not in menu:
        raise InvalidInputError(f"{meal} is not available in the menu.")
    isValidMenu = menu[meal]
except InvalidInputError as e:
    error_type = type(e).__name__
    print(f"The error type is: {error_type}")
    print(f"The error message is: {e}")