import datetime
# Variables

name = "Ali"
age = 34
print(name)
print(age)

name = "hussein"
print(name)

isActive = True
print(isActive)

# Receiving input from the user

# firstname = input("Enter your firstname: ")
# lastname = input("Enter your lastname: ")
# print("Your firstname is " + firstname + " and lastname is " + lastname)

# Type conversion

# num1 = input("Enter a number: ")
# num2 = input("Enter a second number: ")
# sum = int(num1) + int(num2)
# print(sum)

gu = input("War gu'gee dhalatay: ")
currentDate = datetime.datetime.now()
age = currentDate.year - int(gu)

print(f'Waxaad jirtaa {age}  sano')
print("Waxaad jirtaa " + str(age) +  "sano")