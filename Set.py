# set does not allow duplicate values

languages = {'html', 'java', 'python'}
# remove - removes the specified value from the set
languages.remove('java')
print(languages)

# pop - removes the first element in the set
languages.pop()
print(languages)

# difference - retuns elements found in the first set and not in the second set
x = {"apple", "banana", "cherry", "facebook"}
y = {"google", "microsoft", "apple", "facebook"}
z = x.difference(y) 
print(z)

#  symmetric_difference() - returns a set that contains all items from both sets, but not the items that are present in both sets
m = {"apple", "banana", "cherry"}
n = {"google", "microsoft", "apple"}
k = m.symmetric_difference(n)
print(k)

# union - returns a set that contains all items from both sets, where an element exists in both sets, it will only appear once in the new set
z=m.union(n)
print(z)








