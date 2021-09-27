poss_positive_user_words = ["great", "good", "awesome"]
poss_negative_user_words = ["great", "good", "awesome"]

feel = input("How are you feeling? ==> ").lower().strip("!.")

if feel in poss_positive_user_words:
    print("That's great to hear!")
elif feel in poss_negative_user_words:
    print("That's too bad!")
