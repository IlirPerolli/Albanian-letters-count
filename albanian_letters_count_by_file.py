from matplotlib import pyplot as plt
import itertools
from collections import Counter
letters = {'a':0,'b':0,'c':0,'ç':0,'d':0,'dh':0,'e':0,'ë':0,'f':0,'g':0,'gj':0,'h':0,'i':0,'j':0,'k':0,'l':0,'ll':0,'m':0,
           'n':0,'nj':0,'o':0,'p':0,'q':0,'r':0,'rr':0,'s':0,'sh':0,'t':0,'th':0,'u':0,'v':0,'x':0,'xh':0,'y':0,'z':0,'zh':0, '.':0, ',':0, '?':0, '!':0}
zanoret = ['a','e','ë','i','o', 'u', 'y']
bigramet = ['dh','gj','ll','nj','rr', 'sh', 'th', 'xh', 'zh']
file = open("article.txt", "r", encoding='utf8')
input = file.read().lower()
file.close()
file = open('output.txt', 'w+')
file.write('')
file.close()
fjalet_input = input.split()
fjalet = Counter(fjalet_input) #numero fjalet
counter_to_dictionary = dict(fjalet) #kthe ne dictionary
fjalet_me_te_perseritura =dict(sorted(counter_to_dictionary.items(), key=lambda item: item[1],reverse=True)) #order DESC
fjalet_me_te_perseritura = dict(itertools.islice(fjalet_me_te_perseritura.items(), 15)) #merr 15 elementet e para
print ('\nFjala me e shpeshte eshte: ' +str(list(fjalet_me_te_perseritura)[0]) + " -> "+ str(fjalet_me_te_perseritura[list(fjalet_me_te_perseritura)[0]])+ ' here')
file = open('output.txt', 'a+')
file.write('Fjala me e shpeshte eshte: ' +str(list(fjalet_me_te_perseritura)[0]) + " -> "+ str(fjalet_me_te_perseritura[list(fjalet_me_te_perseritura)[0]])+ ' here. \n \n')
file.close()
print(" ")
for i in letters:
    if (i in input):
        if (i =='dh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='gj'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='ll'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='nj'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='rr'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='sh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='th'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='xh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        elif (i =='zh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        letters[i]= input.count(i)

print ('Shkronjat e perseritura: \n')
file = open('output.txt', 'a+', encoding='utf8')
file.write('Shkronjat e perseritura: \n')
for i in letters:
    print(str(i) +' -> '+ str(letters[i]))
    file.write(str(i) +' -> '+ str(letters[i]) + '\n')
file.close()
print("")
sorted_letters = (dict(sorted(letters.items(), key=lambda item: item[1],reverse=True)))
sorted_letters = dict(itertools.islice(sorted_letters.items(), 15)) #merr 15 elementet e para

most_common_letter = list(sorted_letters)
print('Shkronja me e shpeshte eshte: ' + str(most_common_letter[0]) + " -> "+ str(letters[most_common_letter[0]]) + " here. \n ")
file = open('output.txt', 'a+', encoding='utf8')
file.write('\nShkronja me e shpeshte eshte: ' + str(most_common_letter[0]) + " -> "+ str(letters[most_common_letter[0]]) + " here. \n")
file.close()

file = open('output.txt', 'a+', encoding='utf8')
print ('Perseritja e zanoreve:')
file.write('\nPerseritja e zanoreve: \n')

for i in zanoret:
    print (str(i) + ' -> ' + str(letters[i]))
    file.write(str(i) + ' -> ' + str(letters[i]) + "\n")
    file.write('')
print ('')
file.close()

file = open('output.txt', 'a+', encoding='utf8')
print ('Perseritja e bigrameve:')
file.write('\nPerseritja e bigrameve: \n')

for i in bigramet:
    print (str(i) + ' -> ' + str(letters[i]))
    file.write(str(i) + ' -> ' + str(letters[i]) + "\n")
    file.write('')
print ('')
file.close()

plot1 = plt.figure(1)


plt.bar(sorted_letters.keys(), sorted_letters.values(), color='#117892')
plt.title("Shkronjat më të shpeshta")
plt.ylabel("Numri i përseritjeve")
plt.xlabel("Shkronjat")

zanoret_e_perseritura = {i:j for i , j in zip(zanoret, [letters[i] for i in zanoret])}
zanoret_e_sortuara = (dict(sorted(zanoret_e_perseritura.items(), key=lambda item: item[1],reverse=True)))
zanoret_e_sortuara = dict(itertools.islice(zanoret_e_sortuara.items(), 15)) #merr 15 elementet e para

# print (zanoret_e_sortuara)
plot2 = plt.figure(2)
plt.plot(zanoret_e_sortuara.keys(),zanoret_e_sortuara.values(), color='#117892' ,marker='o')
plt.title("Perseritja e zanoreve")
plt.ylabel("Numri i përseritjeve")
plt.xlabel("Shkronjat")
plt.show()

