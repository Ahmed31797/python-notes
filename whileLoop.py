num = 10
while num < 15:
    print(num)
    num = num + 1


# break - terminates the loop
num = 1
while num < 5:
    if num == 3:
        break
    print(num)
    num = num + 1


# continue - skips where the condition is true and moves to the next one
num = 1
while num < 5:
    num = num + 1
    if num == 3:
        continue
    print(f"Num  {num}")

# else - what to do at the end of the loop
num = 10
while num < 15:
    print(num)
    num = num + 1
else:
    print("End of the loop")
