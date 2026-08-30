def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
    yield "Cup 4"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))
#print(next(chai)) #will givw error

