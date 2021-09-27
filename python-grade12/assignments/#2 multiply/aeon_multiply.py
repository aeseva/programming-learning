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
