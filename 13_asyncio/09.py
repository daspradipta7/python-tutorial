import threading

stock = 0

def chai_stock():
    global stock
    for _ in range(1000000):
        stock += 1

threads = [threading.Thread(target=chai_stock) for _ in range(2)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print("Chai stock: ", stock)