import random
num = random.randint(1,10)
your_name = input("What is your name? ")
print(your_name + ", I have a number between 1 and 10")
number_of_tries = 0
while number_of_tries < 5:
    guess = int(input("Guess the number: "))
    number_of_tries +=1
    if guess < num:
        print("Your guess is lower than the number")
    if guess > num:
        print("Your guess is higher than he number")
    if guess == num:
        break

if guess == num:
    print("You guessed the number in " + str(number_of_tries) + " tries")
else:
    print("Sorry, " + your_name + " time is up. Number was " + str(num))
