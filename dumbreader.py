verbs = []
verbstring = ''
with open('frenchverbs.csv') as f:
    verbstring=f.read()
#    for line in f:
        
#        verbs.append(line)

verblines = []
verblines = verbstring.splitlines()
verblines.sort()
#print(verblines)

with open('alphaverbs.csv','w') as alpha:
    for line in verblines:
        alpha.write(line + '\n')

