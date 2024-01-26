""" 
Function
_________
A function is a block of organized, reusable code that is used to perform a single, related action.
Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) )
Any input parameters or arguments should be placed within these parentheses.
The code block within every function starts with a colon (:) and is indented. 

"""

# ex1
def my_function():
    print("Samaha Technologies")

my_function()

""" 
Arguments
__________
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
Arguments are often shortened to args in Python documentations.
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective: A parameter is the variable listed inside the parentheses in the function definition while an argument is the value that is 
sent to the function when it is called. 

"""
def greetings(firstname):
    print("Hello " + firstname)

greetings("Mohamed")
greetings("Ali")
greetings("Amina")

""" 
Arbitrary Arguments, *args
___________________________
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:

 """

def fav_languages(*languages):
    print("My favorite language is " + languages[1])

fav_languages("Javascript", "Python", "Php", 'Swift')


""" 
Keyword Arguments
_________________
You can also send arguments with the key = value syntax.
The phrase Keyword Arguments are often shortened to kwargs.
"""
def programming(frontend, backend, mobile):
    print("I like " + backend + " development.")

programming(frontend = "Javascript", backend = "Python", mobile = "Swift")

""" 
Arbitrary Keyword Arguments, **kwargs
_____________________________________
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
# """
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His height is " + kid["height"])

my_function(fname = "Tobias", lname = "Refsnes", height = '2.5ft')

def programming2(**progs):
    print("I like " + progs['frontend'] + " development.")

programming2(frontend = "Javascript", backend = "Python", mobile = "Swift")


# Passing a List as an Argument
def fav_fruits(fruit):
  for x in fruit:
    print(x + " is one of my favorite fruits." )

fruits = ["apple", "banana", "cherry"]
fav_fruits(fruits)

# Return statement
# ex 1
def my_function(x):                                                
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# ex 2
def net_salary(salary, nhif, nssf, meetings, meetingAllowance):
  allowance = meetings * meetingAllowance
  tax = 2.5/100 * salary
  net_pay = salary - nhif - nssf - tax + allowance
  return net_pay

print(net_salary(50000,300,400,5,2000))
print(net_salary(30000,300,400,7,1000))



