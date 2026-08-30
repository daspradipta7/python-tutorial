def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elachi Chai"


def inte_chai():
    yield "Matcha"
    yield "Oolang"


def todays_menu():
    yield from local_chai()
    yield from inte_chai()

for chai in todays_menu():
    print(chai)