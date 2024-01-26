names = ['ahmed', 'abdi', 'ali', 'yussuf', 'ali']

# Looping the array
for name in names:
    print(name)

# first element
print(names[0])

# Last element
print(names[-1])

# Length of the list/array
print(len(names)) 

# List methods
# append() - adds an element to the list at the end
names.append("mohamed")
print(names)

# clear() - clears the list
# names.clear()
# print(names)

# count() - it returns the number of times an element appears in the list
print(names.count("ali"))

# insert - it adds an element to list at a specified index
names.insert(2, "amina")
print(names)

# index - returns the first occurence of the element
print(names.index("ali"))

# pop - removes an element a specified position/index
names.pop(3)
print(names)

# remove - removes the item with the specified value
names.remove("yussuf")
print(names)

# reverse - it reverses the order of the list
names.reverse()
print(names)

# sort - sorts the list
names.sort()
print(names)