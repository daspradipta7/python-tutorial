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