import threading
import time

def prepared_chai(type_,  wait_time):
    print(f"{type_} chai brewing...")
    time.sleep(wait_time)
    print(f"{type_} is ready.")


t1 = threading.Thread(target=prepared_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepared_chai, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()
