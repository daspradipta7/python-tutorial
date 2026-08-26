#create list
myList = ["apple", "banana", "cherry"]
print(f"List the fruits: {myList}")

#duplicates
myList = ["apple", "banana", "cherry", "cherry"]
print(f"Duplicate List the fruits: {myList}")

# length of the list
print(f"Length of the list {len(myList)}")

# list with strings, integers and boolean values:
list1 = ["Apple", 1, True, False]
print(f"List1: {list1}")

# access data using index
list1 = ["Tiger", "Zebra", "Lion", "Chiken"]
print(f"Second animal: {list1[1]}")
print(f"animal: {list1[::2]}")

# check item exist in list
print(f"Check if Tiger present: {'Tiger' in list1}")

# add a item in lis
list1[1] = "Deer"
print(f"updated list: {list1}")

# add range of animals
fruitList = ["apple", "banana", "cherry"]
fruitList[1:3] = ["orange", "kiwi"]
print(f"Added range of fruits: {fruitList}")

# insert items
newFruitList = ["apple", "banana", "cherry"]
newFruitList.insert(1, "kiwi")
print(f"New fruit list: {newFruitList}")

#append in list
thisList = ["apple", "banana", "cherry"]
thisList.append("kiwi")

# extend list
list1 = ["apple", "banana", "cherry"]
list2 = ["kiwi", "pineapple", "papaya"]
list1.extend(list2)
print(f"Extended list: {list1}")

# extend the tupple with list
list1 = ["apple", "banana", "cherry"]
list2 = ("kiwi", "pineapple", "papaya")
list1.extend(list2)
print(f"Etended tupplelist: {list1}")

# remove specific fruit
list1 = ["apple", "banana", "cherry"]
list1.remove("apple")

print(f"Removesd list {list1}")

# remove fromspecific index
list1 = ["apple", "cherry"]
popped = list1.pop(1)
print(f"Removed index 1 {list1}, popped: {popped}")


#remove the last index
list1 = ["apple", "cherry"]
popped = list1.pop()
print(f"Removed index 1 {list1}, popped: {popped}")

# delete entries
list1 = ["apple", "cherry"]
del list1[1]
print(f"Removed index 1 {list1}")

# clear the list

list1 = ["apple", "cherry"]
list1.clear()
print(f"Clear list1 {list1}")


#loop through the list
for fruit in fruitList:
    print(fruit)

[print(x) for x in fruitList]

#filter the list to return the fruit which contains 'a' letter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

filteredList = [x for x in fruits if "a" in x]
print(f"filtered list: {filteredList}")

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(f"new list: {newlist}")