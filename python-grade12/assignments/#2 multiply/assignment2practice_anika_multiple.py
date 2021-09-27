#START OF DESCRIPTION
#Assignment #2: Write a program to help out a little kid who is trying to remember their times tables.  The program should allow the user to request multiplication practice for a specific multiplier, or else allow for 'random' practice for multipliers within a specified range.  The program should have the user make a guess of the correct answer and then tell them if they got it right or wrong.  To generate random numbers within a certain range, use the following technique: 

#import random
# this is a random number generator module)

#multiplier = random.randint(lower_limit_integer, upper_limit_integer)
# this line loads the variable multiplier with a random number that is between and inclusive of the numbers that are represented by the variables between the brackets. 

#For this program, I'm not expecting that the user can play multiple times; there is a separate technique I will show you that will help with that.  Name the file using the naming convention as follows: {your first name}_multiply.py, and attach it to a reply post to this message.
#END OF DESCRIPTION

#Establishing Randomized Numbers for Multiplier & Multiplicand
lower_limit_integer = 0
upper_limit_integer = 12

import random
multiplier_int = random.randint(lower_limit_integer, upper_limit_integer)

multiplicand_int = random.randint(lower_limit_integer, upper_limit_integer)

#Solving Randomized Multiplier & Multiplicand to an Integer
answer_int = multiplier_int * multiplicand_int

#Converting Each Integer to Strings
multiplier_str = str(multiplier_int)
multiplicand_str = str(multiplicand_int)
answer_str = str(answer_int)

#Concatenating Strings to Display Multiplier & Multiplicand & Asking for User's Answer
user_answer_input = input('What is ' + multiplier_str + ' * ' + multiplicand_str + '?: ')

#Displaying actual answer for user to check their answer
print('The answer is: ' + answer_str)