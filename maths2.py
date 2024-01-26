import math

# in-built functions
marks = [90,67,89,58,70] 
# min
print(min(marks))

# max
print(max(marks))

# abs
x = -67
print(abs(x))

# pow
print(pow(2,8))

# Functions imported from math libray
# ceil
y = 5.2
print(math.ceil(y))

# floor
j = 5.9
print(math.floor(j))

# fsum
total = math.fsum(marks)
print(total)

# sqrt
print(math.sqrt(625))

# pi
# area of a circle = pi*r*r
radius = float(input("Enter radius of the circle: "))
# area = math.pi * radius * radius
area = math.pi * pow(radius, 2)
print(f'{area:.2f}')