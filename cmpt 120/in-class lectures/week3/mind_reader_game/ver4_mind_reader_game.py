# Mind Reader Game (Ver 4)

import random

listPossible = ("nature", "games", "flower", "horse")

# FOR repeating a SPECIFIC number of times.

for i in range(3): #<=== HARDCODING number of times to repeat

	# # # Establish it restarting to a NEW GAME # # #
    print("\n=== NEW GAME: different, random word!\n")
    print("Game Number ", i + 1)
	
    theWord = random.choice(listPossible)
        
    print("PLAYER 1 - What do you associate with the word, '", theWord, "'?")
        
    word1_P1 = input("1st association --> ")
    word2_P1 = input("2st association --> ")
    word3_P1 = input("3st association --> ")
        
    # # #
    print("\n")
    # # #

    # # # Player 2 # # #

    print("PLAYER 2 - What do you associate with the word", theWord, "?")

    word_P2 = input("Your association --> ")

    listP1words = (word1_P1, word2_P1, word3_P1)

    # # # GOAL: Winning/Losing # # #

    if word_P2 in listP1words:
        print("Yay, you win!")
    else:
        print("Try again, next time!")
	
