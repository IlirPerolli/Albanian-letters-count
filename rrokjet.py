input = input('Ju lutem shenoni fjalen: ')
fjala = ''
zanoret = ['a','e','ë','i', 'o', 'u','y']
for i in input:
    fjala += i
    for j in zanoret:
        if (i == j):
            fjala +="-"
            break

if (fjala[-1] == '-'):
    print (fjala[0:len(fjala)-1])
