def changeCase(func):
    def innerFunc():
        return func().upper()
    return innerFunc

@changeCase
def myfunction():
    return "Hello World"

print(myfunction())