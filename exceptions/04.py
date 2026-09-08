file = open("order.txt", "w")

try:
    print("Placing order...")
    file.write("Order placed successfully.")
except Exception as e:
    error_type = type(e).__name__
    print(f"The error type is: {error_type}")
    print(f"The error message is: {e}")
finally:
    if 'file' in locals():
        print("Closing the file.")
        file.close()