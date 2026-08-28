device_status = "active"
temp = 35

if device_status == "active":
    if temp > 35:
        print("Hot tempreture")
    else:
        print("Cool Tempreture")
else:
    print("Device is offline")