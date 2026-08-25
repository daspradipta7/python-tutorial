thistuple = ("apple", "banana", "cherry")

# loop using for loop
for x in thistuple:
    print(x)

#loop using indexing
for i in range(len(thistuple)):
    print(f"{i}: {thistuple[i]}")

#loop using while loop
i = 0

while i < len(thistuple):
    print(f"{i} index: {thistuple[i]}")
    i += 1

#Join two tuples:
tuple1 = ("one", "two")
tuple2 = ("three", "four")
tuple3 = tuple1 + tuple2
print(f"Tuple3: {tuple3}")

# multiply tuple
tuple4 = tuple1 * 3
print(f"tuple4: {tuple4}")

#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 5, 8, 7, 5, 4, 6, 8, 5)
number_of_5 = thistuple.count(5)
print(f"Number of 5: {number_of_5}")

#Search for the first occurrence of the value 8, and return its position:
index_of_8 = thistuple.index(8)
print(f"index of 8: {index_of_8}")
