names = ["abdi", "ali", "yussuf", "ibrahim", "jaamac", "yussuf"]

# first element
print(names[0])

# last element
print(names[-1])

# len of the list
print(len(names))

# LIST METHODS
# append
names.append("xaliima")
print(names)

# clear
# names.clear()
# print(names)

# count
print(names.count("yussuf"))

# insert
names.insert(1, "yasmiin")
print(names)

# index
print(names.index("yussuf"))

# pop
names.pop(3)
print(names)

# remove
names.remove("ali")
print(names)

# reverse
names.reverse()
print(names)

# sort
names.sort()
print(names)