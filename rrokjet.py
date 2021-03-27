input = input('Ju lutem shenoni fjalen: ')
fjala = ''
for i in input:
    fjala += i
    if i == 'a':
        fjala +="-"
    if i == 'e':
        fjala +="-"
    if i == 'ë':
        fjala +="-"
    if i == 'i':
        fjala +="-"
    if i == 'o':
        fjala +="-"
    if i == 'u':
        fjala +="-"
    if i == 'y':
        fjala +="-"

if (fjala[-1] == '-'):
    print (fjala[0:len(fjala)-1])
