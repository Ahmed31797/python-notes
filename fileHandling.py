import os
# how to open/read an existing file
# opening file in the current directory
file = open('samaha.txt')
print(file.read())

for student in file:
  print(student)

# opening file in a different directory
file2 = open('C:/Users/Ahmed/Desktop/samaha.txt')
myNewFile = open('student.txt', 'w')
print(file2.read())

# how to create a new file
myNewFile = open('students.txt', 'w')
myNewFile.write("Samaha Students \n")
myNewFile.write("Mohamed \n")
myNewFile.write("Nasteexo \n")
myNewFile.write("Lawrence \n")
myNewFile.close()

st = open('students.txt')
print(st.read())


# how to write to a file
myNewFile = open('students.txt', 'w')
myNewFile.write("University students\n")
myNewFile.close()

st = open('students.txt')
print(st.read())

# how to append to a file
myNewFile = open('students.txt', 'a')
myNewFile.write("College students\n")
myNewFile.close()

st = open('students.txt')
print(st.read())

# how to delete as file
# To delete a file, import os

# exclusive  creation error create file if dones not exist else raise error
# myTest = open('myTest.txt', 'x')
os.remove('mytest.txt')