# if/else expressions

x = 3

if x % 2 == 0:
    print('x is EVEN')
else:
    print('x is ODD')

# if/elif/else expressions

x = 12
y = 12.0

if x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')
else:
    print('x and y are the same')

# i dont understand this lmao (and why it prints D when the score is 93???? x suddenly being 93 makes it D????)

x = 93
score = 93

if score >= 90:
    grade = "A"
if score >= 80:
    grade = "B"
if score >= 70:
    grade = "C"
if score >= 60:
    grade = "D"
if score < 60:
    grade = "E"
print(grade)

# activity 4.13.4

#1 - my work
hours = 45
rate = 10
overtimeRate = 1.5 * rate
#grossPay = 0 (why do i need this???)

if hours <= 40:
    grossPay = hours * rate
else:
    overtime = hours - 40
    grossPay = (overtime * overtimeRate) + (40 * rate)
print(grossPay)

#2 - their work
# Initializing variables
hours = 45
rate = 10
# overtimeRate is 1.5 the rate amount
overtimeRate = rate * 1.5
grossPay = 0
# Begin conditional to see if hours are within regular pay
if hours <= 40:
    #if within 40 hours, pay will be hours * rate
    grossPay = hours * rate
# Else statement for when hours are greater than 40
else:
    # Create variable for overtime hours
    overTime = hours % 40
    # Pay will equal the regular rate for 40 hours,
    # plus the overtime rate for the extra hours
    grossPay = (rate * 40) + (overTime * overtimeRate)
# Print the final pay
print(grossPay)

#QuESTIONS:
# -how does the modulus operator work in this case???? how would it work?? does the remainder work the same way as subtraction???

# ~Activity 4.13.9~

#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
    # Score   Grade
    #>= 0.9     A
    #>= 0.8     B
    #>= 0.7     C
    #>= 0.6     D
    # < 0.6     F

    #Enter score: 0.95
    #A

score = 0.95

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score < 0.6:
    grade = 'F'
print(grade)

# ~Activity 4.13.12~

#Write a procedure that takes 2 ints, total price, and amount in wallet. Print “You have enough money” if the difference between the wallet and price is 0 or greater; otherwise, print “Get more money”.

price_str = input('What is the total price?')
wallet_str = input('How much do you have in your wallet?')

price_int = int(price_str)
wallet_int = int(wallet_str)

difference = (wallet_int - price_int)

if difference >= 0:
    print('You have enough money')
else:
    print('Get more money')

# ~Acticity 4.13.13~

#3 criteria must be taken into account to identify leap years:
    #The year is evenly divisible by 4;
    #If the year can be evenly divided by 100, it is NOT a leap year, unless;
    #The year is also evenly divisible by 400. Then it is a leap year.
#Write a program that takes a year as a parameter and sets leapYear equal to True if the year is a leap year, False otherwise. (use a few different years to test your work)

year_str = input('Enter the year to determine if it is a Leap Year or not.')
year_int = int(year_str)

if year_int % 4 == 0 or year_int % 400 == 0:
    leapYear = True
elif year_int % 100 == 0:
    leapYear = False
else:
    leapYear = False
print(leapYear)