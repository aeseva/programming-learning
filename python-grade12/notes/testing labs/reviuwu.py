# OVERALL:
#   Direct Print
#   Variable Print

# ~Variables~

#1 - string

# class
print(type('Hello'))

print('hello')

a = 'hello'
print(a)

#2 - integer

# class
print(type(5))

print(5)

a = 5
print(a)

#3 - float

# class
print(type(4.5))

print(4.5)

a = 4.5
print(a)

#4 - boolean


# ~Concatenation~

# direct print
a = 'world'
b = 'to work'
c = 'not to feel.'

print('Hello, ' + a + '. Programmed ' + b + ' and ' + c)

# variable print
a = 'world'
b = 'to work'
c = 'not to feel.'
abc = 'Hello, ' + a + '. Programmed ' + b + ' and ' + c

print(abc)

# ~Input~

ownerName = input('Hello there! What is your name?: ')
ownerPronouns = input('What are your pronouns?: ')
ownerTipsFedora = input('And are you a milady or a mitheydy? (note: milady stands for both men and women): ')

robotPronouns = 'they/them'
favFlavour = 'vanilla'

print('Hello, ' + ownerName + '. My name is robottit and my pronouns are: ' + robotPronouns + '. I am here to provide any assistance you may need. A fun fact about me: my favourite flavour is ' + favFlavour + '. I will be ready when you give the command, ' + ownerTipsFedora + '. *tips fedora*')