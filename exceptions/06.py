with open("order.txt1", "r") as file:
    try:
        print("Reading order...")
        content = file.read()
        print("Order content:", content)
    except Exception as e:
        error_type = type(e).__name__
        print(f"The error type is: {error_type}")
        print(f"The error message is: {e}")