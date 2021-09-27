# ~ Chapter 2: Question 5 (See Question 9 for other way of Converting)~
#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off. Using the int() function and modulus operator could come in handy!

#Asking user for values (automatically become strings)
current_time_string = input('What is you current time (24 hour time)?')
waiting_time_string = input('How many hours until we screech at you, milady?')

#Converting strings to integers to evaluate
current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

#Evaluating Time of Alarm
time = (current_time_int + waiting_time_int) % 24

#Showing Calculated Time of Alarm
print(time)