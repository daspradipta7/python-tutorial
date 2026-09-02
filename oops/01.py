class FirstClass:
    name = "FirstClass"

firstObject = FirstClass()
secondObject = FirstClass()

secondObject.name = "Changed Name"
secondObject.gender = "Female"


print(firstObject)
print(secondObject)

#delete the name attribute from secondObject
del secondObject.name
del secondObject.gender

print(firstObject)
print(secondObject)