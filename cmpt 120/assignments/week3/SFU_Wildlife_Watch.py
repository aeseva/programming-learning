# SFU_Wildlife_Watch.py
# Class: CMPT 120 (D200)
# Author: Aeon Seva
# Date: Sept 28th, 2021

# chatbot survival rpg
# EACH ROUND: 
    # 1) PLAYER chooses location on SFU Campus ("AQ" or "ASB")
    # 2) COMPUTER generates random CREATURE (bear, coyote, friend, prof) @ RANDOMLY CHOSEN location by computer
    # 3.1) PLAYER and CREATURE in *same location* = INTERACTION (player chooses "greet" or "avoid")
    # 3.2) PLAYER and CREATURE in *different location* = "No Interaction for Now" is displayed

# RULES FOR SURVIVING:
    # if meet coyote/bear = PLAYER *survives* if "avoid"
    # if meet friend = PLAYER *survives* if "greet"
    # if meet professor = PLAYER survives if "greet" or "avoid"

# REQUIREMENTS:
    # 1) Accept both UPPER- & LOWER-CASE INPUT from user
        # & IGNORE BLANK SPACE
    # 2) Let user play exactly 3 ROUNDS.
    # 3) Use in KEYWORD & for LOOP with range FUNCTION to achieve 3 rounds.
    # 4) Use lists to store possible creatures & locations in game.
    # 5) Use random.choice function from random module to randomly generate creatures & locations
    # 6) Use nested conditional (if/elif/else) at least once for game logic.
    # 7) Include header for name & date

import random

intro = "Welcome to: \n SFU Wildlife Watch \nA survival RPG to specifically bully the first years into leaving SFU \n f o r e v e r. \nIf you can survive for 3 rounds, you win and get to stay at SFU throughout your 2nd year, that is, until the next Wildlife Watch gets you... \n muahahahahhaa... \n nyehehehehhehe. \n*ahem* Now, onto the game!"
print(intro)

# # # SPACE # # #
print("\n")
# # #       # # #

# EACH ROUND: 
    # 1) PLAYER chooses location on SFU Campus ("AQ" or "ASB")

playerLocation = input("Where would you like to go? \n(Choose and enter either 'AQ' or 'ASB') \n>>> ")

    # 2) COMPUTER (CPU) generates random CREATURE (bear, coyote, friend, professor) @ RANDOMLY CHOSEN location by computer

lst_cpuCreature = ["bear", "coyote", "friend", "professor"]
lst_cpuLocation = ["AQ", "ASB"]

cpuCreature = random.choice(lst_cpuCreature)
cpuLocation = random.choice(lst_cpuLocation)

    # 3.1) INTERACTION: PLAYER and CREATURE in *same location* = player presses "ENTER" for action to be randomly chosen (not by player) w/ options: "greet" or "avoid"
lst_playerAction = ["greet", "avoid"]
playerAction = random.choice(lst_playerAction)

if cpuLocation == playerLocation:
    print("A wild", cpuCreature, "appears!")

    input("What will you do? \n(Press 'enter' to continue...)")

        # RULES FOR SURVIVING:
        # if meet coyote/bear = PLAYER *survives* if "avoid"
    if (cpuCreature == "coyote") or (cpuCreature == "bear"):
        if playerAction == "greet":
            print("YOU LOSE. The", cpuCreature, "used Tackle, then ate your innerds.")
        elif playerAction == "avoid":
            print("")
        # if meet friend = PLAYER *survives* if "greet"
        # if meet professor = PLAYER survives if "greet" or "avoid"



    # 3.2) NO INTERACTION: PLAYER and CREATURE in *different location* = "No Interaction for Now" is displayed
else:
    print("No Interaction, for Now...")
