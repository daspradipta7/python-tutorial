import threading
import time

def monitor_water_temp():
    while True:
        print("Water tempreture is being monitored")
        time.sleep(1)

threading.Thread(target=monitor_water_temp).start()

print("Main program is done")