import random
# I don't know if pre-defining things up here is strictly necessary
# But it wasn't working before
verblist = []
v = ''

# Read in the verbs
with open('alphaverbs.csv') as f:
    v = f.read()

# Turns one giant string into a list of strings at linebreaks
verblist = v.splitlines()

# Now we're making a list of lists
splitverbs = []
for verbs in verblist:
    splitverbs.append(verbs.split(','))


# Multiple modes, let's start with translation or conjugation

modeChoice = ''

forms =  ['je ', 'tu ', 'il/elle ', 'nous ', 'vous ', 'ils/elles ']

print('Type "done" to exit')
print('How would you like to practice?')
modeChoice =input('Choose translation (t) or conjugation (c) > ')

translationChoices = ['t', 'T', 'translation', 'Translation']
conjugationChoices = ['c', 'C', 'conjugation', 'Conjugation']

def drill(prompt, form):
    guess = input(prompt)
    if guess == 'done':
        print('Ciao!')
        quit()
    if guess == splitverbs[i][form]:
        print('Nickel!')
        return True
    else:
        print('Nope, sorry')
        return False

if modeChoice in translationChoices:
    while True:
        i = random.randint(1,len(splitverbs))
        print(splitverbs[i][1])
        drill('What French word is this? ', 0)

if modeChoice in conjugationChoices:
    i = random.randint(1,len(splitverbs))
    print(splitverbs[i][0], splitverbs[i][1])
    number_correct = 0
    column = 2
    for form in forms:
        if drill(form, column):
            number_correct = number_correct + 1
        column = column + 1
    print('You got', number_correct, 'correct answers.')
    
    print('je         ', splitverbs[i][2])
    print('tu         ', splitverbs[i][3])
    print('il/elle    ', splitverbs[i][4])
    print('nous       ', splitverbs[i][5])
    print('vous       ', splitverbs[i][6])
    print('ils/elles  ', splitverbs[i][7])

else:
    print('Not sure what you want there, buddy.')

