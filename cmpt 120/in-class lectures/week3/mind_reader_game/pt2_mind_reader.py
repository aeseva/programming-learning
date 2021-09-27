# greet user

print("\nWElcome to the mind reader game!")
print("\nVersion 1 - one word only for player 1")
print()         # just for space

# first version - HARD CODED word "nature"
theWord = 'nature'

# 1st player is given THE word
# then is asked to provide 3 words they associate with it.
print("PLAYER 1 - What do you associate with the word", theWord)

word1 = input("first association --> ")
word2 = input("second association --> ")
word3 = input("third association --> ")

# 'clean' the screen (simulated with text interface)
print("\n*5")   # cleaning the screen

# 2nd player must then try to guess at least one of the words
print("PLAYER 2 - What do you associate with the word", theWord)

wordP2 = input("your association --> ")

lstP1words = [word1, word2, word3]

# if it's a match, the 2nd player wins
if wordP2 in lstP1words:
    print("Yay, you won!")
else:
    print("Next time!")

# end program
print("The game ended")