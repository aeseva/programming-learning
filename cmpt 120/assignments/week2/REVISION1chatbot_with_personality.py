# CMPT 120 (D200)
# chatbot with personality
# Author: Aeon Seva
# Date: Sept 21, 2021
import random

# Asking User's Name & Pronouns
userName = input("Hello! What is your name, my dear friend? ==> ")
userPronouns = input("And what are your pronouns, if you don't mind me asking? — Feel free to leave the space blank if you don't want to share. :) ==> ").strip(" ")

# Confirming Pronouns
# (moving on if response is "yes" and looping confirmation if response is "no")
if userPronouns == "":
    print()
else:
    confirm_userPronouns = input("Just to make sure, your pronouns are '" + userPronouns + "'. Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")
    if confirm_userPronouns == "yes":
        print()
    while confirm_userPronouns == "no":
        userPronouns = input("Could you repeat your pronouns to me, again? ==> ")
        confirm_userPronouns = input("Just to make sure, your pronouns are, '" + userPronouns + "'. Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")

# Confirming Name AND Responding Accordingly
# (moving on if response is "yes" and looping confirmation if response is "no")
confirm_userName = input("So, your name is, '" + userName + "'. Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")

if confirm_userName == "yes":
    response_userName = [userName + ", that's a very lovely name. :)", userName + ", what a wonderful name! :D", userName + ", you have a name I like very much! :D", userName + "... a name that sounds just as great as the person. :)"]
    rndmResponse_userName = random.choice(response_userName)

    print(rndmResponse_userName)

elif confirm_userName == "no":
    while confirm_userName == "no":
        userName = input("Could you repeat your name to me, again? ==> ")
        confirm_userName = input("So, your name is " + userName + ". Is this correct? (Type in 'yes' or 'no' to confirm) ==> ").lower().strip("!.?")

        if confirm_userName == "yes":
            response_userName = [userName + ", that's a very lovely name. :)", userName + ", what a wonderful name! :D", userName + ", you have a name I like very much! :D", userName + "... a name that sounds just as great as the person. :)"]
            rndmResponse_userName = random.choice(response_userName)
            
            print(rndmResponse_userName)
        
        elif confirm_userName == "no":
            print()
        
        else:
            print()

else:
    confirm_userName = input("Sorry, I didn't catch that. Server overload, please try again. ")

# notes: (suggestions, noting mistakes, noting wrongs)
# 1) i don't have an "else" within the block of "else" in the Confirming Pronouns section. so, if someone mistyped something, it would go straight to the Confirming Name section.
# 2) i could have done the "print(rndmResponse_userName)" at the end of the "if/elif/else" statements and that would have reduced the clutter.
# 3) LMAO, i realized i fixed my 1) suggestion in the confirming username section. oh well, i was rushing, so it was a time