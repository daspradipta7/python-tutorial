from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing {name} chai...")
    time.sleep(3)
    print(f"End of brewing {name}")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i + 1}",))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    for p in chai_makers:
        p.join()

    print("All chai served")
