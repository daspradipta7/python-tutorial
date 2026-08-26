#sort the list asc
list1 = [10, 9, 4, 5]
list1.sort()
print(f"Asc: {list1}")
list1.sort(reverse=True)
print(f"Desc {list1}")

#copy list
list1 = [10, 9, 4, 5]
list2 = list(list1)
print(f"List1 copy to list 2: {list2}")
list2 = list1.copy()
print(f"List1 copy to list 2 method 2 : {list2}")

# copy using slice operator
thislist = ["apple", "banana", "cherry"]
list2 = thislist[:]
print(f"List1 copy to list 2 method 3 : {list2}")
