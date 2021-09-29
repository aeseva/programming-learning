# iNITIALIZE Accumulators
blen = 0
rena = 0 
star = 0
times = 0

# FOR each person

for person in range(10):

	print("Interviewing Person" + str(person + 1))     #<== OR print("………", person)
	
	# 1) Ask Preference (i.e. vote)
	vote = input(" preference? (B/R/S/T) ==> ").upper().strip("!. ")
	
	# check which accumulator applies (IF's!)
	# accumulate in the adequate accumulator
	
	if (vote == "B"):
		blen = blen + 1
	elif (vote == "R"):
		rena += 1     #<== abbreviation for rena = rena + 1
	elif (vote == "S"):
		star += 1
	elif (vote == "T"):
		times += 1
	else:
		print("You lose your vote… I don't understand.")

# Show Totals to user after For loop is over
print("totals…")
print("blenz", blen, "renaissance", rena, "starbucks", star, "tims", tims)