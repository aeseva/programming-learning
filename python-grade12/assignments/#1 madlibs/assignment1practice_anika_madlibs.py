#Assignment #1: I'm sure you have heard of madlibs before.  Write a program that will get inputs from the user to load named variables, then concatenate (combine) the variables together to make a goofy sentence.  The sentence should have user provided inputs for at least 2 nouns, 2 adjectives, 1 verb and 1 adverb (you could include more....just to show off.    Name the file using the naming convention as follows: {your first name}_madlib.py, and attach it to a reply post to this message.

#A 'lil added intro to the madlibs
intro = "Welcome to your Wasteland Madlibs! \nA nuclear war between nations wiped out the whole country. Thankfully, you and other residents fled to fallout shelters deep underground right before the bombs rained down. Living your whole life in a fallout shelter, you were curious about the life of wasteland dwellers. That was when a group of 6 people decided to take their chances on living on the surface. You are one of these 6 people. How will you survive in this post-apocalyptic world?\n"
print(intro)

#Asking for input from user
noun_1 = input("Type in a noun (plural):")
noun_2 = input("Type in another noun:")
adjective_1 = input("Type in an adjective:")
adjective_2 = input("Type in another adjective:")
verb_1 = input("Type in a verb:")
adverb_1 = input("Type in an adverb:")

#Concatenating input strings into madlibs
output = 'As soon as you left your fallout shelter, 6 mutated ' + noun_1 + ' attack the group. One of the mutated ' + noun_1 + ' pins you down, knocking you in and out of consciousness. Without knowing what is by your side, you grab a ' + noun_2 + ' and chuck it at one of the ' + noun_1 + '. From the impact, its ' + adjective_1 + ' guts spew out, successfully killing it. ' + 'The others seemed to have killed the rest of them, as you were busy dealing with your own mate. One person out of the group of 6 died, leaving 3 ' + adjective_2 + ' people and 2 frightened wusses left to survive. You all carry along, and ' + verb_1 + ' as you walk through the dead valleys, in such a ' + adverb_1 + ' manner. What will the fallout dwellers do next in their journey through the wasteland?'
print(output)