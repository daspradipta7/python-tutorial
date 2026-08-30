def infinite_chai_1():
    count = 1

    while True:
        print(f"{count}")
        count += 1

        if count == 3: break

infinite_chai_1()

def infinite_chai():
    count = 1

    while True:
        yield f"Cup {count}"
        count += 1

cup = infinite_chai()

for _ in range(5):
    print(next(cup))