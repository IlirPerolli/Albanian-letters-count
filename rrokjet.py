input = input('Ju lutem shenoni fjalen: ')
fjala = ''
for i in input:
    fjala += i
    if i == 'a':
        fjala +="-"
    elif i == 'e':
        fjala +="-"
    elif i == 'ë':
        fjala +="-"
    elif i == 'i':
        fjala +="-"
    elif i == 'o':
        fjala +="-"
    elif i == 'u':
        fjala +="-"
    elif i == 'y':
        fjala +="-"

if (fjala[-1] == '-'):
    print (fjala[0:len(fjala)-1])
