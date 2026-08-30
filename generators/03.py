def chai_cutomer():
    print("Welcome to the Chai shop!!!")

    order = yield

    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_cutomer()
next(stall)

stall.send("Kadak Chai")
stall.send("Elachi Chai")