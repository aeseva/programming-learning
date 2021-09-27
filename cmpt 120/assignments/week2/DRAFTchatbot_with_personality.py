# CMPT 120 (D200)
# chatbot with personality
# Author: Aeon Seva
# Date: Sept 21, 2021
import random

# Asking User's Name & Pronouns
userName = input("Hello! What is your name, my dear friend? ==> ")
userPronouns = input("And what are your pronouns, if you don't mind me asking? — Feel free to leave the space blank if you don't want to share. :) ==> ").strip(" ")

# Confirming Pronouns AND Responding Accordingly
if userPronouns == "":
    print()
else:
    confirm_userPronouns = input("Just to make sure, your pronouns are " + userPronouns + ". Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")
    if confirm_userPronouns == "yes":
        print()
    while confirm_userPronouns == "no":
        userPronouns = input("Could you repeat your pronouns to me, again? ==> ")
        confirm_userPronouns = input("Just to make sure, your pronouns are '" + userPronouns + "'. Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")

# Confirming Name AND Responding Accordingly

confirm_userName = input("So, your name is " + userName + ". Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")

if confirm_userName == "yes":
    response_userName = [userName + ", that's a very lovely name. :)", userName + ", what a wonderful name! :D", userName + ", you have a name I like very much! :D", userName + "... a name that sounds just as great as the person. :)"]
    rndmResponse_userName = random.choice(response_userName)

    print(rndmResponse_userName)
elif confirm_userName == "no":
    while confirm_userName == "no":
        userName = input("Could you repeat your name to me, again? ==> ")
        confirm_userName = input("So, your name is " + userName + ". Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")
    
    response_userName = [userName + ", that's a very lovely name. :)", userName + ", what a wonderful name! :D", userName + ", you have a name I like very much! :D", userName + "... a name that sounds just as great as the person. :)"]
    rndmResponse_userName = random.choice(response_userName)

    print(rndmResponse_userName)

else:
    confirm_userName = input("Sorry, I didn't catch that. Server overload, please try again. ")

# Confirming Pronouns

# OVERALL GOAL: 

#EXTRA: use the turtle like a loading screen

# USER'S NAME & PRONOUNS
# ask for the user's name
# provide 3-5 options (different elements, index of 3-5) for the robot to randomly choose from with the response of: liking user's name

# ask for user's pronouns

# clarify if user's name & pronouns are correct
# Greet the user with their name.

# "I haven't introduced myself. My name is Ferne and I'll be the being you'll be chatting with today. I'm here to 

# at least 3 questions to the user
# at least 1 of each of if statement varients:
    # if(with no else), if/else, & if/elif/else
# use answer (input) from user
