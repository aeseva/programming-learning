#Activity 6.1.2 - Updating Variables
x = 0
x = x + 1
print(x)

#Activity 6.2.1 - "while" Statement
#TRANSLATION: “While n is greater than 0, display the value of n and then reduce the value of n by 1. When you get to 0, exit the while statement and display the word Blastoff!"
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

#6.3 - Infinite Loop
#due to it INCREMENTING forever
n = 5
while n > 0:
    print(n)
    n = n + 1
print('Blastoff!')

#OR

#due to it DECREMENTING forever
n = 5
while n < 0:
    print(n)
    n = n - 1
print('Blastoff!')

#OR

#due to the condition being True
#(DON'T RUN THESE INFINITE LOOPS UNLESS U KNOW HOW TO GET OUT OF THEM)
n = 10
while True:
    print(n, end=' ')
    n = n - 1   
print('Done!')

#6.3 - "break" = GETTING OUT of Infinite Loops
while True:
    line = input('Word: ')
    if line == 'done':
        break
    print(line)
print('Done!')

#6.4 - "continue" = SKIPPING/ENDING Iterations

# hashtag # = don't print this (like commenting lines out)
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done':
        break
    else:
        print(line)
print ('Done!')

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done':
        break
    else:
        print(line)
print ('Done!')

n = 0
while (n < 10):
    n = n + 1
    if n == 8:
        continue
    print(n)

# Activity 6.5.3 - "for" loop
#Translation: "Run the statements in the body of the for loop once for each 'friend' in the set named 'friends'."
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

names = ['Prisha', 'Kahlil', 'Nirav', 'Aliyah', 'Antonella']
for name in names:
    print("Hello,", name)
print("All done!")

# Activity 6.6.2.1
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

# Activity 6.6.2.3
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

#Actiity 6.6.2.4
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

nums = [1,2,3,4,5]
print(min(nums))

# 6.9 - Multiple Choice Questions

#Activity 6.9.7 - How many asterisks will be printed when the following code executes?
for x in [0, 1, 2, 3]:
    for y in [0, 1, 2, 3, 4]:
        print('*')

# 6.10 - Mixed Up Code Questions

#The following program segment should calculate and print the average of a list of numbers using a for loop.
numbers = [90, 94, 85, 78, 87, 98]
sum = 0
for number in numbers:
    sum = sum + number
print(sum/6)

#The following program segment should calculate the sum of all odd numbers between 0 and 30.
sum = 0
numbers = range(1, 30, 2)
for number in numbers:
    sum = sum + number
print(sum)

#The following program should find the sum of every multiple of 3 between 3 and 36 and print the sum after each addition.
sum = 0
numbers = range(3, 37, 3)
for number in numbers:
    sum = sum + number
    print(sum)

#The following program should find the average pH of 6 water samples.
total = 0
pHValues = [7.0, 8.2, 6.7, 7.5, 8.0, 7.2]
for number in pHValues:
    total = total + number
average = total / 6
print(average)

#The following program should print the numbers 5 through 1, starting with 5.
counter = 5
while counter > 0:
    counter = counter - 1
print(counter)

# 6.11 - Write Code Questions

#Activity 6.11.4
#Make 5 changes to the code below to correctly print a count up from -10 to 0, including 0.

output = ""
x = -11
while x < 0:
    x = x + 1
    output = output + str(x) + " "
print(output)

#Activity 6.11.7
#Complete the code on lines 4 and 6 so that it prints the number 6.

x = 3
i = 0
while i < 3:
    x = x + 1
    i = i + 1
print(x)

#Activity 6.11.10
#changing for-loop to while-loop
#for-loop
def sumFunc(start, stop):
    sum = 0
    for num in range(start, stop + 1):
        sum = sum + num
    return sum

print(sumFunc(1,10))

#while-loop
def sumFunc(start, stop):
    sum = 0
    num = start
    while num <= stop:
        sum = sum + num
        num += 1
    return sum

print(sumFunc(1, 10))

#Activity 6.11.13 - combining for-loop AND while-loop
#for-loop
for x in range(1, 4):
    for y in range(1, 4):
        print(str(x) + " * " + str(y) + " = " + str(x * y))

#while-loop
x = 1
y = 1
while x < 3:
    while y < 3:
        y = y + 1
        x = x + 1
    print(str(x) + " * " + str(y) + " = " + str(x * y))

#for-loop AND while-loop
for x in range(1, 4):
    y = 1
    while y < 4:
        print(str(x) + " * " + str(y) + " = " + str(x * y))
        y = y + 1

#Activity 6.11.15
#for-loop
product = 1  # Start out with nothing
numbers = range(1,11)
for number in numbers:
    product = product * number
print(product)

#while-loop
#DON'T RUN THIS THIS IS WRONG IT ENDS UP AS AN INFINITE LOOP
product = 1
number = 1
while number < 10:
    while product < 10:
        product = product * number
print(product)
number = number + 1

#6.12.1 "for" Statements

#"set" within for-loop
print("hello")
for x in [2, 7, 1]:
    print("the number is", x)
print("goodbye")

#"variable" within for-loop instead of "set")

#strings
#iterates over each character ins tring
#length of string determines how many times body of loop will run
for c in "Hi!":
    print(c)

#6.12.2 - "range" Function
#wanting to print letters A to Z, using a loop

for i in range(65, 91):
    print(chr(i))

#6.12.3 - "while" Function
#Activity 6.12.3.5
#If deleted line 4, 0 would print INFINITELY

i = 0
while i < 3:
    print(i)
    i = i + 2
print("goodbye")

# TWO ways to do this
#1 - function
def add(n):
    i = 0
    total = 0
    while i < n:
        total = total + int(input('Enter a value:'))
        i = i + 1
    print(total)

add(5)

#2 - initializing
n = 5
i = 0
total = 0
while i < n:
    total = total + int(input('Enter a value:'))
    i = i + 1
print(total)
