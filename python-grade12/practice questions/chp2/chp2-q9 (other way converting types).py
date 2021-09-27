totalMinutes = 270
numMinutes = totalMinutes % 60
numHours = (totalMinutes - numMinutes) / 60

#LONG WAY
#convert integers to strings
totalMinutes_string = str(totalMinutes)
numMinutes_string = str(numMinutes)
numHours_string = str(numHours)

#concatenate strings
phrase = totalMinutes_string + " is " + numHours_string + " hours and " + numMinutes_string + " minutes."

print(phrase)

#OR SHORTER WAY
print(str(totalMinutes) + " is " + str(numHours) + " hours and " + str(numMinutes) + " minutes.")