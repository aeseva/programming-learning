# Aeon S
# Sept 9th, 2021

name_inp = input("What is your name? ")
name_len = len(name_inp)

if name_len >= 5 and name_len <= 10:
    print(name_inp + ", why let things stress us when in the end, we're all gonna die someday anyway?")
elif name_len <= 5:
    print("Dear " + name_inp + ", Today is going to be a good day. And here's why: because today, today at least you're you and that's enough.​ (From, Dear Evan Hansen)")
else:
    print("reject humanity return to monke")
