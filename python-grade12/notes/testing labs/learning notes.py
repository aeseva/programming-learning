# ~ Booleans (bool)~

# Comparisons:
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object Identity:      is

#1 - true VS false
if True:
    print('Conditional was True')
# VS
if False:
    print('Conditional was True')

#2 - if/elif/else
language = 'C#'

if language == 'Python':
    print('Language is Python')
elif language == 'C#':
    print('Language is C#')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

#3 - logical operators

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')