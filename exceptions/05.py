try:
    file = open("order.txt1", "r")

    print("Reading order...")
    content = file.read()
    print("Order content:", content)
except Exception as e:
    error_type = type(e).__name__
    print(f"The error type is: {error_type}")
    print(f"The error message is: {e}")
finally:
    if 'file' in locals():
        print("Closing the file.")
        file.close()