import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 required lock a")
        with lock_b:
            print("Task 1 required lock b")

def task2():
    with lock_b:
        print("Task 2 required lock b")
        with lock_a:
            print("Task 2 required lock a")


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()


