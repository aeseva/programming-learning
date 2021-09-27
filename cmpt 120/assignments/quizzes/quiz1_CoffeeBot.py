creamResponse = input("Would you like cream, dear User? ==> ").lower().strip("!.")

if creamResponse == "yes":
    print("Here you go, my friend! :D")
elif creamResponse == "no":
    print("Of course, no cream for a good friend like you! :D")
else:
    print("I'm sorry, I don't understand what you mean. Would you like cream, dear User?")
