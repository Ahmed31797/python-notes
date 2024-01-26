import math
# Built-in functions
# min
numbers = [4,5,6,1]
print(min(numbers))

# max
print(max(numbers))

# abs
num = -90
print(abs(num))

# pow
print(pow(2,8))
print(pow(3,3))

# Math module
# ceil
n = 6.2
print(math.ceil(n))

# floor
x = 9.9
print(math.floor(x))

# fsum
print(math.fsum(numbers))

# sqrt
print(math.sqrt(100))
print(math.sqrt(81))

# pi
pi = math.pi
print(pi)

# area of a circle
# area = pi * r * r
radius = int(input("Enter radius: "))
area = math.pi * radius*radius
print(f'Area {area:.2f}')