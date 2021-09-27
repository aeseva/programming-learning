#
def printFlavours():
    print('Vanilla')
    print('Chocolate')
    print('Strawberry')
def printProducts():
    print('Ice Cream')
    print('Milkshake')
    print('Frozen Yogurt')
    print('**********')
    print('Flavors:')
    printFlavours()
printProducts()

# ~5.15 Mixed-up Code Questions (Drag & Drop)

#
def caught_speeding(speed, is_birthday):
    if is_birthday is True:
        if speed <= 65:
            return "no ticket"
        elif speed <= 85:
            return "minor ticket"
        else:
            return "major ticket"
    else:
        if speed <= 60:
            return "no ticket"
        elif speed <= 80:
            return "minor ticket"
        else:
            return "major ticket"

#Create a check_guess function which computes if a guess is too low, too high, or correct. Return 'too low' if guess is less than target, 'correct' if they are equal, and 'too high' if guess is greater than target. For example, check_guess(5, 7) returns 'too low', check_guess(7, 7) returns 'correct', and check_guess(9, 7) returns 'too high'. Note: there are three extra code blocks, and watch your indentation!
def check_guess(guess, target):
    if guess < target:
        return 'too low'
    elif guess == target:
        return 'correct'
    else:
        return 'too high'
x = check_guess(5, 7)
print(x)

#Create a check_guess function which computes if a guess is too low, too high, or correct. Return 'too low' if guess is less than target, 'correct' if they are equal, and 'too high' if guess is greater than target. For example, check_guess(5, 7) returns 'too low', check_guess(7, 7) returns 'correct', and check_guess(9, 7) returns 'too high'. Note: there are three extra code blocks, and watch your indentation!
def check_guess(guess, target):
    if guess < target:
        return 'too low'
    elif guess == target:
        return 'correct'
    else:
        return 'too high'
x = check_guess(5, 7)
print(x)

# Put the code blocks below in order to solve the following problem. Given a day of the week encoded as 0 = Sun, 1 = Mon, 2 = Tue, …6 = Sat, and a boolean indicating if we are on vacation, return a string indicating when the alarm clock should ring. If we are on vacation and it is a weekend (0 = Saturday or 6 = Sunday), it should return "off", and otherwise return "10:00". If we are not on vacation and it is a weekend, it should return "10:00", and otherwise return "7:00". Note: there are two extra code blocks, and watch your indentation!
def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        else:
            return "7:00"
a = alarm_clock(6, False)
print(a)

#The following code should create two functions. First create a function called square_it which squares the parameter n and returns the result. Then, create a function called cube_it which cubes the parameter n and returns the result. Finally, ask the user to input a number and print out the user’s input squared and then cubed. Watch out for extra code blocks and indentation! Note: there are four extra code blocks, and watch your indentation!
def square_it(n):
    return n ** 2

def cube_it(n):
    return n ** 3

userNumInput = int(input('Please enter a number: '))

print(square_it(userNumInput))
print(cube_it(userNumInput))

# OR

square_ans = square_it(userNumInput)
cube_ans = cube_it(userNumInput)

print(square_ans)
print(cube_ans)

#i have no idea what this was (i wouldn't have figured it out myself without the drag&drop boxes):

#The following code creates three functions that use Python’s math module to calculate geometric equations. First, create a function called distance which finds and returns the distance between two coordinates using the distance formula: d = √((x_2 - x_1)² + (y_2 - y_1)²). Then, create a function called area which returns the area of a circle given its radius using the formula: A = πr². Finally, create a function called area2 which uses the distance function to find the radius and the area function to find the circle’s area. Watch your indentation!

import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = math.pow(dx, 2) + math.pow(dy, 2)
    result = math.sqrt(dsquared)
    return result
    
def area(radius):
    b = math.pi * math.pow(radius, 2)
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result2 = area(radius)
    return result2

distance_ans = distance(2, 5, 1, 9)
area_ans = area(4)
area2_ans = area2(4, 5, 1, 5)

print(distance_ans)
print(area_ans)
print(area2_ans)

# ~

#
def tripCost(miles, milesPerGallon, pricePerGallon):
    numGallons = miles / milesPerGallon
    total = numGallons * pricePerGallon
    return total

print(tripCost(500, 26, 3.45))

#
def computegrade(score):
    if score < 1:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return 'Bad score'

print(computegrade(2))

#
import math

def areaOfCircle(r):
    area = math.pi * r**2
    return area

print(areaOfCircle(2))

#Activity 5.16.15 (DON'T KNOW HOW TO DO)
#Finish the function to return the average of three numbers, but drop the lowest value. For example, get_avg_drop_lowest(100, 10, 0) returns 55 and get_avg_drop_lowest(4, 3, 10) returns 7.

def get_avg_drop_lowest(num1, num2, num3):
    lowest = min(num1, num2, num3)
    avg = ((num1 + num2 + num3) - lowest) / 3
    return avg

print(get_avg_drop_lowest(100, 10, 0))

#Activity 5.16.16
#You are driving a little too fast, and a police officer stops you. Write code to compute the kind of ticke you’ll receive, encoded as an int value: 0 = no ticket, 1 = small ticket, and 2 = big ticket. If speed is 60 or less, return 0. If speed is between 61 and 80 inclusive, return 1. If speed is 81 or more, return 2. If it is your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed <= 85:
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed <= 80:
            return 1
        else:
            return 2

#
def birthday(month, day, year):
    month = input('Enter the month (MM)')
    day = input('Enter the day (DD)')
    year = input('Enter the year (YYYY)')
    date = month + '/' + day + '/' + year
    return date
print(birthday(0, 0, 0))

#
def num_to_strings_weekdays_and_weekends(num):
    if (num >= 1) and (num <= 5):
        if num == 1:
            return "This is a weekday, and it's Monday."
        elif num == 2:
            return "This is a weekday, and it's Tuesday."
        elif num == 3:
            return "This is a weekday, and it's Wednesday."
        elif num == 4:
            return "This is a weekday, and it's Thursday."
        else:
            return "This is a weekday, and it's Friday."
    elif (num > 5) and (num <= 7):
        if num == 6:
            return "It is the weekend, and it's Saturday."
        else:
            return "It is the weekend, and it's Sunday."
    else:
        return "The number does not correspond to a day of the week."

#Activity 5.24.1

def get_letter_grade(percentage):
    if percentage > 100:
        return "You can't get over 100."
    elif percentage <= 100:
        if percentage >= 90 :
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "E"

#
def even_or_odd(num):
    if num % 2 == 1:
        return 'This is odd.'
    else:
        return 'This is even.'

#
def which_quadrant(x, y):
    if (x != 0) and (y != 0):
        if (x > 0) and (y > 0):
            return "Quadrant 1"
        elif (x < 0) and (y > 0):
            return "Quadrant 2"
        elif (x < 0) and (y < 0):
            return "Quadrant 3"
        else:
            return "Quadrant 4"
    else:
        return "It's not in a quadrant."

#
def which_axis_or_is_origin(x, y):
    if (x != 0) and (y != 0):
        return "This coordinate is not on an axis. It's in a quadrant."
    elif (x == 0) and (y == 0):
        return "This coordinate is the origin."
    elif (x == 0):
        return "This coordinate is on the y-axis."
    else:
        return "This coordinate is on the x-axis."

#
def bonus(years, quality):
    if years > 5:
        return "Eligible for Bonus"
    elif quality > 90:
        return "Eligible for Bonus"
    elif (years >= 3) and (quality > 80):
        return "Eligible for Bonus"
    else:
        return "Ineligible for Bonus"

#Activity 5.26.5
#Create a function called move_elevator to move elevator from one floor to another. The method takes two parameters current_floor and nex_floor. If the elevator moves to a floor above then it should return “Up”, otherwise it should return “Down”. Also if the next_floor is negative or if it is the same as current_floor it should return 0.
def move_elevator(current_floor, next_floor):
    if next_floor > 0:
        if current_floor < next_floor:
            return "Up"
        elif current_floor == next_floor:
            return 0
        else:
            return "Down"
    else:
        return 0

#OR - actual answer provided \/

def move_elevator(current_floor, next_floor):
    if next_floor < 0:
        return 0
    elif  next_floor < current_floor:
        return "Down"
    elif next_floor > current_floor:
        return "Up"
    else:
        return 0

#
def lunch_break(class_standing):
    if class_standing == 'Freshman':
        return 40
    elif class_standing == "Sophomore":
        return 30
    elif class_standing == "Junior":
        return 20
    elif class_standing == "Senior":
        return 15
    else:
        return 0

#Activity 5.26.9 (donut know what im doin lmao)
def pay_rent(units):
    units = 0
    if units < 200:
        return 100
    elif units < 500:
        return 200
    elif units > 500:
        extraUnit = units - 500
        return (200 + (0.1 * extraUnit))

#
def play_weather(weather):
    if (weather == "sunny") or (weather == "cloudy"):
        return "The person should play"
    elif (weather == "rainy") or (weather == "windy") or (weather == "snowy"):
        return "Person should not play"
    elif (weather == "storm"):
        return "Not safe to go outside"

#Activity 5.28.1
#Create a function called average_of_num_list that takes in a parameter num_list and returns the average of all the numbers in num_list.
def average_of_num_list(num_list):
    return sum(num_list) / len(num_list)

#Activity 5.28.3
#Create a function called names that takes in a parameter name_list and returns an alphabetically sorted name_list.
def names(name_list):
    name_list.sort()
    return name_list

#Activity 5.28.5
#Create a function called remove_min_value that takes in a parameter num_list and returns a num_list without the minimum value from num_list.
def remove_min_value(num_list):
    num_list.remove(min(num_list))
    return num_list

#Activity 5.28.7
#Create a function called range_given_list that takes in a parameter list_of_nums and returns the range (max value - min value) of the values. Try using the sort method and indexing.
def range_given_list(list_of_nums):
    list_of_nums.sort()
    range_value = list_of_nums[-1] - list_of_nums[0]
    #OR range_value = list_of_nums[len(list_of_nums) - 1] - list_of_nums[0]
    return range_value

#Activity 5.28.10
#Create a function called remove_indices_after_first_max_value that takes in a parameter num_list and returns a new_num_list with values up to the max value of the list. For example, given a num_list = [5, 10, 5, 200, 15, 20, 200, 15], the function would return [5, 10, 5, 200].
def remove_indices_after_first_max_value(num_list):
    index_value = num_list.index(max(num_list)) + 1
    new_num_list = num_list[:index_value]
    return new_num_list

#Activity 5.28.11
#Given these two lists: [5, 20, 3, 15, 200, 0, 17] and [‘Hello’, ‘Bye’, ‘How are you?’], how would you would transform them into [‘Bye’, ‘Hello’, ‘How are you?’, 0, 200, 15, 3, 20, 5]? Hint: Use list methods (e.g., pop, sort, append, reverse, and extend).
def transformed_and_combined_list(list_one, list_two):
    #removes 17 from list_one
    list_one.pop(-1)
    #removes 0 from list_one and assigns it to a variable
    returned_value = list_one.pop(-1)
    #sorts list_two alphabetically
    list_two.sort()
    #adds popped and saved value to list_two
    list_two.append(returned_value)
    #reverses the order of list_one
    list_one.reverse()
    #adds contents of list_one to the end of list_two
    list_two.extend(list_one)
    return list_two