mytuple = ("one", "two", "three", "four")

print(mytuple)

(one, *two) = mytuple
print(f"one {one}, two {two}")

#access tuple using indexing
print(f"First index {mytuple[0]}")

# acces last index
print(f"Last index {mytuple[-1]}")

# range of index
print(f"Rang of index {mytuple[0:2]}")

#length of the tuple
print(f"Length of the tuple {len(mytuple)}")

# check item eist in tuple
if "two" in mytuple:
    print("Yes two present")
elif "three" in mytuple:
    print("Yes three present")
else:
    print("Default")

# add tuple path 1
updatedTuple = ("five",)
updatedTuple += mytuple
print(f"New updated tuple: {updatedTuple}")

# add tuple path 2
listtuple = list(mytuple)
listtuple.append("six")
listtuple = tuple(listtuple)
print(f"List tuple: {listtuple}")

# update a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "pineapple"
x = tuple(y)
print(f"Update the eiting tuple path 1: {x}")

# remove from tuple
x = ("lion", "zebra", "tiger")
y = list(x)
y.remove("tiger")
x = tuple(y)
print(f"Animal: {x}")

# delete the tuple
animal = ("lion", "zebra", "tiger")
del animal
#print(animal)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(apple, *mango) = fruits

print(f"apple: {apple}, mango: {mango}, type_of_mango: {type(mango)}")