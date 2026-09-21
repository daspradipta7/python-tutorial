import threading
import time

def boil_milk():
    print("Boiling Milk...")
    time.sleep(2)
    print("Milk Boiled...")

def toast_bun():
    print("Toasting Bun")
    time.sleep(3)
    print("Toasted bun")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t2.join()
t2.join()

end = time.time()

print(f"breakfast is ready in {end - start:.2f} seconds")